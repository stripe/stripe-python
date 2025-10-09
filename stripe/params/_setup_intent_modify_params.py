# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import Dict, List
from typing_extensions import Literal, NotRequired, TypedDict


class SetupIntentModifyParams(RequestOptions):
    attach_to_self: NotRequired[bool]
    """
    If present, the SetupIntent's payment method will be attached to the in-context Stripe Account.

    It can only be used for this Stripe Account's own money movement flows like InboundTransfer and OutboundTransfers. It cannot be set to true when setting up a PaymentMethod for a Customer, and defaults to false when attaching a PaymentMethod to a Customer.
    """
    customer: NotRequired[str]
    """
    ID of the Customer this SetupIntent belongs to, if one exists.

    If present, the SetupIntent's payment method will be attached to the Customer on successful setup. Payment methods attached to other Customers cannot be used with this SetupIntent.
    """
    customer_account: NotRequired[str]
    """
    ID of the Account this SetupIntent belongs to, if one exists.

    If present, the SetupIntent's payment method will be attached to the Account on successful setup. Payment methods attached to other Accounts cannot be used with this SetupIntent.
    """
    description: NotRequired[str]
    """
    An arbitrary string attached to the object. Often useful for displaying to users.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    flow_directions: NotRequired[List[Literal["inbound", "outbound"]]]
    """
    Indicates the directions of money movement for which this payment method is intended to be used.

    Include `inbound` if you intend to use the payment method as the origin to pull funds from. Include `outbound` if you intend to use the payment method as the destination to send funds to. You can include both if you intend to use the payment method for both purposes.
    """
    metadata: NotRequired["Literal['']|Dict[str, str]"]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """
    payment_method: NotRequired[str]
    """
    ID of the payment method (a PaymentMethod, Card, or saved Source object) to attach to this SetupIntent. To unset this field to null, pass in an empty string.
    """
    payment_method_configuration: NotRequired[str]
    """
    The ID of the [payment method configuration](https://stripe.com/docs/api/payment_method_configurations) to use with this SetupIntent.
    """
    payment_method_data: NotRequired[
        "SetupIntentModifyParamsPaymentMethodData"
    ]
    """
    When included, this hash creates a PaymentMethod that is set as the [`payment_method`](https://stripe.com/docs/api/setup_intents/object#setup_intent_object-payment_method)
    value in the SetupIntent.
    """
    payment_method_options: NotRequired[
        "SetupIntentModifyParamsPaymentMethodOptions"
    ]
    """
    Payment method-specific configuration for this SetupIntent.
    """
    payment_method_types: NotRequired[List[str]]
    """
    The list of payment method types (for example, card) that this SetupIntent can set up. If you don't provide this, Stripe will dynamically show relevant payment methods from your [payment method settings](https://dashboard.stripe.com/settings/payment_methods). A list of valid payment method types can be found [here](https://docs.stripe.com/api/payment_methods/object#payment_method_object-type).
    """
    setup_details: NotRequired["SetupIntentModifyParamsSetupDetails"]
    """
    Provides industry-specific information about the SetupIntent.
    """


class SetupIntentModifyParamsPaymentMethodData(TypedDict):
    acss_debit: NotRequired[
        "SetupIntentModifyParamsPaymentMethodDataAcssDebit"
    ]
    """
    If this is an `acss_debit` PaymentMethod, this hash contains details about the ACSS Debit payment method.
    """
    affirm: NotRequired["SetupIntentModifyParamsPaymentMethodDataAffirm"]
    """
    If this is an `affirm` PaymentMethod, this hash contains details about the Affirm payment method.
    """
    afterpay_clearpay: NotRequired[
        "SetupIntentModifyParamsPaymentMethodDataAfterpayClearpay"
    ]
    """
    If this is an `AfterpayClearpay` PaymentMethod, this hash contains details about the AfterpayClearpay payment method.
    """
    alipay: NotRequired["SetupIntentModifyParamsPaymentMethodDataAlipay"]
    """
    If this is an `Alipay` PaymentMethod, this hash contains details about the Alipay payment method.
    """
    allow_redisplay: NotRequired[Literal["always", "limited", "unspecified"]]
    """
    This field indicates whether this payment method can be shown again to its customer in a checkout flow. Stripe products such as Checkout and Elements use this field to determine whether a payment method can be shown as a saved payment method in a checkout flow. The field defaults to `unspecified`.
    """
    alma: NotRequired["SetupIntentModifyParamsPaymentMethodDataAlma"]
    """
    If this is a Alma PaymentMethod, this hash contains details about the Alma payment method.
    """
    amazon_pay: NotRequired[
        "SetupIntentModifyParamsPaymentMethodDataAmazonPay"
    ]
    """
    If this is a AmazonPay PaymentMethod, this hash contains details about the AmazonPay payment method.
    """
    au_becs_debit: NotRequired[
        "SetupIntentModifyParamsPaymentMethodDataAuBecsDebit"
    ]
    """
    If this is an `au_becs_debit` PaymentMethod, this hash contains details about the bank account.
    """
    bacs_debit: NotRequired[
        "SetupIntentModifyParamsPaymentMethodDataBacsDebit"
    ]
    """
    If this is a `bacs_debit` PaymentMethod, this hash contains details about the Bacs Direct Debit bank account.
    """
    bancontact: NotRequired[
        "SetupIntentModifyParamsPaymentMethodDataBancontact"
    ]
    """
    If this is a `bancontact` PaymentMethod, this hash contains details about the Bancontact payment method.
    """
    billie: NotRequired["SetupIntentModifyParamsPaymentMethodDataBillie"]
    """
    If this is a `billie` PaymentMethod, this hash contains details about the Billie payment method.
    """
    billing_details: NotRequired[
        "SetupIntentModifyParamsPaymentMethodDataBillingDetails"
    ]
    """
    Billing information associated with the PaymentMethod that may be used or required by particular types of payment methods.
    """
    blik: NotRequired["SetupIntentModifyParamsPaymentMethodDataBlik"]
    """
    If this is a `blik` PaymentMethod, this hash contains details about the BLIK payment method.
    """
    boleto: NotRequired["SetupIntentModifyParamsPaymentMethodDataBoleto"]
    """
    If this is a `boleto` PaymentMethod, this hash contains details about the Boleto payment method.
    """
    cashapp: NotRequired["SetupIntentModifyParamsPaymentMethodDataCashapp"]
    """
    If this is a `cashapp` PaymentMethod, this hash contains details about the Cash App Pay payment method.
    """
    crypto: NotRequired["SetupIntentModifyParamsPaymentMethodDataCrypto"]
    """
    If this is a Crypto PaymentMethod, this hash contains details about the Crypto payment method.
    """
    customer_balance: NotRequired[
        "SetupIntentModifyParamsPaymentMethodDataCustomerBalance"
    ]
    """
    If this is a `customer_balance` PaymentMethod, this hash contains details about the CustomerBalance payment method.
    """
    eps: NotRequired["SetupIntentModifyParamsPaymentMethodDataEps"]
    """
    If this is an `eps` PaymentMethod, this hash contains details about the EPS payment method.
    """
    fpx: NotRequired["SetupIntentModifyParamsPaymentMethodDataFpx"]
    """
    If this is an `fpx` PaymentMethod, this hash contains details about the FPX payment method.
    """
    giropay: NotRequired["SetupIntentModifyParamsPaymentMethodDataGiropay"]
    """
    If this is a `giropay` PaymentMethod, this hash contains details about the Giropay payment method.
    """
    gopay: NotRequired["SetupIntentModifyParamsPaymentMethodDataGopay"]
    """
    If this is a Gopay PaymentMethod, this hash contains details about the Gopay payment method.
    """
    grabpay: NotRequired["SetupIntentModifyParamsPaymentMethodDataGrabpay"]
    """
    If this is a `grabpay` PaymentMethod, this hash contains details about the GrabPay payment method.
    """
    id_bank_transfer: NotRequired[
        "SetupIntentModifyParamsPaymentMethodDataIdBankTransfer"
    ]
    """
    If this is an `IdBankTransfer` PaymentMethod, this hash contains details about the IdBankTransfer payment method.
    """
    ideal: NotRequired["SetupIntentModifyParamsPaymentMethodDataIdeal"]
    """
    If this is an `ideal` PaymentMethod, this hash contains details about the iDEAL payment method.
    """
    interac_present: NotRequired[
        "SetupIntentModifyParamsPaymentMethodDataInteracPresent"
    ]
    """
    If this is an `interac_present` PaymentMethod, this hash contains details about the Interac Present payment method.
    """
    kakao_pay: NotRequired["SetupIntentModifyParamsPaymentMethodDataKakaoPay"]
    """
    If this is a `kakao_pay` PaymentMethod, this hash contains details about the Kakao Pay payment method.
    """
    klarna: NotRequired["SetupIntentModifyParamsPaymentMethodDataKlarna"]
    """
    If this is a `klarna` PaymentMethod, this hash contains details about the Klarna payment method.
    """
    konbini: NotRequired["SetupIntentModifyParamsPaymentMethodDataKonbini"]
    """
    If this is a `konbini` PaymentMethod, this hash contains details about the Konbini payment method.
    """
    kr_card: NotRequired["SetupIntentModifyParamsPaymentMethodDataKrCard"]
    """
    If this is a `kr_card` PaymentMethod, this hash contains details about the Korean Card payment method.
    """
    link: NotRequired["SetupIntentModifyParamsPaymentMethodDataLink"]
    """
    If this is an `Link` PaymentMethod, this hash contains details about the Link payment method.
    """
    mb_way: NotRequired["SetupIntentModifyParamsPaymentMethodDataMbWay"]
    """
    If this is a MB WAY PaymentMethod, this hash contains details about the MB WAY payment method.
    """
    metadata: NotRequired[Dict[str, str]]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """
    mobilepay: NotRequired["SetupIntentModifyParamsPaymentMethodDataMobilepay"]
    """
    If this is a `mobilepay` PaymentMethod, this hash contains details about the MobilePay payment method.
    """
    multibanco: NotRequired[
        "SetupIntentModifyParamsPaymentMethodDataMultibanco"
    ]
    """
    If this is a `multibanco` PaymentMethod, this hash contains details about the Multibanco payment method.
    """
    naver_pay: NotRequired["SetupIntentModifyParamsPaymentMethodDataNaverPay"]
    """
    If this is a `naver_pay` PaymentMethod, this hash contains details about the Naver Pay payment method.
    """
    nz_bank_account: NotRequired[
        "SetupIntentModifyParamsPaymentMethodDataNzBankAccount"
    ]
    """
    If this is an nz_bank_account PaymentMethod, this hash contains details about the nz_bank_account payment method.
    """
    oxxo: NotRequired["SetupIntentModifyParamsPaymentMethodDataOxxo"]
    """
    If this is an `oxxo` PaymentMethod, this hash contains details about the OXXO payment method.
    """
    p24: NotRequired["SetupIntentModifyParamsPaymentMethodDataP24"]
    """
    If this is a `p24` PaymentMethod, this hash contains details about the P24 payment method.
    """
    pay_by_bank: NotRequired[
        "SetupIntentModifyParamsPaymentMethodDataPayByBank"
    ]
    """
    If this is a `pay_by_bank` PaymentMethod, this hash contains details about the PayByBank payment method.
    """
    payco: NotRequired["SetupIntentModifyParamsPaymentMethodDataPayco"]
    """
    If this is a `payco` PaymentMethod, this hash contains details about the PAYCO payment method.
    """
    paynow: NotRequired["SetupIntentModifyParamsPaymentMethodDataPaynow"]
    """
    If this is a `paynow` PaymentMethod, this hash contains details about the PayNow payment method.
    """
    paypal: NotRequired["SetupIntentModifyParamsPaymentMethodDataPaypal"]
    """
    If this is a `paypal` PaymentMethod, this hash contains details about the PayPal payment method.
    """
    paypay: NotRequired["SetupIntentModifyParamsPaymentMethodDataPaypay"]
    """
    If this is a `paypay` PaymentMethod, this hash contains details about the PayPay payment method.
    """
    payto: NotRequired["SetupIntentModifyParamsPaymentMethodDataPayto"]
    """
    If this is a `payto` PaymentMethod, this hash contains details about the PayTo payment method.
    """
    pix: NotRequired["SetupIntentModifyParamsPaymentMethodDataPix"]
    """
    If this is a `pix` PaymentMethod, this hash contains details about the Pix payment method.
    """
    promptpay: NotRequired["SetupIntentModifyParamsPaymentMethodDataPromptpay"]
    """
    If this is a `promptpay` PaymentMethod, this hash contains details about the PromptPay payment method.
    """
    qris: NotRequired["SetupIntentModifyParamsPaymentMethodDataQris"]
    """
    If this is a `qris` PaymentMethod, this hash contains details about the QRIS payment method.
    """
    radar_options: NotRequired[
        "SetupIntentModifyParamsPaymentMethodDataRadarOptions"
    ]
    """
    Options to configure Radar. See [Radar Session](https://stripe.com/docs/radar/radar-session) for more information.
    """
    rechnung: NotRequired["SetupIntentModifyParamsPaymentMethodDataRechnung"]
    """
    If this is a `rechnung` PaymentMethod, this hash contains details about the Rechnung payment method.
    """
    revolut_pay: NotRequired[
        "SetupIntentModifyParamsPaymentMethodDataRevolutPay"
    ]
    """
    If this is a `revolut_pay` PaymentMethod, this hash contains details about the Revolut Pay payment method.
    """
    samsung_pay: NotRequired[
        "SetupIntentModifyParamsPaymentMethodDataSamsungPay"
    ]
    """
    If this is a `samsung_pay` PaymentMethod, this hash contains details about the SamsungPay payment method.
    """
    satispay: NotRequired["SetupIntentModifyParamsPaymentMethodDataSatispay"]
    """
    If this is a `satispay` PaymentMethod, this hash contains details about the Satispay payment method.
    """
    sepa_debit: NotRequired[
        "SetupIntentModifyParamsPaymentMethodDataSepaDebit"
    ]
    """
    If this is a `sepa_debit` PaymentMethod, this hash contains details about the SEPA debit bank account.
    """
    shopeepay: NotRequired["SetupIntentModifyParamsPaymentMethodDataShopeepay"]
    """
    If this is a Shopeepay PaymentMethod, this hash contains details about the Shopeepay payment method.
    """
    sofort: NotRequired["SetupIntentModifyParamsPaymentMethodDataSofort"]
    """
    If this is a `sofort` PaymentMethod, this hash contains details about the SOFORT payment method.
    """
    stripe_balance: NotRequired[
        "SetupIntentModifyParamsPaymentMethodDataStripeBalance"
    ]
    """
    This hash contains details about the Stripe balance payment method.
    """
    swish: NotRequired["SetupIntentModifyParamsPaymentMethodDataSwish"]
    """
    If this is a `swish` PaymentMethod, this hash contains details about the Swish payment method.
    """
    twint: NotRequired["SetupIntentModifyParamsPaymentMethodDataTwint"]
    """
    If this is a TWINT PaymentMethod, this hash contains details about the TWINT payment method.
    """
    type: Literal[
        "acss_debit",
        "affirm",
        "afterpay_clearpay",
        "alipay",
        "alma",
        "amazon_pay",
        "au_becs_debit",
        "bacs_debit",
        "bancontact",
        "billie",
        "blik",
        "boleto",
        "cashapp",
        "crypto",
        "customer_balance",
        "eps",
        "fpx",
        "giropay",
        "gopay",
        "grabpay",
        "id_bank_transfer",
        "ideal",
        "kakao_pay",
        "klarna",
        "konbini",
        "kr_card",
        "link",
        "mb_way",
        "mobilepay",
        "multibanco",
        "naver_pay",
        "nz_bank_account",
        "oxxo",
        "p24",
        "pay_by_bank",
        "payco",
        "paynow",
        "paypal",
        "paypay",
        "payto",
        "pix",
        "promptpay",
        "qris",
        "rechnung",
        "revolut_pay",
        "samsung_pay",
        "satispay",
        "sepa_debit",
        "shopeepay",
        "sofort",
        "stripe_balance",
        "swish",
        "twint",
        "us_bank_account",
        "wechat_pay",
        "zip",
    ]
    """
    The type of the PaymentMethod. An additional hash is included on the PaymentMethod with a name matching this value. It contains additional information specific to the PaymentMethod type.
    """
    us_bank_account: NotRequired[
        "SetupIntentModifyParamsPaymentMethodDataUsBankAccount"
    ]
    """
    If this is an `us_bank_account` PaymentMethod, this hash contains details about the US bank account payment method.
    """
    wechat_pay: NotRequired[
        "SetupIntentModifyParamsPaymentMethodDataWechatPay"
    ]
    """
    If this is an `wechat_pay` PaymentMethod, this hash contains details about the wechat_pay payment method.
    """
    zip: NotRequired["SetupIntentModifyParamsPaymentMethodDataZip"]
    """
    If this is a `zip` PaymentMethod, this hash contains details about the Zip payment method.
    """


class SetupIntentModifyParamsPaymentMethodDataAcssDebit(TypedDict):
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


class SetupIntentModifyParamsPaymentMethodDataAffirm(TypedDict):
    pass


class SetupIntentModifyParamsPaymentMethodDataAfterpayClearpay(TypedDict):
    pass


class SetupIntentModifyParamsPaymentMethodDataAlipay(TypedDict):
    pass


class SetupIntentModifyParamsPaymentMethodDataAlma(TypedDict):
    pass


class SetupIntentModifyParamsPaymentMethodDataAmazonPay(TypedDict):
    pass


class SetupIntentModifyParamsPaymentMethodDataAuBecsDebit(TypedDict):
    account_number: str
    """
    The account number for the bank account.
    """
    bsb_number: str
    """
    Bank-State-Branch number of the bank account.
    """


class SetupIntentModifyParamsPaymentMethodDataBacsDebit(TypedDict):
    account_number: NotRequired[str]
    """
    Account number of the bank account that the funds will be debited from.
    """
    sort_code: NotRequired[str]
    """
    Sort code of the bank account. (e.g., `10-20-30`)
    """


class SetupIntentModifyParamsPaymentMethodDataBancontact(TypedDict):
    pass


class SetupIntentModifyParamsPaymentMethodDataBillie(TypedDict):
    pass


class SetupIntentModifyParamsPaymentMethodDataBillingDetails(TypedDict):
    address: NotRequired[
        "Literal['']|SetupIntentModifyParamsPaymentMethodDataBillingDetailsAddress"
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
    tax_id: NotRequired[str]
    """
    Taxpayer identification number. Used only for transactions between LATAM buyers and non-LATAM sellers.
    """


class SetupIntentModifyParamsPaymentMethodDataBillingDetailsAddress(TypedDict):
    city: NotRequired[str]
    """
    City, district, suburb, town, or village.
    """
    country: NotRequired[str]
    """
    Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
    """
    line1: NotRequired[str]
    """
    Address line 1, such as the street, PO Box, or company name.
    """
    line2: NotRequired[str]
    """
    Address line 2, such as the apartment, suite, unit, or building.
    """
    postal_code: NotRequired[str]
    """
    ZIP or postal code.
    """
    state: NotRequired[str]
    """
    State, county, province, or region.
    """


class SetupIntentModifyParamsPaymentMethodDataBlik(TypedDict):
    pass


class SetupIntentModifyParamsPaymentMethodDataBoleto(TypedDict):
    tax_id: str
    """
    The tax ID of the customer (CPF for individual consumers or CNPJ for businesses consumers)
    """


class SetupIntentModifyParamsPaymentMethodDataCashapp(TypedDict):
    pass


class SetupIntentModifyParamsPaymentMethodDataCrypto(TypedDict):
    pass


class SetupIntentModifyParamsPaymentMethodDataCustomerBalance(TypedDict):
    pass


class SetupIntentModifyParamsPaymentMethodDataEps(TypedDict):
    bank: NotRequired[
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
    The customer's bank.
    """


class SetupIntentModifyParamsPaymentMethodDataFpx(TypedDict):
    account_holder_type: NotRequired[Literal["company", "individual"]]
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


class SetupIntentModifyParamsPaymentMethodDataGiropay(TypedDict):
    pass


class SetupIntentModifyParamsPaymentMethodDataGopay(TypedDict):
    pass


class SetupIntentModifyParamsPaymentMethodDataGrabpay(TypedDict):
    pass


class SetupIntentModifyParamsPaymentMethodDataIdBankTransfer(TypedDict):
    bank: NotRequired[Literal["bca", "bni", "bri", "cimb", "permata"]]
    """
    Bank where the account is held.
    """


class SetupIntentModifyParamsPaymentMethodDataIdeal(TypedDict):
    bank: NotRequired[
        Literal[
            "abn_amro",
            "asn_bank",
            "bunq",
            "buut",
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
    The customer's bank. Only use this parameter for existing customers. Don't use it for new customers.
    """


class SetupIntentModifyParamsPaymentMethodDataInteracPresent(TypedDict):
    pass


class SetupIntentModifyParamsPaymentMethodDataKakaoPay(TypedDict):
    pass


class SetupIntentModifyParamsPaymentMethodDataKlarna(TypedDict):
    dob: NotRequired["SetupIntentModifyParamsPaymentMethodDataKlarnaDob"]
    """
    Customer's date of birth
    """


class SetupIntentModifyParamsPaymentMethodDataKlarnaDob(TypedDict):
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


class SetupIntentModifyParamsPaymentMethodDataKonbini(TypedDict):
    pass


class SetupIntentModifyParamsPaymentMethodDataKrCard(TypedDict):
    pass


class SetupIntentModifyParamsPaymentMethodDataLink(TypedDict):
    pass


class SetupIntentModifyParamsPaymentMethodDataMbWay(TypedDict):
    pass


class SetupIntentModifyParamsPaymentMethodDataMobilepay(TypedDict):
    pass


class SetupIntentModifyParamsPaymentMethodDataMultibanco(TypedDict):
    pass


class SetupIntentModifyParamsPaymentMethodDataNaverPay(TypedDict):
    funding: NotRequired[Literal["card", "points"]]
    """
    Whether to use Naver Pay points or a card to fund this transaction. If not provided, this defaults to `card`.
    """


class SetupIntentModifyParamsPaymentMethodDataNzBankAccount(TypedDict):
    account_holder_name: NotRequired[str]
    """
    The name on the bank account. Only required if the account holder name is different from the name of the authorized signatory collected in the PaymentMethod's billing details.
    """
    account_number: str
    """
    The account number for the bank account.
    """
    bank_code: str
    """
    The numeric code for the bank account's bank.
    """
    branch_code: str
    """
    The numeric code for the bank account's bank branch.
    """
    reference: NotRequired[str]
    suffix: str
    """
    The suffix of the bank account number.
    """


class SetupIntentModifyParamsPaymentMethodDataOxxo(TypedDict):
    pass


class SetupIntentModifyParamsPaymentMethodDataP24(TypedDict):
    bank: NotRequired[
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
            "velobank",
            "volkswagen_bank",
        ]
    ]
    """
    The customer's bank.
    """


class SetupIntentModifyParamsPaymentMethodDataPayByBank(TypedDict):
    pass


class SetupIntentModifyParamsPaymentMethodDataPayco(TypedDict):
    pass


class SetupIntentModifyParamsPaymentMethodDataPaynow(TypedDict):
    pass


class SetupIntentModifyParamsPaymentMethodDataPaypal(TypedDict):
    pass


class SetupIntentModifyParamsPaymentMethodDataPaypay(TypedDict):
    pass


class SetupIntentModifyParamsPaymentMethodDataPayto(TypedDict):
    account_number: NotRequired[str]
    """
    The account number for the bank account.
    """
    bsb_number: NotRequired[str]
    """
    Bank-State-Branch number of the bank account.
    """
    pay_id: NotRequired[str]
    """
    The PayID alias for the bank account.
    """


class SetupIntentModifyParamsPaymentMethodDataPix(TypedDict):
    pass


class SetupIntentModifyParamsPaymentMethodDataPromptpay(TypedDict):
    pass


class SetupIntentModifyParamsPaymentMethodDataQris(TypedDict):
    pass


class SetupIntentModifyParamsPaymentMethodDataRadarOptions(TypedDict):
    session: NotRequired[str]
    """
    A [Radar Session](https://stripe.com/docs/radar/radar-session) is a snapshot of the browser metadata and device details that help Radar make more accurate predictions on your payments.
    """


class SetupIntentModifyParamsPaymentMethodDataRechnung(TypedDict):
    dob: "SetupIntentModifyParamsPaymentMethodDataRechnungDob"
    """
    Customer's date of birth
    """


class SetupIntentModifyParamsPaymentMethodDataRechnungDob(TypedDict):
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


class SetupIntentModifyParamsPaymentMethodDataRevolutPay(TypedDict):
    pass


class SetupIntentModifyParamsPaymentMethodDataSamsungPay(TypedDict):
    pass


class SetupIntentModifyParamsPaymentMethodDataSatispay(TypedDict):
    pass


class SetupIntentModifyParamsPaymentMethodDataSepaDebit(TypedDict):
    iban: str
    """
    IBAN of the bank account.
    """


class SetupIntentModifyParamsPaymentMethodDataShopeepay(TypedDict):
    pass


class SetupIntentModifyParamsPaymentMethodDataSofort(TypedDict):
    country: Literal["AT", "BE", "DE", "ES", "IT", "NL"]
    """
    Two-letter ISO code representing the country the bank account is located in.
    """


class SetupIntentModifyParamsPaymentMethodDataStripeBalance(TypedDict):
    account: NotRequired[str]
    """
    The connected account ID whose Stripe balance to use as the source of payment
    """
    source_type: NotRequired[Literal["bank_account", "card", "fpx"]]
    """
    The [source_type](https://docs.stripe.com/api/balance/balance_object#balance_object-available-source_types) of the balance
    """


class SetupIntentModifyParamsPaymentMethodDataSwish(TypedDict):
    pass


class SetupIntentModifyParamsPaymentMethodDataTwint(TypedDict):
    pass


class SetupIntentModifyParamsPaymentMethodDataUsBankAccount(TypedDict):
    account_holder_type: NotRequired[Literal["company", "individual"]]
    """
    Account holder type: individual or company.
    """
    account_number: NotRequired[str]
    """
    Account number of the bank account.
    """
    account_type: NotRequired[Literal["checking", "savings"]]
    """
    Account type: checkings or savings. Defaults to checking if omitted.
    """
    financial_connections_account: NotRequired[str]
    """
    The ID of a Financial Connections Account to use as a payment method.
    """
    routing_number: NotRequired[str]
    """
    Routing number of the bank account.
    """


class SetupIntentModifyParamsPaymentMethodDataWechatPay(TypedDict):
    pass


class SetupIntentModifyParamsPaymentMethodDataZip(TypedDict):
    pass


class SetupIntentModifyParamsPaymentMethodOptions(TypedDict):
    acss_debit: NotRequired[
        "SetupIntentModifyParamsPaymentMethodOptionsAcssDebit"
    ]
    """
    If this is a `acss_debit` SetupIntent, this sub-hash contains details about the ACSS Debit payment method options.
    """
    amazon_pay: NotRequired[
        "SetupIntentModifyParamsPaymentMethodOptionsAmazonPay"
    ]
    """
    If this is a `amazon_pay` SetupIntent, this sub-hash contains details about the AmazonPay payment method options.
    """
    bacs_debit: NotRequired[
        "SetupIntentModifyParamsPaymentMethodOptionsBacsDebit"
    ]
    """
    If this is a `bacs_debit` SetupIntent, this sub-hash contains details about the Bacs Debit payment method options.
    """
    card: NotRequired["SetupIntentModifyParamsPaymentMethodOptionsCard"]
    """
    Configuration for any card setup attempted on this SetupIntent.
    """
    card_present: NotRequired[
        "SetupIntentModifyParamsPaymentMethodOptionsCardPresent"
    ]
    """
    If this is a `card_present` PaymentMethod, this sub-hash contains details about the card-present payment method options.
    """
    klarna: NotRequired["SetupIntentModifyParamsPaymentMethodOptionsKlarna"]
    """
    If this is a `klarna` PaymentMethod, this hash contains details about the Klarna payment method options.
    """
    link: NotRequired["SetupIntentModifyParamsPaymentMethodOptionsLink"]
    """
    If this is a `link` PaymentMethod, this sub-hash contains details about the Link payment method options.
    """
    paypal: NotRequired["SetupIntentModifyParamsPaymentMethodOptionsPaypal"]
    """
    If this is a `paypal` PaymentMethod, this sub-hash contains details about the PayPal payment method options.
    """
    payto: NotRequired["SetupIntentModifyParamsPaymentMethodOptionsPayto"]
    """
    If this is a `payto` SetupIntent, this sub-hash contains details about the PayTo payment method options.
    """
    pix: NotRequired["SetupIntentModifyParamsPaymentMethodOptionsPix"]
    """
    If this is a `pix` SetupIntent, this sub-hash contains details about the Pix payment method options.
    """
    sepa_debit: NotRequired[
        "SetupIntentModifyParamsPaymentMethodOptionsSepaDebit"
    ]
    """
    If this is a `sepa_debit` SetupIntent, this sub-hash contains details about the SEPA Debit payment method options.
    """
    us_bank_account: NotRequired[
        "SetupIntentModifyParamsPaymentMethodOptionsUsBankAccount"
    ]
    """
    If this is a `us_bank_account` SetupIntent, this sub-hash contains details about the US bank account payment method options.
    """


class SetupIntentModifyParamsPaymentMethodOptionsAcssDebit(TypedDict):
    currency: NotRequired[Literal["cad", "usd"]]
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    mandate_options: NotRequired[
        "SetupIntentModifyParamsPaymentMethodOptionsAcssDebitMandateOptions"
    ]
    """
    Additional fields for Mandate creation
    """
    verification_method: NotRequired[
        Literal["automatic", "instant", "microdeposits"]
    ]
    """
    Bank account verification method.
    """


class SetupIntentModifyParamsPaymentMethodOptionsAcssDebitMandateOptions(
    TypedDict,
):
    custom_mandate_url: NotRequired["Literal['']|str"]
    """
    A URL for custom mandate text to render during confirmation step.
    The URL will be rendered with additional GET parameters `payment_intent` and `payment_intent_client_secret` when confirming a Payment Intent,
    or `setup_intent` and `setup_intent_client_secret` when confirming a Setup Intent.
    """
    default_for: NotRequired[List[Literal["invoice", "subscription"]]]
    """
    List of Stripe products where this mandate can be selected automatically.
    """
    interval_description: NotRequired[str]
    """
    Description of the mandate interval. Only required if 'payment_schedule' parameter is 'interval' or 'combined'.
    """
    payment_schedule: NotRequired[Literal["combined", "interval", "sporadic"]]
    """
    Payment schedule for the mandate.
    """
    transaction_type: NotRequired[Literal["business", "personal"]]
    """
    Transaction type of the mandate.
    """


class SetupIntentModifyParamsPaymentMethodOptionsAmazonPay(TypedDict):
    pass


class SetupIntentModifyParamsPaymentMethodOptionsBacsDebit(TypedDict):
    mandate_options: NotRequired[
        "SetupIntentModifyParamsPaymentMethodOptionsBacsDebitMandateOptions"
    ]
    """
    Additional fields for Mandate creation
    """


class SetupIntentModifyParamsPaymentMethodOptionsBacsDebitMandateOptions(
    TypedDict,
):
    reference_prefix: NotRequired["Literal['']|str"]
    """
    Prefix used to generate the Mandate reference. Must be at most 12 characters long. Must consist of only uppercase letters, numbers, spaces, or the following special characters: '/', '_', '-', '&', '.'. Cannot begin with 'DDIC' or 'STRIPE'.
    """


class SetupIntentModifyParamsPaymentMethodOptionsCard(TypedDict):
    mandate_options: NotRequired[
        "SetupIntentModifyParamsPaymentMethodOptionsCardMandateOptions"
    ]
    """
    Configuration options for setting up an eMandate for cards issued in India.
    """
    moto: NotRequired[bool]
    """
    When specified, this parameter signals that a card has been collected
    as MOTO (Mail Order Telephone Order) and thus out of scope for SCA. This
    parameter can only be provided during confirmation.
    """
    network: NotRequired[
        Literal[
            "amex",
            "cartes_bancaires",
            "diners",
            "discover",
            "eftpos_au",
            "girocard",
            "interac",
            "jcb",
            "link",
            "mastercard",
            "unionpay",
            "unknown",
            "visa",
        ]
    ]
    """
    Selected network to process this SetupIntent on. Depends on the available networks of the card attached to the SetupIntent. Can be only set confirm-time.
    """
    request_three_d_secure: NotRequired[
        Literal["any", "automatic", "challenge"]
    ]
    """
    We strongly recommend that you rely on our SCA Engine to automatically prompt your customers for authentication based on risk level and [other requirements](https://stripe.com/docs/strong-customer-authentication). However, if you wish to request 3D Secure based on logic from your own fraud engine, provide this option. If not provided, this value defaults to `automatic`. Read our guide on [manually requesting 3D Secure](https://stripe.com/docs/payments/3d-secure/authentication-flow#manual-three-ds) for more information on how this configuration interacts with Radar and our SCA Engine.
    """
    three_d_secure: NotRequired[
        "SetupIntentModifyParamsPaymentMethodOptionsCardThreeDSecure"
    ]
    """
    If 3D Secure authentication was performed with a third-party provider,
    the authentication details to use for this setup.
    """


class SetupIntentModifyParamsPaymentMethodOptionsCardMandateOptions(TypedDict):
    amount: int
    """
    Amount to be charged for future payments.
    """
    amount_type: Literal["fixed", "maximum"]
    """
    One of `fixed` or `maximum`. If `fixed`, the `amount` param refers to the exact amount to be charged in future payments. If `maximum`, the amount charged can be up to the value passed for the `amount` param.
    """
    currency: str
    """
    Currency in which future payments will be charged. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    description: NotRequired[str]
    """
    A description of the mandate or subscription that is meant to be displayed to the customer.
    """
    end_date: NotRequired[int]
    """
    End date of the mandate or subscription. If not provided, the mandate will be active until canceled. If provided, end date should be after start date.
    """
    interval: Literal["day", "month", "sporadic", "week", "year"]
    """
    Specifies payment frequency. One of `day`, `week`, `month`, `year`, or `sporadic`.
    """
    interval_count: NotRequired[int]
    """
    The number of intervals between payments. For example, `interval=month` and `interval_count=3` indicates one payment every three months. Maximum of one year interval allowed (1 year, 12 months, or 52 weeks). This parameter is optional when `interval=sporadic`.
    """
    reference: str
    """
    Unique identifier for the mandate or subscription.
    """
    start_date: int
    """
    Start date of the mandate or subscription. Start date should not be lesser than yesterday.
    """
    supported_types: NotRequired[List[Literal["india"]]]
    """
    Specifies the type of mandates supported. Possible values are `india`.
    """


class SetupIntentModifyParamsPaymentMethodOptionsCardThreeDSecure(TypedDict):
    ares_trans_status: NotRequired[Literal["A", "C", "I", "N", "R", "U", "Y"]]
    """
    The `transStatus` returned from the card Issuer's ACS in the ARes.
    """
    cryptogram: NotRequired[str]
    """
    The cryptogram, also known as the "authentication value" (AAV, CAVV or
    AEVV). This value is 20 bytes, base64-encoded into a 28-character string.
    (Most 3D Secure providers will return the base64-encoded version, which
    is what you should specify here.)
    """
    electronic_commerce_indicator: NotRequired[
        Literal["01", "02", "05", "06", "07"]
    ]
    """
    The Electronic Commerce Indicator (ECI) is returned by your 3D Secure
    provider and indicates what degree of authentication was performed.
    """
    network_options: NotRequired[
        "SetupIntentModifyParamsPaymentMethodOptionsCardThreeDSecureNetworkOptions"
    ]
    """
    Network specific 3DS fields. Network specific arguments require an
    explicit card brand choice. The parameter `payment_method_options.card.network``
    must be populated accordingly
    """
    requestor_challenge_indicator: NotRequired[str]
    """
    The challenge indicator (`threeDSRequestorChallengeInd`) which was requested in the
    AReq sent to the card Issuer's ACS. A string containing 2 digits from 01-99.
    """
    transaction_id: NotRequired[str]
    """
    For 3D Secure 1, the XID. For 3D Secure 2, the Directory Server
    Transaction ID (dsTransID).
    """
    version: NotRequired[Literal["1.0.2", "2.1.0", "2.2.0"]]
    """
    The version of 3D Secure that was performed.
    """


class SetupIntentModifyParamsPaymentMethodOptionsCardThreeDSecureNetworkOptions(
    TypedDict,
):
    cartes_bancaires: NotRequired[
        "SetupIntentModifyParamsPaymentMethodOptionsCardThreeDSecureNetworkOptionsCartesBancaires"
    ]
    """
    Cartes Bancaires-specific 3DS fields.
    """


class SetupIntentModifyParamsPaymentMethodOptionsCardThreeDSecureNetworkOptionsCartesBancaires(
    TypedDict,
):
    cb_avalgo: Literal["0", "1", "2", "3", "4", "A"]
    """
    The cryptogram calculation algorithm used by the card Issuer's ACS
    to calculate the Authentication cryptogram. Also known as `cavvAlgorithm`.
    messageExtension: CB-AVALGO
    """
    cb_exemption: NotRequired[str]
    """
    The exemption indicator returned from Cartes Bancaires in the ARes.
    message extension: CB-EXEMPTION; string (4 characters)
    This is a 3 byte bitmap (low significant byte first and most significant
    bit first) that has been Base64 encoded
    """
    cb_score: NotRequired[int]
    """
    The risk score returned from Cartes Bancaires in the ARes.
    message extension: CB-SCORE; numeric value 0-99
    """


class SetupIntentModifyParamsPaymentMethodOptionsCardPresent(TypedDict):
    pass


class SetupIntentModifyParamsPaymentMethodOptionsKlarna(TypedDict):
    currency: NotRequired[str]
    """
    The currency of the SetupIntent. Three letter ISO currency code.
    """
    on_demand: NotRequired[
        "SetupIntentModifyParamsPaymentMethodOptionsKlarnaOnDemand"
    ]
    """
    On-demand details if setting up a payment method for on-demand payments.
    """
    preferred_locale: NotRequired[
        Literal[
            "cs-CZ",
            "da-DK",
            "de-AT",
            "de-CH",
            "de-DE",
            "el-GR",
            "en-AT",
            "en-AU",
            "en-BE",
            "en-CA",
            "en-CH",
            "en-CZ",
            "en-DE",
            "en-DK",
            "en-ES",
            "en-FI",
            "en-FR",
            "en-GB",
            "en-GR",
            "en-IE",
            "en-IT",
            "en-NL",
            "en-NO",
            "en-NZ",
            "en-PL",
            "en-PT",
            "en-RO",
            "en-SE",
            "en-US",
            "es-ES",
            "es-US",
            "fi-FI",
            "fr-BE",
            "fr-CA",
            "fr-CH",
            "fr-FR",
            "it-CH",
            "it-IT",
            "nb-NO",
            "nl-BE",
            "nl-NL",
            "pl-PL",
            "pt-PT",
            "ro-RO",
            "sv-FI",
            "sv-SE",
        ]
    ]
    """
    Preferred language of the Klarna authorization page that the customer is redirected to
    """
    subscriptions: NotRequired[
        "Literal['']|List[SetupIntentModifyParamsPaymentMethodOptionsKlarnaSubscription]"
    ]
    """
    Subscription details if setting up or charging a subscription
    """


class SetupIntentModifyParamsPaymentMethodOptionsKlarnaOnDemand(TypedDict):
    average_amount: NotRequired[int]
    """
    Your average amount value. You can use a value across your customer base, or segment based on customer type, country, etc.
    """
    maximum_amount: NotRequired[int]
    """
    The maximum value you may charge a customer per purchase. You can use a value across your customer base, or segment based on customer type, country, etc.
    """
    minimum_amount: NotRequired[int]
    """
    The lowest or minimum value you may charge a customer per purchase. You can use a value across your customer base, or segment based on customer type, country, etc.
    """
    purchase_interval: NotRequired[Literal["day", "month", "week", "year"]]
    """
    Interval at which the customer is making purchases
    """
    purchase_interval_count: NotRequired[int]
    """
    The number of `purchase_interval` between charges
    """


class SetupIntentModifyParamsPaymentMethodOptionsKlarnaSubscription(TypedDict):
    interval: Literal["day", "month", "week", "year"]
    """
    Unit of time between subscription charges.
    """
    interval_count: NotRequired[int]
    """
    The number of intervals (specified in the `interval` attribute) between subscription charges. For example, `interval=month` and `interval_count=3` charges every 3 months.
    """
    name: NotRequired[str]
    """
    Name for subscription.
    """
    next_billing: "SetupIntentModifyParamsPaymentMethodOptionsKlarnaSubscriptionNextBilling"
    """
    Describes the upcoming charge for this subscription.
    """
    reference: str
    """
    A non-customer-facing reference to correlate subscription charges in the Klarna app. Use a value that persists across subscription charges.
    """


class SetupIntentModifyParamsPaymentMethodOptionsKlarnaSubscriptionNextBilling(
    TypedDict,
):
    amount: int
    """
    The amount of the next charge for the subscription.
    """
    date: str
    """
    The date of the next charge for the subscription in YYYY-MM-DD format.
    """


class SetupIntentModifyParamsPaymentMethodOptionsLink(TypedDict):
    persistent_token: NotRequired[str]
    """
    [Deprecated] This is a legacy parameter that no longer has any function.
    """


class SetupIntentModifyParamsPaymentMethodOptionsPaypal(TypedDict):
    billing_agreement_id: NotRequired[str]
    """
    The PayPal Billing Agreement ID (BAID). This is an ID generated by PayPal which represents the mandate between the merchant and the customer.
    """
    currency: NotRequired[str]
    subsellers: NotRequired[List[str]]
    """
    The Stripe connected account IDs of the sellers on the platform for this transaction (optional). Only allowed when [separate charges and transfers](https://stripe.com/docs/connect/separate-charges-and-transfers) are used.
    """


class SetupIntentModifyParamsPaymentMethodOptionsPayto(TypedDict):
    mandate_options: NotRequired[
        "SetupIntentModifyParamsPaymentMethodOptionsPaytoMandateOptions"
    ]
    """
    Additional fields for Mandate creation.
    """


class SetupIntentModifyParamsPaymentMethodOptionsPaytoMandateOptions(
    TypedDict
):
    amount: NotRequired[int]
    """
    Amount that will be collected. It is required when `amount_type` is `fixed`.
    """
    amount_type: NotRequired[Literal["fixed", "maximum"]]
    """
    The type of amount that will be collected. The amount charged must be exact or up to the value of `amount` param for `fixed` or `maximum` type respectively.
    """
    end_date: NotRequired[str]
    """
    Date, in YYYY-MM-DD format, after which payments will not be collected. Defaults to no end date.
    """
    payment_schedule: NotRequired[
        Literal[
            "adhoc",
            "annual",
            "daily",
            "fortnightly",
            "monthly",
            "quarterly",
            "semi_annual",
            "weekly",
        ]
    ]
    """
    The periodicity at which payments will be collected.
    """
    payments_per_period: NotRequired[int]
    """
    The number of payments that will be made during a payment period. Defaults to 1 except for when `payment_schedule` is `adhoc`. In that case, it defaults to no limit.
    """
    purpose: NotRequired[
        Literal[
            "dependant_support",
            "government",
            "loan",
            "mortgage",
            "other",
            "pension",
            "personal",
            "retail",
            "salary",
            "tax",
            "utility",
        ]
    ]
    """
    The purpose for which payments are made. Defaults to retail.
    """
    start_date: NotRequired[str]
    """
    Date, in YYYY-MM-DD format, from which payments will be collected. Defaults to confirmation time.
    """


class SetupIntentModifyParamsPaymentMethodOptionsPix(TypedDict):
    mandate_options: NotRequired[
        "SetupIntentModifyParamsPaymentMethodOptionsPixMandateOptions"
    ]
    """
    Additional fields for mandate creation.
    """


class SetupIntentModifyParamsPaymentMethodOptionsPixMandateOptions(TypedDict):
    amount: NotRequired[int]
    """
    Amount to be charged for future payments. Required when `amount_type=fixed`. If not provided for `amount_type=maximum`, defaults to 40000.
    """
    amount_includes_iof: NotRequired[Literal["always", "never"]]
    """
    Determines if the amount includes the IOF tax. Defaults to `never`.
    """
    amount_type: NotRequired[Literal["fixed", "maximum"]]
    """
    Type of amount. Defaults to `maximum`.
    """
    currency: NotRequired[str]
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Only `brl` is supported currently.
    """
    end_date: NotRequired[str]
    """
    Date when the mandate expires and no further payments will be charged, in `YYYY-MM-DD`. If not provided, the mandate will be active until canceled. If provided, end date should be after start date.
    """
    payment_schedule: NotRequired[
        Literal["halfyearly", "monthly", "quarterly", "weekly", "yearly"]
    ]
    """
    Schedule at which the future payments will be charged. Defaults to `weekly`.
    """
    reference: NotRequired[str]
    """
    Subscription name displayed to buyers in their bank app. Defaults to the displayable business name.
    """
    start_date: NotRequired[str]
    """
    Start date of the mandate, in `YYYY-MM-DD`. Start date should be at least 3 days in the future. Defaults to 3 days after the current date.
    """


class SetupIntentModifyParamsPaymentMethodOptionsSepaDebit(TypedDict):
    mandate_options: NotRequired[
        "SetupIntentModifyParamsPaymentMethodOptionsSepaDebitMandateOptions"
    ]
    """
    Additional fields for Mandate creation
    """


class SetupIntentModifyParamsPaymentMethodOptionsSepaDebitMandateOptions(
    TypedDict,
):
    reference_prefix: NotRequired["Literal['']|str"]
    """
    Prefix used to generate the Mandate reference. Must be at most 12 characters long. Must consist of only uppercase letters, numbers, spaces, or the following special characters: '/', '_', '-', '&', '.'. Cannot begin with 'STRIPE'.
    """


class SetupIntentModifyParamsPaymentMethodOptionsUsBankAccount(TypedDict):
    financial_connections: NotRequired[
        "SetupIntentModifyParamsPaymentMethodOptionsUsBankAccountFinancialConnections"
    ]
    """
    Additional fields for Financial Connections Session creation
    """
    mandate_options: NotRequired[
        "SetupIntentModifyParamsPaymentMethodOptionsUsBankAccountMandateOptions"
    ]
    """
    Additional fields for Mandate creation
    """
    networks: NotRequired[
        "SetupIntentModifyParamsPaymentMethodOptionsUsBankAccountNetworks"
    ]
    """
    Additional fields for network related functions
    """
    verification_method: NotRequired[
        Literal["automatic", "instant", "microdeposits"]
    ]
    """
    Bank account verification method.
    """


class SetupIntentModifyParamsPaymentMethodOptionsUsBankAccountFinancialConnections(
    TypedDict,
):
    filters: NotRequired[
        "SetupIntentModifyParamsPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters"
    ]
    """
    Provide filters for the linked accounts that the customer can select for the payment method.
    """
    manual_entry: NotRequired[
        "SetupIntentModifyParamsPaymentMethodOptionsUsBankAccountFinancialConnectionsManualEntry"
    ]
    """
    Customize manual entry behavior
    """
    permissions: NotRequired[
        List[
            Literal["balances", "ownership", "payment_method", "transactions"]
        ]
    ]
    """
    The list of permissions to request. If this parameter is passed, the `payment_method` permission must be included. Valid permissions include: `balances`, `ownership`, `payment_method`, and `transactions`.
    """
    prefetch: NotRequired[
        List[
            Literal[
                "balances", "inferred_balances", "ownership", "transactions"
            ]
        ]
    ]
    """
    List of data features that you would like to retrieve upon account creation.
    """
    return_url: NotRequired[str]
    """
    For webview integrations only. Upon completing OAuth login in the native browser, the user will be redirected to this URL to return to your app.
    """


class SetupIntentModifyParamsPaymentMethodOptionsUsBankAccountFinancialConnectionsFilters(
    TypedDict,
):
    account_subcategories: NotRequired[List[Literal["checking", "savings"]]]
    """
    The account subcategories to use to filter for selectable accounts. Valid subcategories are `checking` and `savings`.
    """
    institution: NotRequired[str]
    """
    ID of the institution to use to filter for selectable accounts.
    """


class SetupIntentModifyParamsPaymentMethodOptionsUsBankAccountFinancialConnectionsManualEntry(
    TypedDict,
):
    mode: Literal["automatic", "custom"]
    """
    Settings for configuring manual entry of account details.
    """


class SetupIntentModifyParamsPaymentMethodOptionsUsBankAccountMandateOptions(
    TypedDict,
):
    collection_method: NotRequired["Literal['']|Literal['paper']"]
    """
    The method used to collect offline mandate customer acceptance.
    """


class SetupIntentModifyParamsPaymentMethodOptionsUsBankAccountNetworks(
    TypedDict,
):
    requested: NotRequired[List[Literal["ach", "us_domestic_wire"]]]
    """
    Triggers validations to run across the selected networks
    """


class SetupIntentModifyParamsSetupDetails(TypedDict):
    benefit: NotRequired["SetupIntentModifyParamsSetupDetailsBenefit"]
    """
    Benefit details for this SetupIntent
    """


class SetupIntentModifyParamsSetupDetailsBenefit(TypedDict):
    fr_meal_voucher: NotRequired[
        "SetupIntentModifyParamsSetupDetailsBenefitFrMealVoucher"
    ]
    """
    French meal voucher benefit details for this SetupIntent.
    """


class SetupIntentModifyParamsSetupDetailsBenefitFrMealVoucher(TypedDict):
    siret: str
    """
    The 14-digit SIRET of the meal voucher acceptor.
    """
