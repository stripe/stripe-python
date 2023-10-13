# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import util
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import Any, Dict, List, Optional, Union, cast
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
    from stripe.api_resources.customer import Customer
    from stripe.api_resources.mandate import Mandate
    from stripe.api_resources.payment_intent import PaymentIntent
    from stripe.api_resources.payment_method import PaymentMethod
    from stripe.api_resources.setup_attempt import SetupAttempt
    from stripe.api_resources.source import Source


class SetupIntent(
    CreateableAPIResource["SetupIntent"],
    ListableAPIResource["SetupIntent"],
    UpdateableAPIResource["SetupIntent"],
):
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

    OBJECT_NAME = "setup_intent"

    class AutomaticPaymentMethods(StripeObject):
        allow_redirects: Optional[Literal["always", "never"]]
        enabled: Optional[bool]

    class LastSetupError(StripeObject):
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

    class NextAction(StripeObject):
        class CashappHandleRedirectOrDisplayQrCode(StripeObject):
            class QrCode(StripeObject):
                expires_at: int
                image_url_png: str
                image_url_svg: str

            hosted_instructions_url: str
            mobile_auth_url: str
            qr_code: QrCode
            _inner_class_types = {"qr_code": QrCode}

        class RedirectToUrl(StripeObject):
            return_url: Optional[str]
            url: Optional[str]

        class VerifyWithMicrodeposits(StripeObject):
            arrival_date: int
            hosted_verification_url: str
            microdeposit_type: Optional[Literal["amounts", "descriptor_code"]]

        cashapp_handle_redirect_or_display_qr_code: Optional[
            CashappHandleRedirectOrDisplayQrCode
        ]
        redirect_to_url: Optional[RedirectToUrl]
        type: str
        use_stripe_sdk: Optional[Dict[str, Any]]
        verify_with_microdeposits: Optional[VerifyWithMicrodeposits]
        _inner_class_types = {
            "cashapp_handle_redirect_or_display_qr_code": CashappHandleRedirectOrDisplayQrCode,
            "redirect_to_url": RedirectToUrl,
            "verify_with_microdeposits": VerifyWithMicrodeposits,
        }

    class PaymentMethodConfigurationDetails(StripeObject):
        id: str
        parent: Optional[str]

    class PaymentMethodOptions(StripeObject):
        class AcssDebit(StripeObject):
            class MandateOptions(StripeObject):
                custom_mandate_url: Optional[str]
                default_for: Optional[List[Literal["invoice", "subscription"]]]
                interval_description: Optional[str]
                payment_schedule: Optional[
                    Literal["combined", "interval", "sporadic"]
                ]
                transaction_type: Optional[Literal["business", "personal"]]

            currency: Optional[Literal["cad", "usd"]]
            mandate_options: Optional[MandateOptions]
            verification_method: Optional[
                Literal["automatic", "instant", "microdeposits"]
            ]
            _inner_class_types = {"mandate_options": MandateOptions}

        class Card(StripeObject):
            class MandateOptions(StripeObject):
                amount: int
                amount_type: Literal["fixed", "maximum"]
                currency: str
                description: Optional[str]
                end_date: Optional[int]
                interval: Literal["day", "month", "sporadic", "week", "year"]
                interval_count: Optional[int]
                reference: str
                start_date: int
                supported_types: Optional[List[Literal["india"]]]

            mandate_options: Optional[MandateOptions]
            network: Optional[
                Literal[
                    "amex",
                    "cartes_bancaires",
                    "diners",
                    "discover",
                    "eftpos_au",
                    "interac",
                    "jcb",
                    "mastercard",
                    "unionpay",
                    "unknown",
                    "visa",
                ]
            ]
            request_three_d_secure: Optional[
                Literal["any", "automatic", "challenge_only"]
            ]
            _inner_class_types = {"mandate_options": MandateOptions}

        class Link(StripeObject):
            persistent_token: Optional[str]

        class Paypal(StripeObject):
            billing_agreement_id: Optional[str]
            currency: Optional[str]

        class SepaDebit(StripeObject):
            class MandateOptions(StripeObject):
                pass

            mandate_options: Optional[MandateOptions]
            _inner_class_types = {"mandate_options": MandateOptions}

        class UsBankAccount(StripeObject):
            class FinancialConnections(StripeObject):
                class ManualEntry(StripeObject):
                    mode: Optional[Literal["automatic", "custom"]]

                manual_entry: Optional[ManualEntry]
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
                return_url: Optional[str]
                _inner_class_types = {"manual_entry": ManualEntry}

            financial_connections: Optional[FinancialConnections]
            verification_method: Optional[
                Literal["automatic", "instant", "microdeposits"]
            ]
            _inner_class_types = {
                "financial_connections": FinancialConnections
            }

        acss_debit: Optional[AcssDebit]
        card: Optional[Card]
        link: Optional[Link]
        paypal: Optional[Paypal]
        sepa_debit: Optional[SepaDebit]
        us_bank_account: Optional[UsBankAccount]
        _inner_class_types = {
            "acss_debit": AcssDebit,
            "card": Card,
            "link": Link,
            "paypal": Paypal,
            "sepa_debit": SepaDebit,
            "us_bank_account": UsBankAccount,
        }

    if TYPE_CHECKING:

        class CancelParams(RequestOptions):
            cancellation_reason: NotRequired[
                "Literal['abandoned', 'duplicate', 'requested_by_customer']|None"
            ]
            expand: NotRequired["List[str]|None"]

        class ConfirmParams(RequestOptions):
            confirmation_token: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            mandate_data: NotRequired[
                "Literal['']|SetupIntent.ConfirmParamsMandateData|SetupIntent.ConfirmParamsMandateData2|None"
            ]
            payment_method: NotRequired["str|None"]
            payment_method_data: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodData|None"
            ]
            payment_method_options: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodOptions|None"
            ]
            return_url: NotRequired["str|None"]
            use_stripe_sdk: NotRequired["bool|None"]

        class ConfirmParamsPaymentMethodOptions(TypedDict):
            acss_debit: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodOptionsAcssDebit|None"
            ]
            card: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodOptionsCard|None"
            ]
            link: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodOptionsLink|None"
            ]
            paypal: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodOptionsPaypal|None"
            ]
            sepa_debit: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodOptionsSepaDebit|None"
            ]
            us_bank_account: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodOptionsUsBankAccount|None"
            ]

        class ConfirmParamsPaymentMethodOptionsUsBankAccount(TypedDict):
            financial_connections: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodOptionsUsBankAccountFinancialConnections|None"
            ]
            networks: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodOptionsUsBankAccountNetworks|None"
            ]
            verification_method: NotRequired[
                "Literal['automatic', 'instant', 'microdeposits']|None"
            ]

        class ConfirmParamsPaymentMethodOptionsUsBankAccountNetworks(
            TypedDict
        ):
            requested: NotRequired[
                "List[Literal['ach', 'us_domestic_wire']]|None"
            ]

        class ConfirmParamsPaymentMethodOptionsUsBankAccountFinancialConnections(
            TypedDict,
        ):
            manual_entry: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodOptionsUsBankAccountFinancialConnectionsManualEntry|None"
            ]
            permissions: NotRequired[
                "List[Literal['balances', 'ownership', 'payment_method', 'transactions']]|None"
            ]
            prefetch: NotRequired[
                "List[Literal['balances', 'inferred_balances', 'ownership', 'transactions']]|None"
            ]
            return_url: NotRequired["str|None"]

        class ConfirmParamsPaymentMethodOptionsUsBankAccountFinancialConnectionsManualEntry(
            TypedDict,
        ):
            mode: Literal["automatic", "custom"]

        class ConfirmParamsPaymentMethodOptionsSepaDebit(TypedDict):
            mandate_options: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodOptionsSepaDebitMandateOptions|None"
            ]

        class ConfirmParamsPaymentMethodOptionsSepaDebitMandateOptions(
            TypedDict,
        ):
            pass

        class ConfirmParamsPaymentMethodOptionsPaypal(TypedDict):
            billing_agreement_id: NotRequired["str|None"]
            currency: NotRequired["str|None"]

        class ConfirmParamsPaymentMethodOptionsLink(TypedDict):
            persistent_token: NotRequired["str|None"]

        class ConfirmParamsPaymentMethodOptionsCard(TypedDict):
            mandate_options: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodOptionsCardMandateOptions|None"
            ]
            moto: NotRequired["bool|None"]
            network: NotRequired[
                "Literal['amex', 'cartes_bancaires', 'diners', 'discover', 'eftpos_au', 'interac', 'jcb', 'mastercard', 'unionpay', 'unknown', 'visa']|None"
            ]
            request_three_d_secure: NotRequired[
                "Literal['any', 'automatic']|None"
            ]

        class ConfirmParamsPaymentMethodOptionsCardMandateOptions(TypedDict):
            amount: int
            amount_type: Literal["fixed", "maximum"]
            currency: str
            description: NotRequired["str|None"]
            end_date: NotRequired["int|None"]
            interval: Literal["day", "month", "sporadic", "week", "year"]
            interval_count: NotRequired["int|None"]
            reference: str
            start_date: int
            supported_types: NotRequired["List[Literal['india']]|None"]

        class ConfirmParamsPaymentMethodOptionsAcssDebit(TypedDict):
            currency: NotRequired["Literal['cad', 'usd']|None"]
            mandate_options: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodOptionsAcssDebitMandateOptions|None"
            ]
            verification_method: NotRequired[
                "Literal['automatic', 'instant', 'microdeposits']|None"
            ]

        class ConfirmParamsPaymentMethodOptionsAcssDebitMandateOptions(
            TypedDict,
        ):
            custom_mandate_url: NotRequired["Literal['']|str|None"]
            default_for: NotRequired[
                "List[Literal['invoice', 'subscription']]|None"
            ]
            interval_description: NotRequired["str|None"]
            payment_schedule: NotRequired[
                "Literal['combined', 'interval', 'sporadic']|None"
            ]
            transaction_type: NotRequired[
                "Literal['business', 'personal']|None"
            ]

        class ConfirmParamsPaymentMethodData(TypedDict):
            acss_debit: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataAcssDebit|None"
            ]
            affirm: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataAffirm|None"
            ]
            afterpay_clearpay: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataAfterpayClearpay|None"
            ]
            alipay: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataAlipay|None"
            ]
            au_becs_debit: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataAuBecsDebit|None"
            ]
            bacs_debit: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataBacsDebit|None"
            ]
            bancontact: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataBancontact|None"
            ]
            billing_details: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataBillingDetails|None"
            ]
            blik: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataBlik|None"
            ]
            boleto: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataBoleto|None"
            ]
            cashapp: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataCashapp|None"
            ]
            customer_balance: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataCustomerBalance|None"
            ]
            eps: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataEps|None"
            ]
            fpx: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataFpx|None"
            ]
            giropay: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataGiropay|None"
            ]
            grabpay: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataGrabpay|None"
            ]
            ideal: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataIdeal|None"
            ]
            interac_present: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataInteracPresent|None"
            ]
            klarna: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataKlarna|None"
            ]
            konbini: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataKonbini|None"
            ]
            link: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataLink|None"
            ]
            metadata: NotRequired["Dict[str, str]|None"]
            oxxo: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataOxxo|None"
            ]
            p24: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataP24|None"
            ]
            paynow: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataPaynow|None"
            ]
            paypal: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataPaypal|None"
            ]
            pix: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataPix|None"
            ]
            promptpay: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataPromptpay|None"
            ]
            radar_options: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataRadarOptions|None"
            ]
            sepa_debit: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataSepaDebit|None"
            ]
            sofort: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataSofort|None"
            ]
            type: Literal[
                "acss_debit",
                "affirm",
                "afterpay_clearpay",
                "alipay",
                "au_becs_debit",
                "bacs_debit",
                "bancontact",
                "blik",
                "boleto",
                "cashapp",
                "customer_balance",
                "eps",
                "fpx",
                "giropay",
                "grabpay",
                "ideal",
                "klarna",
                "konbini",
                "link",
                "oxxo",
                "p24",
                "paynow",
                "paypal",
                "pix",
                "promptpay",
                "sepa_debit",
                "sofort",
                "us_bank_account",
                "wechat_pay",
                "zip",
            ]
            us_bank_account: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataUsBankAccount|None"
            ]
            wechat_pay: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataWechatPay|None"
            ]
            zip: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataZip|None"
            ]

        class ConfirmParamsPaymentMethodDataZip(TypedDict):
            pass

        class ConfirmParamsPaymentMethodDataWechatPay(TypedDict):
            pass

        class ConfirmParamsPaymentMethodDataUsBankAccount(TypedDict):
            account_holder_type: NotRequired[
                "Literal['company', 'individual']|None"
            ]
            account_number: NotRequired["str|None"]
            account_type: NotRequired["Literal['checking', 'savings']|None"]
            financial_connections_account: NotRequired["str|None"]
            routing_number: NotRequired["str|None"]

        class ConfirmParamsPaymentMethodDataSofort(TypedDict):
            country: Literal["AT", "BE", "DE", "ES", "IT", "NL"]

        class ConfirmParamsPaymentMethodDataSepaDebit(TypedDict):
            iban: str

        class ConfirmParamsPaymentMethodDataRadarOptions(TypedDict):
            session: NotRequired["str|None"]

        class ConfirmParamsPaymentMethodDataPromptpay(TypedDict):
            pass

        class ConfirmParamsPaymentMethodDataPix(TypedDict):
            pass

        class ConfirmParamsPaymentMethodDataPaypal(TypedDict):
            pass

        class ConfirmParamsPaymentMethodDataPaynow(TypedDict):
            pass

        class ConfirmParamsPaymentMethodDataP24(TypedDict):
            bank: NotRequired[
                "Literal['alior_bank', 'bank_millennium', 'bank_nowy_bfg_sa', 'bank_pekao_sa', 'banki_spbdzielcze', 'blik', 'bnp_paribas', 'boz', 'citi_handlowy', 'credit_agricole', 'envelobank', 'etransfer_pocztowy24', 'getin_bank', 'ideabank', 'ing', 'inteligo', 'mbank_mtransfer', 'nest_przelew', 'noble_pay', 'pbac_z_ipko', 'plus_bank', 'santander_przelew24', 'tmobile_usbugi_bankowe', 'toyota_bank', 'volkswagen_bank']|None"
            ]

        class ConfirmParamsPaymentMethodDataOxxo(TypedDict):
            pass

        class ConfirmParamsPaymentMethodDataLink(TypedDict):
            pass

        class ConfirmParamsPaymentMethodDataKonbini(TypedDict):
            pass

        class ConfirmParamsPaymentMethodDataKlarna(TypedDict):
            dob: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataKlarnaDob|None"
            ]

        class ConfirmParamsPaymentMethodDataKlarnaDob(TypedDict):
            day: int
            month: int
            year: int

        class ConfirmParamsPaymentMethodDataInteracPresent(TypedDict):
            pass

        class ConfirmParamsPaymentMethodDataIdeal(TypedDict):
            bank: NotRequired[
                "Literal['abn_amro', 'asn_bank', 'bunq', 'handelsbanken', 'ing', 'knab', 'moneyou', 'n26', 'rabobank', 'regiobank', 'revolut', 'sns_bank', 'triodos_bank', 'van_lanschot', 'yoursafe']|None"
            ]

        class ConfirmParamsPaymentMethodDataGrabpay(TypedDict):
            pass

        class ConfirmParamsPaymentMethodDataGiropay(TypedDict):
            pass

        class ConfirmParamsPaymentMethodDataFpx(TypedDict):
            account_holder_type: NotRequired[
                "Literal['company', 'individual']|None"
            ]
            bank: Literal[
                "affin_bank",
                "agrobank",
                "alliance_bank",
                "ambank",
                "bank_islam",
                "bank_muamalat",
                "bank_of_china",
                "bank_rakyat",
                "bsn",
                "cimb",
                "deutsche_bank",
                "hong_leong_bank",
                "hsbc",
                "kfh",
                "maybank2e",
                "maybank2u",
                "ocbc",
                "pb_enterprise",
                "public_bank",
                "rhb",
                "standard_chartered",
                "uob",
            ]

        class ConfirmParamsPaymentMethodDataEps(TypedDict):
            bank: NotRequired[
                "Literal['arzte_und_apotheker_bank', 'austrian_anadi_bank_ag', 'bank_austria', 'bankhaus_carl_spangler', 'bankhaus_schelhammer_und_schattera_ag', 'bawag_psk_ag', 'bks_bank_ag', 'brull_kallmus_bank_ag', 'btv_vier_lander_bank', 'capital_bank_grawe_gruppe_ag', 'deutsche_bank_ag', 'dolomitenbank', 'easybank_ag', 'erste_bank_und_sparkassen', 'hypo_alpeadriabank_international_ag', 'hypo_bank_burgenland_aktiengesellschaft', 'hypo_noe_lb_fur_niederosterreich_u_wien', 'hypo_oberosterreich_salzburg_steiermark', 'hypo_tirol_bank_ag', 'hypo_vorarlberg_bank_ag', 'marchfelder_bank', 'oberbank_ag', 'raiffeisen_bankengruppe_osterreich', 'schoellerbank_ag', 'sparda_bank_wien', 'volksbank_gruppe', 'volkskreditbank_ag', 'vr_bank_braunau']|None"
            ]

        class ConfirmParamsPaymentMethodDataCustomerBalance(TypedDict):
            pass

        class ConfirmParamsPaymentMethodDataCashapp(TypedDict):
            pass

        class ConfirmParamsPaymentMethodDataBoleto(TypedDict):
            tax_id: str

        class ConfirmParamsPaymentMethodDataBlik(TypedDict):
            pass

        class ConfirmParamsPaymentMethodDataBillingDetails(TypedDict):
            address: NotRequired[
                "Literal['']|SetupIntent.ConfirmParamsPaymentMethodDataBillingDetailsAddress|None"
            ]
            email: NotRequired["Literal['']|str|None"]
            name: NotRequired["Literal['']|str|None"]
            phone: NotRequired["Literal['']|str|None"]

        class ConfirmParamsPaymentMethodDataBillingDetailsAddress(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]

        class ConfirmParamsPaymentMethodDataBancontact(TypedDict):
            pass

        class ConfirmParamsPaymentMethodDataBacsDebit(TypedDict):
            account_number: NotRequired["str|None"]
            sort_code: NotRequired["str|None"]

        class ConfirmParamsPaymentMethodDataAuBecsDebit(TypedDict):
            account_number: str
            bsb_number: str

        class ConfirmParamsPaymentMethodDataAlipay(TypedDict):
            pass

        class ConfirmParamsPaymentMethodDataAfterpayClearpay(TypedDict):
            pass

        class ConfirmParamsPaymentMethodDataAffirm(TypedDict):
            pass

        class ConfirmParamsPaymentMethodDataAcssDebit(TypedDict):
            account_number: str
            institution_number: str
            transit_number: str

        class ConfirmParamsMandateData2(TypedDict):
            customer_acceptance: "SetupIntent.ConfirmParamsMandateDataCustomerAcceptance2"

        class ConfirmParamsMandateDataCustomerAcceptance2(TypedDict):
            online: "SetupIntent.ConfirmParamsMandateDataCustomerAcceptanceOnline2"
            type: Literal["online"]

        class ConfirmParamsMandateDataCustomerAcceptanceOnline2(TypedDict):
            ip_address: NotRequired["str|None"]
            user_agent: NotRequired["str|None"]

        class ConfirmParamsMandateData(TypedDict):
            customer_acceptance: "SetupIntent.ConfirmParamsMandateDataCustomerAcceptance"

        class ConfirmParamsMandateDataCustomerAcceptance(TypedDict):
            accepted_at: NotRequired["int|None"]
            offline: NotRequired[
                "SetupIntent.ConfirmParamsMandateDataCustomerAcceptanceOffline|None"
            ]
            online: NotRequired[
                "SetupIntent.ConfirmParamsMandateDataCustomerAcceptanceOnline|None"
            ]
            type: Literal["offline", "online"]

        class ConfirmParamsMandateDataCustomerAcceptanceOnline(TypedDict):
            ip_address: str
            user_agent: str

        class ConfirmParamsMandateDataCustomerAcceptanceOffline(TypedDict):
            pass

        class CreateParams(RequestOptions):
            attach_to_self: NotRequired["bool|None"]
            automatic_payment_methods: NotRequired[
                "SetupIntent.CreateParamsAutomaticPaymentMethods|None"
            ]
            confirm: NotRequired["bool|None"]
            confirmation_token: NotRequired["str|None"]
            customer: NotRequired["str|None"]
            description: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            flow_directions: NotRequired[
                "List[Literal['inbound', 'outbound']]|None"
            ]
            mandate_data: NotRequired[
                "Literal['']|SetupIntent.CreateParamsMandateData|None"
            ]
            metadata: NotRequired["Dict[str, str]|None"]
            on_behalf_of: NotRequired["str|None"]
            payment_method: NotRequired["str|None"]
            payment_method_configuration: NotRequired["str|None"]
            payment_method_data: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodData|None"
            ]
            payment_method_options: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodOptions|None"
            ]
            payment_method_types: NotRequired["List[str]|None"]
            return_url: NotRequired["str|None"]
            single_use: NotRequired["SetupIntent.CreateParamsSingleUse|None"]
            usage: NotRequired["Literal['off_session', 'on_session']|None"]
            use_stripe_sdk: NotRequired["bool|None"]

        class CreateParamsSingleUse(TypedDict):
            amount: int
            currency: str

        class CreateParamsPaymentMethodOptions(TypedDict):
            acss_debit: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodOptionsAcssDebit|None"
            ]
            card: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodOptionsCard|None"
            ]
            link: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodOptionsLink|None"
            ]
            paypal: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodOptionsPaypal|None"
            ]
            sepa_debit: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodOptionsSepaDebit|None"
            ]
            us_bank_account: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodOptionsUsBankAccount|None"
            ]

        class CreateParamsPaymentMethodOptionsUsBankAccount(TypedDict):
            financial_connections: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodOptionsUsBankAccountFinancialConnections|None"
            ]
            networks: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodOptionsUsBankAccountNetworks|None"
            ]
            verification_method: NotRequired[
                "Literal['automatic', 'instant', 'microdeposits']|None"
            ]

        class CreateParamsPaymentMethodOptionsUsBankAccountNetworks(TypedDict):
            requested: NotRequired[
                "List[Literal['ach', 'us_domestic_wire']]|None"
            ]

        class CreateParamsPaymentMethodOptionsUsBankAccountFinancialConnections(
            TypedDict,
        ):
            manual_entry: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodOptionsUsBankAccountFinancialConnectionsManualEntry|None"
            ]
            permissions: NotRequired[
                "List[Literal['balances', 'ownership', 'payment_method', 'transactions']]|None"
            ]
            prefetch: NotRequired[
                "List[Literal['balances', 'inferred_balances', 'ownership', 'transactions']]|None"
            ]
            return_url: NotRequired["str|None"]

        class CreateParamsPaymentMethodOptionsUsBankAccountFinancialConnectionsManualEntry(
            TypedDict,
        ):
            mode: Literal["automatic", "custom"]

        class CreateParamsPaymentMethodOptionsSepaDebit(TypedDict):
            mandate_options: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodOptionsSepaDebitMandateOptions|None"
            ]

        class CreateParamsPaymentMethodOptionsSepaDebitMandateOptions(
            TypedDict,
        ):
            pass

        class CreateParamsPaymentMethodOptionsPaypal(TypedDict):
            billing_agreement_id: NotRequired["str|None"]
            currency: NotRequired["str|None"]

        class CreateParamsPaymentMethodOptionsLink(TypedDict):
            persistent_token: NotRequired["str|None"]

        class CreateParamsPaymentMethodOptionsCard(TypedDict):
            mandate_options: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodOptionsCardMandateOptions|None"
            ]
            moto: NotRequired["bool|None"]
            network: NotRequired[
                "Literal['amex', 'cartes_bancaires', 'diners', 'discover', 'eftpos_au', 'interac', 'jcb', 'mastercard', 'unionpay', 'unknown', 'visa']|None"
            ]
            request_three_d_secure: NotRequired[
                "Literal['any', 'automatic']|None"
            ]

        class CreateParamsPaymentMethodOptionsCardMandateOptions(TypedDict):
            amount: int
            amount_type: Literal["fixed", "maximum"]
            currency: str
            description: NotRequired["str|None"]
            end_date: NotRequired["int|None"]
            interval: Literal["day", "month", "sporadic", "week", "year"]
            interval_count: NotRequired["int|None"]
            reference: str
            start_date: int
            supported_types: NotRequired["List[Literal['india']]|None"]

        class CreateParamsPaymentMethodOptionsAcssDebit(TypedDict):
            currency: NotRequired["Literal['cad', 'usd']|None"]
            mandate_options: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodOptionsAcssDebitMandateOptions|None"
            ]
            verification_method: NotRequired[
                "Literal['automatic', 'instant', 'microdeposits']|None"
            ]

        class CreateParamsPaymentMethodOptionsAcssDebitMandateOptions(
            TypedDict,
        ):
            custom_mandate_url: NotRequired["Literal['']|str|None"]
            default_for: NotRequired[
                "List[Literal['invoice', 'subscription']]|None"
            ]
            interval_description: NotRequired["str|None"]
            payment_schedule: NotRequired[
                "Literal['combined', 'interval', 'sporadic']|None"
            ]
            transaction_type: NotRequired[
                "Literal['business', 'personal']|None"
            ]

        class CreateParamsPaymentMethodData(TypedDict):
            acss_debit: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataAcssDebit|None"
            ]
            affirm: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataAffirm|None"
            ]
            afterpay_clearpay: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataAfterpayClearpay|None"
            ]
            alipay: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataAlipay|None"
            ]
            au_becs_debit: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataAuBecsDebit|None"
            ]
            bacs_debit: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataBacsDebit|None"
            ]
            bancontact: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataBancontact|None"
            ]
            billing_details: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataBillingDetails|None"
            ]
            blik: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataBlik|None"
            ]
            boleto: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataBoleto|None"
            ]
            cashapp: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataCashapp|None"
            ]
            customer_balance: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataCustomerBalance|None"
            ]
            eps: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataEps|None"
            ]
            fpx: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataFpx|None"
            ]
            giropay: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataGiropay|None"
            ]
            grabpay: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataGrabpay|None"
            ]
            ideal: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataIdeal|None"
            ]
            interac_present: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataInteracPresent|None"
            ]
            klarna: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataKlarna|None"
            ]
            konbini: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataKonbini|None"
            ]
            link: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataLink|None"
            ]
            metadata: NotRequired["Dict[str, str]|None"]
            oxxo: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataOxxo|None"
            ]
            p24: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataP24|None"
            ]
            paynow: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataPaynow|None"
            ]
            paypal: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataPaypal|None"
            ]
            pix: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataPix|None"
            ]
            promptpay: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataPromptpay|None"
            ]
            radar_options: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataRadarOptions|None"
            ]
            sepa_debit: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataSepaDebit|None"
            ]
            sofort: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataSofort|None"
            ]
            type: Literal[
                "acss_debit",
                "affirm",
                "afterpay_clearpay",
                "alipay",
                "au_becs_debit",
                "bacs_debit",
                "bancontact",
                "blik",
                "boleto",
                "cashapp",
                "customer_balance",
                "eps",
                "fpx",
                "giropay",
                "grabpay",
                "ideal",
                "klarna",
                "konbini",
                "link",
                "oxxo",
                "p24",
                "paynow",
                "paypal",
                "pix",
                "promptpay",
                "sepa_debit",
                "sofort",
                "us_bank_account",
                "wechat_pay",
                "zip",
            ]
            us_bank_account: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataUsBankAccount|None"
            ]
            wechat_pay: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataWechatPay|None"
            ]
            zip: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataZip|None"
            ]

        class CreateParamsPaymentMethodDataZip(TypedDict):
            pass

        class CreateParamsPaymentMethodDataWechatPay(TypedDict):
            pass

        class CreateParamsPaymentMethodDataUsBankAccount(TypedDict):
            account_holder_type: NotRequired[
                "Literal['company', 'individual']|None"
            ]
            account_number: NotRequired["str|None"]
            account_type: NotRequired["Literal['checking', 'savings']|None"]
            financial_connections_account: NotRequired["str|None"]
            routing_number: NotRequired["str|None"]

        class CreateParamsPaymentMethodDataSofort(TypedDict):
            country: Literal["AT", "BE", "DE", "ES", "IT", "NL"]

        class CreateParamsPaymentMethodDataSepaDebit(TypedDict):
            iban: str

        class CreateParamsPaymentMethodDataRadarOptions(TypedDict):
            session: NotRequired["str|None"]

        class CreateParamsPaymentMethodDataPromptpay(TypedDict):
            pass

        class CreateParamsPaymentMethodDataPix(TypedDict):
            pass

        class CreateParamsPaymentMethodDataPaypal(TypedDict):
            pass

        class CreateParamsPaymentMethodDataPaynow(TypedDict):
            pass

        class CreateParamsPaymentMethodDataP24(TypedDict):
            bank: NotRequired[
                "Literal['alior_bank', 'bank_millennium', 'bank_nowy_bfg_sa', 'bank_pekao_sa', 'banki_spbdzielcze', 'blik', 'bnp_paribas', 'boz', 'citi_handlowy', 'credit_agricole', 'envelobank', 'etransfer_pocztowy24', 'getin_bank', 'ideabank', 'ing', 'inteligo', 'mbank_mtransfer', 'nest_przelew', 'noble_pay', 'pbac_z_ipko', 'plus_bank', 'santander_przelew24', 'tmobile_usbugi_bankowe', 'toyota_bank', 'volkswagen_bank']|None"
            ]

        class CreateParamsPaymentMethodDataOxxo(TypedDict):
            pass

        class CreateParamsPaymentMethodDataLink(TypedDict):
            pass

        class CreateParamsPaymentMethodDataKonbini(TypedDict):
            pass

        class CreateParamsPaymentMethodDataKlarna(TypedDict):
            dob: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataKlarnaDob|None"
            ]

        class CreateParamsPaymentMethodDataKlarnaDob(TypedDict):
            day: int
            month: int
            year: int

        class CreateParamsPaymentMethodDataInteracPresent(TypedDict):
            pass

        class CreateParamsPaymentMethodDataIdeal(TypedDict):
            bank: NotRequired[
                "Literal['abn_amro', 'asn_bank', 'bunq', 'handelsbanken', 'ing', 'knab', 'moneyou', 'n26', 'rabobank', 'regiobank', 'revolut', 'sns_bank', 'triodos_bank', 'van_lanschot', 'yoursafe']|None"
            ]

        class CreateParamsPaymentMethodDataGrabpay(TypedDict):
            pass

        class CreateParamsPaymentMethodDataGiropay(TypedDict):
            pass

        class CreateParamsPaymentMethodDataFpx(TypedDict):
            account_holder_type: NotRequired[
                "Literal['company', 'individual']|None"
            ]
            bank: Literal[
                "affin_bank",
                "agrobank",
                "alliance_bank",
                "ambank",
                "bank_islam",
                "bank_muamalat",
                "bank_of_china",
                "bank_rakyat",
                "bsn",
                "cimb",
                "deutsche_bank",
                "hong_leong_bank",
                "hsbc",
                "kfh",
                "maybank2e",
                "maybank2u",
                "ocbc",
                "pb_enterprise",
                "public_bank",
                "rhb",
                "standard_chartered",
                "uob",
            ]

        class CreateParamsPaymentMethodDataEps(TypedDict):
            bank: NotRequired[
                "Literal['arzte_und_apotheker_bank', 'austrian_anadi_bank_ag', 'bank_austria', 'bankhaus_carl_spangler', 'bankhaus_schelhammer_und_schattera_ag', 'bawag_psk_ag', 'bks_bank_ag', 'brull_kallmus_bank_ag', 'btv_vier_lander_bank', 'capital_bank_grawe_gruppe_ag', 'deutsche_bank_ag', 'dolomitenbank', 'easybank_ag', 'erste_bank_und_sparkassen', 'hypo_alpeadriabank_international_ag', 'hypo_bank_burgenland_aktiengesellschaft', 'hypo_noe_lb_fur_niederosterreich_u_wien', 'hypo_oberosterreich_salzburg_steiermark', 'hypo_tirol_bank_ag', 'hypo_vorarlberg_bank_ag', 'marchfelder_bank', 'oberbank_ag', 'raiffeisen_bankengruppe_osterreich', 'schoellerbank_ag', 'sparda_bank_wien', 'volksbank_gruppe', 'volkskreditbank_ag', 'vr_bank_braunau']|None"
            ]

        class CreateParamsPaymentMethodDataCustomerBalance(TypedDict):
            pass

        class CreateParamsPaymentMethodDataCashapp(TypedDict):
            pass

        class CreateParamsPaymentMethodDataBoleto(TypedDict):
            tax_id: str

        class CreateParamsPaymentMethodDataBlik(TypedDict):
            pass

        class CreateParamsPaymentMethodDataBillingDetails(TypedDict):
            address: NotRequired[
                "Literal['']|SetupIntent.CreateParamsPaymentMethodDataBillingDetailsAddress|None"
            ]
            email: NotRequired["Literal['']|str|None"]
            name: NotRequired["Literal['']|str|None"]
            phone: NotRequired["Literal['']|str|None"]

        class CreateParamsPaymentMethodDataBillingDetailsAddress(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]

        class CreateParamsPaymentMethodDataBancontact(TypedDict):
            pass

        class CreateParamsPaymentMethodDataBacsDebit(TypedDict):
            account_number: NotRequired["str|None"]
            sort_code: NotRequired["str|None"]

        class CreateParamsPaymentMethodDataAuBecsDebit(TypedDict):
            account_number: str
            bsb_number: str

        class CreateParamsPaymentMethodDataAlipay(TypedDict):
            pass

        class CreateParamsPaymentMethodDataAfterpayClearpay(TypedDict):
            pass

        class CreateParamsPaymentMethodDataAffirm(TypedDict):
            pass

        class CreateParamsPaymentMethodDataAcssDebit(TypedDict):
            account_number: str
            institution_number: str
            transit_number: str

        class CreateParamsMandateData(TypedDict):
            customer_acceptance: "SetupIntent.CreateParamsMandateDataCustomerAcceptance"

        class CreateParamsMandateDataCustomerAcceptance(TypedDict):
            accepted_at: NotRequired["int|None"]
            offline: NotRequired[
                "SetupIntent.CreateParamsMandateDataCustomerAcceptanceOffline|None"
            ]
            online: NotRequired[
                "SetupIntent.CreateParamsMandateDataCustomerAcceptanceOnline|None"
            ]
            type: Literal["offline", "online"]

        class CreateParamsMandateDataCustomerAcceptanceOnline(TypedDict):
            ip_address: str
            user_agent: str

        class CreateParamsMandateDataCustomerAcceptanceOffline(TypedDict):
            pass

        class CreateParamsAutomaticPaymentMethods(TypedDict):
            allow_redirects: NotRequired["Literal['always', 'never']|None"]
            enabled: bool

        class ListParams(RequestOptions):
            attach_to_self: NotRequired["bool|None"]
            created: NotRequired["SetupIntent.ListParamsCreated|int|None"]
            customer: NotRequired["str|None"]
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            payment_method: NotRequired["str|None"]
            starting_after: NotRequired["str|None"]

        class ListParamsCreated(TypedDict):
            gt: NotRequired["int|None"]
            gte: NotRequired["int|None"]
            lt: NotRequired["int|None"]
            lte: NotRequired["int|None"]

        class ModifyParams(RequestOptions):
            attach_to_self: NotRequired["bool|None"]
            customer: NotRequired["str|None"]
            description: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            flow_directions: NotRequired[
                "List[Literal['inbound', 'outbound']]|None"
            ]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            payment_method: NotRequired["str|None"]
            payment_method_configuration: NotRequired["str|None"]
            payment_method_data: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodData|None"
            ]
            payment_method_options: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodOptions|None"
            ]
            payment_method_types: NotRequired["List[str]|None"]

        class ModifyParamsPaymentMethodOptions(TypedDict):
            acss_debit: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodOptionsAcssDebit|None"
            ]
            card: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodOptionsCard|None"
            ]
            link: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodOptionsLink|None"
            ]
            paypal: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodOptionsPaypal|None"
            ]
            sepa_debit: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodOptionsSepaDebit|None"
            ]
            us_bank_account: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodOptionsUsBankAccount|None"
            ]

        class ModifyParamsPaymentMethodOptionsUsBankAccount(TypedDict):
            financial_connections: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodOptionsUsBankAccountFinancialConnections|None"
            ]
            networks: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodOptionsUsBankAccountNetworks|None"
            ]
            verification_method: NotRequired[
                "Literal['automatic', 'instant', 'microdeposits']|None"
            ]

        class ModifyParamsPaymentMethodOptionsUsBankAccountNetworks(TypedDict):
            requested: NotRequired[
                "List[Literal['ach', 'us_domestic_wire']]|None"
            ]

        class ModifyParamsPaymentMethodOptionsUsBankAccountFinancialConnections(
            TypedDict,
        ):
            manual_entry: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodOptionsUsBankAccountFinancialConnectionsManualEntry|None"
            ]
            permissions: NotRequired[
                "List[Literal['balances', 'ownership', 'payment_method', 'transactions']]|None"
            ]
            prefetch: NotRequired[
                "List[Literal['balances', 'inferred_balances', 'ownership', 'transactions']]|None"
            ]
            return_url: NotRequired["str|None"]

        class ModifyParamsPaymentMethodOptionsUsBankAccountFinancialConnectionsManualEntry(
            TypedDict,
        ):
            mode: Literal["automatic", "custom"]

        class ModifyParamsPaymentMethodOptionsSepaDebit(TypedDict):
            mandate_options: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodOptionsSepaDebitMandateOptions|None"
            ]

        class ModifyParamsPaymentMethodOptionsSepaDebitMandateOptions(
            TypedDict,
        ):
            pass

        class ModifyParamsPaymentMethodOptionsPaypal(TypedDict):
            billing_agreement_id: NotRequired["str|None"]
            currency: NotRequired["str|None"]

        class ModifyParamsPaymentMethodOptionsLink(TypedDict):
            persistent_token: NotRequired["str|None"]

        class ModifyParamsPaymentMethodOptionsCard(TypedDict):
            mandate_options: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodOptionsCardMandateOptions|None"
            ]
            moto: NotRequired["bool|None"]
            network: NotRequired[
                "Literal['amex', 'cartes_bancaires', 'diners', 'discover', 'eftpos_au', 'interac', 'jcb', 'mastercard', 'unionpay', 'unknown', 'visa']|None"
            ]
            request_three_d_secure: NotRequired[
                "Literal['any', 'automatic']|None"
            ]

        class ModifyParamsPaymentMethodOptionsCardMandateOptions(TypedDict):
            amount: int
            amount_type: Literal["fixed", "maximum"]
            currency: str
            description: NotRequired["str|None"]
            end_date: NotRequired["int|None"]
            interval: Literal["day", "month", "sporadic", "week", "year"]
            interval_count: NotRequired["int|None"]
            reference: str
            start_date: int
            supported_types: NotRequired["List[Literal['india']]|None"]

        class ModifyParamsPaymentMethodOptionsAcssDebit(TypedDict):
            currency: NotRequired["Literal['cad', 'usd']|None"]
            mandate_options: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodOptionsAcssDebitMandateOptions|None"
            ]
            verification_method: NotRequired[
                "Literal['automatic', 'instant', 'microdeposits']|None"
            ]

        class ModifyParamsPaymentMethodOptionsAcssDebitMandateOptions(
            TypedDict,
        ):
            custom_mandate_url: NotRequired["Literal['']|str|None"]
            default_for: NotRequired[
                "List[Literal['invoice', 'subscription']]|None"
            ]
            interval_description: NotRequired["str|None"]
            payment_schedule: NotRequired[
                "Literal['combined', 'interval', 'sporadic']|None"
            ]
            transaction_type: NotRequired[
                "Literal['business', 'personal']|None"
            ]

        class ModifyParamsPaymentMethodData(TypedDict):
            acss_debit: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataAcssDebit|None"
            ]
            affirm: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataAffirm|None"
            ]
            afterpay_clearpay: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataAfterpayClearpay|None"
            ]
            alipay: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataAlipay|None"
            ]
            au_becs_debit: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataAuBecsDebit|None"
            ]
            bacs_debit: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataBacsDebit|None"
            ]
            bancontact: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataBancontact|None"
            ]
            billing_details: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataBillingDetails|None"
            ]
            blik: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataBlik|None"
            ]
            boleto: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataBoleto|None"
            ]
            cashapp: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataCashapp|None"
            ]
            customer_balance: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataCustomerBalance|None"
            ]
            eps: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataEps|None"
            ]
            fpx: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataFpx|None"
            ]
            giropay: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataGiropay|None"
            ]
            grabpay: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataGrabpay|None"
            ]
            ideal: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataIdeal|None"
            ]
            interac_present: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataInteracPresent|None"
            ]
            klarna: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataKlarna|None"
            ]
            konbini: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataKonbini|None"
            ]
            link: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataLink|None"
            ]
            metadata: NotRequired["Dict[str, str]|None"]
            oxxo: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataOxxo|None"
            ]
            p24: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataP24|None"
            ]
            paynow: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataPaynow|None"
            ]
            paypal: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataPaypal|None"
            ]
            pix: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataPix|None"
            ]
            promptpay: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataPromptpay|None"
            ]
            radar_options: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataRadarOptions|None"
            ]
            sepa_debit: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataSepaDebit|None"
            ]
            sofort: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataSofort|None"
            ]
            type: Literal[
                "acss_debit",
                "affirm",
                "afterpay_clearpay",
                "alipay",
                "au_becs_debit",
                "bacs_debit",
                "bancontact",
                "blik",
                "boleto",
                "cashapp",
                "customer_balance",
                "eps",
                "fpx",
                "giropay",
                "grabpay",
                "ideal",
                "klarna",
                "konbini",
                "link",
                "oxxo",
                "p24",
                "paynow",
                "paypal",
                "pix",
                "promptpay",
                "sepa_debit",
                "sofort",
                "us_bank_account",
                "wechat_pay",
                "zip",
            ]
            us_bank_account: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataUsBankAccount|None"
            ]
            wechat_pay: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataWechatPay|None"
            ]
            zip: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataZip|None"
            ]

        class ModifyParamsPaymentMethodDataZip(TypedDict):
            pass

        class ModifyParamsPaymentMethodDataWechatPay(TypedDict):
            pass

        class ModifyParamsPaymentMethodDataUsBankAccount(TypedDict):
            account_holder_type: NotRequired[
                "Literal['company', 'individual']|None"
            ]
            account_number: NotRequired["str|None"]
            account_type: NotRequired["Literal['checking', 'savings']|None"]
            financial_connections_account: NotRequired["str|None"]
            routing_number: NotRequired["str|None"]

        class ModifyParamsPaymentMethodDataSofort(TypedDict):
            country: Literal["AT", "BE", "DE", "ES", "IT", "NL"]

        class ModifyParamsPaymentMethodDataSepaDebit(TypedDict):
            iban: str

        class ModifyParamsPaymentMethodDataRadarOptions(TypedDict):
            session: NotRequired["str|None"]

        class ModifyParamsPaymentMethodDataPromptpay(TypedDict):
            pass

        class ModifyParamsPaymentMethodDataPix(TypedDict):
            pass

        class ModifyParamsPaymentMethodDataPaypal(TypedDict):
            pass

        class ModifyParamsPaymentMethodDataPaynow(TypedDict):
            pass

        class ModifyParamsPaymentMethodDataP24(TypedDict):
            bank: NotRequired[
                "Literal['alior_bank', 'bank_millennium', 'bank_nowy_bfg_sa', 'bank_pekao_sa', 'banki_spbdzielcze', 'blik', 'bnp_paribas', 'boz', 'citi_handlowy', 'credit_agricole', 'envelobank', 'etransfer_pocztowy24', 'getin_bank', 'ideabank', 'ing', 'inteligo', 'mbank_mtransfer', 'nest_przelew', 'noble_pay', 'pbac_z_ipko', 'plus_bank', 'santander_przelew24', 'tmobile_usbugi_bankowe', 'toyota_bank', 'volkswagen_bank']|None"
            ]

        class ModifyParamsPaymentMethodDataOxxo(TypedDict):
            pass

        class ModifyParamsPaymentMethodDataLink(TypedDict):
            pass

        class ModifyParamsPaymentMethodDataKonbini(TypedDict):
            pass

        class ModifyParamsPaymentMethodDataKlarna(TypedDict):
            dob: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataKlarnaDob|None"
            ]

        class ModifyParamsPaymentMethodDataKlarnaDob(TypedDict):
            day: int
            month: int
            year: int

        class ModifyParamsPaymentMethodDataInteracPresent(TypedDict):
            pass

        class ModifyParamsPaymentMethodDataIdeal(TypedDict):
            bank: NotRequired[
                "Literal['abn_amro', 'asn_bank', 'bunq', 'handelsbanken', 'ing', 'knab', 'moneyou', 'n26', 'rabobank', 'regiobank', 'revolut', 'sns_bank', 'triodos_bank', 'van_lanschot', 'yoursafe']|None"
            ]

        class ModifyParamsPaymentMethodDataGrabpay(TypedDict):
            pass

        class ModifyParamsPaymentMethodDataGiropay(TypedDict):
            pass

        class ModifyParamsPaymentMethodDataFpx(TypedDict):
            account_holder_type: NotRequired[
                "Literal['company', 'individual']|None"
            ]
            bank: Literal[
                "affin_bank",
                "agrobank",
                "alliance_bank",
                "ambank",
                "bank_islam",
                "bank_muamalat",
                "bank_of_china",
                "bank_rakyat",
                "bsn",
                "cimb",
                "deutsche_bank",
                "hong_leong_bank",
                "hsbc",
                "kfh",
                "maybank2e",
                "maybank2u",
                "ocbc",
                "pb_enterprise",
                "public_bank",
                "rhb",
                "standard_chartered",
                "uob",
            ]

        class ModifyParamsPaymentMethodDataEps(TypedDict):
            bank: NotRequired[
                "Literal['arzte_und_apotheker_bank', 'austrian_anadi_bank_ag', 'bank_austria', 'bankhaus_carl_spangler', 'bankhaus_schelhammer_und_schattera_ag', 'bawag_psk_ag', 'bks_bank_ag', 'brull_kallmus_bank_ag', 'btv_vier_lander_bank', 'capital_bank_grawe_gruppe_ag', 'deutsche_bank_ag', 'dolomitenbank', 'easybank_ag', 'erste_bank_und_sparkassen', 'hypo_alpeadriabank_international_ag', 'hypo_bank_burgenland_aktiengesellschaft', 'hypo_noe_lb_fur_niederosterreich_u_wien', 'hypo_oberosterreich_salzburg_steiermark', 'hypo_tirol_bank_ag', 'hypo_vorarlberg_bank_ag', 'marchfelder_bank', 'oberbank_ag', 'raiffeisen_bankengruppe_osterreich', 'schoellerbank_ag', 'sparda_bank_wien', 'volksbank_gruppe', 'volkskreditbank_ag', 'vr_bank_braunau']|None"
            ]

        class ModifyParamsPaymentMethodDataCustomerBalance(TypedDict):
            pass

        class ModifyParamsPaymentMethodDataCashapp(TypedDict):
            pass

        class ModifyParamsPaymentMethodDataBoleto(TypedDict):
            tax_id: str

        class ModifyParamsPaymentMethodDataBlik(TypedDict):
            pass

        class ModifyParamsPaymentMethodDataBillingDetails(TypedDict):
            address: NotRequired[
                "Literal['']|SetupIntent.ModifyParamsPaymentMethodDataBillingDetailsAddress|None"
            ]
            email: NotRequired["Literal['']|str|None"]
            name: NotRequired["Literal['']|str|None"]
            phone: NotRequired["Literal['']|str|None"]

        class ModifyParamsPaymentMethodDataBillingDetailsAddress(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]

        class ModifyParamsPaymentMethodDataBancontact(TypedDict):
            pass

        class ModifyParamsPaymentMethodDataBacsDebit(TypedDict):
            account_number: NotRequired["str|None"]
            sort_code: NotRequired["str|None"]

        class ModifyParamsPaymentMethodDataAuBecsDebit(TypedDict):
            account_number: str
            bsb_number: str

        class ModifyParamsPaymentMethodDataAlipay(TypedDict):
            pass

        class ModifyParamsPaymentMethodDataAfterpayClearpay(TypedDict):
            pass

        class ModifyParamsPaymentMethodDataAffirm(TypedDict):
            pass

        class ModifyParamsPaymentMethodDataAcssDebit(TypedDict):
            account_number: str
            institution_number: str
            transit_number: str

        class RetrieveParams(RequestOptions):
            client_secret: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]

        class VerifyMicrodepositsParams(RequestOptions):
            amounts: NotRequired["List[int]|None"]
            descriptor_code: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]

    application: Optional[ExpandableField["Application"]]
    attach_to_self: Optional[bool]
    automatic_payment_methods: Optional[AutomaticPaymentMethods]
    cancellation_reason: Optional[
        Literal["abandoned", "duplicate", "requested_by_customer"]
    ]
    client_secret: Optional[str]
    created: int
    customer: Optional[ExpandableField["Customer"]]
    description: Optional[str]
    flow_directions: Optional[List[Literal["inbound", "outbound"]]]
    id: str
    last_setup_error: Optional[LastSetupError]
    latest_attempt: Optional[ExpandableField["SetupAttempt"]]
    livemode: bool
    mandate: Optional[ExpandableField["Mandate"]]
    metadata: Optional[Dict[str, str]]
    next_action: Optional[NextAction]
    object: Literal["setup_intent"]
    on_behalf_of: Optional[ExpandableField["Account"]]
    payment_method: Optional[ExpandableField["PaymentMethod"]]
    payment_method_configuration_details: Optional[
        PaymentMethodConfigurationDetails
    ]
    payment_method_options: Optional[PaymentMethodOptions]
    payment_method_types: List[str]
    single_use_mandate: Optional[ExpandableField["Mandate"]]
    status: Literal[
        "canceled",
        "processing",
        "requires_action",
        "requires_confirmation",
        "requires_payment_method",
        "succeeded",
    ]
    usage: str

    @classmethod
    def _cls_cancel(
        cls,
        intent: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["SetupIntent.CancelParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/setup_intents/{intent}/cancel".format(
                intent=util.sanitize_id(intent)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_cancel")
    def cancel(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["SetupIntent.CancelParams"]
    ):
        return self._request(
            "post",
            "/v1/setup_intents/{intent}/cancel".format(
                intent=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_confirm(
        cls,
        intent: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["SetupIntent.ConfirmParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/setup_intents/{intent}/confirm".format(
                intent=util.sanitize_id(intent)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_confirm")
    def confirm(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["SetupIntent.ConfirmParams"]
    ):
        return self._request(
            "post",
            "/v1/setup_intents/{intent}/confirm".format(
                intent=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["SetupIntent.CreateParams"]
    ) -> "SetupIntent":
        return cast(
            "SetupIntent",
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
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["SetupIntent.ListParams"]
    ) -> ListObject["SetupIntent"]:
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
    def modify(
        cls, id, **params: Unpack["SetupIntent.ModifyParams"]
    ) -> "SetupIntent":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "SetupIntent",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["SetupIntent.RetrieveParams"]
    ) -> "SetupIntent":
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    def _cls_verify_microdeposits(
        cls,
        intent: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["SetupIntent.VerifyMicrodepositsParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/setup_intents/{intent}/verify_microdeposits".format(
                intent=util.sanitize_id(intent)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_verify_microdeposits")
    def verify_microdeposits(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["SetupIntent.VerifyMicrodepositsParams"]
    ):
        return self._request(
            "post",
            "/v1/setup_intents/{intent}/verify_microdeposits".format(
                intent=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    _inner_class_types = {
        "automatic_payment_methods": AutomaticPaymentMethods,
        "last_setup_error": LastSetupError,
        "next_action": NextAction,
        "payment_method_configuration_details": PaymentMethodConfigurationDetails,
        "payment_method_options": PaymentMethodOptions,
    }
