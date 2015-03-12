from setuptools import setup, find_packages

version = '0.7.0.dev'

long_description = (
    open('README.rst').read()
    + '\n' +
    open('CONTRIBUTORS.rst').read()
    + '\n' +
    open('CHANGES.rst').read()
    + '\n')

setup(
    name='ploneintranet.network',
    version=version,
    description="Personal profile + follow/unfollow functionality "
    "for the Plonesocial suite",
    long_description=long_description,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Plone :: 4.2',
        'Framework :: Plone :: 4.3',
        'Framework :: Plone',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='plone, zope, socbiz, ploneintranet',
    author='Guido Stevens',
    author_email='guido.stevens@cosent.net',
    url='http://github.com/cosent/ploneintranet.network',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'ploneintranet.core',
        'plone.app.layout',
        'plone.api',
        'Products.CMFCore',
        'Products.CMFPlone >=4.2',
        'Products.GenericSetup',
        'setuptools',
        'zope.component',
        'zope.i18nmessageid',
        'zope.interface',
    ],
    extras_require={
        'test': [
            'plone.app.testing',
            'plone.app.contenttypes[test]',
            'plone.browserlayer',
            'unittest2',
            'ploneintranet.microblog',
            'plone.app.discussion',
        ],
    },
    entry_points="""
      # -*- Entry points: -*-
          [z3c.autoinclude.plugin]
          target = plone
      """,)
