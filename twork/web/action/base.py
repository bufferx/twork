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

from util import g_logger
from util import HttpUtil
from util import decorator as util_decorator

from domain.object.error import ParameterEmptyError
from domain.object.error import ParameterTypeError

class BaseHandler(RequestHandler):

    HTTP_SERVER_NAME = 'ZWS/1.0'

    def initialize(self, version):
        self.version = version
        if __debug__:
            g_logger.debug(HttpUtil.get_header_string(self.request))

    def set_default_headers(self):
        self.set_header('Server', BaseHandler.HTTP_SERVER_NAME)

    def on_connection_close(self):
        g_logger.info('connection close.')

    def on_finish(self):
        '''Require: tornado.version > 2.1.1
        '''
        request_time = 1000.0 * self.request.request_time()
        g_logger.info("%d %s %.2fms", self.get_status(),
                   self._request_summary(), request_time)

    def finish(self, chunk=None):
        if not self.request.connection.stream.closed():
            RequestHandler.finish(self, chunk)

    def api_response(self, data):
        if not self._finished:
            self.finish(data)

    @util_decorator.time_it(_logger=g_logger)
    def _check_argument(self, parameter_name,
            default_value=None, expect_types=()):
        v = self.get_argument(parameter_name, default_value)
        if v is None:
            raise ParameterEmptyError(parameter_name)

        if expect_types and not isinstance(v, expect_types): 
            raise ParameterTypeError(parameter_name)
        return v
