from twork.web.action import StatHandler
from twork_app.web.action.health_check import HealthCheckHandler
from twork_app.web.action.not_found import NotFoundHandler


HANDLERS = [
        (r'/v1.0/twork_app/stats$', StatHandler, {'version': (1, 0)}),
        (r'/healthcheck.html$', HealthCheckHandler, {'version': (1, 0)}),
        (r"/(.*)$", NotFoundHandler, {'version': (1, 0)}),
        ]
