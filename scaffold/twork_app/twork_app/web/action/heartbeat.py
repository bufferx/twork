#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''HeartBeatHandler
'''

from tornado.web import HTTPError

from twork_app.constants import ST_ITEM_HEARTBEAT
from twork_app.web.action.base import BaseHandler


class HeartBeatHandler(BaseHandler):
    '''HeartBeatHandler, RESTFUL SUPPORTED.
    '''

    ST_ITEM = ST_ITEM_HEARTBEAT

    def post(self, *args, **kwargs):
        raise HTTPError(405)

    def put(self, *args, **kwargs):
        raise HTTPError(405)

    def delete(self, *args, **kwargs):
        raise HTTPError(405)

    def head(self, *args, **kwargs):
        pass

    def get(self, *args, **kwargs):
        self.api_response('It works!')
