Introduction
============

Plonesocial.network is part of the `plonesocial suite`_.

This package provides a building block for Plone integrators who want to create a custom social business solution in Plone.

If you're an end-user looking for a pre-integrated solution, you should install `plonesocial.suite`_ instead.


plonesocial.network
===================

Plonesocial.network provides user profiles with follow/unfollow functionality.
It intercepts and overrides the default Plone ``author.cpt`` profile page.
If `plonesocial.activitystream`_ is installed, it will show status updates on the profile page.

Additionally, plonesocial.network provides ``@@following`` and ``@@followers`` views
that enable exploration of the social graph.

Core rendering logic is factored into two content providers, ``maxiprofile_provider``
and ``miniprofile_provider``. This enables and promotes code re-use across different views.

All browser views are anchored on the Site Root, so technically there's no user context
in the form of a Member folder required.

For a full social networking stack, install `plonesocial.suite`_.

bugs
----

Uninstalling either `plonesocial.microblog`_ or plonesocial_network removes both utilities, deleting all data.

.. _plonesocial suite: https://github.com/cosent/plonesocial.suite
.. _plonesocial.microblog: https://github.com/cosent/plonesocial.microblog
.. _plonesocial.activitystream: https://github.com/cosent/plonesocial.activitystream
.. _plonesocial.suite: https://github.com/cosent/plonesocial.suite

