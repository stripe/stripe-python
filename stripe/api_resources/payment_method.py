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
from stripe.util import class_method_variant
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
    from stripe.api_resources.customer import Customer


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
    if TYPE_CHECKING:

        class AttachParams(RequestOptions):
            customer: str
            """
            The ID of the customer to which to attach the PaymentMethod.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

        class CreateParams(RequestOptions):
            acss_debit: NotRequired["PaymentMethod.CreateParamsAcssDebit|None"]
            """
            If this is an `acss_debit` PaymentMethod, this hash contains details about the ACSS Debit payment method.
            """
            affirm: NotRequired["PaymentMethod.CreateParamsAffirm|None"]
            """
            If this is an `affirm` PaymentMethod, this hash contains details about the Affirm payment method.
            """
            afterpay_clearpay: NotRequired[
                "PaymentMethod.CreateParamsAfterpayClearpay|None"
            ]
            """
            If this is an `AfterpayClearpay` PaymentMethod, this hash contains details about the AfterpayClearpay payment method.
            """
            alipay: NotRequired["PaymentMethod.CreateParamsAlipay|None"]
            """
            If this is an `Alipay` PaymentMethod, this hash contains details about the Alipay payment method.
            """
            au_becs_debit: NotRequired[
                "PaymentMethod.CreateParamsAuBecsDebit|None"
            ]
            """
            If this is an `au_becs_debit` PaymentMethod, this hash contains details about the bank account.
            """
            bacs_debit: NotRequired["PaymentMethod.CreateParamsBacsDebit|None"]
            """
            If this is a `bacs_debit` PaymentMethod, this hash contains details about the Bacs Direct Debit bank account.
            """
            bancontact: NotRequired[
                "PaymentMethod.CreateParamsBancontact|None"
            ]
            """
            If this is a `bancontact` PaymentMethod, this hash contains details about the Bancontact payment method.
            """
            billing_details: NotRequired[
                "PaymentMethod.CreateParamsBillingDetails|None"
            ]
            """
            Billing information associated with the PaymentMethod that may be used or required by particular types of payment methods.
            """
            blik: NotRequired["PaymentMethod.CreateParamsBlik|None"]
            """
            If this is a `blik` PaymentMethod, this hash contains details about the BLIK payment method.
            """
            boleto: NotRequired["PaymentMethod.CreateParamsBoleto|None"]
            """
            If this is a `boleto` PaymentMethod, this hash contains details about the Boleto payment method.
            """
            card: NotRequired[
                "PaymentMethod.CreateParamsCard|PaymentMethod.CreateParamsCard2|None"
            ]
            """
            If this is a `card` PaymentMethod, this hash contains the user's card details. For backwards compatibility, you can alternatively provide a Stripe token (e.g., for Apple Pay, Amex Express Checkout, or legacy Checkout) into the card hash with format `card: {token: "tok_visa"}`. When providing a card number, you must meet the requirements for [PCI compliance](https://stripe.com/docs/security#validating-pci-compliance). We strongly recommend using Stripe.js instead of interacting with this API directly.
            """
            cashapp: NotRequired["PaymentMethod.CreateParamsCashapp|None"]
            """
            If this is a `cashapp` PaymentMethod, this hash contains details about the Cash App Pay payment method.
            """
            customer: NotRequired["str|None"]
            """
            The `Customer` to whom the original PaymentMethod is attached.
            """
            customer_balance: NotRequired[
                "PaymentMethod.CreateParamsCustomerBalance|None"
            ]
            """
            If this is a `customer_balance` PaymentMethod, this hash contains details about the CustomerBalance payment method.
            """
            eps: NotRequired["PaymentMethod.CreateParamsEps|None"]
            """
            If this is an `eps` PaymentMethod, this hash contains details about the EPS payment method.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            fpx: NotRequired["PaymentMethod.CreateParamsFpx|None"]
            """
            If this is an `fpx` PaymentMethod, this hash contains details about the FPX payment method.
            """
            giropay: NotRequired["PaymentMethod.CreateParamsGiropay|None"]
            """
            If this is a `giropay` PaymentMethod, this hash contains details about the Giropay payment method.
            """
            grabpay: NotRequired["PaymentMethod.CreateParamsGrabpay|None"]
            """
            If this is a `grabpay` PaymentMethod, this hash contains details about the GrabPay payment method.
            """
            ideal: NotRequired["PaymentMethod.CreateParamsIdeal|None"]
            """
            If this is an `ideal` PaymentMethod, this hash contains details about the iDEAL payment method.
            """
            interac_present: NotRequired[
                "PaymentMethod.CreateParamsInteracPresent|None"
            ]
            """
            If this is an `interac_present` PaymentMethod, this hash contains details about the Interac Present payment method.
            """
            klarna: NotRequired["PaymentMethod.CreateParamsKlarna|None"]
            """
            If this is a `klarna` PaymentMethod, this hash contains details about the Klarna payment method.
            """
            konbini: NotRequired["PaymentMethod.CreateParamsKonbini|None"]
            """
            If this is a `konbini` PaymentMethod, this hash contains details about the Konbini payment method.
            """
            link: NotRequired["PaymentMethod.CreateParamsLink|None"]
            """
            If this is an `Link` PaymentMethod, this hash contains details about the Link payment method.
            """
            metadata: NotRequired["Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """
            oxxo: NotRequired["PaymentMethod.CreateParamsOxxo|None"]
            """
            If this is an `oxxo` PaymentMethod, this hash contains details about the OXXO payment method.
            """
            p24: NotRequired["PaymentMethod.CreateParamsP24|None"]
            """
            If this is a `p24` PaymentMethod, this hash contains details about the P24 payment method.
            """
            payment_method: NotRequired["str|None"]
            """
            The PaymentMethod to share.
            """
            paynow: NotRequired["PaymentMethod.CreateParamsPaynow|None"]
            """
            If this is a `paynow` PaymentMethod, this hash contains details about the PayNow payment method.
            """
            paypal: NotRequired["PaymentMethod.CreateParamsPaypal|None"]
            """
            If this is a `paypal` PaymentMethod, this hash contains details about the PayPal payment method.
            """
            pix: NotRequired["PaymentMethod.CreateParamsPix|None"]
            """
            If this is a `pix` PaymentMethod, this hash contains details about the Pix payment method.
            """
            promptpay: NotRequired["PaymentMethod.CreateParamsPromptpay|None"]
            """
            If this is a `promptpay` PaymentMethod, this hash contains details about the PromptPay payment method.
            """
            radar_options: NotRequired[
                "PaymentMethod.CreateParamsRadarOptions|None"
            ]
            """
            Options to configure Radar. See [Radar Session](https://stripe.com/docs/radar/radar-session) for more information.
            """
            sepa_debit: NotRequired["PaymentMethod.CreateParamsSepaDebit|None"]
            """
            If this is a `sepa_debit` PaymentMethod, this hash contains details about the SEPA debit bank account.
            """
            sofort: NotRequired["PaymentMethod.CreateParamsSofort|None"]
            """
            If this is a `sofort` PaymentMethod, this hash contains details about the SOFORT payment method.
            """
            type: NotRequired[
                "Literal['acss_debit', 'affirm', 'afterpay_clearpay', 'alipay', 'au_becs_debit', 'bacs_debit', 'bancontact', 'blik', 'boleto', 'card', 'cashapp', 'customer_balance', 'eps', 'fpx', 'giropay', 'grabpay', 'ideal', 'klarna', 'konbini', 'link', 'oxxo', 'p24', 'paynow', 'paypal', 'pix', 'promptpay', 'sepa_debit', 'sofort', 'us_bank_account', 'wechat_pay', 'zip']|None"
            ]
            """
            The type of the PaymentMethod. An additional hash is included on the PaymentMethod with a name matching this value. It contains additional information specific to the PaymentMethod type.
            """
            us_bank_account: NotRequired[
                "PaymentMethod.CreateParamsUsBankAccount|None"
            ]
            """
            If this is an `us_bank_account` PaymentMethod, this hash contains details about the US bank account payment method.
            """
            wechat_pay: NotRequired["PaymentMethod.CreateParamsWechatPay|None"]
            """
            If this is an `wechat_pay` PaymentMethod, this hash contains details about the wechat_pay payment method.
            """
            zip: NotRequired["PaymentMethod.CreateParamsZip|None"]
            """
            If this is a `zip` PaymentMethod, this hash contains details about the Zip payment method.
            """

        class CreateParamsZip(TypedDict):
            pass

        class CreateParamsWechatPay(TypedDict):
            pass

        class CreateParamsUsBankAccount(TypedDict):
            account_holder_type: NotRequired[
                "Literal['company', 'individual']|None"
            ]
            """
            Account holder type: individual or company.
            """
            account_number: NotRequired["str|None"]
            """
            Account number of the bank account.
            """
            account_type: NotRequired["Literal['checking', 'savings']|None"]
            """
            Account type: checkings or savings. Defaults to checking if omitted.
            """
            financial_connections_account: NotRequired["str|None"]
            """
            The ID of a Financial Connections Account to use as a payment method.
            """
            routing_number: NotRequired["str|None"]
            """
            Routing number of the bank account.
            """

        class CreateParamsSofort(TypedDict):
            country: Literal["AT", "BE", "DE", "ES", "IT", "NL"]
            """
            Two-letter ISO code representing the country the bank account is located in.
            """

        class CreateParamsSepaDebit(TypedDict):
            iban: str
            """
            IBAN of the bank account.
            """

        class CreateParamsRadarOptions(TypedDict):
            session: NotRequired["str|None"]
            """
            A [Radar Session](https://stripe.com/docs/radar/radar-session) is a snapshot of the browser metadata and device details that help Radar make more accurate predictions on your payments.
            """

        class CreateParamsPromptpay(TypedDict):
            pass

        class CreateParamsPix(TypedDict):
            pass

        class CreateParamsPaypal(TypedDict):
            pass

        class CreateParamsPaynow(TypedDict):
            pass

        class CreateParamsP24(TypedDict):
            bank: NotRequired[
                "Literal['alior_bank', 'bank_millennium', 'bank_nowy_bfg_sa', 'bank_pekao_sa', 'banki_spbdzielcze', 'blik', 'bnp_paribas', 'boz', 'citi_handlowy', 'credit_agricole', 'envelobank', 'etransfer_pocztowy24', 'getin_bank', 'ideabank', 'ing', 'inteligo', 'mbank_mtransfer', 'nest_przelew', 'noble_pay', 'pbac_z_ipko', 'plus_bank', 'santander_przelew24', 'tmobile_usbugi_bankowe', 'toyota_bank', 'volkswagen_bank']|None"
            ]
            """
            The customer's bank.
            """

        class CreateParamsOxxo(TypedDict):
            pass

        class CreateParamsLink(TypedDict):
            pass

        class CreateParamsKonbini(TypedDict):
            pass

        class CreateParamsKlarna(TypedDict):
            dob: NotRequired["PaymentMethod.CreateParamsKlarnaDob|None"]
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

        class CreateParamsInteracPresent(TypedDict):
            pass

        class CreateParamsIdeal(TypedDict):
            bank: NotRequired[
                "Literal['abn_amro', 'asn_bank', 'bunq', 'handelsbanken', 'ing', 'knab', 'moneyou', 'n26', 'rabobank', 'regiobank', 'revolut', 'sns_bank', 'triodos_bank', 'van_lanschot', 'yoursafe']|None"
            ]
            """
            The customer's bank.
            """

        class CreateParamsGrabpay(TypedDict):
            pass

        class CreateParamsGiropay(TypedDict):
            pass

        class CreateParamsFpx(TypedDict):
            account_holder_type: NotRequired[
                "Literal['company', 'individual']|None"
            ]
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

        class CreateParamsEps(TypedDict):
            bank: NotRequired[
                "Literal['arzte_und_apotheker_bank', 'austrian_anadi_bank_ag', 'bank_austria', 'bankhaus_carl_spangler', 'bankhaus_schelhammer_und_schattera_ag', 'bawag_psk_ag', 'bks_bank_ag', 'brull_kallmus_bank_ag', 'btv_vier_lander_bank', 'capital_bank_grawe_gruppe_ag', 'deutsche_bank_ag', 'dolomitenbank', 'easybank_ag', 'erste_bank_und_sparkassen', 'hypo_alpeadriabank_international_ag', 'hypo_bank_burgenland_aktiengesellschaft', 'hypo_noe_lb_fur_niederosterreich_u_wien', 'hypo_oberosterreich_salzburg_steiermark', 'hypo_tirol_bank_ag', 'hypo_vorarlberg_bank_ag', 'marchfelder_bank', 'oberbank_ag', 'raiffeisen_bankengruppe_osterreich', 'schoellerbank_ag', 'sparda_bank_wien', 'volksbank_gruppe', 'volkskreditbank_ag', 'vr_bank_braunau']|None"
            ]
            """
            The customer's bank.
            """

        class CreateParamsCustomerBalance(TypedDict):
            pass

        class CreateParamsCashapp(TypedDict):
            pass

        class CreateParamsCard2(TypedDict):
            token: str
            """
            For backwards compatibility, you can alternatively provide a Stripe token (e.g., for Apple Pay, Amex Express Checkout, or legacy Checkout) into the card hash with format card: {token: "tok_visa"}.
            """

        class CreateParamsCard(TypedDict):
            cvc: NotRequired["str|None"]
            """
            The card's CVC. It is highly recommended to always include this value.
            """
            exp_month: int
            """
            Two-digit number representing the card's expiration month.
            """
            exp_year: int
            """
            Four-digit number representing the card's expiration year.
            """
            number: str
            """
            The card number, as a string without any separators.
            """

        class CreateParamsBoleto(TypedDict):
            tax_id: str
            """
            The tax ID of the customer (CPF for individual consumers or CNPJ for businesses consumers)
            """

        class CreateParamsBlik(TypedDict):
            pass

        class CreateParamsBillingDetails(TypedDict):
            address: NotRequired[
                "Literal['']|PaymentMethod.CreateParamsBillingDetailsAddress|None"
            ]
            """
            Billing address.
            """
            email: NotRequired["Literal['']|str|None"]
            """
            Email address.
            """
            name: NotRequired["Literal['']|str|None"]
            """
            Full name.
            """
            phone: NotRequired["Literal['']|str|None"]
            """
            Billing phone number (including extension).
            """

        class CreateParamsBillingDetailsAddress(TypedDict):
            city: NotRequired["str|None"]
            """
            City, district, suburb, town, or village.
            """
            country: NotRequired["str|None"]
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            line1: NotRequired["str|None"]
            """
            Address line 1 (e.g., street, PO Box, or company name).
            """
            line2: NotRequired["str|None"]
            """
            Address line 2 (e.g., apartment, suite, unit, or building).
            """
            postal_code: NotRequired["str|None"]
            """
            ZIP or postal code.
            """
            state: NotRequired["str|None"]
            """
            State, county, province, or region.
            """

        class CreateParamsBancontact(TypedDict):
            pass

        class CreateParamsBacsDebit(TypedDict):
            account_number: NotRequired["str|None"]
            """
            Account number of the bank account that the funds will be debited from.
            """
            sort_code: NotRequired["str|None"]
            """
            Sort code of the bank account. (e.g., `10-20-30`)
            """

        class CreateParamsAuBecsDebit(TypedDict):
            account_number: str
            """
            The account number for the bank account.
            """
            bsb_number: str
            """
            Bank-State-Branch number of the bank account.
            """

        class CreateParamsAlipay(TypedDict):
            pass

        class CreateParamsAfterpayClearpay(TypedDict):
            pass

        class CreateParamsAffirm(TypedDict):
            pass

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

        class DetachParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

        class ListParams(RequestOptions):
            customer: NotRequired["str|None"]
            """
            The ID of the customer whose PaymentMethods will be retrieved.
            """
            ending_before: NotRequired["str|None"]
            """
            A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            limit: NotRequired["int|None"]
            """
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            """
            starting_after: NotRequired["str|None"]
            """
            A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            """
            type: NotRequired[
                "Literal['acss_debit', 'affirm', 'afterpay_clearpay', 'alipay', 'au_becs_debit', 'bacs_debit', 'bancontact', 'blik', 'boleto', 'card', 'cashapp', 'customer_balance', 'eps', 'fpx', 'giropay', 'grabpay', 'ideal', 'klarna', 'konbini', 'link', 'oxxo', 'p24', 'paynow', 'paypal', 'pix', 'promptpay', 'sepa_debit', 'sofort', 'us_bank_account', 'wechat_pay', 'zip']|None"
            ]
            """
            An optional filter on the list, based on the object `type` field. Without the filter, the list includes all current and future payment method types. If your integration expects only one type of payment method in the response, make sure to provide a type value in the request.
            """

        class ModifyParams(RequestOptions):
            billing_details: NotRequired[
                "PaymentMethod.ModifyParamsBillingDetails|None"
            ]
            """
            Billing information associated with the PaymentMethod that may be used or required by particular types of payment methods.
            """
            card: NotRequired["PaymentMethod.ModifyParamsCard|None"]
            """
            If this is a `card` PaymentMethod, this hash contains the user's card details.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            link: NotRequired["PaymentMethod.ModifyParamsLink|None"]
            """
            If this is an `Link` PaymentMethod, this hash contains details about the Link payment method.
            """
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """
            us_bank_account: NotRequired[
                "PaymentMethod.ModifyParamsUsBankAccount|None"
            ]
            """
            If this is an `us_bank_account` PaymentMethod, this hash contains details about the US bank account payment method.
            """

        class ModifyParamsUsBankAccount(TypedDict):
            account_holder_type: NotRequired[
                "Literal['company', 'individual']|None"
            ]
            """
            Bank account type.
            """

        class ModifyParamsLink(TypedDict):
            pass

        class ModifyParamsCard(TypedDict):
            exp_month: NotRequired["int|None"]
            """
            Two-digit number representing the card's expiration month.
            """
            exp_year: NotRequired["int|None"]
            """
            Four-digit number representing the card's expiration year.
            """

        class ModifyParamsBillingDetails(TypedDict):
            address: NotRequired[
                "Literal['']|PaymentMethod.ModifyParamsBillingDetailsAddress|None"
            ]
            """
            Billing address.
            """
            email: NotRequired["Literal['']|str|None"]
            """
            Email address.
            """
            name: NotRequired["Literal['']|str|None"]
            """
            Full name.
            """
            phone: NotRequired["Literal['']|str|None"]
            """
            Billing phone number (including extension).
            """

        class ModifyParamsBillingDetailsAddress(TypedDict):
            city: NotRequired["str|None"]
            """
            City, district, suburb, town, or village.
            """
            country: NotRequired["str|None"]
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            line1: NotRequired["str|None"]
            """
            Address line 1 (e.g., street, PO Box, or company name).
            """
            line2: NotRequired["str|None"]
            """
            Address line 2 (e.g., apartment, suite, unit, or building).
            """
            postal_code: NotRequired["str|None"]
            """
            ZIP or postal code.
            """
            state: NotRequired["str|None"]
            """
            State, county, province, or region.
            """

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

    acss_debit: Optional[StripeObject]
    affirm: Optional[StripeObject]
    afterpay_clearpay: Optional[StripeObject]
    alipay: Optional[StripeObject]
    au_becs_debit: Optional[StripeObject]
    bacs_debit: Optional[StripeObject]
    bancontact: Optional[StripeObject]
    billing_details: StripeObject
    blik: Optional[StripeObject]
    boleto: Optional[StripeObject]
    card: Optional[StripeObject]
    card_present: Optional[StripeObject]
    cashapp: Optional[StripeObject]
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    customer: Optional[ExpandableField["Customer"]]
    """
    The ID of the Customer to which this PaymentMethod is saved. This will not be set when the PaymentMethod has not been saved to a Customer.
    """
    customer_balance: Optional[StripeObject]
    eps: Optional[StripeObject]
    fpx: Optional[StripeObject]
    giropay: Optional[StripeObject]
    grabpay: Optional[StripeObject]
    id: str
    """
    Unique identifier for the object.
    """
    ideal: Optional[StripeObject]
    interac_present: Optional[StripeObject]
    klarna: Optional[StripeObject]
    konbini: Optional[StripeObject]
    link: Optional[StripeObject]
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
    oxxo: Optional[StripeObject]
    p24: Optional[StripeObject]
    paynow: Optional[StripeObject]
    paypal: Optional[StripeObject]
    pix: Optional[StripeObject]
    promptpay: Optional[StripeObject]
    radar_options: Optional[StripeObject]
    """
    Options to configure Radar. See [Radar Session](https://stripe.com/docs/radar/radar-session) for more information.
    """
    sepa_debit: Optional[StripeObject]
    sofort: Optional[StripeObject]
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
    """
    The type of the PaymentMethod. An additional hash is included on the PaymentMethod with a name matching this value. It contains additional information specific to the PaymentMethod type.
    """
    us_bank_account: Optional[StripeObject]
    wechat_pay: Optional[StripeObject]
    zip: Optional[StripeObject]

    @classmethod
    def _cls_attach(
        cls,
        payment_method: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["PaymentMethod.AttachParams"]
    ) -> "PaymentMethod":
        return cast(
            "PaymentMethod",
            cls._static_request(
                "post",
                "/v1/payment_methods/{payment_method}/attach".format(
                    payment_method=util.sanitize_id(payment_method)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @overload
    @classmethod
    def attach(
        cls,
        payment_method: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["PaymentMethod.AttachParams"]
    ) -> "PaymentMethod":
        ...

    @overload
    def attach(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["PaymentMethod.AttachParams"]
    ) -> "PaymentMethod":
        ...

    @class_method_variant("_cls_attach")
    def attach(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["PaymentMethod.AttachParams"]
    ) -> "PaymentMethod":
        return cast(
            "PaymentMethod",
            self._request(
                "post",
                "/v1/payment_methods/{payment_method}/attach".format(
                    payment_method=util.sanitize_id(self.get("id"))
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
        **params: Unpack["PaymentMethod.CreateParams"]
    ) -> "PaymentMethod":
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
        **params: Unpack["PaymentMethod.DetachParams"]
    ) -> "PaymentMethod":
        return cast(
            "PaymentMethod",
            cls._static_request(
                "post",
                "/v1/payment_methods/{payment_method}/detach".format(
                    payment_method=util.sanitize_id(payment_method)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @overload
    @classmethod
    def detach(
        cls,
        payment_method: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["PaymentMethod.DetachParams"]
    ) -> "PaymentMethod":
        ...

    @overload
    def detach(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["PaymentMethod.DetachParams"]
    ) -> "PaymentMethod":
        ...

    @class_method_variant("_cls_detach")
    def detach(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["PaymentMethod.DetachParams"]
    ) -> "PaymentMethod":
        return cast(
            "PaymentMethod",
            self._request(
                "post",
                "/v1/payment_methods/{payment_method}/detach".format(
                    payment_method=util.sanitize_id(self.get("id"))
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
        **params: Unpack["PaymentMethod.ListParams"]
    ) -> ListObject["PaymentMethod"]:
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
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "PaymentMethod",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["PaymentMethod.RetrieveParams"]
    ) -> "PaymentMethod":
        instance = cls(id, **params)
        instance.refresh()
        return instance
