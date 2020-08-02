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
.codegen-src: .venv
	$(MKDIR) cfg/src/templates
	$(CP) cfg/src/.openapi-generator-ignore src/
	$(OPENAPI_CLI) generate -g python -i ../data.json -o src -c cfg/codegen.json -t cfg/src/templates
	$(RMDIR) src/digital/forge/data/models
	$(RM) src/.openapi-generator-ignore
	$(POETRY) run autoflake --in-place --recursive --remove-all-unused-imports --ignore-init-module-imports src/digital
	$(TOUCH) .codegen-src

# Test code:
# This uses the python generator to get test files for the model.
.codegen-tests: .venv
	$(MKDIR) cfg/tests/templates
	$(CP) cfg/tests/.openapi-generator-ignore src/
	$(OPENAPI_CLI) generate -g python -i ../data.json -o src -c cfg/codegen.json -t cfg/tests/templates
	$(RMDIR) src/digital/forge/data/models
	$(RM) src/.openapi-generator-ignore
	$(POETRY) run autoflake --in-place --recursive --remove-all-unused-imports src/test
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
