from Products.Five import zcml
from Products.Five import fiveconfigure

from Testing import ZopeTestCase as ztc

from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import onsetup

ztc.installProduct('Maps')
ztc.installProduct('Relations')
ztc.installProduct('TKContactManager')

@onsetup
def setup_tkcontactmanager():
    """Set up the additional products required by TKContactManager."""

    # load the zcml configuration file from TKContactManager
    fiveconfigure.debug_mode = True
    import Products.TKContactManager
    zcml.load_config('configure.zcml', Products.TKContactManager)
    fiveconfigure.debug_mode = False

    ztc.installPackage('Products.TKContactManager')

#setup_tkcontactmanager()
ptc.setupPloneSite(products=['Products.TKContactManager'])

class TKContactManagerTestCase(ptc.PloneTestCase):
    """ We use this base class for all the tests """

    
class TKContactManagerFunctionalTestCase(ptc.FunctionalTestCase):
    """ Test case for functional tests """
