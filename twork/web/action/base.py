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

from twork.util import g_logger

from twork.domain.object.error import ParameterEmptyError
from twork.domain.object.error import ParameterTypeError
from twork.domain.object.common import USER_AGENT

define("mcq", default=0, help = "Max Concurrency reQuests")


class BaseHandler(RequestHandler):

    ST_ITEM          = 'BASE'

    def initialize(self, version):
        self.VERSION = version
        self.USER_AGENT = '%s_%s' % (USER_AGENT, options.env.upper())

        if __debug__:
            g_logger.debug(self.request)

    @property
    def version(self):
        if not hasattr(self, '_version'):
            self._version = 'V%s' % ('.'.join(['%d' % i for i in self.VERSION]))
        return self._version

    def prepare(self):
        if self.application._requests >= options.mcq:
            g_logger.warning('Too Many Request: %d',
                    self.application._requests)
            self._mcq_error = True
            raise HTTPError(403)

        self.application._requests += 1

    def set_default_headers(self):
        self.set_header('Server', twork.SERVER_INFO)

    def on_connection_close(self):
        g_logger.debug('connection close.')

    def on_finish(self):
        if not hasattr(self, '_mcq_error'):
            self.application._requests -= 1

        self.application.update_handler_st(self.ST_ITEM,
                self.request.method, self.request.request_time())

    def finish(self, chunk=None):
        if not self.request.connection.stream.closed():
            RequestHandler.finish(self, chunk)

    def api_response(self, data):
        if not self._finished:
            self.finish(data)

    def _check_argument(self, parameter_name,
            default_value=None, expect_types=()):
        v = self.get_argument(parameter_name, default_value)
        if v is None:
            raise ParameterEmptyError(parameter_name)

        if expect_types and not isinstance(v, expect_types): 
            raise ParameterTypeError(parameter_name)
        return v
