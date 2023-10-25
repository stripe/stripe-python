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
from typing import ClassVar, Dict, List, Optional, cast
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

    OBJECT_NAME: ClassVar[Literal["payment_link"]] = "payment_link"

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
        class Liability(StripeObject):
            account: Optional[ExpandableField["Account"]]
            type: Literal["account", "self"]

        enabled: bool
        liability: Optional[Liability]
        _inner_class_types = {"liability": Liability}

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

            class Issuer(StripeObject):
                account: Optional[ExpandableField["Account"]]
                type: Literal["account", "self"]

            class RenderingOptions(StripeObject):
                amount_tax_display: Optional[str]

            account_tax_ids: Optional[List[ExpandableField["TaxId"]]]
            custom_fields: Optional[List[CustomField]]
            description: Optional[str]
            footer: Optional[str]
            issuer: Optional[Issuer]
            metadata: Optional[Dict[str, str]]
            rendering_options: Optional[RenderingOptions]
            _inner_class_types = {
                "custom_fields": CustomField,
                "issuer": Issuer,
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
        class InvoiceSettings(StripeObject):
            class Issuer(StripeObject):
                account: Optional[ExpandableField["Account"]]
                type: Literal["account", "self"]

            issuer: Optional[Issuer]
            _inner_class_types = {"issuer": Issuer}

        description: Optional[str]
        invoice_settings: Optional[InvoiceSettings]
        metadata: Dict[str, str]
        trial_period_days: Optional[int]
        _inner_class_types = {"invoice_settings": InvoiceSettings}

    class TaxIdCollection(StripeObject):
        enabled: bool

    class TransferData(StripeObject):
        amount: Optional[int]
        destination: ExpandableField["Account"]

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
            invoice_settings: NotRequired[
                "PaymentLink.CreateParamsSubscriptionDataInvoiceSettings|None"
            ]
            metadata: NotRequired["Dict[str, str]|None"]
            trial_period_days: NotRequired["int|None"]

        class CreateParamsSubscriptionDataInvoiceSettings(TypedDict):
            issuer: NotRequired[
                "PaymentLink.CreateParamsSubscriptionDataInvoiceSettingsIssuer|None"
            ]

        class CreateParamsSubscriptionDataInvoiceSettingsIssuer(TypedDict):
            account: NotRequired["str|None"]
            type: Literal["account", "self"]

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
            issuer: NotRequired[
                "PaymentLink.CreateParamsInvoiceCreationInvoiceDataIssuer|None"
            ]
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

        class CreateParamsInvoiceCreationInvoiceDataIssuer(TypedDict):
            account: NotRequired["str|None"]
            type: Literal["account", "self"]

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
            liability: NotRequired[
                "PaymentLink.CreateParamsAutomaticTaxLiability|None"
            ]

        class CreateParamsAutomaticTaxLiability(TypedDict):
            account: NotRequired["str|None"]
            type: Literal["account", "self"]

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
            invoice_settings: NotRequired[
                "PaymentLink.ModifyParamsSubscriptionDataInvoiceSettings|None"
            ]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]

        class ModifyParamsSubscriptionDataInvoiceSettings(TypedDict):
            issuer: NotRequired[
                "PaymentLink.ModifyParamsSubscriptionDataInvoiceSettingsIssuer|None"
            ]

        class ModifyParamsSubscriptionDataInvoiceSettingsIssuer(TypedDict):
            account: NotRequired["str|None"]
            type: Literal["account", "self"]

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
            issuer: NotRequired[
                "PaymentLink.ModifyParamsInvoiceCreationInvoiceDataIssuer|None"
            ]
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

        class ModifyParamsInvoiceCreationInvoiceDataIssuer(TypedDict):
            account: NotRequired["str|None"]
            type: Literal["account", "self"]

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
            liability: NotRequired[
                "PaymentLink.ModifyParamsAutomaticTaxLiability|None"
            ]

        class ModifyParamsAutomaticTaxLiability(TypedDict):
            account: NotRequired["str|None"]
            type: Literal["account", "self"]

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
    ) -> ListObject["LineItem"]:
        return cast(
            ListObject["LineItem"],
            cls._static_request(
                "get",
                "/v1/payment_links/{payment_link}/line_items".format(
                    payment_link=util.sanitize_id(payment_link)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @util.class_method_variant("_cls_list_line_items")
    def list_line_items(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["PaymentLink.ListLineItemsParams"]
    ) -> ListObject["LineItem"]:
        return cast(
            ListObject["LineItem"],
            self._request(
                "get",
                "/v1/payment_links/{payment_link}/line_items".format(
                    payment_link=util.sanitize_id(self.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
        )

    @classmethod
    def modify(
        cls, id: str, **params: Unpack["PaymentLink.ModifyParams"]
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
