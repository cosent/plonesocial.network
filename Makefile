default: buildout test

buildout: bin/buildout
	bin/buildout -c buildout.cfg -N -t 3

test:
	bin/test
	bin/flake8 plonesocial

bin/buildout: bin/python buildout-cache/downloads
	bin/python bootstrap.py -v 2.2.1

bin/python:
	virtualenv --clear --no-site-packages --setuptools --python=python2.7 .

buildout-cache/downloads:
	[ -d buildout-cache ] || mkdir -p buildout-cache/downloads

clean:
	rm -rf bin/* .installed.cfg parts/download

