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
            Optional["PaymentLink.CreateAfterCompletionParams"]
        ]
        allow_promotion_codes: NotRequired[Optional[bool]]
        application_fee_amount: NotRequired[Optional[int]]
        application_fee_percent: NotRequired[Optional[float]]
        automatic_tax: NotRequired[
            Optional["PaymentLink.CreateAutomaticTaxParams"]
        ]
        billing_address_collection: NotRequired[
            Optional[Literal["auto", "required"]]
        ]
        consent_collection: NotRequired[
            Optional["PaymentLink.CreateConsentCollectionParams"]
        ]
        currency: NotRequired[Optional[str]]
        custom_fields: NotRequired[
            Optional[
                List[
                    "PaymentLink.CreateInvoiceCreationInvoiceDataCustomFieldParams"
                ]
            ]
        ]
        custom_text: NotRequired[
            Optional["PaymentLink.CreateCustomTextParams"]
        ]
        customer_creation: NotRequired[
            Optional[Literal["always", "if_required"]]
        ]
        expand: NotRequired[Optional[List[str]]]
        invoice_creation: NotRequired[
            Optional["PaymentLink.CreateInvoiceCreationParams"]
        ]
        line_items: List["PaymentLink.CreateLineItemParams"]
        metadata: NotRequired[Optional[Dict[str, str]]]
        on_behalf_of: NotRequired[Optional[str]]
        payment_intent_data: NotRequired[
            Optional["PaymentLink.CreatePaymentIntentDataParams"]
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
            Optional["PaymentLink.CreatePhoneNumberCollectionParams"]
        ]
        shipping_address_collection: NotRequired[
            Optional["PaymentLink.CreateShippingAddressCollectionParams"]
        ]
        shipping_options: NotRequired[
            Optional[List["PaymentLink.CreateShippingOptionParams"]]
        ]
        submit_type: NotRequired[
            Optional[Literal["auto", "book", "donate", "pay"]]
        ]
        subscription_data: NotRequired[
            Optional["PaymentLink.CreateSubscriptionDataParams"]
        ]
        tax_id_collection: NotRequired[
            Optional["PaymentLink.CreateTaxIdCollectionParams"]
        ]
        transfer_data: NotRequired[
            Optional["PaymentLink.CreateTransferDataParams"]
        ]

    class CreateTransferDataParams(TypedDict):
        amount: NotRequired[Optional[int]]
        destination: str

    class CreateTaxIdCollectionParams(TypedDict):
        enabled: bool

    class CreateSubscriptionDataParams(TypedDict):
        description: NotRequired[Optional[str]]
        metadata: NotRequired[Optional[Dict[str, str]]]
        trial_period_days: NotRequired[Optional[int]]

    class CreateShippingOptionParams(TypedDict):
        shipping_rate: NotRequired[Optional[str]]

    class CreateShippingAddressCollectionParams(TypedDict):
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

    class CreatePhoneNumberCollectionParams(TypedDict):
        enabled: bool

    class CreatePaymentIntentDataParams(TypedDict):
        capture_method: NotRequired[
            Optional[Literal["automatic", "automatic_async", "manual"]]
        ]
        metadata: NotRequired[Optional[Dict[str, str]]]
        setup_future_usage: NotRequired[
            Optional[Literal["off_session", "on_session"]]
        ]
        statement_descriptor: NotRequired[Optional[str]]
        statement_descriptor_suffix: NotRequired[Optional[str]]

    class CreateLineItemParams(TypedDict):
        adjustable_quantity: NotRequired[
            Optional["PaymentLink.CreateLineItemAdjustableQuantityParams"]
        ]
        price: str
        quantity: int

    class CreateLineItemAdjustableQuantityParams(TypedDict):
        enabled: bool
        maximum: NotRequired[Optional[int]]
        minimum: NotRequired[Optional[int]]

    class CreateInvoiceCreationParams(TypedDict):
        enabled: bool
        invoice_data: NotRequired[
            Optional["PaymentLink.CreateInvoiceCreationInvoiceDataParams"]
        ]

    class CreateInvoiceCreationInvoiceDataParams(TypedDict):
        account_tax_ids: NotRequired[Optional[Union[Literal[""], List[str]]]]
        custom_fields: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    List[
                        "PaymentLink.CreateInvoiceCreationInvoiceDataCustomFieldParams"
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
                    "PaymentLink.CreateInvoiceCreationInvoiceDataRenderingOptionsParams",
                ]
            ]
        ]

    class CreateInvoiceCreationInvoiceDataRenderingOptionsParams(TypedDict):
        amount_tax_display: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    Literal["exclude_tax", "include_inclusive_tax"],
                ]
            ]
        ]

    class CreateInvoiceCreationInvoiceDataCustomFieldParams(TypedDict):
        name: str
        value: str

    class CreateCustomTextParams(TypedDict):
        shipping_address: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentLink.CreateCustomTextShippingAddressParams",
                ]
            ]
        ]
        submit: NotRequired[
            Optional[
                Union[Literal[""], "PaymentLink.CreateCustomTextSubmitParams"]
            ]
        ]
        terms_of_service_acceptance: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentLink.CreateCustomTextTermsOfServiceAcceptanceParams",
                ]
            ]
        ]

    class CreateCustomTextTermsOfServiceAcceptanceParams(TypedDict):
        message: str

    class CreateCustomTextSubmitParams(TypedDict):
        message: str

    class CreateCustomTextShippingAddressParams(TypedDict):
        message: str

    class CreateCustomFieldParams(TypedDict):
        dropdown: NotRequired[
            Optional["PaymentLink.CreateCustomFieldDropdownParams"]
        ]
        key: str
        label: "PaymentLink.CreateCustomFieldLabelParams"
        numeric: NotRequired[
            Optional["PaymentLink.CreateCustomFieldNumericParams"]
        ]
        optional: NotRequired[Optional[bool]]
        text: NotRequired[Optional["PaymentLink.CreateCustomFieldTextParams"]]
        type: Literal["dropdown", "numeric", "text"]

    class CreateCustomFieldTextParams(TypedDict):
        maximum_length: NotRequired[Optional[int]]
        minimum_length: NotRequired[Optional[int]]

    class CreateCustomFieldNumericParams(TypedDict):
        maximum_length: NotRequired[Optional[int]]
        minimum_length: NotRequired[Optional[int]]

    class CreateCustomFieldLabelParams(TypedDict):
        custom: str
        type: Literal["custom"]

    class CreateCustomFieldDropdownParams(TypedDict):
        options: List["PaymentLink.CreateCustomFieldDropdownOptionParams"]

    class CreateCustomFieldDropdownOptionParams(TypedDict):
        label: str
        value: str

    class CreateConsentCollectionParams(TypedDict):
        promotions: NotRequired[Optional[Literal["auto", "none"]]]
        terms_of_service: NotRequired[Optional[Literal["none", "required"]]]

    class CreateAutomaticTaxParams(TypedDict):
        enabled: bool

    class CreateAfterCompletionParams(TypedDict):
        hosted_confirmation: NotRequired[
            Optional[
                "PaymentLink.CreateAfterCompletionHostedConfirmationParams"
            ]
        ]
        redirect: NotRequired[
            Optional["PaymentLink.CreateAfterCompletionRedirectParams"]
        ]
        type: Literal["hosted_confirmation", "redirect"]

    class CreateAfterCompletionRedirectParams(TypedDict):
        url: str

    class CreateAfterCompletionHostedConfirmationParams(TypedDict):
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
            Optional["PaymentLink.ModifyAfterCompletionParams"]
        ]
        allow_promotion_codes: NotRequired[Optional[bool]]
        automatic_tax: NotRequired[
            Optional["PaymentLink.ModifyAutomaticTaxParams"]
        ]
        billing_address_collection: NotRequired[
            Optional[Literal["auto", "required"]]
        ]
        custom_fields: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    List[
                        "PaymentLink.ModifyInvoiceCreationInvoiceDataCustomFieldParams"
                    ],
                ]
            ]
        ]
        custom_text: NotRequired[
            Optional["PaymentLink.ModifyCustomTextParams"]
        ]
        customer_creation: NotRequired[
            Optional[Literal["always", "if_required"]]
        ]
        expand: NotRequired[Optional[List[str]]]
        invoice_creation: NotRequired[
            Optional["PaymentLink.ModifyInvoiceCreationParams"]
        ]
        line_items: NotRequired[
            Optional[List["PaymentLink.ModifyLineItemParams"]]
        ]
        metadata: NotRequired[Optional[Dict[str, str]]]
        payment_intent_data: NotRequired[
            Optional["PaymentLink.ModifyPaymentIntentDataParams"]
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
                    "PaymentLink.ModifyShippingAddressCollectionParams",
                ]
            ]
        ]
        subscription_data: NotRequired[
            Optional["PaymentLink.ModifySubscriptionDataParams"]
        ]

    class ModifySubscriptionDataParams(TypedDict):
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]

    class ModifyShippingAddressCollectionParams(TypedDict):
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

    class ModifyPaymentIntentDataParams(TypedDict):
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]
        statement_descriptor: NotRequired[Optional[Union[Literal[""], str]]]
        statement_descriptor_suffix: NotRequired[
            Optional[Union[Literal[""], str]]
        ]

    class ModifyLineItemParams(TypedDict):
        adjustable_quantity: NotRequired[
            Optional["PaymentLink.ModifyLineItemAdjustableQuantityParams"]
        ]
        id: str
        quantity: NotRequired[Optional[int]]

    class ModifyLineItemAdjustableQuantityParams(TypedDict):
        enabled: bool
        maximum: NotRequired[Optional[int]]
        minimum: NotRequired[Optional[int]]

    class ModifyInvoiceCreationParams(TypedDict):
        enabled: bool
        invoice_data: NotRequired[
            Optional["PaymentLink.ModifyInvoiceCreationInvoiceDataParams"]
        ]

    class ModifyInvoiceCreationInvoiceDataParams(TypedDict):
        account_tax_ids: NotRequired[Optional[Union[Literal[""], List[str]]]]
        custom_fields: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    List[
                        "PaymentLink.ModifyInvoiceCreationInvoiceDataCustomFieldParams"
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
                    "PaymentLink.ModifyInvoiceCreationInvoiceDataRenderingOptionsParams",
                ]
            ]
        ]

    class ModifyInvoiceCreationInvoiceDataRenderingOptionsParams(TypedDict):
        amount_tax_display: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    Literal["exclude_tax", "include_inclusive_tax"],
                ]
            ]
        ]

    class ModifyInvoiceCreationInvoiceDataCustomFieldParams(TypedDict):
        name: str
        value: str

    class ModifyCustomTextParams(TypedDict):
        shipping_address: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentLink.ModifyCustomTextShippingAddressParams",
                ]
            ]
        ]
        submit: NotRequired[
            Optional[
                Union[Literal[""], "PaymentLink.ModifyCustomTextSubmitParams"]
            ]
        ]
        terms_of_service_acceptance: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentLink.ModifyCustomTextTermsOfServiceAcceptanceParams",
                ]
            ]
        ]

    class ModifyCustomTextTermsOfServiceAcceptanceParams(TypedDict):
        message: str

    class ModifyCustomTextSubmitParams(TypedDict):
        message: str

    class ModifyCustomTextShippingAddressParams(TypedDict):
        message: str

    class ModifyCustomFieldParams(TypedDict):
        dropdown: NotRequired[
            Optional["PaymentLink.ModifyCustomFieldDropdownParams"]
        ]
        key: str
        label: "PaymentLink.ModifyCustomFieldLabelParams"
        numeric: NotRequired[
            Optional["PaymentLink.ModifyCustomFieldNumericParams"]
        ]
        optional: NotRequired[Optional[bool]]
        text: NotRequired[Optional["PaymentLink.ModifyCustomFieldTextParams"]]
        type: Literal["dropdown", "numeric", "text"]

    class ModifyCustomFieldTextParams(TypedDict):
        maximum_length: NotRequired[Optional[int]]
        minimum_length: NotRequired[Optional[int]]

    class ModifyCustomFieldNumericParams(TypedDict):
        maximum_length: NotRequired[Optional[int]]
        minimum_length: NotRequired[Optional[int]]

    class ModifyCustomFieldLabelParams(TypedDict):
        custom: str
        type: Literal["custom"]

    class ModifyCustomFieldDropdownParams(TypedDict):
        options: List["PaymentLink.ModifyCustomFieldDropdownOptionParams"]

    class ModifyCustomFieldDropdownOptionParams(TypedDict):
        label: str
        value: str

    class ModifyAutomaticTaxParams(TypedDict):
        enabled: bool

    class ModifyAfterCompletionParams(TypedDict):
        hosted_confirmation: NotRequired[
            Optional[
                "PaymentLink.ModifyAfterCompletionHostedConfirmationParams"
            ]
        ]
        redirect: NotRequired[
            Optional["PaymentLink.ModifyAfterCompletionRedirectParams"]
        ]
        type: Literal["hosted_confirmation", "redirect"]

    class ModifyAfterCompletionRedirectParams(TypedDict):
        url: str

    class ModifyAfterCompletionHostedConfirmationParams(TypedDict):
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
