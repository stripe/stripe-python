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
    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            after_completion: NotRequired[
                "PaymentLink.CreateParamsAfterCompletion|None"
            ]
            allow_promotion_codes: NotRequired["bool|None"]
            application_fee_amount: NotRequired["int|None"]
            application_fee_percent: NotRequired["float|None"]
            automatic_tax: NotRequired[
                "PaymentLink.CreateParamsAutomaticTax|None"
            ]
            billing_address_collection: NotRequired[
                "Literal['auto', 'required']|None"
            ]
            consent_collection: NotRequired[
                "PaymentLink.CreateParamsConsentCollection|None"
            ]
            currency: NotRequired["str|None"]
            custom_fields: NotRequired[
                "List[PaymentLink.CreateParamsCustomField]|None"
            ]
            custom_text: NotRequired["PaymentLink.CreateParamsCustomText|None"]
            customer_creation: NotRequired[
                "Literal['always', 'if_required']|None"
            ]
            expand: NotRequired["List[str]|None"]
            invoice_creation: NotRequired[
                "PaymentLink.CreateParamsInvoiceCreation|None"
            ]
            line_items: List["PaymentLink.CreateParamsLineItem"]
            metadata: NotRequired["Dict[str, str]|None"]
            on_behalf_of: NotRequired["str|None"]
            payment_intent_data: NotRequired[
                "PaymentLink.CreateParamsPaymentIntentData|None"
            ]
            payment_method_collection: NotRequired[
                "Literal['always', 'if_required']|None"
            ]
            payment_method_types: NotRequired[
                "List[Literal['affirm', 'afterpay_clearpay', 'alipay', 'au_becs_debit', 'bacs_debit', 'bancontact', 'blik', 'boleto', 'card', 'cashapp', 'eps', 'fpx', 'giropay', 'grabpay', 'ideal', 'klarna', 'konbini', 'link', 'oxxo', 'p24', 'paynow', 'paypal', 'pix', 'promptpay', 'sepa_debit', 'sofort', 'us_bank_account', 'wechat_pay']]|None"
            ]
            phone_number_collection: NotRequired[
                "PaymentLink.CreateParamsPhoneNumberCollection|None"
            ]
            shipping_address_collection: NotRequired[
                "PaymentLink.CreateParamsShippingAddressCollection|None"
            ]
            shipping_options: NotRequired[
                "List[PaymentLink.CreateParamsShippingOption]|None"
            ]
            submit_type: NotRequired[
                "Literal['auto', 'book', 'donate', 'pay']|None"
            ]
            subscription_data: NotRequired[
                "PaymentLink.CreateParamsSubscriptionData|None"
            ]
            tax_id_collection: NotRequired[
                "PaymentLink.CreateParamsTaxIdCollection|None"
            ]
            transfer_data: NotRequired[
                "PaymentLink.CreateParamsTransferData|None"
            ]

        class CreateParamsTransferData(TypedDict):
            amount: NotRequired["int|None"]
            destination: str

        class CreateParamsTaxIdCollection(TypedDict):
            enabled: bool

        class CreateParamsSubscriptionData(TypedDict):
            description: NotRequired["str|None"]
            metadata: NotRequired["Dict[str, str]|None"]
            trial_period_days: NotRequired["int|None"]

        class CreateParamsShippingOption(TypedDict):
            shipping_rate: NotRequired["str|None"]

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
                "Literal['automatic', 'automatic_async', 'manual']|None"
            ]
            metadata: NotRequired["Dict[str, str]|None"]
            setup_future_usage: NotRequired[
                "Literal['off_session', 'on_session']|None"
            ]
            statement_descriptor: NotRequired["str|None"]
            statement_descriptor_suffix: NotRequired["str|None"]

        class CreateParamsLineItem(TypedDict):
            adjustable_quantity: NotRequired[
                "PaymentLink.CreateParamsLineItemAdjustableQuantity|None"
            ]
            price: str
            quantity: int

        class CreateParamsLineItemAdjustableQuantity(TypedDict):
            enabled: bool
            maximum: NotRequired["int|None"]
            minimum: NotRequired["int|None"]

        class CreateParamsInvoiceCreation(TypedDict):
            enabled: bool
            invoice_data: NotRequired[
                "PaymentLink.CreateParamsInvoiceCreationInvoiceData|None"
            ]

        class CreateParamsInvoiceCreationInvoiceData(TypedDict):
            account_tax_ids: NotRequired["Literal['']|List[str]|None"]
            custom_fields: NotRequired[
                "Literal['']|List[PaymentLink.CreateParamsInvoiceCreationInvoiceDataCustomField]|None"
            ]
            description: NotRequired["str|None"]
            footer: NotRequired["str|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            rendering_options: NotRequired[
                "Literal['']|PaymentLink.CreateParamsInvoiceCreationInvoiceDataRenderingOptions|None"
            ]

        class CreateParamsInvoiceCreationInvoiceDataRenderingOptions(
            TypedDict
        ):
            amount_tax_display: NotRequired[
                "Literal['']|Literal['exclude_tax', 'include_inclusive_tax']|None"
            ]

        class CreateParamsInvoiceCreationInvoiceDataCustomField(TypedDict):
            name: str
            value: str

        class CreateParamsCustomText(TypedDict):
            shipping_address: NotRequired[
                "Literal['']|PaymentLink.CreateParamsCustomTextShippingAddress|None"
            ]
            submit: NotRequired[
                "Literal['']|PaymentLink.CreateParamsCustomTextSubmit|None"
            ]
            terms_of_service_acceptance: NotRequired[
                "Literal['']|PaymentLink.CreateParamsCustomTextTermsOfServiceAcceptance|None"
            ]

        class CreateParamsCustomTextTermsOfServiceAcceptance(TypedDict):
            message: str

        class CreateParamsCustomTextSubmit(TypedDict):
            message: str

        class CreateParamsCustomTextShippingAddress(TypedDict):
            message: str

        class CreateParamsCustomField(TypedDict):
            dropdown: NotRequired[
                "PaymentLink.CreateParamsCustomFieldDropdown|None"
            ]
            key: str
            label: "PaymentLink.CreateParamsCustomFieldLabel"
            numeric: NotRequired[
                "PaymentLink.CreateParamsCustomFieldNumeric|None"
            ]
            optional: NotRequired["bool|None"]
            text: NotRequired["PaymentLink.CreateParamsCustomFieldText|None"]
            type: Literal["dropdown", "numeric", "text"]

        class CreateParamsCustomFieldText(TypedDict):
            maximum_length: NotRequired["int|None"]
            minimum_length: NotRequired["int|None"]

        class CreateParamsCustomFieldNumeric(TypedDict):
            maximum_length: NotRequired["int|None"]
            minimum_length: NotRequired["int|None"]

        class CreateParamsCustomFieldLabel(TypedDict):
            custom: str
            type: Literal["custom"]

        class CreateParamsCustomFieldDropdown(TypedDict):
            options: List["PaymentLink.CreateParamsCustomFieldDropdownOption"]

        class CreateParamsCustomFieldDropdownOption(TypedDict):
            label: str
            value: str

        class CreateParamsConsentCollection(TypedDict):
            promotions: NotRequired["Literal['auto', 'none']|None"]
            terms_of_service: NotRequired["Literal['none', 'required']|None"]

        class CreateParamsAutomaticTax(TypedDict):
            enabled: bool

        class CreateParamsAfterCompletion(TypedDict):
            hosted_confirmation: NotRequired[
                "PaymentLink.CreateParamsAfterCompletionHostedConfirmation|None"
            ]
            redirect: NotRequired[
                "PaymentLink.CreateParamsAfterCompletionRedirect|None"
            ]
            type: Literal["hosted_confirmation", "redirect"]

        class CreateParamsAfterCompletionRedirect(TypedDict):
            url: str

        class CreateParamsAfterCompletionHostedConfirmation(TypedDict):
            custom_message: NotRequired["str|None"]

        class ListParams(RequestOptions):
            active: NotRequired["bool|None"]
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]

        class ListLineItemsParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]

        class ModifyParams(RequestOptions):
            active: NotRequired["bool|None"]
            after_completion: NotRequired[
                "PaymentLink.ModifyParamsAfterCompletion|None"
            ]
            allow_promotion_codes: NotRequired["bool|None"]
            automatic_tax: NotRequired[
                "PaymentLink.ModifyParamsAutomaticTax|None"
            ]
            billing_address_collection: NotRequired[
                "Literal['auto', 'required']|None"
            ]
            custom_fields: NotRequired[
                "Literal['']|List[PaymentLink.ModifyParamsCustomField]|None"
            ]
            custom_text: NotRequired["PaymentLink.ModifyParamsCustomText|None"]
            customer_creation: NotRequired[
                "Literal['always', 'if_required']|None"
            ]
            expand: NotRequired["List[str]|None"]
            invoice_creation: NotRequired[
                "PaymentLink.ModifyParamsInvoiceCreation|None"
            ]
            line_items: NotRequired[
                "List[PaymentLink.ModifyParamsLineItem]|None"
            ]
            metadata: NotRequired["Dict[str, str]|None"]
            payment_intent_data: NotRequired[
                "PaymentLink.ModifyParamsPaymentIntentData|None"
            ]
            payment_method_collection: NotRequired[
                "Literal['always', 'if_required']|None"
            ]
            payment_method_types: NotRequired[
                "Literal['']|List[Literal['affirm', 'afterpay_clearpay', 'alipay', 'au_becs_debit', 'bacs_debit', 'bancontact', 'blik', 'boleto', 'card', 'cashapp', 'eps', 'fpx', 'giropay', 'grabpay', 'ideal', 'klarna', 'konbini', 'link', 'oxxo', 'p24', 'paynow', 'paypal', 'pix', 'promptpay', 'sepa_debit', 'sofort', 'us_bank_account', 'wechat_pay']]|None"
            ]
            shipping_address_collection: NotRequired[
                "Literal['']|PaymentLink.ModifyParamsShippingAddressCollection|None"
            ]
            subscription_data: NotRequired[
                "PaymentLink.ModifyParamsSubscriptionData|None"
            ]

        class ModifyParamsSubscriptionData(TypedDict):
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]

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
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            statement_descriptor: NotRequired["Literal['']|str|None"]
            statement_descriptor_suffix: NotRequired["Literal['']|str|None"]

        class ModifyParamsLineItem(TypedDict):
            adjustable_quantity: NotRequired[
                "PaymentLink.ModifyParamsLineItemAdjustableQuantity|None"
            ]
            id: str
            quantity: NotRequired["int|None"]

        class ModifyParamsLineItemAdjustableQuantity(TypedDict):
            enabled: bool
            maximum: NotRequired["int|None"]
            minimum: NotRequired["int|None"]

        class ModifyParamsInvoiceCreation(TypedDict):
            enabled: bool
            invoice_data: NotRequired[
                "PaymentLink.ModifyParamsInvoiceCreationInvoiceData|None"
            ]

        class ModifyParamsInvoiceCreationInvoiceData(TypedDict):
            account_tax_ids: NotRequired["Literal['']|List[str]|None"]
            custom_fields: NotRequired[
                "Literal['']|List[PaymentLink.ModifyParamsInvoiceCreationInvoiceDataCustomField]|None"
            ]
            description: NotRequired["str|None"]
            footer: NotRequired["str|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            rendering_options: NotRequired[
                "Literal['']|PaymentLink.ModifyParamsInvoiceCreationInvoiceDataRenderingOptions|None"
            ]

        class ModifyParamsInvoiceCreationInvoiceDataRenderingOptions(
            TypedDict
        ):
            amount_tax_display: NotRequired[
                "Literal['']|Literal['exclude_tax', 'include_inclusive_tax']|None"
            ]

        class ModifyParamsInvoiceCreationInvoiceDataCustomField(TypedDict):
            name: str
            value: str

        class ModifyParamsCustomText(TypedDict):
            shipping_address: NotRequired[
                "Literal['']|PaymentLink.ModifyParamsCustomTextShippingAddress|None"
            ]
            submit: NotRequired[
                "Literal['']|PaymentLink.ModifyParamsCustomTextSubmit|None"
            ]
            terms_of_service_acceptance: NotRequired[
                "Literal['']|PaymentLink.ModifyParamsCustomTextTermsOfServiceAcceptance|None"
            ]

        class ModifyParamsCustomTextTermsOfServiceAcceptance(TypedDict):
            message: str

        class ModifyParamsCustomTextSubmit(TypedDict):
            message: str

        class ModifyParamsCustomTextShippingAddress(TypedDict):
            message: str

        class ModifyParamsCustomField(TypedDict):
            dropdown: NotRequired[
                "PaymentLink.ModifyParamsCustomFieldDropdown|None"
            ]
            key: str
            label: "PaymentLink.ModifyParamsCustomFieldLabel"
            numeric: NotRequired[
                "PaymentLink.ModifyParamsCustomFieldNumeric|None"
            ]
            optional: NotRequired["bool|None"]
            text: NotRequired["PaymentLink.ModifyParamsCustomFieldText|None"]
            type: Literal["dropdown", "numeric", "text"]

        class ModifyParamsCustomFieldText(TypedDict):
            maximum_length: NotRequired["int|None"]
            minimum_length: NotRequired["int|None"]

        class ModifyParamsCustomFieldNumeric(TypedDict):
            maximum_length: NotRequired["int|None"]
            minimum_length: NotRequired["int|None"]

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
                "PaymentLink.ModifyParamsAfterCompletionHostedConfirmation|None"
            ]
            redirect: NotRequired[
                "PaymentLink.ModifyParamsAfterCompletionRedirect|None"
            ]
            type: Literal["hosted_confirmation", "redirect"]

        class ModifyParamsAfterCompletionRedirect(TypedDict):
            url: str

        class ModifyParamsAfterCompletionHostedConfirmation(TypedDict):
            custom_message: NotRequired["str|None"]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

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
