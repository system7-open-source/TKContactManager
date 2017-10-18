# -*- coding: utf-8 -*-
#
# File: IEmailAddressProvider.py
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

class IEmailAddressProvider(zope.interface.Interface):
    '''Any class storing an email address is to realise this interface if the
       class is meant to provide the stored email address to any other classes
       or parts of the system requesting it.
    '''

    ##code-section class-header_IEmailAddressProvider #fill in your manual code here
    ##/code-section class-header_IEmailAddressProvider




    def getEmailAddress():
       """This operation returns an email address upon request.
       """
       
       


##code-section module-footer #fill in your manual code here
##/code-section module-footer



