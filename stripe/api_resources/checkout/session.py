# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import util
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
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
    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            after_expiration: NotRequired[
                "Session.CreateParamsAfterExpiration|None"
            ]
            allow_promotion_codes: NotRequired["bool|None"]
            automatic_tax: NotRequired["Session.CreateParamsAutomaticTax|None"]
            billing_address_collection: NotRequired[
                "Literal['auto', 'required']|None"
            ]
            cancel_url: NotRequired["str|None"]
            client_reference_id: NotRequired["str|None"]
            consent_collection: NotRequired[
                "Session.CreateParamsConsentCollection|None"
            ]
            currency: NotRequired["str|None"]
            custom_fields: NotRequired[
                "List[Session.CreateParamsCustomField]|None"
            ]
            custom_text: NotRequired["Session.CreateParamsCustomText|None"]
            customer: NotRequired["str|None"]
            customer_creation: NotRequired[
                "Literal['always', 'if_required']|None"
            ]
            customer_email: NotRequired["str|None"]
            customer_update: NotRequired[
                "Session.CreateParamsCustomerUpdate|None"
            ]
            discounts: NotRequired["List[Session.CreateParamsDiscount]|None"]
            expand: NotRequired["List[str]|None"]
            expires_at: NotRequired["int|None"]
            invoice_creation: NotRequired[
                "Session.CreateParamsInvoiceCreation|None"
            ]
            line_items: NotRequired["List[Session.CreateParamsLineItem]|None"]
            locale: NotRequired[
                "Literal['auto', 'bg', 'cs', 'da', 'de', 'el', 'en', 'en-GB', 'es', 'es-419', 'et', 'fi', 'fil', 'fr', 'fr-CA', 'hr', 'hu', 'id', 'it', 'ja', 'ko', 'lt', 'lv', 'ms', 'mt', 'nb', 'nl', 'pl', 'pt', 'pt-BR', 'ro', 'ru', 'sk', 'sl', 'sv', 'th', 'tr', 'vi', 'zh', 'zh-HK', 'zh-TW']|None"
            ]
            metadata: NotRequired["Dict[str, str]|None"]
            mode: NotRequired[
                "Literal['payment', 'setup', 'subscription']|None"
            ]
            payment_intent_data: NotRequired[
                "Session.CreateParamsPaymentIntentData|None"
            ]
            payment_method_collection: NotRequired[
                "Literal['always', 'if_required']|None"
            ]
            payment_method_configuration: NotRequired["str|None"]
            payment_method_options: NotRequired[
                "Session.CreateParamsPaymentMethodOptions|None"
            ]
            payment_method_types: NotRequired[
                "List[Literal['acss_debit', 'affirm', 'afterpay_clearpay', 'alipay', 'au_becs_debit', 'bacs_debit', 'bancontact', 'blik', 'boleto', 'card', 'cashapp', 'customer_balance', 'eps', 'fpx', 'giropay', 'grabpay', 'ideal', 'klarna', 'konbini', 'link', 'oxxo', 'p24', 'paynow', 'paypal', 'pix', 'promptpay', 'sepa_debit', 'sofort', 'us_bank_account', 'wechat_pay', 'zip']]|None"
            ]
            phone_number_collection: NotRequired[
                "Session.CreateParamsPhoneNumberCollection|None"
            ]
            redirect_on_completion: NotRequired[
                "Literal['always', 'if_required', 'never']|None"
            ]
            return_url: NotRequired["str|None"]
            setup_intent_data: NotRequired[
                "Session.CreateParamsSetupIntentData|None"
            ]
            shipping_address_collection: NotRequired[
                "Session.CreateParamsShippingAddressCollection|None"
            ]
            shipping_options: NotRequired[
                "List[Session.CreateParamsShippingOption]|None"
            ]
            submit_type: NotRequired[
                "Literal['auto', 'book', 'donate', 'pay']|None"
            ]
            subscription_data: NotRequired[
                "Session.CreateParamsSubscriptionData|None"
            ]
            success_url: NotRequired["str|None"]
            tax_id_collection: NotRequired[
                "Session.CreateParamsTaxIdCollection|None"
            ]
            ui_mode: NotRequired["Literal['embedded', 'hosted']|None"]

        class CreateParamsTaxIdCollection(TypedDict):
            enabled: bool

        class CreateParamsSubscriptionData(TypedDict):
            application_fee_percent: NotRequired["float|None"]
            billing_cycle_anchor: NotRequired["int|None"]
            default_tax_rates: NotRequired["List[str]|None"]
            description: NotRequired["str|None"]
            metadata: NotRequired["Dict[str, str]|None"]
            on_behalf_of: NotRequired["str|None"]
            proration_behavior: NotRequired[
                "Literal['create_prorations', 'none']|None"
            ]
            transfer_data: NotRequired[
                "Session.CreateParamsSubscriptionDataTransferData|None"
            ]
            trial_end: NotRequired["int|None"]
            trial_period_days: NotRequired["int|None"]
            trial_settings: NotRequired[
                "Session.CreateParamsSubscriptionDataTrialSettings|None"
            ]

        class CreateParamsSubscriptionDataTrialSettings(TypedDict):
            end_behavior: "Session.CreateParamsSubscriptionDataTrialSettingsEndBehavior"

        class CreateParamsSubscriptionDataTrialSettingsEndBehavior(TypedDict):
            missing_payment_method: Literal[
                "cancel", "create_invoice", "pause"
            ]

        class CreateParamsSubscriptionDataTransferData(TypedDict):
            amount_percent: NotRequired["float|None"]
            destination: str

        class CreateParamsShippingOption(TypedDict):
            shipping_rate: NotRequired["str|None"]
            shipping_rate_data: NotRequired[
                "Session.CreateParamsShippingOptionShippingRateData|None"
            ]

        class CreateParamsShippingOptionShippingRateData(TypedDict):
            delivery_estimate: NotRequired[
                "Session.CreateParamsShippingOptionShippingRateDataDeliveryEstimate|None"
            ]
            display_name: str
            fixed_amount: NotRequired[
                "Session.CreateParamsShippingOptionShippingRateDataFixedAmount|None"
            ]
            metadata: NotRequired["Dict[str, str]|None"]
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            tax_code: NotRequired["str|None"]
            type: NotRequired["Literal['fixed_amount']|None"]

        class CreateParamsShippingOptionShippingRateDataFixedAmount(TypedDict):
            amount: int
            currency: str
            currency_options: NotRequired[
                "Dict[str, Session.CreateParamsShippingOptionShippingRateDataFixedAmountCurrencyOptions]|None"
            ]

        class CreateParamsShippingOptionShippingRateDataFixedAmountCurrencyOptions(
            TypedDict,
        ):
            amount: int
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]

        class CreateParamsShippingOptionShippingRateDataDeliveryEstimate(
            TypedDict,
        ):
            maximum: NotRequired[
                "Session.CreateParamsShippingOptionShippingRateDataDeliveryEstimateMaximum|None"
            ]
            minimum: NotRequired[
                "Session.CreateParamsShippingOptionShippingRateDataDeliveryEstimateMinimum|None"
            ]

        class CreateParamsShippingOptionShippingRateDataDeliveryEstimateMinimum(
            TypedDict,
        ):
            unit: Literal["business_day", "day", "hour", "month", "week"]
            value: int

        class CreateParamsShippingOptionShippingRateDataDeliveryEstimateMaximum(
            TypedDict,
        ):
            unit: Literal["business_day", "day", "hour", "month", "week"]
            value: int

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

        class CreateParamsSetupIntentData(TypedDict):
            description: NotRequired["str|None"]
            metadata: NotRequired["Dict[str, str]|None"]
            on_behalf_of: NotRequired["str|None"]

        class CreateParamsPhoneNumberCollection(TypedDict):
            enabled: bool

        class CreateParamsPaymentMethodOptions(TypedDict):
            acss_debit: NotRequired[
                "Session.CreateParamsPaymentMethodOptionsAcssDebit|None"
            ]
            affirm: NotRequired[
                "Session.CreateParamsPaymentMethodOptionsAffirm|None"
            ]
            afterpay_clearpay: NotRequired[
                "Session.CreateParamsPaymentMethodOptionsAfterpayClearpay|None"
            ]
            alipay: NotRequired[
                "Session.CreateParamsPaymentMethodOptionsAlipay|None"
            ]
            au_becs_debit: NotRequired[
                "Session.CreateParamsPaymentMethodOptionsAuBecsDebit|None"
            ]
            bacs_debit: NotRequired[
                "Session.CreateParamsPaymentMethodOptionsBacsDebit|None"
            ]
            bancontact: NotRequired[
                "Session.CreateParamsPaymentMethodOptionsBancontact|None"
            ]
            boleto: NotRequired[
                "Session.CreateParamsPaymentMethodOptionsBoleto|None"
            ]
            card: NotRequired[
                "Session.CreateParamsPaymentMethodOptionsCard|None"
            ]
            cashapp: NotRequired[
                "Session.CreateParamsPaymentMethodOptionsCashapp|None"
            ]
            customer_balance: NotRequired[
                "Session.CreateParamsPaymentMethodOptionsCustomerBalance|None"
            ]
            eps: NotRequired[
                "Session.CreateParamsPaymentMethodOptionsEps|None"
            ]
            fpx: NotRequired[
                "Session.CreateParamsPaymentMethodOptionsFpx|None"
            ]
            giropay: NotRequired[
                "Session.CreateParamsPaymentMethodOptionsGiropay|None"
            ]
            grabpay: NotRequired[
                "Session.CreateParamsPaymentMethodOptionsGrabpay|None"
            ]
            ideal: NotRequired[
                "Session.CreateParamsPaymentMethodOptionsIdeal|None"
            ]
            klarna: NotRequired[
                "Session.CreateParamsPaymentMethodOptionsKlarna|None"
            ]
            konbini: NotRequired[
                "Session.CreateParamsPaymentMethodOptionsKonbini|None"
            ]
            link: NotRequired[
                "Session.CreateParamsPaymentMethodOptionsLink|None"
            ]
            oxxo: NotRequired[
                "Session.CreateParamsPaymentMethodOptionsOxxo|None"
            ]
            p24: NotRequired[
                "Session.CreateParamsPaymentMethodOptionsP24|None"
            ]
            paynow: NotRequired[
                "Session.CreateParamsPaymentMethodOptionsPaynow|None"
            ]
            paypal: NotRequired[
                "Session.CreateParamsPaymentMethodOptionsPaypal|None"
            ]
            pix: NotRequired[
                "Session.CreateParamsPaymentMethodOptionsPix|None"
            ]
            sepa_debit: NotRequired[
                "Session.CreateParamsPaymentMethodOptionsSepaDebit|None"
            ]
            sofort: NotRequired[
                "Session.CreateParamsPaymentMethodOptionsSofort|None"
            ]
            us_bank_account: NotRequired[
                "Session.CreateParamsPaymentMethodOptionsUsBankAccount|None"
            ]
            wechat_pay: NotRequired[
                "Session.CreateParamsPaymentMethodOptionsWechatPay|None"
            ]

        class CreateParamsPaymentMethodOptionsWechatPay(TypedDict):
            app_id: NotRequired["str|None"]
            client: Literal["android", "ios", "web"]
            setup_future_usage: NotRequired["Literal['none']|None"]

        class CreateParamsPaymentMethodOptionsUsBankAccount(TypedDict):
            financial_connections: NotRequired[
                "Session.CreateParamsPaymentMethodOptionsUsBankAccountFinancialConnections|None"
            ]
            setup_future_usage: NotRequired[
                "Literal['none', 'off_session', 'on_session']|None"
            ]
            verification_method: NotRequired[
                "Literal['automatic', 'instant']|None"
            ]

        class CreateParamsPaymentMethodOptionsUsBankAccountFinancialConnections(
            TypedDict,
        ):
            permissions: NotRequired[
                "List[Literal['balances', 'ownership', 'payment_method', 'transactions']]|None"
            ]
            prefetch: NotRequired["List[Literal['balances']]|None"]

        class CreateParamsPaymentMethodOptionsSofort(TypedDict):
            setup_future_usage: NotRequired["Literal['none']|None"]

        class CreateParamsPaymentMethodOptionsSepaDebit(TypedDict):
            setup_future_usage: NotRequired[
                "Literal['none', 'off_session', 'on_session']|None"
            ]

        class CreateParamsPaymentMethodOptionsPix(TypedDict):
            expires_after_seconds: NotRequired["int|None"]

        class CreateParamsPaymentMethodOptionsPaypal(TypedDict):
            capture_method: NotRequired["Literal['']|Literal['manual']|None"]
            preferred_locale: NotRequired[
                "Literal['cs-CZ', 'da-DK', 'de-AT', 'de-DE', 'de-LU', 'el-GR', 'en-GB', 'en-US', 'es-ES', 'fi-FI', 'fr-BE', 'fr-FR', 'fr-LU', 'hu-HU', 'it-IT', 'nl-BE', 'nl-NL', 'pl-PL', 'pt-PT', 'sk-SK', 'sv-SE']|None"
            ]
            reference: NotRequired["str|None"]
            risk_correlation_id: NotRequired["str|None"]
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session']|None"
            ]

        class CreateParamsPaymentMethodOptionsPaynow(TypedDict):
            setup_future_usage: NotRequired["Literal['none']|None"]

        class CreateParamsPaymentMethodOptionsP24(TypedDict):
            setup_future_usage: NotRequired["Literal['none']|None"]
            tos_shown_and_accepted: NotRequired["bool|None"]

        class CreateParamsPaymentMethodOptionsOxxo(TypedDict):
            expires_after_days: NotRequired["int|None"]
            setup_future_usage: NotRequired["Literal['none']|None"]

        class CreateParamsPaymentMethodOptionsLink(TypedDict):
            setup_future_usage: NotRequired[
                "Literal['none', 'off_session']|None"
            ]

        class CreateParamsPaymentMethodOptionsKonbini(TypedDict):
            expires_after_days: NotRequired["int|None"]
            setup_future_usage: NotRequired["Literal['none']|None"]

        class CreateParamsPaymentMethodOptionsKlarna(TypedDict):
            setup_future_usage: NotRequired["Literal['none']|None"]

        class CreateParamsPaymentMethodOptionsIdeal(TypedDict):
            setup_future_usage: NotRequired["Literal['none']|None"]

        class CreateParamsPaymentMethodOptionsGrabpay(TypedDict):
            setup_future_usage: NotRequired["Literal['none']|None"]

        class CreateParamsPaymentMethodOptionsGiropay(TypedDict):
            setup_future_usage: NotRequired["Literal['none']|None"]

        class CreateParamsPaymentMethodOptionsFpx(TypedDict):
            setup_future_usage: NotRequired["Literal['none']|None"]

        class CreateParamsPaymentMethodOptionsEps(TypedDict):
            setup_future_usage: NotRequired["Literal['none']|None"]

        class CreateParamsPaymentMethodOptionsCustomerBalance(TypedDict):
            bank_transfer: NotRequired[
                "Session.CreateParamsPaymentMethodOptionsCustomerBalanceBankTransfer|None"
            ]
            funding_type: NotRequired["Literal['bank_transfer']|None"]
            setup_future_usage: NotRequired["Literal['none']|None"]

        class CreateParamsPaymentMethodOptionsCustomerBalanceBankTransfer(
            TypedDict,
        ):
            eu_bank_transfer: NotRequired[
                "Session.CreateParamsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer|None"
            ]
            requested_address_types: NotRequired[
                "List[Literal['aba', 'iban', 'sepa', 'sort_code', 'spei', 'swift', 'zengin']]|None"
            ]
            type: Literal[
                "eu_bank_transfer",
                "gb_bank_transfer",
                "jp_bank_transfer",
                "mx_bank_transfer",
                "us_bank_transfer",
            ]

        class CreateParamsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer(
            TypedDict,
        ):
            country: str

        class CreateParamsPaymentMethodOptionsCashapp(TypedDict):
            setup_future_usage: NotRequired[
                "Literal['none', 'off_session', 'on_session']|None"
            ]

        class CreateParamsPaymentMethodOptionsCard(TypedDict):
            installments: NotRequired[
                "Session.CreateParamsPaymentMethodOptionsCardInstallments|None"
            ]
            setup_future_usage: NotRequired[
                "Literal['off_session', 'on_session']|None"
            ]
            statement_descriptor_suffix_kana: NotRequired["str|None"]
            statement_descriptor_suffix_kanji: NotRequired["str|None"]

        class CreateParamsPaymentMethodOptionsCardInstallments(TypedDict):
            enabled: NotRequired["bool|None"]

        class CreateParamsPaymentMethodOptionsBoleto(TypedDict):
            expires_after_days: NotRequired["int|None"]
            setup_future_usage: NotRequired[
                "Literal['none', 'off_session', 'on_session']|None"
            ]

        class CreateParamsPaymentMethodOptionsBancontact(TypedDict):
            setup_future_usage: NotRequired["Literal['none']|None"]

        class CreateParamsPaymentMethodOptionsBacsDebit(TypedDict):
            setup_future_usage: NotRequired[
                "Literal['none', 'off_session', 'on_session']|None"
            ]

        class CreateParamsPaymentMethodOptionsAuBecsDebit(TypedDict):
            setup_future_usage: NotRequired["Literal['none']|None"]

        class CreateParamsPaymentMethodOptionsAlipay(TypedDict):
            setup_future_usage: NotRequired["Literal['none']|None"]

        class CreateParamsPaymentMethodOptionsAfterpayClearpay(TypedDict):
            setup_future_usage: NotRequired["Literal['none']|None"]

        class CreateParamsPaymentMethodOptionsAffirm(TypedDict):
            setup_future_usage: NotRequired["Literal['none']|None"]

        class CreateParamsPaymentMethodOptionsAcssDebit(TypedDict):
            currency: NotRequired["Literal['cad', 'usd']|None"]
            mandate_options: NotRequired[
                "Session.CreateParamsPaymentMethodOptionsAcssDebitMandateOptions|None"
            ]
            setup_future_usage: NotRequired[
                "Literal['none', 'off_session', 'on_session']|None"
            ]
            verification_method: NotRequired[
                "Literal['automatic', 'instant', 'microdeposits']|None"
            ]

        class CreateParamsPaymentMethodOptionsAcssDebitMandateOptions(
            TypedDict,
        ):
            custom_mandate_url: NotRequired["Literal['']|str|None"]
            default_for: NotRequired[
                "List[Literal['invoice', 'subscription']]|None"
            ]
            interval_description: NotRequired["str|None"]
            payment_schedule: NotRequired[
                "Literal['combined', 'interval', 'sporadic']|None"
            ]
            transaction_type: NotRequired[
                "Literal['business', 'personal']|None"
            ]

        class CreateParamsPaymentIntentData(TypedDict):
            application_fee_amount: NotRequired["int|None"]
            capture_method: NotRequired[
                "Literal['automatic', 'automatic_async', 'manual']|None"
            ]
            description: NotRequired["str|None"]
            metadata: NotRequired["Dict[str, str]|None"]
            on_behalf_of: NotRequired["str|None"]
            receipt_email: NotRequired["str|None"]
            setup_future_usage: NotRequired[
                "Literal['off_session', 'on_session']|None"
            ]
            shipping: NotRequired[
                "Session.CreateParamsPaymentIntentDataShipping|None"
            ]
            statement_descriptor: NotRequired["str|None"]
            statement_descriptor_suffix: NotRequired["str|None"]
            transfer_data: NotRequired[
                "Session.CreateParamsPaymentIntentDataTransferData|None"
            ]
            transfer_group: NotRequired["str|None"]

        class CreateParamsPaymentIntentDataTransferData(TypedDict):
            amount: NotRequired["int|None"]
            destination: str

        class CreateParamsPaymentIntentDataShipping(TypedDict):
            address: "Session.CreateParamsPaymentIntentDataShippingAddress"
            carrier: NotRequired["str|None"]
            name: str
            phone: NotRequired["str|None"]
            tracking_number: NotRequired["str|None"]

        class CreateParamsPaymentIntentDataShippingAddress(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: str
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]

        class CreateParamsLineItem(TypedDict):
            adjustable_quantity: NotRequired[
                "Session.CreateParamsLineItemAdjustableQuantity|None"
            ]
            dynamic_tax_rates: NotRequired["List[str]|None"]
            price: NotRequired["str|None"]
            price_data: NotRequired[
                "Session.CreateParamsLineItemPriceData|None"
            ]
            quantity: NotRequired["int|None"]
            tax_rates: NotRequired["List[str]|None"]

        class CreateParamsLineItemPriceData(TypedDict):
            currency: str
            product: NotRequired["str|None"]
            product_data: NotRequired[
                "Session.CreateParamsLineItemPriceDataProductData|None"
            ]
            recurring: NotRequired[
                "Session.CreateParamsLineItemPriceDataRecurring|None"
            ]
            tax_behavior: NotRequired[
                "Literal['exclusive', 'inclusive', 'unspecified']|None"
            ]
            unit_amount: NotRequired["int|None"]
            unit_amount_decimal: NotRequired["float|None"]

        class CreateParamsLineItemPriceDataRecurring(TypedDict):
            interval: Literal["day", "month", "week", "year"]
            interval_count: NotRequired["int|None"]

        class CreateParamsLineItemPriceDataProductData(TypedDict):
            description: NotRequired["str|None"]
            images: NotRequired["List[str]|None"]
            metadata: NotRequired["Dict[str, str]|None"]
            name: str
            tax_code: NotRequired["str|None"]

        class CreateParamsLineItemAdjustableQuantity(TypedDict):
            enabled: bool
            maximum: NotRequired["int|None"]
            minimum: NotRequired["int|None"]

        class CreateParamsInvoiceCreation(TypedDict):
            enabled: bool
            invoice_data: NotRequired[
                "Session.CreateParamsInvoiceCreationInvoiceData|None"
            ]

        class CreateParamsInvoiceCreationInvoiceData(TypedDict):
            account_tax_ids: NotRequired["Literal['']|List[str]|None"]
            custom_fields: NotRequired[
                "Literal['']|List[Session.CreateParamsInvoiceCreationInvoiceDataCustomField]|None"
            ]
            description: NotRequired["str|None"]
            footer: NotRequired["str|None"]
            metadata: NotRequired["Dict[str, str]|None"]
            rendering_options: NotRequired[
                "Literal['']|Session.CreateParamsInvoiceCreationInvoiceDataRenderingOptions|None"
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

        class CreateParamsDiscount(TypedDict):
            coupon: NotRequired["str|None"]
            promotion_code: NotRequired["str|None"]

        class CreateParamsCustomerUpdate(TypedDict):
            address: NotRequired["Literal['auto', 'never']|None"]
            name: NotRequired["Literal['auto', 'never']|None"]
            shipping: NotRequired["Literal['auto', 'never']|None"]

        class CreateParamsCustomText(TypedDict):
            shipping_address: NotRequired[
                "Literal['']|Session.CreateParamsCustomTextShippingAddress|None"
            ]
            submit: NotRequired[
                "Literal['']|Session.CreateParamsCustomTextSubmit|None"
            ]
            terms_of_service_acceptance: NotRequired[
                "Literal['']|Session.CreateParamsCustomTextTermsOfServiceAcceptance|None"
            ]

        class CreateParamsCustomTextTermsOfServiceAcceptance(TypedDict):
            message: str

        class CreateParamsCustomTextSubmit(TypedDict):
            message: str

        class CreateParamsCustomTextShippingAddress(TypedDict):
            message: str

        class CreateParamsCustomField(TypedDict):
            dropdown: NotRequired[
                "Session.CreateParamsCustomFieldDropdown|None"
            ]
            key: str
            label: "Session.CreateParamsCustomFieldLabel"
            numeric: NotRequired["Session.CreateParamsCustomFieldNumeric|None"]
            optional: NotRequired["bool|None"]
            text: NotRequired["Session.CreateParamsCustomFieldText|None"]
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
            options: List["Session.CreateParamsCustomFieldDropdownOption"]

        class CreateParamsCustomFieldDropdownOption(TypedDict):
            label: str
            value: str

        class CreateParamsConsentCollection(TypedDict):
            promotions: NotRequired["Literal['auto', 'none']|None"]
            terms_of_service: NotRequired["Literal['none', 'required']|None"]

        class CreateParamsAutomaticTax(TypedDict):
            enabled: bool

        class CreateParamsAfterExpiration(TypedDict):
            recovery: NotRequired[
                "Session.CreateParamsAfterExpirationRecovery|None"
            ]

        class CreateParamsAfterExpirationRecovery(TypedDict):
            allow_promotion_codes: NotRequired["bool|None"]
            enabled: bool

        class ExpireParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

        class ListParams(RequestOptions):
            customer: NotRequired["str|None"]
            customer_details: NotRequired[
                "Session.ListParamsCustomerDetails|None"
            ]
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            payment_intent: NotRequired["str|None"]
            payment_link: NotRequired["str|None"]
            starting_after: NotRequired["str|None"]
            subscription: NotRequired["str|None"]

        class ListParamsCustomerDetails(TypedDict):
            email: str

        class ListLineItemsParams(RequestOptions):
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

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
