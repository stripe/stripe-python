test:
	pipenv run detox

ci:
	pipenv run pytest --cov=stripe -n 8

coveralls:
	pipenv run coveralls

lint:
	pipenv run tox -e lint
