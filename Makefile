VENV_NAME?=venv
PIP?=pip
PYTHON?=python

venv: $(VENV_NAME)/bin/activate

$(VENV_NAME)/bin/activate: setup.py
	$(PIP) install --upgrade pip virtualenv
	@test -d $(VENV_NAME) || $(PYTHON) -m virtualenv --clear $(VENV_NAME)
	${VENV_NAME}/bin/python -m pip install -U pip tox twine
	${VENV_NAME}/bin/python -m pip install -e .
	@touch $(VENV_NAME)/bin/activate

test: venv
	@${VENV_NAME}/bin/tox -p auto $(TOX_ARGS)

test-nomock: venv
	@${VENV_NAME}/bin/tox -p auto -- --nomock $(TOX_ARGS)

test-gh-actions: venv
	${VENV_NAME}/bin/python -m pip install -U tox-gh-actions
	@${VENV_NAME}/bin/tox -p auto $(TOX_ARGS)

coveralls: venv
	${VENV_NAME}/bin/python -m pip install -U coveralls
	@${VENV_NAME}/bin/tox -e coveralls

fmt: venv
	@${VENV_NAME}/bin/tox -e fmt

fmtcheck: venv
	@${VENV_NAME}/bin/tox -e fmt -- --check --verbose

lint: venv
	@${VENV_NAME}/bin/tox -e lint

clean:
	@rm -rf $(VENV_NAME) .coverage .coverage.* build/ dist/ htmlcov/

update-version:
	@echo "$(VERSION)" > VERSION
	@perl -pi -e 's|VERSION = "[.\d\w]+"|VERSION = "$(VERSION)"|' stripe/version.py

codegen-format: fmt

.PHONY: clean codegen-format coveralls fmt fmtcheck lint test test-nomock test-travis update-version venv
