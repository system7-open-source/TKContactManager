# -*- coding: utf-8 -*-
#
# File: IUsernameProvider.py
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

class IUsernameProvider(zope.interface.Interface):
    '''Any component meant to provide a stored or computed system ID
       (a username) to any other part of the system is to realise this
       interface.
    '''

    ##code-section class-header_IUsernameProvider #fill in your manual code here
    ##/code-section class-header_IUsernameProvider




    def getUsername():
       """This operation returns a system ID (a username) of a person.
       """
       
       


##code-section module-footer #fill in your manual code here
##/code-section module-footer



