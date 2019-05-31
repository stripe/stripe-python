test:
	poetry run tox -p auto

ci:
	poetry run pytest --cov=stripe

coveralls:
	poetry run coveralls

fmt:
	poetry run tox -e fmt

fmtcheck:
	poetry run tox -e fmt -- --check --verbose

lint:
	poetry run tox -e lint
