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

    OBJECT_NAME = "payment_method"

    class AttachParams(RequestOptions):
        customer: str
        expand: NotRequired[Optional[List[str]]]

    class CreateParams(RequestOptions):
        acss_debit: NotRequired[
            Optional["PaymentMethod.CreateAcssDebitParams"]
        ]
        affirm: NotRequired[Optional["PaymentMethod.CreateAffirmParams"]]
        afterpay_clearpay: NotRequired[
            Optional["PaymentMethod.CreateAfterpayClearpayParams"]
        ]
        alipay: NotRequired[Optional["PaymentMethod.CreateAlipayParams"]]
        au_becs_debit: NotRequired[
            Optional["PaymentMethod.CreateAuBecsDebitParams"]
        ]
        bacs_debit: NotRequired[
            Optional["PaymentMethod.CreateBacsDebitParams"]
        ]
        bancontact: NotRequired[
            Optional["PaymentMethod.CreateBancontactParams"]
        ]
        billing_details: NotRequired[
            Optional["PaymentMethod.CreateBillingDetailsParams"]
        ]
        blik: NotRequired[Optional["PaymentMethod.CreateBlikParams"]]
        boleto: NotRequired[Optional["PaymentMethod.CreateBoletoParams"]]
        card: NotRequired[
            Optional[
                Union[
                    "PaymentMethod.CreateCardParams",
                    "PaymentMethod.CreateCardParams",
                ]
            ]
        ]
        cashapp: NotRequired[Optional["PaymentMethod.CreateCashappParams"]]
        customer: NotRequired[Optional[str]]
        customer_balance: NotRequired[
            Optional["PaymentMethod.CreateCustomerBalanceParams"]
        ]
        eps: NotRequired[Optional["PaymentMethod.CreateEpsParams"]]
        expand: NotRequired[Optional[List[str]]]
        fpx: NotRequired[Optional["PaymentMethod.CreateFpxParams"]]
        giropay: NotRequired[Optional["PaymentMethod.CreateGiropayParams"]]
        grabpay: NotRequired[Optional["PaymentMethod.CreateGrabpayParams"]]
        ideal: NotRequired[Optional["PaymentMethod.CreateIdealParams"]]
        interac_present: NotRequired[
            Optional["PaymentMethod.CreateInteracPresentParams"]
        ]
        klarna: NotRequired[Optional["PaymentMethod.CreateKlarnaParams"]]
        konbini: NotRequired[Optional["PaymentMethod.CreateKonbiniParams"]]
        link: NotRequired[Optional["PaymentMethod.CreateLinkParams"]]
        metadata: NotRequired[Optional[Dict[str, str]]]
        oxxo: NotRequired[Optional["PaymentMethod.CreateOxxoParams"]]
        p24: NotRequired[Optional["PaymentMethod.CreateP24Params"]]
        payment_method: NotRequired[Optional[str]]
        paynow: NotRequired[Optional["PaymentMethod.CreatePaynowParams"]]
        paypal: NotRequired[Optional["PaymentMethod.CreatePaypalParams"]]
        pix: NotRequired[Optional["PaymentMethod.CreatePixParams"]]
        promptpay: NotRequired[Optional["PaymentMethod.CreatePromptpayParams"]]
        radar_options: NotRequired[
            Optional["PaymentMethod.CreateRadarOptionsParams"]
        ]
        sepa_debit: NotRequired[
            Optional["PaymentMethod.CreateSepaDebitParams"]
        ]
        sofort: NotRequired[Optional["PaymentMethod.CreateSofortParams"]]
        type: NotRequired[
            Optional[
                Literal[
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
            ]
        ]
        us_bank_account: NotRequired[
            Optional["PaymentMethod.CreateUsBankAccountParams"]
        ]
        wechat_pay: NotRequired[
            Optional["PaymentMethod.CreateWechatPayParams"]
        ]
        zip: NotRequired[Optional["PaymentMethod.CreateZipParams"]]

    class CreateZipParams(TypedDict):
        pass

    class CreateWechatPayParams(TypedDict):
        pass

    class CreateUsBankAccountParams(TypedDict):
        account_holder_type: NotRequired[
            Optional[Literal["company", "individual"]]
        ]
        account_number: NotRequired[Optional[str]]
        account_type: NotRequired[Optional[Literal["checking", "savings"]]]
        financial_connections_account: NotRequired[Optional[str]]
        routing_number: NotRequired[Optional[str]]

    class CreateSofortParams(TypedDict):
        country: Literal["AT", "BE", "DE", "ES", "IT", "NL"]

    class CreateSepaDebitParams(TypedDict):
        iban: str

    class CreateRadarOptionsParams(TypedDict):
        session: NotRequired[Optional[str]]

    class CreatePromptpayParams(TypedDict):
        pass

    class CreatePixParams(TypedDict):
        pass

    class CreatePaypalParams(TypedDict):
        pass

    class CreatePaynowParams(TypedDict):
        pass

    class CreateP24Params(TypedDict):
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

    class CreateOxxoParams(TypedDict):
        pass

    class CreateLinkParams(TypedDict):
        pass

    class CreateKonbiniParams(TypedDict):
        pass

    class CreateKlarnaParams(TypedDict):
        dob: NotRequired[Optional["PaymentMethod.CreateKlarnaDobParams"]]

    class CreateKlarnaDobParams(TypedDict):
        day: int
        month: int
        year: int

    class CreateInteracPresentParams(TypedDict):
        pass

    class CreateIdealParams(TypedDict):
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

    class CreateGrabpayParams(TypedDict):
        pass

    class CreateGiropayParams(TypedDict):
        pass

    class CreateFpxParams(TypedDict):
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

    class CreateEpsParams(TypedDict):
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

    class CreateCustomerBalanceParams(TypedDict):
        pass

    class CreateCashappParams(TypedDict):
        pass

    class CreateCardParams(TypedDict):
        token: str

    class CreateBoletoParams(TypedDict):
        tax_id: str

    class CreateBlikParams(TypedDict):
        pass

    class CreateBillingDetailsParams(TypedDict):
        address: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentMethod.CreateBillingDetailsAddressParams",
                ]
            ]
        ]
        email: NotRequired[Optional[Union[Literal[""], str]]]
        name: NotRequired[Optional[Union[Literal[""], str]]]
        phone: NotRequired[Optional[Union[Literal[""], str]]]

    class CreateBillingDetailsAddressParams(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class CreateBancontactParams(TypedDict):
        pass

    class CreateBacsDebitParams(TypedDict):
        account_number: NotRequired[Optional[str]]
        sort_code: NotRequired[Optional[str]]

    class CreateAuBecsDebitParams(TypedDict):
        account_number: str
        bsb_number: str

    class CreateAlipayParams(TypedDict):
        pass

    class CreateAfterpayClearpayParams(TypedDict):
        pass

    class CreateAffirmParams(TypedDict):
        pass

    class CreateAcssDebitParams(TypedDict):
        account_number: str
        institution_number: str
        transit_number: str

    class DetachParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    class ListParams(RequestOptions):
        customer: NotRequired[Optional[str]]
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        starting_after: NotRequired[Optional[str]]
        type: NotRequired[
            Optional[
                Literal[
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
            ]
        ]

    class ModifyParams(RequestOptions):
        billing_details: NotRequired[
            Optional["PaymentMethod.ModifyBillingDetailsParams"]
        ]
        card: NotRequired[Optional["PaymentMethod.ModifyCardParams"]]
        expand: NotRequired[Optional[List[str]]]
        link: NotRequired[Optional["PaymentMethod.ModifyLinkParams"]]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]
        us_bank_account: NotRequired[
            Optional["PaymentMethod.ModifyUsBankAccountParams"]
        ]

    class ModifyUsBankAccountParams(TypedDict):
        account_holder_type: NotRequired[
            Optional[Literal["company", "individual"]]
        ]

    class ModifyLinkParams(TypedDict):
        pass

    class ModifyCardParams(TypedDict):
        exp_month: NotRequired[Optional[int]]
        exp_year: NotRequired[Optional[int]]

    class ModifyBillingDetailsParams(TypedDict):
        address: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentMethod.ModifyBillingDetailsAddressParams",
                ]
            ]
        ]
        email: NotRequired[Optional[Union[Literal[""], str]]]
        name: NotRequired[Optional[Union[Literal[""], str]]]
        phone: NotRequired[Optional[Union[Literal[""], str]]]

    class ModifyBillingDetailsAddressParams(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class RetrieveParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

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
    customer: Optional[ExpandableField["Customer"]]
    customer_balance: Optional[StripeObject]
    eps: Optional[StripeObject]
    fpx: Optional[StripeObject]
    giropay: Optional[StripeObject]
    grabpay: Optional[StripeObject]
    id: str
    ideal: Optional[StripeObject]
    interac_present: Optional[StripeObject]
    klarna: Optional[StripeObject]
    konbini: Optional[StripeObject]
    link: Optional[StripeObject]
    livemode: bool
    metadata: Optional[Dict[str, str]]
    object: Literal["payment_method"]
    oxxo: Optional[StripeObject]
    p24: Optional[StripeObject]
    paynow: Optional[StripeObject]
    paypal: Optional[StripeObject]
    pix: Optional[StripeObject]
    promptpay: Optional[StripeObject]
    radar_options: Optional[StripeObject]
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
    ):
        return cls._static_request(
            "post",
            "/v1/payment_methods/{payment_method}/attach".format(
                payment_method=util.sanitize_id(payment_method)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_attach")
    def attach(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["PaymentMethod.AttachParams"]
    ):
        return self._request(
            "post",
            "/v1/payment_methods/{payment_method}/attach".format(
                payment_method=util.sanitize_id(self.get("id"))
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
    ):
        return cls._static_request(
            "post",
            "/v1/payment_methods/{payment_method}/detach".format(
                payment_method=util.sanitize_id(payment_method)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_detach")
    def detach(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["PaymentMethod.DetachParams"]
    ):
        return self._request(
            "post",
            "/v1/payment_methods/{payment_method}/detach".format(
                payment_method=util.sanitize_id(self.get("id"))
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
        cls, id, **params: Unpack["PaymentMethod.ModifyParams"]
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
