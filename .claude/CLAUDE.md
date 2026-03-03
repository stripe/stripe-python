# stripe-python

## Testing

- Run all tests: `just test`
- Run a specific test by name: `just test-one test_name`
- Run a specific test file: `just test tests/path/to/test_file.py`

## Formatting & Linting

- Format: `just format` (uses ruff)
- Lint: `just lint` (uses flake8)
- Typecheck: `just typecheck` (uses pyright)

## Key Locations

- HTTP client (request execution, retries, headers): `stripe/_http_client.py`
- Main client class: `stripe/_stripe_client.py`
- Client options/config: `stripe/_client_options.py`
- API requestor (request building, auth): `stripe/_api_requestor.py`

## Generated Code

- Files containing `File generated from our OpenAPI spec` at the top are generated; do not edit. Similarly, any code block starting with `The beginning of the section generated from our OpenAPI spec` is generated and should not be edited directly.
    - If something in a generated file/range needs to be updated, add a summary of the change to your report but don't attempt to edit it directly.
- Most files under `stripe/` resource subdirectories (e.g. `stripe/_customer.py`, `stripe/params/`, `stripe/resources/`) are generated.
- The HTTP client layer (`_http_client.py`, `_stripe_client.py`, `_api_requestor.py`, `_client_options.py`) is NOT generated.

## Conventions

- Uses `requests` library by default for sync HTTP, `httpx` for async
- Type hints throughout
- Virtual env managed in `.venv/`; `just` recipes handle setup automatically
- Work is not complete until `just test`, `just lint` and `just typecheck` complete successfully.
- All code must run on all supported Python versions (full list in the test section of @.github/workflows/ci.yml)

### Comments

- Comments MUST only be used to:
    1. Document a function
    2. Explain the WHY of a piece of code
    3. Explain a particularly complicated piece of code
- Comments NEVER should be used to:
    1. Say what used to be there. That's no longer relevant!
    2. Explain the WHAT of a piece of code (unless it's very non-obvious)

It's ok not to put comments on/in a function if their addition wouldn't meaningfully clarify anything.
