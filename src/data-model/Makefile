PROJECT_ROOT ?= $(shell git rev-parse --show-toplevel)
include $(PROJECT_ROOT)/tools/make/common.mk
include $(PROJECT_ROOT)/tools/make/openapi.mk
include $(PROJECT_ROOT)/tools/make/python.mk

# Make the dist folder a default target.
all: dist
clean: clean-dist

# ---- Code generation ---- #

# Source code:
# This uses the relatively complete model from the python-flask generator.
.codegen-src:
	$(CP) cfg/src/.openapi-generator-ignore src/
	$(OPENAPI_CLI) generate -g python-flask -i ../data.json -o src -c cfg/codegen.json -t cfg/src/templates
	$(RMDIR) src/digital/forge/data/controllers
	$(RMDIR) src/digital/forge/data/openapi
	$(RMDIR) src/digital/forge/data/test
	$(TOUCH) .codegen-src

# Test code:
# This uses the python generator to get test files for the model.
.codegen-tests:
	$(CP) cfg/tests/.openapi-generator-ignore src/
	$(OPENAPI_CLI) generate -g python -i ../data.json -o src -c cfg/codegen.json -t cfg/tests/templates
	$(RMDIR) src/digital/forge/data/api
	$(TOUCH) .codegen-tests

# Targets for the above.
.codegen: .codegen-src .codegen-tests
	$(TOUCH) .codegen
clean-codegen:
	$(RM) .codegen-src
	$(RM) .codegen-tests
	$(RM) .codegen

# Can't build wheels without the source!
dist: .codegen
