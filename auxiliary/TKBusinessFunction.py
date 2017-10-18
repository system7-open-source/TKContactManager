# -*- coding: utf-8 -*-
#
# File: TKBusinessFunction.py
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
from Products.TKContactManager.config import *

##code-section module-header #fill in your manual code here
##/code-section module-header

schema = Schema((

    StringField(
        name='department',
        widget=StringWidget(
            label='Department',
            label_msgid='TKContactManager_label_department',
            i18n_domain='TKContactManager',
        ),
        schemata="Business Function",
        searchable=1,
    ),

    StringField(
        name='jobTitle',
        widget=StringWidget(
            label='Job title',
            label_msgid='TKContactManager_label_jobTitle',
            i18n_domain='TKContactManager',
        ),
        schemata="Business Function",
        searchable=1,
    ),

    TextField(
        name='responsibilities',
        allowable_content_types=('text/plain', 'text/structured', 'text/html',
                                 'application/msword',),
        widget=RichWidget(
            label='Responsibilities',
            label_msgid='TKContactManager_label_responsibilities',
            i18n_domain='TKContactManager',
        ),
        default_output_type='text/html',
        schemata="Business Function",
        searchable=1
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

TKBusinessFunction_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class TKBusinessFunction:
    """This mixin class is responsible for storing a business function related
       information like:
       - job title
       - responsibilities
    """
    security = ClassSecurityInfo()

    # This name appears in the 'add' box
    archetype_name = 'TKBusinessFunction'

    meta_type = 'TKBusinessFunction'
    portal_type = 'TKBusinessFunction'
    allowed_content_types = []
    filter_content_types = 0
    global_allow = 1
    #content_icon = 'TKBusinessFunction.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "TKBusinessFunction"
    typeDescMsgId = 'description_edit_tkbusinessfunction'

    _at_rename_after_creation = True

    schema = TKBusinessFunction_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

# end of class TKBusinessFunction

##code-section module-footer #fill in your manual code here
##/code-section module-footer



