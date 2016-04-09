#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2012 Zhang ZY<http://idupx.blogspot.com/> 
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# Copyright 2009 Facebook
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import distutils.core
import os
import sys
# Importing setuptools adds some features like "setup.py develop", but
# it's optional so swallow the error if it's not there.
try:
    import setuptools
except ImportError:
    pass

import twork

kwargs = {}

major, minor = sys.version_info[:2]
python_26 = (major > 2 or (major == 2 and minor >= 6))

if major >= 3:
    import setuptools  # setuptools is required for use_2to3
    kwargs["use_2to3"] = True

distutils.core.setup(
    name="twork",
    version=twork.version,
    long_description=open(os.path.join(os.path.dirname(__file__),
                                         'README.rst')).read(),
    platforms=['POSIX'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
    ],
    keywords=['tornado',
              'web framework',
              'web server',
              'server framework',
              'twork'],
    author="ZY Zhang",
    author_email="idup2x@gmail.com",
    url="https://github.com/bufferx/twork",
    license="http://www.apache.org/licenses/LICENSE-2.0",
    description=("twork is a Tornado Application FrameWork, "
                 "it supports plug-in module injection, "
                 "the module called TworkApp."
                 ),
    packages = setuptools.find_packages(exclude=["test", "*.log"]),
    package_data = {
        "twork": ["web/static/favicon.ico"],
        "scaffold": [
            "twork_app/setup.py",
            "twork_app/tox.ini",
            "twork_app/Makefile",
            "twork_app/.bumpversion.cfg",
            "twork_app/.gitignore",
            "twork_app/tests/*.py",
            "twork_app/twork_app/*.py",
            "twork_app/twork_app/app/*.py",
            "twork_app/twork_app/domain/*.py",
            "twork_app/twork_app/domain/bs/*.py",
            "twork_app/twork_app/domain/dao/*.py",
            "twork_app/twork_app/domain/model/*.py",
            "twork_app/twork_app/libs/__init__.py",
            "twork_app/twork_app/utils/__init__.py",
            "twork_app/twork_app/web/*.py",
            "twork_app/twork_app/web/action/*.py",
            "twork_app/twork_app/web/static/favicon.ico",
            "twork_app/twork_app/web/templates/README.md",
            "twork_app/conf/twork.conf",
            "twork_app/conf/log.conf",
            ],
    },
    scripts=["script/cut_twork_log.sh", "script/kill_tworkd.sh",
        "script/reopen_twork_log.sh",],
    entry_points = {
     'console_scripts': [
         'tworkd = twork.tworkd:main',
         'twork-admin = scaffold.twork_admin:main',
         ],
      },
    install_requires=['setproctitle==1.1.8', 'nose==1.3.3', 'tornado==4.2.1',
            'psutil==3.2.2',
            ],
    **kwargs
)
