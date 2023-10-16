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
from typing import Dict, List, Optional, cast
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

    OBJECT_NAME = "payment_method"
    if TYPE_CHECKING:

        class AttachParams(RequestOptions):
            customer: str
            expand: NotRequired["List[str]|None"]

        class CreateParams(RequestOptions):
            acss_debit: NotRequired["PaymentMethod.CreateParamsAcssDebit|None"]
            affirm: NotRequired["PaymentMethod.CreateParamsAffirm|None"]
            afterpay_clearpay: NotRequired[
                "PaymentMethod.CreateParamsAfterpayClearpay|None"
            ]
            alipay: NotRequired["PaymentMethod.CreateParamsAlipay|None"]
            au_becs_debit: NotRequired[
                "PaymentMethod.CreateParamsAuBecsDebit|None"
            ]
            bacs_debit: NotRequired["PaymentMethod.CreateParamsBacsDebit|None"]
            bancontact: NotRequired[
                "PaymentMethod.CreateParamsBancontact|None"
            ]
            billing_details: NotRequired[
                "PaymentMethod.CreateParamsBillingDetails|None"
            ]
            blik: NotRequired["PaymentMethod.CreateParamsBlik|None"]
            boleto: NotRequired["PaymentMethod.CreateParamsBoleto|None"]
            card: NotRequired[
                "PaymentMethod.CreateParamsCard|PaymentMethod.CreateParamsCard2|None"
            ]
            cashapp: NotRequired["PaymentMethod.CreateParamsCashapp|None"]
            customer: NotRequired["str|None"]
            customer_balance: NotRequired[
                "PaymentMethod.CreateParamsCustomerBalance|None"
            ]
            eps: NotRequired["PaymentMethod.CreateParamsEps|None"]
            expand: NotRequired["List[str]|None"]
            fpx: NotRequired["PaymentMethod.CreateParamsFpx|None"]
            giropay: NotRequired["PaymentMethod.CreateParamsGiropay|None"]
            grabpay: NotRequired["PaymentMethod.CreateParamsGrabpay|None"]
            ideal: NotRequired["PaymentMethod.CreateParamsIdeal|None"]
            interac_present: NotRequired[
                "PaymentMethod.CreateParamsInteracPresent|None"
            ]
            klarna: NotRequired["PaymentMethod.CreateParamsKlarna|None"]
            konbini: NotRequired["PaymentMethod.CreateParamsKonbini|None"]
            link: NotRequired["PaymentMethod.CreateParamsLink|None"]
            metadata: NotRequired["Dict[str, str]|None"]
            oxxo: NotRequired["PaymentMethod.CreateParamsOxxo|None"]
            p24: NotRequired["PaymentMethod.CreateParamsP24|None"]
            payment_method: NotRequired["str|None"]
            paynow: NotRequired["PaymentMethod.CreateParamsPaynow|None"]
            paypal: NotRequired["PaymentMethod.CreateParamsPaypal|None"]
            pix: NotRequired["PaymentMethod.CreateParamsPix|None"]
            promptpay: NotRequired["PaymentMethod.CreateParamsPromptpay|None"]
            radar_options: NotRequired[
                "PaymentMethod.CreateParamsRadarOptions|None"
            ]
            sepa_debit: NotRequired["PaymentMethod.CreateParamsSepaDebit|None"]
            sofort: NotRequired["PaymentMethod.CreateParamsSofort|None"]
            type: NotRequired[
                "Literal['acss_debit', 'affirm', 'afterpay_clearpay', 'alipay', 'au_becs_debit', 'bacs_debit', 'bancontact', 'blik', 'boleto', 'card', 'cashapp', 'customer_balance', 'eps', 'fpx', 'giropay', 'grabpay', 'ideal', 'klarna', 'konbini', 'link', 'oxxo', 'p24', 'paynow', 'paypal', 'pix', 'promptpay', 'sepa_debit', 'sofort', 'us_bank_account', 'wechat_pay', 'zip']|None"
            ]
            us_bank_account: NotRequired[
                "PaymentMethod.CreateParamsUsBankAccount|None"
            ]
            wechat_pay: NotRequired["PaymentMethod.CreateParamsWechatPay|None"]
            zip: NotRequired["PaymentMethod.CreateParamsZip|None"]

        class CreateParamsZip(TypedDict):
            pass

        class CreateParamsWechatPay(TypedDict):
            pass

        class CreateParamsUsBankAccount(TypedDict):
            account_holder_type: NotRequired[
                "Literal['company', 'individual']|None"
            ]
            account_number: NotRequired["str|None"]
            account_type: NotRequired["Literal['checking', 'savings']|None"]
            financial_connections_account: NotRequired["str|None"]
            routing_number: NotRequired["str|None"]

        class CreateParamsSofort(TypedDict):
            country: Literal["AT", "BE", "DE", "ES", "IT", "NL"]

        class CreateParamsSepaDebit(TypedDict):
            iban: str

        class CreateParamsRadarOptions(TypedDict):
            session: NotRequired["str|None"]

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

        class CreateParamsOxxo(TypedDict):
            pass

        class CreateParamsLink(TypedDict):
            pass

        class CreateParamsKonbini(TypedDict):
            pass

        class CreateParamsKlarna(TypedDict):
            dob: NotRequired["PaymentMethod.CreateParamsKlarnaDob|None"]

        class CreateParamsKlarnaDob(TypedDict):
            day: int
            month: int
            year: int

        class CreateParamsInteracPresent(TypedDict):
            pass

        class CreateParamsIdeal(TypedDict):
            bank: NotRequired[
                "Literal['abn_amro', 'asn_bank', 'bunq', 'handelsbanken', 'ing', 'knab', 'moneyou', 'n26', 'rabobank', 'regiobank', 'revolut', 'sns_bank', 'triodos_bank', 'van_lanschot', 'yoursafe']|None"
            ]

        class CreateParamsGrabpay(TypedDict):
            pass

        class CreateParamsGiropay(TypedDict):
            pass

        class CreateParamsFpx(TypedDict):
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

        class CreateParamsEps(TypedDict):
            bank: NotRequired[
                "Literal['arzte_und_apotheker_bank', 'austrian_anadi_bank_ag', 'bank_austria', 'bankhaus_carl_spangler', 'bankhaus_schelhammer_und_schattera_ag', 'bawag_psk_ag', 'bks_bank_ag', 'brull_kallmus_bank_ag', 'btv_vier_lander_bank', 'capital_bank_grawe_gruppe_ag', 'deutsche_bank_ag', 'dolomitenbank', 'easybank_ag', 'erste_bank_und_sparkassen', 'hypo_alpeadriabank_international_ag', 'hypo_bank_burgenland_aktiengesellschaft', 'hypo_noe_lb_fur_niederosterreich_u_wien', 'hypo_oberosterreich_salzburg_steiermark', 'hypo_tirol_bank_ag', 'hypo_vorarlberg_bank_ag', 'marchfelder_bank', 'oberbank_ag', 'raiffeisen_bankengruppe_osterreich', 'schoellerbank_ag', 'sparda_bank_wien', 'volksbank_gruppe', 'volkskreditbank_ag', 'vr_bank_braunau']|None"
            ]

        class CreateParamsCustomerBalance(TypedDict):
            pass

        class CreateParamsCashapp(TypedDict):
            pass

        class CreateParamsCard2(TypedDict):
            token: str

        class CreateParamsCard(TypedDict):
            cvc: NotRequired["str|None"]
            exp_month: int
            exp_year: int
            number: str

        class CreateParamsBoleto(TypedDict):
            tax_id: str

        class CreateParamsBlik(TypedDict):
            pass

        class CreateParamsBillingDetails(TypedDict):
            address: NotRequired[
                "Literal['']|PaymentMethod.CreateParamsBillingDetailsAddress|None"
            ]
            email: NotRequired["Literal['']|str|None"]
            name: NotRequired["Literal['']|str|None"]
            phone: NotRequired["Literal['']|str|None"]

        class CreateParamsBillingDetailsAddress(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]

        class CreateParamsBancontact(TypedDict):
            pass

        class CreateParamsBacsDebit(TypedDict):
            account_number: NotRequired["str|None"]
            sort_code: NotRequired["str|None"]

        class CreateParamsAuBecsDebit(TypedDict):
            account_number: str
            bsb_number: str

        class CreateParamsAlipay(TypedDict):
            pass

        class CreateParamsAfterpayClearpay(TypedDict):
            pass

        class CreateParamsAffirm(TypedDict):
            pass

        class CreateParamsAcssDebit(TypedDict):
            account_number: str
            institution_number: str
            transit_number: str

        class DetachParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class ListParams(RequestOptions):
            customer: NotRequired["str|None"]
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]
            type: NotRequired[
                "Literal['acss_debit', 'affirm', 'afterpay_clearpay', 'alipay', 'au_becs_debit', 'bacs_debit', 'bancontact', 'blik', 'boleto', 'card', 'cashapp', 'customer_balance', 'eps', 'fpx', 'giropay', 'grabpay', 'ideal', 'klarna', 'konbini', 'link', 'oxxo', 'p24', 'paynow', 'paypal', 'pix', 'promptpay', 'sepa_debit', 'sofort', 'us_bank_account', 'wechat_pay', 'zip']|None"
            ]

        class ModifyParams(RequestOptions):
            billing_details: NotRequired[
                "PaymentMethod.ModifyParamsBillingDetails|None"
            ]
            card: NotRequired["PaymentMethod.ModifyParamsCard|None"]
            expand: NotRequired["List[str]|None"]
            link: NotRequired["PaymentMethod.ModifyParamsLink|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            us_bank_account: NotRequired[
                "PaymentMethod.ModifyParamsUsBankAccount|None"
            ]

        class ModifyParamsUsBankAccount(TypedDict):
            account_holder_type: NotRequired[
                "Literal['company', 'individual']|None"
            ]

        class ModifyParamsLink(TypedDict):
            pass

        class ModifyParamsCard(TypedDict):
            exp_month: NotRequired["int|None"]
            exp_year: NotRequired["int|None"]

        class ModifyParamsBillingDetails(TypedDict):
            address: NotRequired[
                "Literal['']|PaymentMethod.ModifyParamsBillingDetailsAddress|None"
            ]
            email: NotRequired["Literal['']|str|None"]
            name: NotRequired["Literal['']|str|None"]
            phone: NotRequired["Literal['']|str|None"]

        class ModifyParamsBillingDetailsAddress(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

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
