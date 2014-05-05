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
* /asyncread

feature
----------
* Process-level global variable
* Asynchronous Read 
* Decorator Demo
'''

import os
import time

import tornado.web
from tornado.web import HTTPError
from tornado.httpclient import AsyncHTTPClient
from tornado import gen

from util import g_logger

from base import BaseHandler 
from errors import ErrorCode as ECODE
from errors import BaseError

class AsyncReadHandler(BaseHandler):

    @tornado.web.asynchronous
    @gen.engine
    def get(self):
        self.name = self._check_argument('name', expect_types=(str, unicode))

        urlist = ['http://www.example.com', 'http://www.google.com']

        try:
            for url in urlist:
                request = tornado.httpclient.HTTPRequest(url,
                                                         method='GET',
                                                         connect_timeout=1,
                                                         request_timeout=5,
                                                         user_agent='TWORK-SPIDER',
                                                         )
                http_client = AsyncHTTPClient()

                response = yield gen.Task(http_client.fetch, request)
                result = self.__handle_async_request(response)
                self.finish(result)
                break
            else:
                self.finish({'e_code':ECODE.HTTP, 'e_msg': 'SUCCESS'})
            pass
        except HTTPError, e:
            g_logger.error(e, exc_info=True)
            self.api_response({'e_code':ECODE.HTTP, 'e_msg': '%s' % e})
            raise StopIteration
        except BaseError, e:
            g_logger.error(e, exc_info=True)
            self.api_response({'e_code':e.e_code, 'e_msg': '%s' % e})
            raise StopIteration
        except Exception, e:
            g_logger.error(e, exc_info=True)
            self.api_response({'e_code':e.e_code, 'e_msg': '%s' % e})
            raise StopIteration

    def __handle_async_request(self, response):
        if response is None:
            return None
        #g_logger.debug('STACK_CONTEXT\tself.name=%s' % self.name)
        g_logger.debug('RESPONSE_ERROR\t%s' % response.error)
        g_logger.debug('RESPONSE\t%s' % response)

        return response.body
