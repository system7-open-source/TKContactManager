# -*- coding: utf-8 -*-
#
# File: TKEmailAddress.py
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
from Products.TKContactManager.interfaces.IEmailAddressProvider \
     import IEmailAddressProvider
from Products.TKContactManager.interfaces.IContactDetails \
     import IContactDetails
from Products.TKContactManager.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    StringField(
        name='email',
        widget=StringWidget(
            label='Email',
            label_msgid='TKContactManager_label_email',
            i18n_domain='TKContactManager',
        ),
        schemata="Internet Contact Details",
        label="E-mail address"
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

TKEmailAddress_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class TKEmailAddress(BaseContent):
    """This class is responsible for storing an email address.
       It realises two zope3 interfaces:
       - IEmailAddressProvider
       - IContactDetails
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseContent,'__implements__',()),)
    # zope3 interfaces
    zope.interface.implements(IEmailAddressProvider, IContactDetails)

    # This name appears in the 'add' box
    archetype_name = 'E-mail Address'

    __doc__ = 'E-mail Address'

    meta_type = 'TKEmailAddress'
    portal_type = 'TKEmailAddress'
    allowed_content_types = []
    filter_content_types = 0
    global_allow = 1
    #content_icon = 'TKEmailAddress.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "E-mail Address"
    typeDescMsgId = 'description_edit_tkemailaddress'

    _at_rename_after_creation = True

    schema = TKEmailAddress_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    security.declarePublic('getEmailAddress')
    def getEmailAddress(self):
        """This method implements an operation defined in the
           IEmailAddressProvider interface.
        """
        
        return self.getEmail()

registerType(TKEmailAddress, PROJECTNAME)
# end of class TKEmailAddress

##code-section module-footer #fill in your manual code here
##/code-section module-footer



