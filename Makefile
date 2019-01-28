init:
	# Pin pipenv to 2018.10.13 because further releases are incompatible with
	# PyPy3. The issue was fixed in https://github.com/pypa/pipenv/pull/3322
	# but no new version has been released yet.
	pip install --upgrade pipenv==2018.10.13
	pipenv install --dev --skip-lock

test:
	pipenv run tox -p auto

ci:
	pipenv run pytest --cov=stripe

coveralls:
	pipenv run coveralls

fmt:
	pipenv run tox -e fmt

fmtcheck:
	pipenv run tox -e fmt -- --check --verbose

lint:
	pipenv run tox -e lint
