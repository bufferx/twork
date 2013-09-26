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

from pyutil.lib.tornado.options import define, options

define("v", default = False,
        help = "verbose, print debug info", type = bool)


# 创建记录器
g_logger = logging.getLogger()

def init_logger():
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
        _log_path = '%s/%s.access.log' % (options.log_path, options.app_name)
        _hand = logging.handlers.TimedRotatingFileHandler(_log_path, 'midnight', 1, 0)
        _hand.setLevel(logging.DEBUG)
        _hand.setFormatter(msg_formatter)

        try:
            logger.setLevel(getattr(logging, options.log_level.upper()))
        except AttributeError as e:
            logger.setLevel(logging.DEBUG)
            pass

        logger.addHandler(_hand)

    __init_root_logger()

def main():
    ''' main function
    '''

if __name__ == '__main__':
    main()
