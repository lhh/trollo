#!/usr/bin/env python
# Copyright (c) 2012, Fog Creek Software, Inc.
# Copyright (c) 2016-2018, Red Hat, Inc.
#   License: 2-clause BSD; see LICENSE.txt for details
import setuptools
import re

from textwrap import dedent
from trollo import __version__


def requires(prefix=''):
    """Retrieve requirements from requirements.txt
    """
    try:
        reqs = map(str.strip, open(prefix + 'requirements.txt').readlines())
        return [req for req in reqs if not re.match(r'\W', req)]
    except Exception:
        pass
    return []


setuptools.setup(
    name='trollo',
    version=__version__,
    install_requires=requires(),
    license='BSD',
    long_description=dedent("""\
        Python Trello API Wrapper
        --------------------------
        This Python API is simply a wrapper around the Trello API.

        Getting Started:
        ----------------
        To use the Trello API, install the package either by downloading the source and running

          $ python setup.py install

        or by using pip

          $ pip install trollo

        Documentation:
        --------------
        You can find documentation for the Python API at:

            http://pypi.org/project/trollo/

        And documentation for the Trello API at:

            https://developers.trello.com/reference/

        """),
    author='Red Hat',
    author_email='lhh@redhat.com',
    maintainer='Lon Hohberger',
    maintainer_email='lon@metamorphism.com',
    packages=['trollo'],
    url='http://github.com/lhh/trollo',
    data_files=[("", ["LICENSE.txt"])],
    classifiers=['Development Status :: 4 - Beta',
                 'Intended Audience :: Developers',
                 'Natural Language :: English',
                 'Operating System :: MacOS :: MacOS X',
                 'Operating System :: Microsoft :: Windows',
                 'Operating System :: POSIX',
                 'Operating System :: POSIX :: BSD',
                 'Operating System :: POSIX :: Linux',
                 'Programming Language :: Python',
                 'Topic :: Internet :: WWW/HTTP',
                 'Topic :: Software Development',
                 'Topic :: Software Development :: Libraries',
                 'Topic :: Software Development :: Libraries :: Python Modules',
                 'Topic :: Utilities'],
)
