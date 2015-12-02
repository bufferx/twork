# encoding: utf-8

import requests
import time
import unittest

from twork_test_base import TworkTestCase


class TestHeartBeat(TworkTestCase):
    """Test For The Api Of HeartBeat 
    """

    def test_head_method(self):
        """Test For HTTP_HEAD Method
        """
        uri = '/heartbeat.html'
        url = 'http://%s%s' % (self.run_host, uri)
        payload = 'queryid=%.3f' % time.time()

        self.response = requests.get(url, params=payload, )

        self.assertEqual(self.response.status_code, 200)


if __name__ == '__main__':
    unittest.main()
