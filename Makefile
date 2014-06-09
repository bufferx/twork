all:
	@echo "do nothing"

.PHONY : clean
clean:
	cd ./twork/ && make clean
	cd ./test/ && make clean
	rm -fr twork.egg-info build dist

build: clean
	python setup.py build_py bdist_egg

install: build
	python setup.py easy_install dist/*.egg

publish: clean
	python setup.py build_py bdist_egg upload -r pypi
