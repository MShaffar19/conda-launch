#!/usr/bin/env python
# (c) 2012-2014 Continuum Analytics, Inc. / http://continuum.io
# All Rights Reserved
#
# conda is distributed under the terms of the BSD 3-clause license.
# Consult LICENSE.txt or http://opensource.org/licenses/BSD-3-Clause.

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import versioneer

versioneer.tag_prefix = ''
versioneer.parentdir_prefix = 'conda-launch-'

setup(
    name                = "conda-launch",
    version             = "0.2",
    author              = "Continuum Analytics, Inc.",
    author_email        = "ijstokes@continuum.io",
    url                 = "https://github.com/conda/conda-launch",
    license             = "BSD",
    description         = "appify ipython notebooks",
    long_description    = open('README.md').read(),
    packages            = ['ipyapp'],
    include_package_data= True,
    package_data        = {
            'ipyapp': ['static/*', 'templates/*'],
    },
    zip_safe            = False,
    install_requires    = ['ipython', 'runipy', 'flask', 'requests',
                           'psutil', 'conda-api', 'six'],

    scripts = ['bin/conda-appserver',
               'bin/conda-launch'],

    classifiers = [
        "Development Status :: 4 - Beta",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
)
