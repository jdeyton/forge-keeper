# Allow these Python defines to be provided in advance.
PIP ?= pip
PIPENV ?= pipenv
PYTHON ?= python3

# Windows definitions
ifeq ($(OS),Windows_NT)
	RM = -powershell Remove-Item -ErrorAction Ignore -Force
# Unix definitions
else
	RM = rm -f
endif