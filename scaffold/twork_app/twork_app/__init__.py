#__import__('pkg_resources').declare_namespace(__name__)

from twork_app.version import __VERSION__

version_info = __VERSION__.split('.')
APP_NAME  = 'twork_app'
APP_INFO  = '%s/%s' % (APP_NAME, __VERSION__)
