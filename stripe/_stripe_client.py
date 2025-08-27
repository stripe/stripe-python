# -*- coding: utf-8 -*-

import json
from collections import OrderedDict

from stripe import (
    DEFAULT_API_BASE,
    DEFAULT_CONNECT_API_BASE,
    DEFAULT_UPLOAD_API_BASE,
    DEFAULT_METER_EVENTS_API_BASE,
)

from stripe._api_mode import ApiMode
from stripe._error import AuthenticationError
from stripe._api_requestor import _APIRequestor
from stripe._request_options import extract_options_from_dict
from stripe._requestor_options import RequestorOptions, BaseAddresses
from stripe._client_options import _ClientOptions
from stripe._http_client import (
    HTTPClient,
    new_default_http_client,
    new_http_client_async_fallback,
)
from stripe._api_version import _ApiVersion
from stripe._stripe_object import StripeObject
from stripe._stripe_response import StripeResponse
from stripe._util import _convert_to_stripe_object, get_api_mode, deprecated  # noqa: F401
from stripe._webhook import Webhook, WebhookSignature
from stripe._event import Event
from stripe.v2._event import ThinEvent

from typing import Any, Dict, Optional, Union, cast

# Non-generated services
from stripe._oauth_service import OAuthService

# services: The beginning of the section generated from our OpenAPI spec
from stripe._v1_services import V1Services
from stripe._v2_services import V2Services
from stripe._account_service import AccountService
from stripe._account_link_service import AccountLinkService
from stripe._account_session_service import AccountSessionService
from stripe._apple_pay_domain_service import ApplePayDomainService
from stripe._application_fee_service import ApplicationFeeService
from stripe._apps_service import AppsService
from stripe._balance_service import BalanceService
from stripe._balance_transaction_service import BalanceTransactionService
from stripe._billing_service import BillingService
from stripe._billing_portal_service import BillingPortalService
from stripe._charge_service import ChargeService
from stripe._checkout_service import CheckoutService
from stripe._climate_service import ClimateService
from stripe._confirmation_token_service import ConfirmationTokenService
from stripe._country_spec_service import CountrySpecService
from stripe._coupon_service import CouponService
from stripe._credit_note_service import CreditNoteService
from stripe._customer_service import CustomerService
from stripe._customer_session_service import CustomerSessionService
from stripe._dispute_service import DisputeService
from stripe._entitlements_service import EntitlementsService
from stripe._ephemeral_key_service import EphemeralKeyService
from stripe._event_service import EventService
from stripe._exchange_rate_service import ExchangeRateService
from stripe._file_service import FileService
from stripe._file_link_service import FileLinkService
from stripe._financial_connections_service import FinancialConnectionsService
from stripe._forwarding_service import ForwardingService
from stripe._identity_service import IdentityService
from stripe._invoice_service import InvoiceService
from stripe._invoice_item_service import InvoiceItemService
from stripe._invoice_payment_service import InvoicePaymentService
from stripe._invoice_rendering_template_service import (
    InvoiceRenderingTemplateService,
)
from stripe._issuing_service import IssuingService
from stripe._mandate_service import MandateService
from stripe._payment_intent_service import PaymentIntentService
from stripe._payment_link_service import PaymentLinkService
from stripe._payment_method_service import PaymentMethodService
from stripe._payment_method_configuration_service import (
    PaymentMethodConfigurationService,
)
from stripe._payment_method_domain_service import PaymentMethodDomainService
from stripe._payout_service import PayoutService
from stripe._plan_service import PlanService
from stripe._price_service import PriceService
from stripe._product_service import ProductService
from stripe._promotion_code_service import PromotionCodeService
from stripe._quote_service import QuoteService
from stripe._radar_service import RadarService
from stripe._refund_service import RefundService
from stripe._reporting_service import ReportingService
from stripe._review_service import ReviewService
from stripe._setup_attempt_service import SetupAttemptService
from stripe._setup_intent_service import SetupIntentService
from stripe._shipping_rate_service import ShippingRateService
from stripe._sigma_service import SigmaService
from stripe._source_service import SourceService
from stripe._subscription_service import SubscriptionService
from stripe._subscription_item_service import SubscriptionItemService
from stripe._subscription_schedule_service import SubscriptionScheduleService
from stripe._tax_service import TaxService
from stripe._tax_code_service import TaxCodeService
from stripe._tax_id_service import TaxIdService
from stripe._tax_rate_service import TaxRateService
from stripe._terminal_service import TerminalService
from stripe._test_helpers_service import TestHelpersService
from stripe._token_service import TokenService
from stripe._topup_service import TopupService
from stripe._transfer_service import TransferService
from stripe._treasury_service import TreasuryService
from stripe._webhook_endpoint_service import WebhookEndpointService
# services: The end of the section generated from our OpenAPI spec


class StripeClient(object):
    def __init__(
        self,
        api_key: str,
        *,
        stripe_account: Optional[str] = None,
        stripe_context: Optional[str] = None,
        stripe_version: Optional[str] = None,
        base_addresses: BaseAddresses = {},
        client_id: Optional[str] = None,
        verify_ssl_certs: bool = True,
        proxy: Optional[str] = None,
        max_network_retries: Optional[int] = None,
        http_client: Optional[HTTPClient] = None,
    ):
        # The types forbid this, but let's give users without types a friendly error.
        if api_key is None:  # pyright: ignore[reportUnnecessaryComparison]
            raise AuthenticationError(
                "No API key provided. (HINT: set your API key using "
                '"client = stripe.StripeClient(<API-KEY>)"). You can '
                "generate API keys from the Stripe web interface. "
                "See https://stripe.com/api for details, or email "
                "support@stripe.com if you have any questions."
            )

        if http_client and (proxy or verify_ssl_certs is not True):
            raise ValueError(
                "You cannot specify `proxy` or `verify_ssl_certs` when passing "
                "in a custom `http_client`. Please set these values on your "
                "custom `http_client` instead."
            )

        # Default to stripe.DEFAULT_API_BASE, stripe.DEFAULT_CONNECT_API_BASE,
        # and stripe.DEFAULT_UPLOAD_API_BASE if not set in base_addresses.
        base_addresses = {
            "api": DEFAULT_API_BASE,
            "connect": DEFAULT_CONNECT_API_BASE,
            "files": DEFAULT_UPLOAD_API_BASE,
            "meter_events": DEFAULT_METER_EVENTS_API_BASE,
            **base_addresses,
        }

        requestor_options = RequestorOptions(
            api_key=api_key,
            stripe_account=stripe_account,
            stripe_context=stripe_context,
            stripe_version=stripe_version or _ApiVersion.CURRENT,
            base_addresses=base_addresses,
            max_network_retries=max_network_retries,
        )

        if http_client is None:
            http_client = new_default_http_client(
                async_fallback_client=new_http_client_async_fallback(
                    proxy=proxy, verify_ssl_certs=verify_ssl_certs
                ),
                proxy=proxy,
                verify_ssl_certs=verify_ssl_certs,
            )

        self._requestor = _APIRequestor(
            options=requestor_options,
            client=http_client,
        )

        self._options = _ClientOptions(
            client_id=client_id,
            proxy=proxy,
            verify_ssl_certs=verify_ssl_certs,
        )

        self.oauth = OAuthService(self._requestor, self._options)

        # top-level services: The beginning of the section generated from our OpenAPI spec
        self.v1 = V1Services(self._requestor)
        self.v2 = V2Services(self._requestor)
        # top-level services: The end of the section generated from our OpenAPI spec

    def parse_thin_event(
        self,
        raw: Union[bytes, str, bytearray],
        sig_header: str,
        secret: str,
        tolerance: int = Webhook.DEFAULT_TOLERANCE,
    ) -> ThinEvent:
        payload = (
            cast(Union[bytes, bytearray], raw).decode("utf-8")
            if hasattr(raw, "decode")
            else cast(str, raw)
        )

        WebhookSignature.verify_header(payload, sig_header, secret, tolerance)

        return ThinEvent(payload)

    def construct_event(
        self,
        payload: Union[bytes, str],
        sig_header: str,
        secret: str,
        tolerance: int = Webhook.DEFAULT_TOLERANCE,
    ) -> Event:
        if hasattr(payload, "decode"):
            payload = cast(bytes, payload).decode("utf-8")

        WebhookSignature.verify_header(payload, sig_header, secret, tolerance)

        data = json.loads(payload, object_pairs_hook=OrderedDict)
        event = Event._construct_from(
            values=data,
            requestor=self._requestor,
            api_mode="V1",
        )

        return event

    def raw_request(self, method_: str, url_: str, **params):
        params = params.copy()
        options, params = extract_options_from_dict(params)
        api_mode = get_api_mode(url_)
        base_address = params.pop("base", "api")

        stripe_context = params.pop("stripe_context", None)

        # stripe-context goes *here* and not in api_requestor. Properties
        # go on api_requestor when you want them to persist onto requests
        # made when you call instance methods on APIResources that come from
        # the first request. No need for that here, as we aren't deserializing APIResources
        if stripe_context is not None:
            options["headers"] = options.get("headers", {})
            assert isinstance(options["headers"], dict)
            options["headers"].update({"Stripe-Context": stripe_context})

        rbody, rcode, rheaders = self._requestor.request_raw(
            method_,
            url_,
            params=params,
            options=options,
            base_address=base_address,
            api_mode=api_mode,
            usage=["raw_request"],
        )

        return self._requestor._interpret_response(
            rbody, rcode, rheaders, api_mode
        )

    async def raw_request_async(self, method_: str, url_: str, **params):
        params = params.copy()
        options, params = extract_options_from_dict(params)
        api_mode = get_api_mode(url_)
        base_address = params.pop("base", "api")

        rbody, rcode, rheaders = await self._requestor.request_raw_async(
            method_,
            url_,
            params=params,
            options=options,
            base_address=base_address,
            api_mode=api_mode,
            usage=["raw_request"],
        )

        return self._requestor._interpret_response(
            rbody, rcode, rheaders, api_mode
        )

    def deserialize(
        self,
        resp: Union[StripeResponse, Dict[str, Any]],
        params: Optional[Dict[str, Any]] = None,
        *,
        api_mode: ApiMode,
    ) -> StripeObject:
        return _convert_to_stripe_object(
            resp=resp,
            params=params,
            requestor=self._requestor,
            api_mode=api_mode,
        )

    # deprecated v1 services: The beginning of the section generated from our OpenAPI spec
    @property
    def accounts(self) -> AccountService:
        """
        Deprecation Warning:
          StripeClient.accounts will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.accounts.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.accounts

    @property
    def account_links(self) -> AccountLinkService:
        """
        Deprecation Warning:
          StripeClient.account_links will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.account_links.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.account_links

    @property
    def account_sessions(self) -> AccountSessionService:
        """
        Deprecation Warning:
          StripeClient.account_sessions will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.account_sessions.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.account_sessions

    @property
    def apple_pay_domains(self) -> ApplePayDomainService:
        """
        Deprecation Warning:
          StripeClient.apple_pay_domains will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.apple_pay_domains.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.apple_pay_domains

    @property
    def application_fees(self) -> ApplicationFeeService:
        """
        Deprecation Warning:
          StripeClient.application_fees will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.application_fees.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.application_fees

    @property
    def apps(self) -> AppsService:
        """
        Deprecation Warning:
          StripeClient.apps will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.apps.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.apps

    @property
    def balance(self) -> BalanceService:
        """
        Deprecation Warning:
          StripeClient.balance will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.balance.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.balance

    @property
    def balance_transactions(self) -> BalanceTransactionService:
        """
        Deprecation Warning:
          StripeClient.balance_transactions will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.balance_transactions.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.balance_transactions

    @property
    def billing(self) -> BillingService:
        """
        Deprecation Warning:
          StripeClient.billing will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.billing.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.billing

    @property
    def billing_portal(self) -> BillingPortalService:
        """
        Deprecation Warning:
          StripeClient.billing_portal will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.billing_portal.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.billing_portal

    @property
    def charges(self) -> ChargeService:
        """
        Deprecation Warning:
          StripeClient.charges will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.charges.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.charges

    @property
    def checkout(self) -> CheckoutService:
        """
        Deprecation Warning:
          StripeClient.checkout will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.checkout.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.checkout

    @property
    def climate(self) -> ClimateService:
        """
        Deprecation Warning:
          StripeClient.climate will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.climate.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.climate

    @property
    def confirmation_tokens(self) -> ConfirmationTokenService:
        """
        Deprecation Warning:
          StripeClient.confirmation_tokens will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.confirmation_tokens.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.confirmation_tokens

    @property
    def country_specs(self) -> CountrySpecService:
        """
        Deprecation Warning:
          StripeClient.country_specs will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.country_specs.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.country_specs

    @property
    def coupons(self) -> CouponService:
        """
        Deprecation Warning:
          StripeClient.coupons will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.coupons.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.coupons

    @property
    def credit_notes(self) -> CreditNoteService:
        """
        Deprecation Warning:
          StripeClient.credit_notes will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.credit_notes.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.credit_notes

    @property
    def customers(self) -> CustomerService:
        """
        Deprecation Warning:
          StripeClient.customers will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.customers.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.customers

    @property
    def customer_sessions(self) -> CustomerSessionService:
        """
        Deprecation Warning:
          StripeClient.customer_sessions will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.customer_sessions.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.customer_sessions

    @property
    def disputes(self) -> DisputeService:
        """
        Deprecation Warning:
          StripeClient.disputes will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.disputes.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.disputes

    @property
    def entitlements(self) -> EntitlementsService:
        """
        Deprecation Warning:
          StripeClient.entitlements will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.entitlements.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.entitlements

    @property
    def ephemeral_keys(self) -> EphemeralKeyService:
        """
        Deprecation Warning:
          StripeClient.ephemeral_keys will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.ephemeral_keys.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.ephemeral_keys

    @property
    def events(self) -> EventService:
        """
        Deprecation Warning:
          StripeClient.events will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.events.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.events

    @property
    def exchange_rates(self) -> ExchangeRateService:
        """
        Deprecation Warning:
          StripeClient.exchange_rates will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.exchange_rates.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.exchange_rates

    @property
    def files(self) -> FileService:
        """
        Deprecation Warning:
          StripeClient.files will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.files.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.files

    @property
    def file_links(self) -> FileLinkService:
        """
        Deprecation Warning:
          StripeClient.file_links will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.file_links.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.file_links

    @property
    def financial_connections(self) -> FinancialConnectionsService:
        """
        Deprecation Warning:
          StripeClient.financial_connections will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.financial_connections.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.financial_connections

    @property
    def forwarding(self) -> ForwardingService:
        """
        Deprecation Warning:
          StripeClient.forwarding will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.forwarding.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.forwarding

    @property
    def identity(self) -> IdentityService:
        """
        Deprecation Warning:
          StripeClient.identity will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.identity.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.identity

    @property
    def invoices(self) -> InvoiceService:
        """
        Deprecation Warning:
          StripeClient.invoices will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.invoices.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.invoices

    @property
    def invoice_items(self) -> InvoiceItemService:
        """
        Deprecation Warning:
          StripeClient.invoice_items will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.invoice_items.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.invoice_items

    @property
    def invoice_payments(self) -> InvoicePaymentService:
        """
        Deprecation Warning:
          StripeClient.invoice_payments will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.invoice_payments.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.invoice_payments

    @property
    def invoice_rendering_templates(self) -> InvoiceRenderingTemplateService:
        """
        Deprecation Warning:
          StripeClient.invoice_rendering_templates will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.invoice_rendering_templates.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.invoice_rendering_templates

    @property
    def issuing(self) -> IssuingService:
        """
        Deprecation Warning:
          StripeClient.issuing will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.issuing.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.issuing

    @property
    def mandates(self) -> MandateService:
        """
        Deprecation Warning:
          StripeClient.mandates will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.mandates.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.mandates

    @property
    def payment_intents(self) -> PaymentIntentService:
        """
        Deprecation Warning:
          StripeClient.payment_intents will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.payment_intents.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.payment_intents

    @property
    def payment_links(self) -> PaymentLinkService:
        """
        Deprecation Warning:
          StripeClient.payment_links will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.payment_links.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.payment_links

    @property
    def payment_methods(self) -> PaymentMethodService:
        """
        Deprecation Warning:
          StripeClient.payment_methods will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.payment_methods.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.payment_methods

    @property
    def payment_method_configurations(
        self,
    ) -> PaymentMethodConfigurationService:
        """
        Deprecation Warning:
          StripeClient.payment_method_configurations will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.payment_method_configurations.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.payment_method_configurations

    @property
    def payment_method_domains(self) -> PaymentMethodDomainService:
        """
        Deprecation Warning:
          StripeClient.payment_method_domains will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.payment_method_domains.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.payment_method_domains

    @property
    def payouts(self) -> PayoutService:
        """
        Deprecation Warning:
          StripeClient.payouts will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.payouts.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.payouts

    @property
    def plans(self) -> PlanService:
        """
        Deprecation Warning:
          StripeClient.plans will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.plans.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.plans

    @property
    def prices(self) -> PriceService:
        """
        Deprecation Warning:
          StripeClient.prices will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.prices.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.prices

    @property
    def products(self) -> ProductService:
        """
        Deprecation Warning:
          StripeClient.products will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.products.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.products

    @property
    def promotion_codes(self) -> PromotionCodeService:
        """
        Deprecation Warning:
          StripeClient.promotion_codes will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.promotion_codes.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.promotion_codes

    @property
    def quotes(self) -> QuoteService:
        """
        Deprecation Warning:
          StripeClient.quotes will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.quotes.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.quotes

    @property
    def radar(self) -> RadarService:
        """
        Deprecation Warning:
          StripeClient.radar will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.radar.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.radar

    @property
    def refunds(self) -> RefundService:
        """
        Deprecation Warning:
          StripeClient.refunds will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.refunds.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.refunds

    @property
    def reporting(self) -> ReportingService:
        """
        Deprecation Warning:
          StripeClient.reporting will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.reporting.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.reporting

    @property
    def reviews(self) -> ReviewService:
        """
        Deprecation Warning:
          StripeClient.reviews will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.reviews.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.reviews

    @property
    def setup_attempts(self) -> SetupAttemptService:
        """
        Deprecation Warning:
          StripeClient.setup_attempts will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.setup_attempts.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.setup_attempts

    @property
    def setup_intents(self) -> SetupIntentService:
        """
        Deprecation Warning:
          StripeClient.setup_intents will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.setup_intents.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.setup_intents

    @property
    def shipping_rates(self) -> ShippingRateService:
        """
        Deprecation Warning:
          StripeClient.shipping_rates will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.shipping_rates.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.shipping_rates

    @property
    def sigma(self) -> SigmaService:
        """
        Deprecation Warning:
          StripeClient.sigma will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.sigma.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.sigma

    @property
    def sources(self) -> SourceService:
        """
        Deprecation Warning:
          StripeClient.sources will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.sources.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.sources

    @property
    def subscriptions(self) -> SubscriptionService:
        """
        Deprecation Warning:
          StripeClient.subscriptions will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.subscriptions.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.subscriptions

    @property
    def subscription_items(self) -> SubscriptionItemService:
        """
        Deprecation Warning:
          StripeClient.subscription_items will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.subscription_items.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.subscription_items

    @property
    def subscription_schedules(self) -> SubscriptionScheduleService:
        """
        Deprecation Warning:
          StripeClient.subscription_schedules will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.subscription_schedules.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.subscription_schedules

    @property
    def tax(self) -> TaxService:
        """
        Deprecation Warning:
          StripeClient.tax will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.tax.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.tax

    @property
    def tax_codes(self) -> TaxCodeService:
        """
        Deprecation Warning:
          StripeClient.tax_codes will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.tax_codes.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.tax_codes

    @property
    def tax_ids(self) -> TaxIdService:
        """
        Deprecation Warning:
          StripeClient.tax_ids will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.tax_ids.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.tax_ids

    @property
    def tax_rates(self) -> TaxRateService:
        """
        Deprecation Warning:
          StripeClient.tax_rates will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.tax_rates.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.tax_rates

    @property
    def terminal(self) -> TerminalService:
        """
        Deprecation Warning:
          StripeClient.terminal will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.terminal.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.terminal

    @property
    def test_helpers(self) -> TestHelpersService:
        """
        Deprecation Warning:
          StripeClient.test_helpers will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.test_helpers.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.test_helpers

    @property
    def tokens(self) -> TokenService:
        """
        Deprecation Warning:
          StripeClient.tokens will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.tokens.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.tokens

    @property
    def topups(self) -> TopupService:
        """
        Deprecation Warning:
          StripeClient.topups will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.topups.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.topups

    @property
    def transfers(self) -> TransferService:
        """
        Deprecation Warning:
          StripeClient.transfers will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.transfers.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.transfers

    @property
    def treasury(self) -> TreasuryService:
        """
        Deprecation Warning:
          StripeClient.treasury will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.treasury.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.treasury

    @property
    def webhook_endpoints(self) -> WebhookEndpointService:
        """
        Deprecation Warning:
          StripeClient.webhook_endpoints will be deprecated in the next major release.
          All functionality under it has been copied over to StripeClient.v1.webhook_endpoints.
          See [migration guide](https://github.com/stripe/stripe-python/wiki/v1-namespace-in-StripeClient) for more on this and tips on migrating to the new v1 namespace.
        """
        return self.v1.webhook_endpoints

    # deprecated v1 services: The end of the section generated from our OpenAPI spec
