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
from stripe.stripe_object import StripeObject
from typing import Any, Dict, List, Optional, cast
from typing_extensions import Literal
from urllib.parse import quote_plus

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.account import Account
    from stripe.api_resources.application import Application
    from stripe.api_resources.line_item import LineItem
    from stripe.api_resources.shipping_rate import ShippingRate
    from stripe.api_resources.tax_id import TaxId


class PaymentLink(
    CreateableAPIResource["PaymentLink"],
    ListableAPIResource["PaymentLink"],
    UpdateableAPIResource["PaymentLink"],
):
    """
    A payment link is a shareable URL that will take your customers to a hosted payment page. A payment link can be shared and used multiple times.

    When a customer opens a payment link it will open a new [checkout session](https://stripe.com/docs/api/checkout/sessions) to render the payment page. You can use [checkout session events](https://stripe.com/docs/api/events/types#event_types-checkout.session.completed) to track payments through payment links.

    Related guide: [Payment Links API](https://stripe.com/docs/payment-links)
    """

    OBJECT_NAME = "payment_link"

    class AfterCompletion(StripeObject):
        class HostedConfirmation(StripeObject):
            custom_message: Optional[str]

        class Redirect(StripeObject):
            url: str

        hosted_confirmation: Optional[HostedConfirmation]
        redirect: Optional[Redirect]
        type: Literal["hosted_confirmation", "redirect"]
        _inner_class_types = {
            "hosted_confirmation": HostedConfirmation,
            "redirect": Redirect,
        }

    class AutomaticTax(StripeObject):
        enabled: bool

    class ConsentCollection(StripeObject):
        promotions: Optional[Literal["auto", "none"]]
        terms_of_service: Optional[Literal["none", "required"]]

    class CustomField(StripeObject):
        class Dropdown(StripeObject):
            class Option(StripeObject):
                label: str
                value: str

            options: List[Option]
            _inner_class_types = {"options": Option}

        class Label(StripeObject):
            custom: Optional[str]
            type: Literal["custom"]

        class Numeric(StripeObject):
            maximum_length: Optional[int]
            minimum_length: Optional[int]

        class Text(StripeObject):
            maximum_length: Optional[int]
            minimum_length: Optional[int]

        dropdown: Optional[Dropdown]
        key: str
        label: Label
        numeric: Optional[Numeric]
        optional: bool
        text: Optional[Text]
        type: Literal["dropdown", "numeric", "text"]
        _inner_class_types = {
            "dropdown": Dropdown,
            "label": Label,
            "numeric": Numeric,
            "text": Text,
        }

    class CustomText(StripeObject):
        class ShippingAddress(StripeObject):
            message: str

        class Submit(StripeObject):
            message: str

        class TermsOfServiceAcceptance(StripeObject):
            message: str

        shipping_address: Optional[ShippingAddress]
        submit: Optional[Submit]
        terms_of_service_acceptance: Optional[TermsOfServiceAcceptance]
        _inner_class_types = {
            "shipping_address": ShippingAddress,
            "submit": Submit,
            "terms_of_service_acceptance": TermsOfServiceAcceptance,
        }

    class InvoiceCreation(StripeObject):
        class InvoiceData(StripeObject):
            class CustomField(StripeObject):
                name: str
                value: str

            class RenderingOptions(StripeObject):
                amount_tax_display: Optional[str]

            account_tax_ids: Optional[List[ExpandableField["TaxId"]]]
            custom_fields: Optional[List[CustomField]]
            description: Optional[str]
            footer: Optional[str]
            metadata: Optional[Dict[str, str]]
            rendering_options: Optional[RenderingOptions]
            _inner_class_types = {
                "custom_fields": CustomField,
                "rendering_options": RenderingOptions,
            }

        enabled: bool
        invoice_data: Optional[InvoiceData]
        _inner_class_types = {"invoice_data": InvoiceData}

    class PaymentIntentData(StripeObject):
        capture_method: Optional[
            Literal["automatic", "automatic_async", "manual"]
        ]
        metadata: Dict[str, str]
        setup_future_usage: Optional[Literal["off_session", "on_session"]]
        statement_descriptor: Optional[str]
        statement_descriptor_suffix: Optional[str]

    class PhoneNumberCollection(StripeObject):
        enabled: bool

    class ShippingAddressCollection(StripeObject):
        allowed_countries: List[
            Literal[
                "AC",
                "AD",
                "AE",
                "AF",
                "AG",
                "AI",
                "AL",
                "AM",
                "AO",
                "AQ",
                "AR",
                "AT",
                "AU",
                "AW",
                "AX",
                "AZ",
                "BA",
                "BB",
                "BD",
                "BE",
                "BF",
                "BG",
                "BH",
                "BI",
                "BJ",
                "BL",
                "BM",
                "BN",
                "BO",
                "BQ",
                "BR",
                "BS",
                "BT",
                "BV",
                "BW",
                "BY",
                "BZ",
                "CA",
                "CD",
                "CF",
                "CG",
                "CH",
                "CI",
                "CK",
                "CL",
                "CM",
                "CN",
                "CO",
                "CR",
                "CV",
                "CW",
                "CY",
                "CZ",
                "DE",
                "DJ",
                "DK",
                "DM",
                "DO",
                "DZ",
                "EC",
                "EE",
                "EG",
                "EH",
                "ER",
                "ES",
                "ET",
                "FI",
                "FJ",
                "FK",
                "FO",
                "FR",
                "GA",
                "GB",
                "GD",
                "GE",
                "GF",
                "GG",
                "GH",
                "GI",
                "GL",
                "GM",
                "GN",
                "GP",
                "GQ",
                "GR",
                "GS",
                "GT",
                "GU",
                "GW",
                "GY",
                "HK",
                "HN",
                "HR",
                "HT",
                "HU",
                "ID",
                "IE",
                "IL",
                "IM",
                "IN",
                "IO",
                "IQ",
                "IS",
                "IT",
                "JE",
                "JM",
                "JO",
                "JP",
                "KE",
                "KG",
                "KH",
                "KI",
                "KM",
                "KN",
                "KR",
                "KW",
                "KY",
                "KZ",
                "LA",
                "LB",
                "LC",
                "LI",
                "LK",
                "LR",
                "LS",
                "LT",
                "LU",
                "LV",
                "LY",
                "MA",
                "MC",
                "MD",
                "ME",
                "MF",
                "MG",
                "MK",
                "ML",
                "MM",
                "MN",
                "MO",
                "MQ",
                "MR",
                "MS",
                "MT",
                "MU",
                "MV",
                "MW",
                "MX",
                "MY",
                "MZ",
                "NA",
                "NC",
                "NE",
                "NG",
                "NI",
                "NL",
                "NO",
                "NP",
                "NR",
                "NU",
                "NZ",
                "OM",
                "PA",
                "PE",
                "PF",
                "PG",
                "PH",
                "PK",
                "PL",
                "PM",
                "PN",
                "PR",
                "PS",
                "PT",
                "PY",
                "QA",
                "RE",
                "RO",
                "RS",
                "RU",
                "RW",
                "SA",
                "SB",
                "SC",
                "SE",
                "SG",
                "SH",
                "SI",
                "SJ",
                "SK",
                "SL",
                "SM",
                "SN",
                "SO",
                "SR",
                "SS",
                "ST",
                "SV",
                "SX",
                "SZ",
                "TA",
                "TC",
                "TD",
                "TF",
                "TG",
                "TH",
                "TJ",
                "TK",
                "TL",
                "TM",
                "TN",
                "TO",
                "TR",
                "TT",
                "TV",
                "TW",
                "TZ",
                "UA",
                "UG",
                "US",
                "UY",
                "UZ",
                "VA",
                "VC",
                "VE",
                "VG",
                "VN",
                "VU",
                "WF",
                "WS",
                "XK",
                "YE",
                "YT",
                "ZA",
                "ZM",
                "ZW",
                "ZZ",
            ]
        ]

    class ShippingOption(StripeObject):
        shipping_amount: int
        shipping_rate: ExpandableField["ShippingRate"]

    class SubscriptionData(StripeObject):
        description: Optional[str]
        metadata: Dict[str, str]
        trial_period_days: Optional[int]

    class TaxIdCollection(StripeObject):
        enabled: bool

    class TransferData(StripeObject):
        amount: Optional[int]
        destination: ExpandableField["Account"]

    active: bool
    after_completion: AfterCompletion
    allow_promotion_codes: bool
    application: Optional[ExpandableField["Application"]]
    application_fee_amount: Optional[int]
    application_fee_percent: Optional[float]
    automatic_tax: AutomaticTax
    billing_address_collection: Literal["auto", "required"]
    consent_collection: Optional[ConsentCollection]
    currency: str
    custom_fields: List[CustomField]
    custom_text: CustomText
    customer_creation: Literal["always", "if_required"]
    id: str
    invoice_creation: Optional[InvoiceCreation]
    line_items: Optional[ListObject["LineItem"]]
    livemode: bool
    metadata: Dict[str, str]
    object: Literal["payment_link"]
    on_behalf_of: Optional[ExpandableField["Account"]]
    payment_intent_data: Optional[PaymentIntentData]
    payment_method_collection: Literal["always", "if_required"]
    payment_method_types: Optional[
        List[
            Literal[
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
            ]
        ]
    ]
    phone_number_collection: PhoneNumberCollection
    shipping_address_collection: Optional[ShippingAddressCollection]
    shipping_options: List[ShippingOption]
    submit_type: Literal["auto", "book", "donate", "pay"]
    subscription_data: Optional[SubscriptionData]
    tax_id_collection: TaxIdCollection
    transfer_data: Optional[TransferData]
    url: str

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> "PaymentLink":
        return cast(
            "PaymentLink",
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
    ) -> ListObject["PaymentLink"]:
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
    def _cls_list_line_items(
        cls,
        payment_link: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "get",
            "/v1/payment_links/{payment_link}/line_items".format(
                payment_link=util.sanitize_id(payment_link)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_list_line_items")
    def list_line_items(
        self, idempotency_key: Optional[str] = None, **params: Any
    ):
        return self._request(
            "get",
            "/v1/payment_links/{payment_link}/line_items".format(
                payment_link=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def modify(cls, id, **params: Any) -> "PaymentLink":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "PaymentLink",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "PaymentLink":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance

    _inner_class_types = {
        "after_completion": AfterCompletion,
        "automatic_tax": AutomaticTax,
        "consent_collection": ConsentCollection,
        "custom_fields": CustomField,
        "custom_text": CustomText,
        "invoice_creation": InvoiceCreation,
        "payment_intent_data": PaymentIntentData,
        "phone_number_collection": PhoneNumberCollection,
        "shipping_address_collection": ShippingAddressCollection,
        "shipping_options": ShippingOption,
        "subscription_data": SubscriptionData,
        "tax_id_collection": TaxIdCollection,
        "transfer_data": TransferData,
    }
