# -*- coding: utf-8 -*-
#
# File: TKOrganisation.py
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
from Products.ATContentTypes.content.folder import ATFolder
from Products.Archetypes.ReferenceEngine import ContentReferenceCreator
from Products.Relations.field import RelationField
from Products.TKContactManager.config import *

from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget \
     import ReferenceBrowserWidget
from Products.TKContactManager.interfaces.ITKOrganisation import ITKOrganisation
from zope.interface import implements

schema = Schema((

    StringField(
        name='name',
        widget=StringWidget(
            label='Name',
            label_msgid='TKContactManager_label_name',
            i18n_domain='TKContactManager',
        ),
        required=1,
        schemata="Organisation Details",
        searchable=1
    ),

    StringField(
        name='registrationNumber',
        widget=StringWidget(
            label='Registration number',
            label_msgid='TKContactManager_label_registrationNumber',
            i18n_domain='TKContactManager',
        ),
        schemata="Organisation Details",
    ),

    StringField(
        name='VATNumber',
        widget=StringWidget(
            label='VAT number',
            label_msgid='TKContactManager_label_VATNumber',
            i18n_domain='TKContactManager',
        ),
        schemata="Organisation Details",
    ),

    RelationField(
        name='client',
        widget=ReferenceBrowserWidget(
            label='Client',
            label_msgid='TKContactManager_label_client',
            i18n_domain='TKContactManager',
        ),
        multiValued=1,
        relationship='suppliers_client'
    ),

    RelationField(
        name='annotations',
        widget=ReferenceBrowserWidget(
            label='Annotations',
            label_msgid='TKContactManager_label_annotations',
            i18n_domain='TKContactManager',
            hide_inaccessible=1,
        ),
        multiValued=1,
        relationship='concerningorganisation_annotations'
    ),

    RelationField(
        name='diaries',
        widget=ReferenceBrowserWidget(
            label='Diaries',
            label_msgid='TKContactManager_label_diaries',
            i18n_domain='TKContactManager',
            hide_inaccessible=1,
        ),
        multiValued=1,
        relationship='concerningorganisation_diaries'
    ),

    RelationField(
        name='subsidiaries_associates',
        widget=ReferenceBrowserWidget(
            label='Subsidiaries/associates',
            label_msgid='TKContactManager_label_subsidiaries_associates',
            i18n_domain='TKContactManager',
        ),
        multiValued=1,
        relationship='TKShare'
    ),

    RelationField(
        name='employees',
        widget=ReferenceBrowserWidget(
            label='Employees',
            label_msgid='TKContactManager_label_employees',
            i18n_domain='TKContactManager',
        ),
        multiValued=1,
        relationship='employers_employees'
    ),

    RelationField(
        name='suppliers',
        widget=ReferenceBrowserWidget(
            label='Suppliers',
            label_msgid='TKContactManager_label_suppliers',
            i18n_domain='TKContactManager',
        ),
        multiValued=1,
        relationship='client_suppliers'
    ),

    RelationField(
        name='ourPrimaryContactsForThisOrganisation',
        widget=ReferenceBrowserWidget(
            label='Our primary contacts for this organisation',
            label_msgid='TKContactManager_label_' \
                        'ourPrimaryContactsForThisOrganisation',
            i18n_domain='TKContactManager',
        ),
        multiValued=0,
        relationship='primarycontactfororganisations_' \
                     'ourprimarycontactsforthisorganisation'
    ),

    RelationField(
        name='ourSecondaryContactsForThisOrganisation',
        widget=ReferenceBrowserWidget(
            label='Our secondary contacts for this organisation',
            label_msgid='TKContactManager_label_' \
                        'ourSecondaryContactsForThisOrganisation',
            i18n_domain='TKContactManager',
        ),
        multiValued=1,
        relationship='secondarycontactfororganisations_' \
                     'oursecondarycontactsforthisorganisation'
    ),

    RelationField(
        name='parents',
        widget=ReferenceBrowserWidget(
            label='Parents',
            label_msgid='TKContactManager_label_parents',
            i18n_domain='TKContactManager',
        ),
        multiValued=1,
        relationship='subsidiaries_associates_parents'
    ),

),
)

TKOrganisation_schema = getattr(ATFolder, 'schema', Schema(())).copy() + \
    schema.copy()

# Hide the 'title' field in both the view and edit mode and make it optional.
# This content type does not need it. Also, see a definition of the Title()
# method below.
TKOrganisation_schema["title"].required = 0
TKOrganisation_schema["title"].widget.visible = {"edit": "invisible",
						 "view": "invisible"}

class TKOrganisation(ATFolder):
    """This class is responsible for storing all the information about an
       organisation including the information about associations between
       organisations and other entities related to them (vide the schema).
    """
    security = ClassSecurityInfo()
    __implements__ = (getattr(ATFolder,'__implements__',()),)

    # This name appears in the 'add' box
    archetype_name = 'Organisation'

    __doc__ = 'Organisation'

    meta_type = 'TKOrganisation'
    portal_type = 'TKOrganisation'
    allowed_content_types = ['Folder', 'TKPerson', 'TKAddress',
                             'TKOrganisation', 'TKEmailAddress',
                             'TKInstantMessengerContact',
                             'TKTelephoneNumber', 'TKWebpage' ]
    filter_content_types = 1
    global_allow = 1
    content_icon = 'organisation.png'
    immediate_view = '@@view'
    default_view = '@@view'
    suppl_views = ()
    typeDescription = "Organisation"
    typeDescMsgId = 'description_edit_tkorganisation'

    _at_rename_after_creation = True

    schema = TKOrganisation_schema

    ##code-section class-header #fill in your manual code here
    implements(ITKOrganisation)
    ##/code-section class-header

    # Methods

    security.declarePublic('Title')
    def Title(self):
        """As this class does not need a separate title, this method is here to
           fulfil the Dublin Core standard and return an organisation name
           whenever the title is required. The Title field itself is hidden and
           invisible to users (vide supra).
        """
        
        return self.getName()

registerType(TKOrganisation, PROJECTNAME)
# end of class TKOrganisation

##code-section module-footer #fill in your manual code here
##/code-section module-footer



