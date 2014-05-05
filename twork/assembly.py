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

''' set classpath
'''

import os
import sys

CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))
PROJECT_PATH = os.path.realpath(os.path.join(CURRENT_PATH, '..'))

if PROJECT_PATH not in sys.path:
    sys.path.insert(0, PROJECT_PATH)

def main():
    print 'CURRENT_PATH:', CURRENT_PATH
    print 'PROJECT_PATH:', PROJECT_PATH

if __name__ == '__main__':
    main()
