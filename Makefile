VENV_NAME?=venv
PIP?=pip
PYTHON?=python

venv: $(VENV_NAME)/bin/activate

$(VENV_NAME)/bin/activate: setup.py
	$(PIP) install --upgrade pip virtualenv
	@test -d $(VENV_NAME) || $(PYTHON) -m virtualenv --clear $(VENV_NAME)
	${VENV_NAME}/bin/python -m pip install -U pip tox twine -c constraints.txt
	${VENV_NAME}/bin/python -m pip install -e .
	@touch $(VENV_NAME)/bin/activate

test: venv
	@${VENV_NAME}/bin/tox -p auto $(TOX_ARGS)

test-nomock: venv
	@${VENV_NAME}/bin/tox -p auto -- --nomock $(TOX_ARGS)

stubdiff:
	cd typeshed_parity && ./generate_stubdiff.sh ../${VENV_NAME}/bin/python

stubdiff_pristine:
	${VENV_NAME}/bin/python -m pip install -U mypy -c constraints.txt
	cd typeshed_parity && ./generate_stubdiff.sh ../${VENV_NAME}/bin/python && git diff --exit-code stubdiff

ci-test: venv
	${VENV_NAME}/bin/python -m pip install -U tox-gh-actions
	@${VENV_NAME}/bin/tox $(TOX_ARGS)

coveralls: venv
	${VENV_NAME}/bin/python -m pip install -U coveralls
	@${VENV_NAME}/bin/tox -e coveralls

fmt: venv
	@${VENV_NAME}/bin/tox -e fmt -- --extend-exclude typeshed_parity

fmtcheck: venv
	@${VENV_NAME}/bin/tox -e fmt -- --extend-exclude typeshed_parity --check --verbose

lint: venv
	@${VENV_NAME}/bin/tox -e lint

clean:
	@rm -rf $(VENV_NAME) .coverage .coverage.* build/ dist/ htmlcov/

update-version:
	@echo "$(VERSION)" > VERSION
	@perl -pi -e 's|VERSION = "[.\d\w]+"|VERSION = "$(VERSION)"|' stripe/version.py

codegen-format: fmt

.PHONY: ci-test clean codegen-format coveralls fmt fmtcheck lint test test-nomock test-travis update-version venv stubdiff
