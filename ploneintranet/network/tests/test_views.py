# -*- coding: utf-8 -*-
from ploneintranet.network.browser.author import AuthorView
from ploneintranet.network.browser.interfaces import IPloneIntranetNetworkLayer
from ploneintranet.network.testing import IntegrationTestCase
from zope.interface import directlyProvides


class TestViews(IntegrationTestCase):

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']
        directlyProvides(self.request, IPloneIntranetNetworkLayer)

    def test_author(self):
        ''' We have to be sure that we get our custom author zope view and
        not the FSControllerPageTemplate
        This is going to fail in Plone4
        '''
        author_view = self.portal.restrictedTraverse('author')
        self.assertIsInstance(author_view, AuthorView)
