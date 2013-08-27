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
import sys
# Importing setuptools adds some features like "setup.py develop", but
# it's optional so swallow the error if it's not there.
try:
    import setuptools
except ImportError:
    pass

kwargs = {}

major, minor = sys.version_info[:2]
python_26 = (major > 2 or (major == 2 and minor >= 6))

version = "1.0.0"

if major >= 3:
    import setuptools  # setuptools is required for use_2to3
    kwargs["use_2to3"] = True

distutils.core.setup(
    name="twork",
    version=version,
    author="Zhang ZY",
    author_email="idup2x@gmail.com",
    url="https://github.com/bufferx/twork",
    license="http://www.apache.org/licenses/LICENSE-2.0",
    description="twork is a network server framework based on tornado",
    packages = setuptools.find_packages(exclude=["test", "*.log"]),
    package_data = {
        "twork": ["www/static/favicon.ico"],
    },
    entry_points = {
     'console_scripts': [
         'tworkd = twork.bin.tworkd:main',
         ],
      },
    **kwargs
)
