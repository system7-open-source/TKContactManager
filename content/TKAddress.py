
# -*- coding: utf-8 -*-
#
# File: TKAddress.py
#
# Copyright (c) 2007 by Tomasz J. Kotarba
# Generator: ArchGenXML Version 1.5.2
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
# 02110-1301, USA.
#

__author__ = """Tomasz J. Kotarba <tomasz@kotarba.net>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
import zope
from Products.TKContactManager.interfaces.IContactDetails \
    import IContactDetails
from Products.TKContactManager.config import *

# additional imports from tagged value 'import'
from Products.Maps.field import LocationField, LocationWidget

##code-section module-header #fill in your manual code here
from Products.ATCountryWidget.Widget import CountryWidget
from Products.Maps.interfaces import IMap, IMarker, IGeoLocation
from zope.interface import implements
from zope.component import getMultiAdapter

##/code-section module-header

schema = Schema((

        LinesField(
            name='street',
            widget=LinesField._properties['widget'](
                label='Street',
                label_msgid='TKContactManager_label_street',
                i18n_domain='TKContactManager',
                ),
            schemata="Address Details"
            ),

        StringField(
            name='city',
            widget=StringWidget(
                label='City',
                label_msgid='TKContactManager_label_city',
                i18n_domain='TKContactManager',
                ),
            schemata="Address Details"
            ),

        StringField(
            name='postcode',
            widget=StringWidget(
                label='Postcode',
                label_msgid='TKContactManager_label_postcode',
                i18n_domain='TKContactManager',
                ),
            schemata="Address Details"
            ),

        StringField(
            name='country',
            validators=('isValidISOCountry',),
            widget=CountryWidget(
                label='Country',
                label_msgid='TKContactManager_label_country',
                i18n_domain='TKContactManager',
                description='Select a country',
                ),
            schemata="Address Details"
            ),

        LocationField(
            name='geolocation',
            widget=LocationWidget(
                label='Geolocation',
                label_msgid='TKContactManager_label_geoLocation',
                i18n_domain='TKContactManager',
                ),
            label="Geographical location",
            ),
        
        StringField(
            'markerIcon',
            languageIndependent = 1,
            vocabulary="getMarkerIconVocab",
            enforceVocabulary=True,
            widget=SelectionWidget(
                format="select",
                label='Marker icon',
                label_msgid='label_markericon',
                description_msgid='help_markericon',
                i18n_domain='maps',
                ),
            ),
        
        ))

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

TKAddress_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class TKAddress(BaseContent):
    """This class is responsible for storing address details (see its schema).
    It realises one interface:
    - IContactDetails
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseContent,'__implements__',()),)
    # zope3 interfaces
    zope.interface.implements(IContactDetails)

    # This name appears in the 'add' box
    archetype_name = 'Address'

    __doc__ = 'Address'

    meta_type = 'TKAddress'
    portal_type = 'TKAddress'
    allowed_content_types = []
    filter_content_types = 0
    global_allow = 1
    #content_icon = 'TKAddress.gif'
    immediate_view = 'maps_location'
    default_view = 'maps_location'
    suppl_views = ()
    typeDescription = "Address"
    typeDescMsgId = 'description_edit_tkaddress'

    _at_rename_after_creation = True

    schema = TKAddress_schema

    ##code-section class-header #fill in your manual code here
    # Import the extraschema file (defining additional schema for this content
    # class) if it exists. Fail silently.
    from Products.TKContactManager.extraschema import extraschemas
    schema, extraschemata = extraschemas.gen_extraschema(meta_type, schema)

    def getMarkerIconVocab(self):
        config = getMultiAdapter((self, self.REQUEST), 
                                 name="maps_configuration")
        marker_icons = config.marker_icons
        result = DisplayList()
        for icon in marker_icons:
            result.add(icon['name'], icon['name'])
        return result

    def getMarker(self):
        config = getMultiAdapter((self, self.REQUEST), 
                                 name="maps_configuration")
        marker_icons = config.marker_icons
        icon = None
        for mi in marker_icons:
            if mi['name'] == self.getMarkerIcon():
                icon = mi['icon']
        if icon is None:
            icon = marker_icons[0]
        return icon


    def getText(self):
        return "<br />".join([
                '<br />'.join(self.getStreet()),
                self.getCity(),
                self.getPostcode(),
                self.getCountry(),
                ])
    ##/code-section class-header

    # Methods

registerType(TKAddress, PROJECTNAME)
# end of class TKAddress

##code-section module-footer #fill in your manual code here

class GeoLocation(object):
    implements(IGeoLocation)

    def __init__(self, context):
        self.context = context

    @property
    def latitude(self):
        location = self.context.getRawGeoLocation()
        return location[0]

    @property
    def longitude(self):
        location = self.context.getRawGeoLocation()
        return location[1]


class AddressMap(object):
    implements(IMap)

    def __init__(self, context):
        self.context = context

    def getMarkers(self):
        return [IMarker(self.context)]


class AddressMarker(GeoLocation):
    implements(IMarker)

    @property
    def title(self):
        return self.context.Title()

    @property
    def description(self):
        return self.context.Description()

    @property
    def layers(self):
        return self.context.Subject()

    @property
    def icon(self):
        return self.context.getMarkerIcon()

    @property
    def url(self):
        return self.context.absolute_url()


##/code-section module-footer



