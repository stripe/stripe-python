from typing_extensions import TYPE_CHECKING, Literal
from typing import Optional
import sys as _sys
import os
import warnings

# Stripe Python bindings
# API docs at http://stripe.com/docs/api
# Authors:
# Patrick Collison <patrick@stripe.com>
# Greg Brockman <gdb@stripe.com>
# Andrew Metcalf <andrew@stripe.com>

# Configuration variables
from stripe._api_version import _ApiVersion
from stripe._api_requestor import _APIRequestor

# We must import the app_info module early to populate it into
# `sys.modules`; otherwise doing `import stripe.app_info` will end up
# importing that module, and not the global `AppInfo` name from below.
import stripe.app_info
from stripe._app_info import AppInfo as AppInfo
from stripe._version import VERSION as VERSION

# Constants
DEFAULT_API_BASE: str = "https://api.stripe.com"
DEFAULT_CONNECT_API_BASE: str = "https://connect.stripe.com"
DEFAULT_UPLOAD_API_BASE: str = "https://files.stripe.com"
DEFAULT_METER_EVENTS_API_BASE: str = "https://meter-events.stripe.com"


api_key: Optional[str] = None
client_id: Optional[str] = None
api_base: str = DEFAULT_API_BASE
connect_api_base: str = DEFAULT_CONNECT_API_BASE
upload_api_base: str = DEFAULT_UPLOAD_API_BASE
meter_events_api_base: str = DEFAULT_METER_EVENTS_API_BASE
api_version: str = _ApiVersion.CURRENT
verify_ssl_certs: bool = True
proxy: Optional[str] = None
default_http_client: Optional["HTTPClient"] = None
app_info: Optional[AppInfo] = None
enable_telemetry: bool = True
max_network_retries: int = 2
ca_bundle_path: str = os.path.join(
    os.path.dirname(__file__), "data", "ca-certificates.crt"
)

# Lazily initialized stripe.default_http_client
default_http_client = None
_default_proxy = None


def ensure_default_http_client():
    if default_http_client:
        _warn_if_mismatched_proxy()
        return
    _init_default_http_client()


def _init_default_http_client():
    global _default_proxy
    global default_http_client

    # If the stripe.default_http_client has not been set by the user
    # yet, we'll set it here. This way, we aren't creating a new
    # HttpClient for every request.
    default_http_client = new_default_http_client(
        verify_ssl_certs=verify_ssl_certs, proxy=proxy
    )
    _default_proxy = proxy


def _warn_if_mismatched_proxy():
    global _default_proxy
    from stripe import proxy

    if proxy != _default_proxy:
        warnings.warn(
            "stripe.proxy was updated after sending a "
            "request - this is a no-op. To use a different proxy, "
            "set stripe.default_http_client to a new client "
            "configured with the proxy."
        )


# Set to either 'debug' or 'info', controls console logging
log: Optional[Literal["debug", "info"]] = None

# OAuth
from stripe._oauth import OAuth as OAuth
from stripe._oauth_service import OAuthService as OAuthService

# Webhooks
from stripe._webhook import (
    Webhook as Webhook,
    WebhookSignature as WebhookSignature,
)

# StripeClient
from stripe._stripe_client import StripeClient as StripeClient  # noqa


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
from stripe._stripe_context import StripeContext as StripeContext
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
from stripe._requestor_options import (
    RequestorOptions as RequestorOptions,
)
from stripe._api_mode import (
    ApiMode as ApiMode,
)
from stripe._base_address import (
    BaseAddress as BaseAddress,
)

# Response types
from stripe._stripe_response import StripeResponse as StripeResponse
from stripe._stripe_response import StripeResponseBase as StripeResponseBase
from stripe._stripe_response import (
    StripeStreamResponse as StripeStreamResponse,
    StripeStreamResponseAsync as StripeStreamResponseAsync,
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
    HTTPXClient as HTTPXClient,
    AIOHTTPClient as AIOHTTPClient,
    new_default_http_client as new_default_http_client,
)

# Util
from stripe._util import convert_to_stripe_object as convert_to_stripe_object

# Backwards compatibility re-exports
if not TYPE_CHECKING:
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
    billing as billing,
    billing_portal as billing_portal,
    checkout as checkout,
    climate as climate,
    entitlements as entitlements,
    events as events,
    financial_connections as financial_connections,
    forwarding as forwarding,
    identity as identity,
    issuing as issuing,
    radar as radar,
    reporting as reporting,
    sigma as sigma,
    tax as tax,
    terminal as terminal,
    test_helpers as test_helpers,
    treasury as treasury,
    v2 as v2,
)
from stripe._account import Account as Account
from stripe._account_capability_list_params import (
    AccountCapabilityListParams as AccountCapabilityListParams,
)
from stripe._account_capability_retrieve_params import (
    AccountCapabilityRetrieveParams as AccountCapabilityRetrieveParams,
)
from stripe._account_capability_service import (
    AccountCapabilityService as AccountCapabilityService,
)
from stripe._account_capability_update_params import (
    AccountCapabilityUpdateParams as AccountCapabilityUpdateParams,
)
from stripe._account_create_external_account_params import (
    AccountCreateExternalAccountParams as AccountCreateExternalAccountParams,
)
from stripe._account_create_login_link_params import (
    AccountCreateLoginLinkParams as AccountCreateLoginLinkParams,
)
from stripe._account_create_params import (
    AccountCreateParams as AccountCreateParams,
)
from stripe._account_create_person_params import (
    AccountCreatePersonParams as AccountCreatePersonParams,
)
from stripe._account_delete_external_account_params import (
    AccountDeleteExternalAccountParams as AccountDeleteExternalAccountParams,
)
from stripe._account_delete_params import (
    AccountDeleteParams as AccountDeleteParams,
)
from stripe._account_delete_person_params import (
    AccountDeletePersonParams as AccountDeletePersonParams,
)
from stripe._account_external_account_create_params import (
    AccountExternalAccountCreateParams as AccountExternalAccountCreateParams,
)
from stripe._account_external_account_delete_params import (
    AccountExternalAccountDeleteParams as AccountExternalAccountDeleteParams,
)
from stripe._account_external_account_list_params import (
    AccountExternalAccountListParams as AccountExternalAccountListParams,
)
from stripe._account_external_account_retrieve_params import (
    AccountExternalAccountRetrieveParams as AccountExternalAccountRetrieveParams,
)
from stripe._account_external_account_service import (
    AccountExternalAccountService as AccountExternalAccountService,
)
from stripe._account_external_account_update_params import (
    AccountExternalAccountUpdateParams as AccountExternalAccountUpdateParams,
)
from stripe._account_link import AccountLink as AccountLink
from stripe._account_link_create_params import (
    AccountLinkCreateParams as AccountLinkCreateParams,
)
from stripe._account_link_service import (
    AccountLinkService as AccountLinkService,
)
from stripe._account_list_capabilities_params import (
    AccountListCapabilitiesParams as AccountListCapabilitiesParams,
)
from stripe._account_list_external_accounts_params import (
    AccountListExternalAccountsParams as AccountListExternalAccountsParams,
)
from stripe._account_list_params import AccountListParams as AccountListParams
from stripe._account_list_persons_params import (
    AccountListPersonsParams as AccountListPersonsParams,
)
from stripe._account_login_link_create_params import (
    AccountLoginLinkCreateParams as AccountLoginLinkCreateParams,
)
from stripe._account_login_link_service import (
    AccountLoginLinkService as AccountLoginLinkService,
)
from stripe._account_modify_capability_params import (
    AccountModifyCapabilityParams as AccountModifyCapabilityParams,
)
from stripe._account_modify_external_account_params import (
    AccountModifyExternalAccountParams as AccountModifyExternalAccountParams,
)
from stripe._account_modify_person_params import (
    AccountModifyPersonParams as AccountModifyPersonParams,
)
from stripe._account_person_create_params import (
    AccountPersonCreateParams as AccountPersonCreateParams,
)
from stripe._account_person_delete_params import (
    AccountPersonDeleteParams as AccountPersonDeleteParams,
)
from stripe._account_person_list_params import (
    AccountPersonListParams as AccountPersonListParams,
)
from stripe._account_person_retrieve_params import (
    AccountPersonRetrieveParams as AccountPersonRetrieveParams,
)
from stripe._account_person_service import (
    AccountPersonService as AccountPersonService,
)
from stripe._account_person_update_params import (
    AccountPersonUpdateParams as AccountPersonUpdateParams,
)
from stripe._account_persons_params import (
    AccountPersonsParams as AccountPersonsParams,
)
from stripe._account_reject_params import (
    AccountRejectParams as AccountRejectParams,
)
from stripe._account_retrieve_capability_params import (
    AccountRetrieveCapabilityParams as AccountRetrieveCapabilityParams,
)
from stripe._account_retrieve_current_params import (
    AccountRetrieveCurrentParams as AccountRetrieveCurrentParams,
)
from stripe._account_retrieve_external_account_params import (
    AccountRetrieveExternalAccountParams as AccountRetrieveExternalAccountParams,
)
from stripe._account_retrieve_params import (
    AccountRetrieveParams as AccountRetrieveParams,
)
from stripe._account_retrieve_person_params import (
    AccountRetrievePersonParams as AccountRetrievePersonParams,
)
from stripe._account_service import AccountService as AccountService
from stripe._account_session import AccountSession as AccountSession
from stripe._account_session_create_params import (
    AccountSessionCreateParams as AccountSessionCreateParams,
)
from stripe._account_session_service import (
    AccountSessionService as AccountSessionService,
)
from stripe._account_update_params import (
    AccountUpdateParams as AccountUpdateParams,
)
from stripe._apple_pay_domain import ApplePayDomain as ApplePayDomain
from stripe._apple_pay_domain_create_params import (
    ApplePayDomainCreateParams as ApplePayDomainCreateParams,
)
from stripe._apple_pay_domain_delete_params import (
    ApplePayDomainDeleteParams as ApplePayDomainDeleteParams,
)
from stripe._apple_pay_domain_list_params import (
    ApplePayDomainListParams as ApplePayDomainListParams,
)
from stripe._apple_pay_domain_retrieve_params import (
    ApplePayDomainRetrieveParams as ApplePayDomainRetrieveParams,
)
from stripe._apple_pay_domain_service import (
    ApplePayDomainService as ApplePayDomainService,
)
from stripe._application import Application as Application
from stripe._application_fee import ApplicationFee as ApplicationFee
from stripe._application_fee_create_refund_params import (
    ApplicationFeeCreateRefundParams as ApplicationFeeCreateRefundParams,
)
from stripe._application_fee_list_params import (
    ApplicationFeeListParams as ApplicationFeeListParams,
)
from stripe._application_fee_list_refunds_params import (
    ApplicationFeeListRefundsParams as ApplicationFeeListRefundsParams,
)
from stripe._application_fee_modify_refund_params import (
    ApplicationFeeModifyRefundParams as ApplicationFeeModifyRefundParams,
)
from stripe._application_fee_refund import (
    ApplicationFeeRefund as ApplicationFeeRefund,
)
from stripe._application_fee_refund_create_params import (
    ApplicationFeeRefundCreateParams as ApplicationFeeRefundCreateParams,
)
from stripe._application_fee_refund_list_params import (
    ApplicationFeeRefundListParams as ApplicationFeeRefundListParams,
)
from stripe._application_fee_refund_params import (
    ApplicationFeeRefundParams as ApplicationFeeRefundParams,
)
from stripe._application_fee_refund_retrieve_params import (
    ApplicationFeeRefundRetrieveParams as ApplicationFeeRefundRetrieveParams,
)
from stripe._application_fee_refund_service import (
    ApplicationFeeRefundService as ApplicationFeeRefundService,
)
from stripe._application_fee_refund_update_params import (
    ApplicationFeeRefundUpdateParams as ApplicationFeeRefundUpdateParams,
)
from stripe._application_fee_retrieve_params import (
    ApplicationFeeRetrieveParams as ApplicationFeeRetrieveParams,
)
from stripe._application_fee_retrieve_refund_params import (
    ApplicationFeeRetrieveRefundParams as ApplicationFeeRetrieveRefundParams,
)
from stripe._application_fee_service import (
    ApplicationFeeService as ApplicationFeeService,
)
from stripe._apps_service import AppsService as AppsService
from stripe._balance import Balance as Balance
from stripe._balance_retrieve_params import (
    BalanceRetrieveParams as BalanceRetrieveParams,
)
from stripe._balance_service import BalanceService as BalanceService
from stripe._balance_settings import BalanceSettings as BalanceSettings
from stripe._balance_settings_modify_params import (
    BalanceSettingsModifyParams as BalanceSettingsModifyParams,
)
from stripe._balance_settings_retrieve_params import (
    BalanceSettingsRetrieveParams as BalanceSettingsRetrieveParams,
)
from stripe._balance_settings_service import (
    BalanceSettingsService as BalanceSettingsService,
)
from stripe._balance_settings_update_params import (
    BalanceSettingsUpdateParams as BalanceSettingsUpdateParams,
)
from stripe._balance_transaction import (
    BalanceTransaction as BalanceTransaction,
)
from stripe._balance_transaction_list_params import (
    BalanceTransactionListParams as BalanceTransactionListParams,
)
from stripe._balance_transaction_retrieve_params import (
    BalanceTransactionRetrieveParams as BalanceTransactionRetrieveParams,
)
from stripe._balance_transaction_service import (
    BalanceTransactionService as BalanceTransactionService,
)
from stripe._bank_account import BankAccount as BankAccount
from stripe._bank_account_delete_params import (
    BankAccountDeleteParams as BankAccountDeleteParams,
)
from stripe._billing_portal_service import (
    BillingPortalService as BillingPortalService,
)
from stripe._billing_service import BillingService as BillingService
from stripe._capability import Capability as Capability
from stripe._card import Card as Card
from stripe._card_delete_params import CardDeleteParams as CardDeleteParams
from stripe._cash_balance import CashBalance as CashBalance
from stripe._charge import Charge as Charge
from stripe._charge_capture_params import (
    ChargeCaptureParams as ChargeCaptureParams,
)
from stripe._charge_create_params import (
    ChargeCreateParams as ChargeCreateParams,
)
from stripe._charge_list_params import ChargeListParams as ChargeListParams
from stripe._charge_list_refunds_params import (
    ChargeListRefundsParams as ChargeListRefundsParams,
)
from stripe._charge_modify_params import (
    ChargeModifyParams as ChargeModifyParams,
)
from stripe._charge_retrieve_params import (
    ChargeRetrieveParams as ChargeRetrieveParams,
)
from stripe._charge_retrieve_refund_params import (
    ChargeRetrieveRefundParams as ChargeRetrieveRefundParams,
)
from stripe._charge_search_params import (
    ChargeSearchParams as ChargeSearchParams,
)
from stripe._charge_service import ChargeService as ChargeService
from stripe._charge_update_params import (
    ChargeUpdateParams as ChargeUpdateParams,
)
from stripe._checkout_service import CheckoutService as CheckoutService
from stripe._climate_service import ClimateService as ClimateService
from stripe._confirmation_token import ConfirmationToken as ConfirmationToken
from stripe._confirmation_token_create_params import (
    ConfirmationTokenCreateParams as ConfirmationTokenCreateParams,
)
from stripe._confirmation_token_retrieve_params import (
    ConfirmationTokenRetrieveParams as ConfirmationTokenRetrieveParams,
)
from stripe._confirmation_token_service import (
    ConfirmationTokenService as ConfirmationTokenService,
)
from stripe._connect_collection_transfer import (
    ConnectCollectionTransfer as ConnectCollectionTransfer,
)
from stripe._country_spec import CountrySpec as CountrySpec
from stripe._country_spec_list_params import (
    CountrySpecListParams as CountrySpecListParams,
)
from stripe._country_spec_retrieve_params import (
    CountrySpecRetrieveParams as CountrySpecRetrieveParams,
)
from stripe._country_spec_service import (
    CountrySpecService as CountrySpecService,
)
from stripe._coupon import Coupon as Coupon
from stripe._coupon_create_params import (
    CouponCreateParams as CouponCreateParams,
)
from stripe._coupon_delete_params import (
    CouponDeleteParams as CouponDeleteParams,
)
from stripe._coupon_list_params import CouponListParams as CouponListParams
from stripe._coupon_modify_params import (
    CouponModifyParams as CouponModifyParams,
)
from stripe._coupon_retrieve_params import (
    CouponRetrieveParams as CouponRetrieveParams,
)
from stripe._coupon_service import CouponService as CouponService
from stripe._coupon_update_params import (
    CouponUpdateParams as CouponUpdateParams,
)
from stripe._credit_note import CreditNote as CreditNote
from stripe._credit_note_create_params import (
    CreditNoteCreateParams as CreditNoteCreateParams,
)
from stripe._credit_note_line_item import (
    CreditNoteLineItem as CreditNoteLineItem,
)
from stripe._credit_note_line_item_list_params import (
    CreditNoteLineItemListParams as CreditNoteLineItemListParams,
)
from stripe._credit_note_line_item_service import (
    CreditNoteLineItemService as CreditNoteLineItemService,
)
from stripe._credit_note_list_lines_params import (
    CreditNoteListLinesParams as CreditNoteListLinesParams,
)
from stripe._credit_note_list_params import (
    CreditNoteListParams as CreditNoteListParams,
)
from stripe._credit_note_modify_params import (
    CreditNoteModifyParams as CreditNoteModifyParams,
)
from stripe._credit_note_preview_lines_list_params import (
    CreditNotePreviewLinesListParams as CreditNotePreviewLinesListParams,
)
from stripe._credit_note_preview_lines_params import (
    CreditNotePreviewLinesParams as CreditNotePreviewLinesParams,
)
from stripe._credit_note_preview_lines_service import (
    CreditNotePreviewLinesService as CreditNotePreviewLinesService,
)
from stripe._credit_note_preview_params import (
    CreditNotePreviewParams as CreditNotePreviewParams,
)
from stripe._credit_note_retrieve_params import (
    CreditNoteRetrieveParams as CreditNoteRetrieveParams,
)
from stripe._credit_note_service import CreditNoteService as CreditNoteService
from stripe._credit_note_update_params import (
    CreditNoteUpdateParams as CreditNoteUpdateParams,
)
from stripe._credit_note_void_credit_note_params import (
    CreditNoteVoidCreditNoteParams as CreditNoteVoidCreditNoteParams,
)
from stripe._customer import Customer as Customer
from stripe._customer_balance_transaction import (
    CustomerBalanceTransaction as CustomerBalanceTransaction,
)
from stripe._customer_balance_transaction_create_params import (
    CustomerBalanceTransactionCreateParams as CustomerBalanceTransactionCreateParams,
)
from stripe._customer_balance_transaction_list_params import (
    CustomerBalanceTransactionListParams as CustomerBalanceTransactionListParams,
)
from stripe._customer_balance_transaction_retrieve_params import (
    CustomerBalanceTransactionRetrieveParams as CustomerBalanceTransactionRetrieveParams,
)
from stripe._customer_balance_transaction_service import (
    CustomerBalanceTransactionService as CustomerBalanceTransactionService,
)
from stripe._customer_balance_transaction_update_params import (
    CustomerBalanceTransactionUpdateParams as CustomerBalanceTransactionUpdateParams,
)
from stripe._customer_cash_balance_retrieve_params import (
    CustomerCashBalanceRetrieveParams as CustomerCashBalanceRetrieveParams,
)
from stripe._customer_cash_balance_service import (
    CustomerCashBalanceService as CustomerCashBalanceService,
)
from stripe._customer_cash_balance_transaction import (
    CustomerCashBalanceTransaction as CustomerCashBalanceTransaction,
)
from stripe._customer_cash_balance_transaction_list_params import (
    CustomerCashBalanceTransactionListParams as CustomerCashBalanceTransactionListParams,
)
from stripe._customer_cash_balance_transaction_retrieve_params import (
    CustomerCashBalanceTransactionRetrieveParams as CustomerCashBalanceTransactionRetrieveParams,
)
from stripe._customer_cash_balance_transaction_service import (
    CustomerCashBalanceTransactionService as CustomerCashBalanceTransactionService,
)
from stripe._customer_cash_balance_update_params import (
    CustomerCashBalanceUpdateParams as CustomerCashBalanceUpdateParams,
)
from stripe._customer_create_balance_transaction_params import (
    CustomerCreateBalanceTransactionParams as CustomerCreateBalanceTransactionParams,
)
from stripe._customer_create_funding_instructions_params import (
    CustomerCreateFundingInstructionsParams as CustomerCreateFundingInstructionsParams,
)
from stripe._customer_create_params import (
    CustomerCreateParams as CustomerCreateParams,
)
from stripe._customer_create_source_params import (
    CustomerCreateSourceParams as CustomerCreateSourceParams,
)
from stripe._customer_create_tax_id_params import (
    CustomerCreateTaxIdParams as CustomerCreateTaxIdParams,
)
from stripe._customer_delete_discount_params import (
    CustomerDeleteDiscountParams as CustomerDeleteDiscountParams,
)
from stripe._customer_delete_params import (
    CustomerDeleteParams as CustomerDeleteParams,
)
from stripe._customer_delete_source_params import (
    CustomerDeleteSourceParams as CustomerDeleteSourceParams,
)
from stripe._customer_delete_tax_id_params import (
    CustomerDeleteTaxIdParams as CustomerDeleteTaxIdParams,
)
from stripe._customer_fund_cash_balance_params import (
    CustomerFundCashBalanceParams as CustomerFundCashBalanceParams,
)
from stripe._customer_funding_instructions_create_params import (
    CustomerFundingInstructionsCreateParams as CustomerFundingInstructionsCreateParams,
)
from stripe._customer_funding_instructions_service import (
    CustomerFundingInstructionsService as CustomerFundingInstructionsService,
)
from stripe._customer_list_balance_transactions_params import (
    CustomerListBalanceTransactionsParams as CustomerListBalanceTransactionsParams,
)
from stripe._customer_list_cash_balance_transactions_params import (
    CustomerListCashBalanceTransactionsParams as CustomerListCashBalanceTransactionsParams,
)
from stripe._customer_list_params import (
    CustomerListParams as CustomerListParams,
)
from stripe._customer_list_payment_methods_params import (
    CustomerListPaymentMethodsParams as CustomerListPaymentMethodsParams,
)
from stripe._customer_list_sources_params import (
    CustomerListSourcesParams as CustomerListSourcesParams,
)
from stripe._customer_list_tax_ids_params import (
    CustomerListTaxIdsParams as CustomerListTaxIdsParams,
)
from stripe._customer_modify_balance_transaction_params import (
    CustomerModifyBalanceTransactionParams as CustomerModifyBalanceTransactionParams,
)
from stripe._customer_modify_cash_balance_params import (
    CustomerModifyCashBalanceParams as CustomerModifyCashBalanceParams,
)
from stripe._customer_modify_params import (
    CustomerModifyParams as CustomerModifyParams,
)
from stripe._customer_modify_source_params import (
    CustomerModifySourceParams as CustomerModifySourceParams,
)
from stripe._customer_payment_method_list_params import (
    CustomerPaymentMethodListParams as CustomerPaymentMethodListParams,
)
from stripe._customer_payment_method_retrieve_params import (
    CustomerPaymentMethodRetrieveParams as CustomerPaymentMethodRetrieveParams,
)
from stripe._customer_payment_method_service import (
    CustomerPaymentMethodService as CustomerPaymentMethodService,
)
from stripe._customer_payment_source_create_params import (
    CustomerPaymentSourceCreateParams as CustomerPaymentSourceCreateParams,
)
from stripe._customer_payment_source_delete_params import (
    CustomerPaymentSourceDeleteParams as CustomerPaymentSourceDeleteParams,
)
from stripe._customer_payment_source_list_params import (
    CustomerPaymentSourceListParams as CustomerPaymentSourceListParams,
)
from stripe._customer_payment_source_retrieve_params import (
    CustomerPaymentSourceRetrieveParams as CustomerPaymentSourceRetrieveParams,
)
from stripe._customer_payment_source_service import (
    CustomerPaymentSourceService as CustomerPaymentSourceService,
)
from stripe._customer_payment_source_update_params import (
    CustomerPaymentSourceUpdateParams as CustomerPaymentSourceUpdateParams,
)
from stripe._customer_payment_source_verify_params import (
    CustomerPaymentSourceVerifyParams as CustomerPaymentSourceVerifyParams,
)
from stripe._customer_retrieve_balance_transaction_params import (
    CustomerRetrieveBalanceTransactionParams as CustomerRetrieveBalanceTransactionParams,
)
from stripe._customer_retrieve_cash_balance_params import (
    CustomerRetrieveCashBalanceParams as CustomerRetrieveCashBalanceParams,
)
from stripe._customer_retrieve_cash_balance_transaction_params import (
    CustomerRetrieveCashBalanceTransactionParams as CustomerRetrieveCashBalanceTransactionParams,
)
from stripe._customer_retrieve_params import (
    CustomerRetrieveParams as CustomerRetrieveParams,
)
from stripe._customer_retrieve_payment_method_params import (
    CustomerRetrievePaymentMethodParams as CustomerRetrievePaymentMethodParams,
)
from stripe._customer_retrieve_source_params import (
    CustomerRetrieveSourceParams as CustomerRetrieveSourceParams,
)
from stripe._customer_retrieve_tax_id_params import (
    CustomerRetrieveTaxIdParams as CustomerRetrieveTaxIdParams,
)
from stripe._customer_search_params import (
    CustomerSearchParams as CustomerSearchParams,
)
from stripe._customer_service import CustomerService as CustomerService
from stripe._customer_session import CustomerSession as CustomerSession
from stripe._customer_session_create_params import (
    CustomerSessionCreateParams as CustomerSessionCreateParams,
)
from stripe._customer_session_service import (
    CustomerSessionService as CustomerSessionService,
)
from stripe._customer_tax_id_create_params import (
    CustomerTaxIdCreateParams as CustomerTaxIdCreateParams,
)
from stripe._customer_tax_id_delete_params import (
    CustomerTaxIdDeleteParams as CustomerTaxIdDeleteParams,
)
from stripe._customer_tax_id_list_params import (
    CustomerTaxIdListParams as CustomerTaxIdListParams,
)
from stripe._customer_tax_id_retrieve_params import (
    CustomerTaxIdRetrieveParams as CustomerTaxIdRetrieveParams,
)
from stripe._customer_tax_id_service import (
    CustomerTaxIdService as CustomerTaxIdService,
)
from stripe._customer_update_params import (
    CustomerUpdateParams as CustomerUpdateParams,
)
from stripe._discount import Discount as Discount
from stripe._dispute import Dispute as Dispute
from stripe._dispute_close_params import (
    DisputeCloseParams as DisputeCloseParams,
)
from stripe._dispute_list_params import DisputeListParams as DisputeListParams
from stripe._dispute_modify_params import (
    DisputeModifyParams as DisputeModifyParams,
)
from stripe._dispute_retrieve_params import (
    DisputeRetrieveParams as DisputeRetrieveParams,
)
from stripe._dispute_service import DisputeService as DisputeService
from stripe._dispute_update_params import (
    DisputeUpdateParams as DisputeUpdateParams,
)
from stripe._entitlements_service import (
    EntitlementsService as EntitlementsService,
)
from stripe._ephemeral_key import EphemeralKey as EphemeralKey
from stripe._ephemeral_key_create_params import (
    EphemeralKeyCreateParams as EphemeralKeyCreateParams,
)
from stripe._ephemeral_key_delete_params import (
    EphemeralKeyDeleteParams as EphemeralKeyDeleteParams,
)
from stripe._ephemeral_key_service import (
    EphemeralKeyService as EphemeralKeyService,
)
from stripe._error import (
    TemporarySessionExpiredError as TemporarySessionExpiredError,
)
from stripe._event import Event as Event
from stripe._event_list_params import EventListParams as EventListParams
from stripe._event_retrieve_params import (
    EventRetrieveParams as EventRetrieveParams,
)
from stripe._event_service import EventService as EventService
from stripe._exchange_rate import ExchangeRate as ExchangeRate
from stripe._exchange_rate_list_params import (
    ExchangeRateListParams as ExchangeRateListParams,
)
from stripe._exchange_rate_retrieve_params import (
    ExchangeRateRetrieveParams as ExchangeRateRetrieveParams,
)
from stripe._exchange_rate_service import (
    ExchangeRateService as ExchangeRateService,
)
from stripe._file import File as File
from stripe._file_create_params import FileCreateParams as FileCreateParams
from stripe._file_link import FileLink as FileLink
from stripe._file_link_create_params import (
    FileLinkCreateParams as FileLinkCreateParams,
)
from stripe._file_link_list_params import (
    FileLinkListParams as FileLinkListParams,
)
from stripe._file_link_modify_params import (
    FileLinkModifyParams as FileLinkModifyParams,
)
from stripe._file_link_retrieve_params import (
    FileLinkRetrieveParams as FileLinkRetrieveParams,
)
from stripe._file_link_service import FileLinkService as FileLinkService
from stripe._file_link_update_params import (
    FileLinkUpdateParams as FileLinkUpdateParams,
)
from stripe._file_list_params import FileListParams as FileListParams
from stripe._file_retrieve_params import (
    FileRetrieveParams as FileRetrieveParams,
)
from stripe._file_service import FileService as FileService
from stripe._financial_connections_service import (
    FinancialConnectionsService as FinancialConnectionsService,
)
from stripe._forwarding_service import ForwardingService as ForwardingService
from stripe._funding_instructions import (
    FundingInstructions as FundingInstructions,
)
from stripe._identity_service import IdentityService as IdentityService
from stripe._invoice import Invoice as Invoice
from stripe._invoice_add_lines_params import (
    InvoiceAddLinesParams as InvoiceAddLinesParams,
)
from stripe._invoice_attach_payment_params import (
    InvoiceAttachPaymentParams as InvoiceAttachPaymentParams,
)
from stripe._invoice_create_params import (
    InvoiceCreateParams as InvoiceCreateParams,
)
from stripe._invoice_create_preview_params import (
    InvoiceCreatePreviewParams as InvoiceCreatePreviewParams,
)
from stripe._invoice_delete_params import (
    InvoiceDeleteParams as InvoiceDeleteParams,
)
from stripe._invoice_finalize_invoice_params import (
    InvoiceFinalizeInvoiceParams as InvoiceFinalizeInvoiceParams,
)
from stripe._invoice_item import InvoiceItem as InvoiceItem
from stripe._invoice_item_create_params import (
    InvoiceItemCreateParams as InvoiceItemCreateParams,
)
from stripe._invoice_item_delete_params import (
    InvoiceItemDeleteParams as InvoiceItemDeleteParams,
)
from stripe._invoice_item_list_params import (
    InvoiceItemListParams as InvoiceItemListParams,
)
from stripe._invoice_item_modify_params import (
    InvoiceItemModifyParams as InvoiceItemModifyParams,
)
from stripe._invoice_item_retrieve_params import (
    InvoiceItemRetrieveParams as InvoiceItemRetrieveParams,
)
from stripe._invoice_item_service import (
    InvoiceItemService as InvoiceItemService,
)
from stripe._invoice_item_update_params import (
    InvoiceItemUpdateParams as InvoiceItemUpdateParams,
)
from stripe._invoice_line_item import InvoiceLineItem as InvoiceLineItem
from stripe._invoice_line_item_list_params import (
    InvoiceLineItemListParams as InvoiceLineItemListParams,
)
from stripe._invoice_line_item_modify_params import (
    InvoiceLineItemModifyParams as InvoiceLineItemModifyParams,
)
from stripe._invoice_line_item_service import (
    InvoiceLineItemService as InvoiceLineItemService,
)
from stripe._invoice_line_item_update_params import (
    InvoiceLineItemUpdateParams as InvoiceLineItemUpdateParams,
)
from stripe._invoice_list_lines_params import (
    InvoiceListLinesParams as InvoiceListLinesParams,
)
from stripe._invoice_list_params import InvoiceListParams as InvoiceListParams
from stripe._invoice_mark_uncollectible_params import (
    InvoiceMarkUncollectibleParams as InvoiceMarkUncollectibleParams,
)
from stripe._invoice_modify_params import (
    InvoiceModifyParams as InvoiceModifyParams,
)
from stripe._invoice_pay_params import InvoicePayParams as InvoicePayParams
from stripe._invoice_payment import InvoicePayment as InvoicePayment
from stripe._invoice_payment_list_params import (
    InvoicePaymentListParams as InvoicePaymentListParams,
)
from stripe._invoice_payment_retrieve_params import (
    InvoicePaymentRetrieveParams as InvoicePaymentRetrieveParams,
)
from stripe._invoice_payment_service import (
    InvoicePaymentService as InvoicePaymentService,
)
from stripe._invoice_remove_lines_params import (
    InvoiceRemoveLinesParams as InvoiceRemoveLinesParams,
)
from stripe._invoice_rendering_template import (
    InvoiceRenderingTemplate as InvoiceRenderingTemplate,
)
from stripe._invoice_rendering_template_archive_params import (
    InvoiceRenderingTemplateArchiveParams as InvoiceRenderingTemplateArchiveParams,
)
from stripe._invoice_rendering_template_list_params import (
    InvoiceRenderingTemplateListParams as InvoiceRenderingTemplateListParams,
)
from stripe._invoice_rendering_template_retrieve_params import (
    InvoiceRenderingTemplateRetrieveParams as InvoiceRenderingTemplateRetrieveParams,
)
from stripe._invoice_rendering_template_service import (
    InvoiceRenderingTemplateService as InvoiceRenderingTemplateService,
)
from stripe._invoice_rendering_template_unarchive_params import (
    InvoiceRenderingTemplateUnarchiveParams as InvoiceRenderingTemplateUnarchiveParams,
)
from stripe._invoice_retrieve_params import (
    InvoiceRetrieveParams as InvoiceRetrieveParams,
)
from stripe._invoice_search_params import (
    InvoiceSearchParams as InvoiceSearchParams,
)
from stripe._invoice_send_invoice_params import (
    InvoiceSendInvoiceParams as InvoiceSendInvoiceParams,
)
from stripe._invoice_service import InvoiceService as InvoiceService
from stripe._invoice_update_lines_params import (
    InvoiceUpdateLinesParams as InvoiceUpdateLinesParams,
)
from stripe._invoice_update_params import (
    InvoiceUpdateParams as InvoiceUpdateParams,
)
from stripe._invoice_void_invoice_params import (
    InvoiceVoidInvoiceParams as InvoiceVoidInvoiceParams,
)
from stripe._issuing_service import IssuingService as IssuingService
from stripe._line_item import LineItem as LineItem
from stripe._login_link import LoginLink as LoginLink
from stripe._mandate import Mandate as Mandate
from stripe._mandate_retrieve_params import (
    MandateRetrieveParams as MandateRetrieveParams,
)
from stripe._mandate_service import MandateService as MandateService
from stripe._payment_intent import PaymentIntent as PaymentIntent
from stripe._payment_intent_apply_customer_balance_params import (
    PaymentIntentApplyCustomerBalanceParams as PaymentIntentApplyCustomerBalanceParams,
)
from stripe._payment_intent_cancel_params import (
    PaymentIntentCancelParams as PaymentIntentCancelParams,
)
from stripe._payment_intent_capture_params import (
    PaymentIntentCaptureParams as PaymentIntentCaptureParams,
)
from stripe._payment_intent_confirm_params import (
    PaymentIntentConfirmParams as PaymentIntentConfirmParams,
)
from stripe._payment_intent_create_params import (
    PaymentIntentCreateParams as PaymentIntentCreateParams,
)
from stripe._payment_intent_increment_authorization_params import (
    PaymentIntentIncrementAuthorizationParams as PaymentIntentIncrementAuthorizationParams,
)
from stripe._payment_intent_list_params import (
    PaymentIntentListParams as PaymentIntentListParams,
)
from stripe._payment_intent_modify_params import (
    PaymentIntentModifyParams as PaymentIntentModifyParams,
)
from stripe._payment_intent_retrieve_params import (
    PaymentIntentRetrieveParams as PaymentIntentRetrieveParams,
)
from stripe._payment_intent_search_params import (
    PaymentIntentSearchParams as PaymentIntentSearchParams,
)
from stripe._payment_intent_service import (
    PaymentIntentService as PaymentIntentService,
)
from stripe._payment_intent_update_params import (
    PaymentIntentUpdateParams as PaymentIntentUpdateParams,
)
from stripe._payment_intent_verify_microdeposits_params import (
    PaymentIntentVerifyMicrodepositsParams as PaymentIntentVerifyMicrodepositsParams,
)
from stripe._payment_link import PaymentLink as PaymentLink
from stripe._payment_link_create_params import (
    PaymentLinkCreateParams as PaymentLinkCreateParams,
)
from stripe._payment_link_line_item_list_params import (
    PaymentLinkLineItemListParams as PaymentLinkLineItemListParams,
)
from stripe._payment_link_line_item_service import (
    PaymentLinkLineItemService as PaymentLinkLineItemService,
)
from stripe._payment_link_list_line_items_params import (
    PaymentLinkListLineItemsParams as PaymentLinkListLineItemsParams,
)
from stripe._payment_link_list_params import (
    PaymentLinkListParams as PaymentLinkListParams,
)
from stripe._payment_link_modify_params import (
    PaymentLinkModifyParams as PaymentLinkModifyParams,
)
from stripe._payment_link_retrieve_params import (
    PaymentLinkRetrieveParams as PaymentLinkRetrieveParams,
)
from stripe._payment_link_service import (
    PaymentLinkService as PaymentLinkService,
)
from stripe._payment_link_update_params import (
    PaymentLinkUpdateParams as PaymentLinkUpdateParams,
)
from stripe._payment_method import PaymentMethod as PaymentMethod
from stripe._payment_method_attach_params import (
    PaymentMethodAttachParams as PaymentMethodAttachParams,
)
from stripe._payment_method_configuration import (
    PaymentMethodConfiguration as PaymentMethodConfiguration,
)
from stripe._payment_method_configuration_create_params import (
    PaymentMethodConfigurationCreateParams as PaymentMethodConfigurationCreateParams,
)
from stripe._payment_method_configuration_list_params import (
    PaymentMethodConfigurationListParams as PaymentMethodConfigurationListParams,
)
from stripe._payment_method_configuration_modify_params import (
    PaymentMethodConfigurationModifyParams as PaymentMethodConfigurationModifyParams,
)
from stripe._payment_method_configuration_retrieve_params import (
    PaymentMethodConfigurationRetrieveParams as PaymentMethodConfigurationRetrieveParams,
)
from stripe._payment_method_configuration_service import (
    PaymentMethodConfigurationService as PaymentMethodConfigurationService,
)
from stripe._payment_method_configuration_update_params import (
    PaymentMethodConfigurationUpdateParams as PaymentMethodConfigurationUpdateParams,
)
from stripe._payment_method_create_params import (
    PaymentMethodCreateParams as PaymentMethodCreateParams,
)
from stripe._payment_method_detach_params import (
    PaymentMethodDetachParams as PaymentMethodDetachParams,
)
from stripe._payment_method_domain import (
    PaymentMethodDomain as PaymentMethodDomain,
)
from stripe._payment_method_domain_create_params import (
    PaymentMethodDomainCreateParams as PaymentMethodDomainCreateParams,
)
from stripe._payment_method_domain_list_params import (
    PaymentMethodDomainListParams as PaymentMethodDomainListParams,
)
from stripe._payment_method_domain_modify_params import (
    PaymentMethodDomainModifyParams as PaymentMethodDomainModifyParams,
)
from stripe._payment_method_domain_retrieve_params import (
    PaymentMethodDomainRetrieveParams as PaymentMethodDomainRetrieveParams,
)
from stripe._payment_method_domain_service import (
    PaymentMethodDomainService as PaymentMethodDomainService,
)
from stripe._payment_method_domain_update_params import (
    PaymentMethodDomainUpdateParams as PaymentMethodDomainUpdateParams,
)
from stripe._payment_method_domain_validate_params import (
    PaymentMethodDomainValidateParams as PaymentMethodDomainValidateParams,
)
from stripe._payment_method_list_params import (
    PaymentMethodListParams as PaymentMethodListParams,
)
from stripe._payment_method_modify_params import (
    PaymentMethodModifyParams as PaymentMethodModifyParams,
)
from stripe._payment_method_retrieve_params import (
    PaymentMethodRetrieveParams as PaymentMethodRetrieveParams,
)
from stripe._payment_method_service import (
    PaymentMethodService as PaymentMethodService,
)
from stripe._payment_method_update_params import (
    PaymentMethodUpdateParams as PaymentMethodUpdateParams,
)
from stripe._payout import Payout as Payout
from stripe._payout_cancel_params import (
    PayoutCancelParams as PayoutCancelParams,
)
from stripe._payout_create_params import (
    PayoutCreateParams as PayoutCreateParams,
)
from stripe._payout_list_params import PayoutListParams as PayoutListParams
from stripe._payout_modify_params import (
    PayoutModifyParams as PayoutModifyParams,
)
from stripe._payout_retrieve_params import (
    PayoutRetrieveParams as PayoutRetrieveParams,
)
from stripe._payout_reverse_params import (
    PayoutReverseParams as PayoutReverseParams,
)
from stripe._payout_service import PayoutService as PayoutService
from stripe._payout_update_params import (
    PayoutUpdateParams as PayoutUpdateParams,
)
from stripe._person import Person as Person
from stripe._plan import Plan as Plan
from stripe._plan_create_params import PlanCreateParams as PlanCreateParams
from stripe._plan_delete_params import PlanDeleteParams as PlanDeleteParams
from stripe._plan_list_params import PlanListParams as PlanListParams
from stripe._plan_modify_params import PlanModifyParams as PlanModifyParams
from stripe._plan_retrieve_params import (
    PlanRetrieveParams as PlanRetrieveParams,
)
from stripe._plan_service import PlanService as PlanService
from stripe._plan_update_params import PlanUpdateParams as PlanUpdateParams
from stripe._price import Price as Price
from stripe._price_create_params import PriceCreateParams as PriceCreateParams
from stripe._price_list_params import PriceListParams as PriceListParams
from stripe._price_modify_params import PriceModifyParams as PriceModifyParams
from stripe._price_retrieve_params import (
    PriceRetrieveParams as PriceRetrieveParams,
)
from stripe._price_search_params import PriceSearchParams as PriceSearchParams
from stripe._price_service import PriceService as PriceService
from stripe._price_update_params import PriceUpdateParams as PriceUpdateParams
from stripe._product import Product as Product
from stripe._product_create_feature_params import (
    ProductCreateFeatureParams as ProductCreateFeatureParams,
)
from stripe._product_create_params import (
    ProductCreateParams as ProductCreateParams,
)
from stripe._product_delete_feature_params import (
    ProductDeleteFeatureParams as ProductDeleteFeatureParams,
)
from stripe._product_delete_params import (
    ProductDeleteParams as ProductDeleteParams,
)
from stripe._product_feature import ProductFeature as ProductFeature
from stripe._product_feature_create_params import (
    ProductFeatureCreateParams as ProductFeatureCreateParams,
)
from stripe._product_feature_delete_params import (
    ProductFeatureDeleteParams as ProductFeatureDeleteParams,
)
from stripe._product_feature_list_params import (
    ProductFeatureListParams as ProductFeatureListParams,
)
from stripe._product_feature_retrieve_params import (
    ProductFeatureRetrieveParams as ProductFeatureRetrieveParams,
)
from stripe._product_feature_service import (
    ProductFeatureService as ProductFeatureService,
)
from stripe._product_list_features_params import (
    ProductListFeaturesParams as ProductListFeaturesParams,
)
from stripe._product_list_params import ProductListParams as ProductListParams
from stripe._product_modify_params import (
    ProductModifyParams as ProductModifyParams,
)
from stripe._product_retrieve_feature_params import (
    ProductRetrieveFeatureParams as ProductRetrieveFeatureParams,
)
from stripe._product_retrieve_params import (
    ProductRetrieveParams as ProductRetrieveParams,
)
from stripe._product_search_params import (
    ProductSearchParams as ProductSearchParams,
)
from stripe._product_service import ProductService as ProductService
from stripe._product_update_params import (
    ProductUpdateParams as ProductUpdateParams,
)
from stripe._promotion_code import PromotionCode as PromotionCode
from stripe._promotion_code_create_params import (
    PromotionCodeCreateParams as PromotionCodeCreateParams,
)
from stripe._promotion_code_list_params import (
    PromotionCodeListParams as PromotionCodeListParams,
)
from stripe._promotion_code_modify_params import (
    PromotionCodeModifyParams as PromotionCodeModifyParams,
)
from stripe._promotion_code_retrieve_params import (
    PromotionCodeRetrieveParams as PromotionCodeRetrieveParams,
)
from stripe._promotion_code_service import (
    PromotionCodeService as PromotionCodeService,
)
from stripe._promotion_code_update_params import (
    PromotionCodeUpdateParams as PromotionCodeUpdateParams,
)
from stripe._quote import Quote as Quote
from stripe._quote_accept_params import QuoteAcceptParams as QuoteAcceptParams
from stripe._quote_cancel_params import QuoteCancelParams as QuoteCancelParams
from stripe._quote_computed_upfront_line_items_list_params import (
    QuoteComputedUpfrontLineItemsListParams as QuoteComputedUpfrontLineItemsListParams,
)
from stripe._quote_computed_upfront_line_items_service import (
    QuoteComputedUpfrontLineItemsService as QuoteComputedUpfrontLineItemsService,
)
from stripe._quote_create_params import QuoteCreateParams as QuoteCreateParams
from stripe._quote_finalize_quote_params import (
    QuoteFinalizeQuoteParams as QuoteFinalizeQuoteParams,
)
from stripe._quote_line_item_list_params import (
    QuoteLineItemListParams as QuoteLineItemListParams,
)
from stripe._quote_line_item_service import (
    QuoteLineItemService as QuoteLineItemService,
)
from stripe._quote_list_computed_upfront_line_items_params import (
    QuoteListComputedUpfrontLineItemsParams as QuoteListComputedUpfrontLineItemsParams,
)
from stripe._quote_list_line_items_params import (
    QuoteListLineItemsParams as QuoteListLineItemsParams,
)
from stripe._quote_list_params import QuoteListParams as QuoteListParams
from stripe._quote_modify_params import QuoteModifyParams as QuoteModifyParams
from stripe._quote_pdf_params import QuotePdfParams as QuotePdfParams
from stripe._quote_retrieve_params import (
    QuoteRetrieveParams as QuoteRetrieveParams,
)
from stripe._quote_service import QuoteService as QuoteService
from stripe._quote_update_params import QuoteUpdateParams as QuoteUpdateParams
from stripe._radar_service import RadarService as RadarService
from stripe._refund import Refund as Refund
from stripe._refund_cancel_params import (
    RefundCancelParams as RefundCancelParams,
)
from stripe._refund_create_params import (
    RefundCreateParams as RefundCreateParams,
)
from stripe._refund_expire_params import (
    RefundExpireParams as RefundExpireParams,
)
from stripe._refund_list_params import RefundListParams as RefundListParams
from stripe._refund_modify_params import (
    RefundModifyParams as RefundModifyParams,
)
from stripe._refund_retrieve_params import (
    RefundRetrieveParams as RefundRetrieveParams,
)
from stripe._refund_service import RefundService as RefundService
from stripe._refund_update_params import (
    RefundUpdateParams as RefundUpdateParams,
)
from stripe._reporting_service import ReportingService as ReportingService
from stripe._reserve_transaction import (
    ReserveTransaction as ReserveTransaction,
)
from stripe._reversal import Reversal as Reversal
from stripe._review import Review as Review
from stripe._review_approve_params import (
    ReviewApproveParams as ReviewApproveParams,
)
from stripe._review_list_params import ReviewListParams as ReviewListParams
from stripe._review_retrieve_params import (
    ReviewRetrieveParams as ReviewRetrieveParams,
)
from stripe._review_service import ReviewService as ReviewService
from stripe._setup_attempt import SetupAttempt as SetupAttempt
from stripe._setup_attempt_list_params import (
    SetupAttemptListParams as SetupAttemptListParams,
)
from stripe._setup_attempt_service import (
    SetupAttemptService as SetupAttemptService,
)
from stripe._setup_intent import SetupIntent as SetupIntent
from stripe._setup_intent_cancel_params import (
    SetupIntentCancelParams as SetupIntentCancelParams,
)
from stripe._setup_intent_confirm_params import (
    SetupIntentConfirmParams as SetupIntentConfirmParams,
)
from stripe._setup_intent_create_params import (
    SetupIntentCreateParams as SetupIntentCreateParams,
)
from stripe._setup_intent_list_params import (
    SetupIntentListParams as SetupIntentListParams,
)
from stripe._setup_intent_modify_params import (
    SetupIntentModifyParams as SetupIntentModifyParams,
)
from stripe._setup_intent_retrieve_params import (
    SetupIntentRetrieveParams as SetupIntentRetrieveParams,
)
from stripe._setup_intent_service import (
    SetupIntentService as SetupIntentService,
)
from stripe._setup_intent_update_params import (
    SetupIntentUpdateParams as SetupIntentUpdateParams,
)
from stripe._setup_intent_verify_microdeposits_params import (
    SetupIntentVerifyMicrodepositsParams as SetupIntentVerifyMicrodepositsParams,
)
from stripe._shipping_rate import ShippingRate as ShippingRate
from stripe._shipping_rate_create_params import (
    ShippingRateCreateParams as ShippingRateCreateParams,
)
from stripe._shipping_rate_list_params import (
    ShippingRateListParams as ShippingRateListParams,
)
from stripe._shipping_rate_modify_params import (
    ShippingRateModifyParams as ShippingRateModifyParams,
)
from stripe._shipping_rate_retrieve_params import (
    ShippingRateRetrieveParams as ShippingRateRetrieveParams,
)
from stripe._shipping_rate_service import (
    ShippingRateService as ShippingRateService,
)
from stripe._shipping_rate_update_params import (
    ShippingRateUpdateParams as ShippingRateUpdateParams,
)
from stripe._sigma_service import SigmaService as SigmaService
from stripe._source import Source as Source
from stripe._source_create_params import (
    SourceCreateParams as SourceCreateParams,
)
from stripe._source_detach_params import (
    SourceDetachParams as SourceDetachParams,
)
from stripe._source_list_source_transactions_params import (
    SourceListSourceTransactionsParams as SourceListSourceTransactionsParams,
)
from stripe._source_mandate_notification import (
    SourceMandateNotification as SourceMandateNotification,
)
from stripe._source_modify_params import (
    SourceModifyParams as SourceModifyParams,
)
from stripe._source_retrieve_params import (
    SourceRetrieveParams as SourceRetrieveParams,
)
from stripe._source_service import SourceService as SourceService
from stripe._source_transaction import SourceTransaction as SourceTransaction
from stripe._source_transaction_list_params import (
    SourceTransactionListParams as SourceTransactionListParams,
)
from stripe._source_transaction_service import (
    SourceTransactionService as SourceTransactionService,
)
from stripe._source_update_params import (
    SourceUpdateParams as SourceUpdateParams,
)
from stripe._source_verify_params import (
    SourceVerifyParams as SourceVerifyParams,
)
from stripe._subscription import Subscription as Subscription
from stripe._subscription_cancel_params import (
    SubscriptionCancelParams as SubscriptionCancelParams,
)
from stripe._subscription_create_params import (
    SubscriptionCreateParams as SubscriptionCreateParams,
)
from stripe._subscription_delete_discount_params import (
    SubscriptionDeleteDiscountParams as SubscriptionDeleteDiscountParams,
)
from stripe._subscription_item import SubscriptionItem as SubscriptionItem
from stripe._subscription_item_create_params import (
    SubscriptionItemCreateParams as SubscriptionItemCreateParams,
)
from stripe._subscription_item_delete_params import (
    SubscriptionItemDeleteParams as SubscriptionItemDeleteParams,
)
from stripe._subscription_item_list_params import (
    SubscriptionItemListParams as SubscriptionItemListParams,
)
from stripe._subscription_item_modify_params import (
    SubscriptionItemModifyParams as SubscriptionItemModifyParams,
)
from stripe._subscription_item_retrieve_params import (
    SubscriptionItemRetrieveParams as SubscriptionItemRetrieveParams,
)
from stripe._subscription_item_service import (
    SubscriptionItemService as SubscriptionItemService,
)
from stripe._subscription_item_update_params import (
    SubscriptionItemUpdateParams as SubscriptionItemUpdateParams,
)
from stripe._subscription_list_params import (
    SubscriptionListParams as SubscriptionListParams,
)
from stripe._subscription_migrate_params import (
    SubscriptionMigrateParams as SubscriptionMigrateParams,
)
from stripe._subscription_modify_params import (
    SubscriptionModifyParams as SubscriptionModifyParams,
)
from stripe._subscription_resume_params import (
    SubscriptionResumeParams as SubscriptionResumeParams,
)
from stripe._subscription_retrieve_params import (
    SubscriptionRetrieveParams as SubscriptionRetrieveParams,
)
from stripe._subscription_schedule import (
    SubscriptionSchedule as SubscriptionSchedule,
)
from stripe._subscription_schedule_cancel_params import (
    SubscriptionScheduleCancelParams as SubscriptionScheduleCancelParams,
)
from stripe._subscription_schedule_create_params import (
    SubscriptionScheduleCreateParams as SubscriptionScheduleCreateParams,
)
from stripe._subscription_schedule_list_params import (
    SubscriptionScheduleListParams as SubscriptionScheduleListParams,
)
from stripe._subscription_schedule_modify_params import (
    SubscriptionScheduleModifyParams as SubscriptionScheduleModifyParams,
)
from stripe._subscription_schedule_release_params import (
    SubscriptionScheduleReleaseParams as SubscriptionScheduleReleaseParams,
)
from stripe._subscription_schedule_retrieve_params import (
    SubscriptionScheduleRetrieveParams as SubscriptionScheduleRetrieveParams,
)
from stripe._subscription_schedule_service import (
    SubscriptionScheduleService as SubscriptionScheduleService,
)
from stripe._subscription_schedule_update_params import (
    SubscriptionScheduleUpdateParams as SubscriptionScheduleUpdateParams,
)
from stripe._subscription_search_params import (
    SubscriptionSearchParams as SubscriptionSearchParams,
)
from stripe._subscription_service import (
    SubscriptionService as SubscriptionService,
)
from stripe._subscription_update_params import (
    SubscriptionUpdateParams as SubscriptionUpdateParams,
)
from stripe._tax_code import TaxCode as TaxCode
from stripe._tax_code_list_params import TaxCodeListParams as TaxCodeListParams
from stripe._tax_code_retrieve_params import (
    TaxCodeRetrieveParams as TaxCodeRetrieveParams,
)
from stripe._tax_code_service import TaxCodeService as TaxCodeService
from stripe._tax_deducted_at_source import (
    TaxDeductedAtSource as TaxDeductedAtSource,
)
from stripe._tax_id import TaxId as TaxId
from stripe._tax_id_create_params import TaxIdCreateParams as TaxIdCreateParams
from stripe._tax_id_delete_params import TaxIdDeleteParams as TaxIdDeleteParams
from stripe._tax_id_list_params import TaxIdListParams as TaxIdListParams
from stripe._tax_id_retrieve_params import (
    TaxIdRetrieveParams as TaxIdRetrieveParams,
)
from stripe._tax_id_service import TaxIdService as TaxIdService
from stripe._tax_rate import TaxRate as TaxRate
from stripe._tax_rate_create_params import (
    TaxRateCreateParams as TaxRateCreateParams,
)
from stripe._tax_rate_list_params import TaxRateListParams as TaxRateListParams
from stripe._tax_rate_modify_params import (
    TaxRateModifyParams as TaxRateModifyParams,
)
from stripe._tax_rate_retrieve_params import (
    TaxRateRetrieveParams as TaxRateRetrieveParams,
)
from stripe._tax_rate_service import TaxRateService as TaxRateService
from stripe._tax_rate_update_params import (
    TaxRateUpdateParams as TaxRateUpdateParams,
)
from stripe._tax_service import TaxService as TaxService
from stripe._terminal_service import TerminalService as TerminalService
from stripe._test_helpers_service import (
    TestHelpersService as TestHelpersService,
)
from stripe._token import Token as Token
from stripe._token_create_params import TokenCreateParams as TokenCreateParams
from stripe._token_retrieve_params import (
    TokenRetrieveParams as TokenRetrieveParams,
)
from stripe._token_service import TokenService as TokenService
from stripe._topup import Topup as Topup
from stripe._topup_cancel_params import TopupCancelParams as TopupCancelParams
from stripe._topup_create_params import TopupCreateParams as TopupCreateParams
from stripe._topup_list_params import TopupListParams as TopupListParams
from stripe._topup_modify_params import TopupModifyParams as TopupModifyParams
from stripe._topup_retrieve_params import (
    TopupRetrieveParams as TopupRetrieveParams,
)
from stripe._topup_service import TopupService as TopupService
from stripe._topup_update_params import TopupUpdateParams as TopupUpdateParams
from stripe._transfer import Transfer as Transfer
from stripe._transfer_create_params import (
    TransferCreateParams as TransferCreateParams,
)
from stripe._transfer_create_reversal_params import (
    TransferCreateReversalParams as TransferCreateReversalParams,
)
from stripe._transfer_list_params import (
    TransferListParams as TransferListParams,
)
from stripe._transfer_list_reversals_params import (
    TransferListReversalsParams as TransferListReversalsParams,
)
from stripe._transfer_modify_params import (
    TransferModifyParams as TransferModifyParams,
)
from stripe._transfer_modify_reversal_params import (
    TransferModifyReversalParams as TransferModifyReversalParams,
)
from stripe._transfer_retrieve_params import (
    TransferRetrieveParams as TransferRetrieveParams,
)
from stripe._transfer_retrieve_reversal_params import (
    TransferRetrieveReversalParams as TransferRetrieveReversalParams,
)
from stripe._transfer_reversal_create_params import (
    TransferReversalCreateParams as TransferReversalCreateParams,
)
from stripe._transfer_reversal_list_params import (
    TransferReversalListParams as TransferReversalListParams,
)
from stripe._transfer_reversal_retrieve_params import (
    TransferReversalRetrieveParams as TransferReversalRetrieveParams,
)
from stripe._transfer_reversal_service import (
    TransferReversalService as TransferReversalService,
)
from stripe._transfer_reversal_update_params import (
    TransferReversalUpdateParams as TransferReversalUpdateParams,
)
from stripe._transfer_service import TransferService as TransferService
from stripe._transfer_update_params import (
    TransferUpdateParams as TransferUpdateParams,
)
from stripe._treasury_service import TreasuryService as TreasuryService
from stripe._v1_services import V1Services as V1Services
from stripe._v2_services import V2Services as V2Services
from stripe._webhook_endpoint import WebhookEndpoint as WebhookEndpoint
from stripe._webhook_endpoint_create_params import (
    WebhookEndpointCreateParams as WebhookEndpointCreateParams,
)
from stripe._webhook_endpoint_delete_params import (
    WebhookEndpointDeleteParams as WebhookEndpointDeleteParams,
)
from stripe._webhook_endpoint_list_params import (
    WebhookEndpointListParams as WebhookEndpointListParams,
)
from stripe._webhook_endpoint_modify_params import (
    WebhookEndpointModifyParams as WebhookEndpointModifyParams,
)
from stripe._webhook_endpoint_retrieve_params import (
    WebhookEndpointRetrieveParams as WebhookEndpointRetrieveParams,
)
from stripe._webhook_endpoint_service import (
    WebhookEndpointService as WebhookEndpointService,
)
from stripe._webhook_endpoint_update_params import (
    WebhookEndpointUpdateParams as WebhookEndpointUpdateParams,
)
# The end of the section generated from our OpenAPI spec
