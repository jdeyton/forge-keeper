PROJECT_ROOT ?= $(shell git rev-parse --show-toplevel)
include $(PROJECT_ROOT)/tools/make/common.mk

# The default target:
all:

.PHONY: all clean

# ---- Development dependencies ---- #
# Main rule:
dev-dependencies:
	$(POETRY) config virtualenvs.in-project true
	$(MAKE) -C bin
.PHONY: dev-dependencies
all: dev-dependencies
# Cleanup:
clean-dev-dependencies:
	$(MAKE) -C bin clean
.PHONY: clean-dev-dependencies 
clean: clean-dev-dependencies