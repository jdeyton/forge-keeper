PROJECT_ROOT ?= $(shell git rev-parse --show-toplevel)
include $(PROJECT_ROOT)/tools/make/common.mk

# Python commands:
POETRY ?= poetry

# ---- Build Python wheels ---- #
dist: pyproject.toml
	$(POETRY) build -f wheel
clean-dist:
	$(RM) -r dist
.PHONY: clean-dist

# ---- Initialize Virtual Environment ---- #
.venv: pyproject.toml
	poetry install
	$(TOUCH) $@
clean-venv:
	$(RM) -r .venv
	$(RM) poetry.lock