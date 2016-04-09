#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''BaseHandler
'''

import logging
import time

from twork.errors import (ArgumentNotFoundError,
                          ArgumentTypeError,
                          ArgumentEmptyError,
                          )

from twork.utils.common import parse_web_input

from twork.web.action.base import BaseHandler as TBaseHandler

from twork_app.domain.bs.base import BaseBS


gen_logger = logging.getLogger('twork.general')


class BaseHandler(TBaseHandler):
    '''BaseHandler, RESTFUL SUPPORTED.
    '''

    ST_ITEM = 'TWORKAPP_BASE'

    def get(self, *args, **kwargs):
        """Process GET Method
        """
        input = self._init_input()

        action = BaseBS(input, rsp_json=self.rsp_json)
        action.execute()

    def post(self, *args, **kwargs):
        """Process POST Method
        """
        self._init_input()

    def put(self, *args, **kwargs):
        """Process PUT Method
        """
        self._init_input()

    def delete(self, *args, **kwargs):
        """Process DELETE Method
        """
        self._init_input()

    def _init_input(self):
        """Initialize And Convert WebInput Argument To Inner Argument
        """
        input = parse_web_input(BaseBS.INNER_ARGUMENTS,
                                BaseBS.INPUT_ARGUMENTS,
                                self.get_argument)
        if input.query_id is None:
            input.query_id = '%.6f' % time.time()

        return input
