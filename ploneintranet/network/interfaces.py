# -*- coding: utf-8 -*-
from zope.interface import Interface


class INetworkGraph(Interface):
    """Stores a social network graph of users
    following/unfollowing/blocking eachother.
    """

    def set_follow(actor, other):
        """User <actor> subscribes to user <other>"""

    def set_unfollow(actor, other):
        """User <actor> unsubscribes from user <other>"""

    def get_following(actor):
        """List all users that <actor> subscribes to"""

    def get_followers(actor):
        """List all users that subscribe to <actor>"""


class INetworkTool(INetworkGraph):
    """Provide INetworkContainer as a site utility."""


class ILikesContainer(Interface):
    """Stores likes.
    """


class ILikesTool(ILikesContainer):
    """Provide ILikesContainer as a site utility."""
