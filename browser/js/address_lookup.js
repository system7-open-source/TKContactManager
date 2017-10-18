TKAddress = {};
TKAddress.wait = function() {
    window.setTimeout(TKAddress.init, 1500);
};

TKAddress.init = function() {
    var holder = document.getElementById('archetypes-fieldname-geolocation');
    if (!holder) {
	return;
    };
    
    var inputs = holder.getElementsByTagName('input');
    if (!inputs.length) {
	return;
    };
    
    TKAddress.sfield = inputs[0];

    TKAddress.street = document.getElementById('street');
    registerEventListener(TKAddress.street, 'blur',
			  TKAddress.updateSearch);

    TKAddress.city = document.getElementById('city');
    registerEventListener(TKAddress.city, 'blur',
			  TKAddress.updateSearch);
    
    TKAddress.postcode = document.getElementById('postcode');
    registerEventListener(TKAddress.postcode, 'blur',
			  TKAddress.updateSearch);
    
    TKAddress.country = document.getElementById('country');
    registerEventListener(TKAddress.country, 'blur',
			  TKAddress.updateSearch);
    
    TKAddress.updateSearch();
};

TKAddress.updateSearch = function() {
    if (TKAddress.street.value) {
	TKAddress.sfield.value = TKAddress.street.value.split('\n').join(', ');
    };
    if (TKAddress.city.value) {
	TKAddress.addSeparator();
	TKAddress.sfield.value += TKAddress.city.value;
    };
    if (TKAddress.postcode.value) {
	TKAddress.addSeparator();
	TKAddress.sfield.value += TKAddress.postcode.value;
    };
    if (TKAddress.country.value) {
	TKAddress.addSeparator();
	TKAddress.sfield.value += TKAddress.country.value;
    };
};

TKAddress.addSeparator = function() {
    end = TKAddress.sfield.value.substr(TKAddress.sfield.value.length - 2);
    if (end != ', ') {
	TKAddress.sfield.value += ', ';
    };
};

registerEventListener(window, 'load', 
		      TKAddress.wait);

