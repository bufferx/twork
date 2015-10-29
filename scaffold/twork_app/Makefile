all:
	@echo "do nothing"

clean:
	rm -f `find . -type f -name '*.py[co]' `
	rm -fr *.egg-info build dist

build: clean
	python setup.py build_py bdist_egg --exclude-source-files

install: build
	python setup.py easy_install dist/*.egg

publish: clean
	python setup.py build_py bdist_egg --exclude-source-files upload -r internal
	python setup.py easy_install dist/*.egg

release-major:
	python setup.py release major

release-minor:
	python setup.py release minor

release-patch:
	python setup.py release patch

.PHONY : all clean build install publish release-major release-minor release-patch
