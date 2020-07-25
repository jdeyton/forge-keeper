all: dev-dependencies

.PHONY: dev-dependencies

POETRY ?= poetry

dev-dependencies:
	$(POETRY) config virtualenvs.in-project true
	$(MAKE) -C bin

