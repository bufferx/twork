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

from pyutil.lib.tornado.options import options

# 设置消息格式
msg_formatter = logging.Formatter('%(asctime)s - %(name)s - \
%(levelname)s - %(module)s.%(funcName)s:%(lineno)d - %(process)d - %(thread)d - %(message)s', '') 

# 创建处理器
_log_path = '%s/%s.Main.log' % (options.log_path, options.app_name)
_hand = logging.handlers.TimedRotatingFileHandler(_log_path, 'midnight', 1, 0)
_hand.setLevel(logging.DEBUG)
_hand.setFormatter(msg_formatter)

# 创建记录器
g_logger = logging.getLogger()

try:
    g_logger.setLevel(getattr(logging, options.log_level.upper()))
except AttributeError as e:
    g_logger.setLevel(logging.DEBUG)
    pass

g_logger.addHandler(_hand)

def main():
    ''' main function
    '''

if __name__ == '__main__':
    main()
