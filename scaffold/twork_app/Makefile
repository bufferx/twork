all:
	@echo "do nothing"

clean:
	rm -f `find . -type f -name '*.py[co]' `
	rm -fr *.egg-info build dist

develop:
	python setup.py develop

build_egg: clean
	python setup.py build_py -O2 bdist_egg --exclude-source-files

install_egg: build_egg
	easy_install dist/*.egg

build: clean
	python setup.py build_py bdist_wheel
	cp Makefile dist

install: build
	pip install dist/*.whl -U

install_whl: install

deploy:
	pip install *.whl -U

uninstall:
	pip uninstall -y twork_app

publish_whl: clean
	python setup.py build_py bdist_wheel upload -r internal
	pip install dist/*.whl -U

publish:
	python setup.py build_py -O2 bdist_egg --exclude-source-files upload -r internal
	easy_install dist/*.egg

release-major:
	python setup.py release major

release-minor:
	python setup.py release minor

release-patch:
	python setup.py release patch

.PHONY : all clean build_egg install_egg local_install build install install_whl uninstall publish publish_whl release-major release-minor release-patch
