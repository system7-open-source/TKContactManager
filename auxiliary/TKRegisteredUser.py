# -*- coding: utf-8 -*-
#
# File: TKRegisteredUser.py
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
from Products.TKContactManager.interfaces.IUsernameProvider \
     import IUsernameProvider
from Products.TKContactManager.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    StringField(
        name='systemID',
        widget=StringWidget(
            description="Is this person a registered user of this system?" \
                        " If you know their username you can enter it here.",
            label='System ID',
            label_msgid='TKContactManager_label_systemID',
            description_msgid='TKContactManager_help_systemID',
            i18n_domain='TKContactManager',
        ),
        schemata="System Account",
        searchable=1,
	index='FieldIndex',
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

TKRegisteredUser_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class TKRegisteredUser:
    """This class is responsible for storing all the information needed to
       associate an object of the Person class with a system account.
    """
    security = ClassSecurityInfo()
    # zope3 interfaces
    zope.interface.implements(IUsernameProvider)

    # This name appears in the 'add' box
    archetype_name = 'TKRegisteredUser'

    meta_type = 'TKRegisteredUser'
    portal_type = 'TKRegisteredUser'
    allowed_content_types = []
    filter_content_types = 0
    global_allow = 1
    #content_icon = 'TKRegisteredUser.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "TKRegisteredUser"
    typeDescMsgId = 'description_edit_tkregistereduser'

    _at_rename_after_creation = True

    schema = TKRegisteredUser_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    security.declarePublic('getUsername')
    def getUsername(self):
        """An implementation of the getUsername operation of the
           IUsernameProvider interface.
        """
        return self.getSystemID()

# end of class TKRegisteredUser

##code-section module-footer #fill in your manual code here
##/code-section module-footer



