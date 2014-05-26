import unittest

from twork import utils
from twork.web.server import TApplication


@utils.common.singleton
class _Base(object):
    pass


class Base(object):
    pass


class Derived(Base):
    pass


class WebApplication(TApplication):
    pass


class SingletonTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_singleton(self):
        assert WebApplication.instance() is not None
        assert _Base() is _Base()
        assert Derived() is not Derived()
