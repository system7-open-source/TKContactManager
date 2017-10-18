# Use this file to define extra schema for the TKContactManager content classes.
# Remove this file, leave the file blank or define the "extraschema" variable
# as an empty Schema to skip the use of additional schema for this content
# class.

from Products.Archetypes.atapi import *

extraschema = Schema((

    StringField(
        name='someExtraData',
        widget=StringWidget(
            label='Some Extra Data',
            label_msgid='TKContactManager_label_someExtraData',
            i18n_domain='TKContactManager',
        ),
        required=0,
        schemata="An Extra Schemata",
        searchable=0,
        ),
    
    ),)
