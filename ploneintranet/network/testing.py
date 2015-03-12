# -*- coding: utf-8 -*-
"""Base module for unittesting."""

from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import TEST_USER_ID
from plone.app.testing import TEST_USER_NAME
from plone.app.testing import applyProfile
from plone.app.testing import login
from plone.app.testing import setRoles
from plone.testing import z2
from ploneintranet.network.browser.interfaces import IPloneIntranetNetworkLayer
from zope.interface import alsoProvides

import unittest2 as unittest


def set_browserlayer(request):
    """Set the BrowserLayer for the request.

    We have to set the browserlayer manually, since importing the profile alone
    doesn't do it in tests.
    """
    alsoProvides(request, IPloneIntranetNetworkLayer)


class PloneintranetTodoLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        """Set up Zope."""
        # Load ZCML
        import ploneintranet.network
        self.loadZCML(package=ploneintranet.network)
        z2.installProduct(app, 'ploneintranet.network')
        import ploneintranet.microblog
        self.loadZCML(package=ploneintranet.microblog)
        z2.installProduct(app, 'ploneintranet.microblog')
        import plone.app.discussion
        self.loadZCML(package=plone.app.discussion)
        z2.installProduct(app, 'plone.app.discussion')

    def setUpPloneSite(self, portal):
        """Set up Plone."""
        # Install into Plone site using portal_setup
        applyProfile(portal, 'ploneintranet.network:default')
        applyProfile(portal, 'ploneintranet.microblog:default')
        applyProfile(portal, 'plone.app.discussion:default')

        # Login and create some test content
        setRoles(portal, TEST_USER_ID, ['Manager'])
        login(portal, TEST_USER_NAME)
        portal.invokeFactory('Folder', 'folder')

        # Commit so that the test browser sees these objects
        portal.portal_catalog.clearFindAndRebuild()
        import transaction
        transaction.commit()

    def tearDownZope(self, app):
        """Tear down Zope."""
        z2.uninstallProduct(app, 'ploneintranet.network')


FIXTURE = PloneintranetTodoLayer()
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,), name='PloneintranetNetworkLayer:Integration')
FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE,), name='PloneintranetNetworkLayer:Functional')


class IntegrationTestCase(unittest.TestCase):
    """Base class for integration tests."""

    layer = INTEGRATION_TESTING


class FunctionalTestCase(unittest.TestCase):
    """Base class for functional tests."""

    layer = FUNCTIONAL_TESTING
