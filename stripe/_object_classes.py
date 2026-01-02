# -*- coding: utf-8 -*-
from importlib import import_module
from typing import Dict, Tuple
from typing_extensions import TYPE_CHECKING, Type

from stripe._stripe_object import StripeObject

if TYPE_CHECKING:
    from stripe._api_mode import ApiMode

OBJECT_CLASSES: Dict[str, Tuple[str, str]] = {
    # data structures
    "list": ("stripe._list_object", "ListObject"),
    "search_result": ("stripe._search_result_object", "SearchResultObject"),
    "file": ("stripe._file", "File"),
    # there's also an alt name for compatibility
    "file_upload": ("stripe._file", "File"),
    # Object classes: The beginning of the section generated from our OpenAPI spec
    "account": ("stripe._account", "Account"),
    "account_link": ("stripe._account_link", "AccountLink"),
    "account_notice": ("stripe._account_notice", "AccountNotice"),
    "account_session": ("stripe._account_session", "AccountSession"),
    "apple_pay_domain": ("stripe._apple_pay_domain", "ApplePayDomain"),
    "application": ("stripe._application", "Application"),
    "application_fee": ("stripe._application_fee", "ApplicationFee"),
    "fee_refund": ("stripe._application_fee_refund", "ApplicationFeeRefund"),
    "apps.secret": ("stripe.apps._secret", "Secret"),
    "balance": ("stripe._balance", "Balance"),
    "balance_settings": ("stripe._balance_settings", "BalanceSettings"),
    "balance_transaction": (
        "stripe._balance_transaction",
        "BalanceTransaction",
    ),
    "balance_transfer": ("stripe._balance_transfer", "BalanceTransfer"),
    "bank_account": ("stripe._bank_account", "BankAccount"),
    "billing_portal.configuration": (
        "stripe.billing_portal._configuration",
        "Configuration",
    ),
    "billing_portal.session": ("stripe.billing_portal._session", "Session"),
    "billing.alert": ("stripe.billing._alert", "Alert"),
    "billing.alert_triggered": (
        "stripe.billing._alert_triggered",
        "AlertTriggered",
    ),
    "billing.analytics.meter_usage": (
        "stripe.billing.analytics._meter_usage",
        "MeterUsage",
    ),
    "billing.analytics.meter_usage_row": (
        "stripe.billing.analytics._meter_usage_row",
        "MeterUsageRow",
    ),
    "billing.credit_balance_summary": (
        "stripe.billing._credit_balance_summary",
        "CreditBalanceSummary",
    ),
    "billing.credit_balance_transaction": (
        "stripe.billing._credit_balance_transaction",
        "CreditBalanceTransaction",
    ),
    "billing.credit_grant": ("stripe.billing._credit_grant", "CreditGrant"),
    "billing.meter": ("stripe.billing._meter", "Meter"),
    "billing.meter_event": ("stripe.billing._meter_event", "MeterEvent"),
    "billing.meter_event_adjustment": (
        "stripe.billing._meter_event_adjustment",
        "MeterEventAdjustment",
    ),
    "billing.meter_event_summary": (
        "stripe.billing._meter_event_summary",
        "MeterEventSummary",
    ),
    "capability": ("stripe._capability", "Capability"),
    "capital.financing_offer": (
        "stripe.capital._financing_offer",
        "FinancingOffer",
    ),
    "capital.financing_summary": (
        "stripe.capital._financing_summary",
        "FinancingSummary",
    ),
    "capital.financing_transaction": (
        "stripe.capital._financing_transaction",
        "FinancingTransaction",
    ),
    "card": ("stripe._card", "Card"),
    "cash_balance": ("stripe._cash_balance", "CashBalance"),
    "charge": ("stripe._charge", "Charge"),
    "checkout.session": ("stripe.checkout._session", "Session"),
    "climate.order": ("stripe.climate._order", "Order"),
    "climate.product": ("stripe.climate._product", "Product"),
    "climate.supplier": ("stripe.climate._supplier", "Supplier"),
    "confirmation_token": ("stripe._confirmation_token", "ConfirmationToken"),
    "connect_collection_transfer": (
        "stripe._connect_collection_transfer",
        "ConnectCollectionTransfer",
    ),
    "country_spec": ("stripe._country_spec", "CountrySpec"),
    "coupon": ("stripe._coupon", "Coupon"),
    "credit_note": ("stripe._credit_note", "CreditNote"),
    "credit_note_line_item": (
        "stripe._credit_note_line_item",
        "CreditNoteLineItem",
    ),
    "customer": ("stripe._customer", "Customer"),
    "customer_balance_transaction": (
        "stripe._customer_balance_transaction",
        "CustomerBalanceTransaction",
    ),
    "customer_cash_balance_transaction": (
        "stripe._customer_cash_balance_transaction",
        "CustomerCashBalanceTransaction",
    ),
    "customer_session": ("stripe._customer_session", "CustomerSession"),
    "delegated_checkout.requested_session": (
        "stripe.delegated_checkout._requested_session",
        "RequestedSession",
    ),
    "discount": ("stripe._discount", "Discount"),
    "dispute": ("stripe._dispute", "Dispute"),
    "entitlements.active_entitlement": (
        "stripe.entitlements._active_entitlement",
        "ActiveEntitlement",
    ),
    "entitlements.active_entitlement_summary": (
        "stripe.entitlements._active_entitlement_summary",
        "ActiveEntitlementSummary",
    ),
    "entitlements.feature": ("stripe.entitlements._feature", "Feature"),
    "ephemeral_key": ("stripe._ephemeral_key", "EphemeralKey"),
    "event": ("stripe._event", "Event"),
    "exchange_rate": ("stripe._exchange_rate", "ExchangeRate"),
    "file": ("stripe._file", "File"),
    "file_link": ("stripe._file_link", "FileLink"),
    "financial_connections.account": (
        "stripe.financial_connections._account",
        "Account",
    ),
    "financial_connections.account_inferred_balance": (
        "stripe.financial_connections._account_inferred_balance",
        "AccountInferredBalance",
    ),
    "financial_connections.account_owner": (
        "stripe.financial_connections._account_owner",
        "AccountOwner",
    ),
    "financial_connections.account_ownership": (
        "stripe.financial_connections._account_ownership",
        "AccountOwnership",
    ),
    "financial_connections.institution": (
        "stripe.financial_connections._institution",
        "Institution",
    ),
    "financial_connections.session": (
        "stripe.financial_connections._session",
        "Session",
    ),
    "financial_connections.transaction": (
        "stripe.financial_connections._transaction",
        "Transaction",
    ),
    "forwarding.request": ("stripe.forwarding._request", "Request"),
    "funding_instructions": (
        "stripe._funding_instructions",
        "FundingInstructions",
    ),
    "fx_quote": ("stripe._fx_quote", "FxQuote"),
    "identity.blocklist_entry": (
        "stripe.identity._blocklist_entry",
        "BlocklistEntry",
    ),
    "identity.verification_report": (
        "stripe.identity._verification_report",
        "VerificationReport",
    ),
    "identity.verification_session": (
        "stripe.identity._verification_session",
        "VerificationSession",
    ),
    "invoice": ("stripe._invoice", "Invoice"),
    "invoiceitem": ("stripe._invoice_item", "InvoiceItem"),
    "line_item": ("stripe._invoice_line_item", "InvoiceLineItem"),
    "invoice_payment": ("stripe._invoice_payment", "InvoicePayment"),
    "invoice_rendering_template": (
        "stripe._invoice_rendering_template",
        "InvoiceRenderingTemplate",
    ),
    "issuing.authorization": (
        "stripe.issuing._authorization",
        "Authorization",
    ),
    "issuing.card": ("stripe.issuing._card", "Card"),
    "issuing.cardholder": ("stripe.issuing._cardholder", "Cardholder"),
    "issuing.credit_underwriting_record": (
        "stripe.issuing._credit_underwriting_record",
        "CreditUnderwritingRecord",
    ),
    "issuing.dispute": ("stripe.issuing._dispute", "Dispute"),
    "issuing.dispute_settlement_detail": (
        "stripe.issuing._dispute_settlement_detail",
        "DisputeSettlementDetail",
    ),
    "issuing.fraud_liability_debit": (
        "stripe.issuing._fraud_liability_debit",
        "FraudLiabilityDebit",
    ),
    "issuing.personalization_design": (
        "stripe.issuing._personalization_design",
        "PersonalizationDesign",
    ),
    "issuing.physical_bundle": (
        "stripe.issuing._physical_bundle",
        "PhysicalBundle",
    ),
    "issuing.program": ("stripe.issuing._program", "Program"),
    "issuing.settlement": ("stripe.issuing._settlement", "Settlement"),
    "issuing.token": ("stripe.issuing._token", "Token"),
    "issuing.transaction": ("stripe.issuing._transaction", "Transaction"),
    "item": ("stripe._line_item", "LineItem"),
    "login_link": ("stripe._login_link", "LoginLink"),
    "mandate": ("stripe._mandate", "Mandate"),
    "margin": ("stripe._margin", "Margin"),
    "order": ("stripe._order", "Order"),
    "payment_attempt_record": (
        "stripe._payment_attempt_record",
        "PaymentAttemptRecord",
    ),
    "payment_intent": ("stripe._payment_intent", "PaymentIntent"),
    "payment_intent_amount_details_line_item": (
        "stripe._payment_intent_amount_details_line_item",
        "PaymentIntentAmountDetailsLineItem",
    ),
    "payment_link": ("stripe._payment_link", "PaymentLink"),
    "payment_method": ("stripe._payment_method", "PaymentMethod"),
    "payment_method_balance": (
        "stripe._payment_method_balance",
        "PaymentMethodBalance",
    ),
    "payment_method_configuration": (
        "stripe._payment_method_configuration",
        "PaymentMethodConfiguration",
    ),
    "payment_method_domain": (
        "stripe._payment_method_domain",
        "PaymentMethodDomain",
    ),
    "payment_record": ("stripe._payment_record", "PaymentRecord"),
    "payout": ("stripe._payout", "Payout"),
    "person": ("stripe._person", "Person"),
    "plan": ("stripe._plan", "Plan"),
    "price": ("stripe._price", "Price"),
    "privacy.redaction_job": ("stripe.privacy._redaction_job", "RedactionJob"),
    "privacy.redaction_job_validation_error": (
        "stripe.privacy._redaction_job_validation_error",
        "RedactionJobValidationError",
    ),
    "product": ("stripe._product", "Product"),
    "product_catalog.trial_offer": (
        "stripe.product_catalog._trial_offer",
        "TrialOffer",
    ),
    "product_feature": ("stripe._product_feature", "ProductFeature"),
    "promotion_code": ("stripe._promotion_code", "PromotionCode"),
    "quote": ("stripe._quote", "Quote"),
    "quote_line": ("stripe._quote_line", "QuoteLine"),
    "quote_preview_invoice": (
        "stripe._quote_preview_invoice",
        "QuotePreviewInvoice",
    ),
    "quote_preview_subscription_schedule": (
        "stripe._quote_preview_subscription_schedule",
        "QuotePreviewSubscriptionSchedule",
    ),
    "radar.account_evaluation": (
        "stripe.radar._account_evaluation",
        "AccountEvaluation",
    ),
    "radar.early_fraud_warning": (
        "stripe.radar._early_fraud_warning",
        "EarlyFraudWarning",
    ),
    "radar.value_list": ("stripe.radar._value_list", "ValueList"),
    "radar.value_list_item": (
        "stripe.radar._value_list_item",
        "ValueListItem",
    ),
    "refund": ("stripe._refund", "Refund"),
    "reporting.report_run": ("stripe.reporting._report_run", "ReportRun"),
    "reporting.report_type": ("stripe.reporting._report_type", "ReportType"),
    "reserve_transaction": (
        "stripe._reserve_transaction",
        "ReserveTransaction",
    ),
    "transfer_reversal": ("stripe._reversal", "Reversal"),
    "review": ("stripe._review", "Review"),
    "setup_attempt": ("stripe._setup_attempt", "SetupAttempt"),
    "setup_intent": ("stripe._setup_intent", "SetupIntent"),
    "shared_payment.granted_token": (
        "stripe.shared_payment._granted_token",
        "GrantedToken",
    ),
    "shipping_rate": ("stripe._shipping_rate", "ShippingRate"),
    "scheduled_query_run": (
        "stripe.sigma._scheduled_query_run",
        "ScheduledQueryRun",
    ),
    "source": ("stripe._source", "Source"),
    "source_mandate_notification": (
        "stripe._source_mandate_notification",
        "SourceMandateNotification",
    ),
    "source_transaction": ("stripe._source_transaction", "SourceTransaction"),
    "subscription": ("stripe._subscription", "Subscription"),
    "subscription_item": ("stripe._subscription_item", "SubscriptionItem"),
    "subscription_schedule": (
        "stripe._subscription_schedule",
        "SubscriptionSchedule",
    ),
    "tax.association": ("stripe.tax._association", "Association"),
    "tax.calculation": ("stripe.tax._calculation", "Calculation"),
    "tax.calculation_line_item": (
        "stripe.tax._calculation_line_item",
        "CalculationLineItem",
    ),
    "tax.form": ("stripe.tax._form", "Form"),
    "tax.location": ("stripe.tax._location", "Location"),
    "tax.registration": ("stripe.tax._registration", "Registration"),
    "tax.settings": ("stripe.tax._settings", "Settings"),
    "tax.transaction": ("stripe.tax._transaction", "Transaction"),
    "tax.transaction_line_item": (
        "stripe.tax._transaction_line_item",
        "TransactionLineItem",
    ),
    "tax_code": ("stripe._tax_code", "TaxCode"),
    "tax_deducted_at_source": (
        "stripe._tax_deducted_at_source",
        "TaxDeductedAtSource",
    ),
    "tax_id": ("stripe._tax_id", "TaxId"),
    "tax_rate": ("stripe._tax_rate", "TaxRate"),
    "terminal.configuration": (
        "stripe.terminal._configuration",
        "Configuration",
    ),
    "terminal.connection_token": (
        "stripe.terminal._connection_token",
        "ConnectionToken",
    ),
    "terminal.location": ("stripe.terminal._location", "Location"),
    "terminal.onboarding_link": (
        "stripe.terminal._onboarding_link",
        "OnboardingLink",
    ),
    "terminal.reader": ("stripe.terminal._reader", "Reader"),
    "terminal.reader_collected_data": (
        "stripe.terminal._reader_collected_data",
        "ReaderCollectedData",
    ),
    "test_helpers.test_clock": (
        "stripe.test_helpers._test_clock",
        "TestClock",
    ),
    "token": ("stripe._token", "Token"),
    "topup": ("stripe._topup", "Topup"),
    "transfer": ("stripe._transfer", "Transfer"),
    "transit_balance": ("stripe._transit_balance", "TransitBalance"),
    "treasury.credit_reversal": (
        "stripe.treasury._credit_reversal",
        "CreditReversal",
    ),
    "treasury.debit_reversal": (
        "stripe.treasury._debit_reversal",
        "DebitReversal",
    ),
    "treasury.financial_account": (
        "stripe.treasury._financial_account",
        "FinancialAccount",
    ),
    "treasury.financial_account_features": (
        "stripe.treasury._financial_account_features",
        "FinancialAccountFeatures",
    ),
    "treasury.inbound_transfer": (
        "stripe.treasury._inbound_transfer",
        "InboundTransfer",
    ),
    "treasury.outbound_payment": (
        "stripe.treasury._outbound_payment",
        "OutboundPayment",
    ),
    "treasury.outbound_transfer": (
        "stripe.treasury._outbound_transfer",
        "OutboundTransfer",
    ),
    "treasury.received_credit": (
        "stripe.treasury._received_credit",
        "ReceivedCredit",
    ),
    "treasury.received_debit": (
        "stripe.treasury._received_debit",
        "ReceivedDebit",
    ),
    "treasury.transaction": ("stripe.treasury._transaction", "Transaction"),
    "treasury.transaction_entry": (
        "stripe.treasury._transaction_entry",
        "TransactionEntry",
    ),
    "webhook_endpoint": ("stripe._webhook_endpoint", "WebhookEndpoint"),
    # Object classes: The end of the section generated from our OpenAPI spec
}

V2_OBJECT_CLASSES: Dict[str, Tuple[str, str]] = {
    # V2 Object classes: The beginning of the section generated from our OpenAPI spec
    "v2.billing.bill_setting": (
        "stripe.v2.billing._bill_setting",
        "BillSetting",
    ),
    "v2.billing.bill_setting_version": (
        "stripe.v2.billing._bill_setting_version",
        "BillSettingVersion",
    ),
    "v2.billing.cadence": ("stripe.v2.billing._cadence", "Cadence"),
    "v2.billing.collection_setting": (
        "stripe.v2.billing._collection_setting",
        "CollectionSetting",
    ),
    "v2.billing.collection_setting_version": (
        "stripe.v2.billing._collection_setting_version",
        "CollectionSettingVersion",
    ),
    "v2.billing.custom_pricing_unit": (
        "stripe.v2.billing._custom_pricing_unit",
        "CustomPricingUnit",
    ),
    "v2.billing.intent": ("stripe.v2.billing._intent", "Intent"),
    "v2.billing.intent_action": (
        "stripe.v2.billing._intent_action",
        "IntentAction",
    ),
    "v2.billing.licensed_item": (
        "stripe.v2.billing._licensed_item",
        "LicensedItem",
    ),
    "v2.billing.license_fee": ("stripe.v2.billing._license_fee", "LicenseFee"),
    "v2.billing.license_fee_subscription": (
        "stripe.v2.billing._license_fee_subscription",
        "LicenseFeeSubscription",
    ),
    "v2.billing.license_fee_version": (
        "stripe.v2.billing._license_fee_version",
        "LicenseFeeVersion",
    ),
    "v2.billing.metered_item": (
        "stripe.v2.billing._metered_item",
        "MeteredItem",
    ),
    "v2.billing.meter_event": ("stripe.v2.billing._meter_event", "MeterEvent"),
    "v2.billing.meter_event_adjustment": (
        "stripe.v2.billing._meter_event_adjustment",
        "MeterEventAdjustment",
    ),
    "v2.billing.meter_event_session": (
        "stripe.v2.billing._meter_event_session",
        "MeterEventSession",
    ),
    "v2.billing.pricing_plan": (
        "stripe.v2.billing._pricing_plan",
        "PricingPlan",
    ),
    "v2.billing.pricing_plan_component": (
        "stripe.v2.billing._pricing_plan_component",
        "PricingPlanComponent",
    ),
    "v2.billing.pricing_plan_subscription": (
        "stripe.v2.billing._pricing_plan_subscription",
        "PricingPlanSubscription",
    ),
    "v2.billing.pricing_plan_subscription_components": (
        "stripe.v2.billing._pricing_plan_subscription_components",
        "PricingPlanSubscriptionComponents",
    ),
    "v2.billing.pricing_plan_version": (
        "stripe.v2.billing._pricing_plan_version",
        "PricingPlanVersion",
    ),
    "v2.billing.profile": ("stripe.v2.billing._profile", "Profile"),
    "v2.billing.rate_card": ("stripe.v2.billing._rate_card", "RateCard"),
    "v2.billing.rate_card_rate": (
        "stripe.v2.billing._rate_card_rate",
        "RateCardRate",
    ),
    "v2.billing.rate_card_subscription": (
        "stripe.v2.billing._rate_card_subscription",
        "RateCardSubscription",
    ),
    "v2.billing.rate_card_version": (
        "stripe.v2.billing._rate_card_version",
        "RateCardVersion",
    ),
    "v2.billing.service_action": (
        "stripe.v2.billing._service_action",
        "ServiceAction",
    ),
    "v2.core.account": ("stripe.v2.core._account", "Account"),
    "v2.core.account_link": ("stripe.v2.core._account_link", "AccountLink"),
    "v2.core.account_person": (
        "stripe.v2.core._account_person",
        "AccountPerson",
    ),
    "v2.core.account_person_token": (
        "stripe.v2.core._account_person_token",
        "AccountPersonToken",
    ),
    "v2.core.account_token": ("stripe.v2.core._account_token", "AccountToken"),
    "v2.core.claimable_sandbox": (
        "stripe.v2.core._claimable_sandbox",
        "ClaimableSandbox",
    ),
    "v2.core.event": ("stripe.v2.core._event", "Event"),
    "v2.core.event_destination": (
        "stripe.v2.core._event_destination",
        "EventDestination",
    ),
    "v2.core.vault.gb_bank_account": (
        "stripe.v2.core.vault._gb_bank_account",
        "GbBankAccount",
    ),
    "v2.core.vault.us_bank_account": (
        "stripe.v2.core.vault._us_bank_account",
        "UsBankAccount",
    ),
    "financial_address_credit_simulation": (
        "stripe.v2._financial_address_credit_simulation",
        "FinancialAddressCreditSimulation",
    ),
    "financial_address_generated_microdeposits": (
        "stripe.v2._financial_address_generated_microdeposits",
        "FinancialAddressGeneratedMicrodeposits",
    ),
    "v2.iam.api_key": ("stripe.v2.iam._api_key", "ApiKey"),
    "v2.money_management.adjustment": (
        "stripe.v2.money_management._adjustment",
        "Adjustment",
    ),
    "v2.money_management.currency_conversion": (
        "stripe.v2.money_management._currency_conversion",
        "CurrencyConversion",
    ),
    "v2.money_management.financial_account": (
        "stripe.v2.money_management._financial_account",
        "FinancialAccount",
    ),
    "v2.money_management.financial_address": (
        "stripe.v2.money_management._financial_address",
        "FinancialAddress",
    ),
    "v2.money_management.inbound_transfer": (
        "stripe.v2.money_management._inbound_transfer",
        "InboundTransfer",
    ),
    "v2.money_management.outbound_payment": (
        "stripe.v2.money_management._outbound_payment",
        "OutboundPayment",
    ),
    "v2.money_management.outbound_payment_quote": (
        "stripe.v2.money_management._outbound_payment_quote",
        "OutboundPaymentQuote",
    ),
    "v2.money_management.outbound_setup_intent": (
        "stripe.v2.money_management._outbound_setup_intent",
        "OutboundSetupIntent",
    ),
    "v2.money_management.outbound_transfer": (
        "stripe.v2.money_management._outbound_transfer",
        "OutboundTransfer",
    ),
    "v2.money_management.payout_method": (
        "stripe.v2.money_management._payout_method",
        "PayoutMethod",
    ),
    "v2.money_management.payout_methods_bank_account_spec": (
        "stripe.v2.money_management._payout_methods_bank_account_spec",
        "PayoutMethodsBankAccountSpec",
    ),
    "v2.money_management.received_credit": (
        "stripe.v2.money_management._received_credit",
        "ReceivedCredit",
    ),
    "v2.money_management.received_debit": (
        "stripe.v2.money_management._received_debit",
        "ReceivedDebit",
    ),
    "v2.money_management.recipient_verification": (
        "stripe.v2.money_management._recipient_verification",
        "RecipientVerification",
    ),
    "v2.money_management.transaction": (
        "stripe.v2.money_management._transaction",
        "Transaction",
    ),
    "v2.money_management.transaction_entry": (
        "stripe.v2.money_management._transaction_entry",
        "TransactionEntry",
    ),
    "v2.payments.off_session_payment": (
        "stripe.v2.payments._off_session_payment",
        "OffSessionPayment",
    ),
    "v2.payments.settlement_allocation_intent": (
        "stripe.v2.payments._settlement_allocation_intent",
        "SettlementAllocationIntent",
    ),
    "v2.payments.settlement_allocation_intent_split": (
        "stripe.v2.payments._settlement_allocation_intent_split",
        "SettlementAllocationIntentSplit",
    ),
    "v2.reporting.report": ("stripe.v2.reporting._report", "Report"),
    "v2.reporting.report_run": (
        "stripe.v2.reporting._report_run",
        "ReportRun",
    ),
    "v2.tax.manual_rule": ("stripe.v2.tax._manual_rule", "ManualRule"),
    # V2 Object classes: The end of the section generated from our OpenAPI spec
}


def get_object_class(
    api_mode: "ApiMode", object_name: str
) -> Type[StripeObject]:
    mapping = OBJECT_CLASSES if api_mode == "V1" else V2_OBJECT_CLASSES

    if object_name not in mapping:
        return StripeObject

    import_path, class_name = mapping[object_name]
    return getattr(
        import_module(import_path),
        class_name,
    )
