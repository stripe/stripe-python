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
    from stripe.api_resources.line_item import LineItem


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

    class CreateParams(RequestOptions):
        after_completion: NotRequired[
            Optional["PaymentLink.CreateParamsAfterCompletion"]
        ]
        allow_promotion_codes: NotRequired[Optional[bool]]
        application_fee_amount: NotRequired[Optional[int]]
        application_fee_percent: NotRequired[Optional[float]]
        automatic_tax: NotRequired[
            Optional["PaymentLink.CreateParamsAutomaticTax"]
        ]
        billing_address_collection: NotRequired[
            Optional[Literal["auto", "required"]]
        ]
        consent_collection: NotRequired[
            Optional["PaymentLink.CreateParamsConsentCollection"]
        ]
        currency: NotRequired[Optional[str]]
        custom_fields: NotRequired[
            Optional[
                List[
                    "PaymentLink.CreateParamsInvoiceCreationInvoiceDataCustomField"
                ]
            ]
        ]
        custom_text: NotRequired[
            Optional["PaymentLink.CreateParamsCustomText"]
        ]
        customer_creation: NotRequired[
            Optional[Literal["always", "if_required"]]
        ]
        expand: NotRequired[Optional[List[str]]]
        invoice_creation: NotRequired[
            Optional["PaymentLink.CreateParamsInvoiceCreation"]
        ]
        line_items: List["PaymentLink.CreateParamsLineItem"]
        metadata: NotRequired[Optional[Dict[str, str]]]
        on_behalf_of: NotRequired[Optional[str]]
        payment_intent_data: NotRequired[
            Optional["PaymentLink.CreateParamsPaymentIntentData"]
        ]
        payment_method_collection: NotRequired[
            Optional[Literal["always", "if_required"]]
        ]
        payment_method_types: NotRequired[
            Optional[
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
        ]
        phone_number_collection: NotRequired[
            Optional["PaymentLink.CreateParamsPhoneNumberCollection"]
        ]
        shipping_address_collection: NotRequired[
            Optional["PaymentLink.CreateParamsShippingAddressCollection"]
        ]
        shipping_options: NotRequired[
            Optional[List["PaymentLink.CreateParamsShippingOption"]]
        ]
        submit_type: NotRequired[
            Optional[Literal["auto", "book", "donate", "pay"]]
        ]
        subscription_data: NotRequired[
            Optional["PaymentLink.CreateParamsSubscriptionData"]
        ]
        tax_id_collection: NotRequired[
            Optional["PaymentLink.CreateParamsTaxIdCollection"]
        ]
        transfer_data: NotRequired[
            Optional["PaymentLink.CreateParamsTransferData"]
        ]

    class CreateParamsTransferData(TypedDict):
        amount: NotRequired[Optional[int]]
        destination: str

    class CreateParamsTaxIdCollection(TypedDict):
        enabled: bool

    class CreateParamsSubscriptionData(TypedDict):
        description: NotRequired[Optional[str]]
        metadata: NotRequired[Optional[Dict[str, str]]]
        trial_period_days: NotRequired[Optional[int]]

    class CreateParamsShippingOption(TypedDict):
        shipping_rate: NotRequired[Optional[str]]

    class CreateParamsShippingAddressCollection(TypedDict):
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

    class CreateParamsPhoneNumberCollection(TypedDict):
        enabled: bool

    class CreateParamsPaymentIntentData(TypedDict):
        capture_method: NotRequired[
            Optional[Literal["automatic", "automatic_async", "manual"]]
        ]
        metadata: NotRequired[Optional[Dict[str, str]]]
        setup_future_usage: NotRequired[
            Optional[Literal["off_session", "on_session"]]
        ]
        statement_descriptor: NotRequired[Optional[str]]
        statement_descriptor_suffix: NotRequired[Optional[str]]

    class CreateParamsLineItem(TypedDict):
        adjustable_quantity: NotRequired[
            Optional["PaymentLink.CreateParamsLineItemAdjustableQuantity"]
        ]
        price: str
        quantity: int

    class CreateParamsLineItemAdjustableQuantity(TypedDict):
        enabled: bool
        maximum: NotRequired[Optional[int]]
        minimum: NotRequired[Optional[int]]

    class CreateParamsInvoiceCreation(TypedDict):
        enabled: bool
        invoice_data: NotRequired[
            Optional["PaymentLink.CreateParamsInvoiceCreationInvoiceData"]
        ]

    class CreateParamsInvoiceCreationInvoiceData(TypedDict):
        account_tax_ids: NotRequired[Optional[Union[Literal[""], List[str]]]]
        custom_fields: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    List[
                        "PaymentLink.CreateParamsInvoiceCreationInvoiceDataCustomField"
                    ],
                ]
            ]
        ]
        description: NotRequired[Optional[str]]
        footer: NotRequired[Optional[str]]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]
        rendering_options: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentLink.CreateParamsInvoiceCreationInvoiceDataRenderingOptions",
                ]
            ]
        ]

    class CreateParamsInvoiceCreationInvoiceDataRenderingOptions(TypedDict):
        amount_tax_display: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    Literal["exclude_tax", "include_inclusive_tax"],
                ]
            ]
        ]

    class CreateParamsInvoiceCreationInvoiceDataCustomField(TypedDict):
        name: str
        value: str

    class CreateParamsCustomText(TypedDict):
        shipping_address: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentLink.CreateParamsCustomTextShippingAddress",
                ]
            ]
        ]
        submit: NotRequired[
            Optional[
                Union[Literal[""], "PaymentLink.CreateParamsCustomTextSubmit"]
            ]
        ]
        terms_of_service_acceptance: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentLink.CreateParamsCustomTextTermsOfServiceAcceptance",
                ]
            ]
        ]

    class CreateParamsCustomTextTermsOfServiceAcceptance(TypedDict):
        message: str

    class CreateParamsCustomTextSubmit(TypedDict):
        message: str

    class CreateParamsCustomTextShippingAddress(TypedDict):
        message: str

    class CreateParamsCustomField(TypedDict):
        dropdown: NotRequired[
            Optional["PaymentLink.CreateParamsCustomFieldDropdown"]
        ]
        key: str
        label: "PaymentLink.CreateParamsCustomFieldLabel"
        numeric: NotRequired[
            Optional["PaymentLink.CreateParamsCustomFieldNumeric"]
        ]
        optional: NotRequired[Optional[bool]]
        text: NotRequired[Optional["PaymentLink.CreateParamsCustomFieldText"]]
        type: Literal["dropdown", "numeric", "text"]

    class CreateParamsCustomFieldText(TypedDict):
        maximum_length: NotRequired[Optional[int]]
        minimum_length: NotRequired[Optional[int]]

    class CreateParamsCustomFieldNumeric(TypedDict):
        maximum_length: NotRequired[Optional[int]]
        minimum_length: NotRequired[Optional[int]]

    class CreateParamsCustomFieldLabel(TypedDict):
        custom: str
        type: Literal["custom"]

    class CreateParamsCustomFieldDropdown(TypedDict):
        options: List["PaymentLink.CreateParamsCustomFieldDropdownOption"]

    class CreateParamsCustomFieldDropdownOption(TypedDict):
        label: str
        value: str

    class CreateParamsConsentCollection(TypedDict):
        promotions: NotRequired[Optional[Literal["auto", "none"]]]
        terms_of_service: NotRequired[Optional[Literal["none", "required"]]]

    class CreateParamsAutomaticTax(TypedDict):
        enabled: bool

    class CreateParamsAfterCompletion(TypedDict):
        hosted_confirmation: NotRequired[
            Optional[
                "PaymentLink.CreateParamsAfterCompletionHostedConfirmation"
            ]
        ]
        redirect: NotRequired[
            Optional["PaymentLink.CreateParamsAfterCompletionRedirect"]
        ]
        type: Literal["hosted_confirmation", "redirect"]

    class CreateParamsAfterCompletionRedirect(TypedDict):
        url: str

    class CreateParamsAfterCompletionHostedConfirmation(TypedDict):
        custom_message: NotRequired[Optional[str]]

    class ListParams(RequestOptions):
        active: NotRequired[Optional[bool]]
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        starting_after: NotRequired[Optional[str]]

    class ListLineItemsParams(RequestOptions):
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        starting_after: NotRequired[Optional[str]]

    class ModifyParams(RequestOptions):
        active: NotRequired[Optional[bool]]
        after_completion: NotRequired[
            Optional["PaymentLink.ModifyParamsAfterCompletion"]
        ]
        allow_promotion_codes: NotRequired[Optional[bool]]
        automatic_tax: NotRequired[
            Optional["PaymentLink.ModifyParamsAutomaticTax"]
        ]
        billing_address_collection: NotRequired[
            Optional[Literal["auto", "required"]]
        ]
        custom_fields: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    List[
                        "PaymentLink.ModifyParamsInvoiceCreationInvoiceDataCustomField"
                    ],
                ]
            ]
        ]
        custom_text: NotRequired[
            Optional["PaymentLink.ModifyParamsCustomText"]
        ]
        customer_creation: NotRequired[
            Optional[Literal["always", "if_required"]]
        ]
        expand: NotRequired[Optional[List[str]]]
        invoice_creation: NotRequired[
            Optional["PaymentLink.ModifyParamsInvoiceCreation"]
        ]
        line_items: NotRequired[
            Optional[List["PaymentLink.ModifyParamsLineItem"]]
        ]
        metadata: NotRequired[Optional[Dict[str, str]]]
        payment_intent_data: NotRequired[
            Optional["PaymentLink.ModifyParamsPaymentIntentData"]
        ]
        payment_method_collection: NotRequired[
            Optional[Literal["always", "if_required"]]
        ]
        payment_method_types: NotRequired[
            Optional[
                Union[
                    Literal[""],
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
                    ],
                ]
            ]
        ]
        shipping_address_collection: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentLink.ModifyParamsShippingAddressCollection",
                ]
            ]
        ]
        subscription_data: NotRequired[
            Optional["PaymentLink.ModifyParamsSubscriptionData"]
        ]

    class ModifyParamsSubscriptionData(TypedDict):
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]

    class ModifyParamsShippingAddressCollection(TypedDict):
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

    class ModifyParamsPaymentIntentData(TypedDict):
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]
        statement_descriptor: NotRequired[Optional[Union[Literal[""], str]]]
        statement_descriptor_suffix: NotRequired[
            Optional[Union[Literal[""], str]]
        ]

    class ModifyParamsLineItem(TypedDict):
        adjustable_quantity: NotRequired[
            Optional["PaymentLink.ModifyParamsLineItemAdjustableQuantity"]
        ]
        id: str
        quantity: NotRequired[Optional[int]]

    class ModifyParamsLineItemAdjustableQuantity(TypedDict):
        enabled: bool
        maximum: NotRequired[Optional[int]]
        minimum: NotRequired[Optional[int]]

    class ModifyParamsInvoiceCreation(TypedDict):
        enabled: bool
        invoice_data: NotRequired[
            Optional["PaymentLink.ModifyParamsInvoiceCreationInvoiceData"]
        ]

    class ModifyParamsInvoiceCreationInvoiceData(TypedDict):
        account_tax_ids: NotRequired[Optional[Union[Literal[""], List[str]]]]
        custom_fields: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    List[
                        "PaymentLink.ModifyParamsInvoiceCreationInvoiceDataCustomField"
                    ],
                ]
            ]
        ]
        description: NotRequired[Optional[str]]
        footer: NotRequired[Optional[str]]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]
        rendering_options: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentLink.ModifyParamsInvoiceCreationInvoiceDataRenderingOptions",
                ]
            ]
        ]

    class ModifyParamsInvoiceCreationInvoiceDataRenderingOptions(TypedDict):
        amount_tax_display: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    Literal["exclude_tax", "include_inclusive_tax"],
                ]
            ]
        ]

    class ModifyParamsInvoiceCreationInvoiceDataCustomField(TypedDict):
        name: str
        value: str

    class ModifyParamsCustomText(TypedDict):
        shipping_address: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentLink.ModifyParamsCustomTextShippingAddress",
                ]
            ]
        ]
        submit: NotRequired[
            Optional[
                Union[Literal[""], "PaymentLink.ModifyParamsCustomTextSubmit"]
            ]
        ]
        terms_of_service_acceptance: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentLink.ModifyParamsCustomTextTermsOfServiceAcceptance",
                ]
            ]
        ]

    class ModifyParamsCustomTextTermsOfServiceAcceptance(TypedDict):
        message: str

    class ModifyParamsCustomTextSubmit(TypedDict):
        message: str

    class ModifyParamsCustomTextShippingAddress(TypedDict):
        message: str

    class ModifyParamsCustomField(TypedDict):
        dropdown: NotRequired[
            Optional["PaymentLink.ModifyParamsCustomFieldDropdown"]
        ]
        key: str
        label: "PaymentLink.ModifyParamsCustomFieldLabel"
        numeric: NotRequired[
            Optional["PaymentLink.ModifyParamsCustomFieldNumeric"]
        ]
        optional: NotRequired[Optional[bool]]
        text: NotRequired[Optional["PaymentLink.ModifyParamsCustomFieldText"]]
        type: Literal["dropdown", "numeric", "text"]

    class ModifyParamsCustomFieldText(TypedDict):
        maximum_length: NotRequired[Optional[int]]
        minimum_length: NotRequired[Optional[int]]

    class ModifyParamsCustomFieldNumeric(TypedDict):
        maximum_length: NotRequired[Optional[int]]
        minimum_length: NotRequired[Optional[int]]

    class ModifyParamsCustomFieldLabel(TypedDict):
        custom: str
        type: Literal["custom"]

    class ModifyParamsCustomFieldDropdown(TypedDict):
        options: List["PaymentLink.ModifyParamsCustomFieldDropdownOption"]

    class ModifyParamsCustomFieldDropdownOption(TypedDict):
        label: str
        value: str

    class ModifyParamsAutomaticTax(TypedDict):
        enabled: bool

    class ModifyParamsAfterCompletion(TypedDict):
        hosted_confirmation: NotRequired[
            Optional[
                "PaymentLink.ModifyParamsAfterCompletionHostedConfirmation"
            ]
        ]
        redirect: NotRequired[
            Optional["PaymentLink.ModifyParamsAfterCompletionRedirect"]
        ]
        type: Literal["hosted_confirmation", "redirect"]

    class ModifyParamsAfterCompletionRedirect(TypedDict):
        url: str

    class ModifyParamsAfterCompletionHostedConfirmation(TypedDict):
        custom_message: NotRequired[Optional[str]]

    class RetrieveParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    active: bool
    after_completion: StripeObject
    allow_promotion_codes: bool
    application: Optional[ExpandableField["Application"]]
    application_fee_amount: Optional[int]
    application_fee_percent: Optional[float]
    automatic_tax: StripeObject
    billing_address_collection: Literal["auto", "required"]
    consent_collection: Optional[StripeObject]
    currency: str
    custom_fields: List[StripeObject]
    custom_text: StripeObject
    customer_creation: Literal["always", "if_required"]
    id: str
    invoice_creation: Optional[StripeObject]
    line_items: Optional[ListObject["LineItem"]]
    livemode: bool
    metadata: Dict[str, str]
    object: Literal["payment_link"]
    on_behalf_of: Optional[ExpandableField["Account"]]
    payment_intent_data: Optional[StripeObject]
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
    phone_number_collection: StripeObject
    shipping_address_collection: Optional[StripeObject]
    shipping_options: List[StripeObject]
    submit_type: Literal["auto", "book", "donate", "pay"]
    subscription_data: Optional[StripeObject]
    tax_id_collection: StripeObject
    transfer_data: Optional[StripeObject]
    url: str

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["PaymentLink.CreateParams"]
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
        **params: Unpack["PaymentLink.ListParams"]
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
        **params: Unpack["PaymentLink.ListLineItemsParams"]
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
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["PaymentLink.ListLineItemsParams"]
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
    def modify(
        cls, id, **params: Unpack["PaymentLink.ModifyParams"]
    ) -> "PaymentLink":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "PaymentLink",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["PaymentLink.RetrieveParams"]
    ) -> "PaymentLink":
        instance = cls(id, **params)
        instance.refresh()
        return instance
