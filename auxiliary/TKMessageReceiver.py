# -*- coding: utf-8 -*-
#
# File: TKMessageReceiver.py
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
from Products.TKContactManager.interfaces.IMessageReceiver \
    import IMessageReceiver
from Products.TKContactManager.config import *

##code-section module-header #fill in your manual code here
from Products.CMFCore.utils import getToolByName
from Products.CMFCore.utils import getUtilityByInterfaceName
##/code-section module-header

schema = Schema((

    LinesField(
        name='sendMessagesBy',
        widget=MultiSelectionWidget(
            description="Choose a communication medium the system" \
                "will use to contact this person.",
            label='Send messages by',
            label_msgid='TKContactManager_label_sendMessagesBy',
            description_msgid='TKContactManager_help_sendMessagesBy',
            i18n_domain='TKContactManager',
        ),
        schemata="Notifications",
        multiValued=1,
        vocabulary= "listAvailableCommunicationChannels",
        default="e-mail",
        required=1,
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

TKMessageReceiver_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class TKMessageReceiver:
    """This class is responsible for allowing users to choose a default method
    the system should use for sending text messages to a given person. It
    persists the user choice.
    This class realises the IMessageReceiver interface so it is also
    responsible for fulfilling a contract specified by that interface.
    """
    security = ClassSecurityInfo()
    # zope3 interfaces
    zope.interface.implements(IMessageReceiver)

    # This name appears in the 'add' box
    archetype_name = 'TKMessageReceiver'

    meta_type = 'TKMessageReceiver'
    portal_type = 'TKMessageReceiver'
    allowed_content_types = []
    filter_content_types = 0
    global_allow = 1
    #content_icon = 'TKMessageReceiver.gif'
    immediate_view = 'base_view'
    default_view = 'base_view'
    suppl_views = ()
    typeDescription = "TKMessageReceiver"
    typeDescMsgId = 'description_edit_tkmessagereceiver'

    _at_rename_after_creation = True

    schema = TKMessageReceiver_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    security.declarePublic('sendMessage')
    def sendMessage(self, subject, messageBody, channel='default'):
        """This method implements an operation of the same name specified in
           the IMessageReceiver interface.
        """
        if channel == 'default':
            channel = self.getDefaultCommunicationChannel()
        
        if channel == 'e-mail':
            self._send_message_by_email(subject,messageBody)
        else:
            raise ValueError("'%s' is an unknown communication channel." 
                             % channel)

    
    def _send_message_by_email(self, subject, messageBody):
        """This method sends messages via e-mai. It does not send anything in
           case it does not receive at least one e-mail address from a method
           '_get_email_addresses'.
        """
        addresses = self._get_email_addresses()
        if len(addresses) > 0:
            address = addresses[0]
        else:
            address = None
        
        if address:
            portal = getUtilityByInterfaceName('Products.CMFPlone.interfaces' \
                                               '.siteroot.IPloneSiteRoot')
            mail_from = '"%s" <%s>' % (portal.email_from_name,
                                       portal.email_from_address)
            mh = getToolByName(self,'MailHost')
            mh.send(messageBody, address['e-mail'], mail_from, subject)
        
    def listAvailableCommunicationChannels(self):
        """This method implements an operation of the same name specified in
           the IMessageReceiver interface.
        """
        return ('e-mail',)

    def getDefaultCommunicationChannel(self):
        """This method implements an operation of the same name specified in
           the IMessageReceiver interface.
        """
        
        return 'e-mail'

# end of class TKMessageReceiver

##code-section module-footer #fill in your manual code here
##/code-section module-footer



