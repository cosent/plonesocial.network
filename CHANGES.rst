Changelog
=========

0.7.0 (unreleased)
------------------

* Rename @@profile -> @@author (Assembla #228) [ale-rt]

* Uninstall profile [ale-rt, fulv]

* Plone 5.0a3 porting [ale-rt, fulv, reinhardt]

* add ploneintranet.core dependency [Guido A.J. Stevens]

* Add more basic installation/uninstallation tests [hvelarde]

* Add test to demonstrate INetworkTool has been uninstalled (closes #4) [hvelarde]

* 'Like' functionality [pbauer, reinhardt]


0.6.1 (2014-03-11)
------------------

* Reflect changed version in changelog [gyst]

0.6.0 (2014-03-11)
------------------

* Bind browserviews to INavigationRoot instead of ISiteRoot [gyst]

* Package distribution was fixed by adding classifiers, dependencies and
  fixing license version number as GPLv2; a MANIFEST.in file was also added.
  [hvelarde]

* Brazilian Portuguese translation was added.
  [hvelarde]

* enrich CSS markup [Guido A.J. Stevens]

* bump version [Guido A.J. Stevens]

* make sure only the right subunsub form is processed, fixes #7 [Guido A.J. Stevens]


0.5.2 (2013-07-31)
------------------

* bump version after having pypi release confusion [gyst]
* update docs [gyst]

0.4.3 (2013-04-29)
------------------

* Plone 4.3 compatibility [tdesvenain]
* Dutch translation [maartenkling]

0.4.2 (2012-11-26)
------------------

* add Dutch translation [maartenkling]
* translate follow/unfollow buttons [maartenkling]
* update changelog, release [gyst]
* provide a virtualenv-enabled Travis buildout that can be debugged on a dev box [gyst]
* pep8 fixes [gyst]
* Updated Spanish l10n and Master manual template [macagua]
* Added locales and i18n extract script [macagua]
* Added more improvements about i18n support [macagua]
* Updated contributors file [macagua]
* Updated changelog [macagua]
* fix pyflakes by moving monkey into __init__ [gyst]
* ignore dist [gyst]
* pep8/pyflakes [hvelarde]
* update Travis CI configuration to include pep8/pyflakes testing [hvelarde]
* update location of extended configuration as the plonetest repo was moved to GitHub [hvelarde]
* update list of ignored objects [hvelarde]
* cleanup, bump version [gyst]
* add Travis CI configuration [hvelarde]
* fix rst formatting [gyst]

0.4.1 (2012-10-09)
------------------

* oops. merge. [gyst]
* ignore dist [gyst]
* small fixes [gyst]
* fix inline form submission handling [gyst]
* add profile navigation [gyst]

0.4 (2012-10-09)
----------------

Initial release.

* update docs [gyst]
* fix dependency [gyst]
* reindent for better pep8 [gyst]
* finish following/followers views [gyst]
* extract maxiprofile provider [gyst]
* base skel for following/followers view [gyst]
* provide clear [gyst]
* more styling [gyst]
* intercept /author and redirect to /@@profile [gyst]
* follow/unfollow buttons [gyst]
* s/followees/following/ [gyst]
* document weird uninstall behaviour [gyst]
* show ploneintranet.activitystream, if installed [gyst]
* provide consistency with ploneintranet.activitystream [gyst]
* GS name [gyst]
* base profile [gyst]
* a monkey that works, thx enfold [gyst]
* monkeypatch image sizes -- doesnt work :-( [gyst]
* fix setup.py [gyst]
* base skel for traversable profile view [gyst]
* doc [gyst]
* core follow/unfollow social graph API [gyst]
* provide noop tool install [gyst]
* remove src indirection [gyst]
* initial checkin from zopeskel [gyst]
