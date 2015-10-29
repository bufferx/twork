#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''NotFoundHandler
'''

from tornado.web import HTTPError

from twork_app.web.action.base import BaseHandler


class NotFoundHandler(BaseHandler):
    '''NotFoundHandler, RESTFUL SUPPORTED.
    '''

    ST_ITEM = 'NOT_FOUND'

    def post(self, *args, **kwargs):
        raise HTTPError(404)

    def delete(self, *args, **kwargs):
        raise HTTPError(404)

    def get(self, *args, **kwargs):
        raise HTTPError(404)
