all:
	@echo "do nothing"

.PHONY : clean
clean:
	cd ./twork/ && make clean
	rm -fr twork.egg-info build dist

build: clean
	python setup.py build_py -O2 bdist_egg --exclude-source-files

install: build
	python setup.py easy_install dist/*.egg
