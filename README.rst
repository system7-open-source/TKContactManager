================
TKContactManager
================

A powerful contact manager for Plone (Archetypes + some of the zope3 technologies). Tested with Plone 3.0, the product has proven to be a successful and production-ready CRM solution while in use in one of the FTSE100 corporations.

Please note, I created this project for the now ancient version of Plone and stopped maintaining it in 2008 so it is probably of little use.  I am putting it here for archiving purposes (too many of my projects were either lost or never open sourced).

Main features
-------------
* can be used for storing any information about people, organisations, companies etc. (including but not limited to contact details and some legal information).
* powerful bidirectional relations built in to allow users to reflect real-life associations between modelled entities

  *  customer relationship management and capturing information about external entities and how they are associated 

    * client-supplier relationships
    * primary & secondary internal contacts for persons and organisations

  * modelling the organisational structure

    * employment relationship
    * manager-subordinate relationship
    * direct co-worker relationship
    * parent-subsidiary/associate relationship

* simple yet powerful and flexible mechanism providing multiple independent diaries and annotations which can be associated to persons and organisations in order to capture and store any useful information (e.g. a diary describing a history of all the interactions between entities)
* several new content types (Address, E-mail Address, Instant Messenger Contact, Organisation, Person, Share, Telephone Number, Web Page)
* integrated with Google Maps (depends on the Maps Plone product)
* integrated with Diaries
* easily expandable to incorporate new fields and new relations (see extraschema in the product directory and the PPPTKContactManager branch for an example on how to use the extraschema facility)


Dependencies
------------
See file config.py.

* ATCountryWidget (http://www.gocept.com/open_source_software/ATCountryWidget/)
* Maps (http://plone.org/products/maps)
* Relations (http://plone.org/products/relations) - use the code from the svn.


Setting up and logging in
-------------------------
We use zope.testbrowser to simulate browser interaction.

    >>> from Products.Five.testbrowser import Browser
    >>> browser = Browser()
    >>> portal_url = self.portal.absolute_url()

This is useful when debuging test browser tests. It shows error messages properly.

    >>> browser.handleErrors = False
    >>> self.portal.error_log._ignored_exceptions = ()

We then turn off the various portlets, because they sometimes duplicate links
and text.

    >>> from zope.component import getUtility, getMultiAdapter

    >>> from plone.portlets.interfaces import IPortletManager
    >>> from plone.portlets.interfaces import IPortletAssignmentMapping

    >>> left_column = getUtility(IPortletManager, name=u"plone.leftcolumn")
    >>> left_assignable = getMultiAdapter((self.portal, left_column), IPortletAssignmentMapping)
    >>> for name in left_assignable.keys():
    ...     del left_assignable[name]

    >>> right_column = getUtility(IPortletManager, name=u"plone.rightcolumn")
    >>> right_assignable = getMultiAdapter((self.portal, right_column), IPortletAssignmentMapping)
    >>> for name in right_assignable.keys():
    ...     del right_assignable[name]

We need to log in as the portal owner, we use login page for this.

    >>> from Products.PloneTestCase.setup import portal_owner, default_password

    >>> browser.open(portal_url + '/login_form?came_from=' + portal_url)
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()

This is useful stuff for debugging!

open('/tmp/test-output.html', 'w').write(browser.contents)

Make sure we can add the relevant content types
------------------------------------------------

    >>> browser.open(portal_url)

Verify that we have relevant links to add TKPerson content

    >>> browser.getLink(id='tkperson').url.endswith("createObject?type_name=TKPerson")
    True

Try to add TKEmailAddress content type, we should not be able to add that as it should only be addable from TKPerson.
However it is not implemented yet so we expect this to return True.
We should really expect this here when the change is implemented:
Traceback (most recent call last):
...
LinkNotFoundError

    >>> browser.getLink(id='tkemailaddress').url.endswith("createObject?type_name=TKEmailAddress")
    True

See if we can add new TKPerson and some contact details there.

    >>> browser.open(portal_url)
    >>> browser.getLink(id='tkperson').click()
    >>> browser.getControl(name='forename').value = "John"
    >>> browser.getControl(name='surname').value = "Snow"
    >>> browser.getControl(name='form_submit').click()

Checking if my TKPerson object is there.

    >>> 'john-snow' in self.portal.objectIds()
    True

Get the absolute path to john-snow object, so we can add contact objects in that container.

    >>> johnsnow = self.portal['john-snow']
    >>> johnsnow_url = johnsnow.absolute_url()

Add new object of TKEmailAddress content type.
This will actually give error as there is no tkemailaddress link in drop down menu when you are in TKPerson object.
We need to fix that and run test again!

    >>> browser.open(johnsnow_url)
    >>> browser.getLink(id='tkemailaddress').click()
    >>> browser.getControl(name='title').value = "js-email"
    >>> browser.getControl(name='email').value = "john@localhost"
    >>> browser.getControl(name='form_submit').click()

    >>> 'js-email' in johnsnow.objectIds()
    True

    >>> email1 = johnsnow['js-email']
    >>> email1_url = email1.absolute_url()
    >>> email1.email
    'john@localhost'

