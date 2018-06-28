from __future__ import absolute_import, division, print_function

# Stripe Python bindings
# API docs at http://stripe.com/docs/api
# Authors:
# Patrick Collison <patrick@stripe.com>
# Greg Brockman <gdb@stripe.com>
# Andrew Metcalf <andrew@stripe.com>

# Configuration variables

api_key = None
client_id = None
api_base = 'https://api.stripe.com'
connect_api_base = 'https://connect.stripe.com'
upload_api_base = 'https://uploads.stripe.com'
api_version = None
verify_ssl_certs = True
proxy = None
default_http_client = None
app_info = None

# Set to either 'debug' or 'info', controls console logging
log = None

# Resource
from stripe.api_resources import *  # noqa

# OAuth
from stripe.oauth import OAuth  # noqa

# Webhooks
from stripe.webhook import Webhook, WebhookSignature  # noqa

# Error imports.  Note that we may want to move these out of the root
# namespace in the future and you should prefer to access them via
# the fully qualified `stripe.error` module.

from stripe.error import (  # noqa
    APIConnectionError,
    APIError,
    AuthenticationError,
    PermissionError,
    RateLimitError,
    CardError,
    IdempotencyError,
    InvalidRequestError,
    SignatureVerificationError,
    StripeError)

# OAuth error classes are not imported into the root namespace and must be
# accessed via stripe.oauth_error.<Exception>
from stripe import oauth_error  # noqa

# DEPRECATED: These imports will be moved out of the root stripe namespace
# in version 2.0

from stripe.version import VERSION  # noqa
from stripe.api_requestor import APIRequestor  # noqa

from stripe.stripe_object import StripeObject  # noqa
from stripe.api_resources.abstract import (  # noqa
    APIResource,
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    SingletonAPIResource,
    UpdateableAPIResource)

from stripe.resource import StripeObjectEncoder  # noqa
from stripe.util import (  # noqa
    convert_to_stripe_object,
    json,
    logger)


# Sets some basic information about the running application that's sent along
# with API requests. Useful for plugin authors to identify their plugin when
# communicating with Stripe.
#
# Takes a name and optional version and plugin URL.
def set_app_info(name, partner_id=None, url=None, version=None):
    global app_info
    app_info = {
        'name': name,
        'partner_id': partner_id,
        'url': url,
        'version': version,
    }
