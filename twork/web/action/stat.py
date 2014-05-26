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

"""Stats Interface
"""

from twork.errors import ErrorCode as ECODE
from twork.errors import ErrorMessage as EMSG
from twork.errors import BaseError

from twork.utils import gen_logger

from twork.web.action.base import BaseHandler


class StatHandler(BaseHandler):
    """Stats Handler
    """

    ST_ITEM          = 'STATS'

    def get(self):
        result = {'code': ECODE.SUCCESS, 'msg': EMSG.SUCCESS}
        result['data'] = {}

        try:
            result['datas'] = self.application.stat_info
        except Exception as e:
            gen_logger.error(e, exc_info=True if __debug__ else False)
            result['code'] = ECODE.DEFAULT
            result['msg']  = EMSG.DEFAULT
        finally:
            self.api_response(result)
