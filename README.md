# Stripe Python Library

[![Build Status](https://travis-ci.org/stripe/stripe-python.svg?branch=master)](https://travis-ci.org/stripe/stripe-python)
[![Coverage Status](https://coveralls.io/repos/github/stripe/stripe-python/badge.svg?branch=master)](https://coveralls.io/github/stripe/stripe-python?branch=master)

The Stripe Python library provides convenient access to the Stripe API from
applications written in the Python language. It includes a pre-defined set of
classes for API resources that initialize themselves dynamically from API
responses which makes it compatible with a wide range of versions of the Stripe
API.

## Documentation

See the [Python API docs](https://stripe.com/docs/api/python#intro).

## Installation

You don't need this source code unless you want to modify the package. If you just
want to use the package, just run:

    pip install --upgrade stripe

Install from source with:

    python setup.py install

### Requirements

- Python 2.7+ or Python 3.4+ (PyPy supported)

## Usage

The library needs to be configured with your account's secret key which is
available in your [Stripe Dashboard][api-keys]. Set `stripe.api_key` to its
value:

```python
import stripe
stripe.api_key = "sk_test_..."

# list charges
stripe.Charge.list()

# retrieve single charge
stripe.Charge.retrieve("ch_1A2PUG2eZvKYlo2C4Rej1B9d")
```

### Per-request Configuration

Configure individual requests with keyword arguments. For example, you can make
requests with a specific [Stripe Version](https://stripe.com/docs/api#versioning)
or as a [connected account](https://stripe.com/docs/connect/authentication#authentication-via-the-stripe-account-header):

```python
import stripe

# list charges
stripe.Charge.list(
    api_key="sk_test_...",
    stripe_account="acct_...",
    stripe_version="2019-02-19"
)

# retrieve single charge
stripe.Charge.retrieve(
    "ch_1A2PUG2eZvKYlo2C4Rej1B9d",
    api_key="sk_test_...",
    stripe_account="acct_...",
    stripe_version="2019-02-19"
)
```

### Configuring a Client

The library can be configured to use `urlfetch`, `requests`, `pycurl`, or
`urllib2` with `stripe.default_http_client`:

```python
client = stripe.http_client.UrlFetchClient()
client = stripe.http_client.RequestsClient()
client = stripe.http_client.PycurlClient()
client = stripe.http_client.Urllib2Client()
stripe.default_http_client = client
```

Without a configured client, by default the library will attempt to load
libraries in the order above (i.e. `urlfetch` is preferred with `urllib2` used
as a last resort). We usually recommend that people use `requests`.

### Configuring a Proxy

A proxy can be configured with `stripe.proxy`:

```python
stripe.proxy = "https://user:pass@example.com:1234"
```

### Configuring Automatic Retries

Number of automatic retries on requests that fail due to an intermittent
network problem can be configured:

```python
stripe.max_network_retries = 2
```

[Idempotency keys][idempotency-keys] are automatically generated and added to
requests, when not given, to guarantee that retries are safe.

### Logging

The library can be configured to emit logging that will give you better insight
into what it's doing. The `info` logging level is usually most appropriate for
production use, but `debug` is also available for more verbosity.

There are a few options for enabling it:

1. Set the environment variable `STRIPE_LOG` to the value `debug` or `info`

   ```
   $ export STRIPE_LOG=debug
   ```

2. Set `stripe.log`:

   ```py
   import stripe
   stripe.log = 'debug'
   ```

3. Enable it through Python's logging module:
   ```py
   import logging
   logging.basicConfig()
   logging.getLogger('stripe').setLevel(logging.DEBUG)
   ```

### Writing a Plugin

If you're writing a plugin that uses the library, we'd appreciate it if you
identified using `stripe.set_app_info()`:

```py
stripe.set_app_info("MyAwesomePlugin", version="1.2.34", url="https://myawesomeplugin.info")
```

This information is passed along when the library makes calls to the Stripe
API.

## Development

The test suite depends on [stripe-mock], so make sure to fetch and run it from a
background terminal ([stripe-mock's README][stripe-mock] also contains
instructions for installing via Homebrew and other methods):

    go get -u github.com/stripe/stripe-mock
    stripe-mock

Install [pipenv][pipenv], then install all dependencies for the project:

    pipenv install --dev

Run all tests on all supported Python versions:

    make test

Run all tests for a specific Python version (modify `-e` according to your Python target):

    pipenv run tox -e py27

Run all tests in a single file:

    pipenv run tox -e py27 -- tests/api_resources/abstract/test_updateable_api_resource.py

Run a single test suite:

    pipenv run tox -e py27 -- tests/api_resources/abstract/test_updateable_api_resource.py::TestUpdateableAPIResource

Run a single test:

    pipenv run tox -e py27 -- tests/api_resources/abstract/test_updateable_api_resource.py::TestUpdateableAPIResource::test_save

Run the linter with:

    make lint

The library uses [Black][black] for code formatting. Code must be formatted
with Black before PRs are submitted, otherwise CI will fail. Run the formatter
with:

    make fmt

[api-keys]: https://dashboard.stripe.com/account/apikeys
[black]: https://github.com/ambv/black
[connect]: https://stripe.com/connect
[pipenv]: https://github.com/pypa/pipenv
[stripe-mock]: https://github.com/stripe/stripe-mock
[idempotency-keys]: https://stripe.com/docs/api/idempotent_requests?lang=python

<!--
# vim: set tw=79:
-->
