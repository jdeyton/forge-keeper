PROJECT_ROOT ?= $(shell git rev-parse --show-toplevel)
include $(PROJECT_ROOT)/tools/make/common.mk
include $(PROJECT_ROOT)/tools/make/openapi.mk
include $(PROJECT_ROOT)/tools/make/python.mk

# Make the dist folder a default target.
all: dist
clean: clean-dist

# ---- Code generation ---- #

# Source code:
.codegen-src: .venv
	$(CP) cfg/.openapi-generator-ignore src/
	$(OPENAPI_CLI) generate -g python-flask -i ../data.json -o src -c cfg/codegen.json -t cfg/templates
	$(RMDIR) src/digital/forge/data/models
	$(RM) src/.openapi-generator-ignore
	$(POETRY) run autoflake --in-place --recursive --remove-all-unused-imports src/digital
	$(TOUCH) .codegen-src

# Test code:
.codegen-tests: .venv
	# TODO
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
