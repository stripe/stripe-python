# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import APIResource
from stripe.api_resources.expandable_field import ExpandableField
from stripe.stripe_object import StripeObject
from typing import Any, List, Optional
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.charge import Charge
    from stripe.api_resources.payment_method import PaymentMethod
    from stripe.api_resources.setup_attempt import SetupAttempt


class ConfirmationToken(APIResource["ConfirmationToken"]):
    """
    ConfirmationTokens help transport client side data collected by Stripe JS over
    to your server for confirming a PaymentIntent or SetupIntent. If the confirmation
    is successful, values present on the ConfirmationToken are written onto the Intent.
    """

    OBJECT_NAME = "confirmation_token"

    class MandateData(StripeObject):
        class CustomerAcceptance(StripeObject):
            class Online(StripeObject):
                ip_address: Optional[str]
                user_agent: Optional[str]

            online: Optional[Online]
            type: str
            _inner_class_types = {"online": Online}

        customer_acceptance: CustomerAcceptance
        _inner_class_types = {"customer_acceptance": CustomerAcceptance}

    class PaymentMethodPreview(StripeObject):
        class AcssDebit(StripeObject):
            bank_name: Optional[str]
            fingerprint: Optional[str]
            institution_number: Optional[str]
            last4: Optional[str]
            transit_number: Optional[str]

        class Affirm(StripeObject):
            pass

        class AfterpayClearpay(StripeObject):
            pass

        class Alipay(StripeObject):
            pass

        class AuBecsDebit(StripeObject):
            bsb_number: Optional[str]
            fingerprint: Optional[str]
            last4: Optional[str]

        class BacsDebit(StripeObject):
            fingerprint: Optional[str]
            last4: Optional[str]
            sort_code: Optional[str]

        class Bancontact(StripeObject):
            pass

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

        class Blik(StripeObject):
            pass

        class Boleto(StripeObject):
            tax_id: str

        class Card(StripeObject):
            class Checks(StripeObject):
                address_line1_check: Optional[str]
                address_postal_code_check: Optional[str]
                cvc_check: Optional[str]

            class Networks(StripeObject):
                available: List[str]
                preferred: Optional[str]

            class ThreeDSecureUsage(StripeObject):
                supported: bool

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

            brand: str
            checks: Optional[Checks]
            country: Optional[str]
            description: Optional[str]
            exp_month: int
            exp_year: int
            fingerprint: Optional[str]
            funding: str
            iin: Optional[str]
            issuer: Optional[str]
            last4: str
            networks: Optional[Networks]
            three_d_secure_usage: Optional[ThreeDSecureUsage]
            wallet: Optional[Wallet]
            _inner_class_types = {
                "checks": Checks,
                "networks": Networks,
                "three_d_secure_usage": ThreeDSecureUsage,
                "wallet": Wallet,
            }

        class CardPresent(StripeObject):
            class Networks(StripeObject):
                available: List[str]
                preferred: Optional[str]

            brand: Optional[str]
            cardholder_name: Optional[str]
            country: Optional[str]
            description: Optional[str]
            exp_month: int
            exp_year: int
            fingerprint: Optional[str]
            funding: Optional[str]
            iin: Optional[str]
            issuer: Optional[str]
            last4: Optional[str]
            networks: Optional[Networks]
            read_method: Optional[
                Literal[
                    "contact_emv",
                    "contactless_emv",
                    "contactless_magstripe_mode",
                    "magnetic_stripe_fallback",
                    "magnetic_stripe_track2",
                ]
            ]
            _inner_class_types = {"networks": Networks}

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

        class Giropay(StripeObject):
            pass

        class Grabpay(StripeObject):
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

        class InteracPresent(StripeObject):
            class Networks(StripeObject):
                available: List[str]
                preferred: Optional[str]

            brand: Optional[str]
            cardholder_name: Optional[str]
            country: Optional[str]
            description: Optional[str]
            exp_month: int
            exp_year: int
            fingerprint: Optional[str]
            funding: Optional[str]
            iin: Optional[str]
            issuer: Optional[str]
            last4: Optional[str]
            networks: Optional[Networks]
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
            _inner_class_types = {"networks": Networks}

        class Klarna(StripeObject):
            class Dob(StripeObject):
                day: Optional[int]
                month: Optional[int]
                year: Optional[int]

            dob: Optional[Dob]
            _inner_class_types = {"dob": Dob}

        class Konbini(StripeObject):
            pass

        class Link(StripeObject):
            email: Optional[str]
            persistent_token: Optional[str]

        class Oxxo(StripeObject):
            pass

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

        class Paynow(StripeObject):
            pass

        class Paypal(StripeObject):
            fingerprint: Optional[str]
            payer_email: Optional[str]
            payer_id: Optional[str]
            verified_email: Optional[str]

        class Pix(StripeObject):
            pass

        class Promptpay(StripeObject):
            pass

        class SepaDebit(StripeObject):
            class GeneratedFrom(StripeObject):
                charge: Optional[ExpandableField["Charge"]]
                setup_attempt: Optional[ExpandableField["SetupAttempt"]]

            bank_code: Optional[str]
            branch_code: Optional[str]
            country: Optional[str]
            fingerprint: Optional[str]
            generated_from: Optional[GeneratedFrom]
            last4: Optional[str]
            _inner_class_types = {"generated_from": GeneratedFrom}

        class Sofort(StripeObject):
            country: Optional[str]

        class UsBankAccount(StripeObject):
            class Networks(StripeObject):
                preferred: Optional[str]
                supported: List[Literal["ach", "us_domestic_wire"]]

            class StatusDetails(StripeObject):
                class Blocked(StripeObject):
                    network_code: Optional[
                        Literal[
                            "R02",
                            "R03",
                            "R04",
                            "R05",
                            "R07",
                            "R08",
                            "R10",
                            "R11",
                            "R16",
                            "R20",
                            "R29",
                            "R31",
                        ]
                    ]
                    reason: Optional[
                        Literal[
                            "bank_account_closed",
                            "bank_account_frozen",
                            "bank_account_invalid_details",
                            "bank_account_restricted",
                            "bank_account_unusable",
                            "debit_not_authorized",
                        ]
                    ]

                blocked: Optional[Blocked]
                _inner_class_types = {"blocked": Blocked}

            account_holder_type: Optional[Literal["company", "individual"]]
            account_number: Optional[str]
            account_type: Optional[Literal["checking", "savings"]]
            bank_name: Optional[str]
            financial_connections_account: Optional[str]
            fingerprint: Optional[str]
            last4: Optional[str]
            networks: Optional[Networks]
            routing_number: Optional[str]
            status_details: Optional[StatusDetails]
            _inner_class_types = {
                "networks": Networks,
                "status_details": StatusDetails,
            }

        class WechatPay(StripeObject):
            pass

        class Zip(StripeObject):
            pass

        acss_debit: Optional[AcssDebit]
        affirm: Optional[Affirm]
        afterpay_clearpay: Optional[AfterpayClearpay]
        alipay: Optional[Alipay]
        au_becs_debit: Optional[AuBecsDebit]
        bacs_debit: Optional[BacsDebit]
        bancontact: Optional[Bancontact]
        billing_details: BillingDetails
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
            "card",
            "card_present",
            "cashapp",
            "customer_balance",
            "eps",
            "fpx",
            "giropay",
            "grabpay",
            "ideal",
            "interac_present",
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
            "billing_details": BillingDetails,
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

    class Shipping(StripeObject):
        class Address(StripeObject):
            city: Optional[str]
            country: Optional[str]
            line1: Optional[str]
            line2: Optional[str]
            postal_code: Optional[str]
            state: Optional[str]

        address: Address
        name: str
        phone: Optional[str]
        _inner_class_types = {"address": Address}

    created: int
    expires_at: Optional[int]
    id: str
    livemode: bool
    mandate_data: Optional[MandateData]
    object: Literal["confirmation_token"]
    payment_intent: Optional[str]
    payment_method: Optional[ExpandableField["PaymentMethod"]]
    payment_method_preview: Optional[PaymentMethodPreview]
    return_url: Optional[str]
    setup_future_usage: Optional[Literal["off_session", "on_session"]]
    setup_intent: Optional[str]
    shipping: Optional[Shipping]

    @classmethod
    def retrieve(
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "ConfirmationToken":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance

    _inner_class_types = {
        "mandate_data": MandateData,
        "payment_method_preview": PaymentMethodPreview,
        "shipping": Shipping,
    }
