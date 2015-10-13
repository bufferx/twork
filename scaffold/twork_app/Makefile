all:
	@echo "do nothing"

.PHONY : clean
clean:
	rm -f `find . -type f -name '*.py[co]' `
	rm -fr *.egg-info build dist

build: clean
	python setup.py build_py bdist_egg --exclude-source-files

install: build
	python setup.py easy_install dist/*.egg

publish: clean
	python setup.py build_py -O2 bdist_egg --exclude-source-files upload -r internal
	python setup.py easy_install dist/*.egg
