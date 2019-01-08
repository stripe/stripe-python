init:
	pip install pipenv --upgrade
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
