# -*- coding: utf-8 -*-
#
# File: IMessageReceiver.py
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


##code-section module-header #fill in your manual code here
##/code-section module-header




import zope

class IMessageReceiver(zope.interface.Interface):
    '''Any component realising this interface should be able to send messages
       to its addressee[s]. Defining means of establishing addressees depends
       on implementation. 
    '''

    ##code-section class-header_IMessageReceiver #fill in your manual code here
    ##/code-section class-header_IMessageReceiver

    def sendMessage(subject, messageBody, channel='default'):
       """This operation sends a message, specified by its parameters, to
          its recipient[s] using means of communication specified by 'channel'
          or, in case 'channel' is 'default', defined by a component realising
          this interface (e.g. e-mail message).
       """

    def listAvailableCommunicationChannels():
        """This operation returns a tuple with a list of communication channels
           which can be used to send messages to addressee[s].
        """

    def getDefaultCommunicationChannel():
        """This operation returns a default communication channel in a
           human-readable form recognisable by sendMessage().
        """

##code-section module-footer #fill in your manual code here
##/code-section module-footer



