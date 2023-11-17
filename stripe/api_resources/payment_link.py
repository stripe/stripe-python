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
from stripe.util import class_method_variant
from typing import ClassVar, Dict, List, Optional, cast, overload
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
            """
            The custom message that is displayed to the customer after the purchase is complete.
            """

        class Redirect(StripeObject):
            url: str
            """
            The URL the customer will be redirected to after the purchase is complete.
            """

        hosted_confirmation: Optional[HostedConfirmation]
        redirect: Optional[Redirect]
        type: Literal["hosted_confirmation", "redirect"]
        """
        The specified behavior after the purchase is complete.
        """
        _inner_class_types = {
            "hosted_confirmation": HostedConfirmation,
            "redirect": Redirect,
        }

    class AutomaticTax(StripeObject):
        enabled: bool
        """
        If `true`, tax will be calculated automatically using the customer's location.
        """

    class ConsentCollection(StripeObject):
        promotions: Optional[Literal["auto", "none"]]
        """
        If set to `auto`, enables the collection of customer consent for promotional communications.
        """
        terms_of_service: Optional[Literal["none", "required"]]
        """
        If set to `required`, it requires cutomers to accept the terms of service before being able to pay. If set to `none`, customers won't be shown a checkbox to accept the terms of service.
        """

    class CustomField(StripeObject):
        class Dropdown(StripeObject):
            class Option(StripeObject):
                label: str
                """
                The label for the option, displayed to the customer. Up to 100 characters.
                """
                value: str
                """
                The value for this option, not displayed to the customer, used by your integration to reconcile the option selected by the customer. Must be unique to this option, alphanumeric, and up to 100 characters.
                """

            options: List[Option]
            """
            The options available for the customer to select. Up to 200 options allowed.
            """
            _inner_class_types = {"options": Option}

        class Label(StripeObject):
            custom: Optional[str]
            """
            Custom text for the label, displayed to the customer. Up to 50 characters.
            """
            type: Literal["custom"]
            """
            The type of the label.
            """

        class Numeric(StripeObject):
            maximum_length: Optional[int]
            """
            The maximum character length constraint for the customer's input.
            """
            minimum_length: Optional[int]
            """
            The minimum character length requirement for the customer's input.
            """

        class Text(StripeObject):
            maximum_length: Optional[int]
            """
            The maximum character length constraint for the customer's input.
            """
            minimum_length: Optional[int]
            """
            The minimum character length requirement for the customer's input.
            """

        dropdown: Optional[Dropdown]
        key: str
        """
        String of your choice that your integration can use to reconcile this field. Must be unique to this field, alphanumeric, and up to 200 characters.
        """
        label: Label
        numeric: Optional[Numeric]
        optional: bool
        """
        Whether the customer is required to complete the field before completing the Checkout Session. Defaults to `false`.
        """
        text: Optional[Text]
        type: Literal["dropdown", "numeric", "text"]
        """
        The type of the field.
        """
        _inner_class_types = {
            "dropdown": Dropdown,
            "label": Label,
            "numeric": Numeric,
            "text": Text,
        }

    class CustomText(StripeObject):
        class ShippingAddress(StripeObject):
            message: str
            """
            Text may be up to 1200 characters in length.
            """

        class Submit(StripeObject):
            message: str
            """
            Text may be up to 1200 characters in length.
            """

        class TermsOfServiceAcceptance(StripeObject):
            message: str
            """
            Text may be up to 1200 characters in length.
            """

        shipping_address: Optional[ShippingAddress]
        """
        Custom text that should be displayed alongside shipping address collection.
        """
        submit: Optional[Submit]
        """
        Custom text that should be displayed alongside the payment confirmation button.
        """
        terms_of_service_acceptance: Optional[TermsOfServiceAcceptance]
        """
        Custom text that should be displayed in place of the default terms of service agreement text.
        """
        _inner_class_types = {
            "shipping_address": ShippingAddress,
            "submit": Submit,
            "terms_of_service_acceptance": TermsOfServiceAcceptance,
        }

    class InvoiceCreation(StripeObject):
        class InvoiceData(StripeObject):
            class CustomField(StripeObject):
                name: str
                """
                The name of the custom field.
                """
                value: str
                """
                The value of the custom field.
                """

            class RenderingOptions(StripeObject):
                amount_tax_display: Optional[str]
                """
                How line-item prices and amounts will be displayed with respect to tax on invoice PDFs.
                """

            account_tax_ids: Optional[List[ExpandableField["TaxId"]]]
            """
            The account tax IDs associated with the invoice.
            """
            custom_fields: Optional[List[CustomField]]
            """
            A list of up to 4 custom fields to be displayed on the invoice.
            """
            description: Optional[str]
            """
            An arbitrary string attached to the object. Often useful for displaying to users.
            """
            footer: Optional[str]
            """
            Footer to be displayed on the invoice.
            """
            metadata: Optional[Dict[str, str]]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
            """
            rendering_options: Optional[RenderingOptions]
            """
            Options for invoice PDF rendering.
            """
            _inner_class_types = {
                "custom_fields": CustomField,
                "rendering_options": RenderingOptions,
            }

        enabled: bool
        """
        Enable creating an invoice on successful payment.
        """
        invoice_data: Optional[InvoiceData]
        """
        Configuration for the invoice. Default invoice values will be used if unspecified.
        """
        _inner_class_types = {"invoice_data": InvoiceData}

    class PaymentIntentData(StripeObject):
        capture_method: Optional[
            Literal["automatic", "automatic_async", "manual"]
        ]
        """
        Indicates when the funds will be captured from the customer's account.
        """
        description: Optional[str]
        """
        An arbitrary string attached to the object. Often useful for displaying to users.
        """
        metadata: Dict[str, str]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that will set metadata on [Payment Intents](https://stripe.com/docs/api/payment_intents) generated from this payment link.
        """
        setup_future_usage: Optional[Literal["off_session", "on_session"]]
        """
        Indicates that you intend to make future payments with the payment method collected during checkout.
        """
        statement_descriptor: Optional[str]
        """
        Extra information about the payment. This will appear on your customer's statement when this payment succeeds in creating a charge.
        """
        statement_descriptor_suffix: Optional[str]
        """
        Provides information about the charge that customers see on their statements. Concatenated with the prefix (shortened descriptor) or statement descriptor that's set on the account to form the complete statement descriptor. Maximum 22 characters for the concatenated descriptor.
        """

    class PhoneNumberCollection(StripeObject):
        enabled: bool
        """
        If `true`, a phone number will be collected during checkout.
        """

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
        """
        An array of two-letter ISO country codes representing which countries Checkout should provide as options for shipping locations. Unsupported country codes: `AS, CX, CC, CU, HM, IR, KP, MH, FM, NF, MP, PW, SD, SY, UM, VI`.
        """

    class ShippingOption(StripeObject):
        shipping_amount: int
        """
        A non-negative integer in cents representing how much to charge.
        """
        shipping_rate: ExpandableField["ShippingRate"]
        """
        The ID of the Shipping Rate to use for this shipping option.
        """

    class SubscriptionData(StripeObject):
        description: Optional[str]
        """
        The subscription's description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs.
        """
        metadata: Dict[str, str]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that will set metadata on [Subscriptions](https://stripe.com/docs/api/subscriptions) generated from this payment link.
        """
        trial_period_days: Optional[int]
        """
        Integer representing the number of trial period days before the customer is charged for the first time.
        """

    class TaxIdCollection(StripeObject):
        enabled: bool
        """
        Indicates whether tax ID collection is enabled for the session.
        """

    class TransferData(StripeObject):
        amount: Optional[int]
        """
        The amount in cents (or local equivalent) that will be transferred to the destination account. By default, the entire amount is transferred to the destination.
        """
        destination: ExpandableField["Account"]
        """
        The connected account receiving the transfer.
        """

    class CreateParams(RequestOptions):
        after_completion: NotRequired[
            "PaymentLink.CreateParamsAfterCompletion"
        ]
        """
        Behavior after the purchase is complete.
        """
        allow_promotion_codes: NotRequired["bool"]
        """
        Enables user redeemable promotion codes.
        """
        application_fee_amount: NotRequired["int"]
        """
        The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account. Can only be applied when there are no line items with recurring prices.
        """
        application_fee_percent: NotRequired["float"]
        """
        A non-negative decimal between 0 and 100, with at most two decimal places. This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account. There must be at least 1 line item with a recurring price to use this field.
        """
        automatic_tax: NotRequired["PaymentLink.CreateParamsAutomaticTax"]
        """
        Configuration for automatic tax collection.
        """
        billing_address_collection: NotRequired["Literal['auto', 'required']"]
        """
        Configuration for collecting the customer's billing address.
        """
        consent_collection: NotRequired[
            "PaymentLink.CreateParamsConsentCollection"
        ]
        """
        Configure fields to gather active consent from customers.
        """
        currency: NotRequired["str"]
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies) and supported by each line item's price.
        """
        custom_fields: NotRequired["List[PaymentLink.CreateParamsCustomField]"]
        """
        Collect additional information from your customer using custom fields. Up to 2 fields are supported.
        """
        custom_text: NotRequired["PaymentLink.CreateParamsCustomText"]
        """
        Display additional text for your customers using custom text.
        """
        customer_creation: NotRequired["Literal['always', 'if_required']"]
        """
        Configures whether [checkout sessions](https://stripe.com/docs/api/checkout/sessions) created by this payment link create a [Customer](https://stripe.com/docs/api/customers).
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        invoice_creation: NotRequired[
            "PaymentLink.CreateParamsInvoiceCreation"
        ]
        """
        Generate a post-purchase Invoice for one-time payments.
        """
        line_items: List["PaymentLink.CreateParamsLineItem"]
        """
        The line items representing what is being sold. Each line item represents an item being sold. Up to 20 line items are supported.
        """
        metadata: NotRequired["Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. Metadata associated with this Payment Link will automatically be copied to [checkout sessions](https://stripe.com/docs/api/checkout/sessions) created by this payment link.
        """
        on_behalf_of: NotRequired["str"]
        """
        The account on behalf of which to charge.
        """
        payment_intent_data: NotRequired[
            "PaymentLink.CreateParamsPaymentIntentData"
        ]
        """
        A subset of parameters to be passed to PaymentIntent creation for Checkout Sessions in `payment` mode.
        """
        payment_method_collection: NotRequired[
            "Literal['always', 'if_required']"
        ]
        """
        Specify whether Checkout should collect a payment method. When set to `if_required`, Checkout will not collect a payment method when the total due for the session is 0.This may occur if the Checkout Session includes a free trial or a discount.

        Can only be set in `subscription` mode.

        If you'd like information on how to collect a payment method outside of Checkout, read the guide on [configuring subscriptions with a free trial](https://stripe.com/docs/payments/checkout/free-trials).
        """
        payment_method_types: NotRequired[
            "List[Literal['affirm', 'afterpay_clearpay', 'alipay', 'au_becs_debit', 'bacs_debit', 'bancontact', 'blik', 'boleto', 'card', 'cashapp', 'eps', 'fpx', 'giropay', 'grabpay', 'ideal', 'klarna', 'konbini', 'link', 'oxxo', 'p24', 'paynow', 'paypal', 'pix', 'promptpay', 'sepa_debit', 'sofort', 'us_bank_account', 'wechat_pay']]"
        ]
        """
        The list of payment method types that customers can use. If no value is passed, Stripe will dynamically show relevant payment methods from your [payment method settings](https://dashboard.stripe.com/settings/payment_methods) (20+ payment methods [supported](https://stripe.com/docs/payments/payment-methods/integration-options#payment-method-product-support)).
        """
        phone_number_collection: NotRequired[
            "PaymentLink.CreateParamsPhoneNumberCollection"
        ]
        """
        Controls phone number collection settings during checkout.

        We recommend that you review your privacy policy and check with your legal contacts.
        """
        shipping_address_collection: NotRequired[
            "PaymentLink.CreateParamsShippingAddressCollection"
        ]
        """
        Configuration for collecting the customer's shipping address.
        """
        shipping_options: NotRequired[
            "List[PaymentLink.CreateParamsShippingOption]"
        ]
        """
        The shipping rate options to apply to [checkout sessions](https://stripe.com/docs/api/checkout/sessions) created by this payment link.
        """
        submit_type: NotRequired["Literal['auto', 'book', 'donate', 'pay']"]
        """
        Describes the type of transaction being performed in order to customize relevant text on the page, such as the submit button. Changing this value will also affect the hostname in the [url](https://stripe.com/docs/api/payment_links/payment_links/object#url) property (example: `donate.stripe.com`).
        """
        subscription_data: NotRequired[
            "PaymentLink.CreateParamsSubscriptionData"
        ]
        """
        When creating a subscription, the specified configuration data will be used. There must be at least one line item with a recurring price to use `subscription_data`.
        """
        tax_id_collection: NotRequired[
            "PaymentLink.CreateParamsTaxIdCollection"
        ]
        """
        Controls tax ID collection during checkout.
        """
        transfer_data: NotRequired["PaymentLink.CreateParamsTransferData"]
        """
        The account (if any) the payments will be attributed to for tax reporting, and where funds from each payment will be transferred to.
        """

    class CreateParamsTransferData(TypedDict):
        amount: NotRequired["int"]
        """
        The amount that will be transferred automatically when a charge succeeds.
        """
        destination: str
        """
        If specified, successful charges will be attributed to the destination
        account for tax reporting, and the funds from charges will be transferred
        to the destination account. The ID of the resulting transfer will be
        returned on the successful charge's `transfer` field.
        """

    class CreateParamsTaxIdCollection(TypedDict):
        enabled: bool
        """
        Set to `true` to enable tax ID collection.
        """

    class CreateParamsSubscriptionData(TypedDict):
        description: NotRequired["str"]
        """
        The subscription's description, meant to be displayable to the customer. Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs.
        """
        metadata: NotRequired["Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that will declaratively set metadata on [Subscriptions](https://stripe.com/docs/api/subscriptions) generated from this payment link. Unlike object-level metadata, this field is declarative. Updates will clear prior values.
        """
        trial_period_days: NotRequired["int"]
        """
        Integer representing the number of trial period days before the customer is charged for the first time. Has to be at least 1.
        """

    class CreateParamsShippingOption(TypedDict):
        shipping_rate: NotRequired["str"]
        """
        The ID of the Shipping Rate to use for this shipping option.
        """

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
        """
        An array of two-letter ISO country codes representing which countries Checkout should provide as options for
        shipping locations. Unsupported country codes: `AS, CX, CC, CU, HM, IR, KP, MH, FM, NF, MP, PW, SD, SY, UM, VI`.
        """

    class CreateParamsPhoneNumberCollection(TypedDict):
        enabled: bool
        """
        Set to `true` to enable phone number collection.
        """

    class CreateParamsPaymentIntentData(TypedDict):
        capture_method: NotRequired[
            "Literal['automatic', 'automatic_async', 'manual']"
        ]
        """
        Controls when the funds will be captured from the customer's account.
        """
        description: NotRequired["str"]
        """
        An arbitrary string attached to the object. Often useful for displaying to users.
        """
        metadata: NotRequired["Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that will declaratively set metadata on [Payment Intents](https://stripe.com/docs/api/payment_intents) generated from this payment link. Unlike object-level metadata, this field is declarative. Updates will clear prior values.
        """
        setup_future_usage: NotRequired["Literal['off_session', 'on_session']"]
        """
        Indicates that you intend to [make future payments](https://stripe.com/docs/payments/payment-intents#future-usage) with the payment method collected by this Checkout Session.

        When setting this to `on_session`, Checkout will show a notice to the customer that their payment details will be saved.

        When setting this to `off_session`, Checkout will show a notice to the customer that their payment details will be saved and used for future payments.

        If a Customer has been provided or Checkout creates a new Customer,Checkout will attach the payment method to the Customer.

        If Checkout does not create a Customer, the payment method is not attached to a Customer. To reuse the payment method, you can retrieve it from the Checkout Session's PaymentIntent.

        When processing card payments, Checkout also uses `setup_future_usage` to dynamically optimize your payment flow and comply with regional legislation and network rules, such as SCA.
        """
        statement_descriptor: NotRequired["str"]
        """
        Extra information about the payment. This will appear on your customer's statement when this payment succeeds in creating a charge.
        """
        statement_descriptor_suffix: NotRequired["str"]
        """
        Provides information about the charge that customers see on their statements. Concatenated with the prefix (shortened descriptor) or statement descriptor that's set on the account to form the complete statement descriptor. Maximum 22 characters for the concatenated descriptor.
        """

    class CreateParamsLineItem(TypedDict):
        adjustable_quantity: NotRequired[
            "PaymentLink.CreateParamsLineItemAdjustableQuantity"
        ]
        """
        When set, provides configuration for this item's quantity to be adjusted by the customer during checkout.
        """
        price: str
        """
        The ID of the [Price](https://stripe.com/docs/api/prices) or [Plan](https://stripe.com/docs/api/plans) object.
        """
        quantity: int
        """
        The quantity of the line item being purchased.
        """

    class CreateParamsLineItemAdjustableQuantity(TypedDict):
        enabled: bool
        """
        Set to true if the quantity can be adjusted to any non-negative Integer.
        """
        maximum: NotRequired["int"]
        """
        The maximum quantity the customer can purchase. By default this value is 99. You can specify a value up to 999.
        """
        minimum: NotRequired["int"]
        """
        The minimum quantity the customer can purchase. By default this value is 0. If there is only one item in the cart then that item's quantity cannot go down to 0.
        """

    class CreateParamsInvoiceCreation(TypedDict):
        enabled: bool
        """
        Whether the feature is enabled
        """
        invoice_data: NotRequired[
            "PaymentLink.CreateParamsInvoiceCreationInvoiceData"
        ]
        """
        Invoice PDF configuration.
        """

    class CreateParamsInvoiceCreationInvoiceData(TypedDict):
        account_tax_ids: NotRequired["Literal['']|List[str]"]
        """
        The account tax IDs associated with the invoice.
        """
        custom_fields: NotRequired[
            "Literal['']|List[PaymentLink.CreateParamsInvoiceCreationInvoiceDataCustomField]"
        ]
        """
        Default custom fields to be displayed on invoices for this customer.
        """
        description: NotRequired["str"]
        """
        An arbitrary string attached to the object. Often useful for displaying to users.
        """
        footer: NotRequired["str"]
        """
        Default footer to be displayed on invoices for this customer.
        """
        metadata: NotRequired["Literal['']|Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        rendering_options: NotRequired[
            "Literal['']|PaymentLink.CreateParamsInvoiceCreationInvoiceDataRenderingOptions"
        ]
        """
        Default options for invoice PDF rendering for this customer.
        """

    class CreateParamsInvoiceCreationInvoiceDataRenderingOptions(TypedDict):
        amount_tax_display: NotRequired[
            "Literal['']|Literal['exclude_tax', 'include_inclusive_tax']"
        ]
        """
        How line-item prices and amounts will be displayed with respect to tax on invoice PDFs. One of `exclude_tax` or `include_inclusive_tax`. `include_inclusive_tax` will include inclusive tax (and exclude exclusive tax) in invoice PDF amounts. `exclude_tax` will exclude all tax (inclusive and exclusive alike) from invoice PDF amounts.
        """

    class CreateParamsInvoiceCreationInvoiceDataCustomField(TypedDict):
        name: str
        """
        The name of the custom field. This may be up to 30 characters.
        """
        value: str
        """
        The value of the custom field. This may be up to 30 characters.
        """

    class CreateParamsCustomText(TypedDict):
        shipping_address: NotRequired[
            "Literal['']|PaymentLink.CreateParamsCustomTextShippingAddress"
        ]
        """
        Custom text that should be displayed alongside shipping address collection.
        """
        submit: NotRequired[
            "Literal['']|PaymentLink.CreateParamsCustomTextSubmit"
        ]
        """
        Custom text that should be displayed alongside the payment confirmation button.
        """
        terms_of_service_acceptance: NotRequired[
            "Literal['']|PaymentLink.CreateParamsCustomTextTermsOfServiceAcceptance"
        ]
        """
        Custom text that should be displayed in place of the default terms of service agreement text.
        """

    class CreateParamsCustomTextTermsOfServiceAcceptance(TypedDict):
        message: str
        """
        Text may be up to 1200 characters in length.
        """

    class CreateParamsCustomTextSubmit(TypedDict):
        message: str
        """
        Text may be up to 1200 characters in length.
        """

    class CreateParamsCustomTextShippingAddress(TypedDict):
        message: str
        """
        Text may be up to 1200 characters in length.
        """

    class CreateParamsCustomField(TypedDict):
        dropdown: NotRequired["PaymentLink.CreateParamsCustomFieldDropdown"]
        """
        Configuration for `type=dropdown` fields.
        """
        key: str
        """
        String of your choice that your integration can use to reconcile this field. Must be unique to this field, alphanumeric, and up to 200 characters.
        """
        label: "PaymentLink.CreateParamsCustomFieldLabel"
        """
        The label for the field, displayed to the customer.
        """
        numeric: NotRequired["PaymentLink.CreateParamsCustomFieldNumeric"]
        """
        Configuration for `type=numeric` fields.
        """
        optional: NotRequired["bool"]
        """
        Whether the customer is required to complete the field before completing the Checkout Session. Defaults to `false`.
        """
        text: NotRequired["PaymentLink.CreateParamsCustomFieldText"]
        """
        Configuration for `type=text` fields.
        """
        type: Literal["dropdown", "numeric", "text"]
        """
        The type of the field.
        """

    class CreateParamsCustomFieldText(TypedDict):
        maximum_length: NotRequired["int"]
        """
        The maximum character length constraint for the customer's input.
        """
        minimum_length: NotRequired["int"]
        """
        The minimum character length requirement for the customer's input.
        """

    class CreateParamsCustomFieldNumeric(TypedDict):
        maximum_length: NotRequired["int"]
        """
        The maximum character length constraint for the customer's input.
        """
        minimum_length: NotRequired["int"]
        """
        The minimum character length requirement for the customer's input.
        """

    class CreateParamsCustomFieldLabel(TypedDict):
        custom: str
        """
        Custom text for the label, displayed to the customer. Up to 50 characters.
        """
        type: Literal["custom"]
        """
        The type of the label.
        """

    class CreateParamsCustomFieldDropdown(TypedDict):
        options: List["PaymentLink.CreateParamsCustomFieldDropdownOption"]
        """
        The options available for the customer to select. Up to 200 options allowed.
        """

    class CreateParamsCustomFieldDropdownOption(TypedDict):
        label: str
        """
        The label for the option, displayed to the customer. Up to 100 characters.
        """
        value: str
        """
        The value for this option, not displayed to the customer, used by your integration to reconcile the option selected by the customer. Must be unique to this option, alphanumeric, and up to 100 characters.
        """

    class CreateParamsConsentCollection(TypedDict):
        promotions: NotRequired["Literal['auto', 'none']"]
        """
        If set to `auto`, enables the collection of customer consent for promotional communications. The Checkout
        Session will determine whether to display an option to opt into promotional communication
        from the merchant depending on the customer's locale. Only available to US merchants.
        """
        terms_of_service: NotRequired["Literal['none', 'required']"]
        """
        If set to `required`, it requires customers to check a terms of service checkbox before being able to pay.
        There must be a valid terms of service URL set in your [Dashboard settings](https://dashboard.stripe.com/settings/public).
        """

    class CreateParamsAutomaticTax(TypedDict):
        enabled: bool
        """
        If `true`, tax will be calculated automatically using the customer's location.
        """

    class CreateParamsAfterCompletion(TypedDict):
        hosted_confirmation: NotRequired[
            "PaymentLink.CreateParamsAfterCompletionHostedConfirmation"
        ]
        """
        Configuration when `type=hosted_confirmation`.
        """
        redirect: NotRequired[
            "PaymentLink.CreateParamsAfterCompletionRedirect"
        ]
        """
        Configuration when `type=redirect`.
        """
        type: Literal["hosted_confirmation", "redirect"]
        """
        The specified behavior after the purchase is complete. Either `redirect` or `hosted_confirmation`.
        """

    class CreateParamsAfterCompletionRedirect(TypedDict):
        url: str
        """
        The URL the customer will be redirected to after the purchase is complete. You can embed `{CHECKOUT_SESSION_ID}` into the URL to have the `id` of the completed [checkout session](https://stripe.com/docs/api/checkout/sessions/object#checkout_session_object-id) included.
        """

    class CreateParamsAfterCompletionHostedConfirmation(TypedDict):
        custom_message: NotRequired["str"]
        """
        A custom message to display to the customer after the purchase is complete.
        """

    class ListParams(RequestOptions):
        active: NotRequired["bool"]
        """
        Only return payment links that are active or inactive (e.g., pass `false` to list all inactive payment links).
        """
        ending_before: NotRequired["str"]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        limit: NotRequired["int"]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        starting_after: NotRequired["str"]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """

    class ListLineItemsParams(RequestOptions):
        ending_before: NotRequired["str"]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        limit: NotRequired["int"]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        starting_after: NotRequired["str"]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """

    class ModifyParams(RequestOptions):
        active: NotRequired["bool"]
        """
        Whether the payment link's `url` is active. If `false`, customers visiting the URL will be shown a page saying that the link has been deactivated.
        """
        after_completion: NotRequired[
            "PaymentLink.ModifyParamsAfterCompletion"
        ]
        """
        Behavior after the purchase is complete.
        """
        allow_promotion_codes: NotRequired["bool"]
        """
        Enables user redeemable promotion codes.
        """
        automatic_tax: NotRequired["PaymentLink.ModifyParamsAutomaticTax"]
        """
        Configuration for automatic tax collection.
        """
        billing_address_collection: NotRequired["Literal['auto', 'required']"]
        """
        Configuration for collecting the customer's billing address.
        """
        custom_fields: NotRequired[
            "Literal['']|List[PaymentLink.ModifyParamsCustomField]"
        ]
        """
        Collect additional information from your customer using custom fields. Up to 2 fields are supported.
        """
        custom_text: NotRequired["PaymentLink.ModifyParamsCustomText"]
        """
        Display additional text for your customers using custom text.
        """
        customer_creation: NotRequired["Literal['always', 'if_required']"]
        """
        Configures whether [checkout sessions](https://stripe.com/docs/api/checkout/sessions) created by this payment link create a [Customer](https://stripe.com/docs/api/customers).
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        invoice_creation: NotRequired[
            "PaymentLink.ModifyParamsInvoiceCreation"
        ]
        """
        Generate a post-purchase Invoice for one-time payments.
        """
        line_items: NotRequired["List[PaymentLink.ModifyParamsLineItem]"]
        """
        The line items representing what is being sold. Each line item represents an item being sold. Up to 20 line items are supported.
        """
        metadata: NotRequired["Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`. Metadata associated with this Payment Link will automatically be copied to [checkout sessions](https://stripe.com/docs/api/checkout/sessions) created by this payment link.
        """
        payment_intent_data: NotRequired[
            "PaymentLink.ModifyParamsPaymentIntentData"
        ]
        """
        A subset of parameters to be passed to PaymentIntent creation for Checkout Sessions in `payment` mode.
        """
        payment_method_collection: NotRequired[
            "Literal['always', 'if_required']"
        ]
        """
        Specify whether Checkout should collect a payment method. When set to `if_required`, Checkout will not collect a payment method when the total due for the session is 0.This may occur if the Checkout Session includes a free trial or a discount.

        Can only be set in `subscription` mode.

        If you'd like information on how to collect a payment method outside of Checkout, read the guide on [configuring subscriptions with a free trial](https://stripe.com/docs/payments/checkout/free-trials).
        """
        payment_method_types: NotRequired[
            "Literal['']|List[Literal['affirm', 'afterpay_clearpay', 'alipay', 'au_becs_debit', 'bacs_debit', 'bancontact', 'blik', 'boleto', 'card', 'cashapp', 'eps', 'fpx', 'giropay', 'grabpay', 'ideal', 'klarna', 'konbini', 'link', 'oxxo', 'p24', 'paynow', 'paypal', 'pix', 'promptpay', 'sepa_debit', 'sofort', 'us_bank_account', 'wechat_pay']]"
        ]
        """
        The list of payment method types that customers can use. Pass an empty string to enable dynamic payment methods that use your [payment method settings](https://dashboard.stripe.com/settings/payment_methods).
        """
        shipping_address_collection: NotRequired[
            "Literal['']|PaymentLink.ModifyParamsShippingAddressCollection"
        ]
        """
        Configuration for collecting the customer's shipping address.
        """
        subscription_data: NotRequired[
            "PaymentLink.ModifyParamsSubscriptionData"
        ]
        """
        When creating a subscription, the specified configuration data will be used. There must be at least one line item with a recurring price to use `subscription_data`.
        """

    class ModifyParamsSubscriptionData(TypedDict):
        metadata: NotRequired["Literal['']|Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that will declaratively set metadata on [Subscriptions](https://stripe.com/docs/api/subscriptions) generated from this payment link. Unlike object-level metadata, this field is declarative. Updates will clear prior values.
        """

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
        """
        An array of two-letter ISO country codes representing which countries Checkout should provide as options for
        shipping locations. Unsupported country codes: `AS, CX, CC, CU, HM, IR, KP, MH, FM, NF, MP, PW, SD, SY, UM, VI`.
        """

    class ModifyParamsPaymentIntentData(TypedDict):
        description: NotRequired["Literal['']|str"]
        """
        An arbitrary string attached to the object. Often useful for displaying to users.
        """
        metadata: NotRequired["Literal['']|Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that will declaratively set metadata on [Payment Intents](https://stripe.com/docs/api/payment_intents) generated from this payment link. Unlike object-level metadata, this field is declarative. Updates will clear prior values.
        """
        statement_descriptor: NotRequired["Literal['']|str"]
        """
        Extra information about the payment. This will appear on your customer's statement when this payment succeeds in creating a charge.
        """
        statement_descriptor_suffix: NotRequired["Literal['']|str"]
        """
        Provides information about the charge that customers see on their statements. Concatenated with the prefix (shortened descriptor) or statement descriptor that's set on the account to form the complete statement descriptor. Maximum 22 characters for the concatenated descriptor.
        """

    class ModifyParamsLineItem(TypedDict):
        adjustable_quantity: NotRequired[
            "PaymentLink.ModifyParamsLineItemAdjustableQuantity"
        ]
        """
        When set, provides configuration for this item's quantity to be adjusted by the customer during checkout.
        """
        id: str
        """
        The ID of an existing line item on the payment link.
        """
        quantity: NotRequired["int"]
        """
        The quantity of the line item being purchased.
        """

    class ModifyParamsLineItemAdjustableQuantity(TypedDict):
        enabled: bool
        """
        Set to true if the quantity can be adjusted to any non-negative Integer.
        """
        maximum: NotRequired["int"]
        """
        The maximum quantity the customer can purchase. By default this value is 99. You can specify a value up to 999.
        """
        minimum: NotRequired["int"]
        """
        The minimum quantity the customer can purchase. By default this value is 0. If there is only one item in the cart then that item's quantity cannot go down to 0.
        """

    class ModifyParamsInvoiceCreation(TypedDict):
        enabled: bool
        """
        Whether the feature is enabled
        """
        invoice_data: NotRequired[
            "PaymentLink.ModifyParamsInvoiceCreationInvoiceData"
        ]
        """
        Invoice PDF configuration.
        """

    class ModifyParamsInvoiceCreationInvoiceData(TypedDict):
        account_tax_ids: NotRequired["Literal['']|List[str]"]
        """
        The account tax IDs associated with the invoice.
        """
        custom_fields: NotRequired[
            "Literal['']|List[PaymentLink.ModifyParamsInvoiceCreationInvoiceDataCustomField]"
        ]
        """
        Default custom fields to be displayed on invoices for this customer.
        """
        description: NotRequired["str"]
        """
        An arbitrary string attached to the object. Often useful for displaying to users.
        """
        footer: NotRequired["str"]
        """
        Default footer to be displayed on invoices for this customer.
        """
        metadata: NotRequired["Literal['']|Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """
        rendering_options: NotRequired[
            "Literal['']|PaymentLink.ModifyParamsInvoiceCreationInvoiceDataRenderingOptions"
        ]
        """
        Default options for invoice PDF rendering for this customer.
        """

    class ModifyParamsInvoiceCreationInvoiceDataRenderingOptions(TypedDict):
        amount_tax_display: NotRequired[
            "Literal['']|Literal['exclude_tax', 'include_inclusive_tax']"
        ]
        """
        How line-item prices and amounts will be displayed with respect to tax on invoice PDFs. One of `exclude_tax` or `include_inclusive_tax`. `include_inclusive_tax` will include inclusive tax (and exclude exclusive tax) in invoice PDF amounts. `exclude_tax` will exclude all tax (inclusive and exclusive alike) from invoice PDF amounts.
        """

    class ModifyParamsInvoiceCreationInvoiceDataCustomField(TypedDict):
        name: str
        """
        The name of the custom field. This may be up to 30 characters.
        """
        value: str
        """
        The value of the custom field. This may be up to 30 characters.
        """

    class ModifyParamsCustomText(TypedDict):
        shipping_address: NotRequired[
            "Literal['']|PaymentLink.ModifyParamsCustomTextShippingAddress"
        ]
        """
        Custom text that should be displayed alongside shipping address collection.
        """
        submit: NotRequired[
            "Literal['']|PaymentLink.ModifyParamsCustomTextSubmit"
        ]
        """
        Custom text that should be displayed alongside the payment confirmation button.
        """
        terms_of_service_acceptance: NotRequired[
            "Literal['']|PaymentLink.ModifyParamsCustomTextTermsOfServiceAcceptance"
        ]
        """
        Custom text that should be displayed in place of the default terms of service agreement text.
        """

    class ModifyParamsCustomTextTermsOfServiceAcceptance(TypedDict):
        message: str
        """
        Text may be up to 1200 characters in length.
        """

    class ModifyParamsCustomTextSubmit(TypedDict):
        message: str
        """
        Text may be up to 1200 characters in length.
        """

    class ModifyParamsCustomTextShippingAddress(TypedDict):
        message: str
        """
        Text may be up to 1200 characters in length.
        """

    class ModifyParamsCustomField(TypedDict):
        dropdown: NotRequired["PaymentLink.ModifyParamsCustomFieldDropdown"]
        """
        Configuration for `type=dropdown` fields.
        """
        key: str
        """
        String of your choice that your integration can use to reconcile this field. Must be unique to this field, alphanumeric, and up to 200 characters.
        """
        label: "PaymentLink.ModifyParamsCustomFieldLabel"
        """
        The label for the field, displayed to the customer.
        """
        numeric: NotRequired["PaymentLink.ModifyParamsCustomFieldNumeric"]
        """
        Configuration for `type=numeric` fields.
        """
        optional: NotRequired["bool"]
        """
        Whether the customer is required to complete the field before completing the Checkout Session. Defaults to `false`.
        """
        text: NotRequired["PaymentLink.ModifyParamsCustomFieldText"]
        """
        Configuration for `type=text` fields.
        """
        type: Literal["dropdown", "numeric", "text"]
        """
        The type of the field.
        """

    class ModifyParamsCustomFieldText(TypedDict):
        maximum_length: NotRequired["int"]
        """
        The maximum character length constraint for the customer's input.
        """
        minimum_length: NotRequired["int"]
        """
        The minimum character length requirement for the customer's input.
        """

    class ModifyParamsCustomFieldNumeric(TypedDict):
        maximum_length: NotRequired["int"]
        """
        The maximum character length constraint for the customer's input.
        """
        minimum_length: NotRequired["int"]
        """
        The minimum character length requirement for the customer's input.
        """

    class ModifyParamsCustomFieldLabel(TypedDict):
        custom: str
        """
        Custom text for the label, displayed to the customer. Up to 50 characters.
        """
        type: Literal["custom"]
        """
        The type of the label.
        """

    class ModifyParamsCustomFieldDropdown(TypedDict):
        options: List["PaymentLink.ModifyParamsCustomFieldDropdownOption"]
        """
        The options available for the customer to select. Up to 200 options allowed.
        """

    class ModifyParamsCustomFieldDropdownOption(TypedDict):
        label: str
        """
        The label for the option, displayed to the customer. Up to 100 characters.
        """
        value: str
        """
        The value for this option, not displayed to the customer, used by your integration to reconcile the option selected by the customer. Must be unique to this option, alphanumeric, and up to 100 characters.
        """

    class ModifyParamsAutomaticTax(TypedDict):
        enabled: bool
        """
        If `true`, tax will be calculated automatically using the customer's location.
        """

    class ModifyParamsAfterCompletion(TypedDict):
        hosted_confirmation: NotRequired[
            "PaymentLink.ModifyParamsAfterCompletionHostedConfirmation"
        ]
        """
        Configuration when `type=hosted_confirmation`.
        """
        redirect: NotRequired[
            "PaymentLink.ModifyParamsAfterCompletionRedirect"
        ]
        """
        Configuration when `type=redirect`.
        """
        type: Literal["hosted_confirmation", "redirect"]
        """
        The specified behavior after the purchase is complete. Either `redirect` or `hosted_confirmation`.
        """

    class ModifyParamsAfterCompletionRedirect(TypedDict):
        url: str
        """
        The URL the customer will be redirected to after the purchase is complete. You can embed `{CHECKOUT_SESSION_ID}` into the URL to have the `id` of the completed [checkout session](https://stripe.com/docs/api/checkout/sessions/object#checkout_session_object-id) included.
        """

    class ModifyParamsAfterCompletionHostedConfirmation(TypedDict):
        custom_message: NotRequired["str"]
        """
        A custom message to display to the customer after the purchase is complete.
        """

    class RetrieveParams(RequestOptions):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    active: bool
    """
    Whether the payment link's `url` is active. If `false`, customers visiting the URL will be shown a page saying that the link has been deactivated.
    """
    after_completion: AfterCompletion
    allow_promotion_codes: bool
    """
    Whether user redeemable promotion codes are enabled.
    """
    application: Optional[ExpandableField["Application"]]
    """
    The ID of the Connect application that created the Payment Link.
    """
    application_fee_amount: Optional[int]
    """
    The amount of the application fee (if any) that will be requested to be applied to the payment and transferred to the application owner's Stripe account.
    """
    application_fee_percent: Optional[float]
    """
    This represents the percentage of the subscription invoice total that will be transferred to the application owner's Stripe account.
    """
    automatic_tax: AutomaticTax
    billing_address_collection: Literal["auto", "required"]
    """
    Configuration for collecting the customer's billing address.
    """
    consent_collection: Optional[ConsentCollection]
    """
    When set, provides configuration to gather active consent from customers.
    """
    currency: str
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    custom_fields: List[CustomField]
    """
    Collect additional information from your customer using custom fields. Up to 2 fields are supported.
    """
    custom_text: CustomText
    customer_creation: Literal["always", "if_required"]
    """
    Configuration for Customer creation during checkout.
    """
    id: str
    """
    Unique identifier for the object.
    """
    invoice_creation: Optional[InvoiceCreation]
    """
    Configuration for creating invoice for payment mode payment links.
    """
    line_items: Optional[ListObject["LineItem"]]
    """
    The line items representing what is being sold.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    metadata: Dict[str, str]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    object: Literal["payment_link"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    on_behalf_of: Optional[ExpandableField["Account"]]
    """
    The account on behalf of which to charge. See the [Connect documentation](https://support.stripe.com/questions/sending-invoices-on-behalf-of-connected-accounts) for details.
    """
    payment_intent_data: Optional[PaymentIntentData]
    """
    Indicates the parameters to be passed to PaymentIntent creation during checkout.
    """
    payment_method_collection: Literal["always", "if_required"]
    """
    Configuration for collecting a payment method during checkout.
    """
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
    """
    The list of payment method types that customers can use. When `null`, Stripe will dynamically show relevant payment methods you've enabled in your [payment method settings](https://dashboard.stripe.com/settings/payment_methods).
    """
    phone_number_collection: PhoneNumberCollection
    shipping_address_collection: Optional[ShippingAddressCollection]
    """
    Configuration for collecting the customer's shipping address.
    """
    shipping_options: List[ShippingOption]
    """
    The shipping rate options applied to the session.
    """
    submit_type: Literal["auto", "book", "donate", "pay"]
    """
    Indicates the type of transaction being performed which customizes relevant text on the page, such as the submit button.
    """
    subscription_data: Optional[SubscriptionData]
    """
    When creating a subscription, the specified configuration data will be used. There must be at least one line item with a recurring price to use `subscription_data`.
    """
    tax_id_collection: TaxIdCollection
    transfer_data: Optional[TransferData]
    """
    The account (if any) the payments will be attributed to for tax reporting, and where funds from each payment will be transferred to.
    """
    url: str
    """
    The public URL that can be shared with customers.
    """

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack[
            "PaymentLink.CreateParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> "PaymentLink":
        """
        Creates a payment link.
        """
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
        **params: Unpack[
            "PaymentLink.ListParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> ListObject["PaymentLink"]:
        """
        Returns a list of your payment links.
        """
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
        **params: Unpack[
            "PaymentLink.ListLineItemsParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> ListObject["LineItem"]:
        """
        When retrieving a payment link, there is an includable line_items property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.
        """
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

    @overload
    @staticmethod
    def list_line_items(
        payment_link: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack[
            "PaymentLink.ListLineItemsParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> ListObject["LineItem"]:
        """
        When retrieving a payment link, there is an includable line_items property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.
        """
        ...

    @overload
    def list_line_items(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack[
            "PaymentLink.ListLineItemsParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> ListObject["LineItem"]:
        """
        When retrieving a payment link, there is an includable line_items property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.
        """
        ...

    @class_method_variant("_cls_list_line_items")
    def list_line_items(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack[
            "PaymentLink.ListLineItemsParams"
        ]  # pyright: ignore[reportGeneralTypeIssues]
    ) -> ListObject["LineItem"]:
        """
        When retrieving a payment link, there is an includable line_items property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of line items.
        """
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
        """
        Updates a payment link.
        """
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "PaymentLink",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["PaymentLink.RetrieveParams"]
    ) -> "PaymentLink":
        """
        Retrieve a payment link.
        """
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
