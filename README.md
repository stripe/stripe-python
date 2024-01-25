# Stripe Python Library

[![pypi](https://img.shields.io/pypi/v/stripe.svg)](https://pypi.python.org/pypi/stripe)
[![Build Status](https://github.com/stripe/stripe-python/actions/workflows/ci.yml/badge.svg?branch=master)](https://github.com/stripe/stripe-python/actions?query=branch%3Amaster)
[![Coverage Status](https://coveralls.io/repos/github/stripe/stripe-python/badge.svg?branch=master)](https://coveralls.io/github/stripe/stripe-python?branch=master)

The Stripe Python library provides convenient access to the Stripe API from
applications written in the Python language. It includes a pre-defined set of
classes for API resources that initialize themselves dynamically from API
responses which makes it compatible with a wide range of versions of the Stripe
API.

## Documentation

See the [Python API docs](https://stripe.com/docs/api?lang=python).

See [video demonstrations][youtube-playlist] covering how to use the library.

## Installation

You don't need this source code unless you want to modify the package. If you just
want to use the package, just run:

```sh
pip install --upgrade stripe
```

Install from source with:

```sh
python setup.py install
```

### Requirements

- Python 3.6+ (PyPy supported)

#### Python 2.7 deprecation

[The Python Software Foundation (PSF)](https://www.python.org/psf-landing/) community [announced the end of support of Python 2](https://www.python.org/doc/sunset-python-2/) on 01 January 2020.
Starting with version 6.0.0 Stripe SDK Python packages will no longer support Python 2.7. To continue to get new features and security updates, please make sure to update your Python runtime to Python 3.6+.

The last version of the Stripe SDK that supports Python 2.7 is 5.5.0.

## Usage

The library needs to be configured with your account's secret key which is
available in your [Stripe Dashboard][api-keys]. Set `stripe.api_key` to its
value:

```python
from stripe import StripeClient

client = StripeClient("sk_test_...")

# list customers
customers = client.customers.list()

# print the first customer's email
print(customers.data[0].email)

# retrieve specific Customer
customer = client.customers.retrieve("cus_123456789")

# print that customer's email
print(customer.email)
```

### Handling exceptions

Unsuccessful requests raise exceptions. The class of the exception will reflect
the sort of error that occurred. Please see the [Api
Reference](https://stripe.com/docs/api/errors/handling) for a description of
the error classes you should handle, and for information on how to inspect
these errors.

### Per-request Configuration

Configure individual requests with the `options` argument. For example, you can make
requests with a specific [Stripe Version](https://stripe.com/docs/api#versioning)
or as a [connected account](https://stripe.com/docs/connect/authentication#authentication-via-the-stripe-account-header):

```python
from stripe import StripeClient

client = StripeClient("sk_test_...")

# list customers
client.customers.list(
    options={
        "api_key": "sk_test_...",
        "stripe_account": "acct_...",
        "stripe_version": "2019-02-19",
    }
)

# retrieve single customer
client.customers.retrieve(
    "cus_123456789",
    options={
        "api_key": "sk_test_...",
        "stripe_account": "acct_...",
        "stripe_version": "2019-02-19",
    }
)
```

### Configuring an HTTP Client

You can configure your `StripeClient` to use `urlfetch`, `requests`, `pycurl`, or
`urllib2` with the `http_client` option:

```python
client = StripeClient("sk_test_...", http_client=stripe.UrlFetchClient())
client = StripeClient("sk_test_...", http_client=stripe.RequestsClient())
client = StripeClient("sk_test_...", http_client=stripe.PycurlClient())
client = StripeClient("sk_test_...", http_client=stripe.Urllib2Client())
```

Without a configured client, by default the library will attempt to load
libraries in the order above (i.e. `urlfetch` is preferred with `urllib2` used
as a last resort). We usually recommend that people use `requests`.

### Configuring a Proxy

A proxy can be configured with the `proxy` client option:

```python
client = StripeClient("sk_test_...", proxy="https://user:pass@example.com:1234")
```

### Configuring Automatic Retries

You can enable automatic retries on requests that fail due to a transient
problem by configuring the maximum number of retries:

```python
client = StripeClient("sk_test_...", max_network_retries=2)
```

Various errors can trigger a retry, like a connection error or a timeout, and
also certain API responses like HTTP status `409 Conflict`.

[Idempotency keys][idempotency-keys] are automatically generated and added to
requests, when not given, to guarantee that retries are safe.

### Logging

The library can be configured to emit logging that will give you better insight
into what it's doing. The `info` logging level is usually most appropriate for
production use, but `debug` is also available for more verbosity.

There are a few options for enabling it:

1. Set the environment variable `STRIPE_LOG` to the value `debug` or `info`

    ```sh
    $ export STRIPE_LOG=debug
    ```

2. Set `stripe.log`:

    ```python
    import stripe
    stripe.log = 'debug'
    ```

3. Enable it through Python's logging module:

    ```python
    import logging
    logging.basicConfig()
    logging.getLogger('stripe').setLevel(logging.DEBUG)
    ```

### Accessing response code and headers

You can access the HTTP response code and headers using the `last_response` property of the returned resource.

```python
customer = client.customers.retrieve(
    "cus_123456789"
)

print(customer.last_response.code)
print(customer.last_response.headers)
```

### Writing a Plugin

If you're writing a plugin that uses the library, we'd appreciate it if you
identified using `stripe.set_app_info()`:

```py
stripe.set_app_info("MyAwesomePlugin", version="1.2.34", url="https://myawesomeplugin.info")
```

This information is passed along when the library makes calls to the Stripe
API.

### Telemetry

By default, the library sends telemetry to Stripe regarding request latency and feature usage. These
numbers help Stripe improve the overall latency of its API for all users, and
improve popular features.

You can disable this behavior if you prefer:

```python
stripe.enable_telemetry = False
```

## Types

In [v7.1.0](https://github.com/stripe/stripe-python/releases/tag/v7.1.0) and
newer, the
library includes type annotations. See [the wiki](https://github.com/stripe/stripe-python/wiki/Inline-type-annotations)
for a detailed guide.

Please note that some annotations use features that were only fairly recently accepted,
such as [`Unpack[TypedDict]`](https://peps.python.org/pep-0692/#specification) that was
[accepted](https://discuss.python.org/t/pep-692-using-typeddict-for-more-precise-kwargs-typing/17314/81)
in January 2023. We have tested that these types are recognized properly by [Pyright](https://github.com/microsoft/pyright).
Support for `Unpack` in MyPy is still experimental, but appears to degrade gracefully.
Please [report an issue](https://github.com/stripe/stripe-python/issues/new/choose) if there
is anything we can do to improve the types for your type checker of choice.

### Types and the Versioning Policy

We release type changes in minor releases. While stripe-python follows semantic
versioning, our semantic versions describe the *runtime behavior* of the
library alone. Our *type annotations are not reflected in the semantic
version*. That is, upgrading to a new minor version of stripe-python might
result in your type checker producing a type error that it didn't before. You
can use a `~=x.x` or `x.x.*` [version specifier](https://peps.python.org/pep-0440/#examples)
in your `requirements.txt` to constrain `pip` to a certain minor range of `stripe-python`.

### Types and API Versions

The types describe the [Stripe API version](https://stripe.com/docs/api/versioning)
that was the latest at the time of release. This is the version that your library
sends by default. If you are overriding `stripe.api_version` / `stripe_version` on the `StripeClient`, or using a
[webhook endpoint](https://stripe.com/docs/webhooks#api-versions) tied to an older version,
be aware that the data you see at runtime may not match the types.

## Beta SDKs

Stripe has features in the beta phase that can be accessed via the beta version of this package.
We would love for you to try these and share feedback with us before these features reach the stable phase.
To install a beta version use `pip install` with the exact version you'd like to use:

```
pip install stripe==5.3.0b3
```

> **Note**
> There can be breaking changes between beta versions. Therefore we recommend pinning the package version to a specific beta version in your [requirements file](https://pip.pypa.io/en/stable/user_guide/#requirements-files) or `setup.py`. This way you can install the same version each time without breaking changes unless you are intentionally looking for the latest beta version.

We highly recommend keeping an eye on when the beta feature you are interested in goes from beta to stable so that you can move from using a beta version of the SDK to the stable version.

If your beta feature requires a `Stripe-Version` header to be sent, use the `stripe.api_version` field to set it:

```python
stripe.api_version += "; feature_beta=v3"
```

### Custom requests

If you would like to send a request to an undocumented API (for example you are in a private beta), or if you prefer to bypass the method definitions in the library and specify your request details directly, you can use the `raw_request` method on `stripe`.

```python
response = stripe.raw_request(
    "post", "/v1/beta_endpoint", param=123, stripe_version="2022-11-15; feature_beta=v3"
)

# (Optional) response is a StripeResponse. You can use `stripe.deserialize` to get a StripeObject.
deserialized_resp = stripe.deserialize(response)
```

## Support

New features and bug fixes are released on the latest major version of the Stripe Python library. If you are on an older major version, we recommend that you upgrade to the latest in order to use the new features and bug fixes including those for security vulnerabilities. Older major versions of the package will continue to be available for use, but will not be receiving any updates.

## Development

The test suite depends on [stripe-mock], so make sure to fetch and run it from a
background terminal ([stripe-mock's README][stripe-mock] also contains
instructions for installing via Homebrew and other methods):

```sh
go install github.com/stripe/stripe-mock@latest
stripe-mock
```

Run the following command to set up the development virtualenv:

```sh
make
```

Run all tests on all supported Python versions:

```sh
make test
```

Run all tests for a specific Python version (modify `-e` according to your Python target):

```sh
TOX_ARGS="-e py37" make test
```

Run all tests in a single file:

```sh
TOX_ARGS="-e py37 -- tests/api_resources/abstract/test_updateable_api_resource.py" make test
```

Run a single test suite:

```sh
TOX_ARGS="-e py37 -- tests/api_resources/abstract/test_updateable_api_resource.py::TestUpdateableAPIResource" make test
```

Run a single test:

```sh
TOX_ARGS="-e py37 -- tests/api_resources/abstract/test_updateable_api_resource.py::TestUpdateableAPIResource::test_save" make test
```

Run the linter with:

```sh
make lint
```

The library uses [Black][black] for code formatting. Code must be formatted
with Black before PRs are submitted, otherwise CI will fail. Run the formatter
with:

```sh
make fmt
```

[api-keys]: https://dashboard.stripe.com/account/apikeys
[black]: https://github.com/ambv/black
[connect]: https://stripe.com/connect
[poetry]: https://github.com/sdispater/poetry
[stripe-mock]: https://github.com/stripe/stripe-mock
[idempotency-keys]: https://stripe.com/docs/api/idempotent_requests?lang=python
[youtube-playlist]: https://www.youtube.com/playlist?list=PLy1nL-pvL2M55YVn0mGoQ5r-39A1-ZypO

<!--
# vim: set tw=79:
-->
