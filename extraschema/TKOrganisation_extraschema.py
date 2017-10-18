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
        name='sellerInAcquisitions',
        widget=ReferenceBrowserWidget(
            label='Seller in Acquisitions',
            label_msgid='TKContactManager_label_sellerInAcquisitions',
            i18n_domain='TKContactManager',
            base_query={'portal_type':['PPPAcquisition',]},
	    show_path=0,
	    show_results_without_query=1,
	    allow_browse=1,
        ),
        multiValued=1,
        relationship='acquiredFrom_sellerInAcquisitions',
        schemata='PPP',
        allowed_types=['PPPAcquisition',],
    ),    
    
    RelationField(
        name='suppliedNonBenchmarkedFMServices',
        widget=ReferenceBrowserWidget(
            label='Supplied non Benchmarked FM Services',
            label_msgid='TKContactManager_label_suppliedNonBenchmarkedFMServices',
            i18n_domain='TKContactManager',
            base_query={'portal_type':['NonBenchmarkedFMService',]},
	    show_path=0,
	    show_results_without_query=1,
	    allow_browse=1,
        ),
        multiValued=1,
        relationship='serviceSupplier_suppliedNonBenchmarkedFMServices',
        schemata='PPP',
        allowed_types=['NonBenchmarkedFMService',],
    ),    

    RelationField(
        name='suppliedBenchmarkedFMServices',
        widget=ReferenceBrowserWidget(
            label='Supplied Benchmarked FM Services',
            label_msgid='TKContactManager_label_suppliedBenchmarkedFMServices',
            i18n_domain='TKContactManager',
            base_query={'portal_type':['BenchmarkedFMService',]},
	    show_path=0,
	    show_results_without_query=1,
	    allow_browse=1,
        ),
        multiValued=1,
        relationship='serviceSupplier_suppliedBenchmarkedFMServices',
        schemata='PPP',
        allowed_types=['BenchmarkedFMService',],
    ),    
    
    RelationField(
        name='constructorFor',
        widget=ReferenceBrowserWidget(
            label='Constructor for',
            label_msgid='TKContactManager_label_constructorFor',
            i18n_domain='TKContactManager',
            base_query={'portal_type':['SmifProject','PPPSPC']},
	    show_path=0,
	    show_results_without_query=1,
	    allow_browse=1,
        ),
        multiValued=1,
        relationship='constructor_constructorFor',
        schemata='PPP',
        allowed_types=['SmifProject','PPPSPC'],
    ),    
    
    RelationField(
        name='ownedSPCs',
        widget=ReferenceBrowserWidget(
            label='Owned SPCs',
            label_msgid='TKContactManager_label_ownedSPCs',
            i18n_domain='TKContactManager',
            base_query={'portal_type':['SmifProject','PPPSPC']},
	    show_path=0,
	    show_results_without_query=1,
	    allow_browse=1,
        ),
        multiValued=1,
        relationship='holdCo_ownedSPCs',
        schemata='PPP',
        allowed_types=['SmifProject','PPPSPC'],
    ),    
    
    RelationField(
        name='authorityFor',
        widget=ReferenceBrowserWidget(
            label='Authority for',
            label_msgid='TKContactManager_label_authorityFor',
            i18n_domain='TKContactManager',
            base_query={'portal_type':['SmifProject','PPPSPC']},
	    show_path=0,
	    show_results_without_query=1,
	    allow_browse=1,
        ),
        multiValued=1,
        relationship='authority_authorityFor',
        schemata='PPP',
        allowed_types=['SmifProject','PPPSPC'],
    ),    
    
    RelationField(
        name='managedSPCs',
        widget=ReferenceBrowserWidget(
            label='Managed SPCs',
            label_msgid='TKContactManager_label_managedSPCs',
            i18n_domain='TKContactManager',
            base_query={'portal_type':['SmifProject','PPPSPC']},
	    show_path=0,
	    show_results_without_query=1,
	    allow_browse=1,
        ),
        multiValued=1,
        relationship='manCo_managedSPCs',
        schemata='PPP',
        allowed_types=['SmifProject','PPPSPC'],
    ),    
    
    ),)
