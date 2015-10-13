all:
	@echo "do nothing"

clean:
	rm -f `find . -type f -name '*.py[co]' `
	rm -fr *.egg-info build dist

build: clean
	python setup.py build_py bdist_egg

install: build
	python setup.py easy_install dist/*.egg

publish: clean
	python setup.py register sdist upload -r pypi
