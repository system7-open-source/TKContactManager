import unittest
from Products.TKContactManager.tests.base import TKContactManagerTestCase

from Products.CMFCore.utils import getToolByName


class TestSetup(TKContactManagerTestCase):

    def afterSetUp(self):
        self.types = getToolByName(self.portal, 'portal_types')

    def test_maps_installed(self):
        self.failUnless('GeoLocation' in self.types.objectIds())

    def test_relations_installed(self):
        self.failUnless('Relations Library' in self.types.objectIds())

    def test_tkcontactmanager_installed(self):
        self.failUnless('TKPerson' in self.types.objectIds())

def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestSetup))
    return suite
