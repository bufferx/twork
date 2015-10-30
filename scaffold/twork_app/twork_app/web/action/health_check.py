#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''HealthCheckHandler
'''

from tornado.web import HTTPError

from twork_app.web.action.base import BaseHandler


class HealthCheckHandler(BaseHandler):
    '''HealthCheckHandler, RESTFUL SUPPORTED.
    '''

    ST_ITEM = 'HEALTH_CHECK'

    def post(self, *args, **kwargs):
        raise HTTPError(405)

    def put(self, *args, **kwargs):
        raise HTTPError(405)

    def delete(self, *args, **kwargs):
        raise HTTPError(405)

    def get(self, *args, **kwargs):
        self.api_response('It works!')
