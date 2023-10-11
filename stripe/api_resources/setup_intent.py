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
                        "SetupIntent.ConfirmMandateDataParams",
                        "SetupIntent.ConfirmMandateDataParams",
                    ],
                ]
            ]
        ]
        payment_method: NotRequired[Optional[str]]
        payment_method_data: NotRequired[
            Optional["SetupIntent.ConfirmPaymentMethodDataParams"]
        ]
        payment_method_options: NotRequired[
            Optional["SetupIntent.ConfirmPaymentMethodOptionsParams"]
        ]
        return_url: NotRequired[Optional[str]]
        use_stripe_sdk: NotRequired[Optional[bool]]

    class ConfirmPaymentMethodOptionsParams(TypedDict):
        acss_debit: NotRequired[
            Optional["SetupIntent.ConfirmPaymentMethodOptionsAcssDebitParams"]
        ]
        card: NotRequired[
            Optional["SetupIntent.ConfirmPaymentMethodOptionsCardParams"]
        ]
        link: NotRequired[
            Optional["SetupIntent.ConfirmPaymentMethodOptionsLinkParams"]
        ]
        paypal: NotRequired[
            Optional["SetupIntent.ConfirmPaymentMethodOptionsPaypalParams"]
        ]
        sepa_debit: NotRequired[
            Optional["SetupIntent.ConfirmPaymentMethodOptionsSepaDebitParams"]
        ]
        us_bank_account: NotRequired[
            Optional[
                "SetupIntent.ConfirmPaymentMethodOptionsUsBankAccountParams"
            ]
        ]

    class ConfirmPaymentMethodOptionsUsBankAccountParams(TypedDict):
        financial_connections: NotRequired[
            Optional[
                "SetupIntent.ConfirmPaymentMethodOptionsUsBankAccountFinancialConnectionsParams"
            ]
        ]
        networks: NotRequired[
            Optional[
                "SetupIntent.ConfirmPaymentMethodOptionsUsBankAccountNetworksParams"
            ]
        ]
        verification_method: NotRequired[
            Optional[Literal["automatic", "instant", "microdeposits"]]
        ]

    class ConfirmPaymentMethodOptionsUsBankAccountNetworksParams(TypedDict):
        requested: NotRequired[
            Optional[List[Literal["ach", "us_domestic_wire"]]]
        ]

    class ConfirmPaymentMethodOptionsUsBankAccountFinancialConnectionsParams(
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

    class ConfirmPaymentMethodOptionsSepaDebitParams(TypedDict):
        mandate_options: NotRequired[
            Optional[
                "SetupIntent.ConfirmPaymentMethodOptionsSepaDebitMandateOptionsParams"
            ]
        ]

    class ConfirmPaymentMethodOptionsSepaDebitMandateOptionsParams(TypedDict):
        pass

    class ConfirmPaymentMethodOptionsPaypalParams(TypedDict):
        billing_agreement_id: NotRequired[Optional[str]]

    class ConfirmPaymentMethodOptionsLinkParams(TypedDict):
        persistent_token: NotRequired[Optional[str]]

    class ConfirmPaymentMethodOptionsCardParams(TypedDict):
        mandate_options: NotRequired[
            Optional[
                "SetupIntent.ConfirmPaymentMethodOptionsCardMandateOptionsParams"
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

    class ConfirmPaymentMethodOptionsCardMandateOptionsParams(TypedDict):
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

    class ConfirmPaymentMethodOptionsAcssDebitParams(TypedDict):
        currency: NotRequired[Optional[Literal["cad", "usd"]]]
        mandate_options: NotRequired[
            Optional[
                "SetupIntent.ConfirmPaymentMethodOptionsAcssDebitMandateOptionsParams"
            ]
        ]
        verification_method: NotRequired[
            Optional[Literal["automatic", "instant", "microdeposits"]]
        ]

    class ConfirmPaymentMethodOptionsAcssDebitMandateOptionsParams(TypedDict):
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

    class ConfirmPaymentMethodDataParams(TypedDict):
        acss_debit: NotRequired[
            Optional["SetupIntent.ConfirmPaymentMethodDataAcssDebitParams"]
        ]
        affirm: NotRequired[
            Optional["SetupIntent.ConfirmPaymentMethodDataAffirmParams"]
        ]
        afterpay_clearpay: NotRequired[
            Optional[
                "SetupIntent.ConfirmPaymentMethodDataAfterpayClearpayParams"
            ]
        ]
        alipay: NotRequired[
            Optional["SetupIntent.ConfirmPaymentMethodDataAlipayParams"]
        ]
        au_becs_debit: NotRequired[
            Optional["SetupIntent.ConfirmPaymentMethodDataAuBecsDebitParams"]
        ]
        bacs_debit: NotRequired[
            Optional["SetupIntent.ConfirmPaymentMethodDataBacsDebitParams"]
        ]
        bancontact: NotRequired[
            Optional["SetupIntent.ConfirmPaymentMethodDataBancontactParams"]
        ]
        billing_details: NotRequired[
            Optional[
                "SetupIntent.ConfirmPaymentMethodDataBillingDetailsParams"
            ]
        ]
        blik: NotRequired[
            Optional["SetupIntent.ConfirmPaymentMethodDataBlikParams"]
        ]
        boleto: NotRequired[
            Optional["SetupIntent.ConfirmPaymentMethodDataBoletoParams"]
        ]
        cashapp: NotRequired[
            Optional["SetupIntent.ConfirmPaymentMethodDataCashappParams"]
        ]
        customer_balance: NotRequired[
            Optional[
                "SetupIntent.ConfirmPaymentMethodDataCustomerBalanceParams"
            ]
        ]
        eps: NotRequired[
            Optional["SetupIntent.ConfirmPaymentMethodDataEpsParams"]
        ]
        fpx: NotRequired[
            Optional["SetupIntent.ConfirmPaymentMethodDataFpxParams"]
        ]
        giropay: NotRequired[
            Optional["SetupIntent.ConfirmPaymentMethodDataGiropayParams"]
        ]
        grabpay: NotRequired[
            Optional["SetupIntent.ConfirmPaymentMethodDataGrabpayParams"]
        ]
        ideal: NotRequired[
            Optional["SetupIntent.ConfirmPaymentMethodDataIdealParams"]
        ]
        interac_present: NotRequired[
            Optional[
                "SetupIntent.ConfirmPaymentMethodDataInteracPresentParams"
            ]
        ]
        klarna: NotRequired[
            Optional["SetupIntent.ConfirmPaymentMethodDataKlarnaParams"]
        ]
        konbini: NotRequired[
            Optional["SetupIntent.ConfirmPaymentMethodDataKonbiniParams"]
        ]
        link: NotRequired[
            Optional["SetupIntent.ConfirmPaymentMethodDataLinkParams"]
        ]
        metadata: NotRequired[Optional[Dict[str, str]]]
        oxxo: NotRequired[
            Optional["SetupIntent.ConfirmPaymentMethodDataOxxoParams"]
        ]
        p24: NotRequired[
            Optional["SetupIntent.ConfirmPaymentMethodDataP24Params"]
        ]
        paynow: NotRequired[
            Optional["SetupIntent.ConfirmPaymentMethodDataPaynowParams"]
        ]
        paypal: NotRequired[
            Optional["SetupIntent.ConfirmPaymentMethodDataPaypalParams"]
        ]
        pix: NotRequired[
            Optional["SetupIntent.ConfirmPaymentMethodDataPixParams"]
        ]
        promptpay: NotRequired[
            Optional["SetupIntent.ConfirmPaymentMethodDataPromptpayParams"]
        ]
        radar_options: NotRequired[
            Optional["SetupIntent.ConfirmPaymentMethodDataRadarOptionsParams"]
        ]
        sepa_debit: NotRequired[
            Optional["SetupIntent.ConfirmPaymentMethodDataSepaDebitParams"]
        ]
        sofort: NotRequired[
            Optional["SetupIntent.ConfirmPaymentMethodDataSofortParams"]
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
            Optional["SetupIntent.ConfirmPaymentMethodDataUsBankAccountParams"]
        ]
        wechat_pay: NotRequired[
            Optional["SetupIntent.ConfirmPaymentMethodDataWechatPayParams"]
        ]
        zip: NotRequired[
            Optional["SetupIntent.ConfirmPaymentMethodDataZipParams"]
        ]

    class ConfirmPaymentMethodDataZipParams(TypedDict):
        pass

    class ConfirmPaymentMethodDataWechatPayParams(TypedDict):
        pass

    class ConfirmPaymentMethodDataUsBankAccountParams(TypedDict):
        account_holder_type: NotRequired[
            Optional[Literal["company", "individual"]]
        ]
        account_number: NotRequired[Optional[str]]
        account_type: NotRequired[Optional[Literal["checking", "savings"]]]
        financial_connections_account: NotRequired[Optional[str]]
        routing_number: NotRequired[Optional[str]]

    class ConfirmPaymentMethodDataSofortParams(TypedDict):
        country: Literal["AT", "BE", "DE", "ES", "IT", "NL"]

    class ConfirmPaymentMethodDataSepaDebitParams(TypedDict):
        iban: str

    class ConfirmPaymentMethodDataRadarOptionsParams(TypedDict):
        session: NotRequired[Optional[str]]

    class ConfirmPaymentMethodDataPromptpayParams(TypedDict):
        pass

    class ConfirmPaymentMethodDataPixParams(TypedDict):
        pass

    class ConfirmPaymentMethodDataPaypalParams(TypedDict):
        pass

    class ConfirmPaymentMethodDataPaynowParams(TypedDict):
        pass

    class ConfirmPaymentMethodDataP24Params(TypedDict):
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

    class ConfirmPaymentMethodDataOxxoParams(TypedDict):
        pass

    class ConfirmPaymentMethodDataLinkParams(TypedDict):
        pass

    class ConfirmPaymentMethodDataKonbiniParams(TypedDict):
        pass

    class ConfirmPaymentMethodDataKlarnaParams(TypedDict):
        dob: NotRequired[
            Optional["SetupIntent.ConfirmPaymentMethodDataKlarnaDobParams"]
        ]

    class ConfirmPaymentMethodDataKlarnaDobParams(TypedDict):
        day: int
        month: int
        year: int

    class ConfirmPaymentMethodDataInteracPresentParams(TypedDict):
        pass

    class ConfirmPaymentMethodDataIdealParams(TypedDict):
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

    class ConfirmPaymentMethodDataGrabpayParams(TypedDict):
        pass

    class ConfirmPaymentMethodDataGiropayParams(TypedDict):
        pass

    class ConfirmPaymentMethodDataFpxParams(TypedDict):
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

    class ConfirmPaymentMethodDataEpsParams(TypedDict):
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

    class ConfirmPaymentMethodDataCustomerBalanceParams(TypedDict):
        pass

    class ConfirmPaymentMethodDataCashappParams(TypedDict):
        pass

    class ConfirmPaymentMethodDataBoletoParams(TypedDict):
        tax_id: str

    class ConfirmPaymentMethodDataBlikParams(TypedDict):
        pass

    class ConfirmPaymentMethodDataBillingDetailsParams(TypedDict):
        address: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "SetupIntent.ConfirmPaymentMethodDataBillingDetailsAddressParams",
                ]
            ]
        ]
        email: NotRequired[Optional[Union[Literal[""], str]]]
        name: NotRequired[Optional[Union[Literal[""], str]]]
        phone: NotRequired[Optional[Union[Literal[""], str]]]

    class ConfirmPaymentMethodDataBillingDetailsAddressParams(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class ConfirmPaymentMethodDataBancontactParams(TypedDict):
        pass

    class ConfirmPaymentMethodDataBacsDebitParams(TypedDict):
        account_number: NotRequired[Optional[str]]
        sort_code: NotRequired[Optional[str]]

    class ConfirmPaymentMethodDataAuBecsDebitParams(TypedDict):
        account_number: str
        bsb_number: str

    class ConfirmPaymentMethodDataAlipayParams(TypedDict):
        pass

    class ConfirmPaymentMethodDataAfterpayClearpayParams(TypedDict):
        pass

    class ConfirmPaymentMethodDataAffirmParams(TypedDict):
        pass

    class ConfirmPaymentMethodDataAcssDebitParams(TypedDict):
        account_number: str
        institution_number: str
        transit_number: str

    class ConfirmMandateDataParams(TypedDict):
        customer_acceptance: "SetupIntent.ConfirmMandateDataCustomerAcceptanceParams"

    class ConfirmMandateDataCustomerAcceptanceParams(TypedDict):
        online: "SetupIntent.ConfirmMandateDataCustomerAcceptanceOnlineParams"
        type: Literal["online"]

    class ConfirmMandateDataCustomerAcceptanceOnlineParams(TypedDict):
        ip_address: NotRequired[Optional[str]]
        user_agent: NotRequired[Optional[str]]

    class CreateParams(RequestOptions):
        attach_to_self: NotRequired[Optional[bool]]
        automatic_payment_methods: NotRequired[
            Optional["SetupIntent.CreateAutomaticPaymentMethodsParams"]
        ]
        confirm: NotRequired[Optional[bool]]
        customer: NotRequired[Optional[str]]
        description: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        flow_directions: NotRequired[
            Optional[List[Literal["inbound", "outbound"]]]
        ]
        mandate_data: NotRequired[
            Optional[Union[Literal[""], "SetupIntent.CreateMandateDataParams"]]
        ]
        metadata: NotRequired[Optional[Dict[str, str]]]
        on_behalf_of: NotRequired[Optional[str]]
        payment_method: NotRequired[Optional[str]]
        payment_method_configuration: NotRequired[Optional[str]]
        payment_method_data: NotRequired[
            Optional["SetupIntent.CreatePaymentMethodDataParams"]
        ]
        payment_method_options: NotRequired[
            Optional["SetupIntent.CreatePaymentMethodOptionsParams"]
        ]
        payment_method_types: NotRequired[Optional[List[str]]]
        return_url: NotRequired[Optional[str]]
        single_use: NotRequired[Optional["SetupIntent.CreateSingleUseParams"]]
        usage: NotRequired[Optional[Literal["off_session", "on_session"]]]
        use_stripe_sdk: NotRequired[Optional[bool]]

    class CreateSingleUseParams(TypedDict):
        amount: int
        currency: str

    class CreatePaymentMethodOptionsParams(TypedDict):
        acss_debit: NotRequired[
            Optional["SetupIntent.CreatePaymentMethodOptionsAcssDebitParams"]
        ]
        card: NotRequired[
            Optional["SetupIntent.CreatePaymentMethodOptionsCardParams"]
        ]
        link: NotRequired[
            Optional["SetupIntent.CreatePaymentMethodOptionsLinkParams"]
        ]
        paypal: NotRequired[
            Optional["SetupIntent.CreatePaymentMethodOptionsPaypalParams"]
        ]
        sepa_debit: NotRequired[
            Optional["SetupIntent.CreatePaymentMethodOptionsSepaDebitParams"]
        ]
        us_bank_account: NotRequired[
            Optional[
                "SetupIntent.CreatePaymentMethodOptionsUsBankAccountParams"
            ]
        ]

    class CreatePaymentMethodOptionsUsBankAccountParams(TypedDict):
        financial_connections: NotRequired[
            Optional[
                "SetupIntent.CreatePaymentMethodOptionsUsBankAccountFinancialConnectionsParams"
            ]
        ]
        networks: NotRequired[
            Optional[
                "SetupIntent.CreatePaymentMethodOptionsUsBankAccountNetworksParams"
            ]
        ]
        verification_method: NotRequired[
            Optional[Literal["automatic", "instant", "microdeposits"]]
        ]

    class CreatePaymentMethodOptionsUsBankAccountNetworksParams(TypedDict):
        requested: NotRequired[
            Optional[List[Literal["ach", "us_domestic_wire"]]]
        ]

    class CreatePaymentMethodOptionsUsBankAccountFinancialConnectionsParams(
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

    class CreatePaymentMethodOptionsSepaDebitParams(TypedDict):
        mandate_options: NotRequired[
            Optional[
                "SetupIntent.CreatePaymentMethodOptionsSepaDebitMandateOptionsParams"
            ]
        ]

    class CreatePaymentMethodOptionsSepaDebitMandateOptionsParams(TypedDict):
        pass

    class CreatePaymentMethodOptionsPaypalParams(TypedDict):
        billing_agreement_id: NotRequired[Optional[str]]

    class CreatePaymentMethodOptionsLinkParams(TypedDict):
        persistent_token: NotRequired[Optional[str]]

    class CreatePaymentMethodOptionsCardParams(TypedDict):
        mandate_options: NotRequired[
            Optional[
                "SetupIntent.CreatePaymentMethodOptionsCardMandateOptionsParams"
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

    class CreatePaymentMethodOptionsCardMandateOptionsParams(TypedDict):
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

    class CreatePaymentMethodOptionsAcssDebitParams(TypedDict):
        currency: NotRequired[Optional[Literal["cad", "usd"]]]
        mandate_options: NotRequired[
            Optional[
                "SetupIntent.CreatePaymentMethodOptionsAcssDebitMandateOptionsParams"
            ]
        ]
        verification_method: NotRequired[
            Optional[Literal["automatic", "instant", "microdeposits"]]
        ]

    class CreatePaymentMethodOptionsAcssDebitMandateOptionsParams(TypedDict):
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

    class CreatePaymentMethodDataParams(TypedDict):
        acss_debit: NotRequired[
            Optional["SetupIntent.CreatePaymentMethodDataAcssDebitParams"]
        ]
        affirm: NotRequired[
            Optional["SetupIntent.CreatePaymentMethodDataAffirmParams"]
        ]
        afterpay_clearpay: NotRequired[
            Optional[
                "SetupIntent.CreatePaymentMethodDataAfterpayClearpayParams"
            ]
        ]
        alipay: NotRequired[
            Optional["SetupIntent.CreatePaymentMethodDataAlipayParams"]
        ]
        au_becs_debit: NotRequired[
            Optional["SetupIntent.CreatePaymentMethodDataAuBecsDebitParams"]
        ]
        bacs_debit: NotRequired[
            Optional["SetupIntent.CreatePaymentMethodDataBacsDebitParams"]
        ]
        bancontact: NotRequired[
            Optional["SetupIntent.CreatePaymentMethodDataBancontactParams"]
        ]
        billing_details: NotRequired[
            Optional["SetupIntent.CreatePaymentMethodDataBillingDetailsParams"]
        ]
        blik: NotRequired[
            Optional["SetupIntent.CreatePaymentMethodDataBlikParams"]
        ]
        boleto: NotRequired[
            Optional["SetupIntent.CreatePaymentMethodDataBoletoParams"]
        ]
        cashapp: NotRequired[
            Optional["SetupIntent.CreatePaymentMethodDataCashappParams"]
        ]
        customer_balance: NotRequired[
            Optional[
                "SetupIntent.CreatePaymentMethodDataCustomerBalanceParams"
            ]
        ]
        eps: NotRequired[
            Optional["SetupIntent.CreatePaymentMethodDataEpsParams"]
        ]
        fpx: NotRequired[
            Optional["SetupIntent.CreatePaymentMethodDataFpxParams"]
        ]
        giropay: NotRequired[
            Optional["SetupIntent.CreatePaymentMethodDataGiropayParams"]
        ]
        grabpay: NotRequired[
            Optional["SetupIntent.CreatePaymentMethodDataGrabpayParams"]
        ]
        ideal: NotRequired[
            Optional["SetupIntent.CreatePaymentMethodDataIdealParams"]
        ]
        interac_present: NotRequired[
            Optional["SetupIntent.CreatePaymentMethodDataInteracPresentParams"]
        ]
        klarna: NotRequired[
            Optional["SetupIntent.CreatePaymentMethodDataKlarnaParams"]
        ]
        konbini: NotRequired[
            Optional["SetupIntent.CreatePaymentMethodDataKonbiniParams"]
        ]
        link: NotRequired[
            Optional["SetupIntent.CreatePaymentMethodDataLinkParams"]
        ]
        metadata: NotRequired[Optional[Dict[str, str]]]
        oxxo: NotRequired[
            Optional["SetupIntent.CreatePaymentMethodDataOxxoParams"]
        ]
        p24: NotRequired[
            Optional["SetupIntent.CreatePaymentMethodDataP24Params"]
        ]
        paynow: NotRequired[
            Optional["SetupIntent.CreatePaymentMethodDataPaynowParams"]
        ]
        paypal: NotRequired[
            Optional["SetupIntent.CreatePaymentMethodDataPaypalParams"]
        ]
        pix: NotRequired[
            Optional["SetupIntent.CreatePaymentMethodDataPixParams"]
        ]
        promptpay: NotRequired[
            Optional["SetupIntent.CreatePaymentMethodDataPromptpayParams"]
        ]
        radar_options: NotRequired[
            Optional["SetupIntent.CreatePaymentMethodDataRadarOptionsParams"]
        ]
        sepa_debit: NotRequired[
            Optional["SetupIntent.CreatePaymentMethodDataSepaDebitParams"]
        ]
        sofort: NotRequired[
            Optional["SetupIntent.CreatePaymentMethodDataSofortParams"]
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
            Optional["SetupIntent.CreatePaymentMethodDataUsBankAccountParams"]
        ]
        wechat_pay: NotRequired[
            Optional["SetupIntent.CreatePaymentMethodDataWechatPayParams"]
        ]
        zip: NotRequired[
            Optional["SetupIntent.CreatePaymentMethodDataZipParams"]
        ]

    class CreatePaymentMethodDataZipParams(TypedDict):
        pass

    class CreatePaymentMethodDataWechatPayParams(TypedDict):
        pass

    class CreatePaymentMethodDataUsBankAccountParams(TypedDict):
        account_holder_type: NotRequired[
            Optional[Literal["company", "individual"]]
        ]
        account_number: NotRequired[Optional[str]]
        account_type: NotRequired[Optional[Literal["checking", "savings"]]]
        financial_connections_account: NotRequired[Optional[str]]
        routing_number: NotRequired[Optional[str]]

    class CreatePaymentMethodDataSofortParams(TypedDict):
        country: Literal["AT", "BE", "DE", "ES", "IT", "NL"]

    class CreatePaymentMethodDataSepaDebitParams(TypedDict):
        iban: str

    class CreatePaymentMethodDataRadarOptionsParams(TypedDict):
        session: NotRequired[Optional[str]]

    class CreatePaymentMethodDataPromptpayParams(TypedDict):
        pass

    class CreatePaymentMethodDataPixParams(TypedDict):
        pass

    class CreatePaymentMethodDataPaypalParams(TypedDict):
        pass

    class CreatePaymentMethodDataPaynowParams(TypedDict):
        pass

    class CreatePaymentMethodDataP24Params(TypedDict):
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

    class CreatePaymentMethodDataOxxoParams(TypedDict):
        pass

    class CreatePaymentMethodDataLinkParams(TypedDict):
        pass

    class CreatePaymentMethodDataKonbiniParams(TypedDict):
        pass

    class CreatePaymentMethodDataKlarnaParams(TypedDict):
        dob: NotRequired[
            Optional["SetupIntent.CreatePaymentMethodDataKlarnaDobParams"]
        ]

    class CreatePaymentMethodDataKlarnaDobParams(TypedDict):
        day: int
        month: int
        year: int

    class CreatePaymentMethodDataInteracPresentParams(TypedDict):
        pass

    class CreatePaymentMethodDataIdealParams(TypedDict):
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

    class CreatePaymentMethodDataGrabpayParams(TypedDict):
        pass

    class CreatePaymentMethodDataGiropayParams(TypedDict):
        pass

    class CreatePaymentMethodDataFpxParams(TypedDict):
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

    class CreatePaymentMethodDataEpsParams(TypedDict):
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

    class CreatePaymentMethodDataCustomerBalanceParams(TypedDict):
        pass

    class CreatePaymentMethodDataCashappParams(TypedDict):
        pass

    class CreatePaymentMethodDataBoletoParams(TypedDict):
        tax_id: str

    class CreatePaymentMethodDataBlikParams(TypedDict):
        pass

    class CreatePaymentMethodDataBillingDetailsParams(TypedDict):
        address: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "SetupIntent.CreatePaymentMethodDataBillingDetailsAddressParams",
                ]
            ]
        ]
        email: NotRequired[Optional[Union[Literal[""], str]]]
        name: NotRequired[Optional[Union[Literal[""], str]]]
        phone: NotRequired[Optional[Union[Literal[""], str]]]

    class CreatePaymentMethodDataBillingDetailsAddressParams(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class CreatePaymentMethodDataBancontactParams(TypedDict):
        pass

    class CreatePaymentMethodDataBacsDebitParams(TypedDict):
        account_number: NotRequired[Optional[str]]
        sort_code: NotRequired[Optional[str]]

    class CreatePaymentMethodDataAuBecsDebitParams(TypedDict):
        account_number: str
        bsb_number: str

    class CreatePaymentMethodDataAlipayParams(TypedDict):
        pass

    class CreatePaymentMethodDataAfterpayClearpayParams(TypedDict):
        pass

    class CreatePaymentMethodDataAffirmParams(TypedDict):
        pass

    class CreatePaymentMethodDataAcssDebitParams(TypedDict):
        account_number: str
        institution_number: str
        transit_number: str

    class CreateMandateDataParams(TypedDict):
        customer_acceptance: "SetupIntent.CreateMandateDataCustomerAcceptanceParams"

    class CreateMandateDataCustomerAcceptanceParams(TypedDict):
        accepted_at: NotRequired[Optional[int]]
        offline: NotRequired[
            Optional[
                "SetupIntent.CreateMandateDataCustomerAcceptanceOfflineParams"
            ]
        ]
        online: NotRequired[
            Optional[
                "SetupIntent.CreateMandateDataCustomerAcceptanceOnlineParams"
            ]
        ]
        type: Literal["offline", "online"]

    class CreateMandateDataCustomerAcceptanceOnlineParams(TypedDict):
        ip_address: str
        user_agent: str

    class CreateMandateDataCustomerAcceptanceOfflineParams(TypedDict):
        pass

    class CreateAutomaticPaymentMethodsParams(TypedDict):
        allow_redirects: NotRequired[Optional[Literal["always", "never"]]]
        enabled: bool

    class ListParams(RequestOptions):
        attach_to_self: NotRequired[Optional[bool]]
        created: NotRequired[
            Optional[Union["SetupIntent.ListCreatedParams", int]]
        ]
        customer: NotRequired[Optional[str]]
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        payment_method: NotRequired[Optional[str]]
        starting_after: NotRequired[Optional[str]]

    class ListCreatedParams(TypedDict):
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
            Optional["SetupIntent.ModifyPaymentMethodDataParams"]
        ]
        payment_method_options: NotRequired[
            Optional["SetupIntent.ModifyPaymentMethodOptionsParams"]
        ]
        payment_method_types: NotRequired[Optional[List[str]]]

    class ModifyPaymentMethodOptionsParams(TypedDict):
        acss_debit: NotRequired[
            Optional["SetupIntent.ModifyPaymentMethodOptionsAcssDebitParams"]
        ]
        card: NotRequired[
            Optional["SetupIntent.ModifyPaymentMethodOptionsCardParams"]
        ]
        link: NotRequired[
            Optional["SetupIntent.ModifyPaymentMethodOptionsLinkParams"]
        ]
        paypal: NotRequired[
            Optional["SetupIntent.ModifyPaymentMethodOptionsPaypalParams"]
        ]
        sepa_debit: NotRequired[
            Optional["SetupIntent.ModifyPaymentMethodOptionsSepaDebitParams"]
        ]
        us_bank_account: NotRequired[
            Optional[
                "SetupIntent.ModifyPaymentMethodOptionsUsBankAccountParams"
            ]
        ]

    class ModifyPaymentMethodOptionsUsBankAccountParams(TypedDict):
        financial_connections: NotRequired[
            Optional[
                "SetupIntent.ModifyPaymentMethodOptionsUsBankAccountFinancialConnectionsParams"
            ]
        ]
        networks: NotRequired[
            Optional[
                "SetupIntent.ModifyPaymentMethodOptionsUsBankAccountNetworksParams"
            ]
        ]
        verification_method: NotRequired[
            Optional[Literal["automatic", "instant", "microdeposits"]]
        ]

    class ModifyPaymentMethodOptionsUsBankAccountNetworksParams(TypedDict):
        requested: NotRequired[
            Optional[List[Literal["ach", "us_domestic_wire"]]]
        ]

    class ModifyPaymentMethodOptionsUsBankAccountFinancialConnectionsParams(
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

    class ModifyPaymentMethodOptionsSepaDebitParams(TypedDict):
        mandate_options: NotRequired[
            Optional[
                "SetupIntent.ModifyPaymentMethodOptionsSepaDebitMandateOptionsParams"
            ]
        ]

    class ModifyPaymentMethodOptionsSepaDebitMandateOptionsParams(TypedDict):
        pass

    class ModifyPaymentMethodOptionsPaypalParams(TypedDict):
        billing_agreement_id: NotRequired[Optional[str]]

    class ModifyPaymentMethodOptionsLinkParams(TypedDict):
        persistent_token: NotRequired[Optional[str]]

    class ModifyPaymentMethodOptionsCardParams(TypedDict):
        mandate_options: NotRequired[
            Optional[
                "SetupIntent.ModifyPaymentMethodOptionsCardMandateOptionsParams"
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

    class ModifyPaymentMethodOptionsCardMandateOptionsParams(TypedDict):
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

    class ModifyPaymentMethodOptionsAcssDebitParams(TypedDict):
        currency: NotRequired[Optional[Literal["cad", "usd"]]]
        mandate_options: NotRequired[
            Optional[
                "SetupIntent.ModifyPaymentMethodOptionsAcssDebitMandateOptionsParams"
            ]
        ]
        verification_method: NotRequired[
            Optional[Literal["automatic", "instant", "microdeposits"]]
        ]

    class ModifyPaymentMethodOptionsAcssDebitMandateOptionsParams(TypedDict):
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

    class ModifyPaymentMethodDataParams(TypedDict):
        acss_debit: NotRequired[
            Optional["SetupIntent.ModifyPaymentMethodDataAcssDebitParams"]
        ]
        affirm: NotRequired[
            Optional["SetupIntent.ModifyPaymentMethodDataAffirmParams"]
        ]
        afterpay_clearpay: NotRequired[
            Optional[
                "SetupIntent.ModifyPaymentMethodDataAfterpayClearpayParams"
            ]
        ]
        alipay: NotRequired[
            Optional["SetupIntent.ModifyPaymentMethodDataAlipayParams"]
        ]
        au_becs_debit: NotRequired[
            Optional["SetupIntent.ModifyPaymentMethodDataAuBecsDebitParams"]
        ]
        bacs_debit: NotRequired[
            Optional["SetupIntent.ModifyPaymentMethodDataBacsDebitParams"]
        ]
        bancontact: NotRequired[
            Optional["SetupIntent.ModifyPaymentMethodDataBancontactParams"]
        ]
        billing_details: NotRequired[
            Optional["SetupIntent.ModifyPaymentMethodDataBillingDetailsParams"]
        ]
        blik: NotRequired[
            Optional["SetupIntent.ModifyPaymentMethodDataBlikParams"]
        ]
        boleto: NotRequired[
            Optional["SetupIntent.ModifyPaymentMethodDataBoletoParams"]
        ]
        cashapp: NotRequired[
            Optional["SetupIntent.ModifyPaymentMethodDataCashappParams"]
        ]
        customer_balance: NotRequired[
            Optional[
                "SetupIntent.ModifyPaymentMethodDataCustomerBalanceParams"
            ]
        ]
        eps: NotRequired[
            Optional["SetupIntent.ModifyPaymentMethodDataEpsParams"]
        ]
        fpx: NotRequired[
            Optional["SetupIntent.ModifyPaymentMethodDataFpxParams"]
        ]
        giropay: NotRequired[
            Optional["SetupIntent.ModifyPaymentMethodDataGiropayParams"]
        ]
        grabpay: NotRequired[
            Optional["SetupIntent.ModifyPaymentMethodDataGrabpayParams"]
        ]
        ideal: NotRequired[
            Optional["SetupIntent.ModifyPaymentMethodDataIdealParams"]
        ]
        interac_present: NotRequired[
            Optional["SetupIntent.ModifyPaymentMethodDataInteracPresentParams"]
        ]
        klarna: NotRequired[
            Optional["SetupIntent.ModifyPaymentMethodDataKlarnaParams"]
        ]
        konbini: NotRequired[
            Optional["SetupIntent.ModifyPaymentMethodDataKonbiniParams"]
        ]
        link: NotRequired[
            Optional["SetupIntent.ModifyPaymentMethodDataLinkParams"]
        ]
        metadata: NotRequired[Optional[Dict[str, str]]]
        oxxo: NotRequired[
            Optional["SetupIntent.ModifyPaymentMethodDataOxxoParams"]
        ]
        p24: NotRequired[
            Optional["SetupIntent.ModifyPaymentMethodDataP24Params"]
        ]
        paynow: NotRequired[
            Optional["SetupIntent.ModifyPaymentMethodDataPaynowParams"]
        ]
        paypal: NotRequired[
            Optional["SetupIntent.ModifyPaymentMethodDataPaypalParams"]
        ]
        pix: NotRequired[
            Optional["SetupIntent.ModifyPaymentMethodDataPixParams"]
        ]
        promptpay: NotRequired[
            Optional["SetupIntent.ModifyPaymentMethodDataPromptpayParams"]
        ]
        radar_options: NotRequired[
            Optional["SetupIntent.ModifyPaymentMethodDataRadarOptionsParams"]
        ]
        sepa_debit: NotRequired[
            Optional["SetupIntent.ModifyPaymentMethodDataSepaDebitParams"]
        ]
        sofort: NotRequired[
            Optional["SetupIntent.ModifyPaymentMethodDataSofortParams"]
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
            Optional["SetupIntent.ModifyPaymentMethodDataUsBankAccountParams"]
        ]
        wechat_pay: NotRequired[
            Optional["SetupIntent.ModifyPaymentMethodDataWechatPayParams"]
        ]
        zip: NotRequired[
            Optional["SetupIntent.ModifyPaymentMethodDataZipParams"]
        ]

    class ModifyPaymentMethodDataZipParams(TypedDict):
        pass

    class ModifyPaymentMethodDataWechatPayParams(TypedDict):
        pass

    class ModifyPaymentMethodDataUsBankAccountParams(TypedDict):
        account_holder_type: NotRequired[
            Optional[Literal["company", "individual"]]
        ]
        account_number: NotRequired[Optional[str]]
        account_type: NotRequired[Optional[Literal["checking", "savings"]]]
        financial_connections_account: NotRequired[Optional[str]]
        routing_number: NotRequired[Optional[str]]

    class ModifyPaymentMethodDataSofortParams(TypedDict):
        country: Literal["AT", "BE", "DE", "ES", "IT", "NL"]

    class ModifyPaymentMethodDataSepaDebitParams(TypedDict):
        iban: str

    class ModifyPaymentMethodDataRadarOptionsParams(TypedDict):
        session: NotRequired[Optional[str]]

    class ModifyPaymentMethodDataPromptpayParams(TypedDict):
        pass

    class ModifyPaymentMethodDataPixParams(TypedDict):
        pass

    class ModifyPaymentMethodDataPaypalParams(TypedDict):
        pass

    class ModifyPaymentMethodDataPaynowParams(TypedDict):
        pass

    class ModifyPaymentMethodDataP24Params(TypedDict):
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

    class ModifyPaymentMethodDataOxxoParams(TypedDict):
        pass

    class ModifyPaymentMethodDataLinkParams(TypedDict):
        pass

    class ModifyPaymentMethodDataKonbiniParams(TypedDict):
        pass

    class ModifyPaymentMethodDataKlarnaParams(TypedDict):
        dob: NotRequired[
            Optional["SetupIntent.ModifyPaymentMethodDataKlarnaDobParams"]
        ]

    class ModifyPaymentMethodDataKlarnaDobParams(TypedDict):
        day: int
        month: int
        year: int

    class ModifyPaymentMethodDataInteracPresentParams(TypedDict):
        pass

    class ModifyPaymentMethodDataIdealParams(TypedDict):
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

    class ModifyPaymentMethodDataGrabpayParams(TypedDict):
        pass

    class ModifyPaymentMethodDataGiropayParams(TypedDict):
        pass

    class ModifyPaymentMethodDataFpxParams(TypedDict):
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

    class ModifyPaymentMethodDataEpsParams(TypedDict):
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

    class ModifyPaymentMethodDataCustomerBalanceParams(TypedDict):
        pass

    class ModifyPaymentMethodDataCashappParams(TypedDict):
        pass

    class ModifyPaymentMethodDataBoletoParams(TypedDict):
        tax_id: str

    class ModifyPaymentMethodDataBlikParams(TypedDict):
        pass

    class ModifyPaymentMethodDataBillingDetailsParams(TypedDict):
        address: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "SetupIntent.ModifyPaymentMethodDataBillingDetailsAddressParams",
                ]
            ]
        ]
        email: NotRequired[Optional[Union[Literal[""], str]]]
        name: NotRequired[Optional[Union[Literal[""], str]]]
        phone: NotRequired[Optional[Union[Literal[""], str]]]

    class ModifyPaymentMethodDataBillingDetailsAddressParams(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class ModifyPaymentMethodDataBancontactParams(TypedDict):
        pass

    class ModifyPaymentMethodDataBacsDebitParams(TypedDict):
        account_number: NotRequired[Optional[str]]
        sort_code: NotRequired[Optional[str]]

    class ModifyPaymentMethodDataAuBecsDebitParams(TypedDict):
        account_number: str
        bsb_number: str

    class ModifyPaymentMethodDataAlipayParams(TypedDict):
        pass

    class ModifyPaymentMethodDataAfterpayClearpayParams(TypedDict):
        pass

    class ModifyPaymentMethodDataAffirmParams(TypedDict):
        pass

    class ModifyPaymentMethodDataAcssDebitParams(TypedDict):
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
