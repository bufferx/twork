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


import functools
import logging
import os
import time

from itertools import izip

from tornado.escape import (utf8, url_unescape)

from twork.utils.object_likefy import ObjectLikefy

gen_logger = logging.getLogger('twork.general')

log_time = lambda f, t: 'Function[%s] Consume %.3fms' % (f, (time.time() - t) * 1000)


def time_it(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()

        r = func(*args, **kwargs)
        gen_logger.info('%s\t%s\t%s', args, kwargs,
                log_time(func.__name__, start_time),
                extra={'version': 'v1.0'})
        return r
    return wrapper


def singleton(cls, *args, **kw):
    """Make Class Single
    """
    instance = {}
    def _singleton():
        if cls not in instance:
            instance[cls] = cls(*args, **kw)
        return instance[cls]
    return _singleton


def define_process_title(proc_title='twork'):
    """Define Custom Process Title
    """
    try:
        import setproctitle
        setproctitle.setproctitle(proc_title)
    except ImportError as e:
        gen_logger.error(e)


def parse_web_input(inner_arguments, input_arguments,
        check_argument_func, object_likefy=True):
    """Transform Web Input Request To Inner Variable
    """
    def _convert(v):
        if v is None:
            return None

        return utf8(url_unescape(v))

    argu_values = []
    for argument in input_arguments:
        value = check_argument_func(argument, None)
        argu_values.append(value)

    res = dict(izip(inner_arguments,
                    (_convert(v) for v in argu_values)))

    if object_likefy:
        res = ObjectLikefy(res)

    return res


def check_file_exists(file_path):
    """Check Whether The Specified File Exists
    """
    real_path = os.path.realpath(file_path)
    if os.path.exists(real_path):
        return True
    return False
