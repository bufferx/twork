"""Define URL HANDLERS here
"""

from twork.web.action import StatHandler

from twork_app.web.action.health_check import HealthCheckHandler
from twork_app.web.action.heartbeat import HeartBeatHandler
from twork_app.web.action.not_found import NotFoundHandler


HANDLERS = [
        # stats
        (r'^/v1.0/twork_app/stats$', StatHandler, {'version': (1, 0)}),
        # health check
        (r'^/healthcheck.html$', HealthCheckHandler, {'version': (1, 0)}),
        # heart beat
        (r'^/heartbeat.html$', HeartBeatHandler, {'version': (1, 0)}),
        # not found
        (r'^/(.*)$', NotFoundHandler, {'version': (1, 0)}),
        ]
