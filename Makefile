init:
	pip install pipenv --upgrade
	pipenv install --dev --skip-lock

test:
	pipenv run detox

ci:
	pipenv run pytest --cov=stripe -n 8

coveralls:
	pipenv run coveralls

fmt:
	pipenv run tox -e fmt

lint:
	pipenv run tox -e lint
