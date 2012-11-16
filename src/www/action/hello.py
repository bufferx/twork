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
localtion
----------
* /hello

feature
----------
* Process-level global variable
* Asynchronous HTTP request
* Decorator demo
'''

import os
import time

import tornado.web
from tornado.web import HTTPError
from tornado.httpclient import AsyncHTTPClient

from util import g_logger
from util import HttpUtil
from util import decorator as util_decorator

from base import BaseHandler 
from domain.object.error import ErrorCode as ECODE
from domain.object.error import BaseError

class HelloHandler(BaseHandler):
    @property
    def db(self):
        if __debug__:
            g_logger.debug('call property::db')
        return self.application.db

    @tornado.web.asynchronous
    def post(self):
        self.get()

    @tornado.web.asynchronous
    @util_decorator.validate_ip(_logger=g_logger)
    @util_decorator.time_it(g_logger)
    def get(self):
        try:
            #HttpUtil.validate_ip(self.request)
            # 只检查参数,不作业务逻辑处理
            self.name = self._check_argument('name', expect_types=(str, unicode))

            self.api_response({'e_code': ECODE.SUCCESS, 'e_msg': u'Hello, %s!' %
                    self.name})

            if __debug__:
                g_logger.debug(self.db)
                g_logger.debug(self._db)

            self.async_fetch()
        except HTTPError, e:
            g_logger.error(e, exc_info=True)
            return self.api_response({'e_code':ECODE.HTTP, 'e_msg': '%s' % e})
        except BaseError, e:
            g_logger.error(e, exc_info=True)
            return self.api_response({'e_code':e.e_code, 'e_msg': '%s' % e})
        except Exception, e:
            g_logger.error(e, exc_info=True)
            return self.api_response({'e_code':ECODE.DEFAULT, 'e_msg':
                'Unknown'})

    def async_fetch(self):
        request = tornado.httpclient.HTTPRequest(url='http://www.example.com',
                                                 method='GET',
                                                 connect_timeout=1,
                                                 request_timeout=5,
                                                 user_agent='TWORK-SPIDER',
                                                 )
        http_client = AsyncHTTPClient()
        http_client.fetch(request, self.__handle_async_request)

    def __handle_async_request(self, response):
        g_logger.debug('STACK_CONTEXT\tself.name=%s' % self.name)
        g_logger.debug('RESPONSE_ERROR\t%s' % response.error)
        g_logger.debug('RESPONSE\t%s' % response)
