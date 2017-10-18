# -*- coding: utf-8 -*-
#
# File: TKPerson.py
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
from Products.TKContactManager.auxiliary.TKBusinessFunction \
     import TKBusinessFunction
from Products.TKContactManager.auxiliary.TKRegisteredUser \
     import TKRegisteredUser
from Products.TKContactManager.auxiliary.TKMessageReceiver \
     import TKMessageReceiver
from Products.ATContentTypes.content.folder import ATFolder
from Products.TKContactManager.interfaces.IFullNameProvider \
     import IFullNameProvider
from Products.TKContactManager.interfaces.IContactDetails \
     import IContactDetails
from Products.TKContactManager.interfaces.ITKPerson import ITKPerson
from Products.Relations.field import RelationField
from Products.TKContactManager.config import *

##code-section module-header #fill in your manual code here
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget \
     import ReferenceBrowserWidget

from Products.CMFCore.utils import getToolByName
##/code-section module-header

schema = Schema((

    StringField(
        name='atitle',
        widget=SelectionWidget(
            label='Title',
            label_msgid='TKContactManager_label_atitle',
            i18n_domain='TKContactManager',
        ),
        required=1,
        schemata="Personal Details",
        searchable=0,
        default=' ',
        vocabulary=( ' ', 'Dr', 'Miss', 'Mr', 'Mrs', 'Prof.', 'Rev.' ),
        enforceVocabulary=1
        
    ),

    StringField(
        name='gender',
        widget=SelectionWidget(
            label='Gender',
            label_msgid='TKContactManager_label_gender',
            i18n_domain='TKContactManager',
        ),
        required=1,
        schemata="Personal Details",
        searchable=0,
        default=' ',
        vocabulary=( ' ', 'female', 'male' ),
        enforceVocabulary=1
        
    ),

    StringField(
        name='forename',
        widget=StringWidget(
            label='Forename',
            label_msgid='TKContactManager_label_forename',
            i18n_domain='TKContactManager',
        ),
        required=1,
        schemata="Personal Details",
        searchable=1
    ),

    StringField(
        name='surname',
        widget=StringWidget(
            label='Surname',
            label_msgid='TKContactManager_label_surname',
            i18n_domain='TKContactManager',
        ),
        required=1,
        schemata="Personal Details",
        searchable=1
    ),

    StringField(
        name='middleNames',
        widget=StringWidget(
            label='Middle names',
            label_msgid='TKContactManager_label_middleNames',
            i18n_domain='TKContactManager',
        ),
        schemata="Personal Details",
        searchable=1,
    ),

    TextField(
        name='biography',
        allowable_content_types=('text/plain', 'text/structured', 'text/html',
                                 'application/msword',),
        widget=RichWidget(
            label='Biography',
            label_msgid='TKContactManager_label_biography',
            i18n_domain='TKContactManager',
        ),
        default_output_type='text/html',
        schemata="Personal Details",
        searchable=1
    ),

    RelationField(
        name='employers',
        widget=ReferenceBrowserWidget(
            label='Employers',
            label_msgid='TKContactManager_label_employers',
            i18n_domain='TKContactManager',
        ),
        multiValued=1,
        relationship='employees_employers',
        schemata='Business Structure'
    ),

    RelationField(
        name='reportingTo',
        widget=ReferenceBrowserWidget(
            label='Reporting to',
            label_msgid='TKContactManager_label_reportingTo',
            i18n_domain='TKContactManager',
        ),
        multiValued=1,
        relationship='manages_reportingto',
        schemata='Business Structure'
    ),

    RelationField(
        name='ourPrimaryContactsForThisPerson',
        widget=ReferenceBrowserWidget(
            label='Our primary contacts for this person',
            label_msgid='TKContactManager_label_' \
                        'ourPrimaryContactsForThisPerson',
            i18n_domain='TKContactManager',
        ),
        multiValued=1,
        relationship='primarycontactforpersons_' \
                     'ourprimarycontactsforthisperson',
        schemata='Relationship Management'
    ),

    RelationField(
        name='coworkers',
        widget=ReferenceBrowserWidget(
            label='Direct co-workers',
            label_msgid='TKContactManager_label_coworkers',
            i18n_domain='TKContactManager',
            # Symmetrical relations in Relations seem not to work in both
            # directions so we will hide this field till we have it fixed
            visible = {"edit": "invisible", "view": "invisible"}
        ),
        multiValued=1,
        relationship='coworkers_coworkers',
        schemata='Business Structure'
    ),

    RelationField(
        name='primaryContactForOrganisations',
        widget=ReferenceBrowserWidget(
            label='Primary contact for organisations',
            label_msgid='TKContactManager_label_' \
                        'primaryContactForOrganisations',
            i18n_domain='TKContactManager',
        ),
        multiValued=1,
        relationship='ourprimarycontactsforthisorganisation_' \
                     'primarycontactfororganisations',
        schemata='Relationship Management'
    ),

    RelationField(
        name='ourSecondaryContactsForThisPerson',
        widget=ReferenceBrowserWidget(
            label='Our secondary contacts for this person',
            label_msgid='TKContactManager_label_' \
                        'ourSecondaryContactsForThisPerson',
            i18n_domain='TKContactManager',
        ),
        multiValued=1,
        relationship='secondarycontactforpersons_' \
                     'oursecondarycontactsforthisperson',
        schemata='Relationship Management'
    ),

    RelationField(
        name='secondaryContactForOrganisations',
        widget=ReferenceBrowserWidget(
            label='Secondary contact for organisations',
            label_msgid='TKContactManager_label_' \
                        'secondaryContactForOrganisations',
            i18n_domain='TKContactManager',
        ),
        multiValued=1,
        relationship='oursecondarycontactsforthisorganisation_' \
                     'secondarycontactfororganisations',
        schemata='Relationship Management'
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
        relationship='concerningperson_diaries',
        schemata='Relationship Management'
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
        relationship='tkperson_annotations',
        schemata='Relationship Management'
    ),

    RelationField(
        name='manages',
        widget=ReferenceBrowserWidget(
            label='Manages',
            label_msgid='TKContactManager_label_manages',
            i18n_domain='TKContactManager',
        ),
        multiValued=1,
        relationship='reportingto_manages',
        schemata='Business Structure'
    ),

    RelationField(
        name='primaryContactForPersons',
        widget=ReferenceBrowserWidget(
            label='Primary contact for persons',
            label_msgid='TKContactManager_label_primaryContactForPersons',
            i18n_domain='TKContactManager',
        ),
        multiValued=1,
        relationship='ourprimarycontactsforthisperson_' \
                     'primarycontactforpersons',
        schemata='Relationship Management'
    ),

    RelationField(
        name='secondaryContactForPersons',
        widget=ReferenceBrowserWidget(
            label='Secondary contact for persons',
            label_msgid='TKContactManager_label_secondaryContactForPersons',
            i18n_domain='TKContactManager',
        ),
        multiValued=1,
        relationship='oursecondarycontactsforthisperson_' \
                     'secondarycontactforpersons',
        schemata='Relationship Management'
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

TKPerson_schema = getattr(TKBusinessFunction, 'schema', Schema(())).copy() + \
    getattr(TKRegisteredUser, 'schema', Schema(())).copy() + \
    getattr(TKMessageReceiver, 'schema', Schema(())).copy() + \
    getattr(ATFolder, 'schema', Schema(())).copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here

# Hide the 'title' field in both the view and edit mode and make it optional.
# This content type does not need it. Also, see a definition of the Title()
# method below.
TKPerson_schema["title"].required = 0
TKPerson_schema["title"].widget.visible = {"edit": "invisible",
                                           "view": "invisible"}

##/code-section after-schema

class TKPerson(TKBusinessFunction, TKRegisteredUser,
               TKMessageReceiver, ATFolder):
    """This class is responsible for storing all the information about a person
       including the information about associations between persons and other
       entities related to them (vide the schema).
    """

    security = ClassSecurityInfo()
    __implements__ = (getattr(TKBusinessFunction,'__implements__',()),) \
                   + (getattr(TKRegisteredUser,'__implements__',()),) \
                   + (getattr(TKMessageReceiver,'__implements__',()),) \
                   + (getattr(ATFolder,'__implements__',()),)
    # zope3 interfaces
    #zope.interface.implements(IFullNameProvider)
    zope.interface.implements(ITKPerson)

    # This name appears in the 'add' box
    archetype_name = 'Person'

    __doc__ = 'Person'

    meta_type = 'TKPerson'
    portal_type = 'TKPerson'
    allowed_content_types = ['Folder', 'TKAddress', 'TKEmailAddress',
                             'TKInstantMessengerContact', 'TKTelephoneNumber',
                             'TKWebpage' ] + list(getattr(TKBusinessFunction,
                                              'allowed_content_types', [])) \
                          + list(getattr(TKRegisteredUser,
                                         'allowed_content_types', [])) \
                          + list(getattr(TKMessageReceiver,
                                         'allowed_content_types', [])) \
                          + list(getattr(ATFolder, 'allowed_content_types',
                                     []))
    filter_content_types = 1
    global_allow = 1
    content_icon = 'user.gif'
    immediate_view = '@@view'
    default_view = '@@view'
    suppl_views = ()
    typeDescription = "Person"
    typeDescMsgId = 'description_edit_tkperson'

    _at_rename_after_creation = True

    schema = TKPerson_schema

    ##code-section class-header #fill in your manual code here
    # Import the extraschema file (defining additional schema for this content
    # class) if it exists. Fail silently.
    from Products.TKContactManager.extraschema import extraschemas
    schema, extraschemata = extraschemas.gen_extraschema(meta_type, schema)
    ##/code-section class-header

    # Methods

    security.declarePublic('Title')
    def Title(self):
        """As this class does not need a separate title, this method is here to
           fulfil the Dublin Core standard and return a person's full name
           whenever the title is required. The Title field itself is hidden and
           invisible to users (vide supra).
        """
        
        return self.getFullName()

    security.declarePublic('getFullName')
    def getFullName(self):
        """This method implements an operation of the same name defined in
           IFullNameProvider interface.
        """
        middle = self.getMiddleNames()
        if len(middle) > 0:
            middle = " " + middle + " "
        else:
            middle = " "
        return self.getForename() + middle + self.getSurname()

    def _get_email_addresses(self):
        """This method searches for all e-mail addresses contained directly in
           a folder (TKPerson is a folderish content type) and returns a list
           of dictionaries in the following format:
           {'title' : 'personal e-mail', 'e-mail' : 'tomasz@kotarba.net'} 
        """
        addresses = []
        
        pc = getToolByName(self, 'portal_catalog')
        path = self.absolute_url_path()

        results = pc.searchResults(path=path, depth=0,
                                               portal_type="TKEmailAddress")
        
        for i in results:
            obj = i.getObject()
            addresses.append( { 'title' : obj.Title(),
                                'e-mail' : obj.getEmailAddress() } )
        return addresses

registerType(TKPerson, PROJECTNAME)
# end of class TKPerson

##code-section module-footer #fill in your manual code here
##/code-section module-footer



