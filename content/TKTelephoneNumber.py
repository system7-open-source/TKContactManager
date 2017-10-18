# -*- coding: utf-8 -*-
#
# File: TKTelephoneNumber.py
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

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    ComputedField(
        name='formattedNumber',
        expression="context._computeFormattedNumber()",
        widget=ComputedField._properties['widget'](
            label='Formatted number',
            label_msgid='TKContactManager_label_formattedNumber',
            i18n_domain='TKContactManager',
        ),
        schemata="Telephony",
    ),

    StringField(
        name='countryCode',
        default="44",
        widget=StringWidget(
            description="Please enter a country code (without the preceding " \
                        "'00' or '+'). E.g. 44 for the United Kingdom.",
            label='Country code',
            label_msgid='TKContactManager_label_countryCode',
            description_msgid='TKContactManager_help_countryCode',
            i18n_domain='TKContactManager',
        ),
        required=1,
        schemata="Telephony",
    ),

    StringField(
        name='number',
        validators=('isInternationalPhoneNumber',),
        widget=StringWidget(
            description="Please enter a number (without both a country code " \
            "and a leading zero preceding an area code). E.g. 7724618365",
            label='Number',
            label_msgid='TKContactManager_label_number',
            description_msgid='TKContactManager_help_number',
            i18n_domain='TKContactManager',
        ),
        required=1,
        schemata="Telephony"
    ),

    StringField(
        name='phoneType',
        widget=SelectionWidget(
            label='Type',
            label_msgid='TKContactManager_label_phoneType',
            i18n_domain='TKContactManager',
        ),
        schemata="Telephony",
        vocabulary= ['unknown', 'landline', 'fax', 'mobile' ],
        enforceVocabulary=1,
        default="unknown",
        required=1
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

TKTelephoneNumber_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class TKTelephoneNumber(BaseContent):
    """This class is responsible for storing telephone contact details such as:
       - country code
       - phone number
       - phone type (unknown, landline, fax, mobile)
       
       It is alsa responsible for computing a formatted number (vide a method
       called _computeFormattedNumber).
       
       It realises one interface:
       - IContactDetails
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseContent,'__implements__',()),)
    # zope3 interfaces
    zope.interface.implements(IContactDetails)

    # This name appears in the 'add' box
    archetype_name = 'Telephone Number'

    meta_type = 'TKTelephoneNumber'
    portal_type = 'TKTelephoneNumber'
    allowed_content_types = []
    filter_content_types = 0
    global_allow = 1
    #content_icon = 'TKTelephoneNumber.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "Telephone Number"
    typeDescMsgId = 'description_edit_tktelephonenumber'

    _at_rename_after_creation = True

    schema = TKTelephoneNumber_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    security.declarePrivate('_computeFormattedNumber')
    def _computeFormattedNumber(self):
        """The purpose of this method is to return a full telephone number
           in the following format:
           "+ country_code phone_number"
        """
        
        return "+" + self.getCountryCode() + " " + self.getNumber()

registerType(TKTelephoneNumber, PROJECTNAME)
# end of class TKTelephoneNumber

##code-section module-footer #fill in your manual code here
##/code-section module-footer



