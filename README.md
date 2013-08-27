twork
==========

twork is a network server skeleton based on tornado

Environment
------------
* [virtualenv](http://www.virtualenv.org/en/latest/)

Requirements
------------
The following libraries are required

* [tornado](http://github.com/facebook/tornado)
* [pyutil](https://github.com/bufferx/pyutil)

Usage & Debug
------------
* source $VIRTUALENV/bin/activate
* cd $TORNADO_PATH && python setup.py install
* cd $PYUTIL_PATH && python setup.py install
* python twork/bin/tworkd.py -bind_ip=localhost -port=8000

Deploy
------------
* source $VIRTUALENV/bin/activate
* cd $TORNADO_PATH && python setup.py install
* cd $PYUTIL_PATH && python setup.py install
* python setup.py build_py -O2 bdist_egg --exclude-source-files
* easy_install dist/twork-VERSION-PYTHON.egg

Supervisor
------------
* [supervisord](http://supervisord.org/)
* [conf-template](https://github.com/bufferx/supervisor_conf_tpl)
* command: python -OO $VIRTUALENV/bin/tworkd -bind_ip=localhost -port=8000

Case
------------
* http://localhost:8000/sayhi?name=bufferx

Issues
------

Please report any issues via [github issues](https://github.com/bufferx/twork/issues)
