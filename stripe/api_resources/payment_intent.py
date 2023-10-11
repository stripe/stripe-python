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
            Optional["PaymentIntent.CaptureTransferDataParams"]
        ]

    class CaptureTransferDataParams(TypedDict):
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
                        "PaymentIntent.ConfirmMandateDataParams",
                        "PaymentIntent.ConfirmMandateDataParams",
                    ],
                ]
            ]
        ]
        off_session: NotRequired[
            Optional[Union[bool, Literal["one_off", "recurring"]]]
        ]
        payment_method: NotRequired[Optional[str]]
        payment_method_data: NotRequired[
            Optional["PaymentIntent.ConfirmPaymentMethodDataParams"]
        ]
        payment_method_options: NotRequired[
            Optional["PaymentIntent.ConfirmPaymentMethodOptionsParams"]
        ]
        radar_options: NotRequired[
            Optional["PaymentIntent.ConfirmRadarOptionsParams"]
        ]
        receipt_email: NotRequired[Optional[Union[Literal[""], str]]]
        return_url: NotRequired[Optional[str]]
        setup_future_usage: NotRequired[
            Optional[Union[Literal[""], Literal["off_session", "on_session"]]]
        ]
        shipping: NotRequired[
            Optional[Union[Literal[""], "PaymentIntent.ConfirmShippingParams"]]
        ]
        use_stripe_sdk: NotRequired[Optional[bool]]

    class ConfirmShippingParams(TypedDict):
        address: "PaymentIntent.ConfirmShippingAddressParams"
        carrier: NotRequired[Optional[str]]
        name: str
        phone: NotRequired[Optional[str]]
        tracking_number: NotRequired[Optional[str]]

    class ConfirmShippingAddressParams(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class ConfirmRadarOptionsParams(TypedDict):
        session: NotRequired[Optional[str]]

    class ConfirmPaymentMethodOptionsParams(TypedDict):
        acss_debit: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmPaymentMethodOptionsAcssDebitParams",
                ]
            ]
        ]
        affirm: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmPaymentMethodOptionsAffirmParams",
                ]
            ]
        ]
        afterpay_clearpay: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmPaymentMethodOptionsAfterpayClearpayParams",
                ]
            ]
        ]
        alipay: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmPaymentMethodOptionsAlipayParams",
                ]
            ]
        ]
        au_becs_debit: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmPaymentMethodOptionsAuBecsDebitParams",
                ]
            ]
        ]
        bacs_debit: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmPaymentMethodOptionsBacsDebitParams",
                ]
            ]
        ]
        bancontact: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmPaymentMethodOptionsBancontactParams",
                ]
            ]
        ]
        blik: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmPaymentMethodOptionsBlikParams",
                ]
            ]
        ]
        boleto: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmPaymentMethodOptionsBoletoParams",
                ]
            ]
        ]
        card: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmPaymentMethodOptionsCardParams",
                ]
            ]
        ]
        card_present: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmPaymentMethodOptionsCardPresentParams",
                ]
            ]
        ]
        cashapp: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmPaymentMethodOptionsCashappParams",
                ]
            ]
        ]
        customer_balance: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmPaymentMethodOptionsCustomerBalanceParams",
                ]
            ]
        ]
        eps: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmPaymentMethodOptionsEpsParams",
                ]
            ]
        ]
        fpx: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmPaymentMethodOptionsFpxParams",
                ]
            ]
        ]
        giropay: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmPaymentMethodOptionsGiropayParams",
                ]
            ]
        ]
        grabpay: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmPaymentMethodOptionsGrabpayParams",
                ]
            ]
        ]
        ideal: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmPaymentMethodOptionsIdealParams",
                ]
            ]
        ]
        interac_present: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmPaymentMethodOptionsInteracPresentParams",
                ]
            ]
        ]
        klarna: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmPaymentMethodOptionsKlarnaParams",
                ]
            ]
        ]
        konbini: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmPaymentMethodOptionsKonbiniParams",
                ]
            ]
        ]
        link: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmPaymentMethodOptionsLinkParams",
                ]
            ]
        ]
        oxxo: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmPaymentMethodOptionsOxxoParams",
                ]
            ]
        ]
        p24: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmPaymentMethodOptionsP24Params",
                ]
            ]
        ]
        paynow: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmPaymentMethodOptionsPaynowParams",
                ]
            ]
        ]
        paypal: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmPaymentMethodOptionsPaypalParams",
                ]
            ]
        ]
        pix: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmPaymentMethodOptionsPixParams",
                ]
            ]
        ]
        promptpay: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmPaymentMethodOptionsPromptpayParams",
                ]
            ]
        ]
        sepa_debit: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmPaymentMethodOptionsSepaDebitParams",
                ]
            ]
        ]
        sofort: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmPaymentMethodOptionsSofortParams",
                ]
            ]
        ]
        us_bank_account: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmPaymentMethodOptionsUsBankAccountParams",
                ]
            ]
        ]
        wechat_pay: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmPaymentMethodOptionsWechatPayParams",
                ]
            ]
        ]
        zip: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmPaymentMethodOptionsZipParams",
                ]
            ]
        ]

    class ConfirmPaymentMethodOptionsZipParams(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ConfirmPaymentMethodOptionsWechatPayParams(TypedDict):
        app_id: NotRequired[Optional[str]]
        client: Literal["android", "ios", "web"]
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ConfirmPaymentMethodOptionsUsBankAccountParams(TypedDict):
        financial_connections: NotRequired[
            Optional[
                "PaymentIntent.ConfirmPaymentMethodOptionsUsBankAccountFinancialConnectionsParams"
            ]
        ]
        networks: NotRequired[
            Optional[
                "PaymentIntent.ConfirmPaymentMethodOptionsUsBankAccountNetworksParams"
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

    class ConfirmPaymentMethodOptionsUsBankAccountNetworksParams(TypedDict):
        requested: NotRequired[
            Optional[List[Literal["ach", "us_domestic_wire"]]]
        ]

    class ConfirmPaymentMethodOptionsUsBankAccountFinancialConnectionsParams(
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

    class ConfirmPaymentMethodOptionsSofortParams(TypedDict):
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

    class ConfirmPaymentMethodOptionsSepaDebitParams(TypedDict):
        mandate_options: NotRequired[
            Optional[
                "PaymentIntent.ConfirmPaymentMethodOptionsSepaDebitMandateOptionsParams"
            ]
        ]
        setup_future_usage: NotRequired[
            Optional[
                Union[
                    Literal[""], Literal["none", "off_session", "on_session"]
                ]
            ]
        ]

    class ConfirmPaymentMethodOptionsSepaDebitMandateOptionsParams(TypedDict):
        pass

    class ConfirmPaymentMethodOptionsPromptpayParams(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ConfirmPaymentMethodOptionsPixParams(TypedDict):
        expires_after_seconds: NotRequired[Optional[int]]
        expires_at: NotRequired[Optional[int]]
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ConfirmPaymentMethodOptionsPaypalParams(TypedDict):
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

    class ConfirmPaymentMethodOptionsPaynowParams(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ConfirmPaymentMethodOptionsP24Params(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]
        tos_shown_and_accepted: NotRequired[Optional[bool]]

    class ConfirmPaymentMethodOptionsOxxoParams(TypedDict):
        expires_after_days: NotRequired[Optional[int]]
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ConfirmPaymentMethodOptionsLinkParams(TypedDict):
        capture_method: NotRequired[
            Optional[Union[Literal[""], Literal["manual"]]]
        ]
        persistent_token: NotRequired[Optional[str]]
        setup_future_usage: NotRequired[
            Optional[Union[Literal[""], Literal["none", "off_session"]]]
        ]

    class ConfirmPaymentMethodOptionsKonbiniParams(TypedDict):
        confirmation_number: NotRequired[Optional[Union[Literal[""], str]]]
        expires_after_days: NotRequired[Optional[Union[Literal[""], int]]]
        expires_at: NotRequired[Optional[Union[Literal[""], int]]]
        product_description: NotRequired[Optional[Union[Literal[""], str]]]
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ConfirmPaymentMethodOptionsKlarnaParams(TypedDict):
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

    class ConfirmPaymentMethodOptionsInteracPresentParams(TypedDict):
        pass

    class ConfirmPaymentMethodOptionsIdealParams(TypedDict):
        setup_future_usage: NotRequired[
            Optional[Union[Literal[""], Literal["none", "off_session"]]]
        ]

    class ConfirmPaymentMethodOptionsGrabpayParams(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ConfirmPaymentMethodOptionsGiropayParams(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ConfirmPaymentMethodOptionsFpxParams(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ConfirmPaymentMethodOptionsEpsParams(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ConfirmPaymentMethodOptionsCustomerBalanceParams(TypedDict):
        bank_transfer: NotRequired[
            Optional[
                "PaymentIntent.ConfirmPaymentMethodOptionsCustomerBalanceBankTransferParams"
            ]
        ]
        funding_type: NotRequired[Optional[Literal["bank_transfer"]]]
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ConfirmPaymentMethodOptionsCustomerBalanceBankTransferParams(
        TypedDict,
    ):
        eu_bank_transfer: NotRequired[
            Optional[
                "PaymentIntent.ConfirmPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransferParams"
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

    class ConfirmPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransferParams(
        TypedDict,
    ):
        country: str

    class ConfirmPaymentMethodOptionsCashappParams(TypedDict):
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

    class ConfirmPaymentMethodOptionsCardPresentParams(TypedDict):
        request_extended_authorization: NotRequired[Optional[bool]]
        request_incremental_authorization: NotRequired[
            Optional[Literal["if_available", "never"]]
        ]
        request_incremental_authorization_support: NotRequired[Optional[bool]]

    class ConfirmPaymentMethodOptionsCardParams(TypedDict):
        capture_method: NotRequired[
            Optional[Union[Literal[""], Literal["manual"]]]
        ]
        cvc_token: NotRequired[Optional[str]]
        installments: NotRequired[
            Optional[
                "PaymentIntent.ConfirmPaymentMethodOptionsCardInstallmentsParams"
            ]
        ]
        mandate_options: NotRequired[
            Optional[
                "PaymentIntent.ConfirmPaymentMethodOptionsCardMandateOptionsParams"
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

    class ConfirmPaymentMethodOptionsCardMandateOptionsParams(TypedDict):
        amount: int
        amount_type: Literal["fixed", "maximum"]
        description: NotRequired[Optional[str]]
        end_date: NotRequired[Optional[int]]
        interval: Literal["day", "month", "sporadic", "week", "year"]
        interval_count: NotRequired[Optional[int]]
        reference: str
        start_date: int
        supported_types: NotRequired[Optional[List[Literal["india"]]]]

    class ConfirmPaymentMethodOptionsCardInstallmentsParams(TypedDict):
        enabled: NotRequired[Optional[bool]]
        plan: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmPaymentMethodOptionsCardInstallmentsPlanParams",
                ]
            ]
        ]

    class ConfirmPaymentMethodOptionsCardInstallmentsPlanParams(TypedDict):
        count: int
        interval: Literal["month"]
        type: Literal["fixed_count"]

    class ConfirmPaymentMethodOptionsBoletoParams(TypedDict):
        expires_after_days: NotRequired[Optional[int]]
        setup_future_usage: NotRequired[
            Optional[
                Union[
                    Literal[""], Literal["none", "off_session", "on_session"]
                ]
            ]
        ]

    class ConfirmPaymentMethodOptionsBlikParams(TypedDict):
        code: NotRequired[Optional[str]]

    class ConfirmPaymentMethodOptionsBancontactParams(TypedDict):
        preferred_language: NotRequired[
            Optional[Literal["de", "en", "fr", "nl"]]
        ]
        setup_future_usage: NotRequired[
            Optional[Union[Literal[""], Literal["none", "off_session"]]]
        ]

    class ConfirmPaymentMethodOptionsBacsDebitParams(TypedDict):
        setup_future_usage: NotRequired[
            Optional[
                Union[
                    Literal[""], Literal["none", "off_session", "on_session"]
                ]
            ]
        ]

    class ConfirmPaymentMethodOptionsAuBecsDebitParams(TypedDict):
        setup_future_usage: NotRequired[
            Optional[
                Union[
                    Literal[""], Literal["none", "off_session", "on_session"]
                ]
            ]
        ]

    class ConfirmPaymentMethodOptionsAlipayParams(TypedDict):
        setup_future_usage: NotRequired[
            Optional[Union[Literal[""], Literal["none", "off_session"]]]
        ]

    class ConfirmPaymentMethodOptionsAfterpayClearpayParams(TypedDict):
        capture_method: NotRequired[
            Optional[Union[Literal[""], Literal["manual"]]]
        ]
        reference: NotRequired[Optional[str]]
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ConfirmPaymentMethodOptionsAffirmParams(TypedDict):
        capture_method: NotRequired[
            Optional[Union[Literal[""], Literal["manual"]]]
        ]
        preferred_locale: NotRequired[Optional[str]]
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ConfirmPaymentMethodOptionsAcssDebitParams(TypedDict):
        mandate_options: NotRequired[
            Optional[
                "PaymentIntent.ConfirmPaymentMethodOptionsAcssDebitMandateOptionsParams"
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

    class ConfirmPaymentMethodOptionsAcssDebitMandateOptionsParams(TypedDict):
        custom_mandate_url: NotRequired[Optional[Union[Literal[""], str]]]
        interval_description: NotRequired[Optional[str]]
        payment_schedule: NotRequired[
            Optional[Literal["combined", "interval", "sporadic"]]
        ]
        transaction_type: NotRequired[
            Optional[Literal["business", "personal"]]
        ]

    class ConfirmPaymentMethodDataParams(TypedDict):
        acss_debit: NotRequired[
            Optional["PaymentIntent.ConfirmPaymentMethodDataAcssDebitParams"]
        ]
        affirm: NotRequired[
            Optional["PaymentIntent.ConfirmPaymentMethodDataAffirmParams"]
        ]
        afterpay_clearpay: NotRequired[
            Optional[
                "PaymentIntent.ConfirmPaymentMethodDataAfterpayClearpayParams"
            ]
        ]
        alipay: NotRequired[
            Optional["PaymentIntent.ConfirmPaymentMethodDataAlipayParams"]
        ]
        au_becs_debit: NotRequired[
            Optional["PaymentIntent.ConfirmPaymentMethodDataAuBecsDebitParams"]
        ]
        bacs_debit: NotRequired[
            Optional["PaymentIntent.ConfirmPaymentMethodDataBacsDebitParams"]
        ]
        bancontact: NotRequired[
            Optional["PaymentIntent.ConfirmPaymentMethodDataBancontactParams"]
        ]
        billing_details: NotRequired[
            Optional[
                "PaymentIntent.ConfirmPaymentMethodDataBillingDetailsParams"
            ]
        ]
        blik: NotRequired[
            Optional["PaymentIntent.ConfirmPaymentMethodDataBlikParams"]
        ]
        boleto: NotRequired[
            Optional["PaymentIntent.ConfirmPaymentMethodDataBoletoParams"]
        ]
        cashapp: NotRequired[
            Optional["PaymentIntent.ConfirmPaymentMethodDataCashappParams"]
        ]
        customer_balance: NotRequired[
            Optional[
                "PaymentIntent.ConfirmPaymentMethodDataCustomerBalanceParams"
            ]
        ]
        eps: NotRequired[
            Optional["PaymentIntent.ConfirmPaymentMethodDataEpsParams"]
        ]
        fpx: NotRequired[
            Optional["PaymentIntent.ConfirmPaymentMethodDataFpxParams"]
        ]
        giropay: NotRequired[
            Optional["PaymentIntent.ConfirmPaymentMethodDataGiropayParams"]
        ]
        grabpay: NotRequired[
            Optional["PaymentIntent.ConfirmPaymentMethodDataGrabpayParams"]
        ]
        ideal: NotRequired[
            Optional["PaymentIntent.ConfirmPaymentMethodDataIdealParams"]
        ]
        interac_present: NotRequired[
            Optional[
                "PaymentIntent.ConfirmPaymentMethodDataInteracPresentParams"
            ]
        ]
        klarna: NotRequired[
            Optional["PaymentIntent.ConfirmPaymentMethodDataKlarnaParams"]
        ]
        konbini: NotRequired[
            Optional["PaymentIntent.ConfirmPaymentMethodDataKonbiniParams"]
        ]
        link: NotRequired[
            Optional["PaymentIntent.ConfirmPaymentMethodDataLinkParams"]
        ]
        metadata: NotRequired[Optional[Dict[str, str]]]
        oxxo: NotRequired[
            Optional["PaymentIntent.ConfirmPaymentMethodDataOxxoParams"]
        ]
        p24: NotRequired[
            Optional["PaymentIntent.ConfirmPaymentMethodDataP24Params"]
        ]
        paynow: NotRequired[
            Optional["PaymentIntent.ConfirmPaymentMethodDataPaynowParams"]
        ]
        paypal: NotRequired[
            Optional["PaymentIntent.ConfirmPaymentMethodDataPaypalParams"]
        ]
        pix: NotRequired[
            Optional["PaymentIntent.ConfirmPaymentMethodDataPixParams"]
        ]
        promptpay: NotRequired[
            Optional["PaymentIntent.ConfirmPaymentMethodDataPromptpayParams"]
        ]
        radar_options: NotRequired[
            Optional[
                "PaymentIntent.ConfirmPaymentMethodDataRadarOptionsParams"
            ]
        ]
        sepa_debit: NotRequired[
            Optional["PaymentIntent.ConfirmPaymentMethodDataSepaDebitParams"]
        ]
        sofort: NotRequired[
            Optional["PaymentIntent.ConfirmPaymentMethodDataSofortParams"]
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
                "PaymentIntent.ConfirmPaymentMethodDataUsBankAccountParams"
            ]
        ]
        wechat_pay: NotRequired[
            Optional["PaymentIntent.ConfirmPaymentMethodDataWechatPayParams"]
        ]
        zip: NotRequired[
            Optional["PaymentIntent.ConfirmPaymentMethodDataZipParams"]
        ]

    class ConfirmPaymentMethodDataZipParams(TypedDict):
        pass

    class ConfirmPaymentMethodDataWechatPayParams(TypedDict):
        pass

    class ConfirmPaymentMethodDataUsBankAccountParams(TypedDict):
        account_holder_type: NotRequired[
            Optional[Literal["company", "individual"]]
        ]
        account_number: NotRequired[Optional[str]]
        account_type: NotRequired[Optional[Literal["checking", "savings"]]]
        financial_connections_account: NotRequired[Optional[str]]
        routing_number: NotRequired[Optional[str]]

    class ConfirmPaymentMethodDataSofortParams(TypedDict):
        country: Literal["AT", "BE", "DE", "ES", "IT", "NL"]

    class ConfirmPaymentMethodDataSepaDebitParams(TypedDict):
        iban: str

    class ConfirmPaymentMethodDataRadarOptionsParams(TypedDict):
        session: NotRequired[Optional[str]]

    class ConfirmPaymentMethodDataPromptpayParams(TypedDict):
        pass

    class ConfirmPaymentMethodDataPixParams(TypedDict):
        pass

    class ConfirmPaymentMethodDataPaypalParams(TypedDict):
        pass

    class ConfirmPaymentMethodDataPaynowParams(TypedDict):
        pass

    class ConfirmPaymentMethodDataP24Params(TypedDict):
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

    class ConfirmPaymentMethodDataOxxoParams(TypedDict):
        pass

    class ConfirmPaymentMethodDataLinkParams(TypedDict):
        pass

    class ConfirmPaymentMethodDataKonbiniParams(TypedDict):
        pass

    class ConfirmPaymentMethodDataKlarnaParams(TypedDict):
        dob: NotRequired[
            Optional["PaymentIntent.ConfirmPaymentMethodDataKlarnaDobParams"]
        ]

    class ConfirmPaymentMethodDataKlarnaDobParams(TypedDict):
        day: int
        month: int
        year: int

    class ConfirmPaymentMethodDataInteracPresentParams(TypedDict):
        pass

    class ConfirmPaymentMethodDataIdealParams(TypedDict):
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

    class ConfirmPaymentMethodDataGrabpayParams(TypedDict):
        pass

    class ConfirmPaymentMethodDataGiropayParams(TypedDict):
        pass

    class ConfirmPaymentMethodDataFpxParams(TypedDict):
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

    class ConfirmPaymentMethodDataEpsParams(TypedDict):
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

    class ConfirmPaymentMethodDataCustomerBalanceParams(TypedDict):
        pass

    class ConfirmPaymentMethodDataCashappParams(TypedDict):
        pass

    class ConfirmPaymentMethodDataBoletoParams(TypedDict):
        tax_id: str

    class ConfirmPaymentMethodDataBlikParams(TypedDict):
        pass

    class ConfirmPaymentMethodDataBillingDetailsParams(TypedDict):
        address: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ConfirmPaymentMethodDataBillingDetailsAddressParams",
                ]
            ]
        ]
        email: NotRequired[Optional[Union[Literal[""], str]]]
        name: NotRequired[Optional[Union[Literal[""], str]]]
        phone: NotRequired[Optional[Union[Literal[""], str]]]

    class ConfirmPaymentMethodDataBillingDetailsAddressParams(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class ConfirmPaymentMethodDataBancontactParams(TypedDict):
        pass

    class ConfirmPaymentMethodDataBacsDebitParams(TypedDict):
        account_number: NotRequired[Optional[str]]
        sort_code: NotRequired[Optional[str]]

    class ConfirmPaymentMethodDataAuBecsDebitParams(TypedDict):
        account_number: str
        bsb_number: str

    class ConfirmPaymentMethodDataAlipayParams(TypedDict):
        pass

    class ConfirmPaymentMethodDataAfterpayClearpayParams(TypedDict):
        pass

    class ConfirmPaymentMethodDataAffirmParams(TypedDict):
        pass

    class ConfirmPaymentMethodDataAcssDebitParams(TypedDict):
        account_number: str
        institution_number: str
        transit_number: str

    class ConfirmMandateDataParams(TypedDict):
        customer_acceptance: "PaymentIntent.ConfirmMandateDataCustomerAcceptanceParams"

    class ConfirmMandateDataCustomerAcceptanceParams(TypedDict):
        online: "PaymentIntent.ConfirmMandateDataCustomerAcceptanceOnlineParams"
        type: Literal["online"]

    class ConfirmMandateDataCustomerAcceptanceOnlineParams(TypedDict):
        ip_address: NotRequired[Optional[str]]
        user_agent: NotRequired[Optional[str]]

    class CreateParams(RequestOptions):
        amount: int
        application_fee_amount: NotRequired[Optional[int]]
        automatic_payment_methods: NotRequired[
            Optional["PaymentIntent.CreateAutomaticPaymentMethodsParams"]
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
                Union[Literal[""], "PaymentIntent.CreateMandateDataParams"]
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
            Optional["PaymentIntent.CreatePaymentMethodDataParams"]
        ]
        payment_method_options: NotRequired[
            Optional["PaymentIntent.CreatePaymentMethodOptionsParams"]
        ]
        payment_method_types: NotRequired[Optional[List[str]]]
        radar_options: NotRequired[
            Optional["PaymentIntent.CreateRadarOptionsParams"]
        ]
        receipt_email: NotRequired[Optional[str]]
        return_url: NotRequired[Optional[str]]
        setup_future_usage: NotRequired[
            Optional[Literal["off_session", "on_session"]]
        ]
        shipping: NotRequired[Optional["PaymentIntent.CreateShippingParams"]]
        statement_descriptor: NotRequired[Optional[str]]
        statement_descriptor_suffix: NotRequired[Optional[str]]
        transfer_data: NotRequired[
            Optional["PaymentIntent.CreateTransferDataParams"]
        ]
        transfer_group: NotRequired[Optional[str]]
        use_stripe_sdk: NotRequired[Optional[bool]]

    class CreateTransferDataParams(TypedDict):
        amount: NotRequired[Optional[int]]
        destination: str

    class CreateShippingParams(TypedDict):
        address: "PaymentIntent.CreateShippingAddressParams"
        carrier: NotRequired[Optional[str]]
        name: str
        phone: NotRequired[Optional[str]]
        tracking_number: NotRequired[Optional[str]]

    class CreateShippingAddressParams(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class CreateRadarOptionsParams(TypedDict):
        session: NotRequired[Optional[str]]

    class CreatePaymentMethodOptionsParams(TypedDict):
        acss_debit: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreatePaymentMethodOptionsAcssDebitParams",
                ]
            ]
        ]
        affirm: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreatePaymentMethodOptionsAffirmParams",
                ]
            ]
        ]
        afterpay_clearpay: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreatePaymentMethodOptionsAfterpayClearpayParams",
                ]
            ]
        ]
        alipay: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreatePaymentMethodOptionsAlipayParams",
                ]
            ]
        ]
        au_becs_debit: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreatePaymentMethodOptionsAuBecsDebitParams",
                ]
            ]
        ]
        bacs_debit: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreatePaymentMethodOptionsBacsDebitParams",
                ]
            ]
        ]
        bancontact: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreatePaymentMethodOptionsBancontactParams",
                ]
            ]
        ]
        blik: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreatePaymentMethodOptionsBlikParams",
                ]
            ]
        ]
        boleto: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreatePaymentMethodOptionsBoletoParams",
                ]
            ]
        ]
        card: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreatePaymentMethodOptionsCardParams",
                ]
            ]
        ]
        card_present: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreatePaymentMethodOptionsCardPresentParams",
                ]
            ]
        ]
        cashapp: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreatePaymentMethodOptionsCashappParams",
                ]
            ]
        ]
        customer_balance: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreatePaymentMethodOptionsCustomerBalanceParams",
                ]
            ]
        ]
        eps: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreatePaymentMethodOptionsEpsParams",
                ]
            ]
        ]
        fpx: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreatePaymentMethodOptionsFpxParams",
                ]
            ]
        ]
        giropay: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreatePaymentMethodOptionsGiropayParams",
                ]
            ]
        ]
        grabpay: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreatePaymentMethodOptionsGrabpayParams",
                ]
            ]
        ]
        ideal: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreatePaymentMethodOptionsIdealParams",
                ]
            ]
        ]
        interac_present: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreatePaymentMethodOptionsInteracPresentParams",
                ]
            ]
        ]
        klarna: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreatePaymentMethodOptionsKlarnaParams",
                ]
            ]
        ]
        konbini: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreatePaymentMethodOptionsKonbiniParams",
                ]
            ]
        ]
        link: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreatePaymentMethodOptionsLinkParams",
                ]
            ]
        ]
        oxxo: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreatePaymentMethodOptionsOxxoParams",
                ]
            ]
        ]
        p24: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreatePaymentMethodOptionsP24Params",
                ]
            ]
        ]
        paynow: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreatePaymentMethodOptionsPaynowParams",
                ]
            ]
        ]
        paypal: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreatePaymentMethodOptionsPaypalParams",
                ]
            ]
        ]
        pix: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreatePaymentMethodOptionsPixParams",
                ]
            ]
        ]
        promptpay: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreatePaymentMethodOptionsPromptpayParams",
                ]
            ]
        ]
        sepa_debit: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreatePaymentMethodOptionsSepaDebitParams",
                ]
            ]
        ]
        sofort: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreatePaymentMethodOptionsSofortParams",
                ]
            ]
        ]
        us_bank_account: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreatePaymentMethodOptionsUsBankAccountParams",
                ]
            ]
        ]
        wechat_pay: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreatePaymentMethodOptionsWechatPayParams",
                ]
            ]
        ]
        zip: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreatePaymentMethodOptionsZipParams",
                ]
            ]
        ]

    class CreatePaymentMethodOptionsZipParams(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class CreatePaymentMethodOptionsWechatPayParams(TypedDict):
        app_id: NotRequired[Optional[str]]
        client: Literal["android", "ios", "web"]
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class CreatePaymentMethodOptionsUsBankAccountParams(TypedDict):
        financial_connections: NotRequired[
            Optional[
                "PaymentIntent.CreatePaymentMethodOptionsUsBankAccountFinancialConnectionsParams"
            ]
        ]
        networks: NotRequired[
            Optional[
                "PaymentIntent.CreatePaymentMethodOptionsUsBankAccountNetworksParams"
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

    class CreatePaymentMethodOptionsUsBankAccountNetworksParams(TypedDict):
        requested: NotRequired[
            Optional[List[Literal["ach", "us_domestic_wire"]]]
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
        return_url: NotRequired[Optional[str]]

    class CreatePaymentMethodOptionsSofortParams(TypedDict):
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

    class CreatePaymentMethodOptionsSepaDebitParams(TypedDict):
        mandate_options: NotRequired[
            Optional[
                "PaymentIntent.CreatePaymentMethodOptionsSepaDebitMandateOptionsParams"
            ]
        ]
        setup_future_usage: NotRequired[
            Optional[
                Union[
                    Literal[""], Literal["none", "off_session", "on_session"]
                ]
            ]
        ]

    class CreatePaymentMethodOptionsSepaDebitMandateOptionsParams(TypedDict):
        pass

    class CreatePaymentMethodOptionsPromptpayParams(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class CreatePaymentMethodOptionsPixParams(TypedDict):
        expires_after_seconds: NotRequired[Optional[int]]
        expires_at: NotRequired[Optional[int]]
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

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
        capture_method: NotRequired[
            Optional[Union[Literal[""], Literal["manual"]]]
        ]
        persistent_token: NotRequired[Optional[str]]
        setup_future_usage: NotRequired[
            Optional[Union[Literal[""], Literal["none", "off_session"]]]
        ]

    class CreatePaymentMethodOptionsKonbiniParams(TypedDict):
        confirmation_number: NotRequired[Optional[Union[Literal[""], str]]]
        expires_after_days: NotRequired[Optional[Union[Literal[""], int]]]
        expires_at: NotRequired[Optional[Union[Literal[""], int]]]
        product_description: NotRequired[Optional[Union[Literal[""], str]]]
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class CreatePaymentMethodOptionsKlarnaParams(TypedDict):
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

    class CreatePaymentMethodOptionsInteracPresentParams(TypedDict):
        pass

    class CreatePaymentMethodOptionsIdealParams(TypedDict):
        setup_future_usage: NotRequired[
            Optional[Union[Literal[""], Literal["none", "off_session"]]]
        ]

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
                "PaymentIntent.CreatePaymentMethodOptionsCustomerBalanceBankTransferParams"
            ]
        ]
        funding_type: NotRequired[Optional[Literal["bank_transfer"]]]
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class CreatePaymentMethodOptionsCustomerBalanceBankTransferParams(
        TypedDict,
    ):
        eu_bank_transfer: NotRequired[
            Optional[
                "PaymentIntent.CreatePaymentMethodOptionsCustomerBalanceBankTransferEuBankTransferParams"
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

    class CreatePaymentMethodOptionsCardPresentParams(TypedDict):
        request_extended_authorization: NotRequired[Optional[bool]]
        request_incremental_authorization: NotRequired[
            Optional[Literal["if_available", "never"]]
        ]
        request_incremental_authorization_support: NotRequired[Optional[bool]]

    class CreatePaymentMethodOptionsCardParams(TypedDict):
        capture_method: NotRequired[
            Optional[Union[Literal[""], Literal["manual"]]]
        ]
        cvc_token: NotRequired[Optional[str]]
        installments: NotRequired[
            Optional[
                "PaymentIntent.CreatePaymentMethodOptionsCardInstallmentsParams"
            ]
        ]
        mandate_options: NotRequired[
            Optional[
                "PaymentIntent.CreatePaymentMethodOptionsCardMandateOptionsParams"
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

    class CreatePaymentMethodOptionsCardMandateOptionsParams(TypedDict):
        amount: int
        amount_type: Literal["fixed", "maximum"]
        description: NotRequired[Optional[str]]
        end_date: NotRequired[Optional[int]]
        interval: Literal["day", "month", "sporadic", "week", "year"]
        interval_count: NotRequired[Optional[int]]
        reference: str
        start_date: int
        supported_types: NotRequired[Optional[List[Literal["india"]]]]

    class CreatePaymentMethodOptionsCardInstallmentsParams(TypedDict):
        enabled: NotRequired[Optional[bool]]
        plan: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreatePaymentMethodOptionsCardInstallmentsPlanParams",
                ]
            ]
        ]

    class CreatePaymentMethodOptionsCardInstallmentsPlanParams(TypedDict):
        count: int
        interval: Literal["month"]
        type: Literal["fixed_count"]

    class CreatePaymentMethodOptionsBoletoParams(TypedDict):
        expires_after_days: NotRequired[Optional[int]]
        setup_future_usage: NotRequired[
            Optional[
                Union[
                    Literal[""], Literal["none", "off_session", "on_session"]
                ]
            ]
        ]

    class CreatePaymentMethodOptionsBlikParams(TypedDict):
        code: NotRequired[Optional[str]]

    class CreatePaymentMethodOptionsBancontactParams(TypedDict):
        preferred_language: NotRequired[
            Optional[Literal["de", "en", "fr", "nl"]]
        ]
        setup_future_usage: NotRequired[
            Optional[Union[Literal[""], Literal["none", "off_session"]]]
        ]

    class CreatePaymentMethodOptionsBacsDebitParams(TypedDict):
        setup_future_usage: NotRequired[
            Optional[
                Union[
                    Literal[""], Literal["none", "off_session", "on_session"]
                ]
            ]
        ]

    class CreatePaymentMethodOptionsAuBecsDebitParams(TypedDict):
        setup_future_usage: NotRequired[
            Optional[
                Union[
                    Literal[""], Literal["none", "off_session", "on_session"]
                ]
            ]
        ]

    class CreatePaymentMethodOptionsAlipayParams(TypedDict):
        setup_future_usage: NotRequired[
            Optional[Union[Literal[""], Literal["none", "off_session"]]]
        ]

    class CreatePaymentMethodOptionsAfterpayClearpayParams(TypedDict):
        capture_method: NotRequired[
            Optional[Union[Literal[""], Literal["manual"]]]
        ]
        reference: NotRequired[Optional[str]]
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class CreatePaymentMethodOptionsAffirmParams(TypedDict):
        capture_method: NotRequired[
            Optional[Union[Literal[""], Literal["manual"]]]
        ]
        preferred_locale: NotRequired[Optional[str]]
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class CreatePaymentMethodOptionsAcssDebitParams(TypedDict):
        mandate_options: NotRequired[
            Optional[
                "PaymentIntent.CreatePaymentMethodOptionsAcssDebitMandateOptionsParams"
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

    class CreatePaymentMethodOptionsAcssDebitMandateOptionsParams(TypedDict):
        custom_mandate_url: NotRequired[Optional[Union[Literal[""], str]]]
        interval_description: NotRequired[Optional[str]]
        payment_schedule: NotRequired[
            Optional[Literal["combined", "interval", "sporadic"]]
        ]
        transaction_type: NotRequired[
            Optional[Literal["business", "personal"]]
        ]

    class CreatePaymentMethodDataParams(TypedDict):
        acss_debit: NotRequired[
            Optional["PaymentIntent.CreatePaymentMethodDataAcssDebitParams"]
        ]
        affirm: NotRequired[
            Optional["PaymentIntent.CreatePaymentMethodDataAffirmParams"]
        ]
        afterpay_clearpay: NotRequired[
            Optional[
                "PaymentIntent.CreatePaymentMethodDataAfterpayClearpayParams"
            ]
        ]
        alipay: NotRequired[
            Optional["PaymentIntent.CreatePaymentMethodDataAlipayParams"]
        ]
        au_becs_debit: NotRequired[
            Optional["PaymentIntent.CreatePaymentMethodDataAuBecsDebitParams"]
        ]
        bacs_debit: NotRequired[
            Optional["PaymentIntent.CreatePaymentMethodDataBacsDebitParams"]
        ]
        bancontact: NotRequired[
            Optional["PaymentIntent.CreatePaymentMethodDataBancontactParams"]
        ]
        billing_details: NotRequired[
            Optional[
                "PaymentIntent.CreatePaymentMethodDataBillingDetailsParams"
            ]
        ]
        blik: NotRequired[
            Optional["PaymentIntent.CreatePaymentMethodDataBlikParams"]
        ]
        boleto: NotRequired[
            Optional["PaymentIntent.CreatePaymentMethodDataBoletoParams"]
        ]
        cashapp: NotRequired[
            Optional["PaymentIntent.CreatePaymentMethodDataCashappParams"]
        ]
        customer_balance: NotRequired[
            Optional[
                "PaymentIntent.CreatePaymentMethodDataCustomerBalanceParams"
            ]
        ]
        eps: NotRequired[
            Optional["PaymentIntent.CreatePaymentMethodDataEpsParams"]
        ]
        fpx: NotRequired[
            Optional["PaymentIntent.CreatePaymentMethodDataFpxParams"]
        ]
        giropay: NotRequired[
            Optional["PaymentIntent.CreatePaymentMethodDataGiropayParams"]
        ]
        grabpay: NotRequired[
            Optional["PaymentIntent.CreatePaymentMethodDataGrabpayParams"]
        ]
        ideal: NotRequired[
            Optional["PaymentIntent.CreatePaymentMethodDataIdealParams"]
        ]
        interac_present: NotRequired[
            Optional[
                "PaymentIntent.CreatePaymentMethodDataInteracPresentParams"
            ]
        ]
        klarna: NotRequired[
            Optional["PaymentIntent.CreatePaymentMethodDataKlarnaParams"]
        ]
        konbini: NotRequired[
            Optional["PaymentIntent.CreatePaymentMethodDataKonbiniParams"]
        ]
        link: NotRequired[
            Optional["PaymentIntent.CreatePaymentMethodDataLinkParams"]
        ]
        metadata: NotRequired[Optional[Dict[str, str]]]
        oxxo: NotRequired[
            Optional["PaymentIntent.CreatePaymentMethodDataOxxoParams"]
        ]
        p24: NotRequired[
            Optional["PaymentIntent.CreatePaymentMethodDataP24Params"]
        ]
        paynow: NotRequired[
            Optional["PaymentIntent.CreatePaymentMethodDataPaynowParams"]
        ]
        paypal: NotRequired[
            Optional["PaymentIntent.CreatePaymentMethodDataPaypalParams"]
        ]
        pix: NotRequired[
            Optional["PaymentIntent.CreatePaymentMethodDataPixParams"]
        ]
        promptpay: NotRequired[
            Optional["PaymentIntent.CreatePaymentMethodDataPromptpayParams"]
        ]
        radar_options: NotRequired[
            Optional["PaymentIntent.CreatePaymentMethodDataRadarOptionsParams"]
        ]
        sepa_debit: NotRequired[
            Optional["PaymentIntent.CreatePaymentMethodDataSepaDebitParams"]
        ]
        sofort: NotRequired[
            Optional["PaymentIntent.CreatePaymentMethodDataSofortParams"]
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
                "PaymentIntent.CreatePaymentMethodDataUsBankAccountParams"
            ]
        ]
        wechat_pay: NotRequired[
            Optional["PaymentIntent.CreatePaymentMethodDataWechatPayParams"]
        ]
        zip: NotRequired[
            Optional["PaymentIntent.CreatePaymentMethodDataZipParams"]
        ]

    class CreatePaymentMethodDataZipParams(TypedDict):
        pass

    class CreatePaymentMethodDataWechatPayParams(TypedDict):
        pass

    class CreatePaymentMethodDataUsBankAccountParams(TypedDict):
        account_holder_type: NotRequired[
            Optional[Literal["company", "individual"]]
        ]
        account_number: NotRequired[Optional[str]]
        account_type: NotRequired[Optional[Literal["checking", "savings"]]]
        financial_connections_account: NotRequired[Optional[str]]
        routing_number: NotRequired[Optional[str]]

    class CreatePaymentMethodDataSofortParams(TypedDict):
        country: Literal["AT", "BE", "DE", "ES", "IT", "NL"]

    class CreatePaymentMethodDataSepaDebitParams(TypedDict):
        iban: str

    class CreatePaymentMethodDataRadarOptionsParams(TypedDict):
        session: NotRequired[Optional[str]]

    class CreatePaymentMethodDataPromptpayParams(TypedDict):
        pass

    class CreatePaymentMethodDataPixParams(TypedDict):
        pass

    class CreatePaymentMethodDataPaypalParams(TypedDict):
        pass

    class CreatePaymentMethodDataPaynowParams(TypedDict):
        pass

    class CreatePaymentMethodDataP24Params(TypedDict):
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

    class CreatePaymentMethodDataOxxoParams(TypedDict):
        pass

    class CreatePaymentMethodDataLinkParams(TypedDict):
        pass

    class CreatePaymentMethodDataKonbiniParams(TypedDict):
        pass

    class CreatePaymentMethodDataKlarnaParams(TypedDict):
        dob: NotRequired[
            Optional["PaymentIntent.CreatePaymentMethodDataKlarnaDobParams"]
        ]

    class CreatePaymentMethodDataKlarnaDobParams(TypedDict):
        day: int
        month: int
        year: int

    class CreatePaymentMethodDataInteracPresentParams(TypedDict):
        pass

    class CreatePaymentMethodDataIdealParams(TypedDict):
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

    class CreatePaymentMethodDataGrabpayParams(TypedDict):
        pass

    class CreatePaymentMethodDataGiropayParams(TypedDict):
        pass

    class CreatePaymentMethodDataFpxParams(TypedDict):
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

    class CreatePaymentMethodDataEpsParams(TypedDict):
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

    class CreatePaymentMethodDataCustomerBalanceParams(TypedDict):
        pass

    class CreatePaymentMethodDataCashappParams(TypedDict):
        pass

    class CreatePaymentMethodDataBoletoParams(TypedDict):
        tax_id: str

    class CreatePaymentMethodDataBlikParams(TypedDict):
        pass

    class CreatePaymentMethodDataBillingDetailsParams(TypedDict):
        address: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.CreatePaymentMethodDataBillingDetailsAddressParams",
                ]
            ]
        ]
        email: NotRequired[Optional[Union[Literal[""], str]]]
        name: NotRequired[Optional[Union[Literal[""], str]]]
        phone: NotRequired[Optional[Union[Literal[""], str]]]

    class CreatePaymentMethodDataBillingDetailsAddressParams(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class CreatePaymentMethodDataBancontactParams(TypedDict):
        pass

    class CreatePaymentMethodDataBacsDebitParams(TypedDict):
        account_number: NotRequired[Optional[str]]
        sort_code: NotRequired[Optional[str]]

    class CreatePaymentMethodDataAuBecsDebitParams(TypedDict):
        account_number: str
        bsb_number: str

    class CreatePaymentMethodDataAlipayParams(TypedDict):
        pass

    class CreatePaymentMethodDataAfterpayClearpayParams(TypedDict):
        pass

    class CreatePaymentMethodDataAffirmParams(TypedDict):
        pass

    class CreatePaymentMethodDataAcssDebitParams(TypedDict):
        account_number: str
        institution_number: str
        transit_number: str

    class CreateMandateDataParams(TypedDict):
        customer_acceptance: "PaymentIntent.CreateMandateDataCustomerAcceptanceParams"

    class CreateMandateDataCustomerAcceptanceParams(TypedDict):
        accepted_at: NotRequired[Optional[int]]
        offline: NotRequired[
            Optional[
                "PaymentIntent.CreateMandateDataCustomerAcceptanceOfflineParams"
            ]
        ]
        online: NotRequired[
            Optional[
                "PaymentIntent.CreateMandateDataCustomerAcceptanceOnlineParams"
            ]
        ]
        type: Literal["offline", "online"]

    class CreateMandateDataCustomerAcceptanceOnlineParams(TypedDict):
        ip_address: str
        user_agent: str

    class CreateMandateDataCustomerAcceptanceOfflineParams(TypedDict):
        pass

    class CreateAutomaticPaymentMethodsParams(TypedDict):
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
            Optional["PaymentIntent.IncrementAuthorizationTransferDataParams"]
        ]

    class IncrementAuthorizationTransferDataParams(TypedDict):
        amount: NotRequired[Optional[int]]

    class ListParams(RequestOptions):
        created: NotRequired[
            Optional[Union["PaymentIntent.ListCreatedParams", int]]
        ]
        customer: NotRequired[Optional[str]]
        ending_before: NotRequired[Optional[str]]
        expand: NotRequired[Optional[List[str]]]
        limit: NotRequired[Optional[int]]
        starting_after: NotRequired[Optional[str]]

    class ListCreatedParams(TypedDict):
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
            Optional["PaymentIntent.ModifyPaymentMethodDataParams"]
        ]
        payment_method_options: NotRequired[
            Optional["PaymentIntent.ModifyPaymentMethodOptionsParams"]
        ]
        payment_method_types: NotRequired[Optional[List[str]]]
        receipt_email: NotRequired[Optional[Union[Literal[""], str]]]
        setup_future_usage: NotRequired[
            Optional[Union[Literal[""], Literal["off_session", "on_session"]]]
        ]
        shipping: NotRequired[
            Optional[Union[Literal[""], "PaymentIntent.ModifyShippingParams"]]
        ]
        statement_descriptor: NotRequired[Optional[str]]
        statement_descriptor_suffix: NotRequired[Optional[str]]
        transfer_data: NotRequired[
            Optional["PaymentIntent.ModifyTransferDataParams"]
        ]
        transfer_group: NotRequired[Optional[str]]

    class ModifyTransferDataParams(TypedDict):
        amount: NotRequired[Optional[int]]

    class ModifyShippingParams(TypedDict):
        address: "PaymentIntent.ModifyShippingAddressParams"
        carrier: NotRequired[Optional[str]]
        name: str
        phone: NotRequired[Optional[str]]
        tracking_number: NotRequired[Optional[str]]

    class ModifyShippingAddressParams(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class ModifyPaymentMethodOptionsParams(TypedDict):
        acss_debit: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyPaymentMethodOptionsAcssDebitParams",
                ]
            ]
        ]
        affirm: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyPaymentMethodOptionsAffirmParams",
                ]
            ]
        ]
        afterpay_clearpay: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyPaymentMethodOptionsAfterpayClearpayParams",
                ]
            ]
        ]
        alipay: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyPaymentMethodOptionsAlipayParams",
                ]
            ]
        ]
        au_becs_debit: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyPaymentMethodOptionsAuBecsDebitParams",
                ]
            ]
        ]
        bacs_debit: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyPaymentMethodOptionsBacsDebitParams",
                ]
            ]
        ]
        bancontact: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyPaymentMethodOptionsBancontactParams",
                ]
            ]
        ]
        blik: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyPaymentMethodOptionsBlikParams",
                ]
            ]
        ]
        boleto: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyPaymentMethodOptionsBoletoParams",
                ]
            ]
        ]
        card: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyPaymentMethodOptionsCardParams",
                ]
            ]
        ]
        card_present: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyPaymentMethodOptionsCardPresentParams",
                ]
            ]
        ]
        cashapp: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyPaymentMethodOptionsCashappParams",
                ]
            ]
        ]
        customer_balance: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyPaymentMethodOptionsCustomerBalanceParams",
                ]
            ]
        ]
        eps: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyPaymentMethodOptionsEpsParams",
                ]
            ]
        ]
        fpx: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyPaymentMethodOptionsFpxParams",
                ]
            ]
        ]
        giropay: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyPaymentMethodOptionsGiropayParams",
                ]
            ]
        ]
        grabpay: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyPaymentMethodOptionsGrabpayParams",
                ]
            ]
        ]
        ideal: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyPaymentMethodOptionsIdealParams",
                ]
            ]
        ]
        interac_present: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyPaymentMethodOptionsInteracPresentParams",
                ]
            ]
        ]
        klarna: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyPaymentMethodOptionsKlarnaParams",
                ]
            ]
        ]
        konbini: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyPaymentMethodOptionsKonbiniParams",
                ]
            ]
        ]
        link: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyPaymentMethodOptionsLinkParams",
                ]
            ]
        ]
        oxxo: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyPaymentMethodOptionsOxxoParams",
                ]
            ]
        ]
        p24: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyPaymentMethodOptionsP24Params",
                ]
            ]
        ]
        paynow: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyPaymentMethodOptionsPaynowParams",
                ]
            ]
        ]
        paypal: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyPaymentMethodOptionsPaypalParams",
                ]
            ]
        ]
        pix: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyPaymentMethodOptionsPixParams",
                ]
            ]
        ]
        promptpay: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyPaymentMethodOptionsPromptpayParams",
                ]
            ]
        ]
        sepa_debit: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyPaymentMethodOptionsSepaDebitParams",
                ]
            ]
        ]
        sofort: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyPaymentMethodOptionsSofortParams",
                ]
            ]
        ]
        us_bank_account: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyPaymentMethodOptionsUsBankAccountParams",
                ]
            ]
        ]
        wechat_pay: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyPaymentMethodOptionsWechatPayParams",
                ]
            ]
        ]
        zip: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyPaymentMethodOptionsZipParams",
                ]
            ]
        ]

    class ModifyPaymentMethodOptionsZipParams(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ModifyPaymentMethodOptionsWechatPayParams(TypedDict):
        app_id: NotRequired[Optional[str]]
        client: Literal["android", "ios", "web"]
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ModifyPaymentMethodOptionsUsBankAccountParams(TypedDict):
        financial_connections: NotRequired[
            Optional[
                "PaymentIntent.ModifyPaymentMethodOptionsUsBankAccountFinancialConnectionsParams"
            ]
        ]
        networks: NotRequired[
            Optional[
                "PaymentIntent.ModifyPaymentMethodOptionsUsBankAccountNetworksParams"
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

    class ModifyPaymentMethodOptionsUsBankAccountNetworksParams(TypedDict):
        requested: NotRequired[
            Optional[List[Literal["ach", "us_domestic_wire"]]]
        ]

    class ModifyPaymentMethodOptionsUsBankAccountFinancialConnectionsParams(
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

    class ModifyPaymentMethodOptionsSofortParams(TypedDict):
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

    class ModifyPaymentMethodOptionsSepaDebitParams(TypedDict):
        mandate_options: NotRequired[
            Optional[
                "PaymentIntent.ModifyPaymentMethodOptionsSepaDebitMandateOptionsParams"
            ]
        ]
        setup_future_usage: NotRequired[
            Optional[
                Union[
                    Literal[""], Literal["none", "off_session", "on_session"]
                ]
            ]
        ]

    class ModifyPaymentMethodOptionsSepaDebitMandateOptionsParams(TypedDict):
        pass

    class ModifyPaymentMethodOptionsPromptpayParams(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ModifyPaymentMethodOptionsPixParams(TypedDict):
        expires_after_seconds: NotRequired[Optional[int]]
        expires_at: NotRequired[Optional[int]]
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ModifyPaymentMethodOptionsPaypalParams(TypedDict):
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

    class ModifyPaymentMethodOptionsPaynowParams(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ModifyPaymentMethodOptionsP24Params(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]
        tos_shown_and_accepted: NotRequired[Optional[bool]]

    class ModifyPaymentMethodOptionsOxxoParams(TypedDict):
        expires_after_days: NotRequired[Optional[int]]
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ModifyPaymentMethodOptionsLinkParams(TypedDict):
        capture_method: NotRequired[
            Optional[Union[Literal[""], Literal["manual"]]]
        ]
        persistent_token: NotRequired[Optional[str]]
        setup_future_usage: NotRequired[
            Optional[Union[Literal[""], Literal["none", "off_session"]]]
        ]

    class ModifyPaymentMethodOptionsKonbiniParams(TypedDict):
        confirmation_number: NotRequired[Optional[Union[Literal[""], str]]]
        expires_after_days: NotRequired[Optional[Union[Literal[""], int]]]
        expires_at: NotRequired[Optional[Union[Literal[""], int]]]
        product_description: NotRequired[Optional[Union[Literal[""], str]]]
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ModifyPaymentMethodOptionsKlarnaParams(TypedDict):
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

    class ModifyPaymentMethodOptionsInteracPresentParams(TypedDict):
        pass

    class ModifyPaymentMethodOptionsIdealParams(TypedDict):
        setup_future_usage: NotRequired[
            Optional[Union[Literal[""], Literal["none", "off_session"]]]
        ]

    class ModifyPaymentMethodOptionsGrabpayParams(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ModifyPaymentMethodOptionsGiropayParams(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ModifyPaymentMethodOptionsFpxParams(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ModifyPaymentMethodOptionsEpsParams(TypedDict):
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ModifyPaymentMethodOptionsCustomerBalanceParams(TypedDict):
        bank_transfer: NotRequired[
            Optional[
                "PaymentIntent.ModifyPaymentMethodOptionsCustomerBalanceBankTransferParams"
            ]
        ]
        funding_type: NotRequired[Optional[Literal["bank_transfer"]]]
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ModifyPaymentMethodOptionsCustomerBalanceBankTransferParams(
        TypedDict,
    ):
        eu_bank_transfer: NotRequired[
            Optional[
                "PaymentIntent.ModifyPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransferParams"
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

    class ModifyPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransferParams(
        TypedDict,
    ):
        country: str

    class ModifyPaymentMethodOptionsCashappParams(TypedDict):
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

    class ModifyPaymentMethodOptionsCardPresentParams(TypedDict):
        request_extended_authorization: NotRequired[Optional[bool]]
        request_incremental_authorization: NotRequired[
            Optional[Literal["if_available", "never"]]
        ]
        request_incremental_authorization_support: NotRequired[Optional[bool]]

    class ModifyPaymentMethodOptionsCardParams(TypedDict):
        capture_method: NotRequired[
            Optional[Union[Literal[""], Literal["manual"]]]
        ]
        cvc_token: NotRequired[Optional[str]]
        installments: NotRequired[
            Optional[
                "PaymentIntent.ModifyPaymentMethodOptionsCardInstallmentsParams"
            ]
        ]
        mandate_options: NotRequired[
            Optional[
                "PaymentIntent.ModifyPaymentMethodOptionsCardMandateOptionsParams"
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

    class ModifyPaymentMethodOptionsCardMandateOptionsParams(TypedDict):
        amount: int
        amount_type: Literal["fixed", "maximum"]
        description: NotRequired[Optional[str]]
        end_date: NotRequired[Optional[int]]
        interval: Literal["day", "month", "sporadic", "week", "year"]
        interval_count: NotRequired[Optional[int]]
        reference: str
        start_date: int
        supported_types: NotRequired[Optional[List[Literal["india"]]]]

    class ModifyPaymentMethodOptionsCardInstallmentsParams(TypedDict):
        enabled: NotRequired[Optional[bool]]
        plan: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyPaymentMethodOptionsCardInstallmentsPlanParams",
                ]
            ]
        ]

    class ModifyPaymentMethodOptionsCardInstallmentsPlanParams(TypedDict):
        count: int
        interval: Literal["month"]
        type: Literal["fixed_count"]

    class ModifyPaymentMethodOptionsBoletoParams(TypedDict):
        expires_after_days: NotRequired[Optional[int]]
        setup_future_usage: NotRequired[
            Optional[
                Union[
                    Literal[""], Literal["none", "off_session", "on_session"]
                ]
            ]
        ]

    class ModifyPaymentMethodOptionsBlikParams(TypedDict):
        code: NotRequired[Optional[str]]

    class ModifyPaymentMethodOptionsBancontactParams(TypedDict):
        preferred_language: NotRequired[
            Optional[Literal["de", "en", "fr", "nl"]]
        ]
        setup_future_usage: NotRequired[
            Optional[Union[Literal[""], Literal["none", "off_session"]]]
        ]

    class ModifyPaymentMethodOptionsBacsDebitParams(TypedDict):
        setup_future_usage: NotRequired[
            Optional[
                Union[
                    Literal[""], Literal["none", "off_session", "on_session"]
                ]
            ]
        ]

    class ModifyPaymentMethodOptionsAuBecsDebitParams(TypedDict):
        setup_future_usage: NotRequired[
            Optional[
                Union[
                    Literal[""], Literal["none", "off_session", "on_session"]
                ]
            ]
        ]

    class ModifyPaymentMethodOptionsAlipayParams(TypedDict):
        setup_future_usage: NotRequired[
            Optional[Union[Literal[""], Literal["none", "off_session"]]]
        ]

    class ModifyPaymentMethodOptionsAfterpayClearpayParams(TypedDict):
        capture_method: NotRequired[
            Optional[Union[Literal[""], Literal["manual"]]]
        ]
        reference: NotRequired[Optional[str]]
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ModifyPaymentMethodOptionsAffirmParams(TypedDict):
        capture_method: NotRequired[
            Optional[Union[Literal[""], Literal["manual"]]]
        ]
        preferred_locale: NotRequired[Optional[str]]
        setup_future_usage: NotRequired[Optional[Literal["none"]]]

    class ModifyPaymentMethodOptionsAcssDebitParams(TypedDict):
        mandate_options: NotRequired[
            Optional[
                "PaymentIntent.ModifyPaymentMethodOptionsAcssDebitMandateOptionsParams"
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

    class ModifyPaymentMethodOptionsAcssDebitMandateOptionsParams(TypedDict):
        custom_mandate_url: NotRequired[Optional[Union[Literal[""], str]]]
        interval_description: NotRequired[Optional[str]]
        payment_schedule: NotRequired[
            Optional[Literal["combined", "interval", "sporadic"]]
        ]
        transaction_type: NotRequired[
            Optional[Literal["business", "personal"]]
        ]

    class ModifyPaymentMethodDataParams(TypedDict):
        acss_debit: NotRequired[
            Optional["PaymentIntent.ModifyPaymentMethodDataAcssDebitParams"]
        ]
        affirm: NotRequired[
            Optional["PaymentIntent.ModifyPaymentMethodDataAffirmParams"]
        ]
        afterpay_clearpay: NotRequired[
            Optional[
                "PaymentIntent.ModifyPaymentMethodDataAfterpayClearpayParams"
            ]
        ]
        alipay: NotRequired[
            Optional["PaymentIntent.ModifyPaymentMethodDataAlipayParams"]
        ]
        au_becs_debit: NotRequired[
            Optional["PaymentIntent.ModifyPaymentMethodDataAuBecsDebitParams"]
        ]
        bacs_debit: NotRequired[
            Optional["PaymentIntent.ModifyPaymentMethodDataBacsDebitParams"]
        ]
        bancontact: NotRequired[
            Optional["PaymentIntent.ModifyPaymentMethodDataBancontactParams"]
        ]
        billing_details: NotRequired[
            Optional[
                "PaymentIntent.ModifyPaymentMethodDataBillingDetailsParams"
            ]
        ]
        blik: NotRequired[
            Optional["PaymentIntent.ModifyPaymentMethodDataBlikParams"]
        ]
        boleto: NotRequired[
            Optional["PaymentIntent.ModifyPaymentMethodDataBoletoParams"]
        ]
        cashapp: NotRequired[
            Optional["PaymentIntent.ModifyPaymentMethodDataCashappParams"]
        ]
        customer_balance: NotRequired[
            Optional[
                "PaymentIntent.ModifyPaymentMethodDataCustomerBalanceParams"
            ]
        ]
        eps: NotRequired[
            Optional["PaymentIntent.ModifyPaymentMethodDataEpsParams"]
        ]
        fpx: NotRequired[
            Optional["PaymentIntent.ModifyPaymentMethodDataFpxParams"]
        ]
        giropay: NotRequired[
            Optional["PaymentIntent.ModifyPaymentMethodDataGiropayParams"]
        ]
        grabpay: NotRequired[
            Optional["PaymentIntent.ModifyPaymentMethodDataGrabpayParams"]
        ]
        ideal: NotRequired[
            Optional["PaymentIntent.ModifyPaymentMethodDataIdealParams"]
        ]
        interac_present: NotRequired[
            Optional[
                "PaymentIntent.ModifyPaymentMethodDataInteracPresentParams"
            ]
        ]
        klarna: NotRequired[
            Optional["PaymentIntent.ModifyPaymentMethodDataKlarnaParams"]
        ]
        konbini: NotRequired[
            Optional["PaymentIntent.ModifyPaymentMethodDataKonbiniParams"]
        ]
        link: NotRequired[
            Optional["PaymentIntent.ModifyPaymentMethodDataLinkParams"]
        ]
        metadata: NotRequired[Optional[Dict[str, str]]]
        oxxo: NotRequired[
            Optional["PaymentIntent.ModifyPaymentMethodDataOxxoParams"]
        ]
        p24: NotRequired[
            Optional["PaymentIntent.ModifyPaymentMethodDataP24Params"]
        ]
        paynow: NotRequired[
            Optional["PaymentIntent.ModifyPaymentMethodDataPaynowParams"]
        ]
        paypal: NotRequired[
            Optional["PaymentIntent.ModifyPaymentMethodDataPaypalParams"]
        ]
        pix: NotRequired[
            Optional["PaymentIntent.ModifyPaymentMethodDataPixParams"]
        ]
        promptpay: NotRequired[
            Optional["PaymentIntent.ModifyPaymentMethodDataPromptpayParams"]
        ]
        radar_options: NotRequired[
            Optional["PaymentIntent.ModifyPaymentMethodDataRadarOptionsParams"]
        ]
        sepa_debit: NotRequired[
            Optional["PaymentIntent.ModifyPaymentMethodDataSepaDebitParams"]
        ]
        sofort: NotRequired[
            Optional["PaymentIntent.ModifyPaymentMethodDataSofortParams"]
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
                "PaymentIntent.ModifyPaymentMethodDataUsBankAccountParams"
            ]
        ]
        wechat_pay: NotRequired[
            Optional["PaymentIntent.ModifyPaymentMethodDataWechatPayParams"]
        ]
        zip: NotRequired[
            Optional["PaymentIntent.ModifyPaymentMethodDataZipParams"]
        ]

    class ModifyPaymentMethodDataZipParams(TypedDict):
        pass

    class ModifyPaymentMethodDataWechatPayParams(TypedDict):
        pass

    class ModifyPaymentMethodDataUsBankAccountParams(TypedDict):
        account_holder_type: NotRequired[
            Optional[Literal["company", "individual"]]
        ]
        account_number: NotRequired[Optional[str]]
        account_type: NotRequired[Optional[Literal["checking", "savings"]]]
        financial_connections_account: NotRequired[Optional[str]]
        routing_number: NotRequired[Optional[str]]

    class ModifyPaymentMethodDataSofortParams(TypedDict):
        country: Literal["AT", "BE", "DE", "ES", "IT", "NL"]

    class ModifyPaymentMethodDataSepaDebitParams(TypedDict):
        iban: str

    class ModifyPaymentMethodDataRadarOptionsParams(TypedDict):
        session: NotRequired[Optional[str]]

    class ModifyPaymentMethodDataPromptpayParams(TypedDict):
        pass

    class ModifyPaymentMethodDataPixParams(TypedDict):
        pass

    class ModifyPaymentMethodDataPaypalParams(TypedDict):
        pass

    class ModifyPaymentMethodDataPaynowParams(TypedDict):
        pass

    class ModifyPaymentMethodDataP24Params(TypedDict):
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

    class ModifyPaymentMethodDataOxxoParams(TypedDict):
        pass

    class ModifyPaymentMethodDataLinkParams(TypedDict):
        pass

    class ModifyPaymentMethodDataKonbiniParams(TypedDict):
        pass

    class ModifyPaymentMethodDataKlarnaParams(TypedDict):
        dob: NotRequired[
            Optional["PaymentIntent.ModifyPaymentMethodDataKlarnaDobParams"]
        ]

    class ModifyPaymentMethodDataKlarnaDobParams(TypedDict):
        day: int
        month: int
        year: int

    class ModifyPaymentMethodDataInteracPresentParams(TypedDict):
        pass

    class ModifyPaymentMethodDataIdealParams(TypedDict):
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

    class ModifyPaymentMethodDataGrabpayParams(TypedDict):
        pass

    class ModifyPaymentMethodDataGiropayParams(TypedDict):
        pass

    class ModifyPaymentMethodDataFpxParams(TypedDict):
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

    class ModifyPaymentMethodDataEpsParams(TypedDict):
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

    class ModifyPaymentMethodDataCustomerBalanceParams(TypedDict):
        pass

    class ModifyPaymentMethodDataCashappParams(TypedDict):
        pass

    class ModifyPaymentMethodDataBoletoParams(TypedDict):
        tax_id: str

    class ModifyPaymentMethodDataBlikParams(TypedDict):
        pass

    class ModifyPaymentMethodDataBillingDetailsParams(TypedDict):
        address: NotRequired[
            Optional[
                Union[
                    Literal[""],
                    "PaymentIntent.ModifyPaymentMethodDataBillingDetailsAddressParams",
                ]
            ]
        ]
        email: NotRequired[Optional[Union[Literal[""], str]]]
        name: NotRequired[Optional[Union[Literal[""], str]]]
        phone: NotRequired[Optional[Union[Literal[""], str]]]

    class ModifyPaymentMethodDataBillingDetailsAddressParams(TypedDict):
        city: NotRequired[Optional[str]]
        country: NotRequired[Optional[str]]
        line1: NotRequired[Optional[str]]
        line2: NotRequired[Optional[str]]
        postal_code: NotRequired[Optional[str]]
        state: NotRequired[Optional[str]]

    class ModifyPaymentMethodDataBancontactParams(TypedDict):
        pass

    class ModifyPaymentMethodDataBacsDebitParams(TypedDict):
        account_number: NotRequired[Optional[str]]
        sort_code: NotRequired[Optional[str]]

    class ModifyPaymentMethodDataAuBecsDebitParams(TypedDict):
        account_number: str
        bsb_number: str

    class ModifyPaymentMethodDataAlipayParams(TypedDict):
        pass

    class ModifyPaymentMethodDataAfterpayClearpayParams(TypedDict):
        pass

    class ModifyPaymentMethodDataAffirmParams(TypedDict):
        pass

    class ModifyPaymentMethodDataAcssDebitParams(TypedDict):
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
