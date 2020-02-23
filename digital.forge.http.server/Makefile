include $(shell pipenv --where)/tools/make/common.mk

PROJECT = digital.forge.http.server

.PHONY = clean

all: dist

dist: README.md src setup.json setup.py
	$(PYTHON) setup.py bdist_wheel
clean-dist:
	$(RM) -r build
	$(RM) -r dist
	$(RM) -r src/$(PROJECT).egg-info

clean: clean-dist
