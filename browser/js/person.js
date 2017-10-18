TKPerson = {};
TKPerson.map = '';
TKPerson.cmarker = '';
TKPerson.markers = new Array();

TKPerson.init = function() {
    // Set up foldables

    var showText = '&nbsp;Show &raquo;';
    var hideText = '&nbsp;&laquo; Hide';

    var fsets = $ES('fieldset.foldable');
    fsets.each(function(fs) {
	var exlink = $(document.createElement('a'));
	exlink.setStyle('cursor', 'pointer');
	if (!fs.hasClass('default_open')) {
	    fs.addClass('closed');
	    exlink.setHTML(showText);
	}
	else {
	    exlink.setHTML(hideText);
	}
	exlink.onclick = function() { return false; };
	exlink.addEvent('click', function() {
	    fs.toggleClass('closed');
	    if (!fs.hasClass('closed')) {
		exlink.setHTML(hideText);
	    }
	    else {
		exlink.setHTML(showText);
	    }
	});
	exlink.injectInside($E('legend', fs));
    });

    var moreText = 'Show more &raquo;';
    var lessText = '&laquo; Show fewer';
    var limit = 3;

    // Set up preview lists
    var plists = $ES('ul.preview');
    plists.each(function(plist) {
	var offspring = $ES('li', plist);
	if (offspring.length <= limit) {
	    return;
	}

	plists.addClass('closed');
	var opener = $(document.createElement('a'));
	opener.setStyle('cursor', 'pointer');
	opener.setHTML(moreText);
	opener.onclick = function() { return false; };
	opener.addEvent('click', function() {
	    plist.toggleClass('closed');
	    if (plist.hasClass('closed')) {
		opener.setHTML(moreText);
	    } else {
		opener.setHTML(lessText);
	    }
	});
	
	for (var i=limit; i<offspring.length; i++) {
	    offspring[i].addClass('extra');
	}
	var holder = $(document.createElement('li'));
	holder.setStyle('height', 'auto');
	holder.setStyle('width', 'auto');
	holder.appendChild(opener);
	plist.appendChild(holder);
    });

    // Maps stuff

    var maplinks = $ES('a.maplink');
    maplinks.each(function(maplink) {
	var coords = $E('input.geolocation', maplink).value.split(',');
	var pos = new google.maps.LatLng(coords[0], coords[1]);
	var title = $E('input.title', maplink).value;
	var mtype = $E('input.markertype', maplink).value;
	var icon = new GIcon(G_DEFAULT_ICON);
	icon.image = mtype;

	var mymarker = new GMarker(pos, icon);
	mymarker.bindInfoWindowHtml(title);
	TKPerson.markers.push(mymarker);

	maplink.onclick = function() { return false; };
	maplink.addEvent('click', function() {
	    if (!TKPerson.map) {
		TKPerson.initMap(maplink.parentNode.parentNode);
	    }
	    $(TKPerson.mapdiv).setStyle('display', 'block');
	    TKPerson.hideAllMapMarkers();
	    
	    if (!TKPerson.cmarker) {
		TKPerson.cmarker = mymarker;
	    } else {
		TKPerson.map.removeOverlay(TKPerson.cmarker);
		TKPerson.cmarker = mymarker;
	    }
	    TKPerson.map.addOverlay(TKPerson.cmarker);
	    TKPerson.map.setCenter(pos);
	    TKPerson.map.setZoom(13);
	});
    });
    if (maplinks.length) {
	alink = $(document.createElement('a'));
	alink.setStyle('cursor', 'pointer');
	alink.setHTML('Show all on map &raquo;');
	alink.onclick = function() { return false; };
	alink.addEvent('click', function(link) {
	    if (!TKPerson.map) {
		TKPerson.initMap(maplinks[0].parentNode.parentNode);
	    }
	    TKPerson.hideAllMapMarkers();
	    TKPerson.resizeToFit(TKPerson.map, TKPerson.markers);
	    for (i=0; i<TKPerson.markers.length; i++) {
		TKPerson.map.addOverlay(TKPerson.markers[i]);
	    }
	    $(TKPerson.mapdiv).setStyle('display', 'block');
	});
	alink.injectBefore(maplinks[0].parentNode.parentNode);
    };
    
    TKPerson.initMap = function(beforeThis) {
	TKPerson.mapdiv = $(document.createElement('div'));
	TKPerson.mapdiv.addClass('address-map');
	TKPerson.mapdiv.setText('Map');
	TKPerson.mapdiv.injectBefore(beforeThis);
	TKPerson.map = new google.maps.Map2(TKPerson.mapdiv);
	TKPerson.map.addControl(new google.maps.MapTypeControl());
	TKPerson.map.addControl(new google.maps.SmallMapControl());
	TKPerson.map.addControl(new TKPerson.HideMapControl());
	TKPerson.map.setCenter(new GLatLng(0, 0), 13);
    }

    TKPerson.hideAllMapMarkers = function() {
	for (i=0; i<TKPerson.markers.length; i++) {
	    TKPerson.map.removeOverlay(TKPerson.markers[i]);
	}
    };

    /* Map hider */
    TKPerson.HideMapControl = function() { };
    TKPerson.HideMapControl.prototype = new google.maps.Control();
    TKPerson.HideMapControl.prototype.initialize = function(map) {
	var container = document.createElement('div');
	var hidebutton = document.createElement('div');
	this.setButtonStyle_(hidebutton);

	container.appendChild(hidebutton);
	hidebutton.appendChild(document.createTextNode('Hide Map'));
	GEvent.addDomListener(hidebutton, "click", function() {
	    $(TKPerson.mapdiv).setStyle('display', 'none');
	});
	map.getContainer().appendChild(container);
	return container;    
    };

    TKPerson.HideMapControl.prototype.getDefaultPosition = function() {
	return new google.maps.ControlPosition(G_ANCHOR_BOTTOM_RIGHT, 
					       new google.maps.Size(7, 20));
    };

    TKPerson.HideMapControl.prototype.setButtonStyle_ = function(button) {
	button.style.textDecoration = "none";
	button.style.color = "#000000";
	button.style.backgroundColor = "white";
	button.style.font = "small Arial";
	button.style.border = "1px solid black";
	button.style.padding = "2px";
	button.style.marginBottom = "3px";
	button.style.textAlign = "center";
	button.style.width = "5em";
	button.style.cursor = "pointer";
    };


};

TKPerson.resizeToFit = function(map, markers) {
    var bounds = new GLatLngBounds();	

    for (var i = 0; i < markers.length; i++) {
	bounds.extend(markers[i].getPoint());
    }
    map.setZoom(map.getBoundsZoomLevel(bounds)-1);
    var clat = (bounds.getNorthEast().lat() + bounds.getSouthWest().lat()) /2;
    var clng = (bounds.getNorthEast().lng() + bounds.getSouthWest().lng()) /2;
    map.setCenter(new GLatLng(clat,clng));
}


google.load("maps", "2.x");
window.addEvent('load', TKPerson.init);

