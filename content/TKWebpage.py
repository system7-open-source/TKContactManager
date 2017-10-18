# -*- coding: utf-8 -*-
#
# File: TKWebpage.py
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
from Products.TKContactManager.interfaces.IContactDetails import IContactDetails
from Products.TKContactManager.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    StringField(
        name='webURL',
        widget=StringWidget(
            label='Webpage URL',
            label_msgid='TKContactManager_label_webURL',
            i18n_domain='TKContactManager',
        ),
        schemata="Internet Contact Details",
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

TKWebpage_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class TKWebpage(BaseContent):
    """This class is responsible for storing URLs to webpages.
       It implements the following interfaces:
       - IContactDetails
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseContent,'__implements__',()),)
    # zope3 interfaces
    zope.interface.implements(IContactDetails)

    # This name appears in the 'add' box
    archetype_name = 'Webpage'

    meta_type = 'TKWebpage'
    portal_type = 'TKWebpage'
    allowed_content_types = []
    filter_content_types = 0
    global_allow = 1
    #content_icon = 'TKWebpage.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "Webpage"
    typeDescMsgId = 'description_edit_tkwebpage'

    _at_rename_after_creation = True

    schema = TKWebpage_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

registerType(TKWebpage, PROJECTNAME)
# end of class TKWebpage

##code-section module-footer #fill in your manual code here
##/code-section module-footer



