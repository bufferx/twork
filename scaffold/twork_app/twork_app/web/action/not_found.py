#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''NotFoundHandler
'''

from tornado.web import HTTPError

from twork_app.constants import ST_ITEM_NOTFOUND
from twork_app.web.action.base import BaseHandler


class NotFoundHandler(BaseHandler):
    '''NotFoundHandler, RESTFUL SUPPORTED.
    '''

    ST_ITEM = ST_ITEM_NOTFOUND

    def post(self, *args, **kwargs):
        raise HTTPError(404)

    def put(self, *args, **kwargs):
        raise HTTPError(404)

    def delete(self, *args, **kwargs):
        raise HTTPError(404)

    def head(self, *args, **kwargs):
        raise HTTPError(404)

    def get(self, *args, **kwargs):
        raise HTTPError(404)
