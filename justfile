set quiet

import? '../sdk-codegen/utils.just'

VENV_NAME := ".venv"

export PATH := `pwd` / VENV_NAME / "bin:" + env('PATH')

_default:
    just --list --unsorted

# ⭐ run all unit tests
test *args: install-test-deps
    # configured in pyproject.toml
    pytest {{ args }}

# ⭐ check for potential mistakes
lint: install-dev-deps
    python -m flake8 --show-source stripe tests setup.py

# verify types. optional argument to test as of a specific minor python version (e.g. `8` to test `python 3.8`); otherwise uses current version
typecheck minor_py_version="": install-test-deps install-dev-deps
    # suppress version update warnings
    PYRIGHT_PYTHON_IGNORE_WARNINGS=1 pyright {{ if minor_py_version == "" { "" } else { "--pythonversion 3." + minor_py_version } }}

# ⭐ format all code
format: install-dev-deps
    ruff format . --quiet

# verify formatting, but don't modify files
format-check: install-dev-deps
    ruff format . --check  --quiet

# remove venv & build artifacts
clean:
    rm -rf {{ VENV_NAME }} venv .tox dist stripe.egg-info

# blow away and reinstall virtual env
reset: clean && venv

# build the package for upload
build: install-build-deps
    python -m build
    python -m twine check dist/*

# typecheck some examples w/ mypy
typecheck-examples: _install-all
    # configured in pyproject.toml
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
    # always log deps in CI, but don't do it locally
    python -I -m pip install -r deps/{{ group }}-requirements.txt --disable-pip-version-check {{ if env("CI", "") == "true" {""} else if is_dependency() == "true" {"--quiet"} else {""} }}

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
    echo "{{ version }}" > VERSION
    perl -pi -e 's|VERSION = "[.\d\w]+"|VERSION = "{{ version }}"|' stripe/_version.py
