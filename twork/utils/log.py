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

'''日志
'''

import logging
import logging.handlers
import logging.config

import os

from tornado.options import define, options

from twork import assembly


define('v', default=False,
        help='Verbose, Print Debug Info', type=bool)
define('log_level', default='DEBUG',
        help="Set Log Level")
define('log_root', default=assembly.PROJECT_PATH,
        help='Log File Stored Root Path')


# 创建记录器
gen_logger = logging.getLogger('twork.general')
access_logger = logging.getLogger('twork.access')

def _mkdir(file_dir):
    real_path = os.path.realpath(file_dir)
    if not os.path.exists(real_path):
        os.makedirs(real_path)
        pass

def setup_log():
    def __init_root_logger():
        logger = logging.getLogger()

        # 设置消息格式
        if options.v:
            msg_formatter = logging.Formatter('%(asctime)s - %(name)s - \
%(levelname)1.1s - %(module)s.%(funcName)s:%(lineno)d - %(process)d - \
%(thread)d - %(message)s',
                    '%Y-%m-%d %H:%M:%S')
        else:
            msg_formatter = logging.Formatter('%(asctime)s - %(levelname)1.1s - \
%(module)s:%(lineno)d - %(message)s',
                    '%Y-%m-%d %H:%M:%S')

        # 创建处理器
        _log_path = '%s/twork.access.log' % log_path
        _hand = logging.handlers.TimedRotatingFileHandler(_log_path, 'midnight', 1, 0)
        _hand.setLevel(logging.DEBUG)
        _hand.setFormatter(msg_formatter)

        try:
            logger.setLevel(getattr(logging, options.log_level.upper()))
        except AttributeError as e:
            logger.setLevel(logging.DEBUG)
            pass

        logger.addHandler(_hand)

    def __init_biz_logger():
        biz_logger = logging.getLogger('twork.biz')

        # 设置消息格式
        if options.v:
            msg_formatter = logging.Formatter('%(asctime)s\t%(version)s\t\
%(module)s:%(lineno)d\t%(message)s',
                    '%Y-%m-%d %H:%M:%S')
        else:
            biz_logger.propagate = False
            msg_formatter = logging.Formatter('%(asctime)s\t%(version)s\t\
%(message)s',
                    '%Y-%m-%d %H:%M:%S')

        # 创建处理器
        _log_path = '%s/twork.biz.log' % log_path
        _hand = logging.handlers.TimedRotatingFileHandler(_log_path, 'midnight', 1, 0)
        _hand.setLevel(logging.DEBUG)
        _hand.setFormatter(msg_formatter)

        try:
            biz_logger.setLevel(getattr(logging, options.log_level.upper()))
        except AttributeError as e:
            biz_logger.setLevel(logging.DEBUG)

        biz_logger.addHandler(_hand)

    if os.path.exists(options.log_config):
        logging.config.fileConfig(options.log_config)
        return

    log_path = '%s/log' % (options.log_root)
    _mkdir(log_path)
    __init_root_logger()
    __init_biz_logger()


def main():
    ''' main function
    '''

if __name__ == '__main__':
    main()
