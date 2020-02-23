
# Windows definitions
ifeq ($(OS),Windows_NT)
	PIPENV ?= pipenv.exe
	PYTHON ?= python.exe
	RM = -powershell Remove-Item -Force
# Unix-y definitions
else
	PIPENV ?= pipenv
	PYTHON ?= python3
	RM = rm -f
endif

PROJECT = digital.forge.http.server

.PHONY = clean

dist: README.md src setup.json setup.py
	$(PYTHON) setup.py bdist_wheel
clean-dist:
	$(RM) -r build
	$(RM) -r dist
	$(RM) -r src/$(PROJECT).egg-info

clean: clean-dist
