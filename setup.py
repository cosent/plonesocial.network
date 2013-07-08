from setuptools import setup, find_packages

version = '0.5.1'

long_description = (
    open('README.rst').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(
    name='plonesocial.network',
    version=version,
    description="Personal profile + follow/unfollow functionality "
    "for the Plonesocial suite",
    long_description=long_description,
    # Get more strings from
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=["Programming Language :: Python", ],
    keywords='plone, zope, socbiz, plonesocial',
    author='Guido Stevens',
    author_email='guido.stevens@cosent.net',
    url='http://github.com/cosent/plonesocial.network',
    license='gpl',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['plonesocial'],
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools',
                      'Plone',
                      # -*- Extra requirements: -*-
                      ],
    extras_require={'test': ['plone.app.testing']},
    entry_points="""
      # -*- Entry points: -*-
          [z3c.autoinclude.plugin]
          target = plone
      """,)
