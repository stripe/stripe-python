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
    from stripe.api_resources.application_fee import ApplicationFee
    from stripe.api_resources.balance_transaction import BalanceTransaction
    from stripe.api_resources.customer import Customer
    from stripe.api_resources.invoice import Invoice
    from stripe.api_resources.mandate import Mandate
    from stripe.api_resources.payment_intent import PaymentIntent
    from stripe.api_resources.payment_method import PaymentMethod
    from stripe.api_resources.refund import Refund
    from stripe.api_resources.review import Review
    from stripe.api_resources.transfer import Transfer


class Charge(
    CreateableAPIResource["Charge"],
    ListableAPIResource["Charge"],
    SearchableAPIResource["Charge"],
    UpdateableAPIResource["Charge"],
):
    """
    The `Charge` object represents a single attempt to move money into your Stripe account.
    PaymentIntent confirmation is the most common way to create Charges, but transferring
    money to a different Stripe account through Connect also creates Charges.
    Some legacy payment flows create Charges directly, which is not recommended for new integrations.
    """

    OBJECT_NAME = "charge"

    class BillingDetails(StripeObject):
        class Address(StripeObject):
            city: Optional[str]
            country: Optional[str]
            line1: Optional[str]
            line2: Optional[str]
            postal_code: Optional[str]
            state: Optional[str]

        address: Optional[Address]
        email: Optional[str]
        name: Optional[str]
        phone: Optional[str]
        _inner_class_types = {"address": Address}

    class FraudDetails(StripeObject):
        stripe_report: Optional[str]
        user_report: Optional[str]

    class Level3(StripeObject):
        class LineItem(StripeObject):
            discount_amount: Optional[int]
            product_code: str
            product_description: str
            quantity: Optional[int]
            tax_amount: Optional[int]
            unit_cost: Optional[int]

        customer_reference: Optional[str]
        line_items: List[LineItem]
        merchant_reference: str
        shipping_address_zip: Optional[str]
        shipping_amount: Optional[int]
        shipping_from_zip: Optional[str]
        _inner_class_types = {"line_items": LineItem}

    class Outcome(StripeObject):
        class Rule(StripeObject):
            action: str
            id: str
            predicate: str

        network_status: Optional[str]
        reason: Optional[str]
        risk_level: Optional[str]
        risk_score: Optional[int]
        rule: Optional[ExpandableField[Rule]]
        seller_message: Optional[str]
        type: str
        _inner_class_types = {"rule": Rule}

    class PaymentMethodDetails(StripeObject):
        class AchCreditTransfer(StripeObject):
            account_number: Optional[str]
            bank_name: Optional[str]
            routing_number: Optional[str]
            swift_code: Optional[str]

        class AchDebit(StripeObject):
            account_holder_type: Optional[Literal["company", "individual"]]
            bank_name: Optional[str]
            country: Optional[str]
            fingerprint: Optional[str]
            last4: Optional[str]
            routing_number: Optional[str]

        class AcssDebit(StripeObject):
            bank_name: Optional[str]
            fingerprint: Optional[str]
            institution_number: Optional[str]
            last4: Optional[str]
            mandate: Optional[str]
            transit_number: Optional[str]

        class Affirm(StripeObject):
            pass

        class AfterpayClearpay(StripeObject):
            order_id: Optional[str]
            reference: Optional[str]

        class Alipay(StripeObject):
            buyer_id: Optional[str]
            fingerprint: Optional[str]
            transaction_id: Optional[str]

        class AuBecsDebit(StripeObject):
            bsb_number: Optional[str]
            fingerprint: Optional[str]
            last4: Optional[str]
            mandate: Optional[str]

        class BacsDebit(StripeObject):
            fingerprint: Optional[str]
            last4: Optional[str]
            mandate: Optional[str]
            sort_code: Optional[str]

        class Bancontact(StripeObject):
            bank_code: Optional[str]
            bank_name: Optional[str]
            bic: Optional[str]
            generated_sepa_debit: Optional[ExpandableField["PaymentMethod"]]
            generated_sepa_debit_mandate: Optional[ExpandableField["Mandate"]]
            iban_last4: Optional[str]
            preferred_language: Optional[Literal["de", "en", "fr", "nl"]]
            verified_name: Optional[str]

        class Blik(StripeObject):
            pass

        class Boleto(StripeObject):
            tax_id: str

        class Card(StripeObject):
            class Checks(StripeObject):
                address_line1_check: Optional[str]
                address_postal_code_check: Optional[str]
                cvc_check: Optional[str]

            class ExtendedAuthorization(StripeObject):
                status: Literal["disabled", "enabled"]

            class IncrementalAuthorization(StripeObject):
                status: Literal["available", "unavailable"]

            class Installments(StripeObject):
                class Plan(StripeObject):
                    count: Optional[int]
                    interval: Optional[Literal["month"]]
                    type: Literal["fixed_count"]

                plan: Optional[Plan]
                _inner_class_types = {"plan": Plan}

            class Multicapture(StripeObject):
                status: Literal["available", "unavailable"]

            class NetworkToken(StripeObject):
                used: bool

            class Overcapture(StripeObject):
                maximum_amount_capturable: int
                status: Literal["available", "unavailable"]

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
                class AmexExpressCheckout(StripeObject):
                    pass

                class ApplePay(StripeObject):
                    pass

                class GooglePay(StripeObject):
                    pass

                class Link(StripeObject):
                    pass

                class Masterpass(StripeObject):
                    class BillingAddress(StripeObject):
                        city: Optional[str]
                        country: Optional[str]
                        line1: Optional[str]
                        line2: Optional[str]
                        postal_code: Optional[str]
                        state: Optional[str]

                    class ShippingAddress(StripeObject):
                        city: Optional[str]
                        country: Optional[str]
                        line1: Optional[str]
                        line2: Optional[str]
                        postal_code: Optional[str]
                        state: Optional[str]

                    billing_address: Optional[BillingAddress]
                    email: Optional[str]
                    name: Optional[str]
                    shipping_address: Optional[ShippingAddress]
                    _inner_class_types = {
                        "billing_address": BillingAddress,
                        "shipping_address": ShippingAddress,
                    }

                class SamsungPay(StripeObject):
                    pass

                class VisaCheckout(StripeObject):
                    class BillingAddress(StripeObject):
                        city: Optional[str]
                        country: Optional[str]
                        line1: Optional[str]
                        line2: Optional[str]
                        postal_code: Optional[str]
                        state: Optional[str]

                    class ShippingAddress(StripeObject):
                        city: Optional[str]
                        country: Optional[str]
                        line1: Optional[str]
                        line2: Optional[str]
                        postal_code: Optional[str]
                        state: Optional[str]

                    billing_address: Optional[BillingAddress]
                    email: Optional[str]
                    name: Optional[str]
                    shipping_address: Optional[ShippingAddress]
                    _inner_class_types = {
                        "billing_address": BillingAddress,
                        "shipping_address": ShippingAddress,
                    }

                amex_express_checkout: Optional[AmexExpressCheckout]
                apple_pay: Optional[ApplePay]
                dynamic_last4: Optional[str]
                google_pay: Optional[GooglePay]
                link: Optional[Link]
                masterpass: Optional[Masterpass]
                samsung_pay: Optional[SamsungPay]
                type: Literal[
                    "amex_express_checkout",
                    "apple_pay",
                    "google_pay",
                    "link",
                    "masterpass",
                    "samsung_pay",
                    "visa_checkout",
                ]
                visa_checkout: Optional[VisaCheckout]
                _inner_class_types = {
                    "amex_express_checkout": AmexExpressCheckout,
                    "apple_pay": ApplePay,
                    "google_pay": GooglePay,
                    "link": Link,
                    "masterpass": Masterpass,
                    "samsung_pay": SamsungPay,
                    "visa_checkout": VisaCheckout,
                }

            amount_authorized: Optional[int]
            brand: Optional[str]
            checks: Optional[Checks]
            country: Optional[str]
            description: Optional[str]
            exp_month: int
            exp_year: int
            extended_authorization: Optional[ExtendedAuthorization]
            fingerprint: Optional[str]
            funding: Optional[str]
            iin: Optional[str]
            incremental_authorization: Optional[IncrementalAuthorization]
            installments: Optional[Installments]
            issuer: Optional[str]
            last4: Optional[str]
            mandate: Optional[str]
            moto: Optional[bool]
            multicapture: Optional[Multicapture]
            network: Optional[str]
            network_token: Optional[NetworkToken]
            overcapture: Optional[Overcapture]
            three_d_secure: Optional[ThreeDSecure]
            wallet: Optional[Wallet]
            _inner_class_types = {
                "checks": Checks,
                "extended_authorization": ExtendedAuthorization,
                "incremental_authorization": IncrementalAuthorization,
                "installments": Installments,
                "multicapture": Multicapture,
                "network_token": NetworkToken,
                "overcapture": Overcapture,
                "three_d_secure": ThreeDSecure,
                "wallet": Wallet,
            }

        class CardPresent(StripeObject):
            class Receipt(StripeObject):
                account_type: Optional[
                    Literal["checking", "credit", "prepaid", "unknown"]
                ]
                application_cryptogram: Optional[str]
                application_preferred_name: Optional[str]
                authorization_code: Optional[str]
                authorization_response_code: Optional[str]
                cardholder_verification_method: Optional[str]
                dedicated_file_name: Optional[str]
                terminal_verification_results: Optional[str]
                transaction_status_information: Optional[str]

            amount_authorized: Optional[int]
            brand: Optional[str]
            capture_before: Optional[int]
            cardholder_name: Optional[str]
            country: Optional[str]
            description: Optional[str]
            emv_auth_data: Optional[str]
            exp_month: int
            exp_year: int
            fingerprint: Optional[str]
            funding: Optional[str]
            generated_card: Optional[str]
            iin: Optional[str]
            incremental_authorization_supported: bool
            issuer: Optional[str]
            last4: Optional[str]
            network: Optional[str]
            overcapture_supported: bool
            read_method: Optional[
                Literal[
                    "contact_emv",
                    "contactless_emv",
                    "contactless_magstripe_mode",
                    "magnetic_stripe_fallback",
                    "magnetic_stripe_track2",
                ]
            ]
            receipt: Optional[Receipt]
            _inner_class_types = {"receipt": Receipt}

        class Cashapp(StripeObject):
            buyer_id: Optional[str]
            cashtag: Optional[str]

        class CustomerBalance(StripeObject):
            pass

        class Eps(StripeObject):
            bank: Optional[
                Literal[
                    "arzte_und_apotheker_bank",
                    "austrian_anadi_bank_ag",
                    "bank_austria",
                    "bankhaus_carl_spangler",
                    "bankhaus_schelhammer_und_schattera_ag",
                    "bawag_psk_ag",
                    "bks_bank_ag",
                    "brull_kallmus_bank_ag",
                    "btv_vier_lander_bank",
                    "capital_bank_grawe_gruppe_ag",
                    "deutsche_bank_ag",
                    "dolomitenbank",
                    "easybank_ag",
                    "erste_bank_und_sparkassen",
                    "hypo_alpeadriabank_international_ag",
                    "hypo_bank_burgenland_aktiengesellschaft",
                    "hypo_noe_lb_fur_niederosterreich_u_wien",
                    "hypo_oberosterreich_salzburg_steiermark",
                    "hypo_tirol_bank_ag",
                    "hypo_vorarlberg_bank_ag",
                    "marchfelder_bank",
                    "oberbank_ag",
                    "raiffeisen_bankengruppe_osterreich",
                    "schoellerbank_ag",
                    "sparda_bank_wien",
                    "volksbank_gruppe",
                    "volkskreditbank_ag",
                    "vr_bank_braunau",
                ]
            ]
            verified_name: Optional[str]

        class Fpx(StripeObject):
            account_holder_type: Optional[Literal["company", "individual"]]
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
            transaction_id: Optional[str]

        class Giropay(StripeObject):
            bank_code: Optional[str]
            bank_name: Optional[str]
            bic: Optional[str]
            verified_name: Optional[str]

        class Grabpay(StripeObject):
            transaction_id: Optional[str]

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

        class InteracPresent(StripeObject):
            class Receipt(StripeObject):
                account_type: Optional[
                    Literal["checking", "savings", "unknown"]
                ]
                application_cryptogram: Optional[str]
                application_preferred_name: Optional[str]
                authorization_code: Optional[str]
                authorization_response_code: Optional[str]
                cardholder_verification_method: Optional[str]
                dedicated_file_name: Optional[str]
                terminal_verification_results: Optional[str]
                transaction_status_information: Optional[str]

            brand: Optional[str]
            cardholder_name: Optional[str]
            country: Optional[str]
            description: Optional[str]
            emv_auth_data: Optional[str]
            exp_month: int
            exp_year: int
            fingerprint: Optional[str]
            funding: Optional[str]
            generated_card: Optional[str]
            iin: Optional[str]
            issuer: Optional[str]
            last4: Optional[str]
            network: Optional[str]
            preferred_locales: Optional[List[str]]
            read_method: Optional[
                Literal[
                    "contact_emv",
                    "contactless_emv",
                    "contactless_magstripe_mode",
                    "magnetic_stripe_fallback",
                    "magnetic_stripe_track2",
                ]
            ]
            receipt: Optional[Receipt]
            _inner_class_types = {"receipt": Receipt}

        class Klarna(StripeObject):
            payment_method_category: Optional[str]
            preferred_locale: Optional[str]

        class Konbini(StripeObject):
            class Store(StripeObject):
                chain: Optional[
                    Literal["familymart", "lawson", "ministop", "seicomart"]
                ]

            store: Optional[Store]
            _inner_class_types = {"store": Store}

        class Link(StripeObject):
            country: Optional[str]

        class Multibanco(StripeObject):
            entity: Optional[str]
            reference: Optional[str]

        class Oxxo(StripeObject):
            number: Optional[str]

        class P24(StripeObject):
            bank: Optional[
                Literal[
                    "alior_bank",
                    "bank_millennium",
                    "bank_nowy_bfg_sa",
                    "bank_pekao_sa",
                    "banki_spbdzielcze",
                    "blik",
                    "bnp_paribas",
                    "boz",
                    "citi_handlowy",
                    "credit_agricole",
                    "envelobank",
                    "etransfer_pocztowy24",
                    "getin_bank",
                    "ideabank",
                    "ing",
                    "inteligo",
                    "mbank_mtransfer",
                    "nest_przelew",
                    "noble_pay",
                    "pbac_z_ipko",
                    "plus_bank",
                    "santander_przelew24",
                    "tmobile_usbugi_bankowe",
                    "toyota_bank",
                    "volkswagen_bank",
                ]
            ]
            reference: Optional[str]
            verified_name: Optional[str]

        class Paynow(StripeObject):
            reference: Optional[str]

        class Paypal(StripeObject):
            class SellerProtection(StripeObject):
                dispute_categories: Optional[
                    List[Literal["fraudulent", "product_not_received"]]
                ]
                status: Literal[
                    "eligible", "not_eligible", "partially_eligible"
                ]

            class Shipping(StripeObject):
                city: Optional[str]
                country: Optional[str]
                line1: Optional[str]
                line2: Optional[str]
                postal_code: Optional[str]
                state: Optional[str]

            class VerifiedAddress(StripeObject):
                city: Optional[str]
                country: Optional[str]
                line1: Optional[str]
                line2: Optional[str]
                postal_code: Optional[str]
                state: Optional[str]

            payer_email: Optional[str]
            payer_id: Optional[str]
            payer_name: Optional[str]
            seller_protection: Optional[SellerProtection]
            shipping: Optional[Shipping]
            transaction_id: Optional[str]
            verified_address: Optional[VerifiedAddress]
            verified_email: Optional[str]
            verified_name: Optional[str]
            _inner_class_types = {
                "seller_protection": SellerProtection,
                "shipping": Shipping,
                "verified_address": VerifiedAddress,
            }

        class Pix(StripeObject):
            bank_transaction_id: Optional[str]

        class Promptpay(StripeObject):
            reference: Optional[str]

        class SepaCreditTransfer(StripeObject):
            bank_name: Optional[str]
            bic: Optional[str]
            iban: Optional[str]

        class SepaDebit(StripeObject):
            bank_code: Optional[str]
            branch_code: Optional[str]
            country: Optional[str]
            fingerprint: Optional[str]
            last4: Optional[str]
            mandate: Optional[str]

        class Sofort(StripeObject):
            bank_code: Optional[str]
            bank_name: Optional[str]
            bic: Optional[str]
            country: Optional[str]
            generated_sepa_debit: Optional[ExpandableField["PaymentMethod"]]
            generated_sepa_debit_mandate: Optional[ExpandableField["Mandate"]]
            iban_last4: Optional[str]
            preferred_language: Optional[
                Literal["de", "en", "es", "fr", "it", "nl", "pl"]
            ]
            verified_name: Optional[str]

        class StripeAccount(StripeObject):
            pass

        class UsBankAccount(StripeObject):
            account_holder_type: Optional[Literal["company", "individual"]]
            account_type: Optional[Literal["checking", "savings"]]
            bank_name: Optional[str]
            fingerprint: Optional[str]
            last4: Optional[str]
            routing_number: Optional[str]

        class Wechat(StripeObject):
            pass

        class WechatPay(StripeObject):
            fingerprint: Optional[str]
            transaction_id: Optional[str]

        class Zip(StripeObject):
            pass

        ach_credit_transfer: Optional[AchCreditTransfer]
        ach_debit: Optional[AchDebit]
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
        multibanco: Optional[Multibanco]
        oxxo: Optional[Oxxo]
        p24: Optional[P24]
        paynow: Optional[Paynow]
        paypal: Optional[Paypal]
        pix: Optional[Pix]
        promptpay: Optional[Promptpay]
        sepa_credit_transfer: Optional[SepaCreditTransfer]
        sepa_debit: Optional[SepaDebit]
        sofort: Optional[Sofort]
        stripe_account: Optional[StripeAccount]
        type: str
        us_bank_account: Optional[UsBankAccount]
        wechat: Optional[Wechat]
        wechat_pay: Optional[WechatPay]
        zip: Optional[Zip]
        _inner_class_types = {
            "ach_credit_transfer": AchCreditTransfer,
            "ach_debit": AchDebit,
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
            "multibanco": Multibanco,
            "oxxo": Oxxo,
            "p24": P24,
            "paynow": Paynow,
            "paypal": Paypal,
            "pix": Pix,
            "promptpay": Promptpay,
            "sepa_credit_transfer": SepaCreditTransfer,
            "sepa_debit": SepaDebit,
            "sofort": Sofort,
            "stripe_account": StripeAccount,
            "us_bank_account": UsBankAccount,
            "wechat": Wechat,
            "wechat_pay": WechatPay,
            "zip": Zip,
        }

    class RadarOptions(StripeObject):
        session: Optional[str]

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
    amount_captured: int
    amount_refunded: int
    application: Optional[ExpandableField["Application"]]
    application_fee: Optional[ExpandableField["ApplicationFee"]]
    application_fee_amount: Optional[int]
    authorization_code: Optional[str]
    balance_transaction: Optional[ExpandableField["BalanceTransaction"]]
    billing_details: BillingDetails
    calculated_statement_descriptor: Optional[str]
    captured: bool
    created: int
    currency: str
    customer: Optional[ExpandableField["Customer"]]
    description: Optional[str]
    disputed: bool
    failure_balance_transaction: Optional[
        ExpandableField["BalanceTransaction"]
    ]
    failure_code: Optional[str]
    failure_message: Optional[str]
    fraud_details: Optional[FraudDetails]
    id: str
    invoice: Optional[ExpandableField["Invoice"]]
    level3: Optional[Level3]
    livemode: bool
    metadata: Dict[str, str]
    object: Literal["charge"]
    on_behalf_of: Optional[ExpandableField["Account"]]
    outcome: Optional[Outcome]
    paid: bool
    payment_intent: Optional[ExpandableField["PaymentIntent"]]
    payment_method: Optional[str]
    payment_method_details: Optional[PaymentMethodDetails]
    radar_options: Optional[RadarOptions]
    receipt_email: Optional[str]
    receipt_number: Optional[str]
    receipt_url: Optional[str]
    refunded: bool
    refunds: Optional[ListObject["Refund"]]
    review: Optional[ExpandableField["Review"]]
    shipping: Optional[Shipping]
    source: Optional[Any]
    source_transfer: Optional[ExpandableField["Transfer"]]
    statement_descriptor: Optional[str]
    statement_descriptor_suffix: Optional[str]
    status: Literal["failed", "pending", "succeeded"]
    transfer: Optional[ExpandableField["Transfer"]]
    transfer_data: Optional[TransferData]
    transfer_group: Optional[str]

    @classmethod
    def _cls_capture(
        cls,
        charge: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "post",
            "/v1/charges/{charge}/capture".format(
                charge=util.sanitize_id(charge)
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
            "/v1/charges/{charge}/capture".format(
                charge=util.sanitize_id(self.get("id"))
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
    ) -> "Charge":
        return cast(
            "Charge",
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
        **params: Any
    ) -> ListObject["Charge"]:
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
    def modify(cls, id, **params: Any) -> "Charge":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "Charge",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "Charge":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance

    @classmethod
    def search(cls, *args, **kwargs) -> SearchResultObject["Charge"]:
        return cls._search(search_url="/v1/charges/search", *args, **kwargs)

    @classmethod
    def search_auto_paging_iter(cls, *args, **kwargs):
        return cls.search(*args, **kwargs).auto_paging_iter()

    def mark_as_fraudulent(self, idempotency_key=None):
        params = {"fraud_details": {"user_report": "fraudulent"}}
        url = self.instance_url()
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    def mark_as_safe(self, idempotency_key=None):
        params = {"fraud_details": {"user_report": "safe"}}
        url = self.instance_url()
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request("post", url, params, headers))
        return self

    _inner_class_types = {
        "billing_details": BillingDetails,
        "fraud_details": FraudDetails,
        "level3": Level3,
        "outcome": Outcome,
        "payment_method_details": PaymentMethodDetails,
        "radar_options": RadarOptions,
        "shipping": Shipping,
        "transfer_data": TransferData,
    }
