# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._account_link_service import AccountLinkService
from stripe._account_service import AccountService
from stripe._account_session_service import AccountSessionService
from stripe._apple_pay_domain_service import ApplePayDomainService
from stripe._application_fee_service import ApplicationFeeService
from stripe._apps_service import AppsService
from stripe._balance_service import BalanceService
from stripe._balance_settings_service import BalanceSettingsService
from stripe._balance_transaction_service import BalanceTransactionService
from stripe._billing_portal_service import BillingPortalService
from stripe._billing_service import BillingService
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
from stripe._file_link_service import FileLinkService
from stripe._file_service import FileService
from stripe._financial_connections_service import FinancialConnectionsService
from stripe._forwarding_service import ForwardingService
from stripe._identity_service import IdentityService
from stripe._invoice_item_service import InvoiceItemService
from stripe._invoice_payment_service import InvoicePaymentService
from stripe._invoice_rendering_template_service import (
    InvoiceRenderingTemplateService,
)
from stripe._invoice_service import InvoiceService
from stripe._issuing_service import IssuingService
from stripe._mandate_service import MandateService
from stripe._payment_intent_service import PaymentIntentService
from stripe._payment_link_service import PaymentLinkService
from stripe._payment_method_configuration_service import (
    PaymentMethodConfigurationService,
)
from stripe._payment_method_domain_service import PaymentMethodDomainService
from stripe._payment_method_service import PaymentMethodService
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
from stripe._stripe_service import StripeService
from stripe._subscription_item_service import SubscriptionItemService
from stripe._subscription_schedule_service import SubscriptionScheduleService
from stripe._subscription_service import SubscriptionService
from stripe._tax_code_service import TaxCodeService
from stripe._tax_id_service import TaxIdService
from stripe._tax_rate_service import TaxRateService
from stripe._tax_service import TaxService
from stripe._terminal_service import TerminalService
from stripe._test_helpers_service import TestHelpersService
from stripe._token_service import TokenService
from stripe._topup_service import TopupService
from stripe._transfer_service import TransferService
from stripe._treasury_service import TreasuryService
from stripe._webhook_endpoint_service import WebhookEndpointService
from importlib import import_module

_subservices = {
    "accounts": ["stripe._account_service", "AccountService"],
    "account_links": ["stripe._account_service", "AccountService"],
    "account_sessions": ["stripe._account_service", "AccountService"],
    "apple_pay_domains": ["stripe._account_service", "AccountService"],
    "application_fees": ["stripe._account_service", "AccountService"],
    "apps": ["stripe._account_service", "AccountService"],
    "balance": ["stripe._account_service", "AccountService"],
    "balance_settings": ["stripe._account_service", "AccountService"],
    "balance_transactions": ["stripe._account_service", "AccountService"],
    "billing": ["stripe._account_service", "AccountService"],
    "billing_portal": ["stripe._account_service", "AccountService"],
    "charges": ["stripe._account_service", "AccountService"],
    "checkout": ["stripe._account_service", "AccountService"],
    "climate": ["stripe._account_service", "AccountService"],
    "confirmation_tokens": ["stripe._account_service", "AccountService"],
    "country_specs": ["stripe._account_service", "AccountService"],
    "coupons": ["stripe._account_service", "AccountService"],
    "credit_notes": ["stripe._account_service", "AccountService"],
    "customers": ["stripe._account_service", "AccountService"],
    "customer_sessions": ["stripe._account_service", "AccountService"],
    "disputes": ["stripe._account_service", "AccountService"],
    "entitlements": ["stripe._account_service", "AccountService"],
    "ephemeral_keys": ["stripe._account_service", "AccountService"],
    "events": ["stripe._account_service", "AccountService"],
    "exchange_rates": ["stripe._account_service", "AccountService"],
    "files": ["stripe._account_service", "AccountService"],
    "file_links": ["stripe._account_service", "AccountService"],
    "financial_connections": ["stripe._account_service", "AccountService"],
    "forwarding": ["stripe._account_service", "AccountService"],
    "identity": ["stripe._account_service", "AccountService"],
    "invoices": ["stripe._account_service", "AccountService"],
    "invoice_items": ["stripe._account_service", "AccountService"],
    "invoice_payments": ["stripe._account_service", "AccountService"],
    "invoice_rendering_templates": [
        "stripe._account_service",
        "AccountService",
    ],
    "issuing": ["stripe._account_service", "AccountService"],
    "mandates": ["stripe._account_service", "AccountService"],
    "payment_intents": ["stripe._account_service", "AccountService"],
    "payment_links": ["stripe._account_service", "AccountService"],
    "payment_methods": ["stripe._account_service", "AccountService"],
    "payment_method_configurations": [
        "stripe._account_service",
        "AccountService",
    ],
    "payment_method_domains": ["stripe._account_service", "AccountService"],
    "payouts": ["stripe._account_service", "AccountService"],
    "plans": ["stripe._account_service", "AccountService"],
    "prices": ["stripe._account_service", "AccountService"],
    "products": ["stripe._account_service", "AccountService"],
    "promotion_codes": ["stripe._account_service", "AccountService"],
    "quotes": ["stripe._account_service", "AccountService"],
    "radar": ["stripe._account_service", "AccountService"],
    "refunds": ["stripe._account_service", "AccountService"],
    "reporting": ["stripe._account_service", "AccountService"],
    "reviews": ["stripe._account_service", "AccountService"],
    "setup_attempts": ["stripe._account_service", "AccountService"],
    "setup_intents": ["stripe._account_service", "AccountService"],
    "shipping_rates": ["stripe._account_service", "AccountService"],
    "sigma": ["stripe._account_service", "AccountService"],
    "sources": ["stripe._account_service", "AccountService"],
    "subscriptions": ["stripe._account_service", "AccountService"],
    "subscription_items": ["stripe._account_service", "AccountService"],
    "subscription_schedules": ["stripe._account_service", "AccountService"],
    "tax": ["stripe._account_service", "AccountService"],
    "tax_codes": ["stripe._account_service", "AccountService"],
    "tax_ids": ["stripe._account_service", "AccountService"],
    "tax_rates": ["stripe._account_service", "AccountService"],
    "terminal": ["stripe._account_service", "AccountService"],
    "test_helpers": ["stripe._account_service", "AccountService"],
    "tokens": ["stripe._account_service", "AccountService"],
    "topups": ["stripe._account_service", "AccountService"],
    "transfers": ["stripe._account_service", "AccountService"],
    "treasury": ["stripe._account_service", "AccountService"],
    "webhook_endpoints": ["stripe._account_service", "AccountService"],
}


class V1Services(StripeService):
    def __init__(self, requestor):
        super().__init__(requestor)

    def __getattr__(self, name):
        try:
            import_from, service = _subservices[name]
            service_class = getattr(
                import_module(import_from),
                service,
            )
            setattr(
                self,
                name,
                service_class(self._requestor),
            )
            return getattr(self, name)
        except KeyError:
            pass
