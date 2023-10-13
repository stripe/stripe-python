# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import util
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    SearchableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.api_resources.search_result_object import SearchResultObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import Dict, List, Optional, Union, cast
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)
from urllib.parse import quote_plus

if TYPE_CHECKING:
    from stripe.api_resources.account import Account
    from stripe.api_resources.application import Application
    from stripe.api_resources.bank_account import BankAccount
    from stripe.api_resources.card import Card as CardResource
    from stripe.api_resources.charge import Charge
    from stripe.api_resources.customer import Customer
    from stripe.api_resources.discount import Discount
    from stripe.api_resources.invoice_line_item import InvoiceLineItem
    from stripe.api_resources.payment_intent import PaymentIntent
    from stripe.api_resources.payment_method import PaymentMethod
    from stripe.api_resources.quote import Quote
    from stripe.api_resources.setup_intent import SetupIntent
    from stripe.api_resources.shipping_rate import ShippingRate
    from stripe.api_resources.source import Source
    from stripe.api_resources.subscription import Subscription
    from stripe.api_resources.tax_id import TaxId
    from stripe.api_resources.tax_rate import TaxRate
    from stripe.api_resources.test_helpers.test_clock import TestClock


class Invoice(
    CreateableAPIResource["Invoice"],
    DeletableAPIResource["Invoice"],
    ListableAPIResource["Invoice"],
    SearchableAPIResource["Invoice"],
    UpdateableAPIResource["Invoice"],
):
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

    OBJECT_NAME = "invoice"

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
        source: Optional[
            Union["Account", "BankAccount", "CardResource", "Source"]
        ]
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

    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            account_tax_ids: NotRequired["Literal['']|List[str]|None"]
            application_fee_amount: NotRequired["int|None"]
            auto_advance: NotRequired["bool|None"]
            automatic_tax: NotRequired["Invoice.CreateParamsAutomaticTax|None"]
            collection_method: NotRequired[
                "Literal['charge_automatically', 'send_invoice']|None"
            ]
            currency: NotRequired["str|None"]
            custom_fields: NotRequired[
                "Literal['']|List[Invoice.CreateParamsCustomField]|None"
            ]
            customer: NotRequired["str|None"]
            days_until_due: NotRequired["int|None"]
            default_payment_method: NotRequired["str|None"]
            default_source: NotRequired["str|None"]
            default_tax_rates: NotRequired["List[str]|None"]
            description: NotRequired["str|None"]
            discounts: NotRequired[
                "Literal['']|List[Invoice.CreateParamsDiscount]|None"
            ]
            due_date: NotRequired["int|None"]
            effective_at: NotRequired["int|None"]
            expand: NotRequired["List[str]|None"]
            footer: NotRequired["str|None"]
            from_invoice: NotRequired["Invoice.CreateParamsFromInvoice|None"]
            issuer: NotRequired["Invoice.CreateParamsIssuer|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            on_behalf_of: NotRequired["str|None"]
            payment_settings: NotRequired[
                "Invoice.CreateParamsPaymentSettings|None"
            ]
            pending_invoice_items_behavior: NotRequired[
                "Literal['exclude', 'include', 'include_and_require']|None"
            ]
            rendering: NotRequired["Invoice.CreateParamsRendering|None"]
            rendering_options: NotRequired[
                "Literal['']|Invoice.CreateParamsRenderingOptions|None"
            ]
            shipping_cost: NotRequired["Invoice.CreateParamsShippingCost|None"]
            shipping_details: NotRequired[
                "Invoice.CreateParamsShippingDetails|None"
            ]
            statement_descriptor: NotRequired["str|None"]
            subscription: NotRequired["str|None"]
            transfer_data: NotRequired["Invoice.CreateParamsTransferData|None"]

        class CreateParamsTransferData(TypedDict):
            amount: NotRequired["int|None"]
            destination: str

        class CreateParamsShippingDetails(TypedDict):
            address: "Invoice.CreateParamsShippingDetailsAddress"
            name: str
            phone: NotRequired["Literal['']|str|None"]

        class CreateParamsShippingDetailsAddress(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]

        class CreateParamsShippingCost(TypedDict):
            shipping_rate: NotRequired["str|None"]
            shipping_rate_data: NotRequired[
                "Invoice.CreateParamsShippingCostShippingRateData|None"
            ]

        class CreateParamsShippingCostShippingRateData(TypedDict):
            delivery_estimate: NotRequired[
                "Invoice.CreateParamsShippingCostShippingRateDataDeliveryEstimate|None"
            ]
            display_name: str
            fixed_amount: NotRequired[
                "Invoice.CreateParamsShippingCostShippingRateDataFixedAmount|None"
            ]
            metadata: NotRequired["Dict[str, str]|None"]
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            tax_code: NotRequired["str|None"]
            type: NotRequired["Literal['fixed_amount']|None"]

        class CreateParamsShippingCostShippingRateDataFixedAmount(TypedDict):
            amount: int
            currency: str
            currency_options: NotRequired[
                "Dict[str, Invoice.CreateParamsShippingCostShippingRateDataFixedAmountCurrencyOptions]|None"
            ]

        class CreateParamsShippingCostShippingRateDataFixedAmountCurrencyOptions(
            TypedDict,
        ):
            amount: int
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]

        class CreateParamsShippingCostShippingRateDataDeliveryEstimate(
            TypedDict,
        ):
            maximum: NotRequired[
                "Invoice.CreateParamsShippingCostShippingRateDataDeliveryEstimateMaximum|None"
            ]
            minimum: NotRequired[
                "Invoice.CreateParamsShippingCostShippingRateDataDeliveryEstimateMinimum|None"
            ]

        class CreateParamsShippingCostShippingRateDataDeliveryEstimateMinimum(
            TypedDict,
        ):
            unit: Literal["business_day", "day", "hour", "month", "week"]
            value: int

        class CreateParamsShippingCostShippingRateDataDeliveryEstimateMaximum(
            TypedDict,
        ):
            unit: Literal["business_day", "day", "hour", "month", "week"]
            value: int

        class CreateParamsRenderingOptions(TypedDict):
            amount_tax_display: NotRequired[
                "Literal['']|Literal['exclude_tax', 'include_inclusive_tax']|None"
            ]

        class CreateParamsRendering(TypedDict):
            amount_tax_display: NotRequired[
                "Literal['']|Literal['exclude_tax', 'include_inclusive_tax']|None"
            ]
            pdf: NotRequired["Invoice.CreateParamsRenderingPdf|None"]

        class CreateParamsRenderingPdf(TypedDict):
            page_size: NotRequired["Literal['a4', 'auto', 'letter']|None"]

        class CreateParamsPaymentSettings(TypedDict):
            default_mandate: NotRequired["Literal['']|str|None"]
            payment_method_options: NotRequired[
                "Invoice.CreateParamsPaymentSettingsPaymentMethodOptions|None"
            ]
            payment_method_types: NotRequired[
                "Literal['']|List[Literal['ach_credit_transfer', 'ach_debit', 'acss_debit', 'au_becs_debit', 'bacs_debit', 'bancontact', 'boleto', 'card', 'cashapp', 'customer_balance', 'fpx', 'giropay', 'grabpay', 'ideal', 'konbini', 'link', 'paynow', 'paypal', 'promptpay', 'sepa_credit_transfer', 'sepa_debit', 'sofort', 'us_bank_account', 'wechat_pay']]|None"
            ]

        class CreateParamsPaymentSettingsPaymentMethodOptions(TypedDict):
            acss_debit: NotRequired[
                "Literal['']|Invoice.CreateParamsPaymentSettingsPaymentMethodOptionsAcssDebit|None"
            ]
            bancontact: NotRequired[
                "Literal['']|Invoice.CreateParamsPaymentSettingsPaymentMethodOptionsBancontact|None"
            ]
            card: NotRequired[
                "Literal['']|Invoice.CreateParamsPaymentSettingsPaymentMethodOptionsCard|None"
            ]
            customer_balance: NotRequired[
                "Literal['']|Invoice.CreateParamsPaymentSettingsPaymentMethodOptionsCustomerBalance|None"
            ]
            konbini: NotRequired[
                "Literal['']|Invoice.CreateParamsPaymentSettingsPaymentMethodOptionsKonbini|None"
            ]
            us_bank_account: NotRequired[
                "Literal['']|Invoice.CreateParamsPaymentSettingsPaymentMethodOptionsUsBankAccount|None"
            ]

        class CreateParamsPaymentSettingsPaymentMethodOptionsUsBankAccount(
            TypedDict,
        ):
            financial_connections: NotRequired[
                "Invoice.CreateParamsPaymentSettingsPaymentMethodOptionsUsBankAccountFinancialConnections|None"
            ]
            verification_method: NotRequired[
                "Literal['automatic', 'instant', 'microdeposits']|None"
            ]

        class CreateParamsPaymentSettingsPaymentMethodOptionsUsBankAccountFinancialConnections(
            TypedDict,
        ):
            permissions: NotRequired[
                "List[Literal['balances', 'ownership', 'payment_method', 'transactions']]|None"
            ]
            prefetch: NotRequired[
                "List[Literal['balances', 'inferred_balances', 'ownership', 'transactions']]|None"
            ]

        class CreateParamsPaymentSettingsPaymentMethodOptionsKonbini(
            TypedDict
        ):
            pass

        class CreateParamsPaymentSettingsPaymentMethodOptionsCustomerBalance(
            TypedDict,
        ):
            bank_transfer: NotRequired[
                "Invoice.CreateParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransfer|None"
            ]
            funding_type: NotRequired["str|None"]

        class CreateParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransfer(
            TypedDict,
        ):
            eu_bank_transfer: NotRequired[
                "Invoice.CreateParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer|None"
            ]
            type: NotRequired["str|None"]

        class CreateParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer(
            TypedDict,
        ):
            country: str

        class CreateParamsPaymentSettingsPaymentMethodOptionsCard(TypedDict):
            installments: NotRequired[
                "Invoice.CreateParamsPaymentSettingsPaymentMethodOptionsCardInstallments|None"
            ]
            request_three_d_secure: NotRequired[
                "Literal['any', 'automatic']|None"
            ]

        class CreateParamsPaymentSettingsPaymentMethodOptionsCardInstallments(
            TypedDict,
        ):
            enabled: NotRequired["bool|None"]
            plan: NotRequired[
                "Literal['']|Invoice.CreateParamsPaymentSettingsPaymentMethodOptionsCardInstallmentsPlan|None"
            ]

        class CreateParamsPaymentSettingsPaymentMethodOptionsCardInstallmentsPlan(
            TypedDict,
        ):
            count: int
            interval: Literal["month"]
            type: Literal["fixed_count"]

        class CreateParamsPaymentSettingsPaymentMethodOptionsBancontact(
            TypedDict,
        ):
            preferred_language: NotRequired[
                "Literal['de', 'en', 'fr', 'nl']|None"
            ]

        class CreateParamsPaymentSettingsPaymentMethodOptionsAcssDebit(
            TypedDict,
        ):
            mandate_options: NotRequired[
                "Invoice.CreateParamsPaymentSettingsPaymentMethodOptionsAcssDebitMandateOptions|None"
            ]
            verification_method: NotRequired[
                "Literal['automatic', 'instant', 'microdeposits']|None"
            ]

        class CreateParamsPaymentSettingsPaymentMethodOptionsAcssDebitMandateOptions(
            TypedDict,
        ):
            transaction_type: NotRequired[
                "Literal['business', 'personal']|None"
            ]

        class CreateParamsIssuer(TypedDict):
            account: NotRequired["str|None"]
            type: Literal["account", "self"]

        class CreateParamsFromInvoice(TypedDict):
            action: Literal["revision"]
            invoice: str

        class CreateParamsDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]
            discount_end: NotRequired[
                "Invoice.CreateParamsDiscountDiscountEnd|None"
            ]

        class CreateParamsDiscountDiscountEnd(TypedDict):
            duration: NotRequired[
                "Invoice.CreateParamsDiscountDiscountEndDuration|None"
            ]
            timestamp: NotRequired["int|None"]
            type: Literal["duration", "timestamp"]

        class CreateParamsDiscountDiscountEndDuration(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            interval_count: int

        class CreateParamsCustomField(TypedDict):
            name: str
            value: str

        class CreateParamsAutomaticTax(TypedDict):
            enabled: bool
            liability: NotRequired[
                "Invoice.CreateParamsAutomaticTaxLiability|None"
            ]

        class CreateParamsAutomaticTaxLiability(TypedDict):
            account: NotRequired["str|None"]
            type: Literal["account", "self"]

        class DeleteParams(RequestOptions):
            pass

        class FinalizeInvoiceParams(RequestOptions):
            auto_advance: NotRequired["bool|None"]
            expand: NotRequired["List[str]|None"]

        class ListParams(RequestOptions):
            collection_method: NotRequired[
                "Literal['charge_automatically', 'send_invoice']|None"
            ]
            created: NotRequired["Invoice.ListParamsCreated|int|None"]
            customer: NotRequired["str|None"]
            due_date: NotRequired["Invoice.ListParamsDueDate|int|None"]
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]
            status: NotRequired[
                "Literal['draft', 'open', 'paid', 'uncollectible', 'void']|None"
            ]
            subscription: NotRequired["str|None"]

        class ListParamsDueDate(TypedDict):
            gt: NotRequired["int|None"]
            gte: NotRequired["int|None"]
            lt: NotRequired["int|None"]
            lte: NotRequired["int|None"]

        class ListParamsCreated(TypedDict):
            gt: NotRequired["int|None"]
            gte: NotRequired["int|None"]
            lt: NotRequired["int|None"]
            lte: NotRequired["int|None"]

        class MarkUncollectibleParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class ModifyParams(RequestOptions):
            account_tax_ids: NotRequired["Literal['']|List[str]|None"]
            application_fee_amount: NotRequired["int|None"]
            auto_advance: NotRequired["bool|None"]
            automatic_tax: NotRequired["Invoice.ModifyParamsAutomaticTax|None"]
            collection_method: NotRequired[
                "Literal['charge_automatically', 'send_invoice']|None"
            ]
            custom_fields: NotRequired[
                "Literal['']|List[Invoice.ModifyParamsCustomField]|None"
            ]
            days_until_due: NotRequired["int|None"]
            default_payment_method: NotRequired["str|None"]
            default_source: NotRequired["Literal['']|str|None"]
            default_tax_rates: NotRequired["Literal['']|List[str]|None"]
            description: NotRequired["str|None"]
            discounts: NotRequired[
                "Literal['']|List[Invoice.ModifyParamsDiscount]|None"
            ]
            due_date: NotRequired["int|None"]
            effective_at: NotRequired["Literal['']|int|None"]
            expand: NotRequired["List[str]|None"]
            footer: NotRequired["str|None"]
            issuer: NotRequired["Invoice.ModifyParamsIssuer|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            on_behalf_of: NotRequired["Literal['']|str|None"]
            payment_settings: NotRequired[
                "Invoice.ModifyParamsPaymentSettings|None"
            ]
            rendering: NotRequired["Invoice.ModifyParamsRendering|None"]
            rendering_options: NotRequired[
                "Literal['']|Invoice.ModifyParamsRenderingOptions|None"
            ]
            shipping_cost: NotRequired[
                "Literal['']|Invoice.ModifyParamsShippingCost|None"
            ]
            shipping_details: NotRequired[
                "Literal['']|Invoice.ModifyParamsShippingDetails|None"
            ]
            statement_descriptor: NotRequired["str|None"]
            transfer_data: NotRequired[
                "Literal['']|Invoice.ModifyParamsTransferData|None"
            ]

        class ModifyParamsTransferData(TypedDict):
            amount: NotRequired["int|None"]
            destination: str

        class ModifyParamsShippingDetails(TypedDict):
            address: "Invoice.ModifyParamsShippingDetailsAddress"
            name: str
            phone: NotRequired["Literal['']|str|None"]

        class ModifyParamsShippingDetailsAddress(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]

        class ModifyParamsShippingCost(TypedDict):
            shipping_rate: NotRequired["str|None"]
            shipping_rate_data: NotRequired[
                "Invoice.ModifyParamsShippingCostShippingRateData|None"
            ]

        class ModifyParamsShippingCostShippingRateData(TypedDict):
            delivery_estimate: NotRequired[
                "Invoice.ModifyParamsShippingCostShippingRateDataDeliveryEstimate|None"
            ]
            display_name: str
            fixed_amount: NotRequired[
                "Invoice.ModifyParamsShippingCostShippingRateDataFixedAmount|None"
            ]
            metadata: NotRequired["Dict[str, str]|None"]
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            tax_code: NotRequired["str|None"]
            type: NotRequired["Literal['fixed_amount']|None"]

        class ModifyParamsShippingCostShippingRateDataFixedAmount(TypedDict):
            amount: int
            currency: str
            currency_options: NotRequired[
                "Dict[str, Invoice.ModifyParamsShippingCostShippingRateDataFixedAmountCurrencyOptions]|None"
            ]

        class ModifyParamsShippingCostShippingRateDataFixedAmountCurrencyOptions(
            TypedDict,
        ):
            amount: int
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]

        class ModifyParamsShippingCostShippingRateDataDeliveryEstimate(
            TypedDict,
        ):
            maximum: NotRequired[
                "Invoice.ModifyParamsShippingCostShippingRateDataDeliveryEstimateMaximum|None"
            ]
            minimum: NotRequired[
                "Invoice.ModifyParamsShippingCostShippingRateDataDeliveryEstimateMinimum|None"
            ]

        class ModifyParamsShippingCostShippingRateDataDeliveryEstimateMinimum(
            TypedDict,
        ):
            unit: Literal["business_day", "day", "hour", "month", "week"]
            value: int

        class ModifyParamsShippingCostShippingRateDataDeliveryEstimateMaximum(
            TypedDict,
        ):
            unit: Literal["business_day", "day", "hour", "month", "week"]
            value: int

        class ModifyParamsRenderingOptions(TypedDict):
            amount_tax_display: NotRequired[
                "Literal['']|Literal['exclude_tax', 'include_inclusive_tax']|None"
            ]

        class ModifyParamsRendering(TypedDict):
            amount_tax_display: NotRequired[
                "Literal['']|Literal['exclude_tax', 'include_inclusive_tax']|None"
            ]
            pdf: NotRequired["Invoice.ModifyParamsRenderingPdf|None"]

        class ModifyParamsRenderingPdf(TypedDict):
            page_size: NotRequired["Literal['a4', 'auto', 'letter']|None"]

        class ModifyParamsPaymentSettings(TypedDict):
            default_mandate: NotRequired["Literal['']|str|None"]
            payment_method_options: NotRequired[
                "Invoice.ModifyParamsPaymentSettingsPaymentMethodOptions|None"
            ]
            payment_method_types: NotRequired[
                "Literal['']|List[Literal['ach_credit_transfer', 'ach_debit', 'acss_debit', 'au_becs_debit', 'bacs_debit', 'bancontact', 'boleto', 'card', 'cashapp', 'customer_balance', 'fpx', 'giropay', 'grabpay', 'ideal', 'konbini', 'link', 'paynow', 'paypal', 'promptpay', 'sepa_credit_transfer', 'sepa_debit', 'sofort', 'us_bank_account', 'wechat_pay']]|None"
            ]

        class ModifyParamsPaymentSettingsPaymentMethodOptions(TypedDict):
            acss_debit: NotRequired[
                "Literal['']|Invoice.ModifyParamsPaymentSettingsPaymentMethodOptionsAcssDebit|None"
            ]
            bancontact: NotRequired[
                "Literal['']|Invoice.ModifyParamsPaymentSettingsPaymentMethodOptionsBancontact|None"
            ]
            card: NotRequired[
                "Literal['']|Invoice.ModifyParamsPaymentSettingsPaymentMethodOptionsCard|None"
            ]
            customer_balance: NotRequired[
                "Literal['']|Invoice.ModifyParamsPaymentSettingsPaymentMethodOptionsCustomerBalance|None"
            ]
            konbini: NotRequired[
                "Literal['']|Invoice.ModifyParamsPaymentSettingsPaymentMethodOptionsKonbini|None"
            ]
            us_bank_account: NotRequired[
                "Literal['']|Invoice.ModifyParamsPaymentSettingsPaymentMethodOptionsUsBankAccount|None"
            ]

        class ModifyParamsPaymentSettingsPaymentMethodOptionsUsBankAccount(
            TypedDict,
        ):
            financial_connections: NotRequired[
                "Invoice.ModifyParamsPaymentSettingsPaymentMethodOptionsUsBankAccountFinancialConnections|None"
            ]
            verification_method: NotRequired[
                "Literal['automatic', 'instant', 'microdeposits']|None"
            ]

        class ModifyParamsPaymentSettingsPaymentMethodOptionsUsBankAccountFinancialConnections(
            TypedDict,
        ):
            permissions: NotRequired[
                "List[Literal['balances', 'ownership', 'payment_method', 'transactions']]|None"
            ]
            prefetch: NotRequired[
                "List[Literal['balances', 'inferred_balances', 'ownership', 'transactions']]|None"
            ]

        class ModifyParamsPaymentSettingsPaymentMethodOptionsKonbini(
            TypedDict
        ):
            pass

        class ModifyParamsPaymentSettingsPaymentMethodOptionsCustomerBalance(
            TypedDict,
        ):
            bank_transfer: NotRequired[
                "Invoice.ModifyParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransfer|None"
            ]
            funding_type: NotRequired["str|None"]

        class ModifyParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransfer(
            TypedDict,
        ):
            eu_bank_transfer: NotRequired[
                "Invoice.ModifyParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer|None"
            ]
            type: NotRequired["str|None"]

        class ModifyParamsPaymentSettingsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer(
            TypedDict,
        ):
            country: str

        class ModifyParamsPaymentSettingsPaymentMethodOptionsCard(TypedDict):
            installments: NotRequired[
                "Invoice.ModifyParamsPaymentSettingsPaymentMethodOptionsCardInstallments|None"
            ]
            request_three_d_secure: NotRequired[
                "Literal['any', 'automatic']|None"
            ]

        class ModifyParamsPaymentSettingsPaymentMethodOptionsCardInstallments(
            TypedDict,
        ):
            enabled: NotRequired["bool|None"]
            plan: NotRequired[
                "Literal['']|Invoice.ModifyParamsPaymentSettingsPaymentMethodOptionsCardInstallmentsPlan|None"
            ]

        class ModifyParamsPaymentSettingsPaymentMethodOptionsCardInstallmentsPlan(
            TypedDict,
        ):
            count: int
            interval: Literal["month"]
            type: Literal["fixed_count"]

        class ModifyParamsPaymentSettingsPaymentMethodOptionsBancontact(
            TypedDict,
        ):
            preferred_language: NotRequired[
                "Literal['de', 'en', 'fr', 'nl']|None"
            ]

        class ModifyParamsPaymentSettingsPaymentMethodOptionsAcssDebit(
            TypedDict,
        ):
            mandate_options: NotRequired[
                "Invoice.ModifyParamsPaymentSettingsPaymentMethodOptionsAcssDebitMandateOptions|None"
            ]
            verification_method: NotRequired[
                "Literal['automatic', 'instant', 'microdeposits']|None"
            ]

        class ModifyParamsPaymentSettingsPaymentMethodOptionsAcssDebitMandateOptions(
            TypedDict,
        ):
            transaction_type: NotRequired[
                "Literal['business', 'personal']|None"
            ]

        class ModifyParamsIssuer(TypedDict):
            account: NotRequired["str|None"]
            type: Literal["account", "self"]

        class ModifyParamsDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]
            discount_end: NotRequired[
                "Invoice.ModifyParamsDiscountDiscountEnd|None"
            ]

        class ModifyParamsDiscountDiscountEnd(TypedDict):
            duration: NotRequired[
                "Invoice.ModifyParamsDiscountDiscountEndDuration|None"
            ]
            timestamp: NotRequired["int|None"]
            type: Literal["duration", "timestamp"]

        class ModifyParamsDiscountDiscountEndDuration(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            interval_count: int

        class ModifyParamsCustomField(TypedDict):
            name: str
            value: str

        class ModifyParamsAutomaticTax(TypedDict):
            enabled: bool
            liability: NotRequired[
                "Invoice.ModifyParamsAutomaticTaxLiability|None"
            ]

        class ModifyParamsAutomaticTaxLiability(TypedDict):
            account: NotRequired["str|None"]
            type: Literal["account", "self"]

        class PayParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            forgive: NotRequired["bool|None"]
            mandate: NotRequired["Literal['']|str|None"]
            off_session: NotRequired["bool|None"]
            paid_out_of_band: NotRequired["bool|None"]
            payment_method: NotRequired["str|None"]
            source: NotRequired["str|None"]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class SendInvoiceParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class UpcomingParams(RequestOptions):
            automatic_tax: NotRequired[
                "Invoice.UpcomingParamsAutomaticTax|None"
            ]
            coupon: NotRequired["str|None"]
            currency: NotRequired["str|None"]
            customer: NotRequired["str|None"]
            customer_details: NotRequired[
                "Invoice.UpcomingParamsCustomerDetails|None"
            ]
            discounts: NotRequired[
                "Literal['']|List[Invoice.UpcomingParamsDiscount]|None"
            ]
            expand: NotRequired["List[str]|None"]
            invoice_items: NotRequired[
                "List[Invoice.UpcomingParamsInvoiceItem]|None"
            ]
            issuer: NotRequired["Invoice.UpcomingParamsIssuer|None"]
            on_behalf_of: NotRequired["Literal['']|str|None"]
            schedule: NotRequired["str|None"]
            subscription: NotRequired["str|None"]
            subscription_billing_cycle_anchor: NotRequired[
                "Literal['now', 'unchanged']|int|None"
            ]
            subscription_cancel_at: NotRequired["Literal['']|int|None"]
            subscription_cancel_at_period_end: NotRequired["bool|None"]
            subscription_cancel_now: NotRequired["bool|None"]
            subscription_default_tax_rates: NotRequired[
                "Literal['']|List[str]|None"
            ]
            subscription_items: NotRequired[
                "List[Invoice.UpcomingParamsSubscriptionItem]|None"
            ]
            subscription_prebilling: NotRequired[
                "Invoice.UpcomingParamsSubscriptionPrebilling|None"
            ]
            subscription_proration_behavior: NotRequired[
                "Literal['always_invoice', 'create_prorations', 'none']|None"
            ]
            subscription_proration_date: NotRequired["int|None"]
            subscription_resume_at: NotRequired["Literal['now']|None"]
            subscription_start_date: NotRequired["int|None"]
            subscription_trial_end: NotRequired["Literal['now']|int|None"]
            subscription_trial_from_plan: NotRequired["bool|None"]

        class UpcomingParamsSubscriptionPrebilling(TypedDict):
            iterations: int

        class UpcomingParamsSubscriptionItem(TypedDict):
            billing_thresholds: NotRequired[
                "Literal['']|Invoice.UpcomingParamsSubscriptionItemBillingThresholds|None"
            ]
            clear_usage: NotRequired["bool|None"]
            deleted: NotRequired["bool|None"]
            discounts: NotRequired[
                "Literal['']|List[Invoice.UpcomingParamsSubscriptionItemDiscount]|None"
            ]
            id: NotRequired["str|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            plan: NotRequired["str|None"]
            price: NotRequired["str|None"]
            price_data: NotRequired[
                "Invoice.UpcomingParamsSubscriptionItemPriceData|None"
            ]
            quantity: NotRequired["int|None"]
            tax_rates: NotRequired["Literal['']|List[str]|None"]

        class UpcomingParamsSubscriptionItemPriceData(TypedDict):
            currency: str
            product: str
            recurring: "Invoice.UpcomingParamsSubscriptionItemPriceDataRecurring"
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            unit_amount: NotRequired["int|None"]
            unit_amount_decimal: NotRequired["float|None"]

        class UpcomingParamsSubscriptionItemPriceDataRecurring(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            interval_count: NotRequired["int|None"]

        class UpcomingParamsSubscriptionItemDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]
            discount_end: NotRequired[
                "Invoice.UpcomingParamsSubscriptionItemDiscountDiscountEnd|None"
            ]

        class UpcomingParamsSubscriptionItemDiscountDiscountEnd(TypedDict):
            duration: NotRequired[
                "Invoice.UpcomingParamsSubscriptionItemDiscountDiscountEndDuration|None"
            ]
            timestamp: NotRequired["int|None"]
            type: Literal["duration", "timestamp"]

        class UpcomingParamsSubscriptionItemDiscountDiscountEndDuration(
            TypedDict,
        ):
            interval: Literal["day", "month", "week", "year"]
            interval_count: int

        class UpcomingParamsSubscriptionItemBillingThresholds(TypedDict):
            usage_gte: int

        class UpcomingParamsIssuer(TypedDict):
            account: NotRequired["str|None"]
            type: Literal["account", "self"]

        class UpcomingParamsInvoiceItem(TypedDict):
            amount: NotRequired["int|None"]
            currency: NotRequired["str|None"]
            description: NotRequired["str|None"]
            discountable: NotRequired["bool|None"]
            discounts: NotRequired[
                "Literal['']|List[Invoice.UpcomingParamsInvoiceItemDiscount]|None"
            ]
            invoiceitem: NotRequired["str|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            period: NotRequired["Invoice.UpcomingParamsInvoiceItemPeriod|None"]
            price: NotRequired["str|None"]
            price_data: NotRequired[
                "Invoice.UpcomingParamsInvoiceItemPriceData|None"
            ]
            quantity: NotRequired["int|None"]
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            tax_code: NotRequired["Literal['']|str|None"]
            tax_rates: NotRequired["Literal['']|List[str]|None"]
            unit_amount: NotRequired["int|None"]
            unit_amount_decimal: NotRequired["float|None"]

        class UpcomingParamsInvoiceItemPriceData(TypedDict):
            currency: str
            product: str
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            unit_amount: NotRequired["int|None"]
            unit_amount_decimal: NotRequired["float|None"]

        class UpcomingParamsInvoiceItemPeriod(TypedDict):
            end: int
            start: int

        class UpcomingParamsInvoiceItemDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]
            discount_end: NotRequired[
                "Invoice.UpcomingParamsInvoiceItemDiscountDiscountEnd|None"
            ]

        class UpcomingParamsInvoiceItemDiscountDiscountEnd(TypedDict):
            duration: NotRequired[
                "Invoice.UpcomingParamsInvoiceItemDiscountDiscountEndDuration|None"
            ]
            timestamp: NotRequired["int|None"]
            type: Literal["duration", "timestamp"]

        class UpcomingParamsInvoiceItemDiscountDiscountEndDuration(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            interval_count: int

        class UpcomingParamsDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]
            discount_end: NotRequired[
                "Invoice.UpcomingParamsDiscountDiscountEnd|None"
            ]

        class UpcomingParamsDiscountDiscountEnd(TypedDict):
            duration: NotRequired[
                "Invoice.UpcomingParamsDiscountDiscountEndDuration|None"
            ]
            timestamp: NotRequired["int|None"]
            type: Literal["duration", "timestamp"]

        class UpcomingParamsDiscountDiscountEndDuration(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            interval_count: int

        class UpcomingParamsCustomerDetails(TypedDict):
            address: NotRequired[
                "Literal['']|Invoice.UpcomingParamsCustomerDetailsAddress|None"
            ]
            shipping: NotRequired[
                "Literal['']|Invoice.UpcomingParamsCustomerDetailsShipping|None"
            ]
            tax: NotRequired["Invoice.UpcomingParamsCustomerDetailsTax|None"]
            tax_exempt: NotRequired[
                "Literal['']|Literal['exempt', 'none', 'reverse']|None"
            ]
            tax_ids: NotRequired[
                "List[Invoice.UpcomingParamsCustomerDetailsTaxId]|None"
            ]

        class UpcomingParamsCustomerDetailsTaxId(TypedDict):
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
                "us_ein",
                "uy_ruc",
                "ve_rif",
                "vn_tin",
                "za_vat",
            ]
            value: str

        class UpcomingParamsCustomerDetailsTax(TypedDict):
            ip_address: NotRequired["Literal['']|str|None"]

        class UpcomingParamsCustomerDetailsShipping(TypedDict):
            address: "Invoice.UpcomingParamsCustomerDetailsShippingAddress"
            name: str
            phone: NotRequired["str|None"]

        class UpcomingParamsCustomerDetailsShippingAddress(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]

        class UpcomingParamsCustomerDetailsAddress(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]

        class UpcomingParamsAutomaticTax(TypedDict):
            enabled: bool
            liability: NotRequired[
                "Invoice.UpcomingParamsAutomaticTaxLiability|None"
            ]

        class UpcomingParamsAutomaticTaxLiability(TypedDict):
            account: NotRequired["str|None"]
            type: Literal["account", "self"]

        class UpcomingLinesParams(RequestOptions):
            automatic_tax: NotRequired[
                "Invoice.UpcomingLinesParamsAutomaticTax|None"
            ]
            coupon: NotRequired["str|None"]
            currency: NotRequired["str|None"]
            customer: NotRequired["str|None"]
            customer_details: NotRequired[
                "Invoice.UpcomingLinesParamsCustomerDetails|None"
            ]
            discounts: NotRequired[
                "Literal['']|List[Invoice.UpcomingLinesParamsDiscount]|None"
            ]
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            invoice_items: NotRequired[
                "List[Invoice.UpcomingLinesParamsInvoiceItem]|None"
            ]
            issuer: NotRequired["Invoice.UpcomingLinesParamsIssuer|None"]
            limit: NotRequired["int|None"]
            on_behalf_of: NotRequired["Literal['']|str|None"]
            schedule: NotRequired["str|None"]
            starting_after: NotRequired["str|None"]
            subscription: NotRequired["str|None"]
            subscription_billing_cycle_anchor: NotRequired[
                "Literal['now', 'unchanged']|int|None"
            ]
            subscription_cancel_at: NotRequired["Literal['']|int|None"]
            subscription_cancel_at_period_end: NotRequired["bool|None"]
            subscription_cancel_now: NotRequired["bool|None"]
            subscription_default_tax_rates: NotRequired[
                "Literal['']|List[str]|None"
            ]
            subscription_items: NotRequired[
                "List[Invoice.UpcomingLinesParamsSubscriptionItem]|None"
            ]
            subscription_prebilling: NotRequired[
                "Invoice.UpcomingLinesParamsSubscriptionPrebilling|None"
            ]
            subscription_proration_behavior: NotRequired[
                "Literal['always_invoice', 'create_prorations', 'none']|None"
            ]
            subscription_proration_date: NotRequired["int|None"]
            subscription_resume_at: NotRequired["Literal['now']|None"]
            subscription_start_date: NotRequired["int|None"]
            subscription_trial_end: NotRequired["Literal['now']|int|None"]
            subscription_trial_from_plan: NotRequired["bool|None"]

        class UpcomingLinesParamsSubscriptionPrebilling(TypedDict):
            iterations: int

        class UpcomingLinesParamsSubscriptionItem(TypedDict):
            billing_thresholds: NotRequired[
                "Literal['']|Invoice.UpcomingLinesParamsSubscriptionItemBillingThresholds|None"
            ]
            clear_usage: NotRequired["bool|None"]
            deleted: NotRequired["bool|None"]
            discounts: NotRequired[
                "Literal['']|List[Invoice.UpcomingLinesParamsSubscriptionItemDiscount]|None"
            ]
            id: NotRequired["str|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            plan: NotRequired["str|None"]
            price: NotRequired["str|None"]
            price_data: NotRequired[
                "Invoice.UpcomingLinesParamsSubscriptionItemPriceData|None"
            ]
            quantity: NotRequired["int|None"]
            tax_rates: NotRequired["Literal['']|List[str]|None"]

        class UpcomingLinesParamsSubscriptionItemPriceData(TypedDict):
            currency: str
            product: str
            recurring: "Invoice.UpcomingLinesParamsSubscriptionItemPriceDataRecurring"
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            unit_amount: NotRequired["int|None"]
            unit_amount_decimal: NotRequired["float|None"]

        class UpcomingLinesParamsSubscriptionItemPriceDataRecurring(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            interval_count: NotRequired["int|None"]

        class UpcomingLinesParamsSubscriptionItemDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]
            discount_end: NotRequired[
                "Invoice.UpcomingLinesParamsSubscriptionItemDiscountDiscountEnd|None"
            ]

        class UpcomingLinesParamsSubscriptionItemDiscountDiscountEnd(
            TypedDict
        ):
            duration: NotRequired[
                "Invoice.UpcomingLinesParamsSubscriptionItemDiscountDiscountEndDuration|None"
            ]
            timestamp: NotRequired["int|None"]
            type: Literal["duration", "timestamp"]

        class UpcomingLinesParamsSubscriptionItemDiscountDiscountEndDuration(
            TypedDict,
        ):
            interval: Literal["day", "month", "week", "year"]
            interval_count: int

        class UpcomingLinesParamsSubscriptionItemBillingThresholds(TypedDict):
            usage_gte: int

        class UpcomingLinesParamsIssuer(TypedDict):
            account: NotRequired["str|None"]
            type: Literal["account", "self"]

        class UpcomingLinesParamsInvoiceItem(TypedDict):
            amount: NotRequired["int|None"]
            currency: NotRequired["str|None"]
            description: NotRequired["str|None"]
            discountable: NotRequired["bool|None"]
            discounts: NotRequired[
                "Literal['']|List[Invoice.UpcomingLinesParamsInvoiceItemDiscount]|None"
            ]
            invoiceitem: NotRequired["str|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            period: NotRequired[
                "Invoice.UpcomingLinesParamsInvoiceItemPeriod|None"
            ]
            price: NotRequired["str|None"]
            price_data: NotRequired[
                "Invoice.UpcomingLinesParamsInvoiceItemPriceData|None"
            ]
            quantity: NotRequired["int|None"]
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            tax_code: NotRequired["Literal['']|str|None"]
            tax_rates: NotRequired["Literal['']|List[str]|None"]
            unit_amount: NotRequired["int|None"]
            unit_amount_decimal: NotRequired["float|None"]

        class UpcomingLinesParamsInvoiceItemPriceData(TypedDict):
            currency: str
            product: str
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            unit_amount: NotRequired["int|None"]
            unit_amount_decimal: NotRequired["float|None"]

        class UpcomingLinesParamsInvoiceItemPeriod(TypedDict):
            end: int
            start: int

        class UpcomingLinesParamsInvoiceItemDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]
            discount_end: NotRequired[
                "Invoice.UpcomingLinesParamsInvoiceItemDiscountDiscountEnd|None"
            ]

        class UpcomingLinesParamsInvoiceItemDiscountDiscountEnd(TypedDict):
            duration: NotRequired[
                "Invoice.UpcomingLinesParamsInvoiceItemDiscountDiscountEndDuration|None"
            ]
            timestamp: NotRequired["int|None"]
            type: Literal["duration", "timestamp"]

        class UpcomingLinesParamsInvoiceItemDiscountDiscountEndDuration(
            TypedDict,
        ):
            interval: Literal["day", "month", "week", "year"]
            interval_count: int

        class UpcomingLinesParamsDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            discount: NotRequired["str|None"]
            discount_end: NotRequired[
                "Invoice.UpcomingLinesParamsDiscountDiscountEnd|None"
            ]

        class UpcomingLinesParamsDiscountDiscountEnd(TypedDict):
            duration: NotRequired[
                "Invoice.UpcomingLinesParamsDiscountDiscountEndDuration|None"
            ]
            timestamp: NotRequired["int|None"]
            type: Literal["duration", "timestamp"]

        class UpcomingLinesParamsDiscountDiscountEndDuration(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            interval_count: int

        class UpcomingLinesParamsCustomerDetails(TypedDict):
            address: NotRequired[
                "Literal['']|Invoice.UpcomingLinesParamsCustomerDetailsAddress|None"
            ]
            shipping: NotRequired[
                "Literal['']|Invoice.UpcomingLinesParamsCustomerDetailsShipping|None"
            ]
            tax: NotRequired[
                "Invoice.UpcomingLinesParamsCustomerDetailsTax|None"
            ]
            tax_exempt: NotRequired[
                "Literal['']|Literal['exempt', 'none', 'reverse']|None"
            ]
            tax_ids: NotRequired[
                "List[Invoice.UpcomingLinesParamsCustomerDetailsTaxId]|None"
            ]

        class UpcomingLinesParamsCustomerDetailsTaxId(TypedDict):
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
                "us_ein",
                "uy_ruc",
                "ve_rif",
                "vn_tin",
                "za_vat",
            ]
            value: str

        class UpcomingLinesParamsCustomerDetailsTax(TypedDict):
            ip_address: NotRequired["Literal['']|str|None"]

        class UpcomingLinesParamsCustomerDetailsShipping(TypedDict):
            address: "Invoice.UpcomingLinesParamsCustomerDetailsShippingAddress"
            name: str
            phone: NotRequired["str|None"]

        class UpcomingLinesParamsCustomerDetailsShippingAddress(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]

        class UpcomingLinesParamsCustomerDetailsAddress(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]

        class UpcomingLinesParamsAutomaticTax(TypedDict):
            enabled: bool
            liability: NotRequired[
                "Invoice.UpcomingLinesParamsAutomaticTaxLiability|None"
            ]

        class UpcomingLinesParamsAutomaticTaxLiability(TypedDict):
            account: NotRequired["str|None"]
            type: Literal["account", "self"]

        class VoidInvoiceParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class SearchParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            page: NotRequired["str|None"]
            query: str

    account_country: Optional[str]
    account_name: Optional[str]
    account_tax_ids: Optional[List[ExpandableField["TaxId"]]]
    amount_due: int
    amount_paid: int
    amount_remaining: int
    amount_shipping: int
    application: Optional[ExpandableField["Application"]]
    application_fee_amount: Optional[int]
    attempt_count: int
    attempted: bool
    auto_advance: Optional[bool]
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
    charge: Optional[ExpandableField["Charge"]]
    collection_method: Literal["charge_automatically", "send_invoice"]
    created: int
    currency: str
    custom_fields: Optional[List[CustomField]]
    customer: Optional[ExpandableField["Customer"]]
    customer_address: Optional[CustomerAddress]
    customer_email: Optional[str]
    customer_name: Optional[str]
    customer_phone: Optional[str]
    customer_shipping: Optional[CustomerShipping]
    customer_tax_exempt: Optional[Literal["exempt", "none", "reverse"]]
    customer_tax_ids: Optional[List[CustomerTaxId]]
    default_payment_method: Optional[ExpandableField["PaymentMethod"]]
    default_source: Optional[
        ExpandableField[
            Union["Account", "BankAccount", "CardResource", "Source"]
        ]
    ]
    default_tax_rates: List["TaxRate"]
    description: Optional[str]
    discount: Optional["Discount"]
    discounts: Optional[List[ExpandableField["Discount"]]]
    due_date: Optional[int]
    effective_at: Optional[int]
    ending_balance: Optional[int]
    footer: Optional[str]
    from_invoice: Optional[FromInvoice]
    hosted_invoice_url: Optional[str]
    id: Optional[str]
    invoice_pdf: Optional[str]
    issuer: Optional[Issuer]
    last_finalization_error: Optional[LastFinalizationError]
    latest_revision: Optional[ExpandableField["Invoice"]]
    lines: ListObject["InvoiceLineItem"]
    livemode: bool
    metadata: Optional[Dict[str, str]]
    next_payment_attempt: Optional[int]
    number: Optional[str]
    object: Literal["invoice"]
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
    deleted: Optional[Literal[True]]

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Invoice.CreateParams"]
    ) -> "Invoice":
        return cast(
            "Invoice",
            cls._static_request(
                "post",
                cls.class_url(),
                api_key,
                idempotency_key,
                stripe_version,
                stripe_account,
                params,
            ),
        )

    @classmethod
    def _cls_delete(
        cls, sid: str, **params: Unpack["Invoice.DeleteParams"]
    ) -> "Invoice":
        url = "%s/%s" % (cls.class_url(), quote_plus(sid))
        return cast(
            "Invoice",
            cls._static_request("delete", url, params=params),
        )

    @util.class_method_variant("_cls_delete")
    def delete(self, **params: Unpack["Invoice.DeleteParams"]) -> "Invoice":
        return self._request_and_refresh(
            "delete",
            self.instance_url(),
            params=params,
        )

    @classmethod
    def _cls_finalize_invoice(
        cls,
        invoice: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Invoice.FinalizeInvoiceParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/invoices/{invoice}/finalize".format(
                invoice=util.sanitize_id(invoice)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_finalize_invoice")
    def finalize_invoice(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Invoice.FinalizeInvoiceParams"]
    ):
        return self._request(
            "post",
            "/v1/invoices/{invoice}/finalize".format(
                invoice=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Invoice.ListParams"]
    ) -> ListObject["Invoice"]:
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

    @classmethod
    def _cls_mark_uncollectible(
        cls,
        invoice: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Invoice.MarkUncollectibleParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/invoices/{invoice}/mark_uncollectible".format(
                invoice=util.sanitize_id(invoice)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_mark_uncollectible")
    def mark_uncollectible(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Invoice.MarkUncollectibleParams"]
    ):
        return self._request(
            "post",
            "/v1/invoices/{invoice}/mark_uncollectible".format(
                invoice=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def modify(cls, id, **params: Unpack["Invoice.ModifyParams"]) -> "Invoice":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Invoice",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def _cls_pay(
        cls,
        invoice: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Invoice.PayParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/invoices/{invoice}/pay".format(
                invoice=util.sanitize_id(invoice)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_pay")
    def pay(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Invoice.PayParams"]
    ):
        return self._request(
            "post",
            "/v1/invoices/{invoice}/pay".format(
                invoice=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Invoice.RetrieveParams"]
    ) -> "Invoice":
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    def _cls_send_invoice(
        cls,
        invoice: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Invoice.SendInvoiceParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/invoices/{invoice}/send".format(
                invoice=util.sanitize_id(invoice)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_send_invoice")
    def send_invoice(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Invoice.SendInvoiceParams"]
    ):
        return self._request(
            "post",
            "/v1/invoices/{invoice}/send".format(
                invoice=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def upcoming(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Invoice.UpcomingParams"]
    ):
        return cls._static_request(
            "get",
            "/v1/invoices/upcoming",
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def upcoming_lines(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Invoice.UpcomingLinesParams"]
    ):
        return cls._static_request(
            "get",
            "/v1/invoices/upcoming/lines",
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def _cls_void_invoice(
        cls,
        invoice: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Invoice.VoidInvoiceParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/invoices/{invoice}/void".format(
                invoice=util.sanitize_id(invoice)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_void_invoice")
    def void_invoice(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Invoice.VoidInvoiceParams"]
    ):
        return self._request(
            "post",
            "/v1/invoices/{invoice}/void".format(
                invoice=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def search(
        cls, *args, **kwargs: Unpack["Invoice.SearchParams"]
    ) -> SearchResultObject["Invoice"]:
        return cls._search(search_url="/v1/invoices/search", *args, **kwargs)

    @classmethod
    def search_auto_paging_iter(
        cls, *args, **kwargs: Unpack["Invoice.SearchParams"]
    ):
        return cls.search(*args, **kwargs).auto_paging_iter()

    _inner_class_types = {
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
