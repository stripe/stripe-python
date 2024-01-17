# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import _util
from stripe._createable_api_resource import CreateableAPIResource
from stripe._expandable_field import ExpandableField
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._request_options import RequestOptions
from stripe._stripe_object import StripeObject
from stripe._updateable_api_resource import UpdateableAPIResource
from stripe._util import class_method_variant
from typing import ClassVar, Dict, List, Optional, cast, overload
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)
from urllib.parse import quote_plus

if TYPE_CHECKING:
    from stripe._charge import Charge
    from stripe._customer import Customer
    from stripe._setup_attempt import SetupAttempt


class PaymentMethod(
    CreateableAPIResource["PaymentMethod"],
    ListableAPIResource["PaymentMethod"],
    UpdateableAPIResource["PaymentMethod"],
):
    """
    PaymentMethod objects represent your customer's payment instruments.
    You can use them with [PaymentIntents](https://stripe.com/docs/payments/payment-intents) to collect payments or save them to
    Customer objects to store instrument details for future payments.

    Related guides: [Payment Methods](https://stripe.com/docs/payments/payment-methods) and [More Payment Scenarios](https://stripe.com/docs/payments/more-payment-scenarios).
    """

    OBJECT_NAME: ClassVar[Literal["payment_method"]] = "payment_method"

    class AcssDebit(StripeObject):
        bank_name: Optional[str]
        """
        Name of the bank associated with the bank account.
        """
        fingerprint: Optional[str]
        """
        Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.
        """
        institution_number: Optional[str]
        """
        Institution number of the bank account.
        """
        last4: Optional[str]
        """
        Last four digits of the bank account number.
        """
        transit_number: Optional[str]
        """
        Transit number of the bank account.
        """

    class Affirm(StripeObject):
        pass

    class AfterpayClearpay(StripeObject):
        pass

    class Alipay(StripeObject):
        pass

    class AuBecsDebit(StripeObject):
        bsb_number: Optional[str]
        """
        Six-digit number identifying bank and branch associated with this bank account.
        """
        fingerprint: Optional[str]
        """
        Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.
        """
        last4: Optional[str]
        """
        Last four digits of the bank account number.
        """

    class BacsDebit(StripeObject):
        fingerprint: Optional[str]
        """
        Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.
        """
        last4: Optional[str]
        """
        Last four digits of the bank account number.
        """
        sort_code: Optional[str]
        """
        Sort code of the bank account. (e.g., `10-20-30`)
        """

    class Bancontact(StripeObject):
        pass

    class BillingDetails(StripeObject):
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
        """
        Billing address.
        """
        email: Optional[str]
        """
        Email address.
        """
        name: Optional[str]
        """
        Full name.
        """
        phone: Optional[str]
        """
        Billing phone number (including extension).
        """
        _inner_class_types = {"address": Address}

    class Blik(StripeObject):
        pass

    class Boleto(StripeObject):
        tax_id: str
        """
        Uniquely identifies the customer tax id (CNPJ or CPF)
        """

    class Card(StripeObject):
        class Checks(StripeObject):
            address_line1_check: Optional[str]
            """
            If a address line1 was provided, results of the check, one of `pass`, `fail`, `unavailable`, or `unchecked`.
            """
            address_postal_code_check: Optional[str]
            """
            If a address postal code was provided, results of the check, one of `pass`, `fail`, `unavailable`, or `unchecked`.
            """
            cvc_check: Optional[str]
            """
            If a CVC was provided, results of the check, one of `pass`, `fail`, `unavailable`, or `unchecked`.
            """

        class Networks(StripeObject):
            available: List[str]
            """
            All available networks for the card.
            """
            preferred: Optional[str]
            """
            The preferred network for the card.
            """

        class ThreeDSecureUsage(StripeObject):
            supported: bool
            """
            Whether 3D Secure is supported on this card.
            """

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

                class ShippingAddress(StripeObject):
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

                billing_address: Optional[BillingAddress]
                """
                Owner's verified billing address. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.
                """
                email: Optional[str]
                """
                Owner's verified email. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.
                """
                name: Optional[str]
                """
                Owner's verified full name. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.
                """
                shipping_address: Optional[ShippingAddress]
                """
                Owner's verified shipping address. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.
                """
                _inner_class_types = {
                    "billing_address": BillingAddress,
                    "shipping_address": ShippingAddress,
                }

            class SamsungPay(StripeObject):
                pass

            class VisaCheckout(StripeObject):
                class BillingAddress(StripeObject):
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

                class ShippingAddress(StripeObject):
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

                billing_address: Optional[BillingAddress]
                """
                Owner's verified billing address. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.
                """
                email: Optional[str]
                """
                Owner's verified email. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.
                """
                name: Optional[str]
                """
                Owner's verified full name. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.
                """
                shipping_address: Optional[ShippingAddress]
                """
                Owner's verified shipping address. Values are verified or provided by the wallet directly (if supported) at the time of authorization or settlement. They cannot be set or mutated.
                """
                _inner_class_types = {
                    "billing_address": BillingAddress,
                    "shipping_address": ShippingAddress,
                }

            amex_express_checkout: Optional[AmexExpressCheckout]
            apple_pay: Optional[ApplePay]
            dynamic_last4: Optional[str]
            """
            (For tokenized numbers only.) The last four digits of the device account number.
            """
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
            """
            The type of the card wallet, one of `amex_express_checkout`, `apple_pay`, `google_pay`, `masterpass`, `samsung_pay`, `visa_checkout`, or `link`. An additional hash is included on the Wallet subhash with a name matching this value. It contains additional information specific to the card wallet type.
            """
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
        """
        Card brand. Can be `amex`, `diners`, `discover`, `eftpos_au`, `jcb`, `mastercard`, `unionpay`, `visa`, or `unknown`.
        """
        checks: Optional[Checks]
        """
        Checks on Card address and CVC if provided.
        """
        country: Optional[str]
        """
        Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you've collected.
        """
        description: Optional[str]
        """
        A high-level description of the type of cards issued in this range. (For internal use only and not typically available in standard API requests.)
        """
        exp_month: int
        """
        Two-digit number representing the card's expiration month.
        """
        exp_year: int
        """
        Four-digit number representing the card's expiration year.
        """
        fingerprint: Optional[str]
        """
        Uniquely identifies this particular card number. You can use this attribute to check whether two customers who've signed up with you are using the same card number, for example. For payment methods that tokenize card information (Apple Pay, Google Pay), the tokenized number might be provided instead of the underlying card number.

        *As of May 1, 2021, card fingerprint in India for Connect changed to allow two fingerprints for the same card---one for India and one for the rest of the world.*
        """
        funding: str
        """
        Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`.
        """
        iin: Optional[str]
        """
        Issuer identification number of the card. (For internal use only and not typically available in standard API requests.)
        """
        issuer: Optional[str]
        """
        The name of the card's issuing bank. (For internal use only and not typically available in standard API requests.)
        """
        last4: str
        """
        The last four digits of the card.
        """
        networks: Optional[Networks]
        """
        Contains information about card networks that can be used to process the payment.
        """
        three_d_secure_usage: Optional[ThreeDSecureUsage]
        """
        Contains details on how this Card may be used for 3D Secure authentication.
        """
        wallet: Optional[Wallet]
        """
        If this Card is part of a card wallet, this contains the details of the card wallet.
        """
        _inner_class_types = {
            "checks": Checks,
            "networks": Networks,
            "three_d_secure_usage": ThreeDSecureUsage,
            "wallet": Wallet,
        }

    class CardPresent(StripeObject):
        class Networks(StripeObject):
            available: List[str]
            """
            All available networks for the card.
            """
            preferred: Optional[str]
            """
            The preferred network for the card.
            """

        brand: Optional[str]
        """
        Card brand. Can be `amex`, `diners`, `discover`, `eftpos_au`, `jcb`, `mastercard`, `unionpay`, `visa`, or `unknown`.
        """
        cardholder_name: Optional[str]
        """
        The cardholder name as read from the card, in [ISO 7813](https://en.wikipedia.org/wiki/ISO/IEC_7813) format. May include alphanumeric characters, special characters and first/last name separator (`/`). In some cases, the cardholder name may not be available depending on how the issuer has configured the card. Cardholder name is typically not available on swipe or contactless payments, such as those made with Apple Pay and Google Pay.
        """
        country: Optional[str]
        """
        Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you've collected.
        """
        description: Optional[str]
        """
        A high-level description of the type of cards issued in this range. (For internal use only and not typically available in standard API requests.)
        """
        exp_month: int
        """
        Two-digit number representing the card's expiration month.
        """
        exp_year: int
        """
        Four-digit number representing the card's expiration year.
        """
        fingerprint: Optional[str]
        """
        Uniquely identifies this particular card number. You can use this attribute to check whether two customers who've signed up with you are using the same card number, for example. For payment methods that tokenize card information (Apple Pay, Google Pay), the tokenized number might be provided instead of the underlying card number.

        *As of May 1, 2021, card fingerprint in India for Connect changed to allow two fingerprints for the same card---one for India and one for the rest of the world.*
        """
        funding: Optional[str]
        """
        Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`.
        """
        iin: Optional[str]
        """
        Issuer identification number of the card. (For internal use only and not typically available in standard API requests.)
        """
        issuer: Optional[str]
        """
        The name of the card's issuing bank. (For internal use only and not typically available in standard API requests.)
        """
        last4: Optional[str]
        """
        The last four digits of the card.
        """
        networks: Optional[Networks]
        """
        Contains information about card networks that can be used to process the payment.
        """
        read_method: Optional[
            Literal[
                "contact_emv",
                "contactless_emv",
                "contactless_magstripe_mode",
                "magnetic_stripe_fallback",
                "magnetic_stripe_track2",
            ]
        ]
        """
        How card details were read in this transaction.
        """
        _inner_class_types = {"networks": Networks}

    class Cashapp(StripeObject):
        buyer_id: Optional[str]
        """
        A unique and immutable identifier assigned by Cash App to every buyer.
        """
        cashtag: Optional[str]
        """
        A public identifier for buyers using Cash App.
        """

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
        """
        The customer's bank. Should be one of `arzte_und_apotheker_bank`, `austrian_anadi_bank_ag`, `bank_austria`, `bankhaus_carl_spangler`, `bankhaus_schelhammer_und_schattera_ag`, `bawag_psk_ag`, `bks_bank_ag`, `brull_kallmus_bank_ag`, `btv_vier_lander_bank`, `capital_bank_grawe_gruppe_ag`, `deutsche_bank_ag`, `dolomitenbank`, `easybank_ag`, `erste_bank_und_sparkassen`, `hypo_alpeadriabank_international_ag`, `hypo_noe_lb_fur_niederosterreich_u_wien`, `hypo_oberosterreich_salzburg_steiermark`, `hypo_tirol_bank_ag`, `hypo_vorarlberg_bank_ag`, `hypo_bank_burgenland_aktiengesellschaft`, `marchfelder_bank`, `oberbank_ag`, `raiffeisen_bankengruppe_osterreich`, `schoellerbank_ag`, `sparda_bank_wien`, `volksbank_gruppe`, `volkskreditbank_ag`, or `vr_bank_braunau`.
        """

    class Fpx(StripeObject):
        account_holder_type: Optional[Literal["company", "individual"]]
        """
        Account holder type, if provided. Can be one of `individual` or `company`.
        """
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
        """
        The customer's bank, if provided. Can be one of `affin_bank`, `agrobank`, `alliance_bank`, `ambank`, `bank_islam`, `bank_muamalat`, `bank_rakyat`, `bsn`, `cimb`, `hong_leong_bank`, `hsbc`, `kfh`, `maybank2u`, `ocbc`, `public_bank`, `rhb`, `standard_chartered`, `uob`, `deutsche_bank`, `maybank2e`, `pb_enterprise`, or `bank_of_china`.
        """

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
                "nn",
                "rabobank",
                "regiobank",
                "revolut",
                "sns_bank",
                "triodos_bank",
                "van_lanschot",
                "yoursafe",
            ]
        ]
        """
        The customer's bank, if provided. Can be one of `abn_amro`, `asn_bank`, `bunq`, `handelsbanken`, `ing`, `knab`, `moneyou`, `n26`, `nn`, `rabobank`, `regiobank`, `revolut`, `sns_bank`, `triodos_bank`, `van_lanschot`, or `yoursafe`.
        """
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
                "NNBANL2G",
                "NTSBDEB1",
                "RABONL2U",
                "RBRBNL21",
                "REVOIE23",
                "REVOLT21",
                "SNSBNL2A",
                "TRIONL2U",
            ]
        ]
        """
        The Bank Identifier Code of the customer's bank, if the bank was provided.
        """

    class InteracPresent(StripeObject):
        class Networks(StripeObject):
            available: List[str]
            """
            All available networks for the card.
            """
            preferred: Optional[str]
            """
            The preferred network for the card.
            """

        brand: Optional[str]
        """
        Card brand. Can be `interac`, `mastercard` or `visa`.
        """
        cardholder_name: Optional[str]
        """
        The cardholder name as read from the card, in [ISO 7813](https://en.wikipedia.org/wiki/ISO/IEC_7813) format. May include alphanumeric characters, special characters and first/last name separator (`/`). In some cases, the cardholder name may not be available depending on how the issuer has configured the card. Cardholder name is typically not available on swipe or contactless payments, such as those made with Apple Pay and Google Pay.
        """
        country: Optional[str]
        """
        Two-letter ISO code representing the country of the card. You could use this attribute to get a sense of the international breakdown of cards you've collected.
        """
        description: Optional[str]
        """
        A high-level description of the type of cards issued in this range. (For internal use only and not typically available in standard API requests.)
        """
        exp_month: int
        """
        Two-digit number representing the card's expiration month.
        """
        exp_year: int
        """
        Four-digit number representing the card's expiration year.
        """
        fingerprint: Optional[str]
        """
        Uniquely identifies this particular card number. You can use this attribute to check whether two customers who've signed up with you are using the same card number, for example. For payment methods that tokenize card information (Apple Pay, Google Pay), the tokenized number might be provided instead of the underlying card number.

        *As of May 1, 2021, card fingerprint in India for Connect changed to allow two fingerprints for the same card---one for India and one for the rest of the world.*
        """
        funding: Optional[str]
        """
        Card funding type. Can be `credit`, `debit`, `prepaid`, or `unknown`.
        """
        iin: Optional[str]
        """
        Issuer identification number of the card. (For internal use only and not typically available in standard API requests.)
        """
        issuer: Optional[str]
        """
        The name of the card's issuing bank. (For internal use only and not typically available in standard API requests.)
        """
        last4: Optional[str]
        """
        The last four digits of the card.
        """
        networks: Optional[Networks]
        """
        Contains information about card networks that can be used to process the payment.
        """
        preferred_locales: Optional[List[str]]
        """
        EMV tag 5F2D. Preferred languages specified by the integrated circuit chip.
        """
        read_method: Optional[
            Literal[
                "contact_emv",
                "contactless_emv",
                "contactless_magstripe_mode",
                "magnetic_stripe_fallback",
                "magnetic_stripe_track2",
            ]
        ]
        """
        How card details were read in this transaction.
        """
        _inner_class_types = {"networks": Networks}

    class Klarna(StripeObject):
        class Dob(StripeObject):
            day: Optional[int]
            """
            The day of birth, between 1 and 31.
            """
            month: Optional[int]
            """
            The month of birth, between 1 and 12.
            """
            year: Optional[int]
            """
            The four-digit year of birth.
            """

        dob: Optional[Dob]
        """
        The customer's date of birth, if provided.
        """
        _inner_class_types = {"dob": Dob}

    class Konbini(StripeObject):
        pass

    class Link(StripeObject):
        email: Optional[str]
        """
        Account owner's email address.
        """
        persistent_token: Optional[str]
        """
        [Deprecated] This is a legacy parameter that no longer has any function.
        """

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
        """
        The customer's bank, if provided.
        """

    class Paynow(StripeObject):
        pass

    class Paypal(StripeObject):
        payer_email: Optional[str]
        """
        Owner's email. Values are provided by PayPal directly
        (if supported) at the time of authorization or settlement. They cannot be set or mutated.
        """
        payer_id: Optional[str]
        """
        PayPal account PayerID. This identifier uniquely identifies the PayPal customer.
        """

    class Pix(StripeObject):
        pass

    class Promptpay(StripeObject):
        pass

    class RadarOptions(StripeObject):
        session: Optional[str]
        """
        A [Radar Session](https://stripe.com/docs/radar/radar-session) is a snapshot of the browser metadata and device details that help Radar make more accurate predictions on your payments.
        """

    class RevolutPay(StripeObject):
        pass

    class SepaDebit(StripeObject):
        class GeneratedFrom(StripeObject):
            charge: Optional[ExpandableField["Charge"]]
            """
            The ID of the Charge that generated this PaymentMethod, if any.
            """
            setup_attempt: Optional[ExpandableField["SetupAttempt"]]
            """
            The ID of the SetupAttempt that generated this PaymentMethod, if any.
            """

        bank_code: Optional[str]
        """
        Bank code of bank associated with the bank account.
        """
        branch_code: Optional[str]
        """
        Branch code of bank associated with the bank account.
        """
        country: Optional[str]
        """
        Two-letter ISO code representing the country the bank account is located in.
        """
        fingerprint: Optional[str]
        """
        Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.
        """
        generated_from: Optional[GeneratedFrom]
        """
        Information about the object that generated this PaymentMethod.
        """
        last4: Optional[str]
        """
        Last four characters of the IBAN.
        """
        _inner_class_types = {"generated_from": GeneratedFrom}

    class Sofort(StripeObject):
        country: Optional[str]
        """
        Two-letter ISO code representing the country the bank account is located in.
        """

    class UsBankAccount(StripeObject):
        class Networks(StripeObject):
            preferred: Optional[str]
            """
            The preferred network.
            """
            supported: List[Literal["ach", "us_domestic_wire"]]
            """
            All supported networks.
            """

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
                """
                The ACH network code that resulted in this block.
                """
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
                """
                The reason why this PaymentMethod's fingerprint has been blocked
                """

            blocked: Optional[Blocked]
            _inner_class_types = {"blocked": Blocked}

        account_holder_type: Optional[Literal["company", "individual"]]
        """
        Account holder type: individual or company.
        """
        account_type: Optional[Literal["checking", "savings"]]
        """
        Account type: checkings or savings. Defaults to checking if omitted.
        """
        bank_name: Optional[str]
        """
        The name of the bank.
        """
        financial_connections_account: Optional[str]
        """
        The ID of the Financial Connections Account used to create the payment method.
        """
        fingerprint: Optional[str]
        """
        Uniquely identifies this particular bank account. You can use this attribute to check whether two bank accounts are the same.
        """
        last4: Optional[str]
        """
        Last four digits of the bank account number.
        """
        networks: Optional[Networks]
        """
        Contains information about US bank account networks that can be used.
        """
        routing_number: Optional[str]
        """
        Routing number of the bank account.
        """
        status_details: Optional[StatusDetails]
        """
        Contains information about the future reusability of this PaymentMethod.
        """
        _inner_class_types = {
            "networks": Networks,
            "status_details": StatusDetails,
        }

    class WechatPay(StripeObject):
        pass

    class Zip(StripeObject):
        pass

    class AttachParams(RequestOptions):
        customer: str
        """
        The ID of the customer to which to attach the PaymentMethod.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    class CreateParams(RequestOptions):
        acss_debit: NotRequired["PaymentMethod.CreateParamsAcssDebit"]
        """
        If this is an `acss_debit` PaymentMethod, this hash contains details about the ACSS Debit payment method.
        """
        affirm: NotRequired["PaymentMethod.CreateParamsAffirm"]
        """
        If this is an `affirm` PaymentMethod, this hash contains details about the Affirm payment method.
        """
        afterpay_clearpay: NotRequired[
            "PaymentMethod.CreateParamsAfterpayClearpay"
        ]
        """
        If this is an `AfterpayClearpay` PaymentMethod, this hash contains details about the AfterpayClearpay payment method.
        """
        alipay: NotRequired["PaymentMethod.CreateParamsAlipay"]
        """
        If this is an `Alipay` PaymentMethod, this hash contains details about the Alipay payment method.
        """
        au_becs_debit: NotRequired["PaymentMethod.CreateParamsAuBecsDebit"]
        """
        If this is an `au_becs_debit` PaymentMethod, this hash contains details about the bank account.
        """
        bacs_debit: NotRequired["PaymentMethod.CreateParamsBacsDebit"]
        """
        If this is a `bacs_debit` PaymentMethod, this hash contains details about the Bacs Direct Debit bank account.
        """
        bancontact: NotRequired["PaymentMethod.CreateParamsBancontact"]
        """
        If this is a `bancontact` PaymentMethod, this hash contains details about the Bancontact payment method.
        """
        billing_details: NotRequired[
            "PaymentMethod.CreateParamsBillingDetails"
        ]
        """
        Billing information associated with the PaymentMethod that may be used or required by particular types of payment methods.
        """
        blik: NotRequired["PaymentMethod.CreateParamsBlik"]
        """
        If this is a `blik` PaymentMethod, this hash contains details about the BLIK payment method.
        """
        boleto: NotRequired["PaymentMethod.CreateParamsBoleto"]
        """
        If this is a `boleto` PaymentMethod, this hash contains details about the Boleto payment method.
        """
        card: NotRequired["PaymentMethod.CreateParamsCard"]
        """
        If this is a `card` PaymentMethod, this hash contains the user's card details. For backwards compatibility, you can alternatively provide a Stripe token (e.g., for Apple Pay, Amex Express Checkout, or legacy Checkout) into the card hash with format `card: {token: "tok_visa"}`. When providing a card number, you must meet the requirements for [PCI compliance](https://stripe.com/docs/security#validating-pci-compliance). We strongly recommend using Stripe.js instead of interacting with this API directly.
        """
        cashapp: NotRequired["PaymentMethod.CreateParamsCashapp"]
        """
        If this is a `cashapp` PaymentMethod, this hash contains details about the Cash App Pay payment method.
        """
        customer: NotRequired["str"]
        """
        The `Customer` to whom the original PaymentMethod is attached.
        """
        customer_balance: NotRequired[
            "PaymentMethod.CreateParamsCustomerBalance"
        ]
        """
        If this is a `customer_balance` PaymentMethod, this hash contains details about the CustomerBalance payment method.
        """
        eps: NotRequired["PaymentMethod.CreateParamsEps"]
        """
        If this is an `eps` PaymentMethod, this hash contains details about the EPS payment method.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        fpx: NotRequired["PaymentMethod.CreateParamsFpx"]
        """
        If this is an `fpx` PaymentMethod, this hash contains details about the FPX payment method.
        """
        giropay: NotRequired["PaymentMethod.CreateParamsGiropay"]
        """
        If this is a `giropay` PaymentMethod, this hash contains details about the Giropay payment method.
        """
        grabpay: NotRequired["PaymentMethod.CreateParamsGrabpay"]
        """
        If this is a `grabpay` PaymentMethod, this hash contains details about the GrabPay payment method.
        """
        ideal: NotRequired["PaymentMethod.CreateParamsIdeal"]
        """
        If this is an `ideal` PaymentMethod, this hash contains details about the iDEAL payment method.
        """
        interac_present: NotRequired[
            "PaymentMethod.CreateParamsInteracPresent"
        ]
        """
        If this is an `interac_present` PaymentMethod, this hash contains details about the Interac Present payment method.
        """
        klarna: NotRequired["PaymentMethod.CreateParamsKlarna"]
        """
        If this is a `klarna` PaymentMethod, this hash contains details about the Klarna payment method.
        """
        konbini: NotRequired["PaymentMethod.CreateParamsKonbini"]
        """
        If this is a `konbini` PaymentMethod, this hash contains details about the Konbini payment method.
        """
        link: NotRequired["PaymentMethod.CreateParamsLink"]
        """
        If this is an `Link` PaymentMethod, this hash contains details about the Link payment method.
        """
        metadata: NotRequired["Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        oxxo: NotRequired["PaymentMethod.CreateParamsOxxo"]
        """
        If this is an `oxxo` PaymentMethod, this hash contains details about the OXXO payment method.
        """
        p24: NotRequired["PaymentMethod.CreateParamsP24"]
        """
        If this is a `p24` PaymentMethod, this hash contains details about the P24 payment method.
        """
        payment_method: NotRequired["str"]
        """
        The PaymentMethod to share.
        """
        paynow: NotRequired["PaymentMethod.CreateParamsPaynow"]
        """
        If this is a `paynow` PaymentMethod, this hash contains details about the PayNow payment method.
        """
        paypal: NotRequired["PaymentMethod.CreateParamsPaypal"]
        """
        If this is a `paypal` PaymentMethod, this hash contains details about the PayPal payment method.
        """
        pix: NotRequired["PaymentMethod.CreateParamsPix"]
        """
        If this is a `pix` PaymentMethod, this hash contains details about the Pix payment method.
        """
        promptpay: NotRequired["PaymentMethod.CreateParamsPromptpay"]
        """
        If this is a `promptpay` PaymentMethod, this hash contains details about the PromptPay payment method.
        """
        radar_options: NotRequired["PaymentMethod.CreateParamsRadarOptions"]
        """
        Options to configure Radar. See [Radar Session](https://stripe.com/docs/radar/radar-session) for more information.
        """
        revolut_pay: NotRequired["PaymentMethod.CreateParamsRevolutPay"]
        """
        If this is a `Revolut Pay` PaymentMethod, this hash contains details about the Revolut Pay payment method.
        """
        sepa_debit: NotRequired["PaymentMethod.CreateParamsSepaDebit"]
        """
        If this is a `sepa_debit` PaymentMethod, this hash contains details about the SEPA debit bank account.
        """
        sofort: NotRequired["PaymentMethod.CreateParamsSofort"]
        """
        If this is a `sofort` PaymentMethod, this hash contains details about the SOFORT payment method.
        """
        type: NotRequired[
            "Literal['acss_debit', 'affirm', 'afterpay_clearpay', 'alipay', 'au_becs_debit', 'bacs_debit', 'bancontact', 'blik', 'boleto', 'card', 'cashapp', 'customer_balance', 'eps', 'fpx', 'giropay', 'grabpay', 'ideal', 'klarna', 'konbini', 'link', 'oxxo', 'p24', 'paynow', 'paypal', 'pix', 'promptpay', 'revolut_pay', 'sepa_debit', 'sofort', 'us_bank_account', 'wechat_pay', 'zip']"
        ]
        """
        The type of the PaymentMethod. An additional hash is included on the PaymentMethod with a name matching this value. It contains additional information specific to the PaymentMethod type.
        """
        us_bank_account: NotRequired["PaymentMethod.CreateParamsUsBankAccount"]
        """
        If this is an `us_bank_account` PaymentMethod, this hash contains details about the US bank account payment method.
        """
        wechat_pay: NotRequired["PaymentMethod.CreateParamsWechatPay"]
        """
        If this is an `wechat_pay` PaymentMethod, this hash contains details about the wechat_pay payment method.
        """
        zip: NotRequired["PaymentMethod.CreateParamsZip"]
        """
        If this is a `zip` PaymentMethod, this hash contains details about the Zip payment method.
        """

    class CreateParamsAcssDebit(TypedDict):
        account_number: str
        """
        Customer's bank account number.
        """
        institution_number: str
        """
        Institution number of the customer's bank.
        """
        transit_number: str
        """
        Transit number of the customer's bank.
        """

    class CreateParamsAffirm(TypedDict):
        pass

    class CreateParamsAfterpayClearpay(TypedDict):
        pass

    class CreateParamsAlipay(TypedDict):
        pass

    class CreateParamsAuBecsDebit(TypedDict):
        account_number: str
        """
        The account number for the bank account.
        """
        bsb_number: str
        """
        Bank-State-Branch number of the bank account.
        """

    class CreateParamsBacsDebit(TypedDict):
        account_number: NotRequired["str"]
        """
        Account number of the bank account that the funds will be debited from.
        """
        sort_code: NotRequired["str"]
        """
        Sort code of the bank account. (e.g., `10-20-30`)
        """

    class CreateParamsBancontact(TypedDict):
        pass

    class CreateParamsBillingDetails(TypedDict):
        address: NotRequired[
            "Literal['']|PaymentMethod.CreateParamsBillingDetailsAddress"
        ]
        """
        Billing address.
        """
        email: NotRequired["Literal['']|str"]
        """
        Email address.
        """
        name: NotRequired["Literal['']|str"]
        """
        Full name.
        """
        phone: NotRequired["Literal['']|str"]
        """
        Billing phone number (including extension).
        """

    class CreateParamsBillingDetailsAddress(TypedDict):
        city: NotRequired["str"]
        """
        City, district, suburb, town, or village.
        """
        country: NotRequired["str"]
        """
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
        """
        line1: NotRequired["str"]
        """
        Address line 1 (e.g., street, PO Box, or company name).
        """
        line2: NotRequired["str"]
        """
        Address line 2 (e.g., apartment, suite, unit, or building).
        """
        postal_code: NotRequired["str"]
        """
        ZIP or postal code.
        """
        state: NotRequired["str"]
        """
        State, county, province, or region.
        """

    class CreateParamsBlik(TypedDict):
        pass

    class CreateParamsBoleto(TypedDict):
        tax_id: str
        """
        The tax ID of the customer (CPF for individual consumers or CNPJ for businesses consumers)
        """

    class CreateParamsCard(TypedDict):
        cvc: NotRequired["str"]
        """
        The card's CVC. It is highly recommended to always include this value.
        """
        exp_month: NotRequired["int"]
        """
        Two-digit number representing the card's expiration month.
        """
        exp_year: NotRequired["int"]
        """
        Four-digit number representing the card's expiration year.
        """
        number: NotRequired["str"]
        """
        The card number, as a string without any separators.
        """
        token: NotRequired["str"]
        """
        For backwards compatibility, you can alternatively provide a Stripe token (e.g., for Apple Pay, Amex Express Checkout, or legacy Checkout) into the card hash with format card: {token: "tok_visa"}.
        """

    class CreateParamsCashapp(TypedDict):
        pass

    class CreateParamsCustomerBalance(TypedDict):
        pass

    class CreateParamsEps(TypedDict):
        bank: NotRequired[
            "Literal['arzte_und_apotheker_bank', 'austrian_anadi_bank_ag', 'bank_austria', 'bankhaus_carl_spangler', 'bankhaus_schelhammer_und_schattera_ag', 'bawag_psk_ag', 'bks_bank_ag', 'brull_kallmus_bank_ag', 'btv_vier_lander_bank', 'capital_bank_grawe_gruppe_ag', 'deutsche_bank_ag', 'dolomitenbank', 'easybank_ag', 'erste_bank_und_sparkassen', 'hypo_alpeadriabank_international_ag', 'hypo_bank_burgenland_aktiengesellschaft', 'hypo_noe_lb_fur_niederosterreich_u_wien', 'hypo_oberosterreich_salzburg_steiermark', 'hypo_tirol_bank_ag', 'hypo_vorarlberg_bank_ag', 'marchfelder_bank', 'oberbank_ag', 'raiffeisen_bankengruppe_osterreich', 'schoellerbank_ag', 'sparda_bank_wien', 'volksbank_gruppe', 'volkskreditbank_ag', 'vr_bank_braunau']"
        ]
        """
        The customer's bank.
        """

    class CreateParamsFpx(TypedDict):
        account_holder_type: NotRequired["Literal['company', 'individual']"]
        """
        Account holder type for FPX transaction
        """
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
        """
        The customer's bank.
        """

    class CreateParamsGiropay(TypedDict):
        pass

    class CreateParamsGrabpay(TypedDict):
        pass

    class CreateParamsIdeal(TypedDict):
        bank: NotRequired[
            "Literal['abn_amro', 'asn_bank', 'bunq', 'handelsbanken', 'ing', 'knab', 'moneyou', 'n26', 'nn', 'rabobank', 'regiobank', 'revolut', 'sns_bank', 'triodos_bank', 'van_lanschot', 'yoursafe']"
        ]
        """
        The customer's bank.
        """

    class CreateParamsInteracPresent(TypedDict):
        pass

    class CreateParamsKlarna(TypedDict):
        dob: NotRequired["PaymentMethod.CreateParamsKlarnaDob"]
        """
        Customer's date of birth
        """

    class CreateParamsKlarnaDob(TypedDict):
        day: int
        """
        The day of birth, between 1 and 31.
        """
        month: int
        """
        The month of birth, between 1 and 12.
        """
        year: int
        """
        The four-digit year of birth.
        """

    class CreateParamsKonbini(TypedDict):
        pass

    class CreateParamsLink(TypedDict):
        pass

    class CreateParamsOxxo(TypedDict):
        pass

    class CreateParamsP24(TypedDict):
        bank: NotRequired[
            "Literal['alior_bank', 'bank_millennium', 'bank_nowy_bfg_sa', 'bank_pekao_sa', 'banki_spbdzielcze', 'blik', 'bnp_paribas', 'boz', 'citi_handlowy', 'credit_agricole', 'envelobank', 'etransfer_pocztowy24', 'getin_bank', 'ideabank', 'ing', 'inteligo', 'mbank_mtransfer', 'nest_przelew', 'noble_pay', 'pbac_z_ipko', 'plus_bank', 'santander_przelew24', 'tmobile_usbugi_bankowe', 'toyota_bank', 'volkswagen_bank']"
        ]
        """
        The customer's bank.
        """

    class CreateParamsPaynow(TypedDict):
        pass

    class CreateParamsPaypal(TypedDict):
        pass

    class CreateParamsPix(TypedDict):
        pass

    class CreateParamsPromptpay(TypedDict):
        pass

    class CreateParamsRadarOptions(TypedDict):
        session: NotRequired["str"]
        """
        A [Radar Session](https://stripe.com/docs/radar/radar-session) is a snapshot of the browser metadata and device details that help Radar make more accurate predictions on your payments.
        """

    class CreateParamsRevolutPay(TypedDict):
        pass

    class CreateParamsSepaDebit(TypedDict):
        iban: str
        """
        IBAN of the bank account.
        """

    class CreateParamsSofort(TypedDict):
        country: Literal["AT", "BE", "DE", "ES", "IT", "NL"]
        """
        Two-letter ISO code representing the country the bank account is located in.
        """

    class CreateParamsUsBankAccount(TypedDict):
        account_holder_type: NotRequired["Literal['company', 'individual']"]
        """
        Account holder type: individual or company.
        """
        account_number: NotRequired["str"]
        """
        Account number of the bank account.
        """
        account_type: NotRequired["Literal['checking', 'savings']"]
        """
        Account type: checkings or savings. Defaults to checking if omitted.
        """
        financial_connections_account: NotRequired["str"]
        """
        The ID of a Financial Connections Account to use as a payment method.
        """
        routing_number: NotRequired["str"]
        """
        Routing number of the bank account.
        """

    class CreateParamsWechatPay(TypedDict):
        pass

    class CreateParamsZip(TypedDict):
        pass

    class DetachParams(RequestOptions):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    class ListParams(RequestOptions):
        customer: NotRequired["str"]
        """
        The ID of the customer whose PaymentMethods will be retrieved.
        """
        ending_before: NotRequired["str"]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        limit: NotRequired["int"]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        starting_after: NotRequired["str"]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """
        type: NotRequired[
            "Literal['acss_debit', 'affirm', 'afterpay_clearpay', 'alipay', 'au_becs_debit', 'bacs_debit', 'bancontact', 'blik', 'boleto', 'card', 'cashapp', 'customer_balance', 'eps', 'fpx', 'giropay', 'grabpay', 'ideal', 'klarna', 'konbini', 'link', 'oxxo', 'p24', 'paynow', 'paypal', 'pix', 'promptpay', 'revolut_pay', 'sepa_debit', 'sofort', 'us_bank_account', 'wechat_pay', 'zip']"
        ]
        """
        An optional filter on the list, based on the object `type` field. Without the filter, the list includes all current and future payment method types. If your integration expects only one type of payment method in the response, make sure to provide a type value in the request.
        """

    class ModifyParams(RequestOptions):
        billing_details: NotRequired[
            "PaymentMethod.ModifyParamsBillingDetails"
        ]
        """
        Billing information associated with the PaymentMethod that may be used or required by particular types of payment methods.
        """
        card: NotRequired["PaymentMethod.ModifyParamsCard"]
        """
        If this is a `card` PaymentMethod, this hash contains the user's card details.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        link: NotRequired["PaymentMethod.ModifyParamsLink"]
        """
        If this is an `Link` PaymentMethod, this hash contains details about the Link payment method.
        """
        metadata: NotRequired["Literal['']|Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        us_bank_account: NotRequired["PaymentMethod.ModifyParamsUsBankAccount"]
        """
        If this is an `us_bank_account` PaymentMethod, this hash contains details about the US bank account payment method.
        """

    class ModifyParamsBillingDetails(TypedDict):
        address: NotRequired[
            "Literal['']|PaymentMethod.ModifyParamsBillingDetailsAddress"
        ]
        """
        Billing address.
        """
        email: NotRequired["Literal['']|str"]
        """
        Email address.
        """
        name: NotRequired["Literal['']|str"]
        """
        Full name.
        """
        phone: NotRequired["Literal['']|str"]
        """
        Billing phone number (including extension).
        """

    class ModifyParamsBillingDetailsAddress(TypedDict):
        city: NotRequired["str"]
        """
        City, district, suburb, town, or village.
        """
        country: NotRequired["str"]
        """
        Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
        """
        line1: NotRequired["str"]
        """
        Address line 1 (e.g., street, PO Box, or company name).
        """
        line2: NotRequired["str"]
        """
        Address line 2 (e.g., apartment, suite, unit, or building).
        """
        postal_code: NotRequired["str"]
        """
        ZIP or postal code.
        """
        state: NotRequired["str"]
        """
        State, county, province, or region.
        """

    class ModifyParamsCard(TypedDict):
        exp_month: NotRequired["int"]
        """
        Two-digit number representing the card's expiration month.
        """
        exp_year: NotRequired["int"]
        """
        Four-digit number representing the card's expiration year.
        """

    class ModifyParamsLink(TypedDict):
        pass

    class ModifyParamsUsBankAccount(TypedDict):
        account_holder_type: NotRequired["Literal['company', 'individual']"]
        """
        Bank account type.
        """

    class RetrieveParams(RequestOptions):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

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
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    customer: Optional[ExpandableField["Customer"]]
    """
    The ID of the Customer to which this PaymentMethod is saved. This will not be set when the PaymentMethod has not been saved to a Customer.
    """
    customer_balance: Optional[CustomerBalance]
    eps: Optional[Eps]
    fpx: Optional[Fpx]
    giropay: Optional[Giropay]
    grabpay: Optional[Grabpay]
    id: str
    """
    Unique identifier for the object.
    """
    ideal: Optional[Ideal]
    interac_present: Optional[InteracPresent]
    klarna: Optional[Klarna]
    konbini: Optional[Konbini]
    link: Optional[Link]
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Optional[Dict[str, str]]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["payment_method"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    oxxo: Optional[Oxxo]
    p24: Optional[P24]
    paynow: Optional[Paynow]
    paypal: Optional[Paypal]
    pix: Optional[Pix]
    promptpay: Optional[Promptpay]
    radar_options: Optional[RadarOptions]
    """
    Options to configure Radar. See [Radar Session](https://stripe.com/docs/radar/radar-session) for more information.
    """
    revolut_pay: Optional[RevolutPay]
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
        "revolut_pay",
        "sepa_debit",
        "sofort",
        "us_bank_account",
        "wechat_pay",
        "zip",
    ]
    """
    The type of the PaymentMethod. An additional hash is included on the PaymentMethod with a name matching this value. It contains additional information specific to the PaymentMethod type.
    """
    us_bank_account: Optional[UsBankAccount]
    wechat_pay: Optional[WechatPay]
    zip: Optional[Zip]

    @classmethod
    def _cls_attach(
        cls,
        payment_method: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack[
            "PaymentMethod.AttachParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "PaymentMethod":
        """
        Attaches a PaymentMethod object to a Customer.

        To attach a new PaymentMethod to a customer for future payments, we recommend you use a [SetupIntent](https://stripe.com/docs/api/setup_intents)
        or a PaymentIntent with [setup_future_usage](https://stripe.com/docs/api/payment_intents/create#create_payment_intent-setup_future_usage).
        These approaches will perform any necessary steps to set up the PaymentMethod for future payments. Using the /v1/payment_methods/:id/attach
        endpoint without first using a SetupIntent or PaymentIntent with setup_future_usage does not optimize the PaymentMethod for
        future use, which makes later declines and payment friction more likely.
        See [Optimizing cards for future payments](https://stripe.com/docs/payments/payment-intents#future-usage) for more information about setting up
        future payments.

        To use this PaymentMethod as the default for invoice or subscription payments,
        set [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/update#update_customer-invoice_settings-default_payment_method),
        on the Customer to the PaymentMethod's ID.
        """
        return cast(
            "PaymentMethod",
            cls._static_request(
                "post",
                "/v1/payment_methods/{payment_method}/attach".format(
                    payment_method=_util.sanitize_id(payment_method)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @overload
    @staticmethod
    def attach(
        payment_method: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack[
            "PaymentMethod.AttachParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "PaymentMethod":
        """
        Attaches a PaymentMethod object to a Customer.

        To attach a new PaymentMethod to a customer for future payments, we recommend you use a [SetupIntent](https://stripe.com/docs/api/setup_intents)
        or a PaymentIntent with [setup_future_usage](https://stripe.com/docs/api/payment_intents/create#create_payment_intent-setup_future_usage).
        These approaches will perform any necessary steps to set up the PaymentMethod for future payments. Using the /v1/payment_methods/:id/attach
        endpoint without first using a SetupIntent or PaymentIntent with setup_future_usage does not optimize the PaymentMethod for
        future use, which makes later declines and payment friction more likely.
        See [Optimizing cards for future payments](https://stripe.com/docs/payments/payment-intents#future-usage) for more information about setting up
        future payments.

        To use this PaymentMethod as the default for invoice or subscription payments,
        set [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/update#update_customer-invoice_settings-default_payment_method),
        on the Customer to the PaymentMethod's ID.
        """
        ...

    @overload
    def attach(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack[
            "PaymentMethod.AttachParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "PaymentMethod":
        """
        Attaches a PaymentMethod object to a Customer.

        To attach a new PaymentMethod to a customer for future payments, we recommend you use a [SetupIntent](https://stripe.com/docs/api/setup_intents)
        or a PaymentIntent with [setup_future_usage](https://stripe.com/docs/api/payment_intents/create#create_payment_intent-setup_future_usage).
        These approaches will perform any necessary steps to set up the PaymentMethod for future payments. Using the /v1/payment_methods/:id/attach
        endpoint without first using a SetupIntent or PaymentIntent with setup_future_usage does not optimize the PaymentMethod for
        future use, which makes later declines and payment friction more likely.
        See [Optimizing cards for future payments](https://stripe.com/docs/payments/payment-intents#future-usage) for more information about setting up
        future payments.

        To use this PaymentMethod as the default for invoice or subscription payments,
        set [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/update#update_customer-invoice_settings-default_payment_method),
        on the Customer to the PaymentMethod's ID.
        """
        ...

    @class_method_variant("_cls_attach")
    def attach(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack[
            "PaymentMethod.AttachParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "PaymentMethod":
        """
        Attaches a PaymentMethod object to a Customer.

        To attach a new PaymentMethod to a customer for future payments, we recommend you use a [SetupIntent](https://stripe.com/docs/api/setup_intents)
        or a PaymentIntent with [setup_future_usage](https://stripe.com/docs/api/payment_intents/create#create_payment_intent-setup_future_usage).
        These approaches will perform any necessary steps to set up the PaymentMethod for future payments. Using the /v1/payment_methods/:id/attach
        endpoint without first using a SetupIntent or PaymentIntent with setup_future_usage does not optimize the PaymentMethod for
        future use, which makes later declines and payment friction more likely.
        See [Optimizing cards for future payments](https://stripe.com/docs/payments/payment-intents#future-usage) for more information about setting up
        future payments.

        To use this PaymentMethod as the default for invoice or subscription payments,
        set [invoice_settings.default_payment_method](https://stripe.com/docs/api/customers/update#update_customer-invoice_settings-default_payment_method),
        on the Customer to the PaymentMethod's ID.
        """
        return cast(
            "PaymentMethod",
            self._request(
                "post",
                "/v1/payment_methods/{payment_method}/attach".format(
                    payment_method=_util.sanitize_id(self.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
        )

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack[
            "PaymentMethod.CreateParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "PaymentMethod":
        """
        Creates a PaymentMethod object. Read the [Stripe.js reference](https://stripe.com/docs/stripe-js/reference#stripe-create-payment-method) to learn how to create PaymentMethods via Stripe.js.

        Instead of creating a PaymentMethod directly, we recommend using the [PaymentIntents API to accept a payment immediately or the <a href="/docs/payments/save-and-reuse">SetupIntent](https://stripe.com/docs/payments/accept-a-payment) API to collect payment method details ahead of a future payment.
        """
        return cast(
            "PaymentMethod",
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
    def _cls_detach(
        cls,
        payment_method: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack[
            "PaymentMethod.DetachParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "PaymentMethod":
        """
        Detaches a PaymentMethod object from a Customer. After a PaymentMethod is detached, it can no longer be used for a payment or re-attached to a Customer.
        """
        return cast(
            "PaymentMethod",
            cls._static_request(
                "post",
                "/v1/payment_methods/{payment_method}/detach".format(
                    payment_method=_util.sanitize_id(payment_method)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @overload
    @staticmethod
    def detach(
        payment_method: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack[
            "PaymentMethod.DetachParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "PaymentMethod":
        """
        Detaches a PaymentMethod object from a Customer. After a PaymentMethod is detached, it can no longer be used for a payment or re-attached to a Customer.
        """
        ...

    @overload
    def detach(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack[
            "PaymentMethod.DetachParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "PaymentMethod":
        """
        Detaches a PaymentMethod object from a Customer. After a PaymentMethod is detached, it can no longer be used for a payment or re-attached to a Customer.
        """
        ...

    @class_method_variant("_cls_detach")
    def detach(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack[
            "PaymentMethod.DetachParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "PaymentMethod":
        """
        Detaches a PaymentMethod object from a Customer. After a PaymentMethod is detached, it can no longer be used for a payment or re-attached to a Customer.
        """
        return cast(
            "PaymentMethod",
            self._request(
                "post",
                "/v1/payment_methods/{payment_method}/detach".format(
                    payment_method=_util.sanitize_id(self.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
        )

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack[
            "PaymentMethod.ListParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> ListObject["PaymentMethod"]:
        """
        Returns a list of PaymentMethods for Treasury flows. If you want to list the PaymentMethods attached to a Customer for payments, you should use the [List a Customer's PaymentMethods](https://stripe.com/docs/api/payment_methods/customer_list) API instead.
        """
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
        cls, id: str, **params: Unpack["PaymentMethod.ModifyParams"]
    ) -> "PaymentMethod":
        """
        Updates a PaymentMethod object. A PaymentMethod must be attached a customer to be updated.
        """
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "PaymentMethod",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["PaymentMethod.RetrieveParams"]
    ) -> "PaymentMethod":
        """
        Retrieves a PaymentMethod object attached to the StripeAccount. To retrieve a payment method attached to a Customer, you should use [Retrieve a Customer's PaymentMethods](https://stripe.com/docs/api/payment_methods/customer)
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

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
        "radar_options": RadarOptions,
        "revolut_pay": RevolutPay,
        "sepa_debit": SepaDebit,
        "sofort": Sofort,
        "us_bank_account": UsBankAccount,
        "wechat_pay": WechatPay,
        "zip": Zip,
    }
