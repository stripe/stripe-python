from typing_extensions import TYPE_CHECKING, Literal
from typing import Optional
import sys as _sys
import os

# Stripe Python bindings
# API docs at http://stripe.com/docs/api
# Authors:
# Patrick Collison <patrick@stripe.com>
# Greg Brockman <gdb@stripe.com>
# Andrew Metcalf <andrew@stripe.com>

# Configuration variables
from stripe._api_version import _ApiVersion

# We must import the app_info module early to populate it into
# `sys.modules`; otherwise doing `import stripe.app_info` will end up
# importing that module, and not the global `AppInfo` name from below.
import stripe.app_info
from stripe._app_info import AppInfo as AppInfo
from stripe._version import VERSION as VERSION

api_key: Optional[str] = None
client_id: Optional[str] = None
api_base: str = "https://api.stripe.com"
connect_api_base: str = "https://connect.stripe.com"
upload_api_base: str = "https://files.stripe.com"
api_version: str = _ApiVersion.CURRENT
verify_ssl_certs: bool = True
proxy: Optional[str] = None
default_http_client: Optional["HTTPClient"] = None
app_info: Optional[AppInfo] = None
enable_telemetry: bool = True
max_network_retries: int = 0
ca_bundle_path: str = os.path.join(
    os.path.dirname(__file__), "data", "ca-certificates.crt"
)

# Set to either 'debug' or 'info', controls console logging
log: Optional[Literal["debug", "info"]] = None

# OAuth
from stripe._oauth import OAuth as OAuth

# Webhooks
from stripe._webhook import (
    Webhook as Webhook,
    WebhookSignature as WebhookSignature,
)


# Sets some basic information about the running application that's sent along
# with API requests. Useful for plugin authors to identify their plugin when
# communicating with Stripe.
#
# Takes a name and optional version and plugin URL.
def set_app_info(
    name: str,
    partner_id: Optional[str] = None,
    url: Optional[str] = None,
    version: Optional[str] = None,
):
    global app_info
    app_info = {
        "name": name,
        "partner_id": partner_id,
        "url": url,
        "version": version,
    }


# Infrastructure types
from stripe._api_resource import APIResource as APIResource
from stripe._error_object import ErrorObject as ErrorObject
from stripe._error_object import OAuthErrorObject as OAuthErrorObject
from stripe._list_object import ListObject as ListObject
from stripe._search_result_object import (
    SearchResultObject as SearchResultObject,
)
from stripe._stripe_object import StripeObject as StripeObject
from stripe._request_options import RequestOptions as RequestOptions
from stripe._createable_api_resource import (
    CreateableAPIResource as CreateableAPIResource,
)
from stripe._custom_method import (
    custom_method as custom_method,
)
from stripe._deletable_api_resource import (
    DeletableAPIResource as DeletableAPIResource,
)
from stripe._listable_api_resource import (
    ListableAPIResource as ListableAPIResource,
)
from stripe._nested_resource_class_methods import (
    nested_resource_class_methods as nested_resource_class_methods,
)
from stripe._searchable_api_resource import (
    SearchableAPIResource as SearchableAPIResource,
)
from stripe._singleton_api_resource import (
    SingletonAPIResource as SingletonAPIResource,
)
from stripe._test_helpers import (
    APIResourceTestHelpers as APIResourceTestHelpers,
)
from stripe._updateable_api_resource import (
    UpdateableAPIResource as UpdateableAPIResource,
)
from stripe._verify_mixin import (
    VerifyMixin as VerifyMixin,
)
from stripe._api_requestor import (
    APIRequestor as APIRequestor,
)

# Response types
from stripe._stripe_response import StripeResponse as StripeResponse
from stripe._stripe_response import StripeResponseBase as StripeResponseBase
from stripe._stripe_response import (
    StripeStreamResponse as StripeStreamResponse,
)

# Error types
from stripe._error import StripeError as StripeError
from stripe._error import APIError as APIError
from stripe._error import APIConnectionError as APIConnectionError
from stripe._error import StripeErrorWithParamCode as StripeErrorWithParamCode
from stripe._error import CardError as CardError
from stripe._error import IdempotencyError as IdempotencyError
from stripe._error import InvalidRequestError as InvalidRequestError
from stripe._error import AuthenticationError as AuthenticationError
from stripe._error import PermissionError as PermissionError
from stripe._error import RateLimitError as RateLimitError
from stripe._error import (
    SignatureVerificationError as SignatureVerificationError,
)

# HttpClient
from stripe._http_client import (
    HTTPClient as HTTPClient,
    PycurlClient as PycurlClient,
    RequestsClient as RequestsClient,
    UrlFetchClient as UrlFetchClient,
    new_default_http_client as new_default_http_client,
)

# Util
from stripe._util import convert_to_stripe_object as convert_to_stripe_object

# Backwards compatibility re-exports
if not TYPE_CHECKING:
    from stripe import _api_requestor as api_requestor
    from stripe import _stripe_response as stripe_response
    from stripe import _stripe_object as stripe_object
    from stripe import _error_object as error_object
    from stripe import _error as error
    from stripe import _http_client as http_client
    from stripe import _util as util
    from stripe import _oauth as oauth
    from stripe import _webhook as webhook
    from stripe import _multipart_data_generator as multipart_data_generator
    from stripe import _request_metrics as request_metrics
    from stripe._file import File as FileUpload

    import warnings

    # Python 3.7+ supports module level __getattr__ that allows us to lazy load deprecated modules
    # this matters because if we pre-load all modules from api_resources while suppressing warning
    # users will never see those warnings
    if _sys.version_info[:2] >= (3, 7):

        def __getattr__(name):
            if name == "abstract":
                import stripe.api_resources.abstract as _abstract

                return _abstract
            if name == "api_resources":
                import stripe.api_resources as _api_resources

                return _api_resources
            raise AttributeError(
                f"module {__name__!r} has no attribute {name!r}"
            )

    else:
        with warnings.catch_warnings():
            warnings.filterwarnings("ignore", category=DeprecationWarning)

            import stripe.api_resources.abstract as abstract
            import stripe.api_resources as api_resources


# API resources

# The beginning of the section generated from our OpenAPI spec
from stripe import (
    apps as apps,
    billing_portal as billing_portal,
    checkout as checkout,
    climate as climate,
    financial_connections as financial_connections,
    identity as identity,
    issuing as issuing,
    radar as radar,
    reporting as reporting,
    sigma as sigma,
    tax as tax,
    terminal as terminal,
    test_helpers as test_helpers,
    treasury as treasury,
)
from stripe._account import Account as Account
from stripe._account_link import AccountLink as AccountLink
from stripe._account_session import AccountSession as AccountSession
from stripe._apple_pay_domain import ApplePayDomain as ApplePayDomain
from stripe._application import Application as Application
from stripe._application_fee import ApplicationFee as ApplicationFee
from stripe._application_fee_refund import (
    ApplicationFeeRefund as ApplicationFeeRefund,
)
from stripe._balance import Balance as Balance
from stripe._balance_transaction import (
    BalanceTransaction as BalanceTransaction,
)
from stripe._bank_account import BankAccount as BankAccount
from stripe._capability import Capability as Capability
from stripe._card import Card as Card
from stripe._cash_balance import CashBalance as CashBalance
from stripe._charge import Charge as Charge
from stripe._connect_collection_transfer import (
    ConnectCollectionTransfer as ConnectCollectionTransfer,
)
from stripe._country_spec import CountrySpec as CountrySpec
from stripe._coupon import Coupon as Coupon
from stripe._credit_note import CreditNote as CreditNote
from stripe._credit_note_line_item import (
    CreditNoteLineItem as CreditNoteLineItem,
)
from stripe._customer import Customer as Customer
from stripe._customer_balance_transaction import (
    CustomerBalanceTransaction as CustomerBalanceTransaction,
)
from stripe._customer_cash_balance_transaction import (
    CustomerCashBalanceTransaction as CustomerCashBalanceTransaction,
)
from stripe._discount import Discount as Discount
from stripe._dispute import Dispute as Dispute
from stripe._ephemeral_key import EphemeralKey as EphemeralKey
from stripe._event import Event as Event
from stripe._exchange_rate import ExchangeRate as ExchangeRate
from stripe._file import File as File
from stripe._file_link import FileLink as FileLink
from stripe._funding_instructions import (
    FundingInstructions as FundingInstructions,
)
from stripe._invoice import Invoice as Invoice
from stripe._invoice_item import InvoiceItem as InvoiceItem
from stripe._invoice_line_item import InvoiceLineItem as InvoiceLineItem
from stripe._line_item import LineItem as LineItem
from stripe._login_link import LoginLink as LoginLink
from stripe._mandate import Mandate as Mandate
from stripe._payment_intent import PaymentIntent as PaymentIntent
from stripe._payment_link import PaymentLink as PaymentLink
from stripe._payment_method import PaymentMethod as PaymentMethod
from stripe._payment_method_configuration import (
    PaymentMethodConfiguration as PaymentMethodConfiguration,
)
from stripe._payment_method_domain import (
    PaymentMethodDomain as PaymentMethodDomain,
)
from stripe._payout import Payout as Payout
from stripe._person import Person as Person
from stripe._plan import Plan as Plan
from stripe._platform_tax_fee import PlatformTaxFee as PlatformTaxFee
from stripe._price import Price as Price
from stripe._product import Product as Product
from stripe._promotion_code import PromotionCode as PromotionCode
from stripe._quote import Quote as Quote
from stripe._refund import Refund as Refund
from stripe._reserve_transaction import (
    ReserveTransaction as ReserveTransaction,
)
from stripe._reversal import Reversal as Reversal
from stripe._review import Review as Review
from stripe._setup_attempt import SetupAttempt as SetupAttempt
from stripe._setup_intent import SetupIntent as SetupIntent
from stripe._shipping_rate import ShippingRate as ShippingRate
from stripe._source import Source as Source
from stripe._source_mandate_notification import (
    SourceMandateNotification as SourceMandateNotification,
)
from stripe._source_transaction import SourceTransaction as SourceTransaction
from stripe._subscription import Subscription as Subscription
from stripe._subscription_item import SubscriptionItem as SubscriptionItem
from stripe._subscription_schedule import (
    SubscriptionSchedule as SubscriptionSchedule,
)
from stripe._tax_code import TaxCode as TaxCode
from stripe._tax_deducted_at_source import (
    TaxDeductedAtSource as TaxDeductedAtSource,
)
from stripe._tax_id import TaxId as TaxId
from stripe._tax_rate import TaxRate as TaxRate
from stripe._token import Token as Token
from stripe._topup import Topup as Topup
from stripe._transfer import Transfer as Transfer
from stripe._usage_record import UsageRecord as UsageRecord
from stripe._usage_record_summary import (
    UsageRecordSummary as UsageRecordSummary,
)
from stripe._webhook_endpoint import WebhookEndpoint as WebhookEndpoint

# The end of the section generated from our OpenAPI spec
