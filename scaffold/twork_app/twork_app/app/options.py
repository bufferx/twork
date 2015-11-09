"""Define tornado options here
"""

from tornado.options import define


define("healthcheck_file_path", default='/var/www/healthcheck.html', type=str,
        help="HealthCheck File Path")
