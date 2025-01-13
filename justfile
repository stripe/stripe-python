set quiet := true

import? '../sdk-codegen/justfile'

VENV_NAME := "venv"

export PATH := `pwd` / VENV_NAME / "bin:" + env('PATH')

_default:
    ruff --version
    just --list --unsorted

install: venv
    python -m pip install -r requirements.txt --disable-pip-version-check {{ if is_dependency() == "true" {"--quiet"} else {""} }}

# install deps for unit tests
test-install: venv
    python -I -m pip install -r test-requirements.txt

test *args: install
    # configured in pytest.ini
    pytest {{ args }}

mypy:
    mypy

lint:
    python -m flake8 --show-source stripe tests setup.py

pyright:
    pyright

# use a specific version for this
[no-quiet]
ci-pyright py_version:
    python{{py_version}} --version
    ls venv/bin
    # pyright --pythonversion {{ py_version }}
    python{{py_version}} -m pyright --pythonversion {{ py_version }}

[no-quiet]
ci-pyright2 minor_py_version:
    # python3.{{py_version}} --version
    # ls venv/bin
    # pyright --pythonversion {{ py_version }}
    pyright --pythonversion 3.{{ py_version }}

format:
    ruff format . --quiet

format-check:
    ruff format . --check  --quiet

# create a virtualenv if it doesn't exist
[private]
venv:
    [ -d {{ VENV_NAME }} ] || python -m venv {{ VENV_NAME }}

# called by tooling
[private]
update-version version:
    @echo "{{ version }}" > VERSION
    @perl -pi -e 's|VERSION = "[.\d\w]+"|VERSION = "{{ version }}"|' stripe/_version.py
