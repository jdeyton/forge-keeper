include $(shell pipenv --where)/tools/make/common.mk

PROJECT = digital.forge.http.server.decorator.sqlalchemy

.PHONY = clean

all: dist dist-test

dist: README.md src setup.json setup.py
	$(PYTHON) setup.py bdist_wheel
	$(RM) -r build
	$(RM) -r src/$(PROJECT).egg-info
clean-dist:
	$(RM) -r dist

dist-test: dist setup_test.py
	$(PYTHON) setup_test.py bdist_wheel -d dist-test
	$(RM) -r build
	$(RM) -r src/$(PROJECT).test.egg-info
clean-dist-test:
	$(RM) -r dist-test

clean: clean-dist clean-dist-test
