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
# Copyright 2012 Ethan Zhang<http://github.com/Ethan-Zhang> 
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


define('prefix', default='~/workspace',
        help='install project files in [PREFIX]')
define('project', default='', help='project name, instead of twork')

ORI_PROJECT = 'twork'
ROOT_FILES  = ('.gitignore', 'AUTHORS', 'LICENSE', 'Makefile', 'setup.py')


def make_clean(src_path):
    os.chdir(os.path.join(src_path, ORI_PROJECT))
    args = shlex.split('make clean')
    try:
        p = subprocess.Popen(args)
        p.wait()
    except OSError as e:
        print 'COMMAND[make clean] ERROR: %s' % e

def make_git_repo(dst_path):
    os.chdir(os.path.join(dst_path, options.project))
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

%s is a neTwork server framework based on %s
''' % (options.project, options.project, ORI_PROJECT)
    
    dst_path = os.path.join(dst_path, options.project)

    with open('%s/README.md' % dst_path, 'w') as f:
        f.write(content.lstrip())

def main():
    options.parse_command_line()
    if not options.project:
        options.print_help()
        sys.exit()

    project_name = options.project
    src_path = os.path.normpath(os.path.join(os.path.abspath(sys.argv[0]),
        os.pardir))
    dst_path = os.path.expanduser(options.prefix)

    make_clean(src_path)

    shutil.copytree(os.path.join(src_path, ORI_PROJECT),
            os.path.join(dst_path, project_name, project_name))

    for file_name in ROOT_FILES:
        shutil.copyfile(os.path.join(src_path, file_name),
                os.path.join(dst_path, project_name, file_name))

    for root, dirs, files in os.walk(os.path.join(dst_path, project_name)):
        for name in files:
            if name.find(ORI_PROJECT) != -1:
                old_name = name
                name = name.replace(ORI_PROJECT, project_name)
                os.rename(os.path.join(root, old_name), 
                        os.path.join(root, name))

            if re.match(r'.+[py|md|Makefile]$|'+project_name, name):
                with open(os.path.join(root,name),"r+") as f:
                    d = f.read()
                    d = d.replace(ORI_PROJECT, project_name)
                    d = d.replace(ORI_PROJECT.upper(), project_name.upper())
                    d = d.replace('based on tornado',
                            'based on %s' % ORI_PROJECT)
                    d = d.replace('bufferx/%s' % project_name,
                            'bufferx/%s' % ORI_PROJECT)
                    f.truncate(0)
                    f.seek(0,0)
                    f.write(d)

    make_README(dst_path)
    make_git_repo(dst_path)

if __name__ == '__main__':
    main()
