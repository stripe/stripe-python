# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Any, Dict, List, Optional
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.account import Account
    from stripe.api_resources.application import Application
    from stripe.api_resources.discount import Discount
    from stripe.api_resources.invoice import Invoice
    from stripe.api_resources.invoice_line_item import InvoiceLineItem
    from stripe.api_resources.payment_intent import PaymentIntent
    from stripe.api_resources.payment_method import PaymentMethod
    from stripe.api_resources.quote import Quote
    from stripe.api_resources.setup_intent import SetupIntent
    from stripe.api_resources.shipping_rate import ShippingRate
    from stripe.api_resources.subscription import Subscription
    from stripe.api_resources.tax_id import TaxId
    from stripe.api_resources.tax_rate import TaxRate
    from stripe.api_resources.test_helpers.test_clock import TestClock


class QuotePreviewInvoice(ListableAPIResource["QuotePreviewInvoice"]):
    """
    Invoices are statements of amounts owed by a customer, and are either
    generated one-off, or generated periodically from a subscription.

    They contain [invoice items](https://stripe.com/docs/api#invoiceitems), and proration adjustments
    that may be caused by subscription upgrades/downgrades (if necessary).

    If your invoice is configured to be billed through automatic charges,
    Stripe automatically finalizes your invoice and attempts payment. Note
    that finalizing the invoice,
    [when automatic](https://stripe.com/docs/invoicing/integration/automatic-advancement-collection), does
    not happen immediately as the invoice is created. Stripe waits
    until one hour after the last webhook was successfully sent (or the last
    webhook timed out after failing). If you (and the platforms you may have
    connected to) have no webhooks configured, Stripe waits one hour after
    creation to finalize the invoice.

    If your invoice is configured to be billed by sending an email, then based on your
    [email settings](https://dashboard.stripe.com/account/billing/automatic),
    Stripe will email the invoice to your customer and await payment. These
    emails can contain a link to a hosted page to pay the invoice.

    Stripe applies any customer credit on the account before determining the
    amount due for the invoice (i.e., the amount that will be actually
    charged). If the amount due for the invoice is less than Stripe's [minimum allowed charge
    per currency](https://stripe.com/docs/currencies#minimum-and-maximum-charge-amounts), the
    invoice is automatically marked paid, and we add the amount due to the
    customer's credit balance which is applied to the next invoice.

    More details on the customer's credit balance are
    [here](https://stripe.com/docs/billing/customer/balance).

    Related guide: [Send invoices to customers](https://stripe.com/docs/billing/invoices/sending)
    """

    OBJECT_NAME = "quote_preview_invoice"

    class AppliesTo(StripeObject):
        new_reference: Optional[str]
        subscription_schedule: Optional[str]
        type: Literal["new_reference", "subscription_schedule"]

    class AutomaticTax(StripeObject):
        class Liability(StripeObject):
            account: Optional[ExpandableField["Account"]]
            type: Literal["account", "self"]

        enabled: bool
        liability: Optional[Liability]
        status: Optional[
            Literal["complete", "failed", "requires_location_inputs"]
        ]
        _inner_class_types = {"liability": Liability}

    class CustomField(StripeObject):
        name: str
        value: str

    class CustomerAddress(StripeObject):
        city: Optional[str]
        country: Optional[str]
        line1: Optional[str]
        line2: Optional[str]
        postal_code: Optional[str]
        state: Optional[str]

    class CustomerShipping(StripeObject):
        class Address(StripeObject):
            city: Optional[str]
            country: Optional[str]
            line1: Optional[str]
            line2: Optional[str]
            postal_code: Optional[str]
            state: Optional[str]

        address: Optional[Address]
        carrier: Optional[str]
        name: Optional[str]
        phone: Optional[str]
        tracking_number: Optional[str]
        _inner_class_types = {"address": Address}

    class CustomerTaxId(StripeObject):
        type: Literal[
            "ad_nrt",
            "ae_trn",
            "ar_cuit",
            "au_abn",
            "au_arn",
            "bg_uic",
            "bo_tin",
            "br_cnpj",
            "br_cpf",
            "ca_bn",
            "ca_gst_hst",
            "ca_pst_bc",
            "ca_pst_mb",
            "ca_pst_sk",
            "ca_qst",
            "ch_vat",
            "cl_tin",
            "cn_tin",
            "co_nit",
            "cr_tin",
            "do_rcn",
            "ec_ruc",
            "eg_tin",
            "es_cif",
            "eu_oss_vat",
            "eu_vat",
            "gb_vat",
            "ge_vat",
            "hk_br",
            "hu_tin",
            "id_npwp",
            "il_vat",
            "in_gst",
            "is_vat",
            "jp_cn",
            "jp_rn",
            "jp_trn",
            "ke_pin",
            "kr_brn",
            "li_uid",
            "mx_rfc",
            "my_frp",
            "my_itn",
            "my_sst",
            "no_vat",
            "nz_gst",
            "pe_ruc",
            "ph_tin",
            "ro_tin",
            "rs_pib",
            "ru_inn",
            "ru_kpp",
            "sa_vat",
            "sg_gst",
            "sg_uen",
            "si_tin",
            "sv_nit",
            "th_vat",
            "tr_tin",
            "tw_vat",
            "ua_vat",
            "unknown",
            "us_ein",
            "uy_ruc",
            "ve_rif",
            "vn_tin",
            "za_vat",
        ]
        value: Optional[str]

    class FromInvoice(StripeObject):
        action: str
        invoice: ExpandableField["Invoice"]

    class Issuer(StripeObject):
        account: Optional[ExpandableField["Account"]]
        type: Literal["account", "self"]

    class LastFinalizationError(StripeObject):
        charge: Optional[str]
        code: Optional[
            Literal[
                "account_closed",
                "account_country_invalid_address",
                "account_error_country_change_requires_additional_steps",
                "account_information_mismatch",
                "account_invalid",
                "account_number_invalid",
                "acss_debit_session_incomplete",
                "alipay_upgrade_required",
                "amount_too_large",
                "amount_too_small",
                "api_key_expired",
                "application_fees_not_allowed",
                "authentication_required",
                "balance_insufficient",
                "bank_account_bad_routing_numbers",
                "bank_account_declined",
                "bank_account_exists",
                "bank_account_restricted",
                "bank_account_unusable",
                "bank_account_unverified",
                "bank_account_verification_failed",
                "billing_invalid_mandate",
                "bitcoin_upgrade_required",
                "capture_charge_authorization_expired",
                "capture_unauthorized_payment",
                "card_decline_rate_limit_exceeded",
                "card_declined",
                "cardholder_phone_number_required",
                "charge_already_captured",
                "charge_already_refunded",
                "charge_disputed",
                "charge_exceeds_source_limit",
                "charge_expired_for_capture",
                "charge_invalid_parameter",
                "charge_not_refundable",
                "clearing_code_unsupported",
                "country_code_invalid",
                "country_unsupported",
                "coupon_expired",
                "customer_max_payment_methods",
                "customer_max_subscriptions",
                "debit_not_authorized",
                "email_invalid",
                "expired_card",
                "gift_card_balance_insufficient",
                "gift_card_code_exists",
                "gift_card_inactive",
                "idempotency_key_in_use",
                "incorrect_address",
                "incorrect_cvc",
                "incorrect_number",
                "incorrect_zip",
                "instant_payouts_config_disabled",
                "instant_payouts_currency_disabled",
                "instant_payouts_limit_exceeded",
                "instant_payouts_unsupported",
                "insufficient_funds",
                "intent_invalid_state",
                "intent_verification_method_missing",
                "invalid_card_type",
                "invalid_characters",
                "invalid_charge_amount",
                "invalid_cvc",
                "invalid_expiry_month",
                "invalid_expiry_year",
                "invalid_number",
                "invalid_source_usage",
                "invalid_tax_location",
                "invoice_no_customer_line_items",
                "invoice_no_payment_method_types",
                "invoice_no_subscription_line_items",
                "invoice_not_editable",
                "invoice_on_behalf_of_not_editable",
                "invoice_payment_intent_requires_action",
                "invoice_upcoming_none",
                "livemode_mismatch",
                "lock_timeout",
                "missing",
                "no_account",
                "not_allowed_on_standard_account",
                "out_of_inventory",
                "ownership_declaration_not_allowed",
                "parameter_invalid_empty",
                "parameter_invalid_integer",
                "parameter_invalid_string_blank",
                "parameter_invalid_string_empty",
                "parameter_missing",
                "parameter_unknown",
                "parameters_exclusive",
                "payment_intent_action_required",
                "payment_intent_authentication_failure",
                "payment_intent_incompatible_payment_method",
                "payment_intent_invalid_parameter",
                "payment_intent_konbini_rejected_confirmation_number",
                "payment_intent_mandate_invalid",
                "payment_intent_payment_attempt_expired",
                "payment_intent_payment_attempt_failed",
                "payment_intent_unexpected_state",
                "payment_method_bank_account_already_verified",
                "payment_method_bank_account_blocked",
                "payment_method_billing_details_address_missing",
                "payment_method_configuration_failures",
                "payment_method_currency_mismatch",
                "payment_method_customer_decline",
                "payment_method_invalid_parameter",
                "payment_method_invalid_parameter_testmode",
                "payment_method_microdeposit_failed",
                "payment_method_microdeposit_verification_amounts_invalid",
                "payment_method_microdeposit_verification_amounts_mismatch",
                "payment_method_microdeposit_verification_attempts_exceeded",
                "payment_method_microdeposit_verification_descriptor_code_mismatch",
                "payment_method_microdeposit_verification_timeout",
                "payment_method_not_available",
                "payment_method_provider_decline",
                "payment_method_provider_timeout",
                "payment_method_unactivated",
                "payment_method_unexpected_state",
                "payment_method_unsupported_type",
                "payout_reconciliation_not_ready",
                "payouts_limit_exceeded",
                "payouts_not_allowed",
                "platform_account_required",
                "platform_api_key_expired",
                "postal_code_invalid",
                "processing_error",
                "product_inactive",
                "progressive_onboarding_limit_exceeded",
                "rate_limit",
                "refer_to_customer",
                "refund_disputed_payment",
                "resource_already_exists",
                "resource_missing",
                "return_intent_already_processed",
                "routing_number_invalid",
                "secret_key_required",
                "sensitive_data_access_expired",
                "sepa_unsupported_account",
                "setup_attempt_failed",
                "setup_intent_authentication_failure",
                "setup_intent_invalid_parameter",
                "setup_intent_mandate_invalid",
                "setup_intent_setup_attempt_expired",
                "setup_intent_unexpected_state",
                "shipping_calculation_failed",
                "sku_inactive",
                "state_unsupported",
                "status_transition_invalid",
                "stripe_tax_inactive",
                "tax_id_invalid",
                "taxes_calculation_failed",
                "terminal_location_country_unsupported",
                "terminal_reader_busy",
                "terminal_reader_offline",
                "terminal_reader_timeout",
                "testmode_charges_only",
                "tls_version_unsupported",
                "token_already_used",
                "token_in_use",
                "transfer_source_balance_parameters_mismatch",
                "transfers_not_allowed",
                "url_invalid",
            ]
        ]
        decline_code: Optional[str]
        doc_url: Optional[str]
        message: Optional[str]
        param: Optional[str]
        payment_intent: Optional["PaymentIntent"]
        payment_method: Optional["PaymentMethod"]
        payment_method_type: Optional[str]
        request_log_url: Optional[str]
        setup_intent: Optional["SetupIntent"]
        source: Optional[Any]
        type: Literal[
            "api_error",
            "card_error",
            "idempotency_error",
            "invalid_request_error",
        ]

    class PaymentSettings(StripeObject):
        class PaymentMethodOptions(StripeObject):
            class AcssDebit(StripeObject):
                class MandateOptions(StripeObject):
                    transaction_type: Optional[Literal["business", "personal"]]

                mandate_options: Optional[MandateOptions]
                verification_method: Optional[
                    Literal["automatic", "instant", "microdeposits"]
                ]
                _inner_class_types = {"mandate_options": MandateOptions}

            class Bancontact(StripeObject):
                preferred_language: Literal["de", "en", "fr", "nl"]

            class Card(StripeObject):
                class Installments(StripeObject):
                    enabled: Optional[bool]

                installments: Optional[Installments]
                request_three_d_secure: Optional[Literal["any", "automatic"]]
                _inner_class_types = {"installments": Installments}

            class CustomerBalance(StripeObject):
                class BankTransfer(StripeObject):
                    class EuBankTransfer(StripeObject):
                        country: Literal["BE", "DE", "ES", "FR", "IE", "NL"]

                    eu_bank_transfer: Optional[EuBankTransfer]
                    type: Optional[str]
                    _inner_class_types = {"eu_bank_transfer": EuBankTransfer}

                bank_transfer: Optional[BankTransfer]
                funding_type: Optional[Literal["bank_transfer"]]
                _inner_class_types = {"bank_transfer": BankTransfer}

            class Konbini(StripeObject):
                pass

            class UsBankAccount(StripeObject):
                class FinancialConnections(StripeObject):
                    permissions: Optional[
                        List[
                            Literal[
                                "balances",
                                "ownership",
                                "payment_method",
                                "transactions",
                            ]
                        ]
                    ]
                    prefetch: Optional[
                        List[
                            Literal[
                                "balances",
                                "inferred_balances",
                                "ownership",
                                "transactions",
                            ]
                        ]
                    ]

                financial_connections: Optional[FinancialConnections]
                verification_method: Optional[
                    Literal["automatic", "instant", "microdeposits"]
                ]
                _inner_class_types = {
                    "financial_connections": FinancialConnections,
                }

            acss_debit: Optional[AcssDebit]
            bancontact: Optional[Bancontact]
            card: Optional[Card]
            customer_balance: Optional[CustomerBalance]
            konbini: Optional[Konbini]
            us_bank_account: Optional[UsBankAccount]
            _inner_class_types = {
                "acss_debit": AcssDebit,
                "bancontact": Bancontact,
                "card": Card,
                "customer_balance": CustomerBalance,
                "konbini": Konbini,
                "us_bank_account": UsBankAccount,
            }

        default_mandate: Optional[str]
        payment_method_options: Optional[PaymentMethodOptions]
        payment_method_types: Optional[
            List[
                Literal[
                    "ach_credit_transfer",
                    "ach_debit",
                    "acss_debit",
                    "au_becs_debit",
                    "bacs_debit",
                    "bancontact",
                    "boleto",
                    "card",
                    "cashapp",
                    "customer_balance",
                    "fpx",
                    "giropay",
                    "grabpay",
                    "ideal",
                    "konbini",
                    "link",
                    "paynow",
                    "paypal",
                    "promptpay",
                    "sepa_credit_transfer",
                    "sepa_debit",
                    "sofort",
                    "us_bank_account",
                    "wechat_pay",
                ]
            ]
        ]
        _inner_class_types = {"payment_method_options": PaymentMethodOptions}

    class Rendering(StripeObject):
        class Pdf(StripeObject):
            page_size: Optional[Literal["a4", "auto", "letter"]]

        amount_tax_display: Optional[str]
        pdf: Optional[Pdf]
        _inner_class_types = {"pdf": Pdf}

    class RenderingOptions(StripeObject):
        amount_tax_display: Optional[str]

    class ShippingCost(StripeObject):
        class Tax(StripeObject):
            amount: int
            rate: "TaxRate"
            taxability_reason: Optional[
                Literal[
                    "customer_exempt",
                    "not_collecting",
                    "not_subject_to_tax",
                    "not_supported",
                    "portion_product_exempt",
                    "portion_reduced_rated",
                    "portion_standard_rated",
                    "product_exempt",
                    "product_exempt_holiday",
                    "proportionally_rated",
                    "reduced_rated",
                    "reverse_charge",
                    "standard_rated",
                    "taxable_basis_reduced",
                    "zero_rated",
                ]
            ]
            taxable_amount: Optional[int]

        amount_subtotal: int
        amount_tax: int
        amount_total: int
        shipping_rate: Optional[ExpandableField["ShippingRate"]]
        taxes: Optional[List[Tax]]
        _inner_class_types = {"taxes": Tax}

    class ShippingDetails(StripeObject):
        class Address(StripeObject):
            city: Optional[str]
            country: Optional[str]
            line1: Optional[str]
            line2: Optional[str]
            postal_code: Optional[str]
            state: Optional[str]

        address: Optional[Address]
        carrier: Optional[str]
        name: Optional[str]
        phone: Optional[str]
        tracking_number: Optional[str]
        _inner_class_types = {"address": Address}

    class StatusTransitions(StripeObject):
        finalized_at: Optional[int]
        marked_uncollectible_at: Optional[int]
        paid_at: Optional[int]
        voided_at: Optional[int]

    class SubscriptionDetails(StripeObject):
        class PauseCollection(StripeObject):
            behavior: Literal["keep_as_draft", "mark_uncollectible", "void"]
            resumes_at: Optional[int]

        metadata: Optional[Dict[str, str]]
        pause_collection: Optional[PauseCollection]
        _inner_class_types = {"pause_collection": PauseCollection}

    class ThresholdReason(StripeObject):
        class ItemReason(StripeObject):
            line_item_ids: List[str]
            usage_gte: int

        amount_gte: Optional[int]
        item_reasons: List[ItemReason]
        _inner_class_types = {"item_reasons": ItemReason}

    class TotalDiscountAmount(StripeObject):
        amount: int
        discount: ExpandableField["Discount"]

    class TotalTaxAmount(StripeObject):
        amount: int
        inclusive: bool
        tax_rate: ExpandableField["TaxRate"]
        taxability_reason: Optional[
            Literal[
                "customer_exempt",
                "not_collecting",
                "not_subject_to_tax",
                "not_supported",
                "portion_product_exempt",
                "portion_reduced_rated",
                "portion_standard_rated",
                "product_exempt",
                "product_exempt_holiday",
                "proportionally_rated",
                "reduced_rated",
                "reverse_charge",
                "standard_rated",
                "taxable_basis_reduced",
                "zero_rated",
            ]
        ]
        taxable_amount: Optional[int]

    class TransferData(StripeObject):
        amount: Optional[int]
        destination: ExpandableField["Account"]

    account_country: Optional[str]
    account_name: Optional[str]
    account_tax_ids: Optional[List[ExpandableField["TaxId"]]]
    amount_due: int
    amount_paid: int
    amount_remaining: int
    amount_shipping: int
    application: Optional[ExpandableField["Application"]]
    application_fee_amount: Optional[int]
    applies_to: AppliesTo
    attempt_count: int
    attempted: bool
    automatic_tax: AutomaticTax
    billing_reason: Optional[
        Literal[
            "automatic_pending_invoice_item_invoice",
            "manual",
            "quote_accept",
            "subscription",
            "subscription_create",
            "subscription_cycle",
            "subscription_threshold",
            "subscription_update",
            "upcoming",
        ]
    ]
    collection_method: Literal["charge_automatically", "send_invoice"]
    created: int
    currency: str
    custom_fields: Optional[List[CustomField]]
    customer_address: Optional[CustomerAddress]
    customer_email: Optional[str]
    customer_name: Optional[str]
    customer_phone: Optional[str]
    customer_shipping: Optional[CustomerShipping]
    customer_tax_exempt: Optional[Literal["exempt", "none", "reverse"]]
    customer_tax_ids: Optional[List[CustomerTaxId]]
    default_payment_method: Optional[ExpandableField["PaymentMethod"]]
    default_source: Optional[ExpandableField[Any]]
    default_tax_rates: List["TaxRate"]
    description: Optional[str]
    discount: Optional["Discount"]
    discounts: Optional[List[ExpandableField["Discount"]]]
    due_date: Optional[int]
    effective_at: Optional[int]
    ending_balance: Optional[int]
    footer: Optional[str]
    from_invoice: Optional[FromInvoice]
    id: str
    issuer: Optional[Issuer]
    last_finalization_error: Optional[LastFinalizationError]
    latest_revision: Optional[ExpandableField["Invoice"]]
    lines: ListObject["InvoiceLineItem"]
    livemode: bool
    metadata: Optional[Dict[str, str]]
    next_payment_attempt: Optional[int]
    number: Optional[str]
    object: Literal["quote_preview_invoice"]
    on_behalf_of: Optional[ExpandableField["Account"]]
    paid: bool
    paid_out_of_band: bool
    payment_intent: Optional[ExpandableField["PaymentIntent"]]
    payment_settings: PaymentSettings
    period_end: int
    period_start: int
    post_payment_credit_notes_amount: int
    pre_payment_credit_notes_amount: int
    quote: Optional[ExpandableField["Quote"]]
    receipt_number: Optional[str]
    rendering: Optional[Rendering]
    rendering_options: Optional[RenderingOptions]
    shipping_cost: Optional[ShippingCost]
    shipping_details: Optional[ShippingDetails]
    starting_balance: int
    statement_descriptor: Optional[str]
    status: Optional[Literal["draft", "open", "paid", "uncollectible", "void"]]
    status_transitions: StatusTransitions
    subscription: Optional[ExpandableField["Subscription"]]
    subscription_details: Optional[SubscriptionDetails]
    subscription_proration_date: Optional[int]
    subtotal: int
    subtotal_excluding_tax: Optional[int]
    tax: Optional[int]
    test_clock: Optional[ExpandableField["TestClock"]]
    threshold_reason: Optional[ThresholdReason]
    total: int
    total_discount_amounts: Optional[List[TotalDiscountAmount]]
    total_excluding_tax: Optional[int]
    total_tax_amounts: List[TotalTaxAmount]
    transfer_data: Optional[TransferData]
    webhooks_delivered_at: Optional[int]

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> ListObject["QuotePreviewInvoice"]:
        result = cls._static_request(
            "get",
            cls.class_url(),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )
        if not isinstance(result, ListObject):

            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    _inner_class_types = {
        "applies_to": AppliesTo,
        "automatic_tax": AutomaticTax,
        "custom_fields": CustomField,
        "customer_address": CustomerAddress,
        "customer_shipping": CustomerShipping,
        "customer_tax_ids": CustomerTaxId,
        "from_invoice": FromInvoice,
        "issuer": Issuer,
        "last_finalization_error": LastFinalizationError,
        "payment_settings": PaymentSettings,
        "rendering": Rendering,
        "rendering_options": RenderingOptions,
        "shipping_cost": ShippingCost,
        "shipping_details": ShippingDetails,
        "status_transitions": StatusTransitions,
        "subscription_details": SubscriptionDetails,
        "threshold_reason": ThresholdReason,
        "total_discount_amounts": TotalDiscountAmount,
        "total_tax_amounts": TotalTaxAmount,
        "transfer_data": TransferData,
    }
