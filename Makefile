include $(shell pipenv --where)/tools/make/common.mk

.PHONY = clean clean-venv venv

.venv: Pipfile
	$(PIPENV) install
venv: .venv
clean-venv:
	-$(PIPENV) --rm
	$(RM) Pipfile.lock

clean: clean-venv
