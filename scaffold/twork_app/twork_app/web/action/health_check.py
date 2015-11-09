#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''HealthCheckHandler
'''

import logging

from tornado.options import options
from tornado.web import HTTPError

from twork.utils.common import check_file_exists

from twork_app.constants import ST_ITEM_HEALTHCHECK
from twork_app.web.action.base import BaseHandler


gen_logger = logging.getLogger('twork.general')


class HealthCheckHandler(BaseHandler):
    '''HealthCheckHandler, RESTFUL SUPPORTED.
    '''

    ST_ITEM = ST_ITEM_HEALTHCHECK

    def post(self, *args, **kwargs):
        raise HTTPError(405)

    def put(self, *args, **kwargs):
        raise HTTPError(405)

    def delete(self, *args, **kwargs):
        raise HTTPError(405)

    def head(self, *args, **kwargs):
        if not check_file_exists(options.healthcheck_file_path):
            gen_logger.warn('%s does not exists',
                    options.healthcheck_file_path)
            raise HTTPError(404)

    def get(self, *args, **kwargs):
        if not check_file_exists(options.healthcheck_file_path):
            gen_logger.warn('%s does not exists',
                    options.healthcheck_file_path)
            raise HTTPError(404)

        self.api_response('It works!')
