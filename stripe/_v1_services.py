# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._account_link_service import AccountLinkService
from stripe._account_service import AccountService
from stripe._account_session_service import AccountSessionService
from stripe._apple_pay_domain_service import ApplePayDomainService
from stripe._application_fee_service import ApplicationFeeService
from stripe._apps_service import AppsService
from stripe._balance_service import BalanceService
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


class V1Services(StripeService):
    def __init__(self, requestor):
        super().__init__(requestor)
        self.accounts = AccountService(self._requestor)
        self.account_links = AccountLinkService(self._requestor)
        self.account_sessions = AccountSessionService(self._requestor)
        self.apple_pay_domains = ApplePayDomainService(self._requestor)
        self.application_fees = ApplicationFeeService(self._requestor)
        self.apps = AppsService(self._requestor)
        self.balance = BalanceService(self._requestor)
        self.balance_transactions = BalanceTransactionService(self._requestor)
        self.billing = BillingService(self._requestor)
        self.billing_portal = BillingPortalService(self._requestor)
        self.charges = ChargeService(self._requestor)
        self.checkout = CheckoutService(self._requestor)
        self.climate = ClimateService(self._requestor)
        self.confirmation_tokens = ConfirmationTokenService(self._requestor)
        self.country_specs = CountrySpecService(self._requestor)
        self.coupons = CouponService(self._requestor)
        self.credit_notes = CreditNoteService(self._requestor)
        self.customers = CustomerService(self._requestor)
        self.customer_sessions = CustomerSessionService(self._requestor)
        self.disputes = DisputeService(self._requestor)
        self.entitlements = EntitlementsService(self._requestor)
        self.ephemeral_keys = EphemeralKeyService(self._requestor)
        self.events = EventService(self._requestor)
        self.exchange_rates = ExchangeRateService(self._requestor)
        self.files = FileService(self._requestor)
        self.file_links = FileLinkService(self._requestor)
        self.financial_connections = FinancialConnectionsService(
            self._requestor,
        )
        self.forwarding = ForwardingService(self._requestor)
        self.identity = IdentityService(self._requestor)
        self.invoices = InvoiceService(self._requestor)
        self.invoice_items = InvoiceItemService(self._requestor)
        self.invoice_payments = InvoicePaymentService(self._requestor)
        self.invoice_rendering_templates = InvoiceRenderingTemplateService(
            self._requestor,
        )
        self.issuing = IssuingService(self._requestor)
        self.mandates = MandateService(self._requestor)
        self.payment_intents = PaymentIntentService(self._requestor)
        self.payment_links = PaymentLinkService(self._requestor)
        self.payment_methods = PaymentMethodService(self._requestor)
        self.payment_method_configurations = PaymentMethodConfigurationService(
            self._requestor,
        )
        self.payment_method_domains = PaymentMethodDomainService(
            self._requestor,
        )
        self.payouts = PayoutService(self._requestor)
        self.plans = PlanService(self._requestor)
        self.prices = PriceService(self._requestor)
        self.products = ProductService(self._requestor)
        self.promotion_codes = PromotionCodeService(self._requestor)
        self.quotes = QuoteService(self._requestor)
        self.radar = RadarService(self._requestor)
        self.refunds = RefundService(self._requestor)
        self.reporting = ReportingService(self._requestor)
        self.reviews = ReviewService(self._requestor)
        self.setup_attempts = SetupAttemptService(self._requestor)
        self.setup_intents = SetupIntentService(self._requestor)
        self.shipping_rates = ShippingRateService(self._requestor)
        self.sigma = SigmaService(self._requestor)
        self.sources = SourceService(self._requestor)
        self.subscriptions = SubscriptionService(self._requestor)
        self.subscription_items = SubscriptionItemService(self._requestor)
        self.subscription_schedules = SubscriptionScheduleService(
            self._requestor,
        )
        self.tax = TaxService(self._requestor)
        self.tax_codes = TaxCodeService(self._requestor)
        self.tax_ids = TaxIdService(self._requestor)
        self.tax_rates = TaxRateService(self._requestor)
        self.terminal = TerminalService(self._requestor)
        self.test_helpers = TestHelpersService(self._requestor)
        self.tokens = TokenService(self._requestor)
        self.topups = TopupService(self._requestor)
        self.transfers = TransferService(self._requestor)
        self.treasury = TreasuryService(self._requestor)
        self.webhook_endpoints = WebhookEndpointService(self._requestor)
