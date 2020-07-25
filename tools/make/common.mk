# Allow these Python defines to be provided in advance.

# System commands:
CURL ?= /bin/curl
RM ?= /bin/rm -f
TOUCH ?= /bin/touch

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
