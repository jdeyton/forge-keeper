
# Windows definitions
ifeq ($(OS),Windows_NT)
	PIPENV ?= pipenv.exe
	PYTHON ?= python3.exe
	RM = -powershell Remove-Item -Force
# Unix-y definitions
else
	PIPENV ?= pipenv
	PYTHON ?= python3
	RM = rm -f
endif

.PHONY = clean clean-venv venv

.venv: Pipfile
	$(PIPENV) install
venv: .venv
clean-venv:
	-$(PIPENV) --rm
	$(RM) Pipfile.lock

clean: clean-venv
