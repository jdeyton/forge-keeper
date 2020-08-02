PROJECT_ROOT ?= $(shell git rev-parse --show-toplevel)
include $(PROJECT_ROOT)/tools/make/common.mk
include $(PROJECT_ROOT)/tools/make/openapi.mk
include $(PROJECT_ROOT)/tools/make/python.mk

# Make the dist folder a default target.
all: dist
clean: clean-dist

# ---- Code generation ---- #

PKG_DIR = src/digital/forge/data

# Source code:
.codegen-src: .venv
	$(CP) cfg/src/.openapi-generator-ignore src/
	$(OPENAPI_CLI) generate -g python-flask -i ../data.json -o src -c cfg/codegen.json -t cfg/src/templates
	$(MV) $(PKG_DIR)/__main__.py $(PKG_DIR)/server
	$(MV) $(PKG_DIR)/encoder.py $(PKG_DIR)/server
	$(RMDIR) $(PKG_DIR)/models
	-$(RMDIR) $(PKG_DIR)/test
	$(RM) src/.openapi-generator-ignore
	$(POETRY) run autoflake --in-place --recursive --remove-all-unused-imports --ignore-init-module-imports src/digital
	$(TOUCH) .codegen-src

# Test code:
.codegen-tests: .venv
	$(CP) cfg/tests/.openapi-generator-ignore src/
	$(OPENAPI_CLI) generate -g python-flask -i ../data.json -o src -c cfg/codegen.json -t cfg/tests/templates
	$(MV) $(PKG_DIR)/test src/
	$(RMDIR) $(PKG_DIR)/models
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
