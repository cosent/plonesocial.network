# convenience makefile to boostrap & run buildout
# use `make options=-v` to run buildout with extra options

options = -N -q -t 3

prerequisites:
	sudo apt-get install -qq pep8 pyflakes
	mkdir -p buildout-cache/downloads

install: prerequisites
	python bootstrap.py -c travis.cfg
	bin/buildout -c travis.cfg $(options)

tests:
	bin/test
	pyflakes plonesocial/
	pep8 plonesocial/
