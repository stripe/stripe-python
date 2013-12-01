# Stripe Python bindings
# API docs at http://stripe.com/docs/api
# Authors:
# Patrick Collison <patrick@stripe.com>
# Greg Brockman <gdb@stripe.com>
# Andrew Metcalf <andrew@stripe.com>

# Configuration variables

api_key = None
api_base = 'https://api.stripe.com'
api_version = None
verify_ssl_certs = True

# Resource imports

from stripe.resource import (
    Account, Balance, BalanceTransaction, Card, Charge, Customer, Invoice,
    InvoiceItem, Plan, Token, Coupon, Event, Transfer, Recipient)

# DEPRECATED: These imports will be moved out of the root stripe namespace
# in version 2.0

from stripe.version import VERSION
from stripe.api_requestor import APIRequestor
from stripe.error import (StripeError, APIError, APIConnectionError,
                          AuthenticationError, CardError, InvalidRequestError)
from stripe.resource import (
    convert_to_stripe_object, StripeObject, StripeObjectEncoder,
    APIResource, ListObject, SingletonAPIResource, ListableAPIResource,
    CreateableAPIResource, UpdateableAPIResource, DeletableAPIResource)
from stripe.util import json, utf8, logger
