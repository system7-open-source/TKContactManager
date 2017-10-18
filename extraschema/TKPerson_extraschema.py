# Use this file to define extra schema for the TKContactManager content classes.
# Remove this file, leave the file blank or define the "extraschema" variable
# as an empty Schema to skip the use of additional schema for this content
# class.

from Products.Archetypes.atapi import *
from Products.Relations.field import RelationField
from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import \
     ReferenceBrowserWidget

extraschema = Schema((
        
    RelationField(
        name='fmContactForSites',
        widget=ReferenceBrowserWidget(
            label='FM Contact for Sites',
            label_msgid='TKContactManager_label_fmContactForSites',
            i18n_domain='TKContactManager',
            base_query={'portal_type':['PPPSite',]},
	    show_path=0,
	    show_results_without_query=1,
	    allow_browse=1,
        ),
        multiValued=1,
        relationship='fmContacts_fmContactForSites',
        schemata='PPP',
        allowed_types=['PPPSite',],
    ),

    RelationField(
        name='clientContactForSites',
        widget=ReferenceBrowserWidget(
            label='Client Contact for Sites',
            label_msgid='TKContactManager_label_clientContactForSites',
            i18n_domain='TKContactManager',
            base_query={'portal_type':['PPPSite',]},
	    show_path=0,
	    show_results_without_query=1,
	    allow_browse=1,
        ),
        multiValued=1,
        relationship='clientContacts_clientContactForSites',
        schemata='PPP',
        allowed_types=['PPPSite',],
    ),
    
    RelationField(
        name='regionalDirectorForRegions',
        widget=ReferenceBrowserWidget(
            label='Regional Director for Regions',
            label_msgid='TKContactManager_label_regionalDirectorForRegions',
            i18n_domain='TKContactManager',
            base_query={'portal_type':['PPPRegion',]},
	    show_path=0,
	    show_results_without_query=1,
	    allow_browse=1,
        ),
        multiValued=1,
        relationship='regionalDirector_regionalDirectorForRegions',
        schemata='PPP',
        allowed_types=['PPPRegion',],
    ),
    
    RelationField(
        name='ledAcquisitions',
        widget=ReferenceBrowserWidget(
            label='Led Acquisitions',
            label_msgid='TKContactManager_label_ledAcquisitions',
            i18n_domain='TKContactManager',
            base_query={'portal_type':['PPPAcquisition',]},
	    show_path=0,
	    show_results_without_query=1,
	    allow_browse=1,
        ),
        multiValued=1,
        relationship='acquisitionLead_ledAcquisitions',
        schemata='PPP',
        allowed_types=['PPPAcquisition',],
    ),
    
    ),)
