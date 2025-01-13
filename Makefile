VENV_NAME?=venv
PIP?=pip
PYTHON?=python3.10
DEFAULT_TEST_ENV?=py310

venv: $(VENV_NAME)/bin/activate

$(VENV_NAME)/bin/activate: setup.py requirements.txt
	@test -d $(VENV_NAME) || $(PYTHON) -m venv --clear $(VENV_NAME)
	${VENV_NAME}/bin/python --version
	${VENV_NAME}/bin/python -m pip install -r requirements.txt
	@touch $(VENV_NAME)/bin/activate

test:
	@${VENV_NAME}/bin/tox -p auto -e $(DEFAULT_TEST_ENV) $(TOX_ARGS)

test-nomock: venv
	@${VENV_NAME}/bin/tox -p auto -- --nomock $(TOX_ARGS)

ci-test: venv
	@${VENV_NAME}/bin/tox $(TOX_ARGS)

coveralls: venv
	@${VENV_NAME}/bin/tox -e coveralls

pyright: venv
	@${VENV_NAME}/bin/tox -e pyright $(PYRIGHT_ARGS)

mypy: venv
	@${VENV_NAME}/bin/tox -e mypy $(MYPY_ARGS)

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
	@perl -pi -e 's|VERSION = "[.\d\w]+"|VERSION = "$(VERSION)"|' stripe/_version.py

codegen-format: fmt

.PHONY: ci-test clean codegen-format coveralls fmt fmtcheck lint test test-nomock test-travis update-version venv pyright mypy
