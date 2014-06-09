#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2014 Zhang ZY<https://github.com/bufferx> 
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


import os
import re
from tornado.options import define, options
import shutil
import shlex
import subprocess
import sys

import twork


define('prefix', default='~/workspace',
        help='install twork-app files in [PREFIX]')
define('app', default='', help='twork app name')
define('git_init', default=True, help='git initialize whether or not')

ORI_PROJECT = 'twork_app'


def make_clean(src_path):
    os.chdir(os.path.join(src_path, ORI_PROJECT))
    args = shlex.split('make clean')
    try:
        p = subprocess.Popen(args)
        p.wait()
    except OSError as e:
        print 'COMMAND[make clean] ERROR: %s' % e

def make_git_repo(dst_path):
    os.chdir(os.path.join(dst_path, options.app))
    args = shlex.split('git init')
    try:
        p = subprocess.Popen(args)
        p.wait()
    except OSError as e:
        print 'COMMAND[git init] ERROR: %s' % e

def make_README(dst_path):
    content = \
'''
%s
==========

%s runs as a twork module
''' % (options.app, options.app)
    
    dst_path = os.path.join(dst_path, options.app)

    with open('%s/README.md' % dst_path, 'w') as f:
        f.write(content.lstrip())

def main():
    options.parse_command_line()
    if not options.app:
        options.print_help()
        sys.exit()

    app_name = options.app
    src_path = os.path.realpath(
                os.path.join(twork.__path__[0],
                    '..',
                    'scaffold',
                    ))
    dst_path = os.path.expanduser(options.prefix)

    #make_clean(src_path)

    shutil.copytree(os.path.join(src_path, ORI_PROJECT),
            os.path.join(dst_path, app_name))

    rename_dirs = []
    for root, dirs, files in os.walk(os.path.join(dst_path, app_name)):
        for ori_name in dirs:
            if ORI_PROJECT in ori_name:
                dst_name = ori_name.replace(ORI_PROJECT, app_name)
                rename_dirs.append((os.path.join(root, ori_name),
                        os.path.join(root, dst_name)))

        for name in files:
            if '.pyc' in name:
                os.remove(os.path.realpath(os.path.join(root, name)))

            if re.match(r'.+[py|md|sh|Makefile]$|' + app_name, name):
                with open(os.path.join(root,name),"r+") as f:
                    d = f.read()
                    d = d.replace(ORI_PROJECT, app_name)
                    d = d.replace(ORI_PROJECT.upper(), app_name.upper())
                    f.truncate(0)
                    f.seek(0,0)
                    f.write(d)

    for dirs in reversed(rename_dirs):
        ori_name, dst_name = dirs
        os.rename(ori_name, dst_name)

    make_README(dst_path)
    make_git_repo(dst_path)

if __name__ == '__main__':
    main()
