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
from .resource import (  # noqa
    Account,
    AlipayAccount,
    ApplePayDomain,
    ApplicationFee,
    Balance,
    BalanceTransaction,
    BankAccount,
    BitcoinReceiver,
    BitcoinTransaction,
    Card,
    Charge,
    CountrySpec,
    Coupon,
    Customer,
    Dispute,
    Event,
    FileUpload,
    Invoice,
    InvoiceItem,
    LoginLink,
    Order,
    OrderReturn,
    Payout,
    Plan,
    Product,
    Recipient,
    RecipientTransfer,
    Refund,
    SKU,
    Source,
    Subscription,
    SubscriptionItem,
    ThreeDSecure,
    Token,
    Transfer)

# OAuth
from .oauth import OAuth  # noqa

# Webhooks
from .webhook import Webhook, WebhookSignature  # noqa

# Error imports.  Note that we may want to move these out of the root
# namespace in the future and you should prefer to access them via
# the fully qualified `stripe.error` module.

from .error import (  # noqa
    APIConnectionError,
    APIError,
    AuthenticationError,
    PermissionError,
    RateLimitError,
    CardError,
    InvalidRequestError,
    OAuthError,
    SignatureVerificationError,
    StripeError)

# DEPRECATED: These imports will be moved out of the root stripe namespace
# in version 2.0

from .version import VERSION  # noqa
from .api_requestor import APIRequestor  # noqa
from .resource import (  # noqa
    APIResource,
    CreateableAPIResource,
    DeletableAPIResource,
    ListObject,
    ListableAPIResource,
    SingletonAPIResource,
    StripeObject,
    StripeObjectEncoder,
    UpdateableAPIResource,
    convert_to_stripe_object)
from .util import json, logger  # noqa


# Sets some basic information about the running application that's sent along
# with API requests. Useful for plugin authors to identify their plugin when
# communicating with Stripe.
#
# Takes a name and optional version and plugin URL.
def set_app_info(name, version=None, url=None):
    global app_info
    app_info = {
        'name': name,
        'version': version,
        'url': url,
    }
