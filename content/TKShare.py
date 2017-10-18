# -*- coding: utf-8 -*-
#
# File: TKShare.py
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

# The following two imports are needed for the isValidShare validator
from Products.validation.validators.RangeValidator import RangeValidator
from Products.validation import validation
 
# A validator used by the shareOwned field to ensure that its value stays in
# the [0, 100] range.
isValidShare = RangeValidator("isValidShare", 0, 100)
validation.register(isValidShare)

##/code-section module-header

schema = Schema((

    FloatField(
        name='shareOwned',
        validators=('isValidShare',),
        widget=DecimalWidget(
            description="Percentage owned [0.0 - 100.0]. Please, do not use " \
                        "the '%' character!",
            label='Share owned',
            label_msgid='TKContactManager_label_shareOwned',
            description_msgid='TKContactManager_help_shareOwned',
            i18n_domain='TKContactManager',
        ),
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

TKShare_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class TKShare(BaseContent):
    """This is an association class responsible for storing a numerical value
       (1-100) of a share in a subsidiary/associate company owned by some other
       company. Used by TKOrganisation (parents to subsidiaries/associates
       association).
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(BaseContent,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Share'

    meta_type = 'TKShare'
    portal_type = 'TKShare'
    allowed_content_types = []
    filter_content_types = 0
    global_allow = 1
    #content_icon = 'TKShare.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "Share"
    typeDescMsgId = 'description_edit_tkshare'

    _at_rename_after_creation = True

    schema = TKShare_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

registerType(TKShare, PROJECTNAME)
# end of class TKShare

##code-section module-footer #fill in your manual code here
##/code-section module-footer



