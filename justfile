set quiet

import? '../sdk-codegen/justfile'

VENV_NAME := ".venv"

export PATH := `pwd` / VENV_NAME / "bin:" + env('PATH')

_default:
    just --list --unsorted

# ⭐ run all unit tests
test *args: install-test-deps
    # configured in pytest.ini
    pytest {{ args }}

# ⭐ check for potential mistakes
lint: install-dev-deps
    python -m flake8 --show-source stripe tests setup.py

# verify types. optional argument to test as of a specific minor python version (e.g. `8` to test `python 3.8`); otherwise uses current version
typecheck minor_py_version="": install-dev-deps
    # suppress version update warnings
    PYRIGHT_PYTHON_IGNORE_WARNINGS=1 pyright {{ if minor_py_version == "" { "" } else { "--pythonversion 3." + minor_py_version } }}

# ⭐ format all code
format: install-dev-deps
    ruff format . --quiet

# verify formatting, but don't modify files
format-check: install-dev-deps
    ruff format . --check  --quiet

# remove venv
clean:
    rm -rf {{ VENV_NAME }}

# blow away and reinstall virtual env
reset: clean && venv

# build the package for upload
build: install-build-deps
    # --universal is deprecated, so we'll probably need to look at this eventually
    # given that we don't care about universal 2 and 3 packages, we probably don't need it?
    python -I setup.py clean --all sdist bdist_wheel --universal
    python -m twine check dist/*

# run backup type checker
typecheck-mypy: _install-all
    mypy

# install the tools for local development & static checks
install-dev-deps: (install "dev")

# install everything for unit tests
install-test-deps: (install "test")

# install dependencies to build the package
install-build-deps: (install "build")

_install-all: install-dev-deps install-test-deps install-build-deps

# installs files out of a {group}-requirements.txt into the local venv; mostly used by other recipes
install group: venv
    python -I -m pip install -r deps/{{ group }}-requirements.txt --disable-pip-version-check {{ if is_dependency() == "true" {"--quiet"} else {""} }}

# create a virtualenv if it doesn't exist; always installs the local package
[private]
venv:
    [ -d {{ VENV_NAME }} ] || ( \
        python -m venv {{ VENV_NAME }} && \
        {{ VENV_NAME }}/bin/python -I -m pip install -e . --quiet --disable-pip-version-check \
    )

# called by tooling
[private]
update-version version:
    @echo "{{ version }}" > VERSION
    @perl -pi -e 's|VERSION = "[.\d\w]+"|VERSION = "{{ version }}"|' stripe/_version.py
