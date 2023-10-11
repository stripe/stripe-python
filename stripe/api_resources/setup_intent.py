# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

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
from typing import Dict, List, Optional, Union, cast
from typing_extensions import Literal, NotRequired, TypedDict, Unpack
from urllib.parse import quote_plus

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.account import Account
    from stripe.api_resources.application import Application
    from stripe.api_resources.customer import Customer
    from stripe.api_resources.mandate import Mandate
    from stripe.api_resources.payment_method import PaymentMethod
    from stripe.api_resources.setup_attempt import SetupAttempt


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

    class CancelParams(RequestOptions):
        cancellation_reason: NotRequired[
            Optional[
                Literal["abandoned", "duplicate", "requested_by_customer"]
            ]
        ]
        expand: NotRequired[Optional[List[str]]]

    class ConfirmParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]
        mandate_data: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    Union[
                        "SetupIntent.ConfirmParamsMandateData",
                        "SetupIntent.ConfirmParamsMandateData",
                    ],
                ]
            ]
        ]
        payment_method: NotRequired[Optional[str]]
        payment_method_data: NotRequired[
            Optional["SetupIntent.ConfirmParamsPaymentMethodData"]
        ]
        payment_method_options: NotRequired[
            Optional["SetupIntent.ConfirmParamsPaymentMethodOptions"]
        ]
        return_url: NotRequired[Optional[str]]
        use_stripe_sdk: NotRequired[Optional[bool]]

    class ConfirmParamsPaymentMethodOptions(TypedDict):
        acss_debit: NotRequired[
            Optional["SetupIntent.ConfirmParamsPaymentMethodOptionsAcssDebit"]
        ]
        card: NotRequired[
            Optional["SetupIntent.ConfirmParamsPaymentMethodOptionsCard"]
        ]
        link: NotRequired[
            Optional["SetupIntent.ConfirmParamsPaymentMethodOptionsLink"]
        ]
        paypal: NotRequired[
            Optional["SetupIntent.ConfirmParamsPaymentMethodOptionsPaypal"]
        ]
        sepa_debit: NotRequired[
            Optional["SetupIntent.ConfirmParamsPaymentMethodOptionsSepaDebit"]
        ]
        us_bank_account: NotRequired[
            Optional[
                "SetupIntent.ConfirmParamsPaymentMethodOptionsUsBankAccount"
            ]
        ]

    class ConfirmParamsPaymentMethodOptionsUsBankAccount(TypedDict):
        financial_connections: NotRequired[
            Optional[
                "SetupIntent.ConfirmParamsPaymentMethodOptionsUsBankAccountFinancialConnections"
            ]
        ]
        networks: NotRequired[
            Optional[
                "SetupIntent.ConfirmParamsPaymentMethodOptionsUsBankAccountNetworks"
            ]
        ]
        verification_method: NotRequired[
            Optional[Literal["automatic", "instant", "microdeposits"]]
        ]

    class ConfirmParamsPaymentMethodOptionsUsBankAccountNetworks(TypedDict):
        requested: NotRequired[
            Optional[List[Literal["ach", "us_domestic_wire"]]]
        ]

    class ConfirmParamsPaymentMethodOptionsUsBankAccountFinancialConnections(
        TypedDict,
    ):
        permissions: NotRequired[
            Optional[
                List[
                    Literal[
                        "balances",
                        "ownership",
                        "payment_method",
                        "transactions",
                    ]
                ]
            ]
        ]
        prefetch: NotRequired[Optional[List[Literal["balances"]]]]
        return_url: NotRequired[Optional[str]]

    class ConfirmParamsPaymentMethodOptionsSepaDebit(TypedDict):
        mandate_options: NotRequired[
            Optional[
                "SetupIntent.ConfirmParamsPaymentMethodOptionsSepaDebitMandateOptions"
            ]
        ]

    class ConfirmParamsPaymentMethodOptionsSepaDebitMandateOptions(TypedDict):
        pass

    class ConfirmParamsPaymentMethodOptionsPaypal(TypedDict):
        billing_agreement_id: NotRequired[Optional[str]]

    class ConfirmParamsPaymentMethodOptionsLink(TypedDict):
        persistent_token: NotRequired[Optional[str]]

    class ConfirmParamsPaymentMethodOptionsCard(TypedDict):
        mandate_options: NotRequired[
            Optional[
                "SetupIntent.ConfirmParamsPaymentMethodOptionsCardMandateOptions"
            ]
        ]
        moto: NotRequired[Optional[bool]]
        network: NotRequired[
            Optional[
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
        ]
        request_three_d_secure: NotRequired[
            Optional[Literal["any", "automatic"]]
        ]

    class ConfirmParamsPaymentMethodOptionsCardMandateOptions(TypedDict):
        amount: int
        amount_type: Literal["fixed", "maximum"]
        currency: str
        description: NotRequired[Optional[str]]
        end_date: NotRequired[Optional[int]]
        interval: Literal["day", "month", "sporadic", "week", "year"]
        interval_count: NotRequired[Optional[int]]
        reference: str
        start_date: int
        supported_types: NotRequired[Optional[List[Literal["india"]]]]

    class ConfirmParamsPaymentMethodOptionsAcssDebit(TypedDict):
        currency: NotRequired[Optional[Literal["cad", "usd"]]]
        mandate_options: NotRequired[
            Optional[
                "SetupIntent.ConfirmParamsPaymentMethodOptionsAcssDebitMandateOptions"
            ]
        ]
        verification_method: NotRequired[
            Optional[Literal["automatic", "instant", "microdeposits"]]
        ]

    class ConfirmParamsPaymentMethodOptionsAcssDebitMandateOptions(TypedDict):
        custom_mandate_url: NotRequired[Optional[Union[Literal[""], str]]]
        default_for: NotRequired[
            Optional[List[Literal["invoice", "subscription"]]]
        ]
        interval_description: NotRequired[Optional[str]]
        payment_schedule: NotRequired[
            Optional[Literal["combined", "interval", "sporadic"]]
        ]
        transaction_type: NotRequired[
            Optional[Literal["business", "personal"]]
        ]

    class ConfirmParamsPaymentMethodData(TypedDict):
        acss_debit: NotRequired[
            Optional["SetupIntent.ConfirmParamsPaymentMethodDataAcssDebit"]
        ]
        affirm: NotRequired[
            Optional["SetupIntent.ConfirmParamsPaymentMethodDataAffirm"]
        ]
        afterpay_clearpay: NotRequired[
            Optional[
                "SetupIntent.ConfirmParamsPaymentMethodDataAfterpayClearpay"
            ]
        ]
        alipay: NotRequired[
            Optional["SetupIntent.ConfirmParamsPaymentMethodDataAlipay"]
        ]
        au_becs_debit: NotRequired[
            Optional["SetupIntent.ConfirmParamsPaymentMethodDataAuBecsDebit"]
        ]
        bacs_debit: NotRequired[
            Optional["SetupIntent.ConfirmParamsPaymentMethodDataBacsDebit"]
        ]
        bancontact: NotRequired[
            Optional["SetupIntent.ConfirmParamsPaymentMethodDataBancontact"]
        ]
        billing_details: NotRequired[
            Optional[
                "SetupIntent.ConfirmParamsPaymentMethodDataBillingDetails"
            ]
        ]
        blik: NotRequired[
            Optional["SetupIntent.ConfirmParamsPaymentMethodDataBlik"]
        ]
        boleto: NotRequired[
            Optional["SetupIntent.ConfirmParamsPaymentMethodDataBoleto"]
        ]
        cashapp: NotRequired[
            Optional["SetupIntent.ConfirmParamsPaymentMethodDataCashapp"]
        ]
        customer_balance: NotRequired[
            Optional[
                "SetupIntent.ConfirmParamsPaymentMethodDataCustomerBalance"
            ]
        ]
        eps: NotRequired[
            Optional["SetupIntent.ConfirmParamsPaymentMethodDataEps"]
        ]
        fpx: NotRequired[
            Optional["SetupIntent.ConfirmParamsPaymentMethodDataFpx"]
        ]
        giropay: NotRequired[
            Optional["SetupIntent.ConfirmParamsPaymentMethodDataGiropay"]
        ]
        grabpay: NotRequired[
            Optional["SetupIntent.ConfirmParamsPaymentMethodDataGrabpay"]
        ]
        ideal: NotRequired[
            Optional["SetupIntent.ConfirmParamsPaymentMethodDataIdeal"]
        ]
        interac_present: NotRequired[
            Optional[
                "SetupIntent.ConfirmParamsPaymentMethodDataInteracPresent"
            ]
        ]
        klarna: NotRequired[
            Optional["SetupIntent.ConfirmParamsPaymentMethodDataKlarna"]
        ]
        konbini: NotRequired[
            Optional["SetupIntent.ConfirmParamsPaymentMethodDataKonbini"]
        ]
        link: NotRequired[
            Optional["SetupIntent.ConfirmParamsPaymentMethodDataLink"]
        ]
        metadata: NotRequired[Optional[Dict[str, str]]]
        oxxo: NotRequired[
            Optional["SetupIntent.ConfirmParamsPaymentMethodDataOxxo"]
        ]
        p24: NotRequired[
            Optional["SetupIntent.ConfirmParamsPaymentMethodDataP24"]
        ]
        paynow: NotRequired[
            Optional["SetupIntent.ConfirmParamsPaymentMethodDataPaynow"]
        ]
        paypal: NotRequired[
            Optional["SetupIntent.ConfirmParamsPaymentMethodDataPaypal"]
        ]
        pix: NotRequired[
            Optional["SetupIntent.ConfirmParamsPaymentMethodDataPix"]
        ]
        promptpay: NotRequired[
            Optional["SetupIntent.ConfirmParamsPaymentMethodDataPromptpay"]
        ]
        radar_options: NotRequired[
            Optional["SetupIntent.ConfirmParamsPaymentMethodDataRadarOptions"]
        ]
        sepa_debit: NotRequired[
            Optional["SetupIntent.ConfirmParamsPaymentMethodDataSepaDebit"]
        ]
        sofort: NotRequired[
            Optional["SetupIntent.ConfirmParamsPaymentMethodDataSofort"]
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
            Optional["SetupIntent.ConfirmParamsPaymentMethodDataUsBankAccount"]
        ]
        wechat_pay: NotRequired[
            Optional["SetupIntent.ConfirmParamsPaymentMethodDataWechatPay"]
        ]
        zip: NotRequired[
            Optional["SetupIntent.ConfirmParamsPaymentMethodDataZip"]
        ]

    class ConfirmParamsPaymentMethodDataZip(TypedDict):
        pass

    class ConfirmParamsPaymentMethodDataWechatPay(TypedDict):
        pass

    class ConfirmParamsPaymentMethodDataUsBankAccount(TypedDict):
        account_holder_type: NotRequired[
            Optional[Literal["company", "individual"]]
        ]
        account_number: NotRequired[Optional[str]]
        account_type: NotRequired[Optional[Literal["checking", "savings"]]]
        financial_connections_account: NotRequired[Optional[str]]
        routing_number: NotRequired[Optional[str]]

    class ConfirmParamsPaymentMethodDataSofort(TypedDict):
        country: Literal["AT", "BE", "DE", "ES", "IT", "NL"]

    class ConfirmParamsPaymentMethodDataSepaDebit(TypedDict):
        iban: str

    class ConfirmParamsPaymentMethodDataRadarOptions(TypedDict):
        session: NotRequired[Optional[str]]

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
            Optional[
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
        ]

    class ConfirmParamsPaymentMethodDataOxxo(TypedDict):
        pass

    class ConfirmParamsPaymentMethodDataLink(TypedDict):
        pass

    class ConfirmParamsPaymentMethodDataKonbini(TypedDict):
        pass

    class ConfirmParamsPaymentMethodDataKlarna(TypedDict):
        dob: NotRequired[
            Optional["SetupIntent.ConfirmParamsPaymentMethodDataKlarnaDob"]
        ]

    class ConfirmParamsPaymentMethodDataKlarnaDob(TypedDict):
        day: int
        month: int
        year: int

    class ConfirmParamsPaymentMethodDataInteracPresent(TypedDict):
        pass

    class ConfirmParamsPaymentMethodDataIdeal(TypedDict):
        bank: NotRequired[
            Optional[
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
        ]

    class ConfirmParamsPaymentMethodDataGrabpay(TypedDict):
        pass

    class ConfirmParamsPaymentMethodDataGiropay(TypedDict):
        pass

    class ConfirmParamsPaymentMethodDataFpx(TypedDict):
        account_holder_type: NotRequired[
            Optional[Literal["company", "individual"]]
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
            Optional[
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
            Optional[
                Union[
                    Literal[""],
                    "SetupIntent.ConfirmParamsPaymentMethodDataBillingDetailsAddress",
                ]
            ]
        ]
        email: NotRequired[Optional[Union[Literal[""], str]]]
        name: NotRequired[Optional[Union[Literal[""], str]]]
        phone: NotRequired[Optional[Union[Literal[""], str]]]

    class ConfirmParamsPaymentMethodDataBillingDetailsAddress(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class ConfirmParamsPaymentMethodDataBancontact(TypedDict):
        pass

    class ConfirmParamsPaymentMethodDataBacsDebit(TypedDict):
        account_number: NotRequired[Optional[str]]
        sort_code: NotRequired[Optional[str]]

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

    class ConfirmParamsMandateData(TypedDict):
        customer_acceptance: "SetupIntent.ConfirmParamsMandateDataCustomerAcceptance"

    class ConfirmParamsMandateDataCustomerAcceptance(TypedDict):
        online: "SetupIntent.ConfirmParamsMandateDataCustomerAcceptanceOnline"
        type: Literal["online"]

    class ConfirmParamsMandateDataCustomerAcceptanceOnline(TypedDict):
        ip_address: NotRequired[Optional[str]]
        user_agent: NotRequired[Optional[str]]

    class CreateParams(RequestOptions):
        attach_to_self: NotRequired[Optional[bool]]
        automatic_payment_methods: NotRequired[
            Optional["SetupIntent.CreateParamsAutomaticPaymentMethods"]
        ]
        confirm: NotRequired[Optional[bool]]
        customer: NotRequired[Optional[str]]
        description: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        flow_directions: NotRequired[
            Optional[List[Literal["inbound", "outbound"]]]
        ]
        mandate_data: NotRequired[
            Optional[Union[Literal[""], "SetupIntent.CreateParamsMandateData"]]
        ]
        metadata: NotRequired[Optional[Dict[str, str]]]
        on_behalf_of: NotRequired[Optional[str]]
        payment_method: NotRequired[Optional[str]]
        payment_method_configuration: NotRequired[Optional[str]]
        payment_method_data: NotRequired[
            Optional["SetupIntent.CreateParamsPaymentMethodData"]
        ]
        payment_method_options: NotRequired[
            Optional["SetupIntent.CreateParamsPaymentMethodOptions"]
        ]
        payment_method_types: NotRequired[Optional[List[str]]]
        return_url: NotRequired[Optional[str]]
        single_use: NotRequired[Optional["SetupIntent.CreateParamsSingleUse"]]
        usage: NotRequired[Optional[Literal["off_session", "on_session"]]]
        use_stripe_sdk: NotRequired[Optional[bool]]

    class CreateParamsSingleUse(TypedDict):
        amount: int
        currency: str

    class CreateParamsPaymentMethodOptions(TypedDict):
        acss_debit: NotRequired[
            Optional["SetupIntent.CreateParamsPaymentMethodOptionsAcssDebit"]
        ]
        card: NotRequired[
            Optional["SetupIntent.CreateParamsPaymentMethodOptionsCard"]
        ]
        link: NotRequired[
            Optional["SetupIntent.CreateParamsPaymentMethodOptionsLink"]
        ]
        paypal: NotRequired[
            Optional["SetupIntent.CreateParamsPaymentMethodOptionsPaypal"]
        ]
        sepa_debit: NotRequired[
            Optional["SetupIntent.CreateParamsPaymentMethodOptionsSepaDebit"]
        ]
        us_bank_account: NotRequired[
            Optional[
                "SetupIntent.CreateParamsPaymentMethodOptionsUsBankAccount"
            ]
        ]

    class CreateParamsPaymentMethodOptionsUsBankAccount(TypedDict):
        financial_connections: NotRequired[
            Optional[
                "SetupIntent.CreateParamsPaymentMethodOptionsUsBankAccountFinancialConnections"
            ]
        ]
        networks: NotRequired[
            Optional[
                "SetupIntent.CreateParamsPaymentMethodOptionsUsBankAccountNetworks"
            ]
        ]
        verification_method: NotRequired[
            Optional[Literal["automatic", "instant", "microdeposits"]]
        ]

    class CreateParamsPaymentMethodOptionsUsBankAccountNetworks(TypedDict):
        requested: NotRequired[
            Optional[List[Literal["ach", "us_domestic_wire"]]]
        ]

    class CreateParamsPaymentMethodOptionsUsBankAccountFinancialConnections(
        TypedDict,
    ):
        permissions: NotRequired[
            Optional[
                List[
                    Literal[
                        "balances",
                        "ownership",
                        "payment_method",
                        "transactions",
                    ]
                ]
            ]
        ]
        prefetch: NotRequired[Optional[List[Literal["balances"]]]]
        return_url: NotRequired[Optional[str]]

    class CreateParamsPaymentMethodOptionsSepaDebit(TypedDict):
        mandate_options: NotRequired[
            Optional[
                "SetupIntent.CreateParamsPaymentMethodOptionsSepaDebitMandateOptions"
            ]
        ]

    class CreateParamsPaymentMethodOptionsSepaDebitMandateOptions(TypedDict):
        pass

    class CreateParamsPaymentMethodOptionsPaypal(TypedDict):
        billing_agreement_id: NotRequired[Optional[str]]

    class CreateParamsPaymentMethodOptionsLink(TypedDict):
        persistent_token: NotRequired[Optional[str]]

    class CreateParamsPaymentMethodOptionsCard(TypedDict):
        mandate_options: NotRequired[
            Optional[
                "SetupIntent.CreateParamsPaymentMethodOptionsCardMandateOptions"
            ]
        ]
        moto: NotRequired[Optional[bool]]
        network: NotRequired[
            Optional[
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
        ]
        request_three_d_secure: NotRequired[
            Optional[Literal["any", "automatic"]]
        ]

    class CreateParamsPaymentMethodOptionsCardMandateOptions(TypedDict):
        amount: int
        amount_type: Literal["fixed", "maximum"]
        currency: str
        description: NotRequired[Optional[str]]
        end_date: NotRequired[Optional[int]]
        interval: Literal["day", "month", "sporadic", "week", "year"]
        interval_count: NotRequired[Optional[int]]
        reference: str
        start_date: int
        supported_types: NotRequired[Optional[List[Literal["india"]]]]

    class CreateParamsPaymentMethodOptionsAcssDebit(TypedDict):
        currency: NotRequired[Optional[Literal["cad", "usd"]]]
        mandate_options: NotRequired[
            Optional[
                "SetupIntent.CreateParamsPaymentMethodOptionsAcssDebitMandateOptions"
            ]
        ]
        verification_method: NotRequired[
            Optional[Literal["automatic", "instant", "microdeposits"]]
        ]

    class CreateParamsPaymentMethodOptionsAcssDebitMandateOptions(TypedDict):
        custom_mandate_url: NotRequired[Optional[Union[Literal[""], str]]]
        default_for: NotRequired[
            Optional[List[Literal["invoice", "subscription"]]]
        ]
        interval_description: NotRequired[Optional[str]]
        payment_schedule: NotRequired[
            Optional[Literal["combined", "interval", "sporadic"]]
        ]
        transaction_type: NotRequired[
            Optional[Literal["business", "personal"]]
        ]

    class CreateParamsPaymentMethodData(TypedDict):
        acss_debit: NotRequired[
            Optional["SetupIntent.CreateParamsPaymentMethodDataAcssDebit"]
        ]
        affirm: NotRequired[
            Optional["SetupIntent.CreateParamsPaymentMethodDataAffirm"]
        ]
        afterpay_clearpay: NotRequired[
            Optional[
                "SetupIntent.CreateParamsPaymentMethodDataAfterpayClearpay"
            ]
        ]
        alipay: NotRequired[
            Optional["SetupIntent.CreateParamsPaymentMethodDataAlipay"]
        ]
        au_becs_debit: NotRequired[
            Optional["SetupIntent.CreateParamsPaymentMethodDataAuBecsDebit"]
        ]
        bacs_debit: NotRequired[
            Optional["SetupIntent.CreateParamsPaymentMethodDataBacsDebit"]
        ]
        bancontact: NotRequired[
            Optional["SetupIntent.CreateParamsPaymentMethodDataBancontact"]
        ]
        billing_details: NotRequired[
            Optional["SetupIntent.CreateParamsPaymentMethodDataBillingDetails"]
        ]
        blik: NotRequired[
            Optional["SetupIntent.CreateParamsPaymentMethodDataBlik"]
        ]
        boleto: NotRequired[
            Optional["SetupIntent.CreateParamsPaymentMethodDataBoleto"]
        ]
        cashapp: NotRequired[
            Optional["SetupIntent.CreateParamsPaymentMethodDataCashapp"]
        ]
        customer_balance: NotRequired[
            Optional[
                "SetupIntent.CreateParamsPaymentMethodDataCustomerBalance"
            ]
        ]
        eps: NotRequired[
            Optional["SetupIntent.CreateParamsPaymentMethodDataEps"]
        ]
        fpx: NotRequired[
            Optional["SetupIntent.CreateParamsPaymentMethodDataFpx"]
        ]
        giropay: NotRequired[
            Optional["SetupIntent.CreateParamsPaymentMethodDataGiropay"]
        ]
        grabpay: NotRequired[
            Optional["SetupIntent.CreateParamsPaymentMethodDataGrabpay"]
        ]
        ideal: NotRequired[
            Optional["SetupIntent.CreateParamsPaymentMethodDataIdeal"]
        ]
        interac_present: NotRequired[
            Optional["SetupIntent.CreateParamsPaymentMethodDataInteracPresent"]
        ]
        klarna: NotRequired[
            Optional["SetupIntent.CreateParamsPaymentMethodDataKlarna"]
        ]
        konbini: NotRequired[
            Optional["SetupIntent.CreateParamsPaymentMethodDataKonbini"]
        ]
        link: NotRequired[
            Optional["SetupIntent.CreateParamsPaymentMethodDataLink"]
        ]
        metadata: NotRequired[Optional[Dict[str, str]]]
        oxxo: NotRequired[
            Optional["SetupIntent.CreateParamsPaymentMethodDataOxxo"]
        ]
        p24: NotRequired[
            Optional["SetupIntent.CreateParamsPaymentMethodDataP24"]
        ]
        paynow: NotRequired[
            Optional["SetupIntent.CreateParamsPaymentMethodDataPaynow"]
        ]
        paypal: NotRequired[
            Optional["SetupIntent.CreateParamsPaymentMethodDataPaypal"]
        ]
        pix: NotRequired[
            Optional["SetupIntent.CreateParamsPaymentMethodDataPix"]
        ]
        promptpay: NotRequired[
            Optional["SetupIntent.CreateParamsPaymentMethodDataPromptpay"]
        ]
        radar_options: NotRequired[
            Optional["SetupIntent.CreateParamsPaymentMethodDataRadarOptions"]
        ]
        sepa_debit: NotRequired[
            Optional["SetupIntent.CreateParamsPaymentMethodDataSepaDebit"]
        ]
        sofort: NotRequired[
            Optional["SetupIntent.CreateParamsPaymentMethodDataSofort"]
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
            Optional["SetupIntent.CreateParamsPaymentMethodDataUsBankAccount"]
        ]
        wechat_pay: NotRequired[
            Optional["SetupIntent.CreateParamsPaymentMethodDataWechatPay"]
        ]
        zip: NotRequired[
            Optional["SetupIntent.CreateParamsPaymentMethodDataZip"]
        ]

    class CreateParamsPaymentMethodDataZip(TypedDict):
        pass

    class CreateParamsPaymentMethodDataWechatPay(TypedDict):
        pass

    class CreateParamsPaymentMethodDataUsBankAccount(TypedDict):
        account_holder_type: NotRequired[
            Optional[Literal["company", "individual"]]
        ]
        account_number: NotRequired[Optional[str]]
        account_type: NotRequired[Optional[Literal["checking", "savings"]]]
        financial_connections_account: NotRequired[Optional[str]]
        routing_number: NotRequired[Optional[str]]

    class CreateParamsPaymentMethodDataSofort(TypedDict):
        country: Literal["AT", "BE", "DE", "ES", "IT", "NL"]

    class CreateParamsPaymentMethodDataSepaDebit(TypedDict):
        iban: str

    class CreateParamsPaymentMethodDataRadarOptions(TypedDict):
        session: NotRequired[Optional[str]]

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
            Optional[
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
        ]

    class CreateParamsPaymentMethodDataOxxo(TypedDict):
        pass

    class CreateParamsPaymentMethodDataLink(TypedDict):
        pass

    class CreateParamsPaymentMethodDataKonbini(TypedDict):
        pass

    class CreateParamsPaymentMethodDataKlarna(TypedDict):
        dob: NotRequired[
            Optional["SetupIntent.CreateParamsPaymentMethodDataKlarnaDob"]
        ]

    class CreateParamsPaymentMethodDataKlarnaDob(TypedDict):
        day: int
        month: int
        year: int

    class CreateParamsPaymentMethodDataInteracPresent(TypedDict):
        pass

    class CreateParamsPaymentMethodDataIdeal(TypedDict):
        bank: NotRequired[
            Optional[
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
        ]

    class CreateParamsPaymentMethodDataGrabpay(TypedDict):
        pass

    class CreateParamsPaymentMethodDataGiropay(TypedDict):
        pass

    class CreateParamsPaymentMethodDataFpx(TypedDict):
        account_holder_type: NotRequired[
            Optional[Literal["company", "individual"]]
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
            Optional[
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
            Optional[
                Union[
                    Literal[""],
                    "SetupIntent.CreateParamsPaymentMethodDataBillingDetailsAddress",
                ]
            ]
        ]
        email: NotRequired[Optional[Union[Literal[""], str]]]
        name: NotRequired[Optional[Union[Literal[""], str]]]
        phone: NotRequired[Optional[Union[Literal[""], str]]]

    class CreateParamsPaymentMethodDataBillingDetailsAddress(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class CreateParamsPaymentMethodDataBancontact(TypedDict):
        pass

    class CreateParamsPaymentMethodDataBacsDebit(TypedDict):
        account_number: NotRequired[Optional[str]]
        sort_code: NotRequired[Optional[str]]

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
        accepted_at: NotRequired[Optional[int]]
        offline: NotRequired[
            Optional[
                "SetupIntent.CreateParamsMandateDataCustomerAcceptanceOffline"
            ]
        ]
        online: NotRequired[
            Optional[
                "SetupIntent.CreateParamsMandateDataCustomerAcceptanceOnline"
            ]
        ]
        type: Literal["offline", "online"]

    class CreateParamsMandateDataCustomerAcceptanceOnline(TypedDict):
        ip_address: str
        user_agent: str

    class CreateParamsMandateDataCustomerAcceptanceOffline(TypedDict):
        pass

    class CreateParamsAutomaticPaymentMethods(TypedDict):
        allow_redirects: NotRequired[Optional[Literal["always", "never"]]]
        enabled: bool

    class ListParams(RequestOptions):
        attach_to_self: NotRequired[Optional[bool]]
        created: NotRequired[
            Optional[Union["SetupIntent.ListParamsCreated", int]]
        ]
        customer: NotRequired[Optional[str]]
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        payment_method: NotRequired[Optional[str]]
        starting_after: NotRequired[Optional[str]]

    class ListParamsCreated(TypedDict):
        gt: NotRequired[Optional[int]]
        gte: NotRequired[Optional[int]]
        lt: NotRequired[Optional[int]]
        lte: NotRequired[Optional[int]]

    class ModifyParams(RequestOptions):
        attach_to_self: NotRequired[Optional[bool]]
        customer: NotRequired[Optional[str]]
        description: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        flow_directions: NotRequired[
            Optional[List[Literal["inbound", "outbound"]]]
        ]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]
        payment_method: NotRequired[Optional[str]]
        payment_method_configuration: NotRequired[Optional[str]]
        payment_method_data: NotRequired[
            Optional["SetupIntent.ModifyParamsPaymentMethodData"]
        ]
        payment_method_options: NotRequired[
            Optional["SetupIntent.ModifyParamsPaymentMethodOptions"]
        ]
        payment_method_types: NotRequired[Optional[List[str]]]

    class ModifyParamsPaymentMethodOptions(TypedDict):
        acss_debit: NotRequired[
            Optional["SetupIntent.ModifyParamsPaymentMethodOptionsAcssDebit"]
        ]
        card: NotRequired[
            Optional["SetupIntent.ModifyParamsPaymentMethodOptionsCard"]
        ]
        link: NotRequired[
            Optional["SetupIntent.ModifyParamsPaymentMethodOptionsLink"]
        ]
        paypal: NotRequired[
            Optional["SetupIntent.ModifyParamsPaymentMethodOptionsPaypal"]
        ]
        sepa_debit: NotRequired[
            Optional["SetupIntent.ModifyParamsPaymentMethodOptionsSepaDebit"]
        ]
        us_bank_account: NotRequired[
            Optional[
                "SetupIntent.ModifyParamsPaymentMethodOptionsUsBankAccount"
            ]
        ]

    class ModifyParamsPaymentMethodOptionsUsBankAccount(TypedDict):
        financial_connections: NotRequired[
            Optional[
                "SetupIntent.ModifyParamsPaymentMethodOptionsUsBankAccountFinancialConnections"
            ]
        ]
        networks: NotRequired[
            Optional[
                "SetupIntent.ModifyParamsPaymentMethodOptionsUsBankAccountNetworks"
            ]
        ]
        verification_method: NotRequired[
            Optional[Literal["automatic", "instant", "microdeposits"]]
        ]

    class ModifyParamsPaymentMethodOptionsUsBankAccountNetworks(TypedDict):
        requested: NotRequired[
            Optional[List[Literal["ach", "us_domestic_wire"]]]
        ]

    class ModifyParamsPaymentMethodOptionsUsBankAccountFinancialConnections(
        TypedDict,
    ):
        permissions: NotRequired[
            Optional[
                List[
                    Literal[
                        "balances",
                        "ownership",
                        "payment_method",
                        "transactions",
                    ]
                ]
            ]
        ]
        prefetch: NotRequired[Optional[List[Literal["balances"]]]]
        return_url: NotRequired[Optional[str]]

    class ModifyParamsPaymentMethodOptionsSepaDebit(TypedDict):
        mandate_options: NotRequired[
            Optional[
                "SetupIntent.ModifyParamsPaymentMethodOptionsSepaDebitMandateOptions"
            ]
        ]

    class ModifyParamsPaymentMethodOptionsSepaDebitMandateOptions(TypedDict):
        pass

    class ModifyParamsPaymentMethodOptionsPaypal(TypedDict):
        billing_agreement_id: NotRequired[Optional[str]]

    class ModifyParamsPaymentMethodOptionsLink(TypedDict):
        persistent_token: NotRequired[Optional[str]]

    class ModifyParamsPaymentMethodOptionsCard(TypedDict):
        mandate_options: NotRequired[
            Optional[
                "SetupIntent.ModifyParamsPaymentMethodOptionsCardMandateOptions"
            ]
        ]
        moto: NotRequired[Optional[bool]]
        network: NotRequired[
            Optional[
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
        ]
        request_three_d_secure: NotRequired[
            Optional[Literal["any", "automatic"]]
        ]

    class ModifyParamsPaymentMethodOptionsCardMandateOptions(TypedDict):
        amount: int
        amount_type: Literal["fixed", "maximum"]
        currency: str
        description: NotRequired[Optional[str]]
        end_date: NotRequired[Optional[int]]
        interval: Literal["day", "month", "sporadic", "week", "year"]
        interval_count: NotRequired[Optional[int]]
        reference: str
        start_date: int
        supported_types: NotRequired[Optional[List[Literal["india"]]]]

    class ModifyParamsPaymentMethodOptionsAcssDebit(TypedDict):
        currency: NotRequired[Optional[Literal["cad", "usd"]]]
        mandate_options: NotRequired[
            Optional[
                "SetupIntent.ModifyParamsPaymentMethodOptionsAcssDebitMandateOptions"
            ]
        ]
        verification_method: NotRequired[
            Optional[Literal["automatic", "instant", "microdeposits"]]
        ]

    class ModifyParamsPaymentMethodOptionsAcssDebitMandateOptions(TypedDict):
        custom_mandate_url: NotRequired[Optional[Union[Literal[""], str]]]
        default_for: NotRequired[
            Optional[List[Literal["invoice", "subscription"]]]
        ]
        interval_description: NotRequired[Optional[str]]
        payment_schedule: NotRequired[
            Optional[Literal["combined", "interval", "sporadic"]]
        ]
        transaction_type: NotRequired[
            Optional[Literal["business", "personal"]]
        ]

    class ModifyParamsPaymentMethodData(TypedDict):
        acss_debit: NotRequired[
            Optional["SetupIntent.ModifyParamsPaymentMethodDataAcssDebit"]
        ]
        affirm: NotRequired[
            Optional["SetupIntent.ModifyParamsPaymentMethodDataAffirm"]
        ]
        afterpay_clearpay: NotRequired[
            Optional[
                "SetupIntent.ModifyParamsPaymentMethodDataAfterpayClearpay"
            ]
        ]
        alipay: NotRequired[
            Optional["SetupIntent.ModifyParamsPaymentMethodDataAlipay"]
        ]
        au_becs_debit: NotRequired[
            Optional["SetupIntent.ModifyParamsPaymentMethodDataAuBecsDebit"]
        ]
        bacs_debit: NotRequired[
            Optional["SetupIntent.ModifyParamsPaymentMethodDataBacsDebit"]
        ]
        bancontact: NotRequired[
            Optional["SetupIntent.ModifyParamsPaymentMethodDataBancontact"]
        ]
        billing_details: NotRequired[
            Optional["SetupIntent.ModifyParamsPaymentMethodDataBillingDetails"]
        ]
        blik: NotRequired[
            Optional["SetupIntent.ModifyParamsPaymentMethodDataBlik"]
        ]
        boleto: NotRequired[
            Optional["SetupIntent.ModifyParamsPaymentMethodDataBoleto"]
        ]
        cashapp: NotRequired[
            Optional["SetupIntent.ModifyParamsPaymentMethodDataCashapp"]
        ]
        customer_balance: NotRequired[
            Optional[
                "SetupIntent.ModifyParamsPaymentMethodDataCustomerBalance"
            ]
        ]
        eps: NotRequired[
            Optional["SetupIntent.ModifyParamsPaymentMethodDataEps"]
        ]
        fpx: NotRequired[
            Optional["SetupIntent.ModifyParamsPaymentMethodDataFpx"]
        ]
        giropay: NotRequired[
            Optional["SetupIntent.ModifyParamsPaymentMethodDataGiropay"]
        ]
        grabpay: NotRequired[
            Optional["SetupIntent.ModifyParamsPaymentMethodDataGrabpay"]
        ]
        ideal: NotRequired[
            Optional["SetupIntent.ModifyParamsPaymentMethodDataIdeal"]
        ]
        interac_present: NotRequired[
            Optional["SetupIntent.ModifyParamsPaymentMethodDataInteracPresent"]
        ]
        klarna: NotRequired[
            Optional["SetupIntent.ModifyParamsPaymentMethodDataKlarna"]
        ]
        konbini: NotRequired[
            Optional["SetupIntent.ModifyParamsPaymentMethodDataKonbini"]
        ]
        link: NotRequired[
            Optional["SetupIntent.ModifyParamsPaymentMethodDataLink"]
        ]
        metadata: NotRequired[Optional[Dict[str, str]]]
        oxxo: NotRequired[
            Optional["SetupIntent.ModifyParamsPaymentMethodDataOxxo"]
        ]
        p24: NotRequired[
            Optional["SetupIntent.ModifyParamsPaymentMethodDataP24"]
        ]
        paynow: NotRequired[
            Optional["SetupIntent.ModifyParamsPaymentMethodDataPaynow"]
        ]
        paypal: NotRequired[
            Optional["SetupIntent.ModifyParamsPaymentMethodDataPaypal"]
        ]
        pix: NotRequired[
            Optional["SetupIntent.ModifyParamsPaymentMethodDataPix"]
        ]
        promptpay: NotRequired[
            Optional["SetupIntent.ModifyParamsPaymentMethodDataPromptpay"]
        ]
        radar_options: NotRequired[
            Optional["SetupIntent.ModifyParamsPaymentMethodDataRadarOptions"]
        ]
        sepa_debit: NotRequired[
            Optional["SetupIntent.ModifyParamsPaymentMethodDataSepaDebit"]
        ]
        sofort: NotRequired[
            Optional["SetupIntent.ModifyParamsPaymentMethodDataSofort"]
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
            Optional["SetupIntent.ModifyParamsPaymentMethodDataUsBankAccount"]
        ]
        wechat_pay: NotRequired[
            Optional["SetupIntent.ModifyParamsPaymentMethodDataWechatPay"]
        ]
        zip: NotRequired[
            Optional["SetupIntent.ModifyParamsPaymentMethodDataZip"]
        ]

    class ModifyParamsPaymentMethodDataZip(TypedDict):
        pass

    class ModifyParamsPaymentMethodDataWechatPay(TypedDict):
        pass

    class ModifyParamsPaymentMethodDataUsBankAccount(TypedDict):
        account_holder_type: NotRequired[
            Optional[Literal["company", "individual"]]
        ]
        account_number: NotRequired[Optional[str]]
        account_type: NotRequired[Optional[Literal["checking", "savings"]]]
        financial_connections_account: NotRequired[Optional[str]]
        routing_number: NotRequired[Optional[str]]

    class ModifyParamsPaymentMethodDataSofort(TypedDict):
        country: Literal["AT", "BE", "DE", "ES", "IT", "NL"]

    class ModifyParamsPaymentMethodDataSepaDebit(TypedDict):
        iban: str

    class ModifyParamsPaymentMethodDataRadarOptions(TypedDict):
        session: NotRequired[Optional[str]]

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
            Optional[
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
        ]

    class ModifyParamsPaymentMethodDataOxxo(TypedDict):
        pass

    class ModifyParamsPaymentMethodDataLink(TypedDict):
        pass

    class ModifyParamsPaymentMethodDataKonbini(TypedDict):
        pass

    class ModifyParamsPaymentMethodDataKlarna(TypedDict):
        dob: NotRequired[
            Optional["SetupIntent.ModifyParamsPaymentMethodDataKlarnaDob"]
        ]

    class ModifyParamsPaymentMethodDataKlarnaDob(TypedDict):
        day: int
        month: int
        year: int

    class ModifyParamsPaymentMethodDataInteracPresent(TypedDict):
        pass

    class ModifyParamsPaymentMethodDataIdeal(TypedDict):
        bank: NotRequired[
            Optional[
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
        ]

    class ModifyParamsPaymentMethodDataGrabpay(TypedDict):
        pass

    class ModifyParamsPaymentMethodDataGiropay(TypedDict):
        pass

    class ModifyParamsPaymentMethodDataFpx(TypedDict):
        account_holder_type: NotRequired[
            Optional[Literal["company", "individual"]]
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
            Optional[
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
            Optional[
                Union[
                    Literal[""],
                    "SetupIntent.ModifyParamsPaymentMethodDataBillingDetailsAddress",
                ]
            ]
        ]
        email: NotRequired[Optional[Union[Literal[""], str]]]
        name: NotRequired[Optional[Union[Literal[""], str]]]
        phone: NotRequired[Optional[Union[Literal[""], str]]]

    class ModifyParamsPaymentMethodDataBillingDetailsAddress(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class ModifyParamsPaymentMethodDataBancontact(TypedDict):
        pass

    class ModifyParamsPaymentMethodDataBacsDebit(TypedDict):
        account_number: NotRequired[Optional[str]]
        sort_code: NotRequired[Optional[str]]

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
        client_secret: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]

    class VerifyMicrodepositsParams(RequestOptions):
        amounts: NotRequired[Optional[List[int]]]
        descriptor_code: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]

    application: Optional[ExpandableField["Application"]]
    attach_to_self: Optional[bool]
    automatic_payment_methods: Optional[StripeObject]
    cancellation_reason: Optional[
        Literal["abandoned", "duplicate", "requested_by_customer"]
    ]
    client_secret: Optional[str]
    created: int
    customer: Optional[ExpandableField["Customer"]]
    description: Optional[str]
    flow_directions: Optional[List[Literal["inbound", "outbound"]]]
    id: str
    last_setup_error: Optional[StripeObject]
    latest_attempt: Optional[ExpandableField["SetupAttempt"]]
    livemode: bool
    mandate: Optional[ExpandableField["Mandate"]]
    metadata: Optional[Dict[str, str]]
    next_action: Optional[StripeObject]
    object: Literal["setup_intent"]
    on_behalf_of: Optional[ExpandableField["Account"]]
    payment_method: Optional[ExpandableField["PaymentMethod"]]
    payment_method_configuration_details: Optional[StripeObject]
    payment_method_options: Optional[StripeObject]
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
