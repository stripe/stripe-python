# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import Dict, List, Optional, Union, cast
from typing_extensions import Literal, NotRequired, TypedDict, Unpack

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.customer import Customer
    from stripe.api_resources.invoice import Invoice
    from stripe.api_resources.line_item import LineItem
    from stripe.api_resources.payment_intent import PaymentIntent
    from stripe.api_resources.payment_link import PaymentLink
    from stripe.api_resources.setup_intent import SetupIntent
    from stripe.api_resources.subscription import Subscription


class Session(
    CreateableAPIResource["Session"], ListableAPIResource["Session"]
):
    """
    A Checkout Session represents your customer's session as they pay for
    one-time purchases or subscriptions through [Checkout](https://stripe.com/docs/payments/checkout)
    or [Payment Links](https://stripe.com/docs/payments/payment-links). We recommend creating a
    new Session each time your customer attempts to pay.

    Once payment is successful, the Checkout Session will contain a reference
    to the [Customer](https://stripe.com/docs/api/customers), and either the successful
    [PaymentIntent](https://stripe.com/docs/api/payment_intents) or an active
    [Subscription](https://stripe.com/docs/api/subscriptions).

    You can create a Checkout Session on your server and redirect to its URL
    to begin Checkout.

    Related guide: [Checkout quickstart](https://stripe.com/docs/checkout/quickstart)
    """

    OBJECT_NAME = "checkout.session"

    class CreateParams(RequestOptions):
        after_expiration: NotRequired[
            Optional["Session.CreateAfterExpirationParams"]
        ]
        allow_promotion_codes: NotRequired[Optional[bool]]
        automatic_tax: NotRequired[
            Optional["Session.CreateAutomaticTaxParams"]
        ]
        billing_address_collection: NotRequired[
            Optional[Literal["auto", "required"]]
        ]
        cancel_url: NotRequired[Optional[str]]
        client_reference_id: NotRequired[Optional[str]]
        consent_collection: NotRequired[
            Optional["Session.CreateConsentCollectionParams"]
        ]
        currency: NotRequired[Optional[str]]
        custom_fields: NotRequired[
            Optional[
                List[
                    "Session.CreateInvoiceCreationInvoiceDataCustomFieldParams"
                ]
            ]
        ]
        custom_text: NotRequired[Optional["Session.CreateCustomTextParams"]]
        customer: NotRequired[Optional[str]]
        customer_creation: NotRequired[
            Optional[Literal["always", "if_required"]]
        ]
        customer_email: NotRequired[Optional[str]]
        customer_update: NotRequired[
            Optional["Session.CreateCustomerUpdateParams"]
        ]
        discounts: NotRequired[Optional[List["Session.CreateDiscountParams"]]]
        expand: NotRequired[Optional[List[str]]]
        expires_at: NotRequired[Optional[int]]
        invoice_creation: NotRequired[
            Optional["Session.CreateInvoiceCreationParams"]
        ]
        line_items: NotRequired[Optional[List["Session.CreateLineItemParams"]]]
        locale: NotRequired[
            Optional[
                Literal[
                    "auto",
                    "bg",
                    "cs",
                    "da",
                    "de",
                    "el",
                    "en",
                    "en-GB",
                    "es",
                    "es-419",
                    "et",
                    "fi",
                    "fil",
                    "fr",
                    "fr-CA",
                    "hr",
                    "hu",
                    "id",
                    "it",
                    "ja",
                    "ko",
                    "lt",
                    "lv",
                    "ms",
                    "mt",
                    "nb",
                    "nl",
                    "pl",
                    "pt",
                    "pt-BR",
                    "ro",
                    "ru",
                    "sk",
                    "sl",
                    "sv",
                    "th",
                    "tr",
                    "vi",
                    "zh",
                    "zh-HK",
                    "zh-TW",
                ]
            ]
        ]
        metadata: NotRequired[Optional[Dict[str, str]]]
        mode: NotRequired[
            Optional[Literal["payment", "setup", "subscription"]]
        ]
        payment_intent_data: NotRequired[
            Optional["Session.CreatePaymentIntentDataParams"]
        ]
        payment_method_collection: NotRequired[
            Optional[Literal["always", "if_required"]]
        ]
        payment_method_configuration: NotRequired[Optional[str]]
        payment_method_options: NotRequired[
            Optional["Session.CreatePaymentMethodOptionsParams"]
        ]
        payment_method_types: NotRequired[
            Optional[
                List[
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
        ]
        phone_number_collection: NotRequired[
            Optional["Session.CreatePhoneNumberCollectionParams"]
        ]
        setup_intent_data: NotRequired[
            Optional["Session.CreateSetupIntentDataParams"]
        ]
        shipping_address_collection: NotRequired[
            Optional["Session.CreateShippingAddressCollectionParams"]
        ]
        shipping_options: NotRequired[
            Optional[List["Session.CreateShippingOptionParams"]]
        ]
        submit_type: NotRequired[
            Optional[Literal["auto", "book", "donate", "pay"]]
        ]
        subscription_data: NotRequired[
            Optional["Session.CreateSubscriptionDataParams"]
        ]
        success_url: str
        tax_id_collection: NotRequired[
            Optional["Session.CreateTaxIdCollectionParams"]
        ]

    class CreateTaxIdCollectionParams(TypedDict):
        enabled: bool

    class CreateSubscriptionDataParams(TypedDict):
        application_fee_percent: NotRequired[Optional[float]]
        billing_cycle_anchor: NotRequired[Optional[int]]
        default_tax_rates: NotRequired[Optional[List[str]]]
        description: NotRequired[Optional[str]]
        metadata: NotRequired[Optional[Dict[str, str]]]
        on_behalf_of: NotRequired[Optional[str]]
        proration_behavior: NotRequired[
            Optional[Literal["create_prorations", "none"]]
        ]
        transfer_data: NotRequired[
            Optional["Session.CreateSubscriptionDataTransferDataParams"]
        ]
        trial_end: NotRequired[Optional[int]]
        trial_period_days: NotRequired[Optional[int]]
        trial_settings: NotRequired[
            Optional["Session.CreateSubscriptionDataTrialSettingsParams"]
        ]

    class CreateSubscriptionDataTrialSettingsParams(TypedDict):
        end_behavior: "Session.CreateSubscriptionDataTrialSettingsEndBehaviorParams"

    class CreateSubscriptionDataTrialSettingsEndBehaviorParams(TypedDict):
        missing_payment_method: Literal["cancel", "create_invoice", "pause"]

    class CreateSubscriptionDataTransferDataParams(TypedDict):
        amount_percent: NotRequired[Optional[float]]
        destination: str

    class CreateShippingOptionParams(TypedDict):
        shipping_rate: NotRequired[Optional[str]]
        shipping_rate_data: NotRequired[
            Optional["Session.CreateShippingOptionShippingRateDataParams"]
        ]

    class CreateShippingOptionShippingRateDataParams(TypedDict):
        delivery_estimate: NotRequired[
            Optional[
                "Session.CreateShippingOptionShippingRateDataDeliveryEstimateParams"
            ]
        ]
        display_name: str
        fixed_amount: NotRequired[
            Optional[
                "Session.CreateShippingOptionShippingRateDataFixedAmountParams"
            ]
        ]
        metadata: NotRequired[Optional[Dict[str, str]]]
        tax_behavior: NotRequired[
            Optional[Literal["exclusive", "inclusive", "unspecified"]]
        ]
        tax_code: NotRequired[Optional[str]]
        type: NotRequired[Optional[Literal["fixed_amount"]]]

    class CreateShippingOptionShippingRateDataFixedAmountParams(TypedDict):
        amount: int
        currency: str
        currency_options: NotRequired[
            Optional[
                Dict[
                    str,
                    "Session.CreateShippingOptionShippingRateDataFixedAmountCurrencyOptionsParams",
                ]
            ]
        ]

    class CreateShippingOptionShippingRateDataFixedAmountCurrencyOptionsParams(
        TypedDict,
    ):
        amount: int
        tax_behavior: NotRequired[
            Optional[Literal["exclusive", "inclusive", "unspecified"]]
        ]

    class CreateShippingOptionShippingRateDataDeliveryEstimateParams(
        TypedDict
    ):
        maximum: NotRequired[
            Optional[
                "Session.CreateShippingOptionShippingRateDataDeliveryEstimateMaximumParams"
            ]
        ]
        minimum: NotRequired[
            Optional[
                "Session.CreateShippingOptionShippingRateDataDeliveryEstimateMinimumParams"
            ]
        ]

    class CreateShippingOptionShippingRateDataDeliveryEstimateMinimumParams(
        TypedDict,
    ):
        unit: Literal["business_day", "day", "hour", "month", "week"]
        value: int

    class CreateShippingOptionShippingRateDataDeliveryEstimateMaximumParams(
        TypedDict,
    ):
        unit: Literal["business_day", "day", "hour", "month", "week"]
        value: int

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

    class CreateSetupIntentDataParams(TypedDict):
        description: NotRequired[Optional[str]]
        metadata: NotRequired[Optional[Dict[str, str]]]
        on_behalf_of: NotRequired[Optional[str]]

    class CreatePhoneNumberCollectionParams(TypedDict):
        enabled: bool

    class CreatePaymentMethodOptionsParams(TypedDict):
        acss_debit: NotRequired[
            Optional["Session.CreatePaymentMethodOptionsAcssDebitParams"]
        ]
        affirm: NotRequired[
            Optional["Session.CreatePaymentMethodOptionsAffirmParams"]
        ]
        afterpay_clearpay: NotRequired[
            Optional[
                "Session.CreatePaymentMethodOptionsAfterpayClearpayParams"
            ]
        ]
        alipay: NotRequired[
            Optional["Session.CreatePaymentMethodOptionsAlipayParams"]
        ]
        au_becs_debit: NotRequired[
            Optional["Session.CreatePaymentMethodOptionsAuBecsDebitParams"]
        ]
        bacs_debit: NotRequired[
            Optional["Session.CreatePaymentMethodOptionsBacsDebitParams"]
        ]
        bancontact: NotRequired[
            Optional["Session.CreatePaymentMethodOptionsBancontactParams"]
        ]
        boleto: NotRequired[
            Optional["Session.CreatePaymentMethodOptionsBoletoParams"]
        ]
        card: NotRequired[
            Optional["Session.CreatePaymentMethodOptionsCardParams"]
        ]
        cashapp: NotRequired[
            Optional["Session.CreatePaymentMethodOptionsCashappParams"]
        ]
        customer_balance: NotRequired[
            Optional["Session.CreatePaymentMethodOptionsCustomerBalanceParams"]
        ]
        eps: NotRequired[
            Optional["Session.CreatePaymentMethodOptionsEpsParams"]
        ]
        fpx: NotRequired[
            Optional["Session.CreatePaymentMethodOptionsFpxParams"]
        ]
        giropay: NotRequired[
            Optional["Session.CreatePaymentMethodOptionsGiropayParams"]
        ]
        grabpay: NotRequired[
            Optional["Session.CreatePaymentMethodOptionsGrabpayParams"]
        ]
        ideal: NotRequired[
            Optional["Session.CreatePaymentMethodOptionsIdealParams"]
        ]
        klarna: NotRequired[
            Optional["Session.CreatePaymentMethodOptionsKlarnaParams"]
        ]
        konbini: NotRequired[
            Optional["Session.CreatePaymentMethodOptionsKonbiniParams"]
        ]
        link: NotRequired[
            Optional["Session.CreatePaymentMethodOptionsLinkParams"]
        ]
        oxxo: NotRequired[
            Optional["Session.CreatePaymentMethodOptionsOxxoParams"]
        ]
        p24: NotRequired[
            Optional["Session.CreatePaymentMethodOptionsP24Params"]
        ]
        paynow: NotRequired[
            Optional["Session.CreatePaymentMethodOptionsPaynowParams"]
        ]
        paypal: NotRequired[
            Optional["Session.CreatePaymentMethodOptionsPaypalParams"]
        ]
        pix: NotRequired[
            Optional["Session.CreatePaymentMethodOptionsPixParams"]
        ]
        sepa_debit: NotRequired[
            Optional["Session.CreatePaymentMethodOptionsSepaDebitParams"]
        ]
        sofort: NotRequired[
            Optional["Session.CreatePaymentMethodOptionsSofortParams"]
        ]
        us_bank_account: NotRequired[
            Optional["Session.CreatePaymentMethodOptionsUsBankAccountParams"]
        ]
        wechat_pay: NotRequired[
            Optional["Session.CreatePaymentMethodOptionsWechatPayParams"]
        ]

    class CreatePaymentMethodOptionsWechatPayParams(TypedDict):
        app_id: NotRequired[Optional[str]]
        client: Literal["android", "ios", "web"]
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class CreatePaymentMethodOptionsUsBankAccountParams(TypedDict):
        financial_connections: NotRequired[
            Optional[
                "Session.CreatePaymentMethodOptionsUsBankAccountFinancialConnectionsParams"
            ]
        ]
        setup_future_usage: NotRequired[
            Optional[Literal["none", "off_session", "on_session"]]
        ]
        verification_method: NotRequired[
            Optional[Literal["automatic", "instant"]]
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

    class CreatePaymentMethodOptionsSofortParams(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class CreatePaymentMethodOptionsSepaDebitParams(TypedDict):
        setup_future_usage: NotRequired[
            Optional[Literal["none", "off_session", "on_session"]]
        ]

    class CreatePaymentMethodOptionsPixParams(TypedDict):
        expires_after_seconds: NotRequired[Optional[int]]

    class CreatePaymentMethodOptionsPaypalParams(TypedDict):
        capture_method: NotRequired[
            Optional[Union[Literal[""], Literal["manual"]]]
        ]
        preferred_locale: NotRequired[
            Optional[
                Literal[
                    "cs-CZ",
                    "da-DK",
                    "de-AT",
                    "de-DE",
                    "de-LU",
                    "el-GR",
                    "en-GB",
                    "en-US",
                    "es-ES",
                    "fi-FI",
                    "fr-BE",
                    "fr-FR",
                    "fr-LU",
                    "hu-HU",
                    "it-IT",
                    "nl-BE",
                    "nl-NL",
                    "pl-PL",
                    "pt-PT",
                    "sk-SK",
                    "sv-SE",
                ]
            ]
        ]
        reference: NotRequired[Optional[str]]
        risk_correlation_id: NotRequired[Optional[str]]
        setup_future_usage: NotRequired[
            Optional[Union[Literal[""], Literal["none", "off_session"]]]
        ]

    class CreatePaymentMethodOptionsPaynowParams(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class CreatePaymentMethodOptionsP24Params(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]
        tos_shown_and_accepted: NotRequired[Optional[bool]]

    class CreatePaymentMethodOptionsOxxoParams(TypedDict):
        expires_after_days: NotRequired[Optional[int]]
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class CreatePaymentMethodOptionsLinkParams(TypedDict):
        setup_future_usage: NotRequired[
            Optional[Literal["none", "off_session"]]
        ]

    class CreatePaymentMethodOptionsKonbiniParams(TypedDict):
        expires_after_days: NotRequired[Optional[int]]
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class CreatePaymentMethodOptionsKlarnaParams(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class CreatePaymentMethodOptionsIdealParams(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class CreatePaymentMethodOptionsGrabpayParams(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class CreatePaymentMethodOptionsGiropayParams(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class CreatePaymentMethodOptionsFpxParams(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class CreatePaymentMethodOptionsEpsParams(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class CreatePaymentMethodOptionsCustomerBalanceParams(TypedDict):
        bank_transfer: NotRequired[
            Optional[
                "Session.CreatePaymentMethodOptionsCustomerBalanceBankTransferParams"
            ]
        ]
        funding_type: NotRequired[Optional[Literal["bank_transfer"]]]
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class CreatePaymentMethodOptionsCustomerBalanceBankTransferParams(
        TypedDict,
    ):
        eu_bank_transfer: NotRequired[
            Optional[
                "Session.CreatePaymentMethodOptionsCustomerBalanceBankTransferEuBankTransferParams"
            ]
        ]
        requested_address_types: NotRequired[
            Optional[
                List[
                    Literal[
                        "aba",
                        "iban",
                        "sepa",
                        "sort_code",
                        "spei",
                        "swift",
                        "zengin",
                    ]
                ]
            ]
        ]
        type: Literal[
            "eu_bank_transfer",
            "gb_bank_transfer",
            "jp_bank_transfer",
            "mx_bank_transfer",
            "us_bank_transfer",
        ]

    class CreatePaymentMethodOptionsCustomerBalanceBankTransferEuBankTransferParams(
        TypedDict,
    ):
        country: str

    class CreatePaymentMethodOptionsCashappParams(TypedDict):
        setup_future_usage: NotRequired[
            Optional[Literal["none", "off_session", "on_session"]]
        ]

    class CreatePaymentMethodOptionsCardParams(TypedDict):
        installments: NotRequired[
            Optional[
                "Session.CreatePaymentMethodOptionsCardInstallmentsParams"
            ]
        ]
        setup_future_usage: NotRequired[
            Optional[Literal["off_session", "on_session"]]
        ]
        statement_descriptor_suffix_kana: NotRequired[Optional[str]]
        statement_descriptor_suffix_kanji: NotRequired[Optional[str]]

    class CreatePaymentMethodOptionsCardInstallmentsParams(TypedDict):
        enabled: NotRequired[Optional[bool]]

    class CreatePaymentMethodOptionsBoletoParams(TypedDict):
        expires_after_days: NotRequired[Optional[int]]
        setup_future_usage: NotRequired[
            Optional[Literal["none", "off_session", "on_session"]]
        ]

    class CreatePaymentMethodOptionsBancontactParams(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class CreatePaymentMethodOptionsBacsDebitParams(TypedDict):
        setup_future_usage: NotRequired[
            Optional[Literal["none", "off_session", "on_session"]]
        ]

    class CreatePaymentMethodOptionsAuBecsDebitParams(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class CreatePaymentMethodOptionsAlipayParams(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class CreatePaymentMethodOptionsAfterpayClearpayParams(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class CreatePaymentMethodOptionsAffirmParams(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class CreatePaymentMethodOptionsAcssDebitParams(TypedDict):
        currency: NotRequired[Optional[Literal["cad", "usd"]]]
        mandate_options: NotRequired[
            Optional[
                "Session.CreatePaymentMethodOptionsAcssDebitMandateOptionsParams"
            ]
        ]
        setup_future_usage: NotRequired[
            Optional[Literal["none", "off_session", "on_session"]]
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

    class CreatePaymentIntentDataParams(TypedDict):
        application_fee_amount: NotRequired[Optional[int]]
        capture_method: NotRequired[
            Optional[Literal["automatic", "automatic_async", "manual"]]
        ]
        description: NotRequired[Optional[str]]
        metadata: NotRequired[Optional[Dict[str, str]]]
        on_behalf_of: NotRequired[Optional[str]]
        receipt_email: NotRequired[Optional[str]]
        setup_future_usage: NotRequired[
            Optional[Literal["off_session", "on_session"]]
        ]
        shipping: NotRequired[
            Optional["Session.CreatePaymentIntentDataShippingParams"]
        ]
        statement_descriptor: NotRequired[Optional[str]]
        statement_descriptor_suffix: NotRequired[Optional[str]]
        transfer_data: NotRequired[
            Optional["Session.CreatePaymentIntentDataTransferDataParams"]
        ]
        transfer_group: NotRequired[Optional[str]]

    class CreatePaymentIntentDataTransferDataParams(TypedDict):
        amount: NotRequired[Optional[int]]
        destination: str

    class CreatePaymentIntentDataShippingParams(TypedDict):
        address: "Session.CreatePaymentIntentDataShippingAddressParams"
        carrier: NotRequired[Optional[str]]
        name: str
        phone: NotRequired[Optional[str]]
        tracking_number: NotRequired[Optional[str]]

    class CreatePaymentIntentDataShippingAddressParams(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: str
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class CreateLineItemParams(TypedDict):
        adjustable_quantity: NotRequired[
            Optional["Session.CreateLineItemAdjustableQuantityParams"]
        ]
        dynamic_tax_rates: NotRequired[Optional[List[str]]]
        price: NotRequired[Optional[str]]
        price_data: NotRequired[
            Optional["Session.CreateLineItemPriceDataParams"]
        ]
        quantity: NotRequired[Optional[int]]
        tax_rates: NotRequired[Optional[List[str]]]

    class CreateLineItemPriceDataParams(TypedDict):
        currency: str
        product: NotRequired[Optional[str]]
        product_data: NotRequired[
            Optional["Session.CreateLineItemPriceDataProductDataParams"]
        ]
        recurring: NotRequired[
            Optional["Session.CreateLineItemPriceDataRecurringParams"]
        ]
        tax_behavior: NotRequired[
            Optional[Literal["exclusive", "inclusive", "unspecified"]]
        ]
        unit_amount: NotRequired[Optional[int]]
        unit_amount_decimal: NotRequired[Optional[float]]

    class CreateLineItemPriceDataRecurringParams(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        interval_count: NotRequired[Optional[int]]

    class CreateLineItemPriceDataProductDataParams(TypedDict):
        description: NotRequired[Optional[str]]
        images: NotRequired[Optional[List[str]]]
        metadata: NotRequired[Optional[Dict[str, str]]]
        name: str
        tax_code: NotRequired[Optional[str]]

    class CreateLineItemAdjustableQuantityParams(TypedDict):
        enabled: bool
        maximum: NotRequired[Optional[int]]
        minimum: NotRequired[Optional[int]]

    class CreateInvoiceCreationParams(TypedDict):
        enabled: bool
        invoice_data: NotRequired[
            Optional["Session.CreateInvoiceCreationInvoiceDataParams"]
        ]

    class CreateInvoiceCreationInvoiceDataParams(TypedDict):
        account_tax_ids: NotRequired[Optional[Union[Literal[""], List[str]]]]
        custom_fields: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    List[
                        "Session.CreateInvoiceCreationInvoiceDataCustomFieldParams"
                    ],
                ]
            ]
        ]
        description: NotRequired[Optional[str]]
        footer: NotRequired[Optional[str]]
        metadata: NotRequired[Optional[Dict[str, str]]]
        rendering_options: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Session.CreateInvoiceCreationInvoiceDataRenderingOptionsParams",
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

    class CreateDiscountParams(TypedDict):
        coupon: NotRequired[Optional[str]]
        promotion_code: NotRequired[Optional[str]]

    class CreateCustomerUpdateParams(TypedDict):
        address: NotRequired[Optional[Literal["auto", "never"]]]
        name: NotRequired[Optional[Literal["auto", "never"]]]
        shipping: NotRequired[Optional[Literal["auto", "never"]]]

    class CreateCustomTextParams(TypedDict):
        shipping_address: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Session.CreateCustomTextShippingAddressParams",
                ]
            ]
        ]
        submit: NotRequired[
            Optional[
                Union[Literal[""], "Session.CreateCustomTextSubmitParams"]
            ]
        ]
        terms_of_service_acceptance: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "Session.CreateCustomTextTermsOfServiceAcceptanceParams",
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
            Optional["Session.CreateCustomFieldDropdownParams"]
        ]
        key: str
        label: "Session.CreateCustomFieldLabelParams"
        numeric: NotRequired[
            Optional["Session.CreateCustomFieldNumericParams"]
        ]
        optional: NotRequired[Optional[bool]]
        text: NotRequired[Optional["Session.CreateCustomFieldTextParams"]]
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
        options: List["Session.CreateCustomFieldDropdownOptionParams"]

    class CreateCustomFieldDropdownOptionParams(TypedDict):
        label: str
        value: str

    class CreateConsentCollectionParams(TypedDict):
        promotions: NotRequired[Optional[Literal["auto", "none"]]]
        terms_of_service: NotRequired[Optional[Literal["none", "required"]]]

    class CreateAutomaticTaxParams(TypedDict):
        enabled: bool

    class CreateAfterExpirationParams(TypedDict):
        recovery: NotRequired[
            Optional["Session.CreateAfterExpirationRecoveryParams"]
        ]

    class CreateAfterExpirationRecoveryParams(TypedDict):
        allow_promotion_codes: NotRequired[Optional[bool]]
        enabled: bool

    class ExpireParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    class ListParams(RequestOptions):
        customer: NotRequired[Optional[str]]
        customer_details: NotRequired[
            Optional["Session.ListCustomerDetailsParams"]
        ]
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        payment_intent: NotRequired[Optional[str]]
        payment_link: NotRequired[Optional[str]]
        starting_after: NotRequired[Optional[str]]
        subscription: NotRequired[Optional[str]]

    class ListCustomerDetailsParams(TypedDict):
        email: str

    class ListLineItemsParams(RequestOptions):
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        starting_after: NotRequired[Optional[str]]

    class RetrieveParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

    after_expiration: Optional[StripeObject]
    allow_promotion_codes: Optional[bool]
    amount_subtotal: Optional[int]
    amount_total: Optional[int]
    automatic_tax: StripeObject
    billing_address_collection: Optional[Literal["auto", "required"]]
    cancel_url: Optional[str]
    client_reference_id: Optional[str]
    client_secret: Optional[str]
    consent: Optional[StripeObject]
    consent_collection: Optional[StripeObject]
    created: int
    currency: Optional[str]
    currency_conversion: Optional[StripeObject]
    custom_fields: List[StripeObject]
    custom_text: StripeObject
    customer: Optional[ExpandableField["Customer"]]
    customer_creation: Optional[Literal["always", "if_required"]]
    customer_details: Optional[StripeObject]
    customer_email: Optional[str]
    expires_at: int
    id: str
    invoice: Optional[ExpandableField["Invoice"]]
    invoice_creation: Optional[StripeObject]
    line_items: Optional[ListObject["LineItem"]]
    livemode: bool
    locale: Optional[
        Literal[
            "auto",
            "bg",
            "cs",
            "da",
            "de",
            "el",
            "en",
            "en-GB",
            "es",
            "es-419",
            "et",
            "fi",
            "fil",
            "fr",
            "fr-CA",
            "hr",
            "hu",
            "id",
            "it",
            "ja",
            "ko",
            "lt",
            "lv",
            "ms",
            "mt",
            "nb",
            "nl",
            "pl",
            "pt",
            "pt-BR",
            "ro",
            "ru",
            "sk",
            "sl",
            "sv",
            "th",
            "tr",
            "vi",
            "zh",
            "zh-HK",
            "zh-TW",
        ]
    ]
    metadata: Optional[Dict[str, str]]
    mode: Literal["payment", "setup", "subscription"]
    object: Literal["checkout.session"]
    payment_intent: Optional[ExpandableField["PaymentIntent"]]
    payment_link: Optional[ExpandableField["PaymentLink"]]
    payment_method_collection: Optional[Literal["always", "if_required"]]
    payment_method_configuration_details: Optional[StripeObject]
    payment_method_options: Optional[StripeObject]
    payment_method_types: List[str]
    payment_status: Literal["no_payment_required", "paid", "unpaid"]
    phone_number_collection: Optional[StripeObject]
    recovered_from: Optional[str]
    redirect_on_completion: Optional[Literal["always", "if_required", "never"]]
    return_url: Optional[str]
    setup_intent: Optional[ExpandableField["SetupIntent"]]
    shipping_address_collection: Optional[StripeObject]
    shipping_cost: Optional[StripeObject]
    shipping_details: Optional[StripeObject]
    shipping_options: List[StripeObject]
    status: Optional[Literal["complete", "expired", "open"]]
    submit_type: Optional[Literal["auto", "book", "donate", "pay"]]
    subscription: Optional[ExpandableField["Subscription"]]
    success_url: Optional[str]
    tax_id_collection: Optional[StripeObject]
    total_details: Optional[StripeObject]
    ui_mode: Optional[Literal["embedded", "hosted"]]
    url: Optional[str]

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Session.CreateParams"]
    ) -> "Session":
        return cast(
            "Session",
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
    def _cls_expire(
        cls,
        session: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Session.ExpireParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/checkout/sessions/{session}/expire".format(
                session=util.sanitize_id(session)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_expire")
    def expire(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["Session.ExpireParams"]
    ):
        return self._request(
            "post",
            "/v1/checkout/sessions/{session}/expire".format(
                session=util.sanitize_id(self.get("id"))
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
        **params: Unpack["Session.ListParams"]
    ) -> ListObject["Session"]:
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
        session: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["Session.ListLineItemsParams"]
    ):
        return cls._static_request(
            "get",
            "/v1/checkout/sessions/{session}/line_items".format(
                session=util.sanitize_id(session)
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
        **params: Unpack["Session.ListLineItemsParams"]
    ):
        return self._request(
            "get",
            "/v1/checkout/sessions/{session}/line_items".format(
                session=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["Session.RetrieveParams"]
    ) -> "Session":
        instance = cls(id, **params)
        instance.refresh()
        return instance
