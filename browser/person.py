from Acquisition import aq_inner

from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName

class PersonView:

    attributes = [
        'TKWebpage',
        'TKTelephoneNumber',
        'TKAddress',
        'TKInstantMessengerContact',
        'TKEmailAddress',
        ]

    def getPersonContents(self):
        """ Returns contents which are not attributes """
        
        portal_catalog = getToolByName(self, 'portal_catalog')
        context = aq_inner(self.context)

        query = {}
        # Making sure we get items only for current location
        currentPath = '/'.join(context.getPhysicalPath())
        query['path'] = {'query' : currentPath, 'depth': 1}

        results = portal_catalog.searchResults(**query)

        return [ x for x in results if x['meta_type'] not in self.attributes ]

    def getContactItems(self, portal_type):
        """ Returns list of contact items.
        portal_type can be any of the following: 
        TKTelephoneNumber,TKEmailAddress,TKInstantMessengerContact,TKWebpage """

        portal_catalog = getToolByName(self, 'portal_catalog')
        context = aq_inner(self.context)

        query = {}

        # Making sure we get items only for current location
        currentPath = '/'.join(context.getPhysicalPath())
        query['path'] = {'query' : currentPath, 'depth': 1}

        query['portal_type'] = portal_type

        results = portal_catalog.searchResults(**query)

        return results

    def isContactItem(self):
        """ Returns 1 when there is at least single contact item in container """

        portal_catalog = getToolByName(self, 'portal_catalog')
        context = aq_inner(self.context)
        portal_types = ('TKTelephoneNumber', 
                        'TKEmailAddress', 
                        'TKInstantMessengerContact', 
                        'TKWebpage', )

        currentPath = '/'.join(context.getPhysicalPath())
        path =  {'query' : currentPath, 'depth': 1} 
        results = portal_catalog(path = path, portal_type = portal_types)

        if results:
            return 1

        return 0

    def isAnyRelation(self):
        """ Returns 1 if there is a least one item in relationship to current context """

        relationships = ('employees_employers',
                         'coworkers_coworkers',
                         'manages_reportingto',
                         'reportingto_manages',
                         'primarycontactforpersons_ourprimarycontactsforthisperson',
                         'secondarycontactforpersons_oursecondarycontactsforthisperson',
                         'ourprimarycontactsforthisperson_primarycontactforpersons',
                         'oursecondarycontactsforthisperson_secondarycontactforpersons',
                         'ourprimarycontactsforthisorganisation_primarycontactfororganisations',
                         'oursecondarycontactsforthisorganisation_secondarycontactfororganisations',
                         'concerningperson_diaries',
                         'tkperson_annotations')

        context = aq_inner(self.context)

        for relation in relationships:
            if self.isRelation(relation):
                return 1

        return 0


    def isRelation(self, relationship):
        """ Returns 1 when there is relationship data for current context """

        context = aq_inner(self.context)
        
        if len(context.getRefs(relationship)):
            return 1

        return 0



class OrganisationView(PersonView):
    """ The view for TKOrganisation """

    __call__ = ViewPageTemplateFile('organisation.pt')

    attributes = [
        'TKWebpage',
        'TKTelephoneNumber',
        'TKAddress',
        'TKInstantMessengerContact',
        'TKEmailAddress',
        'TKPerson',
        ]

    def getOrganisationContents(self):
       return self.getPersonContents() 


class EmployeeView:

    def getBatchedEmployees(self):
        b_size = 10
        employees = self.context.getEmployees()

        if self.request.get('all', None):
            b_size = 9999
        from Products.CMFPlone import Batch
        b_start = self.request.get('b_start', 0)
        batch = Batch(employees, b_size, int(b_start), orphan=0)
        return batch

