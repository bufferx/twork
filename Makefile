all:
	@echo "do nothing"

clean:
	rm -f `find . -type f -name '*.py[co]' `
	rm -fr *.egg-info build dist

build_egg: clean
	python setup.py build_py -O2 bdist_egg --exclude-source-files

install_egg: build_egg
	easy_install dist/*.egg

local_install: install_egg

build: clean
	python setup.py build_py bdist_wheel

install: build
	pip install dist/*.whl -U

uninstall:
	pip uninstall -y twork

publish: clean
	python setup.py build_py bdist_wheel upload -r pypi
