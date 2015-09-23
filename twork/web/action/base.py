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

'''BaseRequestHandler 
'''

from tornado.web import RequestHandler
from tornado.web import HTTPError
from tornado.options import define, options

import twork

from twork.utils import gen_logger, access_logger

from twork.errors import (BaseError, ArgumentEmptyError, ArgumentTypeError)
from twork.consts import USER_AGENT

define("max_requests", default=0, help="Max Concurrency Requests")


class BaseHandler(RequestHandler):

    ST_ITEM          = 'BASE'

    def initialize(self, version):
        self.VERSION = version
        self.USER_AGENT = '%s_%s' % (USER_AGENT, options.env.upper())

    @property
    def version(self):
        if not hasattr(self, '_version'):
            self._version = 'V%s' % ('.'.join(['%d' % i for i in self.VERSION]))

        return self._version

    def prepare(self):
        if options.max_requests and \
            self.application._requests >= options.max_requests:
            gen_logger.warning('Too Many Request: %d',
                             self.application._requests)
            self._max_requests = True
            raise HTTPError(429)

        self.application._requests += 1

    def set_default_headers(self):
        self.set_header('Server', twork.SERVER_INFO)
        self.set_header('TworkApp', self.application.APP_INFO)

    def on_finish(self):
        if not hasattr(self, '_max_requests'):
            self.application._requests -= 1

        self.application.update_handler_st(self.ST_ITEM,
                self.request.method, self.request.request_time())

    def finish(self, chunk=None):
        if not self.request.connection.stream.closed():
            RequestHandler.finish(self, chunk)
            access_logger.info('',
                               extra={'version': 'V' + twork.version,
                                      'status': self.get_status(),
                                      'method': self.request.method,
                                      'remoteip': self.request.remote_ip,
                                      'uri': self.request.uri,
                                      'rt': '%.6f' % self.request.request_time()})

    def api_response(self, data):
        if not self._finished:
            self.finish(data)

    def _check_argument(self, argument_name,
            default_value=None, expect_types=()):
        v = self.get_argument(argument_name, default_value)

        if v is None:
            raise ArgumentEmptyError(argument_name)

        if expect_types and not isinstance(v, expect_types): 
            raise ArgumentTypeError(argument_name)

        return v

    def init_rsp_json(self):
        self.rsp_json = {'code': BaseError.ERROR[0],
                        'msg': BaseError.ERROR[1],
                        'data': {}}
