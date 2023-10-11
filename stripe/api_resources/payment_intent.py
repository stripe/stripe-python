# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    SearchableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.api_resources.search_result_object import SearchResultObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import Any, Dict, List, Optional, Union, cast
from typing_extensions import Literal, NotRequired, TypedDict, Unpack
from urllib.parse import quote_plus

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.account import Account
    from stripe.api_resources.application import Application
    from stripe.api_resources.charge import Charge
    from stripe.api_resources.customer import Customer
    from stripe.api_resources.invoice import Invoice
    from stripe.api_resources.payment_method import PaymentMethod
    from stripe.api_resources.review import Review


class PaymentIntent(
    CreateableAPIResource["PaymentIntent"],
    ListableAPIResource["PaymentIntent"],
    SearchableAPIResource["PaymentIntent"],
    UpdateableAPIResource["PaymentIntent"],
):
    """
    A PaymentIntent guides you through the process of collecting a payment from your customer.
    We recommend that you create exactly one PaymentIntent for each order or
    customer session in your system. You can reference the PaymentIntent later to
    see the history of payment attempts for a particular session.

    A PaymentIntent transitions through
    [multiple statuses](https://stripe.com/docs/payments/intents#intent-statuses)
    throughout its lifetime as it interfaces with Stripe.js to perform
    authentication flows and ultimately creates at most one successful charge.

    Related guide: [Payment Intents API](https://stripe.com/docs/payments/payment-intents)
    """

    OBJECT_NAME = "payment_intent"

    class ApplyCustomerBalanceParams(RequestOptions):
        amount: NotRequired[Optional[int]]
        currency: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]

    class CancelParams(RequestOptions):
        cancellation_reason: NotRequired[
            Optional[
                Literal[
                    "abandoned",
                    "duplicate",
                    "fraudulent",
                    "requested_by_customer",
                ]
            ]
        ]
        expand: NotRequired[Optional[List[str]]]

    class CaptureParams(RequestOptions):
        amount_to_capture: NotRequired[Optional[int]]
        application_fee_amount: NotRequired[Optional[int]]
        expand: NotRequired[Optional[List[str]]]
        final_capture: NotRequired[Optional[bool]]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]
        statement_descriptor: NotRequired[Optional[str]]
        statement_descriptor_suffix: NotRequired[Optional[str]]
        transfer_data: NotRequired[
            Optional["PaymentIntent.CaptureParamsTransferData"]
        ]

    class CaptureParamsTransferData(TypedDict):
        amount: NotRequired[Optional[int]]

    class ConfirmParams(RequestOptions):
        capture_method: NotRequired[
            Optional[Literal["automatic", "automatic_async", "manual"]]
        ]
        error_on_requires_action: NotRequired[Optional[bool]]
        expand: NotRequired[Optional[List[str]]]
        mandate: NotRequired[Optional[str]]
        mandate_data: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    Union[
                        "PaymentIntent.ConfirmParamsMandateData",
                        "PaymentIntent.ConfirmParamsMandateData",
                    ],
                ]
            ]
        ]
        off_session: NotRequired[
            Optional[Union[bool, Literal["one_off", "recurring"]]]
        ]
        payment_method: NotRequired[Optional[str]]
        payment_method_data: NotRequired[
            Optional["PaymentIntent.ConfirmParamsPaymentMethodData"]
        ]
        payment_method_options: NotRequired[
            Optional["PaymentIntent.ConfirmParamsPaymentMethodOptions"]
        ]
        radar_options: NotRequired[
            Optional["PaymentIntent.ConfirmParamsRadarOptions"]
        ]
        receipt_email: NotRequired[Optional[Union[Literal[""], str]]]
        return_url: NotRequired[Optional[str]]
        setup_future_usage: NotRequired[
            Optional[Union[Literal[""], Literal["off_session", "on_session"]]]
        ]
        shipping: NotRequired[
            Optional[Union[Literal[""], "PaymentIntent.ConfirmParamsShipping"]]
        ]
        use_stripe_sdk: NotRequired[Optional[bool]]

    class ConfirmParamsShipping(TypedDict):
        address: "PaymentIntent.ConfirmParamsShippingAddress"
        carrier: NotRequired[Optional[str]]
        name: str
        phone: NotRequired[Optional[str]]
        tracking_number: NotRequired[Optional[str]]

    class ConfirmParamsShippingAddress(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class ConfirmParamsRadarOptions(TypedDict):
        session: NotRequired[Optional[str]]

    class ConfirmParamsPaymentMethodOptions(TypedDict):
        acss_debit: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmParamsPaymentMethodOptionsAcssDebit",
                ]
            ]
        ]
        affirm: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmParamsPaymentMethodOptionsAffirm",
                ]
            ]
        ]
        afterpay_clearpay: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmParamsPaymentMethodOptionsAfterpayClearpay",
                ]
            ]
        ]
        alipay: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmParamsPaymentMethodOptionsAlipay",
                ]
            ]
        ]
        au_becs_debit: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmParamsPaymentMethodOptionsAuBecsDebit",
                ]
            ]
        ]
        bacs_debit: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmParamsPaymentMethodOptionsBacsDebit",
                ]
            ]
        ]
        bancontact: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmParamsPaymentMethodOptionsBancontact",
                ]
            ]
        ]
        blik: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmParamsPaymentMethodOptionsBlik",
                ]
            ]
        ]
        boleto: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmParamsPaymentMethodOptionsBoleto",
                ]
            ]
        ]
        card: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmParamsPaymentMethodOptionsCard",
                ]
            ]
        ]
        card_present: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmParamsPaymentMethodOptionsCardPresent",
                ]
            ]
        ]
        cashapp: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmParamsPaymentMethodOptionsCashapp",
                ]
            ]
        ]
        customer_balance: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmParamsPaymentMethodOptionsCustomerBalance",
                ]
            ]
        ]
        eps: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmParamsPaymentMethodOptionsEps",
                ]
            ]
        ]
        fpx: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmParamsPaymentMethodOptionsFpx",
                ]
            ]
        ]
        giropay: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmParamsPaymentMethodOptionsGiropay",
                ]
            ]
        ]
        grabpay: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmParamsPaymentMethodOptionsGrabpay",
                ]
            ]
        ]
        ideal: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmParamsPaymentMethodOptionsIdeal",
                ]
            ]
        ]
        interac_present: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmParamsPaymentMethodOptionsInteracPresent",
                ]
            ]
        ]
        klarna: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmParamsPaymentMethodOptionsKlarna",
                ]
            ]
        ]
        konbini: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmParamsPaymentMethodOptionsKonbini",
                ]
            ]
        ]
        link: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmParamsPaymentMethodOptionsLink",
                ]
            ]
        ]
        oxxo: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmParamsPaymentMethodOptionsOxxo",
                ]
            ]
        ]
        p24: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmParamsPaymentMethodOptionsP24",
                ]
            ]
        ]
        paynow: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmParamsPaymentMethodOptionsPaynow",
                ]
            ]
        ]
        paypal: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmParamsPaymentMethodOptionsPaypal",
                ]
            ]
        ]
        pix: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmParamsPaymentMethodOptionsPix",
                ]
            ]
        ]
        promptpay: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmParamsPaymentMethodOptionsPromptpay",
                ]
            ]
        ]
        sepa_debit: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmParamsPaymentMethodOptionsSepaDebit",
                ]
            ]
        ]
        sofort: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmParamsPaymentMethodOptionsSofort",
                ]
            ]
        ]
        us_bank_account: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmParamsPaymentMethodOptionsUsBankAccount",
                ]
            ]
        ]
        wechat_pay: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmParamsPaymentMethodOptionsWechatPay",
                ]
            ]
        ]
        zip: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmParamsPaymentMethodOptionsZip",
                ]
            ]
        ]

    class ConfirmParamsPaymentMethodOptionsZip(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ConfirmParamsPaymentMethodOptionsWechatPay(TypedDict):
        app_id: NotRequired[Optional[str]]
        client: Literal["android", "ios", "web"]
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ConfirmParamsPaymentMethodOptionsUsBankAccount(TypedDict):
        financial_connections: NotRequired[
            Optional[
                "PaymentIntent.ConfirmParamsPaymentMethodOptionsUsBankAccountFinancialConnections"
            ]
        ]
        networks: NotRequired[
            Optional[
                "PaymentIntent.ConfirmParamsPaymentMethodOptionsUsBankAccountNetworks"
            ]
        ]
        preferred_settlement_speed: NotRequired[
            Optional[Union[Literal[""], Literal["fastest", "standard"]]]
        ]
        setup_future_usage: NotRequired[
            Optional[
                Union[
                    Literal[""], Literal["none", "off_session", "on_session"]
                ]
            ]
        ]
        verification_method: NotRequired[
            Optional[Literal["automatic", "instant", "microdeposits"]]
        ]

    class ConfirmParamsPaymentMethodOptionsUsBankAccountNetworks(TypedDict):
        requested: NotRequired[
            Optional[List[Literal["ach", "us_domestic_wire"]]]
        ]

    class ConfirmParamsPaymentMethodOptionsUsBankAccountFinancialConnections(
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
        return_url: NotRequired[Optional[str]]

    class ConfirmParamsPaymentMethodOptionsSofort(TypedDict):
        preferred_language: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    Literal["de", "en", "es", "fr", "it", "nl", "pl"],
                ]
            ]
        ]
        setup_future_usage: NotRequired[
            Optional[Union[Literal[""], Literal["none", "off_session"]]]
        ]

    class ConfirmParamsPaymentMethodOptionsSepaDebit(TypedDict):
        mandate_options: NotRequired[
            Optional[
                "PaymentIntent.ConfirmParamsPaymentMethodOptionsSepaDebitMandateOptions"
            ]
        ]
        setup_future_usage: NotRequired[
            Optional[
                Union[
                    Literal[""], Literal["none", "off_session", "on_session"]
                ]
            ]
        ]

    class ConfirmParamsPaymentMethodOptionsSepaDebitMandateOptions(TypedDict):
        pass

    class ConfirmParamsPaymentMethodOptionsPromptpay(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ConfirmParamsPaymentMethodOptionsPix(TypedDict):
        expires_after_seconds: NotRequired[Optional[int]]
        expires_at: NotRequired[Optional[int]]
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ConfirmParamsPaymentMethodOptionsPaypal(TypedDict):
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

    class ConfirmParamsPaymentMethodOptionsPaynow(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ConfirmParamsPaymentMethodOptionsP24(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]
        tos_shown_and_accepted: NotRequired[Optional[bool]]

    class ConfirmParamsPaymentMethodOptionsOxxo(TypedDict):
        expires_after_days: NotRequired[Optional[int]]
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ConfirmParamsPaymentMethodOptionsLink(TypedDict):
        capture_method: NotRequired[
            Optional[Union[Literal[""], Literal["manual"]]]
        ]
        persistent_token: NotRequired[Optional[str]]
        setup_future_usage: NotRequired[
            Optional[Union[Literal[""], Literal["none", "off_session"]]]
        ]

    class ConfirmParamsPaymentMethodOptionsKonbini(TypedDict):
        confirmation_number: NotRequired[Optional[Union[Literal[""], str]]]
        expires_after_days: NotRequired[Optional[Union[Literal[""], int]]]
        expires_at: NotRequired[Optional[Union[Literal[""], int]]]
        product_description: NotRequired[Optional[Union[Literal[""], str]]]
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ConfirmParamsPaymentMethodOptionsKlarna(TypedDict):
        capture_method: NotRequired[
            Optional[Union[Literal[""], Literal["manual"]]]
        ]
        preferred_locale: NotRequired[
            Optional[
                Literal[
                    "cs-CZ",
                    "da-DK",
                    "de-AT",
                    "de-CH",
                    "de-DE",
                    "el-GR",
                    "en-AT",
                    "en-AU",
                    "en-BE",
                    "en-CA",
                    "en-CH",
                    "en-CZ",
                    "en-DE",
                    "en-DK",
                    "en-ES",
                    "en-FI",
                    "en-FR",
                    "en-GB",
                    "en-GR",
                    "en-IE",
                    "en-IT",
                    "en-NL",
                    "en-NO",
                    "en-NZ",
                    "en-PL",
                    "en-PT",
                    "en-SE",
                    "en-US",
                    "es-ES",
                    "es-US",
                    "fi-FI",
                    "fr-BE",
                    "fr-CA",
                    "fr-CH",
                    "fr-FR",
                    "it-CH",
                    "it-IT",
                    "nb-NO",
                    "nl-BE",
                    "nl-NL",
                    "pl-PL",
                    "pt-PT",
                    "sv-FI",
                    "sv-SE",
                ]
            ]
        ]
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ConfirmParamsPaymentMethodOptionsInteracPresent(TypedDict):
        pass

    class ConfirmParamsPaymentMethodOptionsIdeal(TypedDict):
        setup_future_usage: NotRequired[
            Optional[Union[Literal[""], Literal["none", "off_session"]]]
        ]

    class ConfirmParamsPaymentMethodOptionsGrabpay(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ConfirmParamsPaymentMethodOptionsGiropay(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ConfirmParamsPaymentMethodOptionsFpx(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ConfirmParamsPaymentMethodOptionsEps(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ConfirmParamsPaymentMethodOptionsCustomerBalance(TypedDict):
        bank_transfer: NotRequired[
            Optional[
                "PaymentIntent.ConfirmParamsPaymentMethodOptionsCustomerBalanceBankTransfer"
            ]
        ]
        funding_type: NotRequired[Optional[Literal["bank_transfer"]]]
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ConfirmParamsPaymentMethodOptionsCustomerBalanceBankTransfer(
        TypedDict,
    ):
        eu_bank_transfer: NotRequired[
            Optional[
                "PaymentIntent.ConfirmParamsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer"
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

    class ConfirmParamsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer(
        TypedDict,
    ):
        country: str

    class ConfirmParamsPaymentMethodOptionsCashapp(TypedDict):
        capture_method: NotRequired[
            Optional[Union[Literal[""], Literal["manual"]]]
        ]
        setup_future_usage: NotRequired[
            Optional[
                Union[
                    Literal[""], Literal["none", "off_session", "on_session"]
                ]
            ]
        ]

    class ConfirmParamsPaymentMethodOptionsCardPresent(TypedDict):
        request_extended_authorization: NotRequired[Optional[bool]]
        request_incremental_authorization: NotRequired[
            Optional[Literal["if_available", "never"]]
        ]
        request_incremental_authorization_support: NotRequired[Optional[bool]]

    class ConfirmParamsPaymentMethodOptionsCard(TypedDict):
        capture_method: NotRequired[
            Optional[Union[Literal[""], Literal["manual"]]]
        ]
        cvc_token: NotRequired[Optional[str]]
        installments: NotRequired[
            Optional[
                "PaymentIntent.ConfirmParamsPaymentMethodOptionsCardInstallments"
            ]
        ]
        mandate_options: NotRequired[
            Optional[
                "PaymentIntent.ConfirmParamsPaymentMethodOptionsCardMandateOptions"
            ]
        ]
        moto: NotRequired[Optional[bool]]
        network: NotRequired[
            Optional[
                Literal[
                    "amex",
                    "cartes_bancaires",
                    "diners",
                    "discover",
                    "eftpos_au",
                    "interac",
                    "jcb",
                    "mastercard",
                    "unionpay",
                    "unknown",
                    "visa",
                ]
            ]
        ]
        request_extended_authorization: NotRequired[
            Optional[Literal["if_available", "never"]]
        ]
        request_incremental_authorization: NotRequired[
            Optional[Literal["if_available", "never"]]
        ]
        request_multicapture: NotRequired[
            Optional[Literal["if_available", "never"]]
        ]
        request_overcapture: NotRequired[
            Optional[Literal["if_available", "never"]]
        ]
        request_three_d_secure: NotRequired[
            Optional[Literal["any", "automatic"]]
        ]
        setup_future_usage: NotRequired[
            Optional[
                Union[
                    Literal[""], Literal["none", "off_session", "on_session"]
                ]
            ]
        ]
        statement_descriptor_suffix_kana: NotRequired[
            Optional[Union[Literal[""], str]]
        ]
        statement_descriptor_suffix_kanji: NotRequired[
            Optional[Union[Literal[""], str]]
        ]

    class ConfirmParamsPaymentMethodOptionsCardMandateOptions(TypedDict):
        amount: int
        amount_type: Literal["fixed", "maximum"]
        description: NotRequired[Optional[str]]
        end_date: NotRequired[Optional[int]]
        interval: Literal["day", "month", "sporadic", "week", "year"]
        interval_count: NotRequired[Optional[int]]
        reference: str
        start_date: int
        supported_types: NotRequired[Optional[List[Literal["india"]]]]

    class ConfirmParamsPaymentMethodOptionsCardInstallments(TypedDict):
        enabled: NotRequired[Optional[bool]]
        plan: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmParamsPaymentMethodOptionsCardInstallmentsPlan",
                ]
            ]
        ]

    class ConfirmParamsPaymentMethodOptionsCardInstallmentsPlan(TypedDict):
        count: int
        interval: Literal["month"]
        type: Literal["fixed_count"]

    class ConfirmParamsPaymentMethodOptionsBoleto(TypedDict):
        expires_after_days: NotRequired[Optional[int]]
        setup_future_usage: NotRequired[
            Optional[
                Union[
                    Literal[""], Literal["none", "off_session", "on_session"]
                ]
            ]
        ]

    class ConfirmParamsPaymentMethodOptionsBlik(TypedDict):
        code: NotRequired[Optional[str]]

    class ConfirmParamsPaymentMethodOptionsBancontact(TypedDict):
        preferred_language: NotRequired[
            Optional[Literal["de", "en", "fr", "nl"]]
        ]
        setup_future_usage: NotRequired[
            Optional[Union[Literal[""], Literal["none", "off_session"]]]
        ]

    class ConfirmParamsPaymentMethodOptionsBacsDebit(TypedDict):
        setup_future_usage: NotRequired[
            Optional[
                Union[
                    Literal[""], Literal["none", "off_session", "on_session"]
                ]
            ]
        ]

    class ConfirmParamsPaymentMethodOptionsAuBecsDebit(TypedDict):
        setup_future_usage: NotRequired[
            Optional[
                Union[
                    Literal[""], Literal["none", "off_session", "on_session"]
                ]
            ]
        ]

    class ConfirmParamsPaymentMethodOptionsAlipay(TypedDict):
        setup_future_usage: NotRequired[
            Optional[Union[Literal[""], Literal["none", "off_session"]]]
        ]

    class ConfirmParamsPaymentMethodOptionsAfterpayClearpay(TypedDict):
        capture_method: NotRequired[
            Optional[Union[Literal[""], Literal["manual"]]]
        ]
        reference: NotRequired[Optional[str]]
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ConfirmParamsPaymentMethodOptionsAffirm(TypedDict):
        capture_method: NotRequired[
            Optional[Union[Literal[""], Literal["manual"]]]
        ]
        preferred_locale: NotRequired[Optional[str]]
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ConfirmParamsPaymentMethodOptionsAcssDebit(TypedDict):
        mandate_options: NotRequired[
            Optional[
                "PaymentIntent.ConfirmParamsPaymentMethodOptionsAcssDebitMandateOptions"
            ]
        ]
        setup_future_usage: NotRequired[
            Optional[
                Union[
                    Literal[""], Literal["none", "off_session", "on_session"]
                ]
            ]
        ]
        verification_method: NotRequired[
            Optional[Literal["automatic", "instant", "microdeposits"]]
        ]

    class ConfirmParamsPaymentMethodOptionsAcssDebitMandateOptions(TypedDict):
        custom_mandate_url: NotRequired[Optional[Union[Literal[""], str]]]
        interval_description: NotRequired[Optional[str]]
        payment_schedule: NotRequired[
            Optional[Literal["combined", "interval", "sporadic"]]
        ]
        transaction_type: NotRequired[
            Optional[Literal["business", "personal"]]
        ]

    class ConfirmParamsPaymentMethodData(TypedDict):
        acss_debit: NotRequired[
            Optional["PaymentIntent.ConfirmParamsPaymentMethodDataAcssDebit"]
        ]
        affirm: NotRequired[
            Optional["PaymentIntent.ConfirmParamsPaymentMethodDataAffirm"]
        ]
        afterpay_clearpay: NotRequired[
            Optional[
                "PaymentIntent.ConfirmParamsPaymentMethodDataAfterpayClearpay"
            ]
        ]
        alipay: NotRequired[
            Optional["PaymentIntent.ConfirmParamsPaymentMethodDataAlipay"]
        ]
        au_becs_debit: NotRequired[
            Optional["PaymentIntent.ConfirmParamsPaymentMethodDataAuBecsDebit"]
        ]
        bacs_debit: NotRequired[
            Optional["PaymentIntent.ConfirmParamsPaymentMethodDataBacsDebit"]
        ]
        bancontact: NotRequired[
            Optional["PaymentIntent.ConfirmParamsPaymentMethodDataBancontact"]
        ]
        billing_details: NotRequired[
            Optional[
                "PaymentIntent.ConfirmParamsPaymentMethodDataBillingDetails"
            ]
        ]
        blik: NotRequired[
            Optional["PaymentIntent.ConfirmParamsPaymentMethodDataBlik"]
        ]
        boleto: NotRequired[
            Optional["PaymentIntent.ConfirmParamsPaymentMethodDataBoleto"]
        ]
        cashapp: NotRequired[
            Optional["PaymentIntent.ConfirmParamsPaymentMethodDataCashapp"]
        ]
        customer_balance: NotRequired[
            Optional[
                "PaymentIntent.ConfirmParamsPaymentMethodDataCustomerBalance"
            ]
        ]
        eps: NotRequired[
            Optional["PaymentIntent.ConfirmParamsPaymentMethodDataEps"]
        ]
        fpx: NotRequired[
            Optional["PaymentIntent.ConfirmParamsPaymentMethodDataFpx"]
        ]
        giropay: NotRequired[
            Optional["PaymentIntent.ConfirmParamsPaymentMethodDataGiropay"]
        ]
        grabpay: NotRequired[
            Optional["PaymentIntent.ConfirmParamsPaymentMethodDataGrabpay"]
        ]
        ideal: NotRequired[
            Optional["PaymentIntent.ConfirmParamsPaymentMethodDataIdeal"]
        ]
        interac_present: NotRequired[
            Optional[
                "PaymentIntent.ConfirmParamsPaymentMethodDataInteracPresent"
            ]
        ]
        klarna: NotRequired[
            Optional["PaymentIntent.ConfirmParamsPaymentMethodDataKlarna"]
        ]
        konbini: NotRequired[
            Optional["PaymentIntent.ConfirmParamsPaymentMethodDataKonbini"]
        ]
        link: NotRequired[
            Optional["PaymentIntent.ConfirmParamsPaymentMethodDataLink"]
        ]
        metadata: NotRequired[Optional[Dict[str, str]]]
        oxxo: NotRequired[
            Optional["PaymentIntent.ConfirmParamsPaymentMethodDataOxxo"]
        ]
        p24: NotRequired[
            Optional["PaymentIntent.ConfirmParamsPaymentMethodDataP24"]
        ]
        paynow: NotRequired[
            Optional["PaymentIntent.ConfirmParamsPaymentMethodDataPaynow"]
        ]
        paypal: NotRequired[
            Optional["PaymentIntent.ConfirmParamsPaymentMethodDataPaypal"]
        ]
        pix: NotRequired[
            Optional["PaymentIntent.ConfirmParamsPaymentMethodDataPix"]
        ]
        promptpay: NotRequired[
            Optional["PaymentIntent.ConfirmParamsPaymentMethodDataPromptpay"]
        ]
        radar_options: NotRequired[
            Optional[
                "PaymentIntent.ConfirmParamsPaymentMethodDataRadarOptions"
            ]
        ]
        sepa_debit: NotRequired[
            Optional["PaymentIntent.ConfirmParamsPaymentMethodDataSepaDebit"]
        ]
        sofort: NotRequired[
            Optional["PaymentIntent.ConfirmParamsPaymentMethodDataSofort"]
        ]
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
        us_bank_account: NotRequired[
            Optional[
                "PaymentIntent.ConfirmParamsPaymentMethodDataUsBankAccount"
            ]
        ]
        wechat_pay: NotRequired[
            Optional["PaymentIntent.ConfirmParamsPaymentMethodDataWechatPay"]
        ]
        zip: NotRequired[
            Optional["PaymentIntent.ConfirmParamsPaymentMethodDataZip"]
        ]

    class ConfirmParamsPaymentMethodDataZip(TypedDict):
        pass

    class ConfirmParamsPaymentMethodDataWechatPay(TypedDict):
        pass

    class ConfirmParamsPaymentMethodDataUsBankAccount(TypedDict):
        account_holder_type: NotRequired[
            Optional[Literal["company", "individual"]]
        ]
        account_number: NotRequired[Optional[str]]
        account_type: NotRequired[Optional[Literal["checking", "savings"]]]
        financial_connections_account: NotRequired[Optional[str]]
        routing_number: NotRequired[Optional[str]]

    class ConfirmParamsPaymentMethodDataSofort(TypedDict):
        country: Literal["AT", "BE", "DE", "ES", "IT", "NL"]

    class ConfirmParamsPaymentMethodDataSepaDebit(TypedDict):
        iban: str

    class ConfirmParamsPaymentMethodDataRadarOptions(TypedDict):
        session: NotRequired[Optional[str]]

    class ConfirmParamsPaymentMethodDataPromptpay(TypedDict):
        pass

    class ConfirmParamsPaymentMethodDataPix(TypedDict):
        pass

    class ConfirmParamsPaymentMethodDataPaypal(TypedDict):
        pass

    class ConfirmParamsPaymentMethodDataPaynow(TypedDict):
        pass

    class ConfirmParamsPaymentMethodDataP24(TypedDict):
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

    class ConfirmParamsPaymentMethodDataOxxo(TypedDict):
        pass

    class ConfirmParamsPaymentMethodDataLink(TypedDict):
        pass

    class ConfirmParamsPaymentMethodDataKonbini(TypedDict):
        pass

    class ConfirmParamsPaymentMethodDataKlarna(TypedDict):
        dob: NotRequired[
            Optional["PaymentIntent.ConfirmParamsPaymentMethodDataKlarnaDob"]
        ]

    class ConfirmParamsPaymentMethodDataKlarnaDob(TypedDict):
        day: int
        month: int
        year: int

    class ConfirmParamsPaymentMethodDataInteracPresent(TypedDict):
        pass

    class ConfirmParamsPaymentMethodDataIdeal(TypedDict):
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

    class ConfirmParamsPaymentMethodDataGrabpay(TypedDict):
        pass

    class ConfirmParamsPaymentMethodDataGiropay(TypedDict):
        pass

    class ConfirmParamsPaymentMethodDataFpx(TypedDict):
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

    class ConfirmParamsPaymentMethodDataEps(TypedDict):
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

    class ConfirmParamsPaymentMethodDataCustomerBalance(TypedDict):
        pass

    class ConfirmParamsPaymentMethodDataCashapp(TypedDict):
        pass

    class ConfirmParamsPaymentMethodDataBoleto(TypedDict):
        tax_id: str

    class ConfirmParamsPaymentMethodDataBlik(TypedDict):
        pass

    class ConfirmParamsPaymentMethodDataBillingDetails(TypedDict):
        address: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmParamsPaymentMethodDataBillingDetailsAddress",
                ]
            ]
        ]
        email: NotRequired[Optional[Union[Literal[""], str]]]
        name: NotRequired[Optional[Union[Literal[""], str]]]
        phone: NotRequired[Optional[Union[Literal[""], str]]]

    class ConfirmParamsPaymentMethodDataBillingDetailsAddress(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class ConfirmParamsPaymentMethodDataBancontact(TypedDict):
        pass

    class ConfirmParamsPaymentMethodDataBacsDebit(TypedDict):
        account_number: NotRequired[Optional[str]]
        sort_code: NotRequired[Optional[str]]

    class ConfirmParamsPaymentMethodDataAuBecsDebit(TypedDict):
        account_number: str
        bsb_number: str

    class ConfirmParamsPaymentMethodDataAlipay(TypedDict):
        pass

    class ConfirmParamsPaymentMethodDataAfterpayClearpay(TypedDict):
        pass

    class ConfirmParamsPaymentMethodDataAffirm(TypedDict):
        pass

    class ConfirmParamsPaymentMethodDataAcssDebit(TypedDict):
        account_number: str
        institution_number: str
        transit_number: str

    class ConfirmParamsMandateData(TypedDict):
        customer_acceptance: "PaymentIntent.ConfirmParamsMandateDataCustomerAcceptance"

    class ConfirmParamsMandateDataCustomerAcceptance(TypedDict):
        online: "PaymentIntent.ConfirmParamsMandateDataCustomerAcceptanceOnline"
        type: Literal["online"]

    class ConfirmParamsMandateDataCustomerAcceptanceOnline(TypedDict):
        ip_address: NotRequired[Optional[str]]
        user_agent: NotRequired[Optional[str]]

    class CreateParams(RequestOptions):
        amount: int
        application_fee_amount: NotRequired[Optional[int]]
        automatic_payment_methods: NotRequired[
            Optional["PaymentIntent.CreateParamsAutomaticPaymentMethods"]
        ]
        capture_method: NotRequired[
            Optional[Literal["automatic", "automatic_async", "manual"]]
        ]
        confirm: NotRequired[Optional[bool]]
        confirmation_method: NotRequired[
            Optional[Literal["automatic", "manual"]]
        ]
        currency: str
        customer: NotRequired[Optional[str]]
        description: NotRequired[Optional[str]]
        error_on_requires_action: NotRequired[Optional[bool]]
        expand: NotRequired[Optional[List[str]]]
        mandate: NotRequired[Optional[str]]
        mandate_data: NotRequired[
            Optional[
                Union[Literal[""], "PaymentIntent.CreateParamsMandateData"]
            ]
        ]
        metadata: NotRequired[Optional[Dict[str, str]]]
        off_session: NotRequired[
            Optional[Union[bool, Literal["one_off", "recurring"]]]
        ]
        on_behalf_of: NotRequired[Optional[str]]
        payment_method: NotRequired[Optional[str]]
        payment_method_configuration: NotRequired[Optional[str]]
        payment_method_data: NotRequired[
            Optional["PaymentIntent.CreateParamsPaymentMethodData"]
        ]
        payment_method_options: NotRequired[
            Optional["PaymentIntent.CreateParamsPaymentMethodOptions"]
        ]
        payment_method_types: NotRequired[Optional[List[str]]]
        radar_options: NotRequired[
            Optional["PaymentIntent.CreateParamsRadarOptions"]
        ]
        receipt_email: NotRequired[Optional[str]]
        return_url: NotRequired[Optional[str]]
        setup_future_usage: NotRequired[
            Optional[Literal["off_session", "on_session"]]
        ]
        shipping: NotRequired[Optional["PaymentIntent.CreateParamsShipping"]]
        statement_descriptor: NotRequired[Optional[str]]
        statement_descriptor_suffix: NotRequired[Optional[str]]
        transfer_data: NotRequired[
            Optional["PaymentIntent.CreateParamsTransferData"]
        ]
        transfer_group: NotRequired[Optional[str]]
        use_stripe_sdk: NotRequired[Optional[bool]]

    class CreateParamsTransferData(TypedDict):
        amount: NotRequired[Optional[int]]
        destination: str

    class CreateParamsShipping(TypedDict):
        address: "PaymentIntent.CreateParamsShippingAddress"
        carrier: NotRequired[Optional[str]]
        name: str
        phone: NotRequired[Optional[str]]
        tracking_number: NotRequired[Optional[str]]

    class CreateParamsShippingAddress(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class CreateParamsRadarOptions(TypedDict):
        session: NotRequired[Optional[str]]

    class CreateParamsPaymentMethodOptions(TypedDict):
        acss_debit: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreateParamsPaymentMethodOptionsAcssDebit",
                ]
            ]
        ]
        affirm: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreateParamsPaymentMethodOptionsAffirm",
                ]
            ]
        ]
        afterpay_clearpay: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreateParamsPaymentMethodOptionsAfterpayClearpay",
                ]
            ]
        ]
        alipay: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreateParamsPaymentMethodOptionsAlipay",
                ]
            ]
        ]
        au_becs_debit: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreateParamsPaymentMethodOptionsAuBecsDebit",
                ]
            ]
        ]
        bacs_debit: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreateParamsPaymentMethodOptionsBacsDebit",
                ]
            ]
        ]
        bancontact: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreateParamsPaymentMethodOptionsBancontact",
                ]
            ]
        ]
        blik: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreateParamsPaymentMethodOptionsBlik",
                ]
            ]
        ]
        boleto: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreateParamsPaymentMethodOptionsBoleto",
                ]
            ]
        ]
        card: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreateParamsPaymentMethodOptionsCard",
                ]
            ]
        ]
        card_present: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreateParamsPaymentMethodOptionsCardPresent",
                ]
            ]
        ]
        cashapp: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreateParamsPaymentMethodOptionsCashapp",
                ]
            ]
        ]
        customer_balance: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreateParamsPaymentMethodOptionsCustomerBalance",
                ]
            ]
        ]
        eps: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreateParamsPaymentMethodOptionsEps",
                ]
            ]
        ]
        fpx: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreateParamsPaymentMethodOptionsFpx",
                ]
            ]
        ]
        giropay: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreateParamsPaymentMethodOptionsGiropay",
                ]
            ]
        ]
        grabpay: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreateParamsPaymentMethodOptionsGrabpay",
                ]
            ]
        ]
        ideal: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreateParamsPaymentMethodOptionsIdeal",
                ]
            ]
        ]
        interac_present: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreateParamsPaymentMethodOptionsInteracPresent",
                ]
            ]
        ]
        klarna: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreateParamsPaymentMethodOptionsKlarna",
                ]
            ]
        ]
        konbini: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreateParamsPaymentMethodOptionsKonbini",
                ]
            ]
        ]
        link: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreateParamsPaymentMethodOptionsLink",
                ]
            ]
        ]
        oxxo: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreateParamsPaymentMethodOptionsOxxo",
                ]
            ]
        ]
        p24: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreateParamsPaymentMethodOptionsP24",
                ]
            ]
        ]
        paynow: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreateParamsPaymentMethodOptionsPaynow",
                ]
            ]
        ]
        paypal: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreateParamsPaymentMethodOptionsPaypal",
                ]
            ]
        ]
        pix: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreateParamsPaymentMethodOptionsPix",
                ]
            ]
        ]
        promptpay: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreateParamsPaymentMethodOptionsPromptpay",
                ]
            ]
        ]
        sepa_debit: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreateParamsPaymentMethodOptionsSepaDebit",
                ]
            ]
        ]
        sofort: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreateParamsPaymentMethodOptionsSofort",
                ]
            ]
        ]
        us_bank_account: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreateParamsPaymentMethodOptionsUsBankAccount",
                ]
            ]
        ]
        wechat_pay: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreateParamsPaymentMethodOptionsWechatPay",
                ]
            ]
        ]
        zip: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreateParamsPaymentMethodOptionsZip",
                ]
            ]
        ]

    class CreateParamsPaymentMethodOptionsZip(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class CreateParamsPaymentMethodOptionsWechatPay(TypedDict):
        app_id: NotRequired[Optional[str]]
        client: Literal["android", "ios", "web"]
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class CreateParamsPaymentMethodOptionsUsBankAccount(TypedDict):
        financial_connections: NotRequired[
            Optional[
                "PaymentIntent.CreateParamsPaymentMethodOptionsUsBankAccountFinancialConnections"
            ]
        ]
        networks: NotRequired[
            Optional[
                "PaymentIntent.CreateParamsPaymentMethodOptionsUsBankAccountNetworks"
            ]
        ]
        preferred_settlement_speed: NotRequired[
            Optional[Union[Literal[""], Literal["fastest", "standard"]]]
        ]
        setup_future_usage: NotRequired[
            Optional[
                Union[
                    Literal[""], Literal["none", "off_session", "on_session"]
                ]
            ]
        ]
        verification_method: NotRequired[
            Optional[Literal["automatic", "instant", "microdeposits"]]
        ]

    class CreateParamsPaymentMethodOptionsUsBankAccountNetworks(TypedDict):
        requested: NotRequired[
            Optional[List[Literal["ach", "us_domestic_wire"]]]
        ]

    class CreateParamsPaymentMethodOptionsUsBankAccountFinancialConnections(
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
        return_url: NotRequired[Optional[str]]

    class CreateParamsPaymentMethodOptionsSofort(TypedDict):
        preferred_language: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    Literal["de", "en", "es", "fr", "it", "nl", "pl"],
                ]
            ]
        ]
        setup_future_usage: NotRequired[
            Optional[Union[Literal[""], Literal["none", "off_session"]]]
        ]

    class CreateParamsPaymentMethodOptionsSepaDebit(TypedDict):
        mandate_options: NotRequired[
            Optional[
                "PaymentIntent.CreateParamsPaymentMethodOptionsSepaDebitMandateOptions"
            ]
        ]
        setup_future_usage: NotRequired[
            Optional[
                Union[
                    Literal[""], Literal["none", "off_session", "on_session"]
                ]
            ]
        ]

    class CreateParamsPaymentMethodOptionsSepaDebitMandateOptions(TypedDict):
        pass

    class CreateParamsPaymentMethodOptionsPromptpay(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class CreateParamsPaymentMethodOptionsPix(TypedDict):
        expires_after_seconds: NotRequired[Optional[int]]
        expires_at: NotRequired[Optional[int]]
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class CreateParamsPaymentMethodOptionsPaypal(TypedDict):
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

    class CreateParamsPaymentMethodOptionsPaynow(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class CreateParamsPaymentMethodOptionsP24(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]
        tos_shown_and_accepted: NotRequired[Optional[bool]]

    class CreateParamsPaymentMethodOptionsOxxo(TypedDict):
        expires_after_days: NotRequired[Optional[int]]
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class CreateParamsPaymentMethodOptionsLink(TypedDict):
        capture_method: NotRequired[
            Optional[Union[Literal[""], Literal["manual"]]]
        ]
        persistent_token: NotRequired[Optional[str]]
        setup_future_usage: NotRequired[
            Optional[Union[Literal[""], Literal["none", "off_session"]]]
        ]

    class CreateParamsPaymentMethodOptionsKonbini(TypedDict):
        confirmation_number: NotRequired[Optional[Union[Literal[""], str]]]
        expires_after_days: NotRequired[Optional[Union[Literal[""], int]]]
        expires_at: NotRequired[Optional[Union[Literal[""], int]]]
        product_description: NotRequired[Optional[Union[Literal[""], str]]]
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class CreateParamsPaymentMethodOptionsKlarna(TypedDict):
        capture_method: NotRequired[
            Optional[Union[Literal[""], Literal["manual"]]]
        ]
        preferred_locale: NotRequired[
            Optional[
                Literal[
                    "cs-CZ",
                    "da-DK",
                    "de-AT",
                    "de-CH",
                    "de-DE",
                    "el-GR",
                    "en-AT",
                    "en-AU",
                    "en-BE",
                    "en-CA",
                    "en-CH",
                    "en-CZ",
                    "en-DE",
                    "en-DK",
                    "en-ES",
                    "en-FI",
                    "en-FR",
                    "en-GB",
                    "en-GR",
                    "en-IE",
                    "en-IT",
                    "en-NL",
                    "en-NO",
                    "en-NZ",
                    "en-PL",
                    "en-PT",
                    "en-SE",
                    "en-US",
                    "es-ES",
                    "es-US",
                    "fi-FI",
                    "fr-BE",
                    "fr-CA",
                    "fr-CH",
                    "fr-FR",
                    "it-CH",
                    "it-IT",
                    "nb-NO",
                    "nl-BE",
                    "nl-NL",
                    "pl-PL",
                    "pt-PT",
                    "sv-FI",
                    "sv-SE",
                ]
            ]
        ]
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class CreateParamsPaymentMethodOptionsInteracPresent(TypedDict):
        pass

    class CreateParamsPaymentMethodOptionsIdeal(TypedDict):
        setup_future_usage: NotRequired[
            Optional[Union[Literal[""], Literal["none", "off_session"]]]
        ]

    class CreateParamsPaymentMethodOptionsGrabpay(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class CreateParamsPaymentMethodOptionsGiropay(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class CreateParamsPaymentMethodOptionsFpx(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class CreateParamsPaymentMethodOptionsEps(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class CreateParamsPaymentMethodOptionsCustomerBalance(TypedDict):
        bank_transfer: NotRequired[
            Optional[
                "PaymentIntent.CreateParamsPaymentMethodOptionsCustomerBalanceBankTransfer"
            ]
        ]
        funding_type: NotRequired[Optional[Literal["bank_transfer"]]]
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class CreateParamsPaymentMethodOptionsCustomerBalanceBankTransfer(
        TypedDict,
    ):
        eu_bank_transfer: NotRequired[
            Optional[
                "PaymentIntent.CreateParamsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer"
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

    class CreateParamsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer(
        TypedDict,
    ):
        country: str

    class CreateParamsPaymentMethodOptionsCashapp(TypedDict):
        capture_method: NotRequired[
            Optional[Union[Literal[""], Literal["manual"]]]
        ]
        setup_future_usage: NotRequired[
            Optional[
                Union[
                    Literal[""], Literal["none", "off_session", "on_session"]
                ]
            ]
        ]

    class CreateParamsPaymentMethodOptionsCardPresent(TypedDict):
        request_extended_authorization: NotRequired[Optional[bool]]
        request_incremental_authorization: NotRequired[
            Optional[Literal["if_available", "never"]]
        ]
        request_incremental_authorization_support: NotRequired[Optional[bool]]

    class CreateParamsPaymentMethodOptionsCard(TypedDict):
        capture_method: NotRequired[
            Optional[Union[Literal[""], Literal["manual"]]]
        ]
        cvc_token: NotRequired[Optional[str]]
        installments: NotRequired[
            Optional[
                "PaymentIntent.CreateParamsPaymentMethodOptionsCardInstallments"
            ]
        ]
        mandate_options: NotRequired[
            Optional[
                "PaymentIntent.CreateParamsPaymentMethodOptionsCardMandateOptions"
            ]
        ]
        moto: NotRequired[Optional[bool]]
        network: NotRequired[
            Optional[
                Literal[
                    "amex",
                    "cartes_bancaires",
                    "diners",
                    "discover",
                    "eftpos_au",
                    "interac",
                    "jcb",
                    "mastercard",
                    "unionpay",
                    "unknown",
                    "visa",
                ]
            ]
        ]
        request_extended_authorization: NotRequired[
            Optional[Literal["if_available", "never"]]
        ]
        request_incremental_authorization: NotRequired[
            Optional[Literal["if_available", "never"]]
        ]
        request_multicapture: NotRequired[
            Optional[Literal["if_available", "never"]]
        ]
        request_overcapture: NotRequired[
            Optional[Literal["if_available", "never"]]
        ]
        request_three_d_secure: NotRequired[
            Optional[Literal["any", "automatic"]]
        ]
        setup_future_usage: NotRequired[
            Optional[
                Union[
                    Literal[""], Literal["none", "off_session", "on_session"]
                ]
            ]
        ]
        statement_descriptor_suffix_kana: NotRequired[
            Optional[Union[Literal[""], str]]
        ]
        statement_descriptor_suffix_kanji: NotRequired[
            Optional[Union[Literal[""], str]]
        ]

    class CreateParamsPaymentMethodOptionsCardMandateOptions(TypedDict):
        amount: int
        amount_type: Literal["fixed", "maximum"]
        description: NotRequired[Optional[str]]
        end_date: NotRequired[Optional[int]]
        interval: Literal["day", "month", "sporadic", "week", "year"]
        interval_count: NotRequired[Optional[int]]
        reference: str
        start_date: int
        supported_types: NotRequired[Optional[List[Literal["india"]]]]

    class CreateParamsPaymentMethodOptionsCardInstallments(TypedDict):
        enabled: NotRequired[Optional[bool]]
        plan: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreateParamsPaymentMethodOptionsCardInstallmentsPlan",
                ]
            ]
        ]

    class CreateParamsPaymentMethodOptionsCardInstallmentsPlan(TypedDict):
        count: int
        interval: Literal["month"]
        type: Literal["fixed_count"]

    class CreateParamsPaymentMethodOptionsBoleto(TypedDict):
        expires_after_days: NotRequired[Optional[int]]
        setup_future_usage: NotRequired[
            Optional[
                Union[
                    Literal[""], Literal["none", "off_session", "on_session"]
                ]
            ]
        ]

    class CreateParamsPaymentMethodOptionsBlik(TypedDict):
        code: NotRequired[Optional[str]]

    class CreateParamsPaymentMethodOptionsBancontact(TypedDict):
        preferred_language: NotRequired[
            Optional[Literal["de", "en", "fr", "nl"]]
        ]
        setup_future_usage: NotRequired[
            Optional[Union[Literal[""], Literal["none", "off_session"]]]
        ]

    class CreateParamsPaymentMethodOptionsBacsDebit(TypedDict):
        setup_future_usage: NotRequired[
            Optional[
                Union[
                    Literal[""], Literal["none", "off_session", "on_session"]
                ]
            ]
        ]

    class CreateParamsPaymentMethodOptionsAuBecsDebit(TypedDict):
        setup_future_usage: NotRequired[
            Optional[
                Union[
                    Literal[""], Literal["none", "off_session", "on_session"]
                ]
            ]
        ]

    class CreateParamsPaymentMethodOptionsAlipay(TypedDict):
        setup_future_usage: NotRequired[
            Optional[Union[Literal[""], Literal["none", "off_session"]]]
        ]

    class CreateParamsPaymentMethodOptionsAfterpayClearpay(TypedDict):
        capture_method: NotRequired[
            Optional[Union[Literal[""], Literal["manual"]]]
        ]
        reference: NotRequired[Optional[str]]
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class CreateParamsPaymentMethodOptionsAffirm(TypedDict):
        capture_method: NotRequired[
            Optional[Union[Literal[""], Literal["manual"]]]
        ]
        preferred_locale: NotRequired[Optional[str]]
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class CreateParamsPaymentMethodOptionsAcssDebit(TypedDict):
        mandate_options: NotRequired[
            Optional[
                "PaymentIntent.CreateParamsPaymentMethodOptionsAcssDebitMandateOptions"
            ]
        ]
        setup_future_usage: NotRequired[
            Optional[
                Union[
                    Literal[""], Literal["none", "off_session", "on_session"]
                ]
            ]
        ]
        verification_method: NotRequired[
            Optional[Literal["automatic", "instant", "microdeposits"]]
        ]

    class CreateParamsPaymentMethodOptionsAcssDebitMandateOptions(TypedDict):
        custom_mandate_url: NotRequired[Optional[Union[Literal[""], str]]]
        interval_description: NotRequired[Optional[str]]
        payment_schedule: NotRequired[
            Optional[Literal["combined", "interval", "sporadic"]]
        ]
        transaction_type: NotRequired[
            Optional[Literal["business", "personal"]]
        ]

    class CreateParamsPaymentMethodData(TypedDict):
        acss_debit: NotRequired[
            Optional["PaymentIntent.CreateParamsPaymentMethodDataAcssDebit"]
        ]
        affirm: NotRequired[
            Optional["PaymentIntent.CreateParamsPaymentMethodDataAffirm"]
        ]
        afterpay_clearpay: NotRequired[
            Optional[
                "PaymentIntent.CreateParamsPaymentMethodDataAfterpayClearpay"
            ]
        ]
        alipay: NotRequired[
            Optional["PaymentIntent.CreateParamsPaymentMethodDataAlipay"]
        ]
        au_becs_debit: NotRequired[
            Optional["PaymentIntent.CreateParamsPaymentMethodDataAuBecsDebit"]
        ]
        bacs_debit: NotRequired[
            Optional["PaymentIntent.CreateParamsPaymentMethodDataBacsDebit"]
        ]
        bancontact: NotRequired[
            Optional["PaymentIntent.CreateParamsPaymentMethodDataBancontact"]
        ]
        billing_details: NotRequired[
            Optional[
                "PaymentIntent.CreateParamsPaymentMethodDataBillingDetails"
            ]
        ]
        blik: NotRequired[
            Optional["PaymentIntent.CreateParamsPaymentMethodDataBlik"]
        ]
        boleto: NotRequired[
            Optional["PaymentIntent.CreateParamsPaymentMethodDataBoleto"]
        ]
        cashapp: NotRequired[
            Optional["PaymentIntent.CreateParamsPaymentMethodDataCashapp"]
        ]
        customer_balance: NotRequired[
            Optional[
                "PaymentIntent.CreateParamsPaymentMethodDataCustomerBalance"
            ]
        ]
        eps: NotRequired[
            Optional["PaymentIntent.CreateParamsPaymentMethodDataEps"]
        ]
        fpx: NotRequired[
            Optional["PaymentIntent.CreateParamsPaymentMethodDataFpx"]
        ]
        giropay: NotRequired[
            Optional["PaymentIntent.CreateParamsPaymentMethodDataGiropay"]
        ]
        grabpay: NotRequired[
            Optional["PaymentIntent.CreateParamsPaymentMethodDataGrabpay"]
        ]
        ideal: NotRequired[
            Optional["PaymentIntent.CreateParamsPaymentMethodDataIdeal"]
        ]
        interac_present: NotRequired[
            Optional[
                "PaymentIntent.CreateParamsPaymentMethodDataInteracPresent"
            ]
        ]
        klarna: NotRequired[
            Optional["PaymentIntent.CreateParamsPaymentMethodDataKlarna"]
        ]
        konbini: NotRequired[
            Optional["PaymentIntent.CreateParamsPaymentMethodDataKonbini"]
        ]
        link: NotRequired[
            Optional["PaymentIntent.CreateParamsPaymentMethodDataLink"]
        ]
        metadata: NotRequired[Optional[Dict[str, str]]]
        oxxo: NotRequired[
            Optional["PaymentIntent.CreateParamsPaymentMethodDataOxxo"]
        ]
        p24: NotRequired[
            Optional["PaymentIntent.CreateParamsPaymentMethodDataP24"]
        ]
        paynow: NotRequired[
            Optional["PaymentIntent.CreateParamsPaymentMethodDataPaynow"]
        ]
        paypal: NotRequired[
            Optional["PaymentIntent.CreateParamsPaymentMethodDataPaypal"]
        ]
        pix: NotRequired[
            Optional["PaymentIntent.CreateParamsPaymentMethodDataPix"]
        ]
        promptpay: NotRequired[
            Optional["PaymentIntent.CreateParamsPaymentMethodDataPromptpay"]
        ]
        radar_options: NotRequired[
            Optional["PaymentIntent.CreateParamsPaymentMethodDataRadarOptions"]
        ]
        sepa_debit: NotRequired[
            Optional["PaymentIntent.CreateParamsPaymentMethodDataSepaDebit"]
        ]
        sofort: NotRequired[
            Optional["PaymentIntent.CreateParamsPaymentMethodDataSofort"]
        ]
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
        us_bank_account: NotRequired[
            Optional[
                "PaymentIntent.CreateParamsPaymentMethodDataUsBankAccount"
            ]
        ]
        wechat_pay: NotRequired[
            Optional["PaymentIntent.CreateParamsPaymentMethodDataWechatPay"]
        ]
        zip: NotRequired[
            Optional["PaymentIntent.CreateParamsPaymentMethodDataZip"]
        ]

    class CreateParamsPaymentMethodDataZip(TypedDict):
        pass

    class CreateParamsPaymentMethodDataWechatPay(TypedDict):
        pass

    class CreateParamsPaymentMethodDataUsBankAccount(TypedDict):
        account_holder_type: NotRequired[
            Optional[Literal["company", "individual"]]
        ]
        account_number: NotRequired[Optional[str]]
        account_type: NotRequired[Optional[Literal["checking", "savings"]]]
        financial_connections_account: NotRequired[Optional[str]]
        routing_number: NotRequired[Optional[str]]

    class CreateParamsPaymentMethodDataSofort(TypedDict):
        country: Literal["AT", "BE", "DE", "ES", "IT", "NL"]

    class CreateParamsPaymentMethodDataSepaDebit(TypedDict):
        iban: str

    class CreateParamsPaymentMethodDataRadarOptions(TypedDict):
        session: NotRequired[Optional[str]]

    class CreateParamsPaymentMethodDataPromptpay(TypedDict):
        pass

    class CreateParamsPaymentMethodDataPix(TypedDict):
        pass

    class CreateParamsPaymentMethodDataPaypal(TypedDict):
        pass

    class CreateParamsPaymentMethodDataPaynow(TypedDict):
        pass

    class CreateParamsPaymentMethodDataP24(TypedDict):
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

    class CreateParamsPaymentMethodDataOxxo(TypedDict):
        pass

    class CreateParamsPaymentMethodDataLink(TypedDict):
        pass

    class CreateParamsPaymentMethodDataKonbini(TypedDict):
        pass

    class CreateParamsPaymentMethodDataKlarna(TypedDict):
        dob: NotRequired[
            Optional["PaymentIntent.CreateParamsPaymentMethodDataKlarnaDob"]
        ]

    class CreateParamsPaymentMethodDataKlarnaDob(TypedDict):
        day: int
        month: int
        year: int

    class CreateParamsPaymentMethodDataInteracPresent(TypedDict):
        pass

    class CreateParamsPaymentMethodDataIdeal(TypedDict):
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

    class CreateParamsPaymentMethodDataGrabpay(TypedDict):
        pass

    class CreateParamsPaymentMethodDataGiropay(TypedDict):
        pass

    class CreateParamsPaymentMethodDataFpx(TypedDict):
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

    class CreateParamsPaymentMethodDataEps(TypedDict):
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

    class CreateParamsPaymentMethodDataCustomerBalance(TypedDict):
        pass

    class CreateParamsPaymentMethodDataCashapp(TypedDict):
        pass

    class CreateParamsPaymentMethodDataBoleto(TypedDict):
        tax_id: str

    class CreateParamsPaymentMethodDataBlik(TypedDict):
        pass

    class CreateParamsPaymentMethodDataBillingDetails(TypedDict):
        address: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreateParamsPaymentMethodDataBillingDetailsAddress",
                ]
            ]
        ]
        email: NotRequired[Optional[Union[Literal[""], str]]]
        name: NotRequired[Optional[Union[Literal[""], str]]]
        phone: NotRequired[Optional[Union[Literal[""], str]]]

    class CreateParamsPaymentMethodDataBillingDetailsAddress(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class CreateParamsPaymentMethodDataBancontact(TypedDict):
        pass

    class CreateParamsPaymentMethodDataBacsDebit(TypedDict):
        account_number: NotRequired[Optional[str]]
        sort_code: NotRequired[Optional[str]]

    class CreateParamsPaymentMethodDataAuBecsDebit(TypedDict):
        account_number: str
        bsb_number: str

    class CreateParamsPaymentMethodDataAlipay(TypedDict):
        pass

    class CreateParamsPaymentMethodDataAfterpayClearpay(TypedDict):
        pass

    class CreateParamsPaymentMethodDataAffirm(TypedDict):
        pass

    class CreateParamsPaymentMethodDataAcssDebit(TypedDict):
        account_number: str
        institution_number: str
        transit_number: str

    class CreateParamsMandateData(TypedDict):
        customer_acceptance: "PaymentIntent.CreateParamsMandateDataCustomerAcceptance"

    class CreateParamsMandateDataCustomerAcceptance(TypedDict):
        accepted_at: NotRequired[Optional[int]]
        offline: NotRequired[
            Optional[
                "PaymentIntent.CreateParamsMandateDataCustomerAcceptanceOffline"
            ]
        ]
        online: NotRequired[
            Optional[
                "PaymentIntent.CreateParamsMandateDataCustomerAcceptanceOnline"
            ]
        ]
        type: Literal["offline", "online"]

    class CreateParamsMandateDataCustomerAcceptanceOnline(TypedDict):
        ip_address: str
        user_agent: str

    class CreateParamsMandateDataCustomerAcceptanceOffline(TypedDict):
        pass

    class CreateParamsAutomaticPaymentMethods(TypedDict):
        allow_redirects: NotRequired[Optional[Literal["always", "never"]]]
        enabled: bool

    class IncrementAuthorizationParams(RequestOptions):
        amount: int
        application_fee_amount: NotRequired[Optional[int]]
        description: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        metadata: NotRequired[Optional[Dict[str, str]]]
        statement_descriptor: NotRequired[Optional[str]]
        transfer_data: NotRequired[
            Optional["PaymentIntent.IncrementAuthorizationParamsTransferData"]
        ]

    class IncrementAuthorizationParamsTransferData(TypedDict):
        amount: NotRequired[Optional[int]]

    class ListParams(RequestOptions):
        created: NotRequired[
            Optional[Union["PaymentIntent.ListParamsCreated", int]]
        ]
        customer: NotRequired[Optional[str]]
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        starting_after: NotRequired[Optional[str]]

    class ListParamsCreated(TypedDict):
        gt: NotRequired[Optional[int]]
        gte: NotRequired[Optional[int]]
        lt: NotRequired[Optional[int]]
        lte: NotRequired[Optional[int]]

    class ModifyParams(RequestOptions):
        amount: NotRequired[Optional[int]]
        application_fee_amount: NotRequired[Optional[Union[Literal[""], int]]]
        capture_method: NotRequired[
            Optional[Literal["automatic", "automatic_async", "manual"]]
        ]
        currency: NotRequired[Optional[str]]
        customer: NotRequired[Optional[str]]
        description: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        metadata: NotRequired[Optional[Union[Literal[""], Dict[str, str]]]]
        payment_method: NotRequired[Optional[str]]
        payment_method_configuration: NotRequired[Optional[str]]
        payment_method_data: NotRequired[
            Optional["PaymentIntent.ModifyParamsPaymentMethodData"]
        ]
        payment_method_options: NotRequired[
            Optional["PaymentIntent.ModifyParamsPaymentMethodOptions"]
        ]
        payment_method_types: NotRequired[Optional[List[str]]]
        receipt_email: NotRequired[Optional[Union[Literal[""], str]]]
        setup_future_usage: NotRequired[
            Optional[Union[Literal[""], Literal["off_session", "on_session"]]]
        ]
        shipping: NotRequired[
            Optional[Union[Literal[""], "PaymentIntent.ModifyParamsShipping"]]
        ]
        statement_descriptor: NotRequired[Optional[str]]
        statement_descriptor_suffix: NotRequired[Optional[str]]
        transfer_data: NotRequired[
            Optional["PaymentIntent.ModifyParamsTransferData"]
        ]
        transfer_group: NotRequired[Optional[str]]

    class ModifyParamsTransferData(TypedDict):
        amount: NotRequired[Optional[int]]

    class ModifyParamsShipping(TypedDict):
        address: "PaymentIntent.ModifyParamsShippingAddress"
        carrier: NotRequired[Optional[str]]
        name: str
        phone: NotRequired[Optional[str]]
        tracking_number: NotRequired[Optional[str]]

    class ModifyParamsShippingAddress(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class ModifyParamsPaymentMethodOptions(TypedDict):
        acss_debit: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyParamsPaymentMethodOptionsAcssDebit",
                ]
            ]
        ]
        affirm: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyParamsPaymentMethodOptionsAffirm",
                ]
            ]
        ]
        afterpay_clearpay: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyParamsPaymentMethodOptionsAfterpayClearpay",
                ]
            ]
        ]
        alipay: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyParamsPaymentMethodOptionsAlipay",
                ]
            ]
        ]
        au_becs_debit: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyParamsPaymentMethodOptionsAuBecsDebit",
                ]
            ]
        ]
        bacs_debit: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyParamsPaymentMethodOptionsBacsDebit",
                ]
            ]
        ]
        bancontact: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyParamsPaymentMethodOptionsBancontact",
                ]
            ]
        ]
        blik: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyParamsPaymentMethodOptionsBlik",
                ]
            ]
        ]
        boleto: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyParamsPaymentMethodOptionsBoleto",
                ]
            ]
        ]
        card: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyParamsPaymentMethodOptionsCard",
                ]
            ]
        ]
        card_present: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyParamsPaymentMethodOptionsCardPresent",
                ]
            ]
        ]
        cashapp: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyParamsPaymentMethodOptionsCashapp",
                ]
            ]
        ]
        customer_balance: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyParamsPaymentMethodOptionsCustomerBalance",
                ]
            ]
        ]
        eps: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyParamsPaymentMethodOptionsEps",
                ]
            ]
        ]
        fpx: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyParamsPaymentMethodOptionsFpx",
                ]
            ]
        ]
        giropay: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyParamsPaymentMethodOptionsGiropay",
                ]
            ]
        ]
        grabpay: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyParamsPaymentMethodOptionsGrabpay",
                ]
            ]
        ]
        ideal: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyParamsPaymentMethodOptionsIdeal",
                ]
            ]
        ]
        interac_present: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyParamsPaymentMethodOptionsInteracPresent",
                ]
            ]
        ]
        klarna: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyParamsPaymentMethodOptionsKlarna",
                ]
            ]
        ]
        konbini: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyParamsPaymentMethodOptionsKonbini",
                ]
            ]
        ]
        link: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyParamsPaymentMethodOptionsLink",
                ]
            ]
        ]
        oxxo: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyParamsPaymentMethodOptionsOxxo",
                ]
            ]
        ]
        p24: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyParamsPaymentMethodOptionsP24",
                ]
            ]
        ]
        paynow: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyParamsPaymentMethodOptionsPaynow",
                ]
            ]
        ]
        paypal: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyParamsPaymentMethodOptionsPaypal",
                ]
            ]
        ]
        pix: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyParamsPaymentMethodOptionsPix",
                ]
            ]
        ]
        promptpay: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyParamsPaymentMethodOptionsPromptpay",
                ]
            ]
        ]
        sepa_debit: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyParamsPaymentMethodOptionsSepaDebit",
                ]
            ]
        ]
        sofort: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyParamsPaymentMethodOptionsSofort",
                ]
            ]
        ]
        us_bank_account: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyParamsPaymentMethodOptionsUsBankAccount",
                ]
            ]
        ]
        wechat_pay: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyParamsPaymentMethodOptionsWechatPay",
                ]
            ]
        ]
        zip: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyParamsPaymentMethodOptionsZip",
                ]
            ]
        ]

    class ModifyParamsPaymentMethodOptionsZip(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ModifyParamsPaymentMethodOptionsWechatPay(TypedDict):
        app_id: NotRequired[Optional[str]]
        client: Literal["android", "ios", "web"]
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ModifyParamsPaymentMethodOptionsUsBankAccount(TypedDict):
        financial_connections: NotRequired[
            Optional[
                "PaymentIntent.ModifyParamsPaymentMethodOptionsUsBankAccountFinancialConnections"
            ]
        ]
        networks: NotRequired[
            Optional[
                "PaymentIntent.ModifyParamsPaymentMethodOptionsUsBankAccountNetworks"
            ]
        ]
        preferred_settlement_speed: NotRequired[
            Optional[Union[Literal[""], Literal["fastest", "standard"]]]
        ]
        setup_future_usage: NotRequired[
            Optional[
                Union[
                    Literal[""], Literal["none", "off_session", "on_session"]
                ]
            ]
        ]
        verification_method: NotRequired[
            Optional[Literal["automatic", "instant", "microdeposits"]]
        ]

    class ModifyParamsPaymentMethodOptionsUsBankAccountNetworks(TypedDict):
        requested: NotRequired[
            Optional[List[Literal["ach", "us_domestic_wire"]]]
        ]

    class ModifyParamsPaymentMethodOptionsUsBankAccountFinancialConnections(
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
        return_url: NotRequired[Optional[str]]

    class ModifyParamsPaymentMethodOptionsSofort(TypedDict):
        preferred_language: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    Literal["de", "en", "es", "fr", "it", "nl", "pl"],
                ]
            ]
        ]
        setup_future_usage: NotRequired[
            Optional[Union[Literal[""], Literal["none", "off_session"]]]
        ]

    class ModifyParamsPaymentMethodOptionsSepaDebit(TypedDict):
        mandate_options: NotRequired[
            Optional[
                "PaymentIntent.ModifyParamsPaymentMethodOptionsSepaDebitMandateOptions"
            ]
        ]
        setup_future_usage: NotRequired[
            Optional[
                Union[
                    Literal[""], Literal["none", "off_session", "on_session"]
                ]
            ]
        ]

    class ModifyParamsPaymentMethodOptionsSepaDebitMandateOptions(TypedDict):
        pass

    class ModifyParamsPaymentMethodOptionsPromptpay(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ModifyParamsPaymentMethodOptionsPix(TypedDict):
        expires_after_seconds: NotRequired[Optional[int]]
        expires_at: NotRequired[Optional[int]]
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ModifyParamsPaymentMethodOptionsPaypal(TypedDict):
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

    class ModifyParamsPaymentMethodOptionsPaynow(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ModifyParamsPaymentMethodOptionsP24(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]
        tos_shown_and_accepted: NotRequired[Optional[bool]]

    class ModifyParamsPaymentMethodOptionsOxxo(TypedDict):
        expires_after_days: NotRequired[Optional[int]]
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ModifyParamsPaymentMethodOptionsLink(TypedDict):
        capture_method: NotRequired[
            Optional[Union[Literal[""], Literal["manual"]]]
        ]
        persistent_token: NotRequired[Optional[str]]
        setup_future_usage: NotRequired[
            Optional[Union[Literal[""], Literal["none", "off_session"]]]
        ]

    class ModifyParamsPaymentMethodOptionsKonbini(TypedDict):
        confirmation_number: NotRequired[Optional[Union[Literal[""], str]]]
        expires_after_days: NotRequired[Optional[Union[Literal[""], int]]]
        expires_at: NotRequired[Optional[Union[Literal[""], int]]]
        product_description: NotRequired[Optional[Union[Literal[""], str]]]
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ModifyParamsPaymentMethodOptionsKlarna(TypedDict):
        capture_method: NotRequired[
            Optional[Union[Literal[""], Literal["manual"]]]
        ]
        preferred_locale: NotRequired[
            Optional[
                Literal[
                    "cs-CZ",
                    "da-DK",
                    "de-AT",
                    "de-CH",
                    "de-DE",
                    "el-GR",
                    "en-AT",
                    "en-AU",
                    "en-BE",
                    "en-CA",
                    "en-CH",
                    "en-CZ",
                    "en-DE",
                    "en-DK",
                    "en-ES",
                    "en-FI",
                    "en-FR",
                    "en-GB",
                    "en-GR",
                    "en-IE",
                    "en-IT",
                    "en-NL",
                    "en-NO",
                    "en-NZ",
                    "en-PL",
                    "en-PT",
                    "en-SE",
                    "en-US",
                    "es-ES",
                    "es-US",
                    "fi-FI",
                    "fr-BE",
                    "fr-CA",
                    "fr-CH",
                    "fr-FR",
                    "it-CH",
                    "it-IT",
                    "nb-NO",
                    "nl-BE",
                    "nl-NL",
                    "pl-PL",
                    "pt-PT",
                    "sv-FI",
                    "sv-SE",
                ]
            ]
        ]
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ModifyParamsPaymentMethodOptionsInteracPresent(TypedDict):
        pass

    class ModifyParamsPaymentMethodOptionsIdeal(TypedDict):
        setup_future_usage: NotRequired[
            Optional[Union[Literal[""], Literal["none", "off_session"]]]
        ]

    class ModifyParamsPaymentMethodOptionsGrabpay(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ModifyParamsPaymentMethodOptionsGiropay(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ModifyParamsPaymentMethodOptionsFpx(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ModifyParamsPaymentMethodOptionsEps(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ModifyParamsPaymentMethodOptionsCustomerBalance(TypedDict):
        bank_transfer: NotRequired[
            Optional[
                "PaymentIntent.ModifyParamsPaymentMethodOptionsCustomerBalanceBankTransfer"
            ]
        ]
        funding_type: NotRequired[Optional[Literal["bank_transfer"]]]
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ModifyParamsPaymentMethodOptionsCustomerBalanceBankTransfer(
        TypedDict,
    ):
        eu_bank_transfer: NotRequired[
            Optional[
                "PaymentIntent.ModifyParamsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer"
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

    class ModifyParamsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer(
        TypedDict,
    ):
        country: str

    class ModifyParamsPaymentMethodOptionsCashapp(TypedDict):
        capture_method: NotRequired[
            Optional[Union[Literal[""], Literal["manual"]]]
        ]
        setup_future_usage: NotRequired[
            Optional[
                Union[
                    Literal[""], Literal["none", "off_session", "on_session"]
                ]
            ]
        ]

    class ModifyParamsPaymentMethodOptionsCardPresent(TypedDict):
        request_extended_authorization: NotRequired[Optional[bool]]
        request_incremental_authorization: NotRequired[
            Optional[Literal["if_available", "never"]]
        ]
        request_incremental_authorization_support: NotRequired[Optional[bool]]

    class ModifyParamsPaymentMethodOptionsCard(TypedDict):
        capture_method: NotRequired[
            Optional[Union[Literal[""], Literal["manual"]]]
        ]
        cvc_token: NotRequired[Optional[str]]
        installments: NotRequired[
            Optional[
                "PaymentIntent.ModifyParamsPaymentMethodOptionsCardInstallments"
            ]
        ]
        mandate_options: NotRequired[
            Optional[
                "PaymentIntent.ModifyParamsPaymentMethodOptionsCardMandateOptions"
            ]
        ]
        moto: NotRequired[Optional[bool]]
        network: NotRequired[
            Optional[
                Literal[
                    "amex",
                    "cartes_bancaires",
                    "diners",
                    "discover",
                    "eftpos_au",
                    "interac",
                    "jcb",
                    "mastercard",
                    "unionpay",
                    "unknown",
                    "visa",
                ]
            ]
        ]
        request_extended_authorization: NotRequired[
            Optional[Literal["if_available", "never"]]
        ]
        request_incremental_authorization: NotRequired[
            Optional[Literal["if_available", "never"]]
        ]
        request_multicapture: NotRequired[
            Optional[Literal["if_available", "never"]]
        ]
        request_overcapture: NotRequired[
            Optional[Literal["if_available", "never"]]
        ]
        request_three_d_secure: NotRequired[
            Optional[Literal["any", "automatic"]]
        ]
        setup_future_usage: NotRequired[
            Optional[
                Union[
                    Literal[""], Literal["none", "off_session", "on_session"]
                ]
            ]
        ]
        statement_descriptor_suffix_kana: NotRequired[
            Optional[Union[Literal[""], str]]
        ]
        statement_descriptor_suffix_kanji: NotRequired[
            Optional[Union[Literal[""], str]]
        ]

    class ModifyParamsPaymentMethodOptionsCardMandateOptions(TypedDict):
        amount: int
        amount_type: Literal["fixed", "maximum"]
        description: NotRequired[Optional[str]]
        end_date: NotRequired[Optional[int]]
        interval: Literal["day", "month", "sporadic", "week", "year"]
        interval_count: NotRequired[Optional[int]]
        reference: str
        start_date: int
        supported_types: NotRequired[Optional[List[Literal["india"]]]]

    class ModifyParamsPaymentMethodOptionsCardInstallments(TypedDict):
        enabled: NotRequired[Optional[bool]]
        plan: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyParamsPaymentMethodOptionsCardInstallmentsPlan",
                ]
            ]
        ]

    class ModifyParamsPaymentMethodOptionsCardInstallmentsPlan(TypedDict):
        count: int
        interval: Literal["month"]
        type: Literal["fixed_count"]

    class ModifyParamsPaymentMethodOptionsBoleto(TypedDict):
        expires_after_days: NotRequired[Optional[int]]
        setup_future_usage: NotRequired[
            Optional[
                Union[
                    Literal[""], Literal["none", "off_session", "on_session"]
                ]
            ]
        ]

    class ModifyParamsPaymentMethodOptionsBlik(TypedDict):
        code: NotRequired[Optional[str]]

    class ModifyParamsPaymentMethodOptionsBancontact(TypedDict):
        preferred_language: NotRequired[
            Optional[Literal["de", "en", "fr", "nl"]]
        ]
        setup_future_usage: NotRequired[
            Optional[Union[Literal[""], Literal["none", "off_session"]]]
        ]

    class ModifyParamsPaymentMethodOptionsBacsDebit(TypedDict):
        setup_future_usage: NotRequired[
            Optional[
                Union[
                    Literal[""], Literal["none", "off_session", "on_session"]
                ]
            ]
        ]

    class ModifyParamsPaymentMethodOptionsAuBecsDebit(TypedDict):
        setup_future_usage: NotRequired[
            Optional[
                Union[
                    Literal[""], Literal["none", "off_session", "on_session"]
                ]
            ]
        ]

    class ModifyParamsPaymentMethodOptionsAlipay(TypedDict):
        setup_future_usage: NotRequired[
            Optional[Union[Literal[""], Literal["none", "off_session"]]]
        ]

    class ModifyParamsPaymentMethodOptionsAfterpayClearpay(TypedDict):
        capture_method: NotRequired[
            Optional[Union[Literal[""], Literal["manual"]]]
        ]
        reference: NotRequired[Optional[str]]
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ModifyParamsPaymentMethodOptionsAffirm(TypedDict):
        capture_method: NotRequired[
            Optional[Union[Literal[""], Literal["manual"]]]
        ]
        preferred_locale: NotRequired[Optional[str]]
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ModifyParamsPaymentMethodOptionsAcssDebit(TypedDict):
        mandate_options: NotRequired[
            Optional[
                "PaymentIntent.ModifyParamsPaymentMethodOptionsAcssDebitMandateOptions"
            ]
        ]
        setup_future_usage: NotRequired[
            Optional[
                Union[
                    Literal[""], Literal["none", "off_session", "on_session"]
                ]
            ]
        ]
        verification_method: NotRequired[
            Optional[Literal["automatic", "instant", "microdeposits"]]
        ]

    class ModifyParamsPaymentMethodOptionsAcssDebitMandateOptions(TypedDict):
        custom_mandate_url: NotRequired[Optional[Union[Literal[""], str]]]
        interval_description: NotRequired[Optional[str]]
        payment_schedule: NotRequired[
            Optional[Literal["combined", "interval", "sporadic"]]
        ]
        transaction_type: NotRequired[
            Optional[Literal["business", "personal"]]
        ]

    class ModifyParamsPaymentMethodData(TypedDict):
        acss_debit: NotRequired[
            Optional["PaymentIntent.ModifyParamsPaymentMethodDataAcssDebit"]
        ]
        affirm: NotRequired[
            Optional["PaymentIntent.ModifyParamsPaymentMethodDataAffirm"]
        ]
        afterpay_clearpay: NotRequired[
            Optional[
                "PaymentIntent.ModifyParamsPaymentMethodDataAfterpayClearpay"
            ]
        ]
        alipay: NotRequired[
            Optional["PaymentIntent.ModifyParamsPaymentMethodDataAlipay"]
        ]
        au_becs_debit: NotRequired[
            Optional["PaymentIntent.ModifyParamsPaymentMethodDataAuBecsDebit"]
        ]
        bacs_debit: NotRequired[
            Optional["PaymentIntent.ModifyParamsPaymentMethodDataBacsDebit"]
        ]
        bancontact: NotRequired[
            Optional["PaymentIntent.ModifyParamsPaymentMethodDataBancontact"]
        ]
        billing_details: NotRequired[
            Optional[
                "PaymentIntent.ModifyParamsPaymentMethodDataBillingDetails"
            ]
        ]
        blik: NotRequired[
            Optional["PaymentIntent.ModifyParamsPaymentMethodDataBlik"]
        ]
        boleto: NotRequired[
            Optional["PaymentIntent.ModifyParamsPaymentMethodDataBoleto"]
        ]
        cashapp: NotRequired[
            Optional["PaymentIntent.ModifyParamsPaymentMethodDataCashapp"]
        ]
        customer_balance: NotRequired[
            Optional[
                "PaymentIntent.ModifyParamsPaymentMethodDataCustomerBalance"
            ]
        ]
        eps: NotRequired[
            Optional["PaymentIntent.ModifyParamsPaymentMethodDataEps"]
        ]
        fpx: NotRequired[
            Optional["PaymentIntent.ModifyParamsPaymentMethodDataFpx"]
        ]
        giropay: NotRequired[
            Optional["PaymentIntent.ModifyParamsPaymentMethodDataGiropay"]
        ]
        grabpay: NotRequired[
            Optional["PaymentIntent.ModifyParamsPaymentMethodDataGrabpay"]
        ]
        ideal: NotRequired[
            Optional["PaymentIntent.ModifyParamsPaymentMethodDataIdeal"]
        ]
        interac_present: NotRequired[
            Optional[
                "PaymentIntent.ModifyParamsPaymentMethodDataInteracPresent"
            ]
        ]
        klarna: NotRequired[
            Optional["PaymentIntent.ModifyParamsPaymentMethodDataKlarna"]
        ]
        konbini: NotRequired[
            Optional["PaymentIntent.ModifyParamsPaymentMethodDataKonbini"]
        ]
        link: NotRequired[
            Optional["PaymentIntent.ModifyParamsPaymentMethodDataLink"]
        ]
        metadata: NotRequired[Optional[Dict[str, str]]]
        oxxo: NotRequired[
            Optional["PaymentIntent.ModifyParamsPaymentMethodDataOxxo"]
        ]
        p24: NotRequired[
            Optional["PaymentIntent.ModifyParamsPaymentMethodDataP24"]
        ]
        paynow: NotRequired[
            Optional["PaymentIntent.ModifyParamsPaymentMethodDataPaynow"]
        ]
        paypal: NotRequired[
            Optional["PaymentIntent.ModifyParamsPaymentMethodDataPaypal"]
        ]
        pix: NotRequired[
            Optional["PaymentIntent.ModifyParamsPaymentMethodDataPix"]
        ]
        promptpay: NotRequired[
            Optional["PaymentIntent.ModifyParamsPaymentMethodDataPromptpay"]
        ]
        radar_options: NotRequired[
            Optional["PaymentIntent.ModifyParamsPaymentMethodDataRadarOptions"]
        ]
        sepa_debit: NotRequired[
            Optional["PaymentIntent.ModifyParamsPaymentMethodDataSepaDebit"]
        ]
        sofort: NotRequired[
            Optional["PaymentIntent.ModifyParamsPaymentMethodDataSofort"]
        ]
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
        us_bank_account: NotRequired[
            Optional[
                "PaymentIntent.ModifyParamsPaymentMethodDataUsBankAccount"
            ]
        ]
        wechat_pay: NotRequired[
            Optional["PaymentIntent.ModifyParamsPaymentMethodDataWechatPay"]
        ]
        zip: NotRequired[
            Optional["PaymentIntent.ModifyParamsPaymentMethodDataZip"]
        ]

    class ModifyParamsPaymentMethodDataZip(TypedDict):
        pass

    class ModifyParamsPaymentMethodDataWechatPay(TypedDict):
        pass

    class ModifyParamsPaymentMethodDataUsBankAccount(TypedDict):
        account_holder_type: NotRequired[
            Optional[Literal["company", "individual"]]
        ]
        account_number: NotRequired[Optional[str]]
        account_type: NotRequired[Optional[Literal["checking", "savings"]]]
        financial_connections_account: NotRequired[Optional[str]]
        routing_number: NotRequired[Optional[str]]

    class ModifyParamsPaymentMethodDataSofort(TypedDict):
        country: Literal["AT", "BE", "DE", "ES", "IT", "NL"]

    class ModifyParamsPaymentMethodDataSepaDebit(TypedDict):
        iban: str

    class ModifyParamsPaymentMethodDataRadarOptions(TypedDict):
        session: NotRequired[Optional[str]]

    class ModifyParamsPaymentMethodDataPromptpay(TypedDict):
        pass

    class ModifyParamsPaymentMethodDataPix(TypedDict):
        pass

    class ModifyParamsPaymentMethodDataPaypal(TypedDict):
        pass

    class ModifyParamsPaymentMethodDataPaynow(TypedDict):
        pass

    class ModifyParamsPaymentMethodDataP24(TypedDict):
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

    class ModifyParamsPaymentMethodDataOxxo(TypedDict):
        pass

    class ModifyParamsPaymentMethodDataLink(TypedDict):
        pass

    class ModifyParamsPaymentMethodDataKonbini(TypedDict):
        pass

    class ModifyParamsPaymentMethodDataKlarna(TypedDict):
        dob: NotRequired[
            Optional["PaymentIntent.ModifyParamsPaymentMethodDataKlarnaDob"]
        ]

    class ModifyParamsPaymentMethodDataKlarnaDob(TypedDict):
        day: int
        month: int
        year: int

    class ModifyParamsPaymentMethodDataInteracPresent(TypedDict):
        pass

    class ModifyParamsPaymentMethodDataIdeal(TypedDict):
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

    class ModifyParamsPaymentMethodDataGrabpay(TypedDict):
        pass

    class ModifyParamsPaymentMethodDataGiropay(TypedDict):
        pass

    class ModifyParamsPaymentMethodDataFpx(TypedDict):
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

    class ModifyParamsPaymentMethodDataEps(TypedDict):
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

    class ModifyParamsPaymentMethodDataCustomerBalance(TypedDict):
        pass

    class ModifyParamsPaymentMethodDataCashapp(TypedDict):
        pass

    class ModifyParamsPaymentMethodDataBoleto(TypedDict):
        tax_id: str

    class ModifyParamsPaymentMethodDataBlik(TypedDict):
        pass

    class ModifyParamsPaymentMethodDataBillingDetails(TypedDict):
        address: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyParamsPaymentMethodDataBillingDetailsAddress",
                ]
            ]
        ]
        email: NotRequired[Optional[Union[Literal[""], str]]]
        name: NotRequired[Optional[Union[Literal[""], str]]]
        phone: NotRequired[Optional[Union[Literal[""], str]]]

    class ModifyParamsPaymentMethodDataBillingDetailsAddress(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class ModifyParamsPaymentMethodDataBancontact(TypedDict):
        pass

    class ModifyParamsPaymentMethodDataBacsDebit(TypedDict):
        account_number: NotRequired[Optional[str]]
        sort_code: NotRequired[Optional[str]]

    class ModifyParamsPaymentMethodDataAuBecsDebit(TypedDict):
        account_number: str
        bsb_number: str

    class ModifyParamsPaymentMethodDataAlipay(TypedDict):
        pass

    class ModifyParamsPaymentMethodDataAfterpayClearpay(TypedDict):
        pass

    class ModifyParamsPaymentMethodDataAffirm(TypedDict):
        pass

    class ModifyParamsPaymentMethodDataAcssDebit(TypedDict):
        account_number: str
        institution_number: str
        transit_number: str

    class RetrieveParams(RequestOptions):
        client_secret: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]

    class VerifyMicrodepositsParams(RequestOptions):
        amounts: NotRequired[Optional[List[int]]]
        descriptor_code: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]

    class SearchParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        page: NotRequired[Optional[str]]
        query: str

    amount: int
    amount_capturable: int
    amount_details: Optional[StripeObject]
    amount_received: int
    application: Optional[ExpandableField["Application"]]
    application_fee_amount: Optional[int]
    automatic_payment_methods: Optional[StripeObject]
    canceled_at: Optional[int]
    cancellation_reason: Optional[
        Literal[
            "abandoned",
            "automatic",
            "duplicate",
            "failed_invoice",
            "fraudulent",
            "requested_by_customer",
            "void_invoice",
        ]
    ]
    capture_method: Literal["automatic", "automatic_async", "manual"]
    client_secret: Optional[str]
    confirmation_method: Literal["automatic", "manual"]
    created: int
    currency: str
    customer: Optional[ExpandableField["Customer"]]
    description: Optional[str]
    id: str
    invoice: Optional[ExpandableField["Invoice"]]
    last_payment_error: Optional[StripeObject]
    latest_charge: Optional[ExpandableField["Charge"]]
    livemode: bool
    metadata: Dict[str, str]
    next_action: Optional[StripeObject]
    object: Literal["payment_intent"]
    on_behalf_of: Optional[ExpandableField["Account"]]
    payment_method: Optional[ExpandableField["PaymentMethod"]]
    payment_method_configuration_details: Optional[StripeObject]
    payment_method_options: Optional[StripeObject]
    payment_method_types: List[str]
    processing: Optional[StripeObject]
    receipt_email: Optional[str]
    review: Optional[ExpandableField["Review"]]
    setup_future_usage: Optional[Literal["off_session", "on_session"]]
    shipping: Optional[StripeObject]
    source: Optional[ExpandableField[Any]]
    statement_descriptor: Optional[str]
    statement_descriptor_suffix: Optional[str]
    status: Literal[
        "canceled",
        "processing",
        "requires_action",
        "requires_capture",
        "requires_confirmation",
        "requires_payment_method",
        "succeeded",
    ]
    transfer_data: Optional[StripeObject]
    transfer_group: Optional[str]

    @classmethod
    def _cls_apply_customer_balance(
        cls,
        intent: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["PaymentIntent.ApplyCustomerBalanceParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/payment_intents/{intent}/apply_customer_balance".format(
                intent=util.sanitize_id(intent)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_apply_customer_balance")
    def apply_customer_balance(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["PaymentIntent.ApplyCustomerBalanceParams"]
    ):
        return self._request(
            "post",
            "/v1/payment_intents/{intent}/apply_customer_balance".format(
                intent=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_cancel(
        cls,
        intent: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["PaymentIntent.CancelParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/payment_intents/{intent}/cancel".format(
                intent=util.sanitize_id(intent)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_cancel")
    def cancel(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["PaymentIntent.CancelParams"]
    ):
        return self._request(
            "post",
            "/v1/payment_intents/{intent}/cancel".format(
                intent=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_capture(
        cls,
        intent: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["PaymentIntent.CaptureParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/payment_intents/{intent}/capture".format(
                intent=util.sanitize_id(intent)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_capture")
    def capture(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["PaymentIntent.CaptureParams"]
    ):
        return self._request(
            "post",
            "/v1/payment_intents/{intent}/capture".format(
                intent=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_confirm(
        cls,
        intent: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["PaymentIntent.ConfirmParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/payment_intents/{intent}/confirm".format(
                intent=util.sanitize_id(intent)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_confirm")
    def confirm(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["PaymentIntent.ConfirmParams"]
    ):
        return self._request(
            "post",
            "/v1/payment_intents/{intent}/confirm".format(
                intent=util.sanitize_id(self.get("id"))
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
        **params: Unpack["PaymentIntent.CreateParams"]
    ) -> "PaymentIntent":
        return cast(
            "PaymentIntent",
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
    def _cls_increment_authorization(
        cls,
        intent: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["PaymentIntent.IncrementAuthorizationParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/payment_intents/{intent}/increment_authorization".format(
                intent=util.sanitize_id(intent)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_increment_authorization")
    def increment_authorization(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["PaymentIntent.IncrementAuthorizationParams"]
    ):
        return self._request(
            "post",
            "/v1/payment_intents/{intent}/increment_authorization".format(
                intent=util.sanitize_id(self.get("id"))
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
        **params: Unpack["PaymentIntent.ListParams"]
    ) -> ListObject["PaymentIntent"]:
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
        cls, id, **params: Unpack["PaymentIntent.ModifyParams"]
    ) -> "PaymentIntent":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "PaymentIntent",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["PaymentIntent.RetrieveParams"]
    ) -> "PaymentIntent":
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    def _cls_verify_microdeposits(
        cls,
        intent: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["PaymentIntent.VerifyMicrodepositsParams"]
    ):
        return cls._static_request(
            "post",
            "/v1/payment_intents/{intent}/verify_microdeposits".format(
                intent=util.sanitize_id(intent)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_verify_microdeposits")
    def verify_microdeposits(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["PaymentIntent.VerifyMicrodepositsParams"]
    ):
        return self._request(
            "post",
            "/v1/payment_intents/{intent}/verify_microdeposits".format(
                intent=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def search(
        cls, *args, **kwargs: Unpack["PaymentIntent.SearchParams"]
    ) -> SearchResultObject["PaymentIntent"]:
        return cls._search(
            search_url="/v1/payment_intents/search", *args, **kwargs
        )

    @classmethod
    def search_auto_paging_iter(cls, *args, **kwargs):
        return cls.search(*args, **kwargs).auto_paging_iter()
