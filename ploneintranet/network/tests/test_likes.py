# -*- coding: utf-8 -*-
import unittest2 as unittest
from plone import api
from plonesocial.network.interfaces import ILikesContainer
from plonesocial.network.interfaces import ILikesTool
from plonesocial.network.likes import LikesContainer
from plonesocial.network.testing import IntegrationTestCase
from zope.component import getUtility
from zope.component import queryUtility


class TestLikesTool(IntegrationTestCase):

    def setUp(self):
        self.portal = self.layer['portal']

    def test_likes_tool_available(self):
        tool = queryUtility(ILikesTool)
        self.assertTrue(ILikesContainer.providedBy(tool))

    def test_likes_tool_uninstalled(self):
        qi = self.portal['portal_quickinstaller']
        with api.env.adopt_roles(['Manager']):
            qi.uninstallProducts(products=['plonesocial.network'])
        self.assertNotIn('plonesocial_likes', self.portal)
        tool = queryUtility(ILikesTool, None)
        self.assertIsNone(tool)

    def test_multiple_liking(self):
        """Test liking with multiple users and various content
        """
        user1 = api.user.create(
            email='john@plone.org',
            username='user1'
        )
        user2 = api.user.create(
            email='jane@plone.org',
            username='user2'
        )
        all_userids = [
            user1.getId(),
            user2.getId(),
            'admin',
        ]
        doc1 = api.content.create(
            container=self.portal,
            type='Document',
            id='doc1',
            title='Doc 1'
        )
        doc2 = api.content.create(
            container=self.portal,
            type='Document',
            id='doc2',
            title='Doc 2'
        )

        util = getUtility(ILikesTool)
        # 1. All users like doc1
        # 2. user1 and user2 like doc2
        # 3. Check counts and who has liked
        util.like(
            user_id=all_userids,
            item_id=doc1.UID(),
        )
        self.assertEqual(len(util._user_uuids_mapping), 3)
        self.assertEqual(len(util._uuid_users_mapping), 1)
        self.assertEqual(
            [doc1.UID()],
            sorted(list(util._uuid_users_mapping))
        )

        user1_id = user1.getId()
        user2_id = user2.getId()
        util.like(
            user_id=[user1_id, user2_id],
            item_id=doc2.UID(),
        )
        results = util.get_users_for_item(doc2.UID())
        self.assertEqual(len(results), 2)
        self.assertIn(user1_id, results)
        self.assertIn(user2_id, results)


class TestLikes(unittest.TestCase):

    def setUp(self):
        # self.portal = self.layer['portal']
        self.userid = 'testperson@test.org'
        self.object_uuid = '827e65bd826a89790eba679e0c9ff864'
        self.container = LikesContainer()

    def _add(self):
        self.container.add(
            self.userid, self.object_uuid)

    def test_add(self):
        self._add()

        liked_items = self.container._user_uuids_mapping[self.userid]
        self.assertEqual(sorted(list(liked_items)), [self.object_uuid])

        liking_users = self.container._uuid_users_mapping[self.object_uuid]
        self.assertEqual(sorted(list(liking_users)), [self.userid])

    def test_liked_by_two_users(self):
        self._add()
        self.container.add(
            'cyclon@test.org', self.object_uuid)

        liked_items = self.container._user_uuids_mapping[self.userid]
        self.assertEqual(sorted(list(liked_items)), [self.object_uuid])
        liked_items = self.container._user_uuids_mapping['cyclon@test.org']
        self.assertEqual(sorted(list(liked_items)), [self.object_uuid])

        liking_users = self.container._uuid_users_mapping[self.object_uuid]
        self.assertEqual(
            sorted(list(liking_users)),
            ['cyclon@test.org', self.userid])

    def test_remove(self):
        self._add()

        self.container.remove(self.userid, self.object_uuid)

        liked_items = self.container._user_uuids_mapping[self.userid]
        self.assertEqual(sorted(list(liked_items)), [])

        liking_users = self.container._uuid_users_mapping[self.object_uuid]
        self.assertEqual(sorted(list(liking_users)), [])

    def test_get(self):
        self._add()
        self.assertEqual(
            sorted(list(self.container.get(self.userid))), [self.object_uuid])

    def test_get_empty(self):
        self.assertEqual(self.container.get(self.userid), [])

    def test_lookup(self):
        self._add()
        self.assertEqual(
            sorted(list(self.container.lookup(self.object_uuid))),
            [self.userid]
        )

    def test_lookup_empty(self):
        self.assertEqual(
            self.container.lookup(self.object_uuid), [])

    def test_is_item_liked_by_user(self):
        self.assertFalse(
            self.container.is_item_liked_by_user(
                self.userid,
                self.object_uuid))

        self._add()

        self.assertTrue(
            self.container.is_item_liked_by_user(
                self.userid,
                self.object_uuid))

    def test_get_items_for_user(self):
        self._add()
        self.assertIn(
            self.object_uuid,
            self.container.get_items_for_user(self.userid)
        )

    def test_get_users_for_item(self):
        self._add()
        self.assertIn(
            self.userid,
            self.container.get_users_for_item(self.object_uuid)
        )
