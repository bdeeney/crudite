#
# Makefile for the crudite project
#
ENVDIR = ./env
SHELL = BASH_ENV=$(ENVDIR)/bin/activate /bin/bash

# Commands
PYTHON = python
PYTHON_VERSION = python2.7
VIRTUALENV = virtualenv
PIP = pip
EASY_INSTALL = easy_install

SETUP := $(PYTHON) setup.py
PACKAGE := $(shell $(SETUP) --name)
VERSION := $(shell $(SETUP) --version)
EGG_LINK := $(ENVDIR)/lib/$(PYTHON_VERSION)/site-packages/$(PACKAGE).egg-link

VIRTUALENVOPTS = --distribute --python=$(PYTHON_VERSION)

# Requirements that cannot be installed via pip (packages
# listed here will be installed via easy_install)
#ADDTLREQS = nose_machineout readline
ADDTLREQS = readline

.PHONY: all virtualenv req dev test clean
all:
	@echo "Nothing to do."

virtualenv: $(ENVDIR)
$(ENVDIR):
	$(VIRTUALENV) $(VIRTUALENVOPTS) $(ENVDIR)
req: .req
.req: $(ENVDIR)
	$(EASY_INSTALL) -U $(ADDTLREQS)
	@touch .req

dev: $(EGG_LINK)
$(EGG_LINK): setup.py .req
	echo $(EGG_LINK)
	$(SETUP) develop

test: dev
	$(SETUP) test

clean:
	@if type -t deactivate | grep -q "^function$$"; then \
		deactivate; \
	fi
	rm -rf $(ENVDIR) .req  *.egg *.egg-info
	find . -name '*.pyc' -print0 | xargs -0 rm
