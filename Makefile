VENV_NAME?=venv
PIP?=pip
PYTHON?=python

venv: $(VENV_NAME)/bin/activate

$(VENV_NAME)/bin/activate: setup.py
	$(PIP) install --upgrade pip virtualenv
	@test -d $(VENV_NAME) || $(PYTHON) -m virtualenv --clear $(VENV_NAME)
	${VENV_NAME}/bin/python -m pip install -r requirements.txt
	@touch $(VENV_NAME)/bin/activate

test: venv
	@${VENV_NAME}/bin/tox -p auto $(TOX_ARGS)

test-nomock: venv
	@${VENV_NAME}/bin/tox -p auto -- --nomock $(TOX_ARGS)

ci-test: venv
	@${VENV_NAME}/bin/tox $(TOX_ARGS)

coveralls: venv
	@${VENV_NAME}/bin/tox -e coveralls

pyright: venv
	# In order for pyright to be able to follow imports, we need "editable_mode=compat" to force setuptools to do
	# an editable install via a .pth file mechanism and not "import hooks". See
	# the "editable installs" section of https://github.com/microsoft/pyright/blob/main/docs/import-resolution.md#editable-installs

	# This command might fail if we're on python 3.6, as versions of pip that
	# support python 3.6 don't know about "--config-settings", but in this case
	# we don't need to pass config-settings anyway because "editable_mode=compat" just
	# means to perform as these old versions of pip already do.
	pip install -e . --config-settings editable_mode=compat || pip install -e .
	@${VENV_NAME}/bin/pyright --version
	@${VENV_NAME}/bin/pyright $(PYRIGHT_ARGS)

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

.PHONY: ci-test clean codegen-format coveralls fmt fmtcheck lint test test-nomock test-travis update-version venv pyright
