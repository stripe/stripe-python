# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._expandable_field import ExpandableField
from stripe._list_object import ListObject
from stripe._stripe_object import StripeObject
from typing import ClassVar, Dict, List, Optional, Union
from typing_extensions import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._account import Account
    from stripe._application import Application
    from stripe._bank_account import BankAccount
    from stripe._card import Card as CardResource
    from stripe._discount import Discount
    from stripe._invoice import Invoice
    from stripe._invoice_line_item import InvoiceLineItem
    from stripe._invoice_payment import InvoicePayment
    from stripe._margin import Margin
    from stripe._payment_intent import PaymentIntent
    from stripe._payment_method import PaymentMethod
    from stripe._quote import Quote
    from stripe._setup_intent import SetupIntent
    from stripe._shipping_rate import ShippingRate
    from stripe._source import Source
    from stripe._subscription import Subscription
    from stripe._tax_id import TaxId
    from stripe._tax_rate import TaxRate
    from stripe.test_helpers._test_clock import TestClock


class QuotePreviewInvoice(StripeObject):
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

    OBJECT_NAME: ClassVar[
        Literal["quote_preview_invoice"]
    ] = "quote_preview_invoice"

    class AmountsDue(StripeObject):
        amount: int
        """
        Incremental amount due for this payment in cents (or local equivalent).
        """
        amount_paid: int
        """
        The amount in cents (or local equivalent) that was paid for this payment.
        """
        amount_remaining: int
        """
        The difference between the payment's amount and amount_paid, in cents (or local equivalent).
        """
        days_until_due: Optional[int]
        """
        Number of days from when invoice is finalized until the payment is due.
        """
        description: Optional[str]
        """
        An arbitrary string attached to the object. Often useful for displaying to users.
        """
        due_date: Optional[int]
        """
        Date on which a payment plan's payment is due.
        """
        paid_at: Optional[int]
        """
        Timestamp when the payment was paid.
        """
        status: Literal["open", "paid", "past_due"]
        """
        The status of the payment, one of `open`, `paid`, or `past_due`
        """

    class AppliesTo(StripeObject):
        new_reference: Optional[str]
        """
        A custom string that identifies a new subscription schedule being created upon quote acceptance. All quote lines with the same `new_reference` field will be applied to the creation of a new subscription schedule.
        """
        subscription_schedule: Optional[str]
        """
        The ID of the schedule the line applies to.
        """
        type: Literal["new_reference", "subscription_schedule"]
        """
        Describes whether the quote line is affecting a new schedule or an existing schedule.
        """

    class AutomaticTax(StripeObject):
        class Liability(StripeObject):
            account: Optional[ExpandableField["Account"]]
            """
            The connected account being referenced when `type` is `account`.
            """
            type: Literal["account", "self"]
            """
            Type of the account referenced.
            """

        enabled: bool
        """
        Whether Stripe automatically computes tax on this invoice. Note that incompatible invoice items (invoice items with manually specified [tax rates](https://stripe.com/docs/api/tax_rates), negative amounts, or `tax_behavior=unspecified`) cannot be added to automatic tax invoices.
        """
        liability: Optional[Liability]
        """
        The account that's liable for tax. If set, the business address and tax registrations required to perform the tax calculation are loaded from this account. The tax transaction is returned in the report of the connected account.
        """
        status: Optional[
            Literal["complete", "failed", "requires_location_inputs"]
        ]
        """
        The status of the most recent automated tax calculation for this invoice.
        """
        _inner_class_types = {"liability": Liability}

    class CustomField(StripeObject):
        name: str
        """
        The name of the custom field.
        """
        value: str
        """
        The value of the custom field.
        """

    class CustomerAddress(StripeObject):
        city: Optional[str]
        """
        City, district, suburb, town, or village.
        """
        country: Optional[str]
        """
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
        """
        line1: Optional[str]
        """
        Address line 1 (e.g., street, PO Box, or company name).
        """
        line2: Optional[str]
        """
        Address line 2 (e.g., apartment, suite, unit, or building).
        """
        postal_code: Optional[str]
        """
        ZIP or postal code.
        """
        state: Optional[str]
        """
        State, county, province, or region.
        """

    class CustomerShipping(StripeObject):
        class Address(StripeObject):
            city: Optional[str]
            """
            City, district, suburb, town, or village.
            """
            country: Optional[str]
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            line1: Optional[str]
            """
            Address line 1 (e.g., street, PO Box, or company name).
            """
            line2: Optional[str]
            """
            Address line 2 (e.g., apartment, suite, unit, or building).
            """
            postal_code: Optional[str]
            """
            ZIP or postal code.
            """
            state: Optional[str]
            """
            State, county, province, or region.
            """

        address: Optional[Address]
        carrier: Optional[str]
        """
        The delivery service that shipped a physical product, such as Fedex, UPS, USPS, etc.
        """
        name: Optional[str]
        """
        Recipient name.
        """
        phone: Optional[str]
        """
        Recipient phone (including extension).
        """
        tracking_number: Optional[str]
        """
        The tracking number for a physical product, obtained from the delivery service. If multiple tracking numbers were generated for this purchase, please separate them with commas.
        """
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
            "no_voec",
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
        """
        The type of the tax ID, one of `ad_nrt`, `ar_cuit`, `eu_vat`, `bo_tin`, `br_cnpj`, `br_cpf`, `cn_tin`, `co_nit`, `cr_tin`, `do_rcn`, `ec_ruc`, `eu_oss_vat`, `pe_ruc`, `ro_tin`, `rs_pib`, `sv_nit`, `uy_ruc`, `ve_rif`, `vn_tin`, `gb_vat`, `nz_gst`, `au_abn`, `au_arn`, `in_gst`, `no_vat`, `no_voec`, `za_vat`, `ch_vat`, `mx_rfc`, `sg_uen`, `ru_inn`, `ru_kpp`, `ca_bn`, `hk_br`, `es_cif`, `tw_vat`, `th_vat`, `jp_cn`, `jp_rn`, `jp_trn`, `li_uid`, `my_itn`, `us_ein`, `kr_brn`, `ca_qst`, `ca_gst_hst`, `ca_pst_bc`, `ca_pst_mb`, `ca_pst_sk`, `my_sst`, `sg_gst`, `ae_trn`, `cl_tin`, `sa_vat`, `id_npwp`, `my_frp`, `il_vat`, `ge_vat`, `ua_vat`, `is_vat`, `bg_uic`, `hu_tin`, `si_tin`, `ke_pin`, `tr_tin`, `eg_tin`, `ph_tin`, or `unknown`
        """
        value: Optional[str]
        """
        The value of the tax ID.
        """

    class FromInvoice(StripeObject):
        action: str
        """
        The relation between this invoice and the cloned invoice
        """
        invoice: ExpandableField["Invoice"]
        """
        The invoice that was cloned.
        """

    class Issuer(StripeObject):
        account: Optional[ExpandableField["Account"]]
        """
        The connected account being referenced when `type` is `account`.
        """
        type: Literal["account", "self"]
        """
        Type of the account referenced.
        """

    class LastFinalizationError(StripeObject):
        charge: Optional[str]
        """
        For card errors, the ID of the failed charge.
        """
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
                "balance_invalid_parameter",
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
                "customer_tax_location_invalid",
                "debit_not_authorized",
                "email_invalid",
                "expired_card",
                "financial_connections_account_inactive",
                "financial_connections_no_successful_transaction_refresh",
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
                "shipping_address_invalid",
                "shipping_calculation_failed",
                "sku_inactive",
                "state_unsupported",
                "status_transition_invalid",
                "stripe_tax_inactive",
                "tax_id_invalid",
                "taxes_calculation_failed",
                "terminal_location_country_unsupported",
                "terminal_reader_busy",
                "terminal_reader_hardware_fault",
                "terminal_reader_offline",
                "terminal_reader_timeout",
                "testmode_charges_only",
                "tls_version_unsupported",
                "token_already_used",
                "token_card_network_invalid",
                "token_in_use",
                "transfer_source_balance_parameters_mismatch",
                "transfers_not_allowed",
                "url_invalid",
            ]
        ]
        """
        For some errors that could be handled programmatically, a short string indicating the [error code](https://stripe.com/docs/error-codes) reported.
        """
        decline_code: Optional[str]
        """
        For card errors resulting from a card issuer decline, a short string indicating the [card issuer's reason for the decline](https://stripe.com/docs/declines#issuer-declines) if they provide one.
        """
        doc_url: Optional[str]
        """
        A URL to more information about the [error code](https://stripe.com/docs/error-codes) reported.
        """
        message: Optional[str]
        """
        A human-readable message providing more details about the error. For card errors, these messages can be shown to your users.
        """
        param: Optional[str]
        """
        If the error is parameter-specific, the parameter related to the error. For example, you can use this to display a message near the correct form field.
        """
        payment_intent: Optional["PaymentIntent"]
        """
        A PaymentIntent guides you through the process of collecting a payment from your customer.
        We recommend that you create exactly one PaymentIntent for each order or
        customer session in your system. You can reference the PaymentIntent later to
        see the history of payment attempts for a particular session.

        A PaymentIntent transitions through
        [multiple statuses](https://stripe.com/docs/payments/intents#intent-statuses)
        throughout its lifetime as it interfaces with Stripe.js to perform
        authentication flows and ultimately creates at most one successful charge.

        Related guide: [Payment Intents API](https://stripe.com/docs/payments/payment-intents)
        """
        payment_method: Optional["PaymentMethod"]
        """
        PaymentMethod objects represent your customer's payment instruments.
        You can use them with [PaymentIntents](https://stripe.com/docs/payments/payment-intents) to collect payments or save them to
        Customer objects to store instrument details for future payments.

        Related guides: [Payment Methods](https://stripe.com/docs/payments/payment-methods) and [More Payment Scenarios](https://stripe.com/docs/payments/more-payment-scenarios).
        """
        payment_method_type: Optional[str]
        """
        If the error is specific to the type of payment method, the payment method type that had a problem. This field is only populated for invoice-related errors.
        """
        request_log_url: Optional[str]
        """
        A URL to the request log entry in your dashboard.
        """
        setup_intent: Optional["SetupIntent"]
        """
        A SetupIntent guides you through the process of setting up and saving a customer's payment credentials for future payments.
        For example, you can use a SetupIntent to set up and save your customer's card without immediately collecting a payment.
        Later, you can use [PaymentIntents](https://stripe.com/docs/api#payment_intents) to drive the payment flow.

        Create a SetupIntent when you're ready to collect your customer's payment credentials.
        Don't maintain long-lived, unconfirmed SetupIntents because they might not be valid.
        The SetupIntent transitions through multiple [statuses](https://stripe.com/docs/payments/intents#intent-statuses) as it guides
        you through the setup process.

        Successful SetupIntents result in payment credentials that are optimized for future payments.
        For example, cardholders in [certain regions](https://stripe.com/guides/strong-customer-authentication) might need to be run through
        [Strong Customer Authentication](https://stripe.com/docs/strong-customer-authentication) during payment method collection
        to streamline later [off-session payments](https://stripe.com/docs/payments/setup-intents).
        If you use the SetupIntent with a [Customer](https://stripe.com/docs/api#setup_intent_object-customer),
        it automatically attaches the resulting payment method to that Customer after successful setup.
        We recommend using SetupIntents or [setup_future_usage](https://stripe.com/docs/api#payment_intent_object-setup_future_usage) on
        PaymentIntents to save payment methods to prevent saving invalid or unoptimized payment methods.

        By using SetupIntents, you can reduce friction for your customers, even as regulations change over time.

        Related guide: [Setup Intents API](https://stripe.com/docs/payments/setup-intents)
        """
        source: Optional[
            Union["Account", "BankAccount", "CardResource", "Source"]
        ]
        type: Literal[
            "api_error",
            "card_error",
            "idempotency_error",
            "invalid_request_error",
        ]
        """
        The type of error returned. One of `api_error`, `card_error`, `idempotency_error`, or `invalid_request_error`
        """

    class PaymentSettings(StripeObject):
        class PaymentMethodOptions(StripeObject):
            class AcssDebit(StripeObject):
                class MandateOptions(StripeObject):
                    transaction_type: Optional[Literal["business", "personal"]]
                    """
                    Transaction type of the mandate.
                    """

                mandate_options: Optional[MandateOptions]
                verification_method: Optional[
                    Literal["automatic", "instant", "microdeposits"]
                ]
                """
                Bank account verification method.
                """
                _inner_class_types = {"mandate_options": MandateOptions}

            class Bancontact(StripeObject):
                preferred_language: Literal["de", "en", "fr", "nl"]
                """
                Preferred language of the Bancontact authorization page that the customer is redirected to.
                """

            class Card(StripeObject):
                class Installments(StripeObject):
                    enabled: Optional[bool]
                    """
                    Whether Installments are enabled for this Invoice.
                    """

                installments: Optional[Installments]
                request_three_d_secure: Optional[
                    Literal["any", "automatic", "challenge"]
                ]
                """
                We strongly recommend that you rely on our SCA Engine to automatically prompt your customers for authentication based on risk level and [other requirements](https://stripe.com/docs/strong-customer-authentication). However, if you wish to request 3D Secure based on logic from your own fraud engine, provide this option. Read our guide on [manually requesting 3D Secure](https://stripe.com/docs/payments/3d-secure/authentication-flow#manual-three-ds) for more information on how this configuration interacts with Radar and our SCA Engine.
                """
                _inner_class_types = {"installments": Installments}

            class CustomerBalance(StripeObject):
                class BankTransfer(StripeObject):
                    class EuBankTransfer(StripeObject):
                        country: Literal["BE", "DE", "ES", "FR", "IE", "NL"]
                        """
                        The desired country code of the bank account information. Permitted values include: `BE`, `DE`, `ES`, `FR`, `IE`, or `NL`.
                        """

                    eu_bank_transfer: Optional[EuBankTransfer]
                    type: Optional[str]
                    """
                    The bank transfer type that can be used for funding. Permitted values include: `eu_bank_transfer`, `gb_bank_transfer`, `jp_bank_transfer`, `mx_bank_transfer`, or `us_bank_transfer`.
                    """
                    _inner_class_types = {"eu_bank_transfer": EuBankTransfer}

                bank_transfer: Optional[BankTransfer]
                funding_type: Optional[Literal["bank_transfer"]]
                """
                The funding method type to be used when there are not enough funds in the customer balance. Permitted values include: `bank_transfer`.
                """
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
                    """
                    The list of permissions to request. The `payment_method` permission must be included.
                    """
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
                    """
                    Data features requested to be retrieved upon account creation.
                    """

                financial_connections: Optional[FinancialConnections]
                verification_method: Optional[
                    Literal["automatic", "instant", "microdeposits"]
                ]
                """
                Bank account verification method.
                """
                _inner_class_types = {
                    "financial_connections": FinancialConnections,
                }

            acss_debit: Optional[AcssDebit]
            """
            If paying by `acss_debit`, this sub-hash contains details about the Canadian pre-authorized debit payment method options to pass to the invoice's PaymentIntent.
            """
            bancontact: Optional[Bancontact]
            """
            If paying by `bancontact`, this sub-hash contains details about the Bancontact payment method options to pass to the invoice's PaymentIntent.
            """
            card: Optional[Card]
            """
            If paying by `card`, this sub-hash contains details about the Card payment method options to pass to the invoice's PaymentIntent.
            """
            customer_balance: Optional[CustomerBalance]
            """
            If paying by `customer_balance`, this sub-hash contains details about the Bank transfer payment method options to pass to the invoice's PaymentIntent.
            """
            konbini: Optional[Konbini]
            """
            If paying by `konbini`, this sub-hash contains details about the Konbini payment method options to pass to the invoice's PaymentIntent.
            """
            us_bank_account: Optional[UsBankAccount]
            """
            If paying by `us_bank_account`, this sub-hash contains details about the ACH direct debit payment method options to pass to the invoice's PaymentIntent.
            """
            _inner_class_types = {
                "acss_debit": AcssDebit,
                "bancontact": Bancontact,
                "card": Card,
                "customer_balance": CustomerBalance,
                "konbini": Konbini,
                "us_bank_account": UsBankAccount,
            }

        default_mandate: Optional[str]
        """
        ID of the mandate to be used for this invoice. It must correspond to the payment method used to pay the invoice, including the invoice's default_payment_method or default_source, if set.
        """
        payment_method_options: Optional[PaymentMethodOptions]
        """
        Payment-method-specific configuration to provide to the invoice's PaymentIntent.
        """
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
                    "eps",
                    "fpx",
                    "giropay",
                    "grabpay",
                    "ideal",
                    "konbini",
                    "link",
                    "p24",
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
        """
        The list of payment method types (e.g. card) to provide to the invoice's PaymentIntent. If not set, Stripe attempts to automatically determine the types to use by looking at the invoice's default payment method, the subscription's default payment method, the customer's default payment method, and your [invoice template settings](https://dashboard.stripe.com/settings/billing/invoice).
        """
        _inner_class_types = {"payment_method_options": PaymentMethodOptions}

    class Rendering(StripeObject):
        class Pdf(StripeObject):
            page_size: Optional[Literal["a4", "auto", "letter"]]
            """
            Page size of invoice pdf. Options include a4, letter, and auto. If set to auto, page size will be switched to a4 or letter based on customer locale.
            """

        amount_tax_display: Optional[str]
        """
        How line-item prices and amounts will be displayed with respect to tax on invoice PDFs.
        """
        pdf: Optional[Pdf]
        """
        Invoice pdf rendering options
        """
        _inner_class_types = {"pdf": Pdf}

    class RenderingOptions(StripeObject):
        amount_tax_display: Optional[str]
        """
        How line-item prices and amounts will be displayed with respect to tax on invoice PDFs.
        """

    class ShippingCost(StripeObject):
        class Tax(StripeObject):
            amount: int
            """
            Amount of tax applied for this rate.
            """
            rate: "TaxRate"
            """
            Tax rates can be applied to [invoices](https://stripe.com/docs/billing/invoices/tax-rates), [subscriptions](https://stripe.com/docs/billing/subscriptions/taxes) and [Checkout Sessions](https://stripe.com/docs/payments/checkout/set-up-a-subscription#tax-rates) to collect tax.

            Related guide: [Tax rates](https://stripe.com/docs/billing/taxes/tax-rates)
            """
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
            """
            The reasoning behind this tax, for example, if the product is tax exempt. The possible values for this field may be extended as new tax rules are supported.
            """
            taxable_amount: Optional[int]
            """
            The amount on which tax is calculated, in cents (or local equivalent).
            """

        amount_subtotal: int
        """
        Total shipping cost before any taxes are applied.
        """
        amount_tax: int
        """
        Total tax amount applied due to shipping costs. If no tax was applied, defaults to 0.
        """
        amount_total: int
        """
        Total shipping cost after taxes are applied.
        """
        shipping_rate: Optional[ExpandableField["ShippingRate"]]
        """
        The ID of the ShippingRate for this invoice.
        """
        taxes: Optional[List[Tax]]
        """
        The taxes applied to the shipping rate.
        """
        _inner_class_types = {"taxes": Tax}

    class ShippingDetails(StripeObject):
        class Address(StripeObject):
            city: Optional[str]
            """
            City, district, suburb, town, or village.
            """
            country: Optional[str]
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            line1: Optional[str]
            """
            Address line 1 (e.g., street, PO Box, or company name).
            """
            line2: Optional[str]
            """
            Address line 2 (e.g., apartment, suite, unit, or building).
            """
            postal_code: Optional[str]
            """
            ZIP or postal code.
            """
            state: Optional[str]
            """
            State, county, province, or region.
            """

        address: Optional[Address]
        carrier: Optional[str]
        """
        The delivery service that shipped a physical product, such as Fedex, UPS, USPS, etc.
        """
        name: Optional[str]
        """
        Recipient name.
        """
        phone: Optional[str]
        """
        Recipient phone (including extension).
        """
        tracking_number: Optional[str]
        """
        The tracking number for a physical product, obtained from the delivery service. If multiple tracking numbers were generated for this purchase, please separate them with commas.
        """
        _inner_class_types = {"address": Address}

    class StatusTransitions(StripeObject):
        finalized_at: Optional[int]
        """
        The time that the invoice draft was finalized.
        """
        marked_uncollectible_at: Optional[int]
        """
        The time that the invoice was marked uncollectible.
        """
        paid_at: Optional[int]
        """
        The time that the invoice was paid.
        """
        voided_at: Optional[int]
        """
        The time that the invoice was voided.
        """

    class SubscriptionDetails(StripeObject):
        class PauseCollection(StripeObject):
            behavior: Literal["keep_as_draft", "mark_uncollectible", "void"]
            """
            The payment collection behavior for this subscription while paused. One of `keep_as_draft`, `mark_uncollectible`, or `void`.
            """
            resumes_at: Optional[int]
            """
            The time after which the subscription will resume collecting payments.
            """

        metadata: Optional[Dict[str, str]]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that will reflect the metadata of the subscription at the time of invoice creation. *Note: This attribute is populated only for invoices created on or after June 29, 2023.*
        """
        pause_collection: Optional[PauseCollection]
        """
        If specified, payment collection for this subscription will be paused.
        """
        _inner_class_types = {"pause_collection": PauseCollection}

    class ThresholdReason(StripeObject):
        class ItemReason(StripeObject):
            line_item_ids: List[str]
            """
            The IDs of the line items that triggered the threshold invoice.
            """
            usage_gte: int
            """
            The quantity threshold boundary that applied to the given line item.
            """

        amount_gte: Optional[int]
        """
        The total invoice amount threshold boundary if it triggered the threshold invoice.
        """
        item_reasons: List[ItemReason]
        """
        Indicates which line items triggered a threshold invoice.
        """
        _inner_class_types = {"item_reasons": ItemReason}

    class TotalDiscountAmount(StripeObject):
        amount: int
        """
        The amount, in cents (or local equivalent), of the discount.
        """
        discount: ExpandableField["Discount"]
        """
        The discount that was applied to get this discount amount.
        """

    class TotalMarginAmount(StripeObject):
        amount: int
        """
        The amount, in cents (or local equivalent), of the reduction in line item amount.
        """
        margin: ExpandableField["Margin"]
        """
        The margin that was applied to get this margin amount.
        """

    class TotalTaxAmount(StripeObject):
        amount: int
        """
        The amount, in cents (or local equivalent), of the tax.
        """
        inclusive: bool
        """
        Whether this tax amount is inclusive or exclusive.
        """
        tax_rate: ExpandableField["TaxRate"]
        """
        The tax rate that was applied to get this tax amount.
        """
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
        """
        The reasoning behind this tax, for example, if the product is tax exempt. The possible values for this field may be extended as new tax rules are supported.
        """
        taxable_amount: Optional[int]
        """
        The amount on which tax is calculated, in cents (or local equivalent).
        """

    class TransferData(StripeObject):
        amount: Optional[int]
        """
        The amount in cents (or local equivalent) that will be transferred to the destination account when the invoice is paid. By default, the entire amount is transferred to the destination.
        """
        destination: ExpandableField["Account"]
        """
        The account where funds from the payment will be transferred to upon payment success.
        """

    account_country: Optional[str]
    """
    The country of the business associated with this invoice, most often the business creating the invoice.
    """
    account_name: Optional[str]
    """
    The public name of the business associated with this invoice, most often the business creating the invoice.
    """
    account_tax_ids: Optional[List[ExpandableField["TaxId"]]]
    """
    The account tax IDs associated with the invoice. Only editable when the invoice is a draft.
    """
    amount_due: int
    """
    Final amount due at this time for this invoice. If the invoice's total is smaller than the minimum charge amount, for example, or if there is account credit that can be applied to the invoice, the `amount_due` may be 0. If there is a positive `starting_balance` for the invoice (the customer owes money), the `amount_due` will also take that into account. The charge that gets generated for the invoice will be for the amount specified in `amount_due`.
    """
    amount_paid: int
    """
    The amount, in cents (or local equivalent), that was paid.
    """
    amount_remaining: int
    """
    The difference between amount_due and amount_paid, in cents (or local equivalent).
    """
    amount_shipping: int
    """
    This is the sum of all the shipping amounts.
    """
    amounts_due: Optional[List[AmountsDue]]
    """
    List of expected payments and corresponding due dates. This value will be null for invoices where collection_method=charge_automatically.
    """
    application: Optional[ExpandableField["Application"]]
    """
    ID of the Connect Application that created the invoice.
    """
    application_fee_amount: Optional[int]
    """
    The fee in cents (or local equivalent) that will be applied to the invoice and transferred to the application owner's Stripe account when the invoice is paid.
    """
    applies_to: AppliesTo
    attempt_count: int
    """
    Number of payment attempts made for this invoice, from the perspective of the payment retry schedule. Any payment attempt counts as the first attempt, and subsequently only automatic retries increment the attempt count. In other words, manual payment attempts after the first attempt do not affect the retry schedule.
    """
    attempted: bool
    """
    Whether an attempt has been made to pay the invoice. An invoice is not attempted until 1 hour after the `invoice.created` webhook, for example, so you might not want to display that invoice as unpaid to your users.
    """
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
    """
    Indicates the reason why the invoice was created.

    * `manual`: Unrelated to a subscription, for example, created via the invoice editor.
    * `subscription`: No longer in use. Applies to subscriptions from before May 2018 where no distinction was made between updates, cycles, and thresholds.
    * `subscription_create`: A new subscription was created.
    * `subscription_cycle`: A subscription advanced into a new period.
    * `subscription_threshold`: A subscription reached a billing threshold.
    * `subscription_update`: A subscription was updated.
    * `upcoming`: Reserved for simulated invoices, per the upcoming invoice endpoint.
    """
    collection_method: Literal["charge_automatically", "send_invoice"]
    """
    Either `charge_automatically`, or `send_invoice`. When charging automatically, Stripe will attempt to pay this invoice using the default source attached to the customer. When sending an invoice, Stripe will email this invoice to the customer with payment instructions.
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    currency: str
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    custom_fields: Optional[List[CustomField]]
    """
    Custom fields displayed on the invoice.
    """
    customer_address: Optional[CustomerAddress]
    """
    The customer's address. Until the invoice is finalized, this field will equal `customer.address`. Once the invoice is finalized, this field will no longer be updated.
    """
    customer_email: Optional[str]
    """
    The customer's email. Until the invoice is finalized, this field will equal `customer.email`. Once the invoice is finalized, this field will no longer be updated.
    """
    customer_name: Optional[str]
    """
    The customer's name. Until the invoice is finalized, this field will equal `customer.name`. Once the invoice is finalized, this field will no longer be updated.
    """
    customer_phone: Optional[str]
    """
    The customer's phone number. Until the invoice is finalized, this field will equal `customer.phone`. Once the invoice is finalized, this field will no longer be updated.
    """
    customer_shipping: Optional[CustomerShipping]
    """
    The customer's shipping information. Until the invoice is finalized, this field will equal `customer.shipping`. Once the invoice is finalized, this field will no longer be updated.
    """
    customer_tax_exempt: Optional[Literal["exempt", "none", "reverse"]]
    """
    The customer's tax exempt status. Until the invoice is finalized, this field will equal `customer.tax_exempt`. Once the invoice is finalized, this field will no longer be updated.
    """
    customer_tax_ids: Optional[List[CustomerTaxId]]
    """
    The customer's tax IDs. Until the invoice is finalized, this field will contain the same tax IDs as `customer.tax_ids`. Once the invoice is finalized, this field will no longer be updated.
    """
    default_margins: Optional[List[ExpandableField["Margin"]]]
    """
    The margins applied to the invoice. Can be overridden by line item `margins`. Use `expand[]=default_margins` to expand each margin.
    """
    default_payment_method: Optional[ExpandableField["PaymentMethod"]]
    """
    ID of the default payment method for the invoice. It must belong to the customer associated with the invoice. If not set, defaults to the subscription's default payment method, if any, or to the default payment method in the customer's invoice settings.
    """
    default_source: Optional[
        ExpandableField[
            Union["Account", "BankAccount", "CardResource", "Source"]
        ]
    ]
    """
    ID of the default payment source for the invoice. It must belong to the customer associated with the invoice and be in a chargeable state. If not set, defaults to the subscription's default source, if any, or to the customer's default source.
    """
    default_tax_rates: List["TaxRate"]
    """
    The tax rates applied to this invoice, if any.
    """
    description: Optional[str]
    """
    An arbitrary string attached to the object. Often useful for displaying to users. Referenced as 'memo' in the Dashboard.
    """
    discount: Optional["Discount"]
    """
    Describes the current discount applied to this invoice, if there is one. Not populated if there are multiple discounts.
    """
    discounts: Optional[List[ExpandableField["Discount"]]]
    """
    The discounts applied to the invoice. Line item discounts are applied before invoice discounts. Use `expand[]=discounts` to expand each discount.
    """
    due_date: Optional[int]
    """
    The date on which payment for this invoice is due. This value will be `null` for invoices where `collection_method=charge_automatically`.
    """
    effective_at: Optional[int]
    """
    The date when this invoice is in effect. Same as `finalized_at` unless overwritten. When defined, this value replaces the system-generated 'Date of issue' printed on the invoice PDF and receipt.
    """
    ending_balance: Optional[int]
    """
    Ending customer balance after the invoice is finalized. Invoices are finalized approximately an hour after successful webhook delivery or when payment collection is attempted for the invoice. If the invoice has not been finalized yet, this will be null.
    """
    footer: Optional[str]
    """
    Footer displayed on the invoice.
    """
    from_invoice: Optional[FromInvoice]
    """
    Details of the invoice that was cloned. See the [revision documentation](https://stripe.com/docs/invoicing/invoice-revisions) for more details.
    """
    id: str
    """
    Unique identifier for the object. This property is always present unless the invoice is an upcoming invoice. See [Retrieve an upcoming invoice](https://stripe.com/docs/api/invoices/upcoming) for more details.
    """
    issuer: Issuer
    last_finalization_error: Optional[LastFinalizationError]
    """
    The error encountered during the previous attempt to finalize the invoice. This field is cleared when the invoice is successfully finalized.
    """
    latest_revision: Optional[ExpandableField["Invoice"]]
    """
    The ID of the most recent non-draft revision of this invoice
    """
    lines: ListObject["InvoiceLineItem"]
    """
    The individual line items that make up the invoice. `lines` is sorted as follows: (1) pending invoice items (including prorations) in reverse chronological order, (2) subscription items in reverse chronological order, and (3) invoice items added after invoice creation in chronological order.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Optional[Dict[str, str]]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    next_payment_attempt: Optional[int]
    """
    The time at which payment will next be attempted. This value will be `null` for invoices where `collection_method=send_invoice`.
    """
    number: Optional[str]
    """
    A unique, identifying string that appears on emails sent to the customer for this invoice. This starts with the customer's unique invoice_prefix if it is specified.
    """
    object: Literal["quote_preview_invoice"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    on_behalf_of: Optional[ExpandableField["Account"]]
    """
    The account (if any) for which the funds of the invoice payment are intended. If set, the invoice will be presented with the branding and support information of the specified account. See the [Invoices with Connect](https://stripe.com/docs/billing/invoices/connect) documentation for details.
    """
    paid: bool
    """
    Whether payment was successfully collected for this invoice. An invoice can be paid (most commonly) with a charge or with credit from the customer's account balance.
    """
    paid_out_of_band: bool
    """
    Returns true if the invoice was manually marked paid, returns false if the invoice hasn't been paid yet or was paid on Stripe.
    """
    payment_intent: Optional[ExpandableField["PaymentIntent"]]
    """
    The PaymentIntent associated with this invoice. The PaymentIntent is generated when the invoice is finalized, and can then be used to pay the invoice. Note that voiding an invoice will cancel the PaymentIntent.
    """
    payment_settings: PaymentSettings
    payments: Optional[ListObject["InvoicePayment"]]
    """
    Payments for this invoice
    """
    period_end: int
    """
    End of the usage period during which invoice items were added to this invoice.
    """
    period_start: int
    """
    Start of the usage period during which invoice items were added to this invoice.
    """
    post_payment_credit_notes_amount: int
    """
    Total amount of all post-payment credit notes issued for this invoice.
    """
    pre_payment_credit_notes_amount: int
    """
    Total amount of all pre-payment credit notes issued for this invoice.
    """
    quote: Optional[ExpandableField["Quote"]]
    """
    The quote this invoice was generated from.
    """
    receipt_number: Optional[str]
    """
    This is the transaction number that appears on email receipts sent for this invoice.
    """
    rendering: Optional[Rendering]
    """
    The rendering-related settings that control how the invoice is displayed on customer-facing surfaces such as PDF and Hosted Invoice Page.
    """
    rendering_options: Optional[RenderingOptions]
    """
    This is a legacy field that will be removed soon. For details about `rendering_options`, refer to `rendering` instead. Options for invoice PDF rendering.
    """
    shipping_cost: Optional[ShippingCost]
    """
    The details of the cost of shipping, including the ShippingRate applied on the invoice.
    """
    shipping_details: Optional[ShippingDetails]
    """
    Shipping details for the invoice. The Invoice PDF will use the `shipping_details` value if it is set, otherwise the PDF will render the shipping address from the customer.
    """
    starting_balance: int
    """
    Starting customer balance before the invoice is finalized. If the invoice has not been finalized yet, this will be the current customer balance. For revision invoices, this also includes any customer balance that was applied to the original invoice.
    """
    statement_descriptor: Optional[str]
    """
    Extra information about an invoice for the customer's credit card statement.
    """
    status: Optional[Literal["draft", "open", "paid", "uncollectible", "void"]]
    """
    The status of the invoice, one of `draft`, `open`, `paid`, `uncollectible`, or `void`. [Learn more](https://stripe.com/docs/billing/invoices/workflow#workflow-overview)
    """
    status_transitions: StatusTransitions
    subscription: Optional[ExpandableField["Subscription"]]
    """
    The subscription that this invoice was prepared for, if any.
    """
    subscription_details: Optional[SubscriptionDetails]
    """
    Details about the subscription that created this invoice.
    """
    subscription_proration_date: Optional[int]
    """
    Only set for upcoming invoices that preview prorations. The time used to calculate prorations.
    """
    subtotal: int
    """
    Total of all subscriptions, invoice items, and prorations on the invoice before any invoice level discount or exclusive tax is applied. Item discounts are already incorporated
    """
    subtotal_excluding_tax: Optional[int]
    """
    The integer amount in cents (or local equivalent) representing the subtotal of the invoice before any invoice level discount or tax is applied. Item discounts are already incorporated
    """
    tax: Optional[int]
    """
    The amount of tax on this invoice. This is the sum of all the tax amounts on this invoice.
    """
    test_clock: Optional[ExpandableField["TestClock"]]
    """
    ID of the test clock this invoice belongs to.
    """
    threshold_reason: Optional[ThresholdReason]
    total: int
    """
    Total after discounts and taxes.
    """
    total_discount_amounts: Optional[List[TotalDiscountAmount]]
    """
    The aggregate amounts calculated per discount across all line items.
    """
    total_excluding_tax: Optional[int]
    """
    The integer amount in cents (or local equivalent) representing the total amount of the invoice including all discounts but excluding all tax.
    """
    total_margin_amounts: Optional[List[TotalMarginAmount]]
    """
    The aggregate amounts calculated per margin across all line items.
    """
    total_tax_amounts: List[TotalTaxAmount]
    """
    The aggregate amounts calculated per tax rate for all line items.
    """
    transfer_data: Optional[TransferData]
    """
    The account (if any) the payment will be attributed to for tax reporting, and where funds from the payment will be transferred to for the invoice.
    """
    webhooks_delivered_at: Optional[int]
    """
    Invoices are automatically paid or sent 1 hour after webhooks are delivered, or until all webhook delivery attempts have [been exhausted](https://stripe.com/docs/billing/webhooks#understand). This field tracks the time when webhooks for this invoice were successfully delivered. If the invoice had no webhooks to deliver, this will be set while the invoice is being created.
    """
    _inner_class_types = {
        "amounts_due": AmountsDue,
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
        "total_margin_amounts": TotalMarginAmount,
        "total_tax_amounts": TotalTaxAmount,
        "transfer_data": TransferData,
    }
