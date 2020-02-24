include $(shell pipenv --where)/tools/make/common.mk

PROJECT = digital.forge.data.server

OPENAPI_JAR = C:\dev\bin\OpenAPI\openapi-generator-cli-4.2.3.jar

.PHONY = clean

all: src dist dist-test

src:
	java -jar $(OPENAPI_JAR) generate -g python-flask -i ../conductor-api.yaml -c config/codegen-config.json -t config/templates -o src
	$(RM) src/digital/forge/data/server/__init__.py
clean-src:
	$(RM) -r src

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

clean: clean-src clean-dist clean-dist-test
