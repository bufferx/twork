from twork.web.action import StatHandler
from twork_app.web import action


HANDLERS = [
        (r'/v1.0/twork_app/stats$', StatHandler, {'version': (1, 0)})]
