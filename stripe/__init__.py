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

# Resource
from stripe.resource import (  # noqa
    Account, Balance, BalanceTransaction, Card, Charge, Customer, Invoice,
    InvoiceItem, Plan, Token, Coupon, Event, Transfer, Recipient,
    ApplicationFee)

# Error imports.  Note that we may want to move these out of the root
# namespace in the future and you should prefer to access them via
# the fully qualified `stripe.error` module.

from stripe.error import (  # noqa
    StripeError, APIError, APIConnectionError, AuthenticationError, CardError,
    InvalidRequestError)

# DEPRECATED: These imports will be moved out of the root stripe namespace
# in version 2.0

from stripe.version import VERSION  # noqa
from stripe.api_requestor import APIRequestor  # noqa
from stripe.resource import (  # noqa
    convert_to_stripe_object, StripeObject, StripeObjectEncoder,
    APIResource, ListObject, SingletonAPIResource, ListableAPIResource,
    CreateableAPIResource, UpdateableAPIResource, DeletableAPIResource)
from stripe.util import json, logger  # noqa


# This is a pretty ugly solution to deprecating modules but a similar
# approach is used in Zope, Twisted and sanctioned in:
# https://mail.python.org/pipermail/python-ideas/2012-May/014969.html
import sys as _sys
import warnings as _warnings
from inspect import isclass as _isclass, ismodule as _ismodule

_dogetattr = object.__getattribute__
_ALLOWED_ATTRIBUTES = (
    'api_key',
    'api_base',
    'api_version',
    'verify_ssl_certs'
)
_original_module = _sys.modules[__name__]


class _DeprecationWrapper(object):

    def __getattribute__(self, name):
        value = getattr(_original_module, name)

        # Allow specific names and resources
        if not (name[0] == '_' or
                name in _ALLOWED_ATTRIBUTES or
                _ismodule(value) or
                (_isclass(value) and
                 issubclass(value, APIResource) and
                 value is not APIResource)):
            _warnings.warn(
                'Attribute `%s` is being moved out of the `stripe` module '
                'in version 2.0 of the Stripe bindings.  Please access it '
                'in the appropriate submodule instead' % (name,),
                DeprecationWarning, stacklevel=2)

        return value

    def __setattr__(self, name, value):
        setattr(_original_module, name, value)

    def __delattr__(self, name):
        delattr(_original_module, name)

_sys.modules[__name__] = _DeprecationWrapper()
