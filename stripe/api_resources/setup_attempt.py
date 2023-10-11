# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Any, List, Optional
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.account import Account
    from stripe.api_resources.application import Application
    from stripe.api_resources.customer import Customer
    from stripe.api_resources.mandate import Mandate
    from stripe.api_resources.payment_intent import PaymentIntent
    from stripe.api_resources.payment_method import PaymentMethod
    from stripe.api_resources.setup_intent import SetupIntent


class SetupAttempt(ListableAPIResource["SetupAttempt"]):
    """
    A SetupAttempt describes one attempted confirmation of a SetupIntent,
    whether that confirmation is successful or unsuccessful. You can use
    SetupAttempts to inspect details of a specific attempt at setting up a
    payment method using a SetupIntent.
    """

    OBJECT_NAME = "setup_attempt"

    class PaymentMethodDetails(StripeObject):
        class AcssDebit(StripeObject):
            pass

        class AuBecsDebit(StripeObject):
            pass

        class BacsDebit(StripeObject):
            pass

        class Bancontact(StripeObject):
            bank_code: Optional[str]
            bank_name: Optional[str]
            bic: Optional[str]
            generated_sepa_debit: Optional[ExpandableField["PaymentMethod"]]
            generated_sepa_debit_mandate: Optional[ExpandableField["Mandate"]]
            iban_last4: Optional[str]
            preferred_language: Optional[Literal["de", "en", "fr", "nl"]]
            verified_name: Optional[str]

        class Boleto(StripeObject):
            pass

        class Card(StripeObject):
            class Checks(StripeObject):
                address_line1_check: Optional[str]
                address_postal_code_check: Optional[str]
                cvc_check: Optional[str]

            class ThreeDSecure(StripeObject):
                authentication_flow: Optional[
                    Literal["challenge", "frictionless"]
                ]
                result: Optional[
                    Literal[
                        "attempt_acknowledged",
                        "authenticated",
                        "exempted",
                        "failed",
                        "not_supported",
                        "processing_error",
                    ]
                ]
                result_reason: Optional[
                    Literal[
                        "abandoned",
                        "bypassed",
                        "canceled",
                        "card_not_enrolled",
                        "network_not_supported",
                        "protocol_error",
                        "rejected",
                    ]
                ]
                version: Optional[Literal["1.0.2", "2.1.0", "2.2.0"]]

            class Wallet(StripeObject):
                class ApplePay(StripeObject):
                    pass

                class GooglePay(StripeObject):
                    pass

                apple_pay: Optional[ApplePay]
                google_pay: Optional[GooglePay]
                type: Literal["apple_pay", "google_pay", "link"]
                _inner_class_types = {
                    "apple_pay": ApplePay,
                    "google_pay": GooglePay,
                }

            brand: Optional[str]
            checks: Optional[Checks]
            country: Optional[str]
            description: Optional[str]
            exp_month: Optional[int]
            exp_year: Optional[int]
            fingerprint: Optional[str]
            funding: Optional[str]
            iin: Optional[str]
            issuer: Optional[str]
            last4: Optional[str]
            network: Optional[str]
            three_d_secure: Optional[ThreeDSecure]
            wallet: Optional[Wallet]
            _inner_class_types = {
                "checks": Checks,
                "three_d_secure": ThreeDSecure,
                "wallet": Wallet,
            }

        class CardPresent(StripeObject):
            generated_card: Optional[ExpandableField["PaymentMethod"]]

        class Cashapp(StripeObject):
            pass

        class Ideal(StripeObject):
            bank: Optional[
                Literal[
                    "abn_amro",
                    "asn_bank",
                    "bunq",
                    "handelsbanken",
                    "ing",
                    "knab",
                    "moneyou",
                    "n26",
                    "rabobank",
                    "regiobank",
                    "revolut",
                    "sns_bank",
                    "triodos_bank",
                    "van_lanschot",
                    "yoursafe",
                ]
            ]
            bic: Optional[
                Literal[
                    "ABNANL2A",
                    "ASNBNL21",
                    "BITSNL2A",
                    "BUNQNL2A",
                    "FVLBNL22",
                    "HANDNL2A",
                    "INGBNL2A",
                    "KNABNL2H",
                    "MOYONL21",
                    "NTSBDEB1",
                    "RABONL2U",
                    "RBRBNL21",
                    "REVOIE23",
                    "REVOLT21",
                    "SNSBNL2A",
                    "TRIONL2U",
                ]
            ]
            generated_sepa_debit: Optional[ExpandableField["PaymentMethod"]]
            generated_sepa_debit_mandate: Optional[ExpandableField["Mandate"]]
            iban_last4: Optional[str]
            verified_name: Optional[str]

        class Klarna(StripeObject):
            pass

        class Link(StripeObject):
            pass

        class Paypal(StripeObject):
            pass

        class SepaDebit(StripeObject):
            pass

        class Sofort(StripeObject):
            bank_code: Optional[str]
            bank_name: Optional[str]
            bic: Optional[str]
            generated_sepa_debit: Optional[ExpandableField["PaymentMethod"]]
            generated_sepa_debit_mandate: Optional[ExpandableField["Mandate"]]
            iban_last4: Optional[str]
            preferred_language: Optional[Literal["de", "en", "fr", "nl"]]
            verified_name: Optional[str]

        class UsBankAccount(StripeObject):
            pass

        acss_debit: Optional[AcssDebit]
        au_becs_debit: Optional[AuBecsDebit]
        bacs_debit: Optional[BacsDebit]
        bancontact: Optional[Bancontact]
        boleto: Optional[Boleto]
        card: Optional[Card]
        card_present: Optional[CardPresent]
        cashapp: Optional[Cashapp]
        ideal: Optional[Ideal]
        klarna: Optional[Klarna]
        link: Optional[Link]
        paypal: Optional[Paypal]
        sepa_debit: Optional[SepaDebit]
        sofort: Optional[Sofort]
        type: str
        us_bank_account: Optional[UsBankAccount]
        _inner_class_types = {
            "acss_debit": AcssDebit,
            "au_becs_debit": AuBecsDebit,
            "bacs_debit": BacsDebit,
            "bancontact": Bancontact,
            "boleto": Boleto,
            "card": Card,
            "card_present": CardPresent,
            "cashapp": Cashapp,
            "ideal": Ideal,
            "klarna": Klarna,
            "link": Link,
            "paypal": Paypal,
            "sepa_debit": SepaDebit,
            "sofort": Sofort,
            "us_bank_account": UsBankAccount,
        }

    class SetupError(StripeObject):
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

    application: Optional[ExpandableField["Application"]]
    attach_to_self: Optional[bool]
    created: int
    customer: Optional[ExpandableField["Customer"]]
    flow_directions: Optional[List[Literal["inbound", "outbound"]]]
    id: str
    livemode: bool
    object: Literal["setup_attempt"]
    on_behalf_of: Optional[ExpandableField["Account"]]
    payment_method: ExpandableField["PaymentMethod"]
    payment_method_details: PaymentMethodDetails
    setup_error: Optional[SetupError]
    setup_intent: ExpandableField["SetupIntent"]
    status: str
    usage: str

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> ListObject["SetupAttempt"]:
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
        "payment_method_details": PaymentMethodDetails,
        "setup_error": SetupError,
    }
