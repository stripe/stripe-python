# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import util
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    SearchableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.api_resources.search_result_object import SearchResultObject
from stripe.stripe_object import StripeObject
from typing import Any, Dict, List, Optional, cast
from typing_extensions import Literal
from urllib.parse import quote_plus

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.account import Account
    from stripe.api_resources.application import Application
    from stripe.api_resources.charge import Charge
    from stripe.api_resources.customer import Customer
    from stripe.api_resources.invoice import Invoice
    from stripe.api_resources.payment_method import PaymentMethod
    from stripe.api_resources.review import Review
    from stripe.api_resources.setup_intent import SetupIntent


class PaymentIntent(
    CreateableAPIResource["PaymentIntent"],
    ListableAPIResource["PaymentIntent"],
    SearchableAPIResource["PaymentIntent"],
    UpdateableAPIResource["PaymentIntent"],
):
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

    OBJECT_NAME = "payment_intent"

    class AmountDetails(StripeObject):
        class Tip(StripeObject):
            amount: Optional[int]

        tip: Optional[Tip]
        _inner_class_types = {"tip": Tip}

    class AutomaticPaymentMethods(StripeObject):
        allow_redirects: Optional[Literal["always", "never"]]
        enabled: bool

    class LastPaymentError(StripeObject):
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

    class NextAction(StripeObject):
        class AlipayHandleRedirect(StripeObject):
            native_data: Optional[str]
            native_url: Optional[str]
            return_url: Optional[str]
            url: Optional[str]

        class BoletoDisplayDetails(StripeObject):
            expires_at: Optional[int]
            hosted_voucher_url: Optional[str]
            number: Optional[str]
            pdf: Optional[str]

        class CardAwaitNotification(StripeObject):
            charge_attempt_at: Optional[int]
            customer_approval_required: Optional[bool]

        class CashappHandleRedirectOrDisplayQrCode(StripeObject):
            class QrCode(StripeObject):
                expires_at: int
                image_url_png: str
                image_url_svg: str

            hosted_instructions_url: str
            mobile_auth_url: str
            qr_code: QrCode
            _inner_class_types = {"qr_code": QrCode}

        class DisplayBankTransferInstructions(StripeObject):
            class FinancialAddress(StripeObject):
                class Iban(StripeObject):
                    account_holder_name: str
                    bic: str
                    country: str
                    iban: str

                class SortCode(StripeObject):
                    account_holder_name: str
                    account_number: str
                    sort_code: str

                class Spei(StripeObject):
                    bank_code: str
                    bank_name: str
                    clabe: str

                class Zengin(StripeObject):
                    account_holder_name: Optional[str]
                    account_number: Optional[str]
                    account_type: Optional[str]
                    bank_code: Optional[str]
                    bank_name: Optional[str]
                    branch_code: Optional[str]
                    branch_name: Optional[str]

                iban: Optional[Iban]
                sort_code: Optional[SortCode]
                spei: Optional[Spei]
                supported_networks: Optional[
                    List[Literal["bacs", "fps", "sepa", "spei", "zengin"]]
                ]
                type: Literal["iban", "sort_code", "spei", "zengin"]
                zengin: Optional[Zengin]
                _inner_class_types = {
                    "iban": Iban,
                    "sort_code": SortCode,
                    "spei": Spei,
                    "zengin": Zengin,
                }

            amount_remaining: Optional[int]
            currency: Optional[str]
            financial_addresses: Optional[List[FinancialAddress]]
            hosted_instructions_url: Optional[str]
            reference: Optional[str]
            type: Literal[
                "eu_bank_transfer",
                "gb_bank_transfer",
                "jp_bank_transfer",
                "mx_bank_transfer",
                "us_bank_transfer",
            ]
            _inner_class_types = {"financial_addresses": FinancialAddress}

        class KonbiniDisplayDetails(StripeObject):
            class Stores(StripeObject):
                class Familymart(StripeObject):
                    confirmation_number: Optional[str]
                    payment_code: str

                class Lawson(StripeObject):
                    confirmation_number: Optional[str]
                    payment_code: str

                class Ministop(StripeObject):
                    confirmation_number: Optional[str]
                    payment_code: str

                class Seicomart(StripeObject):
                    confirmation_number: Optional[str]
                    payment_code: str

                familymart: Optional[Familymart]
                lawson: Optional[Lawson]
                ministop: Optional[Ministop]
                seicomart: Optional[Seicomart]
                _inner_class_types = {
                    "familymart": Familymart,
                    "lawson": Lawson,
                    "ministop": Ministop,
                    "seicomart": Seicomart,
                }

            expires_at: int
            hosted_voucher_url: Optional[str]
            stores: Stores
            _inner_class_types = {"stores": Stores}

        class OxxoDisplayDetails(StripeObject):
            expires_after: Optional[int]
            hosted_voucher_url: Optional[str]
            number: Optional[str]

        class PaynowDisplayQrCode(StripeObject):
            data: str
            hosted_instructions_url: Optional[str]
            image_url_png: str
            image_url_svg: str

        class PixDisplayQrCode(StripeObject):
            data: Optional[str]
            expires_at: Optional[int]
            hosted_instructions_url: Optional[str]
            image_url_png: Optional[str]
            image_url_svg: Optional[str]

        class PromptpayDisplayQrCode(StripeObject):
            data: str
            hosted_instructions_url: str
            image_url_png: str
            image_url_svg: str

        class RedirectToUrl(StripeObject):
            return_url: Optional[str]
            url: Optional[str]

        class VerifyWithMicrodeposits(StripeObject):
            arrival_date: int
            hosted_verification_url: str
            microdeposit_type: Optional[Literal["amounts", "descriptor_code"]]

        class WechatPayDisplayQrCode(StripeObject):
            data: str
            hosted_instructions_url: str
            image_data_url: str
            image_url_png: str
            image_url_svg: str

        class WechatPayRedirectToAndroidApp(StripeObject):
            app_id: str
            nonce_str: str
            package: str
            partner_id: str
            prepay_id: str
            sign: str
            timestamp: str

        class WechatPayRedirectToIosApp(StripeObject):
            native_url: str

        alipay_handle_redirect: Optional[AlipayHandleRedirect]
        boleto_display_details: Optional[BoletoDisplayDetails]
        card_await_notification: Optional[CardAwaitNotification]
        cashapp_handle_redirect_or_display_qr_code: Optional[
            CashappHandleRedirectOrDisplayQrCode
        ]
        display_bank_transfer_instructions: Optional[
            DisplayBankTransferInstructions
        ]
        konbini_display_details: Optional[KonbiniDisplayDetails]
        oxxo_display_details: Optional[OxxoDisplayDetails]
        paynow_display_qr_code: Optional[PaynowDisplayQrCode]
        pix_display_qr_code: Optional[PixDisplayQrCode]
        promptpay_display_qr_code: Optional[PromptpayDisplayQrCode]
        redirect_to_url: Optional[RedirectToUrl]
        type: str
        use_stripe_sdk: Optional[Dict[str, Any]]
        verify_with_microdeposits: Optional[VerifyWithMicrodeposits]
        wechat_pay_display_qr_code: Optional[WechatPayDisplayQrCode]
        wechat_pay_redirect_to_android_app: Optional[
            WechatPayRedirectToAndroidApp
        ]
        wechat_pay_redirect_to_ios_app: Optional[WechatPayRedirectToIosApp]
        _inner_class_types = {
            "alipay_handle_redirect": AlipayHandleRedirect,
            "boleto_display_details": BoletoDisplayDetails,
            "card_await_notification": CardAwaitNotification,
            "cashapp_handle_redirect_or_display_qr_code": CashappHandleRedirectOrDisplayQrCode,
            "display_bank_transfer_instructions": DisplayBankTransferInstructions,
            "konbini_display_details": KonbiniDisplayDetails,
            "oxxo_display_details": OxxoDisplayDetails,
            "paynow_display_qr_code": PaynowDisplayQrCode,
            "pix_display_qr_code": PixDisplayQrCode,
            "promptpay_display_qr_code": PromptpayDisplayQrCode,
            "redirect_to_url": RedirectToUrl,
            "verify_with_microdeposits": VerifyWithMicrodeposits,
            "wechat_pay_display_qr_code": WechatPayDisplayQrCode,
            "wechat_pay_redirect_to_android_app": WechatPayRedirectToAndroidApp,
            "wechat_pay_redirect_to_ios_app": WechatPayRedirectToIosApp,
        }

    class PaymentDetails(StripeObject):
        class CarRental(StripeObject):
            class PickupAddress(StripeObject):
                city: Optional[str]
                country: Optional[str]
                line1: Optional[str]
                line2: Optional[str]
                postal_code: Optional[str]
                state: Optional[str]

            class ReturnAddress(StripeObject):
                city: Optional[str]
                country: Optional[str]
                line1: Optional[str]
                line2: Optional[str]
                postal_code: Optional[str]
                state: Optional[str]

            booking_number: str
            car_class_code: Optional[str]
            car_make: Optional[str]
            car_model: Optional[str]
            company: Optional[str]
            customer_service_phone_number: Optional[str]
            days_rented: int
            extra_charges: Optional[
                List[
                    Literal[
                        "extra_mileage",
                        "gas",
                        "late_return",
                        "one_way_service",
                        "parking_violation",
                    ]
                ]
            ]
            no_show: Optional[bool]
            pickup_address: Optional[PickupAddress]
            pickup_at: int
            rate_amount: Optional[int]
            rate_interval: Optional[Literal["day", "month", "week"]]
            renter_name: Optional[str]
            return_address: Optional[ReturnAddress]
            return_at: int
            tax_exempt: Optional[bool]
            _inner_class_types = {
                "pickup_address": PickupAddress,
                "return_address": ReturnAddress,
            }

        car_rental: Optional[CarRental]
        _inner_class_types = {"car_rental": CarRental}

    class PaymentMethodConfigurationDetails(StripeObject):
        id: str
        parent: Optional[str]

    class PaymentMethodOptions(StripeObject):
        class AcssDebit(StripeObject):
            class MandateOptions(StripeObject):
                custom_mandate_url: Optional[str]
                interval_description: Optional[str]
                payment_schedule: Optional[
                    Literal["combined", "interval", "sporadic"]
                ]
                transaction_type: Optional[Literal["business", "personal"]]

            mandate_options: Optional[MandateOptions]
            setup_future_usage: Optional[
                Literal["none", "off_session", "on_session"]
            ]
            verification_method: Optional[
                Literal["automatic", "instant", "microdeposits"]
            ]
            _inner_class_types = {"mandate_options": MandateOptions}

        class Affirm(StripeObject):
            capture_method: Optional[Literal["manual"]]
            preferred_locale: Optional[str]
            setup_future_usage: Optional[Literal["none"]]

        class AfterpayClearpay(StripeObject):
            capture_method: Optional[Literal["manual"]]
            reference: Optional[str]
            setup_future_usage: Optional[Literal["none"]]

        class Alipay(StripeObject):
            setup_future_usage: Optional[Literal["none", "off_session"]]

        class AuBecsDebit(StripeObject):
            setup_future_usage: Optional[
                Literal["none", "off_session", "on_session"]
            ]

        class BacsDebit(StripeObject):
            setup_future_usage: Optional[
                Literal["none", "off_session", "on_session"]
            ]

        class Bancontact(StripeObject):
            preferred_language: Literal["de", "en", "fr", "nl"]
            setup_future_usage: Optional[Literal["none", "off_session"]]

        class Blik(StripeObject):
            pass

        class Boleto(StripeObject):
            expires_after_days: int
            setup_future_usage: Optional[
                Literal["none", "off_session", "on_session"]
            ]

        class Card(StripeObject):
            class Installments(StripeObject):
                class AvailablePlan(StripeObject):
                    count: Optional[int]
                    interval: Optional[Literal["month"]]
                    type: Literal["fixed_count"]

                class Plan(StripeObject):
                    count: Optional[int]
                    interval: Optional[Literal["month"]]
                    type: Literal["fixed_count"]

                available_plans: Optional[List[AvailablePlan]]
                enabled: bool
                plan: Optional[Plan]
                _inner_class_types = {
                    "available_plans": AvailablePlan,
                    "plan": Plan,
                }

            class MandateOptions(StripeObject):
                amount: int
                amount_type: Literal["fixed", "maximum"]
                description: Optional[str]
                end_date: Optional[int]
                interval: Literal["day", "month", "sporadic", "week", "year"]
                interval_count: Optional[int]
                reference: str
                start_date: int
                supported_types: Optional[List[Literal["india"]]]

            class StatementDetails(StripeObject):
                class Address(StripeObject):
                    city: Optional[str]
                    country: Optional[str]
                    line1: Optional[str]
                    line2: Optional[str]
                    postal_code: Optional[str]
                    state: Optional[str]

                address: Optional[Address]
                phone: Optional[str]
                _inner_class_types = {"address": Address}

            capture_method: Optional[Literal["manual"]]
            installments: Optional[Installments]
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
            request_extended_authorization: Optional[
                Literal["if_available", "never"]
            ]
            request_incremental_authorization: Optional[
                Literal["if_available", "never"]
            ]
            request_multicapture: Optional[Literal["if_available", "never"]]
            request_overcapture: Optional[Literal["if_available", "never"]]
            request_three_d_secure: Optional[
                Literal["any", "automatic", "challenge_only"]
            ]
            setup_future_usage: Optional[
                Literal["none", "off_session", "on_session"]
            ]
            statement_descriptor_suffix_kana: Optional[str]
            statement_descriptor_suffix_kanji: Optional[str]
            statement_details: Optional[StatementDetails]
            _inner_class_types = {
                "installments": Installments,
                "mandate_options": MandateOptions,
                "statement_details": StatementDetails,
            }

        class CardPresent(StripeObject):
            request_extended_authorization: Optional[bool]
            request_incremental_authorization_support: Optional[bool]

        class Cashapp(StripeObject):
            capture_method: Optional[Literal["manual"]]
            setup_future_usage: Optional[
                Literal["none", "off_session", "on_session"]
            ]

        class CustomerBalance(StripeObject):
            class BankTransfer(StripeObject):
                class EuBankTransfer(StripeObject):
                    country: Literal["BE", "DE", "ES", "FR", "IE", "NL"]

                eu_bank_transfer: Optional[EuBankTransfer]
                requested_address_types: Optional[
                    List[
                        Literal[
                            "aba",
                            "iban",
                            "sepa",
                            "sort_code",
                            "spei",
                            "swift",
                            "zengin",
                        ]
                    ]
                ]
                type: Optional[
                    Literal[
                        "eu_bank_transfer",
                        "gb_bank_transfer",
                        "jp_bank_transfer",
                        "mx_bank_transfer",
                        "us_bank_transfer",
                    ]
                ]
                _inner_class_types = {"eu_bank_transfer": EuBankTransfer}

            bank_transfer: Optional[BankTransfer]
            funding_type: Optional[Literal["bank_transfer"]]
            setup_future_usage: Optional[Literal["none"]]
            _inner_class_types = {"bank_transfer": BankTransfer}

        class Eps(StripeObject):
            setup_future_usage: Optional[Literal["none"]]

        class Fpx(StripeObject):
            setup_future_usage: Optional[Literal["none"]]

        class Giropay(StripeObject):
            setup_future_usage: Optional[Literal["none"]]

        class Grabpay(StripeObject):
            setup_future_usage: Optional[Literal["none"]]

        class Ideal(StripeObject):
            setup_future_usage: Optional[Literal["none", "off_session"]]

        class InteracPresent(StripeObject):
            pass

        class Klarna(StripeObject):
            capture_method: Optional[Literal["manual"]]
            preferred_locale: Optional[str]
            setup_future_usage: Optional[Literal["none"]]

        class Konbini(StripeObject):
            confirmation_number: Optional[str]
            expires_after_days: Optional[int]
            expires_at: Optional[int]
            product_description: Optional[str]
            setup_future_usage: Optional[Literal["none"]]

        class Link(StripeObject):
            capture_method: Optional[Literal["manual"]]
            persistent_token: Optional[str]
            setup_future_usage: Optional[Literal["none", "off_session"]]

        class Oxxo(StripeObject):
            expires_after_days: int
            setup_future_usage: Optional[Literal["none"]]

        class P24(StripeObject):
            setup_future_usage: Optional[Literal["none"]]

        class Paynow(StripeObject):
            setup_future_usage: Optional[Literal["none"]]

        class Paypal(StripeObject):
            capture_method: Optional[Literal["manual"]]
            preferred_locale: Optional[str]
            reference: Optional[str]
            reference_id: Optional[str]
            setup_future_usage: Optional[Literal["none", "off_session"]]

        class Pix(StripeObject):
            expires_after_seconds: Optional[int]
            expires_at: Optional[int]
            setup_future_usage: Optional[Literal["none"]]

        class Promptpay(StripeObject):
            setup_future_usage: Optional[Literal["none"]]

        class SepaDebit(StripeObject):
            class MandateOptions(StripeObject):
                pass

            mandate_options: Optional[MandateOptions]
            setup_future_usage: Optional[
                Literal["none", "off_session", "on_session"]
            ]
            _inner_class_types = {"mandate_options": MandateOptions}

        class Sofort(StripeObject):
            preferred_language: Optional[
                Literal["de", "en", "es", "fr", "it", "nl", "pl"]
            ]
            setup_future_usage: Optional[Literal["none", "off_session"]]

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
            preferred_settlement_speed: Optional[
                Literal["fastest", "standard"]
            ]
            setup_future_usage: Optional[
                Literal["none", "off_session", "on_session"]
            ]
            verification_method: Optional[
                Literal["automatic", "instant", "microdeposits"]
            ]
            _inner_class_types = {
                "financial_connections": FinancialConnections
            }

        class WechatPay(StripeObject):
            app_id: Optional[str]
            client: Optional[Literal["android", "ios", "web"]]
            setup_future_usage: Optional[Literal["none"]]

        class Zip(StripeObject):
            setup_future_usage: Optional[Literal["none"]]

        acss_debit: Optional[AcssDebit]
        affirm: Optional[Affirm]
        afterpay_clearpay: Optional[AfterpayClearpay]
        alipay: Optional[Alipay]
        au_becs_debit: Optional[AuBecsDebit]
        bacs_debit: Optional[BacsDebit]
        bancontact: Optional[Bancontact]
        blik: Optional[Blik]
        boleto: Optional[Boleto]
        card: Optional[Card]
        card_present: Optional[CardPresent]
        cashapp: Optional[Cashapp]
        customer_balance: Optional[CustomerBalance]
        eps: Optional[Eps]
        fpx: Optional[Fpx]
        giropay: Optional[Giropay]
        grabpay: Optional[Grabpay]
        ideal: Optional[Ideal]
        interac_present: Optional[InteracPresent]
        klarna: Optional[Klarna]
        konbini: Optional[Konbini]
        link: Optional[Link]
        oxxo: Optional[Oxxo]
        p24: Optional[P24]
        paynow: Optional[Paynow]
        paypal: Optional[Paypal]
        pix: Optional[Pix]
        promptpay: Optional[Promptpay]
        sepa_debit: Optional[SepaDebit]
        sofort: Optional[Sofort]
        us_bank_account: Optional[UsBankAccount]
        wechat_pay: Optional[WechatPay]
        zip: Optional[Zip]
        _inner_class_types = {
            "acss_debit": AcssDebit,
            "affirm": Affirm,
            "afterpay_clearpay": AfterpayClearpay,
            "alipay": Alipay,
            "au_becs_debit": AuBecsDebit,
            "bacs_debit": BacsDebit,
            "bancontact": Bancontact,
            "blik": Blik,
            "boleto": Boleto,
            "card": Card,
            "card_present": CardPresent,
            "cashapp": Cashapp,
            "customer_balance": CustomerBalance,
            "eps": Eps,
            "fpx": Fpx,
            "giropay": Giropay,
            "grabpay": Grabpay,
            "ideal": Ideal,
            "interac_present": InteracPresent,
            "klarna": Klarna,
            "konbini": Konbini,
            "link": Link,
            "oxxo": Oxxo,
            "p24": P24,
            "paynow": Paynow,
            "paypal": Paypal,
            "pix": Pix,
            "promptpay": Promptpay,
            "sepa_debit": SepaDebit,
            "sofort": Sofort,
            "us_bank_account": UsBankAccount,
            "wechat_pay": WechatPay,
            "zip": Zip,
        }

    class Processing(StripeObject):
        class Card(StripeObject):
            class CustomerNotification(StripeObject):
                approval_requested: Optional[bool]
                completes_at: Optional[int]

            customer_notification: Optional[CustomerNotification]
            _inner_class_types = {
                "customer_notification": CustomerNotification
            }

        card: Optional[Card]
        type: Literal["card"]
        _inner_class_types = {"card": Card}

    class Shipping(StripeObject):
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

    class TransferData(StripeObject):
        amount: Optional[int]
        destination: ExpandableField["Account"]

    amount: int
    amount_capturable: int
    amount_details: Optional[AmountDetails]
    amount_received: int
    application: Optional[ExpandableField["Application"]]
    application_fee_amount: Optional[int]
    automatic_payment_methods: Optional[AutomaticPaymentMethods]
    canceled_at: Optional[int]
    cancellation_reason: Optional[
        Literal[
            "abandoned",
            "automatic",
            "duplicate",
            "failed_invoice",
            "fraudulent",
            "requested_by_customer",
            "void_invoice",
        ]
    ]
    capture_method: Literal["automatic", "automatic_async", "manual"]
    client_secret: Optional[str]
    confirmation_method: Literal["automatic", "manual"]
    created: int
    currency: str
    customer: Optional[ExpandableField["Customer"]]
    description: Optional[str]
    id: str
    invoice: Optional[ExpandableField["Invoice"]]
    last_payment_error: Optional[LastPaymentError]
    latest_charge: Optional[ExpandableField["Charge"]]
    livemode: bool
    metadata: Dict[str, str]
    next_action: Optional[NextAction]
    object: Literal["payment_intent"]
    on_behalf_of: Optional[ExpandableField["Account"]]
    payment_details: Optional[PaymentDetails]
    payment_method: Optional[ExpandableField["PaymentMethod"]]
    payment_method_configuration_details: Optional[
        PaymentMethodConfigurationDetails
    ]
    payment_method_options: Optional[PaymentMethodOptions]
    payment_method_types: List[str]
    processing: Optional[Processing]
    receipt_email: Optional[str]
    review: Optional[ExpandableField["Review"]]
    secret_key_confirmation: Optional[Literal["optional", "required"]]
    setup_future_usage: Optional[Literal["off_session", "on_session"]]
    shipping: Optional[Shipping]
    source: Optional[ExpandableField[Any]]
    statement_descriptor: Optional[str]
    statement_descriptor_suffix: Optional[str]
    status: Literal[
        "canceled",
        "processing",
        "requires_action",
        "requires_capture",
        "requires_confirmation",
        "requires_payment_method",
        "succeeded",
    ]
    transfer_data: Optional[TransferData]
    transfer_group: Optional[str]

    @classmethod
    def _cls_apply_customer_balance(
        cls,
        intent: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/payment_intents/{intent}/apply_customer_balance".format(
                intent=util.sanitize_id(intent)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_apply_customer_balance")
    def apply_customer_balance(
        self, idempotency_key: Optional[str] = None, **params: Any
    ):
        return self._request(
            "post",
            "/v1/payment_intents/{intent}/apply_customer_balance".format(
                intent=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_cancel(
        cls,
        intent: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/payment_intents/{intent}/cancel".format(
                intent=util.sanitize_id(intent)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_cancel")
    def cancel(self, idempotency_key: Optional[str] = None, **params: Any):
        return self._request(
            "post",
            "/v1/payment_intents/{intent}/cancel".format(
                intent=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_capture(
        cls,
        intent: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/payment_intents/{intent}/capture".format(
                intent=util.sanitize_id(intent)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_capture")
    def capture(self, idempotency_key: Optional[str] = None, **params: Any):
        return self._request(
            "post",
            "/v1/payment_intents/{intent}/capture".format(
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
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/payment_intents/{intent}/confirm".format(
                intent=util.sanitize_id(intent)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_confirm")
    def confirm(self, idempotency_key: Optional[str] = None, **params: Any):
        return self._request(
            "post",
            "/v1/payment_intents/{intent}/confirm".format(
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
        **params: Any
    ) -> "PaymentIntent":
        return cast(
            "PaymentIntent",
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
    def _cls_increment_authorization(
        cls,
        intent: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/payment_intents/{intent}/increment_authorization".format(
                intent=util.sanitize_id(intent)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_increment_authorization")
    def increment_authorization(
        self, idempotency_key: Optional[str] = None, **params: Any
    ):
        return self._request(
            "post",
            "/v1/payment_intents/{intent}/increment_authorization".format(
                intent=util.sanitize_id(self.get("id"))
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
        **params: Any
    ) -> ListObject["PaymentIntent"]:
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
    def modify(cls, id, **params: Any) -> "PaymentIntent":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "PaymentIntent",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "PaymentIntent":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance

    @classmethod
    def _cls_verify_microdeposits(
        cls,
        intent: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/payment_intents/{intent}/verify_microdeposits".format(
                intent=util.sanitize_id(intent)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_verify_microdeposits")
    def verify_microdeposits(
        self, idempotency_key: Optional[str] = None, **params: Any
    ):
        return self._request(
            "post",
            "/v1/payment_intents/{intent}/verify_microdeposits".format(
                intent=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def search(cls, *args, **kwargs) -> SearchResultObject["PaymentIntent"]:
        return cls._search(
            search_url="/v1/payment_intents/search", *args, **kwargs
        )

    @classmethod
    def search_auto_paging_iter(cls, *args, **kwargs):
        return cls.search(*args, **kwargs).auto_paging_iter()

    _inner_class_types = {
        "amount_details": AmountDetails,
        "automatic_payment_methods": AutomaticPaymentMethods,
        "last_payment_error": LastPaymentError,
        "next_action": NextAction,
        "payment_details": PaymentDetails,
        "payment_method_configuration_details": PaymentMethodConfigurationDetails,
        "payment_method_options": PaymentMethodOptions,
        "processing": Processing,
        "shipping": Shipping,
        "transfer_data": TransferData,
    }
