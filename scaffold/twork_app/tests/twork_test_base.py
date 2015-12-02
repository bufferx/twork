# encoding: utf-8

import os
import requests
import unittest

import twork_env


class TworkTestCase(unittest.TestCase):
    """UnitTestBase For TworkApp 
    """

    def setUp(self):
        env_mode = os.environ['PY_TEST_ENV_TWDEMO']
        self.run_env = twork_env.ENV[env_mode]
        self.run_host = self.run_env['twork_host']

    def tearDown(self):
        if hasattr(self, 'response'):
            self.response.close()


if __name__ == '__main__':
    unittest.main()
