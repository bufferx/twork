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

'''
/hello, HelloWorld :) 
'''

import os
import time

import tornado.web
from tornado.web import HTTPError

from util import g_logger
from util import HttpUtil

from base import BaseHandler 
from domain.object.error import ErrorCode as ECODE
from domain.object.error import BaseError

class HelloHandler(BaseHandler):

    @tornado.web.asynchronous
    def post(self):
        self.get()

    @tornado.web.asynchronous
    def get(self):
        try:
            HttpUtil.validate_ip(self.request)

            # 只检查参数,不作业务逻辑处理
            self.name = self._check_argument('name', None, str)
            if not self.name: return

            self.api_response({'e_code': ECODE.SUCCESS, 'e_msg': 'Hello, %s!' %
                    self.name})

        except HTTPError, e:
            g_logger.error(e)
            return self.api_response({'e_code':ECODE.HTTP, 'e_msg': '%s' % e})
        except BaseError, e:
            g_logger.error(e)
            return self.api_response({'e_code':e.e_code, 'e_msg': '%s' % e})
        except Exception, e:
            g_logger.error(e)
            return self.api_response({'e_code':ECODE.DEFAULT, 'e_msg':
                'Unknown'})
