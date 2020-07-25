PROJECT_ROOT ?= $(shell git rev-parse --show-toplevel)
include $(PROJECT_ROOT)/tools/make/common.mk

# One target to rule them all...
all:

# ---- Python projects ---- #

PY_PROJECTS = \
	data-model \
	data-client \
	data-server

# One target to find them...
$(PY_PROJECTS):
	$(MAKE) -C $@
.PHONY: $(PY_PROJECTS)
all: $(PY_PROJECTS) 

# One ring to bring them all and in the darkness clean them...
CLEAN_PY_PROJECTS = $(addprefix clean-,$(PY_PROJECTS))
$(CLEAN_PY_PROJECTS):
	$(MAKE) -C $(subst clean-,,$@) clean
.PHONY: $(CLEAN_PY_PROJECTS)
clean: $(CLEAN_PY_PROJECTS)

# ---- Virtual environments ---- #
#
# Note: These are NOT included by default because this is something that does
#   not need to be done super frequently.

# These targets make virtual environments.
PY_PROJECT_VENVS = $(addsuffix -venv,$(PY_PROJECTS))
$(PY_PROJECT_VENVS):
	$(MAKE) -C $(subst -venv,,$@) .venv
.PHONY: $(PY_PROJECT_VENVS)
# This specific one makes all of them:
venvs: $(PY_PROJECT_VENVS)
.PHONY: venvs
# These targets remove virtual environments.
PY_PROJECT_CLEAN_VENVS = $(addsuffix -clean-venv,$(PY_PROJECTS))
$(PY_PROJECT_CLEAN_VENVS):
	$(MAKE) -C $(subst -clean-venv,,$@) clean-venv
.PHONY: $(PY_PROJECT_CLEAN_VENVS)
# This specific one removes all of them.
clean-venvs: $(PY_PROJECT_CLEAN_VENVS)