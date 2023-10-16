# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
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
from typing import Dict, List, Optional, Union, cast
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
    from stripe.api_resources.bank_account import BankAccount
    from stripe.api_resources.card import Card
    from stripe.api_resources.charge import Charge
    from stripe.api_resources.customer import Customer
    from stripe.api_resources.invoice import Invoice
    from stripe.api_resources.payment_method import PaymentMethod
    from stripe.api_resources.review import Review
    from stripe.api_resources.source import Source


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
    if TYPE_CHECKING:

        class ApplyCustomerBalanceParams(RequestOptions):
            amount: NotRequired["int|None"]
            currency: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]

        class CancelParams(RequestOptions):
            cancellation_reason: NotRequired[
                "Literal['abandoned', 'duplicate', 'fraudulent', 'requested_by_customer']|None"
            ]
            expand: NotRequired["List[str]|None"]

        class CaptureParams(RequestOptions):
            amount_to_capture: NotRequired["int|None"]
            application_fee_amount: NotRequired["int|None"]
            expand: NotRequired["List[str]|None"]
            final_capture: NotRequired["bool|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            statement_descriptor: NotRequired["str|None"]
            statement_descriptor_suffix: NotRequired["str|None"]
            transfer_data: NotRequired[
                "PaymentIntent.CaptureParamsTransferData|None"
            ]

        class CaptureParamsTransferData(TypedDict):
            amount: NotRequired["int|None"]

        class ConfirmParams(RequestOptions):
            capture_method: NotRequired[
                "Literal['automatic', 'automatic_async', 'manual']|None"
            ]
            error_on_requires_action: NotRequired["bool|None"]
            expand: NotRequired["List[str]|None"]
            mandate: NotRequired["str|None"]
            mandate_data: NotRequired[
                "Literal['']|PaymentIntent.ConfirmParamsMandateData|PaymentIntent.ConfirmParamsMandateData2|None"
            ]
            off_session: NotRequired[
                "bool|Literal['one_off', 'recurring']|None"
            ]
            payment_method: NotRequired["str|None"]
            payment_method_data: NotRequired[
                "PaymentIntent.ConfirmParamsPaymentMethodData|None"
            ]
            payment_method_options: NotRequired[
                "PaymentIntent.ConfirmParamsPaymentMethodOptions|None"
            ]
            radar_options: NotRequired[
                "PaymentIntent.ConfirmParamsRadarOptions|None"
            ]
            receipt_email: NotRequired["Literal['']|str|None"]
            return_url: NotRequired["str|None"]
            setup_future_usage: NotRequired[
                "Literal['']|Literal['off_session', 'on_session']|None"
            ]
            shipping: NotRequired[
                "Literal['']|PaymentIntent.ConfirmParamsShipping|None"
            ]
            use_stripe_sdk: NotRequired["bool|None"]

        class ConfirmParamsShipping(TypedDict):
            address: "PaymentIntent.ConfirmParamsShippingAddress"
            carrier: NotRequired["str|None"]
            name: str
            phone: NotRequired["str|None"]
            tracking_number: NotRequired["str|None"]

        class ConfirmParamsShippingAddress(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]

        class ConfirmParamsRadarOptions(TypedDict):
            session: NotRequired["str|None"]

        class ConfirmParamsPaymentMethodOptions(TypedDict):
            acss_debit: NotRequired[
                "Literal['']|PaymentIntent.ConfirmParamsPaymentMethodOptionsAcssDebit|None"
            ]
            affirm: NotRequired[
                "Literal['']|PaymentIntent.ConfirmParamsPaymentMethodOptionsAffirm|None"
            ]
            afterpay_clearpay: NotRequired[
                "Literal['']|PaymentIntent.ConfirmParamsPaymentMethodOptionsAfterpayClearpay|None"
            ]
            alipay: NotRequired[
                "Literal['']|PaymentIntent.ConfirmParamsPaymentMethodOptionsAlipay|None"
            ]
            au_becs_debit: NotRequired[
                "Literal['']|PaymentIntent.ConfirmParamsPaymentMethodOptionsAuBecsDebit|None"
            ]
            bacs_debit: NotRequired[
                "Literal['']|PaymentIntent.ConfirmParamsPaymentMethodOptionsBacsDebit|None"
            ]
            bancontact: NotRequired[
                "Literal['']|PaymentIntent.ConfirmParamsPaymentMethodOptionsBancontact|None"
            ]
            blik: NotRequired[
                "Literal['']|PaymentIntent.ConfirmParamsPaymentMethodOptionsBlik|None"
            ]
            boleto: NotRequired[
                "Literal['']|PaymentIntent.ConfirmParamsPaymentMethodOptionsBoleto|None"
            ]
            card: NotRequired[
                "Literal['']|PaymentIntent.ConfirmParamsPaymentMethodOptionsCard|None"
            ]
            card_present: NotRequired[
                "Literal['']|PaymentIntent.ConfirmParamsPaymentMethodOptionsCardPresent|None"
            ]
            cashapp: NotRequired[
                "Literal['']|PaymentIntent.ConfirmParamsPaymentMethodOptionsCashapp|None"
            ]
            customer_balance: NotRequired[
                "Literal['']|PaymentIntent.ConfirmParamsPaymentMethodOptionsCustomerBalance|None"
            ]
            eps: NotRequired[
                "Literal['']|PaymentIntent.ConfirmParamsPaymentMethodOptionsEps|None"
            ]
            fpx: NotRequired[
                "Literal['']|PaymentIntent.ConfirmParamsPaymentMethodOptionsFpx|None"
            ]
            giropay: NotRequired[
                "Literal['']|PaymentIntent.ConfirmParamsPaymentMethodOptionsGiropay|None"
            ]
            grabpay: NotRequired[
                "Literal['']|PaymentIntent.ConfirmParamsPaymentMethodOptionsGrabpay|None"
            ]
            ideal: NotRequired[
                "Literal['']|PaymentIntent.ConfirmParamsPaymentMethodOptionsIdeal|None"
            ]
            interac_present: NotRequired[
                "Literal['']|PaymentIntent.ConfirmParamsPaymentMethodOptionsInteracPresent|None"
            ]
            klarna: NotRequired[
                "Literal['']|PaymentIntent.ConfirmParamsPaymentMethodOptionsKlarna|None"
            ]
            konbini: NotRequired[
                "Literal['']|PaymentIntent.ConfirmParamsPaymentMethodOptionsKonbini|None"
            ]
            link: NotRequired[
                "Literal['']|PaymentIntent.ConfirmParamsPaymentMethodOptionsLink|None"
            ]
            oxxo: NotRequired[
                "Literal['']|PaymentIntent.ConfirmParamsPaymentMethodOptionsOxxo|None"
            ]
            p24: NotRequired[
                "Literal['']|PaymentIntent.ConfirmParamsPaymentMethodOptionsP24|None"
            ]
            paynow: NotRequired[
                "Literal['']|PaymentIntent.ConfirmParamsPaymentMethodOptionsPaynow|None"
            ]
            paypal: NotRequired[
                "Literal['']|PaymentIntent.ConfirmParamsPaymentMethodOptionsPaypal|None"
            ]
            pix: NotRequired[
                "Literal['']|PaymentIntent.ConfirmParamsPaymentMethodOptionsPix|None"
            ]
            promptpay: NotRequired[
                "Literal['']|PaymentIntent.ConfirmParamsPaymentMethodOptionsPromptpay|None"
            ]
            sepa_debit: NotRequired[
                "Literal['']|PaymentIntent.ConfirmParamsPaymentMethodOptionsSepaDebit|None"
            ]
            sofort: NotRequired[
                "Literal['']|PaymentIntent.ConfirmParamsPaymentMethodOptionsSofort|None"
            ]
            us_bank_account: NotRequired[
                "Literal['']|PaymentIntent.ConfirmParamsPaymentMethodOptionsUsBankAccount|None"
            ]
            wechat_pay: NotRequired[
                "Literal['']|PaymentIntent.ConfirmParamsPaymentMethodOptionsWechatPay|None"
            ]
            zip: NotRequired[
                "Literal['']|PaymentIntent.ConfirmParamsPaymentMethodOptionsZip|None"
            ]

        class ConfirmParamsPaymentMethodOptionsZip(TypedDict):
            setup_future_usage: NotRequired["Literal['none']|None"]

        class ConfirmParamsPaymentMethodOptionsWechatPay(TypedDict):
            app_id: NotRequired["str|None"]
            client: Literal["android", "ios", "web"]
            setup_future_usage: NotRequired["Literal['none']|None"]

        class ConfirmParamsPaymentMethodOptionsUsBankAccount(TypedDict):
            financial_connections: NotRequired[
                "PaymentIntent.ConfirmParamsPaymentMethodOptionsUsBankAccountFinancialConnections|None"
            ]
            networks: NotRequired[
                "PaymentIntent.ConfirmParamsPaymentMethodOptionsUsBankAccountNetworks|None"
            ]
            preferred_settlement_speed: NotRequired[
                "Literal['']|Literal['fastest', 'standard']|None"
            ]
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session', 'on_session']|None"
            ]
            verification_method: NotRequired[
                "Literal['automatic', 'instant', 'microdeposits']|None"
            ]

        class ConfirmParamsPaymentMethodOptionsUsBankAccountNetworks(
            TypedDict
        ):
            requested: NotRequired[
                "List[Literal['ach', 'us_domestic_wire']]|None"
            ]

        class ConfirmParamsPaymentMethodOptionsUsBankAccountFinancialConnections(
            TypedDict,
        ):
            permissions: NotRequired[
                "List[Literal['balances', 'ownership', 'payment_method', 'transactions']]|None"
            ]
            prefetch: NotRequired["List[Literal['balances']]|None"]
            return_url: NotRequired["str|None"]

        class ConfirmParamsPaymentMethodOptionsSofort(TypedDict):
            preferred_language: NotRequired[
                "Literal['']|Literal['de', 'en', 'es', 'fr', 'it', 'nl', 'pl']|None"
            ]
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session']|None"
            ]

        class ConfirmParamsPaymentMethodOptionsSepaDebit(TypedDict):
            mandate_options: NotRequired[
                "PaymentIntent.ConfirmParamsPaymentMethodOptionsSepaDebitMandateOptions|None"
            ]
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session', 'on_session']|None"
            ]

        class ConfirmParamsPaymentMethodOptionsSepaDebitMandateOptions(
            TypedDict,
        ):
            pass

        class ConfirmParamsPaymentMethodOptionsPromptpay(TypedDict):
            setup_future_usage: NotRequired["Literal['none']|None"]

        class ConfirmParamsPaymentMethodOptionsPix(TypedDict):
            expires_after_seconds: NotRequired["int|None"]
            expires_at: NotRequired["int|None"]
            setup_future_usage: NotRequired["Literal['none']|None"]

        class ConfirmParamsPaymentMethodOptionsPaypal(TypedDict):
            capture_method: NotRequired["Literal['']|Literal['manual']|None"]
            preferred_locale: NotRequired[
                "Literal['cs-CZ', 'da-DK', 'de-AT', 'de-DE', 'de-LU', 'el-GR', 'en-GB', 'en-US', 'es-ES', 'fi-FI', 'fr-BE', 'fr-FR', 'fr-LU', 'hu-HU', 'it-IT', 'nl-BE', 'nl-NL', 'pl-PL', 'pt-PT', 'sk-SK', 'sv-SE']|None"
            ]
            reference: NotRequired["str|None"]
            risk_correlation_id: NotRequired["str|None"]
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session']|None"
            ]

        class ConfirmParamsPaymentMethodOptionsPaynow(TypedDict):
            setup_future_usage: NotRequired["Literal['none']|None"]

        class ConfirmParamsPaymentMethodOptionsP24(TypedDict):
            setup_future_usage: NotRequired["Literal['none']|None"]
            tos_shown_and_accepted: NotRequired["bool|None"]

        class ConfirmParamsPaymentMethodOptionsOxxo(TypedDict):
            expires_after_days: NotRequired["int|None"]
            setup_future_usage: NotRequired["Literal['none']|None"]

        class ConfirmParamsPaymentMethodOptionsLink(TypedDict):
            capture_method: NotRequired["Literal['']|Literal['manual']|None"]
            persistent_token: NotRequired["str|None"]
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session']|None"
            ]

        class ConfirmParamsPaymentMethodOptionsKonbini(TypedDict):
            confirmation_number: NotRequired["Literal['']|str|None"]
            expires_after_days: NotRequired["Literal['']|int|None"]
            expires_at: NotRequired["Literal['']|int|None"]
            product_description: NotRequired["Literal['']|str|None"]
            setup_future_usage: NotRequired["Literal['none']|None"]

        class ConfirmParamsPaymentMethodOptionsKlarna(TypedDict):
            capture_method: NotRequired["Literal['']|Literal['manual']|None"]
            preferred_locale: NotRequired[
                "Literal['cs-CZ', 'da-DK', 'de-AT', 'de-CH', 'de-DE', 'el-GR', 'en-AT', 'en-AU', 'en-BE', 'en-CA', 'en-CH', 'en-CZ', 'en-DE', 'en-DK', 'en-ES', 'en-FI', 'en-FR', 'en-GB', 'en-GR', 'en-IE', 'en-IT', 'en-NL', 'en-NO', 'en-NZ', 'en-PL', 'en-PT', 'en-SE', 'en-US', 'es-ES', 'es-US', 'fi-FI', 'fr-BE', 'fr-CA', 'fr-CH', 'fr-FR', 'it-CH', 'it-IT', 'nb-NO', 'nl-BE', 'nl-NL', 'pl-PL', 'pt-PT', 'sv-FI', 'sv-SE']|None"
            ]
            setup_future_usage: NotRequired["Literal['none']|None"]

        class ConfirmParamsPaymentMethodOptionsInteracPresent(TypedDict):
            pass

        class ConfirmParamsPaymentMethodOptionsIdeal(TypedDict):
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session']|None"
            ]

        class ConfirmParamsPaymentMethodOptionsGrabpay(TypedDict):
            setup_future_usage: NotRequired["Literal['none']|None"]

        class ConfirmParamsPaymentMethodOptionsGiropay(TypedDict):
            setup_future_usage: NotRequired["Literal['none']|None"]

        class ConfirmParamsPaymentMethodOptionsFpx(TypedDict):
            setup_future_usage: NotRequired["Literal['none']|None"]

        class ConfirmParamsPaymentMethodOptionsEps(TypedDict):
            setup_future_usage: NotRequired["Literal['none']|None"]

        class ConfirmParamsPaymentMethodOptionsCustomerBalance(TypedDict):
            bank_transfer: NotRequired[
                "PaymentIntent.ConfirmParamsPaymentMethodOptionsCustomerBalanceBankTransfer|None"
            ]
            funding_type: NotRequired["Literal['bank_transfer']|None"]
            setup_future_usage: NotRequired["Literal['none']|None"]

        class ConfirmParamsPaymentMethodOptionsCustomerBalanceBankTransfer(
            TypedDict,
        ):
            eu_bank_transfer: NotRequired[
                "PaymentIntent.ConfirmParamsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer|None"
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

        class ConfirmParamsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer(
            TypedDict,
        ):
            country: str

        class ConfirmParamsPaymentMethodOptionsCashapp(TypedDict):
            capture_method: NotRequired["Literal['']|Literal['manual']|None"]
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session', 'on_session']|None"
            ]

        class ConfirmParamsPaymentMethodOptionsCardPresent(TypedDict):
            request_extended_authorization: NotRequired["bool|None"]
            request_incremental_authorization: NotRequired[
                "Literal['if_available', 'never']|None"
            ]
            request_incremental_authorization_support: NotRequired["bool|None"]

        class ConfirmParamsPaymentMethodOptionsCard(TypedDict):
            capture_method: NotRequired["Literal['']|Literal['manual']|None"]
            cvc_token: NotRequired["str|None"]
            installments: NotRequired[
                "PaymentIntent.ConfirmParamsPaymentMethodOptionsCardInstallments|None"
            ]
            mandate_options: NotRequired[
                "PaymentIntent.ConfirmParamsPaymentMethodOptionsCardMandateOptions|None"
            ]
            moto: NotRequired["bool|None"]
            network: NotRequired[
                "Literal['amex', 'cartes_bancaires', 'diners', 'discover', 'eftpos_au', 'interac', 'jcb', 'mastercard', 'unionpay', 'unknown', 'visa']|None"
            ]
            request_extended_authorization: NotRequired[
                "Literal['if_available', 'never']|None"
            ]
            request_incremental_authorization: NotRequired[
                "Literal['if_available', 'never']|None"
            ]
            request_multicapture: NotRequired[
                "Literal['if_available', 'never']|None"
            ]
            request_overcapture: NotRequired[
                "Literal['if_available', 'never']|None"
            ]
            request_three_d_secure: NotRequired[
                "Literal['any', 'automatic']|None"
            ]
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session', 'on_session']|None"
            ]
            statement_descriptor_suffix_kana: NotRequired[
                "Literal['']|str|None"
            ]
            statement_descriptor_suffix_kanji: NotRequired[
                "Literal['']|str|None"
            ]

        class ConfirmParamsPaymentMethodOptionsCardMandateOptions(TypedDict):
            amount: int
            amount_type: Literal["fixed", "maximum"]
            description: NotRequired["str|None"]
            end_date: NotRequired["int|None"]
            interval: Literal["day", "month", "sporadic", "week", "year"]
            interval_count: NotRequired["int|None"]
            reference: str
            start_date: int
            supported_types: NotRequired["List[Literal['india']]|None"]

        class ConfirmParamsPaymentMethodOptionsCardInstallments(TypedDict):
            enabled: NotRequired["bool|None"]
            plan: NotRequired[
                "Literal['']|PaymentIntent.ConfirmParamsPaymentMethodOptionsCardInstallmentsPlan|None"
            ]

        class ConfirmParamsPaymentMethodOptionsCardInstallmentsPlan(TypedDict):
            count: int
            interval: Literal["month"]
            type: Literal["fixed_count"]

        class ConfirmParamsPaymentMethodOptionsBoleto(TypedDict):
            expires_after_days: NotRequired["int|None"]
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session', 'on_session']|None"
            ]

        class ConfirmParamsPaymentMethodOptionsBlik(TypedDict):
            code: NotRequired["str|None"]

        class ConfirmParamsPaymentMethodOptionsBancontact(TypedDict):
            preferred_language: NotRequired[
                "Literal['de', 'en', 'fr', 'nl']|None"
            ]
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session']|None"
            ]

        class ConfirmParamsPaymentMethodOptionsBacsDebit(TypedDict):
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session', 'on_session']|None"
            ]

        class ConfirmParamsPaymentMethodOptionsAuBecsDebit(TypedDict):
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session', 'on_session']|None"
            ]

        class ConfirmParamsPaymentMethodOptionsAlipay(TypedDict):
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session']|None"
            ]

        class ConfirmParamsPaymentMethodOptionsAfterpayClearpay(TypedDict):
            capture_method: NotRequired["Literal['']|Literal['manual']|None"]
            reference: NotRequired["str|None"]
            setup_future_usage: NotRequired["Literal['none']|None"]

        class ConfirmParamsPaymentMethodOptionsAffirm(TypedDict):
            capture_method: NotRequired["Literal['']|Literal['manual']|None"]
            preferred_locale: NotRequired["str|None"]
            setup_future_usage: NotRequired["Literal['none']|None"]

        class ConfirmParamsPaymentMethodOptionsAcssDebit(TypedDict):
            mandate_options: NotRequired[
                "PaymentIntent.ConfirmParamsPaymentMethodOptionsAcssDebitMandateOptions|None"
            ]
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session', 'on_session']|None"
            ]
            verification_method: NotRequired[
                "Literal['automatic', 'instant', 'microdeposits']|None"
            ]

        class ConfirmParamsPaymentMethodOptionsAcssDebitMandateOptions(
            TypedDict,
        ):
            custom_mandate_url: NotRequired["Literal['']|str|None"]
            interval_description: NotRequired["str|None"]
            payment_schedule: NotRequired[
                "Literal['combined', 'interval', 'sporadic']|None"
            ]
            transaction_type: NotRequired[
                "Literal['business', 'personal']|None"
            ]

        class ConfirmParamsPaymentMethodData(TypedDict):
            acss_debit: NotRequired[
                "PaymentIntent.ConfirmParamsPaymentMethodDataAcssDebit|None"
            ]
            affirm: NotRequired[
                "PaymentIntent.ConfirmParamsPaymentMethodDataAffirm|None"
            ]
            afterpay_clearpay: NotRequired[
                "PaymentIntent.ConfirmParamsPaymentMethodDataAfterpayClearpay|None"
            ]
            alipay: NotRequired[
                "PaymentIntent.ConfirmParamsPaymentMethodDataAlipay|None"
            ]
            au_becs_debit: NotRequired[
                "PaymentIntent.ConfirmParamsPaymentMethodDataAuBecsDebit|None"
            ]
            bacs_debit: NotRequired[
                "PaymentIntent.ConfirmParamsPaymentMethodDataBacsDebit|None"
            ]
            bancontact: NotRequired[
                "PaymentIntent.ConfirmParamsPaymentMethodDataBancontact|None"
            ]
            billing_details: NotRequired[
                "PaymentIntent.ConfirmParamsPaymentMethodDataBillingDetails|None"
            ]
            blik: NotRequired[
                "PaymentIntent.ConfirmParamsPaymentMethodDataBlik|None"
            ]
            boleto: NotRequired[
                "PaymentIntent.ConfirmParamsPaymentMethodDataBoleto|None"
            ]
            cashapp: NotRequired[
                "PaymentIntent.ConfirmParamsPaymentMethodDataCashapp|None"
            ]
            customer_balance: NotRequired[
                "PaymentIntent.ConfirmParamsPaymentMethodDataCustomerBalance|None"
            ]
            eps: NotRequired[
                "PaymentIntent.ConfirmParamsPaymentMethodDataEps|None"
            ]
            fpx: NotRequired[
                "PaymentIntent.ConfirmParamsPaymentMethodDataFpx|None"
            ]
            giropay: NotRequired[
                "PaymentIntent.ConfirmParamsPaymentMethodDataGiropay|None"
            ]
            grabpay: NotRequired[
                "PaymentIntent.ConfirmParamsPaymentMethodDataGrabpay|None"
            ]
            ideal: NotRequired[
                "PaymentIntent.ConfirmParamsPaymentMethodDataIdeal|None"
            ]
            interac_present: NotRequired[
                "PaymentIntent.ConfirmParamsPaymentMethodDataInteracPresent|None"
            ]
            klarna: NotRequired[
                "PaymentIntent.ConfirmParamsPaymentMethodDataKlarna|None"
            ]
            konbini: NotRequired[
                "PaymentIntent.ConfirmParamsPaymentMethodDataKonbini|None"
            ]
            link: NotRequired[
                "PaymentIntent.ConfirmParamsPaymentMethodDataLink|None"
            ]
            metadata: NotRequired["Dict[str, str]|None"]
            oxxo: NotRequired[
                "PaymentIntent.ConfirmParamsPaymentMethodDataOxxo|None"
            ]
            p24: NotRequired[
                "PaymentIntent.ConfirmParamsPaymentMethodDataP24|None"
            ]
            paynow: NotRequired[
                "PaymentIntent.ConfirmParamsPaymentMethodDataPaynow|None"
            ]
            paypal: NotRequired[
                "PaymentIntent.ConfirmParamsPaymentMethodDataPaypal|None"
            ]
            pix: NotRequired[
                "PaymentIntent.ConfirmParamsPaymentMethodDataPix|None"
            ]
            promptpay: NotRequired[
                "PaymentIntent.ConfirmParamsPaymentMethodDataPromptpay|None"
            ]
            radar_options: NotRequired[
                "PaymentIntent.ConfirmParamsPaymentMethodDataRadarOptions|None"
            ]
            sepa_debit: NotRequired[
                "PaymentIntent.ConfirmParamsPaymentMethodDataSepaDebit|None"
            ]
            sofort: NotRequired[
                "PaymentIntent.ConfirmParamsPaymentMethodDataSofort|None"
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
                "PaymentIntent.ConfirmParamsPaymentMethodDataUsBankAccount|None"
            ]
            wechat_pay: NotRequired[
                "PaymentIntent.ConfirmParamsPaymentMethodDataWechatPay|None"
            ]
            zip: NotRequired[
                "PaymentIntent.ConfirmParamsPaymentMethodDataZip|None"
            ]

        class ConfirmParamsPaymentMethodDataZip(TypedDict):
            pass

        class ConfirmParamsPaymentMethodDataWechatPay(TypedDict):
            pass

        class ConfirmParamsPaymentMethodDataUsBankAccount(TypedDict):
            account_holder_type: NotRequired[
                "Literal['company', 'individual']|None"
            ]
            account_number: NotRequired["str|None"]
            account_type: NotRequired["Literal['checking', 'savings']|None"]
            financial_connections_account: NotRequired["str|None"]
            routing_number: NotRequired["str|None"]

        class ConfirmParamsPaymentMethodDataSofort(TypedDict):
            country: Literal["AT", "BE", "DE", "ES", "IT", "NL"]

        class ConfirmParamsPaymentMethodDataSepaDebit(TypedDict):
            iban: str

        class ConfirmParamsPaymentMethodDataRadarOptions(TypedDict):
            session: NotRequired["str|None"]

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
                "Literal['alior_bank', 'bank_millennium', 'bank_nowy_bfg_sa', 'bank_pekao_sa', 'banki_spbdzielcze', 'blik', 'bnp_paribas', 'boz', 'citi_handlowy', 'credit_agricole', 'envelobank', 'etransfer_pocztowy24', 'getin_bank', 'ideabank', 'ing', 'inteligo', 'mbank_mtransfer', 'nest_przelew', 'noble_pay', 'pbac_z_ipko', 'plus_bank', 'santander_przelew24', 'tmobile_usbugi_bankowe', 'toyota_bank', 'volkswagen_bank']|None"
            ]

        class ConfirmParamsPaymentMethodDataOxxo(TypedDict):
            pass

        class ConfirmParamsPaymentMethodDataLink(TypedDict):
            pass

        class ConfirmParamsPaymentMethodDataKonbini(TypedDict):
            pass

        class ConfirmParamsPaymentMethodDataKlarna(TypedDict):
            dob: NotRequired[
                "PaymentIntent.ConfirmParamsPaymentMethodDataKlarnaDob|None"
            ]

        class ConfirmParamsPaymentMethodDataKlarnaDob(TypedDict):
            day: int
            month: int
            year: int

        class ConfirmParamsPaymentMethodDataInteracPresent(TypedDict):
            pass

        class ConfirmParamsPaymentMethodDataIdeal(TypedDict):
            bank: NotRequired[
                "Literal['abn_amro', 'asn_bank', 'bunq', 'handelsbanken', 'ing', 'knab', 'moneyou', 'n26', 'rabobank', 'regiobank', 'revolut', 'sns_bank', 'triodos_bank', 'van_lanschot', 'yoursafe']|None"
            ]

        class ConfirmParamsPaymentMethodDataGrabpay(TypedDict):
            pass

        class ConfirmParamsPaymentMethodDataGiropay(TypedDict):
            pass

        class ConfirmParamsPaymentMethodDataFpx(TypedDict):
            account_holder_type: NotRequired[
                "Literal['company', 'individual']|None"
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
                "Literal['arzte_und_apotheker_bank', 'austrian_anadi_bank_ag', 'bank_austria', 'bankhaus_carl_spangler', 'bankhaus_schelhammer_und_schattera_ag', 'bawag_psk_ag', 'bks_bank_ag', 'brull_kallmus_bank_ag', 'btv_vier_lander_bank', 'capital_bank_grawe_gruppe_ag', 'deutsche_bank_ag', 'dolomitenbank', 'easybank_ag', 'erste_bank_und_sparkassen', 'hypo_alpeadriabank_international_ag', 'hypo_bank_burgenland_aktiengesellschaft', 'hypo_noe_lb_fur_niederosterreich_u_wien', 'hypo_oberosterreich_salzburg_steiermark', 'hypo_tirol_bank_ag', 'hypo_vorarlberg_bank_ag', 'marchfelder_bank', 'oberbank_ag', 'raiffeisen_bankengruppe_osterreich', 'schoellerbank_ag', 'sparda_bank_wien', 'volksbank_gruppe', 'volkskreditbank_ag', 'vr_bank_braunau']|None"
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
                "Literal['']|PaymentIntent.ConfirmParamsPaymentMethodDataBillingDetailsAddress|None"
            ]
            email: NotRequired["Literal['']|str|None"]
            name: NotRequired["Literal['']|str|None"]
            phone: NotRequired["Literal['']|str|None"]

        class ConfirmParamsPaymentMethodDataBillingDetailsAddress(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]

        class ConfirmParamsPaymentMethodDataBancontact(TypedDict):
            pass

        class ConfirmParamsPaymentMethodDataBacsDebit(TypedDict):
            account_number: NotRequired["str|None"]
            sort_code: NotRequired["str|None"]

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

        class ConfirmParamsMandateData2(TypedDict):
            customer_acceptance: "PaymentIntent.ConfirmParamsMandateDataCustomerAcceptance2"

        class ConfirmParamsMandateDataCustomerAcceptance2(TypedDict):
            online: "PaymentIntent.ConfirmParamsMandateDataCustomerAcceptanceOnline2"
            type: Literal["online"]

        class ConfirmParamsMandateDataCustomerAcceptanceOnline2(TypedDict):
            ip_address: NotRequired["str|None"]
            user_agent: NotRequired["str|None"]

        class ConfirmParamsMandateData(TypedDict):
            customer_acceptance: "PaymentIntent.ConfirmParamsMandateDataCustomerAcceptance"

        class ConfirmParamsMandateDataCustomerAcceptance(TypedDict):
            accepted_at: NotRequired["int|None"]
            offline: NotRequired[
                "PaymentIntent.ConfirmParamsMandateDataCustomerAcceptanceOffline|None"
            ]
            online: NotRequired[
                "PaymentIntent.ConfirmParamsMandateDataCustomerAcceptanceOnline|None"
            ]
            type: Literal["offline", "online"]

        class ConfirmParamsMandateDataCustomerAcceptanceOnline(TypedDict):
            ip_address: str
            user_agent: str

        class ConfirmParamsMandateDataCustomerAcceptanceOffline(TypedDict):
            pass

        class CreateParams(RequestOptions):
            amount: int
            application_fee_amount: NotRequired["int|None"]
            automatic_payment_methods: NotRequired[
                "PaymentIntent.CreateParamsAutomaticPaymentMethods|None"
            ]
            capture_method: NotRequired[
                "Literal['automatic', 'automatic_async', 'manual']|None"
            ]
            confirm: NotRequired["bool|None"]
            confirmation_method: NotRequired[
                "Literal['automatic', 'manual']|None"
            ]
            currency: str
            customer: NotRequired["str|None"]
            description: NotRequired["str|None"]
            error_on_requires_action: NotRequired["bool|None"]
            expand: NotRequired["List[str]|None"]
            mandate: NotRequired["str|None"]
            mandate_data: NotRequired[
                "Literal['']|PaymentIntent.CreateParamsMandateData|None"
            ]
            metadata: NotRequired["Dict[str, str]|None"]
            off_session: NotRequired[
                "bool|Literal['one_off', 'recurring']|None"
            ]
            on_behalf_of: NotRequired["str|None"]
            payment_method: NotRequired["str|None"]
            payment_method_configuration: NotRequired["str|None"]
            payment_method_data: NotRequired[
                "PaymentIntent.CreateParamsPaymentMethodData|None"
            ]
            payment_method_options: NotRequired[
                "PaymentIntent.CreateParamsPaymentMethodOptions|None"
            ]
            payment_method_types: NotRequired["List[str]|None"]
            radar_options: NotRequired[
                "PaymentIntent.CreateParamsRadarOptions|None"
            ]
            receipt_email: NotRequired["str|None"]
            return_url: NotRequired["str|None"]
            setup_future_usage: NotRequired[
                "Literal['off_session', 'on_session']|None"
            ]
            shipping: NotRequired["PaymentIntent.CreateParamsShipping|None"]
            statement_descriptor: NotRequired["str|None"]
            statement_descriptor_suffix: NotRequired["str|None"]
            transfer_data: NotRequired[
                "PaymentIntent.CreateParamsTransferData|None"
            ]
            transfer_group: NotRequired["str|None"]
            use_stripe_sdk: NotRequired["bool|None"]

        class CreateParamsTransferData(TypedDict):
            amount: NotRequired["int|None"]
            destination: str

        class CreateParamsShipping(TypedDict):
            address: "PaymentIntent.CreateParamsShippingAddress"
            carrier: NotRequired["str|None"]
            name: str
            phone: NotRequired["str|None"]
            tracking_number: NotRequired["str|None"]

        class CreateParamsShippingAddress(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]

        class CreateParamsRadarOptions(TypedDict):
            session: NotRequired["str|None"]

        class CreateParamsPaymentMethodOptions(TypedDict):
            acss_debit: NotRequired[
                "Literal['']|PaymentIntent.CreateParamsPaymentMethodOptionsAcssDebit|None"
            ]
            affirm: NotRequired[
                "Literal['']|PaymentIntent.CreateParamsPaymentMethodOptionsAffirm|None"
            ]
            afterpay_clearpay: NotRequired[
                "Literal['']|PaymentIntent.CreateParamsPaymentMethodOptionsAfterpayClearpay|None"
            ]
            alipay: NotRequired[
                "Literal['']|PaymentIntent.CreateParamsPaymentMethodOptionsAlipay|None"
            ]
            au_becs_debit: NotRequired[
                "Literal['']|PaymentIntent.CreateParamsPaymentMethodOptionsAuBecsDebit|None"
            ]
            bacs_debit: NotRequired[
                "Literal['']|PaymentIntent.CreateParamsPaymentMethodOptionsBacsDebit|None"
            ]
            bancontact: NotRequired[
                "Literal['']|PaymentIntent.CreateParamsPaymentMethodOptionsBancontact|None"
            ]
            blik: NotRequired[
                "Literal['']|PaymentIntent.CreateParamsPaymentMethodOptionsBlik|None"
            ]
            boleto: NotRequired[
                "Literal['']|PaymentIntent.CreateParamsPaymentMethodOptionsBoleto|None"
            ]
            card: NotRequired[
                "Literal['']|PaymentIntent.CreateParamsPaymentMethodOptionsCard|None"
            ]
            card_present: NotRequired[
                "Literal['']|PaymentIntent.CreateParamsPaymentMethodOptionsCardPresent|None"
            ]
            cashapp: NotRequired[
                "Literal['']|PaymentIntent.CreateParamsPaymentMethodOptionsCashapp|None"
            ]
            customer_balance: NotRequired[
                "Literal['']|PaymentIntent.CreateParamsPaymentMethodOptionsCustomerBalance|None"
            ]
            eps: NotRequired[
                "Literal['']|PaymentIntent.CreateParamsPaymentMethodOptionsEps|None"
            ]
            fpx: NotRequired[
                "Literal['']|PaymentIntent.CreateParamsPaymentMethodOptionsFpx|None"
            ]
            giropay: NotRequired[
                "Literal['']|PaymentIntent.CreateParamsPaymentMethodOptionsGiropay|None"
            ]
            grabpay: NotRequired[
                "Literal['']|PaymentIntent.CreateParamsPaymentMethodOptionsGrabpay|None"
            ]
            ideal: NotRequired[
                "Literal['']|PaymentIntent.CreateParamsPaymentMethodOptionsIdeal|None"
            ]
            interac_present: NotRequired[
                "Literal['']|PaymentIntent.CreateParamsPaymentMethodOptionsInteracPresent|None"
            ]
            klarna: NotRequired[
                "Literal['']|PaymentIntent.CreateParamsPaymentMethodOptionsKlarna|None"
            ]
            konbini: NotRequired[
                "Literal['']|PaymentIntent.CreateParamsPaymentMethodOptionsKonbini|None"
            ]
            link: NotRequired[
                "Literal['']|PaymentIntent.CreateParamsPaymentMethodOptionsLink|None"
            ]
            oxxo: NotRequired[
                "Literal['']|PaymentIntent.CreateParamsPaymentMethodOptionsOxxo|None"
            ]
            p24: NotRequired[
                "Literal['']|PaymentIntent.CreateParamsPaymentMethodOptionsP24|None"
            ]
            paynow: NotRequired[
                "Literal['']|PaymentIntent.CreateParamsPaymentMethodOptionsPaynow|None"
            ]
            paypal: NotRequired[
                "Literal['']|PaymentIntent.CreateParamsPaymentMethodOptionsPaypal|None"
            ]
            pix: NotRequired[
                "Literal['']|PaymentIntent.CreateParamsPaymentMethodOptionsPix|None"
            ]
            promptpay: NotRequired[
                "Literal['']|PaymentIntent.CreateParamsPaymentMethodOptionsPromptpay|None"
            ]
            sepa_debit: NotRequired[
                "Literal['']|PaymentIntent.CreateParamsPaymentMethodOptionsSepaDebit|None"
            ]
            sofort: NotRequired[
                "Literal['']|PaymentIntent.CreateParamsPaymentMethodOptionsSofort|None"
            ]
            us_bank_account: NotRequired[
                "Literal['']|PaymentIntent.CreateParamsPaymentMethodOptionsUsBankAccount|None"
            ]
            wechat_pay: NotRequired[
                "Literal['']|PaymentIntent.CreateParamsPaymentMethodOptionsWechatPay|None"
            ]
            zip: NotRequired[
                "Literal['']|PaymentIntent.CreateParamsPaymentMethodOptionsZip|None"
            ]

        class CreateParamsPaymentMethodOptionsZip(TypedDict):
            setup_future_usage: NotRequired["Literal['none']|None"]

        class CreateParamsPaymentMethodOptionsWechatPay(TypedDict):
            app_id: NotRequired["str|None"]
            client: Literal["android", "ios", "web"]
            setup_future_usage: NotRequired["Literal['none']|None"]

        class CreateParamsPaymentMethodOptionsUsBankAccount(TypedDict):
            financial_connections: NotRequired[
                "PaymentIntent.CreateParamsPaymentMethodOptionsUsBankAccountFinancialConnections|None"
            ]
            networks: NotRequired[
                "PaymentIntent.CreateParamsPaymentMethodOptionsUsBankAccountNetworks|None"
            ]
            preferred_settlement_speed: NotRequired[
                "Literal['']|Literal['fastest', 'standard']|None"
            ]
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session', 'on_session']|None"
            ]
            verification_method: NotRequired[
                "Literal['automatic', 'instant', 'microdeposits']|None"
            ]

        class CreateParamsPaymentMethodOptionsUsBankAccountNetworks(TypedDict):
            requested: NotRequired[
                "List[Literal['ach', 'us_domestic_wire']]|None"
            ]

        class CreateParamsPaymentMethodOptionsUsBankAccountFinancialConnections(
            TypedDict,
        ):
            permissions: NotRequired[
                "List[Literal['balances', 'ownership', 'payment_method', 'transactions']]|None"
            ]
            prefetch: NotRequired["List[Literal['balances']]|None"]
            return_url: NotRequired["str|None"]

        class CreateParamsPaymentMethodOptionsSofort(TypedDict):
            preferred_language: NotRequired[
                "Literal['']|Literal['de', 'en', 'es', 'fr', 'it', 'nl', 'pl']|None"
            ]
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session']|None"
            ]

        class CreateParamsPaymentMethodOptionsSepaDebit(TypedDict):
            mandate_options: NotRequired[
                "PaymentIntent.CreateParamsPaymentMethodOptionsSepaDebitMandateOptions|None"
            ]
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session', 'on_session']|None"
            ]

        class CreateParamsPaymentMethodOptionsSepaDebitMandateOptions(
            TypedDict,
        ):
            pass

        class CreateParamsPaymentMethodOptionsPromptpay(TypedDict):
            setup_future_usage: NotRequired["Literal['none']|None"]

        class CreateParamsPaymentMethodOptionsPix(TypedDict):
            expires_after_seconds: NotRequired["int|None"]
            expires_at: NotRequired["int|None"]
            setup_future_usage: NotRequired["Literal['none']|None"]

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
            capture_method: NotRequired["Literal['']|Literal['manual']|None"]
            persistent_token: NotRequired["str|None"]
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session']|None"
            ]

        class CreateParamsPaymentMethodOptionsKonbini(TypedDict):
            confirmation_number: NotRequired["Literal['']|str|None"]
            expires_after_days: NotRequired["Literal['']|int|None"]
            expires_at: NotRequired["Literal['']|int|None"]
            product_description: NotRequired["Literal['']|str|None"]
            setup_future_usage: NotRequired["Literal['none']|None"]

        class CreateParamsPaymentMethodOptionsKlarna(TypedDict):
            capture_method: NotRequired["Literal['']|Literal['manual']|None"]
            preferred_locale: NotRequired[
                "Literal['cs-CZ', 'da-DK', 'de-AT', 'de-CH', 'de-DE', 'el-GR', 'en-AT', 'en-AU', 'en-BE', 'en-CA', 'en-CH', 'en-CZ', 'en-DE', 'en-DK', 'en-ES', 'en-FI', 'en-FR', 'en-GB', 'en-GR', 'en-IE', 'en-IT', 'en-NL', 'en-NO', 'en-NZ', 'en-PL', 'en-PT', 'en-SE', 'en-US', 'es-ES', 'es-US', 'fi-FI', 'fr-BE', 'fr-CA', 'fr-CH', 'fr-FR', 'it-CH', 'it-IT', 'nb-NO', 'nl-BE', 'nl-NL', 'pl-PL', 'pt-PT', 'sv-FI', 'sv-SE']|None"
            ]
            setup_future_usage: NotRequired["Literal['none']|None"]

        class CreateParamsPaymentMethodOptionsInteracPresent(TypedDict):
            pass

        class CreateParamsPaymentMethodOptionsIdeal(TypedDict):
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session']|None"
            ]

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
                "PaymentIntent.CreateParamsPaymentMethodOptionsCustomerBalanceBankTransfer|None"
            ]
            funding_type: NotRequired["Literal['bank_transfer']|None"]
            setup_future_usage: NotRequired["Literal['none']|None"]

        class CreateParamsPaymentMethodOptionsCustomerBalanceBankTransfer(
            TypedDict,
        ):
            eu_bank_transfer: NotRequired[
                "PaymentIntent.CreateParamsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer|None"
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
            capture_method: NotRequired["Literal['']|Literal['manual']|None"]
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session', 'on_session']|None"
            ]

        class CreateParamsPaymentMethodOptionsCardPresent(TypedDict):
            request_extended_authorization: NotRequired["bool|None"]
            request_incremental_authorization: NotRequired[
                "Literal['if_available', 'never']|None"
            ]
            request_incremental_authorization_support: NotRequired["bool|None"]

        class CreateParamsPaymentMethodOptionsCard(TypedDict):
            capture_method: NotRequired["Literal['']|Literal['manual']|None"]
            cvc_token: NotRequired["str|None"]
            installments: NotRequired[
                "PaymentIntent.CreateParamsPaymentMethodOptionsCardInstallments|None"
            ]
            mandate_options: NotRequired[
                "PaymentIntent.CreateParamsPaymentMethodOptionsCardMandateOptions|None"
            ]
            moto: NotRequired["bool|None"]
            network: NotRequired[
                "Literal['amex', 'cartes_bancaires', 'diners', 'discover', 'eftpos_au', 'interac', 'jcb', 'mastercard', 'unionpay', 'unknown', 'visa']|None"
            ]
            request_extended_authorization: NotRequired[
                "Literal['if_available', 'never']|None"
            ]
            request_incremental_authorization: NotRequired[
                "Literal['if_available', 'never']|None"
            ]
            request_multicapture: NotRequired[
                "Literal['if_available', 'never']|None"
            ]
            request_overcapture: NotRequired[
                "Literal['if_available', 'never']|None"
            ]
            request_three_d_secure: NotRequired[
                "Literal['any', 'automatic']|None"
            ]
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session', 'on_session']|None"
            ]
            statement_descriptor_suffix_kana: NotRequired[
                "Literal['']|str|None"
            ]
            statement_descriptor_suffix_kanji: NotRequired[
                "Literal['']|str|None"
            ]

        class CreateParamsPaymentMethodOptionsCardMandateOptions(TypedDict):
            amount: int
            amount_type: Literal["fixed", "maximum"]
            description: NotRequired["str|None"]
            end_date: NotRequired["int|None"]
            interval: Literal["day", "month", "sporadic", "week", "year"]
            interval_count: NotRequired["int|None"]
            reference: str
            start_date: int
            supported_types: NotRequired["List[Literal['india']]|None"]

        class CreateParamsPaymentMethodOptionsCardInstallments(TypedDict):
            enabled: NotRequired["bool|None"]
            plan: NotRequired[
                "Literal['']|PaymentIntent.CreateParamsPaymentMethodOptionsCardInstallmentsPlan|None"
            ]

        class CreateParamsPaymentMethodOptionsCardInstallmentsPlan(TypedDict):
            count: int
            interval: Literal["month"]
            type: Literal["fixed_count"]

        class CreateParamsPaymentMethodOptionsBoleto(TypedDict):
            expires_after_days: NotRequired["int|None"]
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session', 'on_session']|None"
            ]

        class CreateParamsPaymentMethodOptionsBlik(TypedDict):
            code: NotRequired["str|None"]

        class CreateParamsPaymentMethodOptionsBancontact(TypedDict):
            preferred_language: NotRequired[
                "Literal['de', 'en', 'fr', 'nl']|None"
            ]
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session']|None"
            ]

        class CreateParamsPaymentMethodOptionsBacsDebit(TypedDict):
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session', 'on_session']|None"
            ]

        class CreateParamsPaymentMethodOptionsAuBecsDebit(TypedDict):
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session', 'on_session']|None"
            ]

        class CreateParamsPaymentMethodOptionsAlipay(TypedDict):
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session']|None"
            ]

        class CreateParamsPaymentMethodOptionsAfterpayClearpay(TypedDict):
            capture_method: NotRequired["Literal['']|Literal['manual']|None"]
            reference: NotRequired["str|None"]
            setup_future_usage: NotRequired["Literal['none']|None"]

        class CreateParamsPaymentMethodOptionsAffirm(TypedDict):
            capture_method: NotRequired["Literal['']|Literal['manual']|None"]
            preferred_locale: NotRequired["str|None"]
            setup_future_usage: NotRequired["Literal['none']|None"]

        class CreateParamsPaymentMethodOptionsAcssDebit(TypedDict):
            mandate_options: NotRequired[
                "PaymentIntent.CreateParamsPaymentMethodOptionsAcssDebitMandateOptions|None"
            ]
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session', 'on_session']|None"
            ]
            verification_method: NotRequired[
                "Literal['automatic', 'instant', 'microdeposits']|None"
            ]

        class CreateParamsPaymentMethodOptionsAcssDebitMandateOptions(
            TypedDict,
        ):
            custom_mandate_url: NotRequired["Literal['']|str|None"]
            interval_description: NotRequired["str|None"]
            payment_schedule: NotRequired[
                "Literal['combined', 'interval', 'sporadic']|None"
            ]
            transaction_type: NotRequired[
                "Literal['business', 'personal']|None"
            ]

        class CreateParamsPaymentMethodData(TypedDict):
            acss_debit: NotRequired[
                "PaymentIntent.CreateParamsPaymentMethodDataAcssDebit|None"
            ]
            affirm: NotRequired[
                "PaymentIntent.CreateParamsPaymentMethodDataAffirm|None"
            ]
            afterpay_clearpay: NotRequired[
                "PaymentIntent.CreateParamsPaymentMethodDataAfterpayClearpay|None"
            ]
            alipay: NotRequired[
                "PaymentIntent.CreateParamsPaymentMethodDataAlipay|None"
            ]
            au_becs_debit: NotRequired[
                "PaymentIntent.CreateParamsPaymentMethodDataAuBecsDebit|None"
            ]
            bacs_debit: NotRequired[
                "PaymentIntent.CreateParamsPaymentMethodDataBacsDebit|None"
            ]
            bancontact: NotRequired[
                "PaymentIntent.CreateParamsPaymentMethodDataBancontact|None"
            ]
            billing_details: NotRequired[
                "PaymentIntent.CreateParamsPaymentMethodDataBillingDetails|None"
            ]
            blik: NotRequired[
                "PaymentIntent.CreateParamsPaymentMethodDataBlik|None"
            ]
            boleto: NotRequired[
                "PaymentIntent.CreateParamsPaymentMethodDataBoleto|None"
            ]
            cashapp: NotRequired[
                "PaymentIntent.CreateParamsPaymentMethodDataCashapp|None"
            ]
            customer_balance: NotRequired[
                "PaymentIntent.CreateParamsPaymentMethodDataCustomerBalance|None"
            ]
            eps: NotRequired[
                "PaymentIntent.CreateParamsPaymentMethodDataEps|None"
            ]
            fpx: NotRequired[
                "PaymentIntent.CreateParamsPaymentMethodDataFpx|None"
            ]
            giropay: NotRequired[
                "PaymentIntent.CreateParamsPaymentMethodDataGiropay|None"
            ]
            grabpay: NotRequired[
                "PaymentIntent.CreateParamsPaymentMethodDataGrabpay|None"
            ]
            ideal: NotRequired[
                "PaymentIntent.CreateParamsPaymentMethodDataIdeal|None"
            ]
            interac_present: NotRequired[
                "PaymentIntent.CreateParamsPaymentMethodDataInteracPresent|None"
            ]
            klarna: NotRequired[
                "PaymentIntent.CreateParamsPaymentMethodDataKlarna|None"
            ]
            konbini: NotRequired[
                "PaymentIntent.CreateParamsPaymentMethodDataKonbini|None"
            ]
            link: NotRequired[
                "PaymentIntent.CreateParamsPaymentMethodDataLink|None"
            ]
            metadata: NotRequired["Dict[str, str]|None"]
            oxxo: NotRequired[
                "PaymentIntent.CreateParamsPaymentMethodDataOxxo|None"
            ]
            p24: NotRequired[
                "PaymentIntent.CreateParamsPaymentMethodDataP24|None"
            ]
            paynow: NotRequired[
                "PaymentIntent.CreateParamsPaymentMethodDataPaynow|None"
            ]
            paypal: NotRequired[
                "PaymentIntent.CreateParamsPaymentMethodDataPaypal|None"
            ]
            pix: NotRequired[
                "PaymentIntent.CreateParamsPaymentMethodDataPix|None"
            ]
            promptpay: NotRequired[
                "PaymentIntent.CreateParamsPaymentMethodDataPromptpay|None"
            ]
            radar_options: NotRequired[
                "PaymentIntent.CreateParamsPaymentMethodDataRadarOptions|None"
            ]
            sepa_debit: NotRequired[
                "PaymentIntent.CreateParamsPaymentMethodDataSepaDebit|None"
            ]
            sofort: NotRequired[
                "PaymentIntent.CreateParamsPaymentMethodDataSofort|None"
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
                "PaymentIntent.CreateParamsPaymentMethodDataUsBankAccount|None"
            ]
            wechat_pay: NotRequired[
                "PaymentIntent.CreateParamsPaymentMethodDataWechatPay|None"
            ]
            zip: NotRequired[
                "PaymentIntent.CreateParamsPaymentMethodDataZip|None"
            ]

        class CreateParamsPaymentMethodDataZip(TypedDict):
            pass

        class CreateParamsPaymentMethodDataWechatPay(TypedDict):
            pass

        class CreateParamsPaymentMethodDataUsBankAccount(TypedDict):
            account_holder_type: NotRequired[
                "Literal['company', 'individual']|None"
            ]
            account_number: NotRequired["str|None"]
            account_type: NotRequired["Literal['checking', 'savings']|None"]
            financial_connections_account: NotRequired["str|None"]
            routing_number: NotRequired["str|None"]

        class CreateParamsPaymentMethodDataSofort(TypedDict):
            country: Literal["AT", "BE", "DE", "ES", "IT", "NL"]

        class CreateParamsPaymentMethodDataSepaDebit(TypedDict):
            iban: str

        class CreateParamsPaymentMethodDataRadarOptions(TypedDict):
            session: NotRequired["str|None"]

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
                "Literal['alior_bank', 'bank_millennium', 'bank_nowy_bfg_sa', 'bank_pekao_sa', 'banki_spbdzielcze', 'blik', 'bnp_paribas', 'boz', 'citi_handlowy', 'credit_agricole', 'envelobank', 'etransfer_pocztowy24', 'getin_bank', 'ideabank', 'ing', 'inteligo', 'mbank_mtransfer', 'nest_przelew', 'noble_pay', 'pbac_z_ipko', 'plus_bank', 'santander_przelew24', 'tmobile_usbugi_bankowe', 'toyota_bank', 'volkswagen_bank']|None"
            ]

        class CreateParamsPaymentMethodDataOxxo(TypedDict):
            pass

        class CreateParamsPaymentMethodDataLink(TypedDict):
            pass

        class CreateParamsPaymentMethodDataKonbini(TypedDict):
            pass

        class CreateParamsPaymentMethodDataKlarna(TypedDict):
            dob: NotRequired[
                "PaymentIntent.CreateParamsPaymentMethodDataKlarnaDob|None"
            ]

        class CreateParamsPaymentMethodDataKlarnaDob(TypedDict):
            day: int
            month: int
            year: int

        class CreateParamsPaymentMethodDataInteracPresent(TypedDict):
            pass

        class CreateParamsPaymentMethodDataIdeal(TypedDict):
            bank: NotRequired[
                "Literal['abn_amro', 'asn_bank', 'bunq', 'handelsbanken', 'ing', 'knab', 'moneyou', 'n26', 'rabobank', 'regiobank', 'revolut', 'sns_bank', 'triodos_bank', 'van_lanschot', 'yoursafe']|None"
            ]

        class CreateParamsPaymentMethodDataGrabpay(TypedDict):
            pass

        class CreateParamsPaymentMethodDataGiropay(TypedDict):
            pass

        class CreateParamsPaymentMethodDataFpx(TypedDict):
            account_holder_type: NotRequired[
                "Literal['company', 'individual']|None"
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
                "Literal['arzte_und_apotheker_bank', 'austrian_anadi_bank_ag', 'bank_austria', 'bankhaus_carl_spangler', 'bankhaus_schelhammer_und_schattera_ag', 'bawag_psk_ag', 'bks_bank_ag', 'brull_kallmus_bank_ag', 'btv_vier_lander_bank', 'capital_bank_grawe_gruppe_ag', 'deutsche_bank_ag', 'dolomitenbank', 'easybank_ag', 'erste_bank_und_sparkassen', 'hypo_alpeadriabank_international_ag', 'hypo_bank_burgenland_aktiengesellschaft', 'hypo_noe_lb_fur_niederosterreich_u_wien', 'hypo_oberosterreich_salzburg_steiermark', 'hypo_tirol_bank_ag', 'hypo_vorarlberg_bank_ag', 'marchfelder_bank', 'oberbank_ag', 'raiffeisen_bankengruppe_osterreich', 'schoellerbank_ag', 'sparda_bank_wien', 'volksbank_gruppe', 'volkskreditbank_ag', 'vr_bank_braunau']|None"
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
                "Literal['']|PaymentIntent.CreateParamsPaymentMethodDataBillingDetailsAddress|None"
            ]
            email: NotRequired["Literal['']|str|None"]
            name: NotRequired["Literal['']|str|None"]
            phone: NotRequired["Literal['']|str|None"]

        class CreateParamsPaymentMethodDataBillingDetailsAddress(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]

        class CreateParamsPaymentMethodDataBancontact(TypedDict):
            pass

        class CreateParamsPaymentMethodDataBacsDebit(TypedDict):
            account_number: NotRequired["str|None"]
            sort_code: NotRequired["str|None"]

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
            accepted_at: NotRequired["int|None"]
            offline: NotRequired[
                "PaymentIntent.CreateParamsMandateDataCustomerAcceptanceOffline|None"
            ]
            online: NotRequired[
                "PaymentIntent.CreateParamsMandateDataCustomerAcceptanceOnline|None"
            ]
            type: Literal["offline", "online"]

        class CreateParamsMandateDataCustomerAcceptanceOnline(TypedDict):
            ip_address: str
            user_agent: str

        class CreateParamsMandateDataCustomerAcceptanceOffline(TypedDict):
            pass

        class CreateParamsAutomaticPaymentMethods(TypedDict):
            allow_redirects: NotRequired["Literal['always', 'never']|None"]
            enabled: bool

        class IncrementAuthorizationParams(RequestOptions):
            amount: int
            application_fee_amount: NotRequired["int|None"]
            description: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            metadata: NotRequired["Dict[str, str]|None"]
            statement_descriptor: NotRequired["str|None"]
            transfer_data: NotRequired[
                "PaymentIntent.IncrementAuthorizationParamsTransferData|None"
            ]

        class IncrementAuthorizationParamsTransferData(TypedDict):
            amount: NotRequired["int|None"]

        class ListParams(RequestOptions):
            created: NotRequired["PaymentIntent.ListParamsCreated|int|None"]
            customer: NotRequired["str|None"]
            ending_before: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            starting_after: NotRequired["str|None"]

        class ListParamsCreated(TypedDict):
            gt: NotRequired["int|None"]
            gte: NotRequired["int|None"]
            lt: NotRequired["int|None"]
            lte: NotRequired["int|None"]

        class ModifyParams(RequestOptions):
            amount: NotRequired["int|None"]
            application_fee_amount: NotRequired["Literal['']|int|None"]
            capture_method: NotRequired[
                "Literal['automatic', 'automatic_async', 'manual']|None"
            ]
            currency: NotRequired["str|None"]
            customer: NotRequired["str|None"]
            description: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            payment_method: NotRequired["str|None"]
            payment_method_configuration: NotRequired["str|None"]
            payment_method_data: NotRequired[
                "PaymentIntent.ModifyParamsPaymentMethodData|None"
            ]
            payment_method_options: NotRequired[
                "PaymentIntent.ModifyParamsPaymentMethodOptions|None"
            ]
            payment_method_types: NotRequired["List[str]|None"]
            receipt_email: NotRequired["Literal['']|str|None"]
            setup_future_usage: NotRequired[
                "Literal['']|Literal['off_session', 'on_session']|None"
            ]
            shipping: NotRequired[
                "Literal['']|PaymentIntent.ModifyParamsShipping|None"
            ]
            statement_descriptor: NotRequired["str|None"]
            statement_descriptor_suffix: NotRequired["str|None"]
            transfer_data: NotRequired[
                "PaymentIntent.ModifyParamsTransferData|None"
            ]
            transfer_group: NotRequired["str|None"]

        class ModifyParamsTransferData(TypedDict):
            amount: NotRequired["int|None"]

        class ModifyParamsShipping(TypedDict):
            address: "PaymentIntent.ModifyParamsShippingAddress"
            carrier: NotRequired["str|None"]
            name: str
            phone: NotRequired["str|None"]
            tracking_number: NotRequired["str|None"]

        class ModifyParamsShippingAddress(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]

        class ModifyParamsPaymentMethodOptions(TypedDict):
            acss_debit: NotRequired[
                "Literal['']|PaymentIntent.ModifyParamsPaymentMethodOptionsAcssDebit|None"
            ]
            affirm: NotRequired[
                "Literal['']|PaymentIntent.ModifyParamsPaymentMethodOptionsAffirm|None"
            ]
            afterpay_clearpay: NotRequired[
                "Literal['']|PaymentIntent.ModifyParamsPaymentMethodOptionsAfterpayClearpay|None"
            ]
            alipay: NotRequired[
                "Literal['']|PaymentIntent.ModifyParamsPaymentMethodOptionsAlipay|None"
            ]
            au_becs_debit: NotRequired[
                "Literal['']|PaymentIntent.ModifyParamsPaymentMethodOptionsAuBecsDebit|None"
            ]
            bacs_debit: NotRequired[
                "Literal['']|PaymentIntent.ModifyParamsPaymentMethodOptionsBacsDebit|None"
            ]
            bancontact: NotRequired[
                "Literal['']|PaymentIntent.ModifyParamsPaymentMethodOptionsBancontact|None"
            ]
            blik: NotRequired[
                "Literal['']|PaymentIntent.ModifyParamsPaymentMethodOptionsBlik|None"
            ]
            boleto: NotRequired[
                "Literal['']|PaymentIntent.ModifyParamsPaymentMethodOptionsBoleto|None"
            ]
            card: NotRequired[
                "Literal['']|PaymentIntent.ModifyParamsPaymentMethodOptionsCard|None"
            ]
            card_present: NotRequired[
                "Literal['']|PaymentIntent.ModifyParamsPaymentMethodOptionsCardPresent|None"
            ]
            cashapp: NotRequired[
                "Literal['']|PaymentIntent.ModifyParamsPaymentMethodOptionsCashapp|None"
            ]
            customer_balance: NotRequired[
                "Literal['']|PaymentIntent.ModifyParamsPaymentMethodOptionsCustomerBalance|None"
            ]
            eps: NotRequired[
                "Literal['']|PaymentIntent.ModifyParamsPaymentMethodOptionsEps|None"
            ]
            fpx: NotRequired[
                "Literal['']|PaymentIntent.ModifyParamsPaymentMethodOptionsFpx|None"
            ]
            giropay: NotRequired[
                "Literal['']|PaymentIntent.ModifyParamsPaymentMethodOptionsGiropay|None"
            ]
            grabpay: NotRequired[
                "Literal['']|PaymentIntent.ModifyParamsPaymentMethodOptionsGrabpay|None"
            ]
            ideal: NotRequired[
                "Literal['']|PaymentIntent.ModifyParamsPaymentMethodOptionsIdeal|None"
            ]
            interac_present: NotRequired[
                "Literal['']|PaymentIntent.ModifyParamsPaymentMethodOptionsInteracPresent|None"
            ]
            klarna: NotRequired[
                "Literal['']|PaymentIntent.ModifyParamsPaymentMethodOptionsKlarna|None"
            ]
            konbini: NotRequired[
                "Literal['']|PaymentIntent.ModifyParamsPaymentMethodOptionsKonbini|None"
            ]
            link: NotRequired[
                "Literal['']|PaymentIntent.ModifyParamsPaymentMethodOptionsLink|None"
            ]
            oxxo: NotRequired[
                "Literal['']|PaymentIntent.ModifyParamsPaymentMethodOptionsOxxo|None"
            ]
            p24: NotRequired[
                "Literal['']|PaymentIntent.ModifyParamsPaymentMethodOptionsP24|None"
            ]
            paynow: NotRequired[
                "Literal['']|PaymentIntent.ModifyParamsPaymentMethodOptionsPaynow|None"
            ]
            paypal: NotRequired[
                "Literal['']|PaymentIntent.ModifyParamsPaymentMethodOptionsPaypal|None"
            ]
            pix: NotRequired[
                "Literal['']|PaymentIntent.ModifyParamsPaymentMethodOptionsPix|None"
            ]
            promptpay: NotRequired[
                "Literal['']|PaymentIntent.ModifyParamsPaymentMethodOptionsPromptpay|None"
            ]
            sepa_debit: NotRequired[
                "Literal['']|PaymentIntent.ModifyParamsPaymentMethodOptionsSepaDebit|None"
            ]
            sofort: NotRequired[
                "Literal['']|PaymentIntent.ModifyParamsPaymentMethodOptionsSofort|None"
            ]
            us_bank_account: NotRequired[
                "Literal['']|PaymentIntent.ModifyParamsPaymentMethodOptionsUsBankAccount|None"
            ]
            wechat_pay: NotRequired[
                "Literal['']|PaymentIntent.ModifyParamsPaymentMethodOptionsWechatPay|None"
            ]
            zip: NotRequired[
                "Literal['']|PaymentIntent.ModifyParamsPaymentMethodOptionsZip|None"
            ]

        class ModifyParamsPaymentMethodOptionsZip(TypedDict):
            setup_future_usage: NotRequired["Literal['none']|None"]

        class ModifyParamsPaymentMethodOptionsWechatPay(TypedDict):
            app_id: NotRequired["str|None"]
            client: Literal["android", "ios", "web"]
            setup_future_usage: NotRequired["Literal['none']|None"]

        class ModifyParamsPaymentMethodOptionsUsBankAccount(TypedDict):
            financial_connections: NotRequired[
                "PaymentIntent.ModifyParamsPaymentMethodOptionsUsBankAccountFinancialConnections|None"
            ]
            networks: NotRequired[
                "PaymentIntent.ModifyParamsPaymentMethodOptionsUsBankAccountNetworks|None"
            ]
            preferred_settlement_speed: NotRequired[
                "Literal['']|Literal['fastest', 'standard']|None"
            ]
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session', 'on_session']|None"
            ]
            verification_method: NotRequired[
                "Literal['automatic', 'instant', 'microdeposits']|None"
            ]

        class ModifyParamsPaymentMethodOptionsUsBankAccountNetworks(TypedDict):
            requested: NotRequired[
                "List[Literal['ach', 'us_domestic_wire']]|None"
            ]

        class ModifyParamsPaymentMethodOptionsUsBankAccountFinancialConnections(
            TypedDict,
        ):
            permissions: NotRequired[
                "List[Literal['balances', 'ownership', 'payment_method', 'transactions']]|None"
            ]
            prefetch: NotRequired["List[Literal['balances']]|None"]
            return_url: NotRequired["str|None"]

        class ModifyParamsPaymentMethodOptionsSofort(TypedDict):
            preferred_language: NotRequired[
                "Literal['']|Literal['de', 'en', 'es', 'fr', 'it', 'nl', 'pl']|None"
            ]
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session']|None"
            ]

        class ModifyParamsPaymentMethodOptionsSepaDebit(TypedDict):
            mandate_options: NotRequired[
                "PaymentIntent.ModifyParamsPaymentMethodOptionsSepaDebitMandateOptions|None"
            ]
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session', 'on_session']|None"
            ]

        class ModifyParamsPaymentMethodOptionsSepaDebitMandateOptions(
            TypedDict,
        ):
            pass

        class ModifyParamsPaymentMethodOptionsPromptpay(TypedDict):
            setup_future_usage: NotRequired["Literal['none']|None"]

        class ModifyParamsPaymentMethodOptionsPix(TypedDict):
            expires_after_seconds: NotRequired["int|None"]
            expires_at: NotRequired["int|None"]
            setup_future_usage: NotRequired["Literal['none']|None"]

        class ModifyParamsPaymentMethodOptionsPaypal(TypedDict):
            capture_method: NotRequired["Literal['']|Literal['manual']|None"]
            preferred_locale: NotRequired[
                "Literal['cs-CZ', 'da-DK', 'de-AT', 'de-DE', 'de-LU', 'el-GR', 'en-GB', 'en-US', 'es-ES', 'fi-FI', 'fr-BE', 'fr-FR', 'fr-LU', 'hu-HU', 'it-IT', 'nl-BE', 'nl-NL', 'pl-PL', 'pt-PT', 'sk-SK', 'sv-SE']|None"
            ]
            reference: NotRequired["str|None"]
            risk_correlation_id: NotRequired["str|None"]
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session']|None"
            ]

        class ModifyParamsPaymentMethodOptionsPaynow(TypedDict):
            setup_future_usage: NotRequired["Literal['none']|None"]

        class ModifyParamsPaymentMethodOptionsP24(TypedDict):
            setup_future_usage: NotRequired["Literal['none']|None"]
            tos_shown_and_accepted: NotRequired["bool|None"]

        class ModifyParamsPaymentMethodOptionsOxxo(TypedDict):
            expires_after_days: NotRequired["int|None"]
            setup_future_usage: NotRequired["Literal['none']|None"]

        class ModifyParamsPaymentMethodOptionsLink(TypedDict):
            capture_method: NotRequired["Literal['']|Literal['manual']|None"]
            persistent_token: NotRequired["str|None"]
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session']|None"
            ]

        class ModifyParamsPaymentMethodOptionsKonbini(TypedDict):
            confirmation_number: NotRequired["Literal['']|str|None"]
            expires_after_days: NotRequired["Literal['']|int|None"]
            expires_at: NotRequired["Literal['']|int|None"]
            product_description: NotRequired["Literal['']|str|None"]
            setup_future_usage: NotRequired["Literal['none']|None"]

        class ModifyParamsPaymentMethodOptionsKlarna(TypedDict):
            capture_method: NotRequired["Literal['']|Literal['manual']|None"]
            preferred_locale: NotRequired[
                "Literal['cs-CZ', 'da-DK', 'de-AT', 'de-CH', 'de-DE', 'el-GR', 'en-AT', 'en-AU', 'en-BE', 'en-CA', 'en-CH', 'en-CZ', 'en-DE', 'en-DK', 'en-ES', 'en-FI', 'en-FR', 'en-GB', 'en-GR', 'en-IE', 'en-IT', 'en-NL', 'en-NO', 'en-NZ', 'en-PL', 'en-PT', 'en-SE', 'en-US', 'es-ES', 'es-US', 'fi-FI', 'fr-BE', 'fr-CA', 'fr-CH', 'fr-FR', 'it-CH', 'it-IT', 'nb-NO', 'nl-BE', 'nl-NL', 'pl-PL', 'pt-PT', 'sv-FI', 'sv-SE']|None"
            ]
            setup_future_usage: NotRequired["Literal['none']|None"]

        class ModifyParamsPaymentMethodOptionsInteracPresent(TypedDict):
            pass

        class ModifyParamsPaymentMethodOptionsIdeal(TypedDict):
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session']|None"
            ]

        class ModifyParamsPaymentMethodOptionsGrabpay(TypedDict):
            setup_future_usage: NotRequired["Literal['none']|None"]

        class ModifyParamsPaymentMethodOptionsGiropay(TypedDict):
            setup_future_usage: NotRequired["Literal['none']|None"]

        class ModifyParamsPaymentMethodOptionsFpx(TypedDict):
            setup_future_usage: NotRequired["Literal['none']|None"]

        class ModifyParamsPaymentMethodOptionsEps(TypedDict):
            setup_future_usage: NotRequired["Literal['none']|None"]

        class ModifyParamsPaymentMethodOptionsCustomerBalance(TypedDict):
            bank_transfer: NotRequired[
                "PaymentIntent.ModifyParamsPaymentMethodOptionsCustomerBalanceBankTransfer|None"
            ]
            funding_type: NotRequired["Literal['bank_transfer']|None"]
            setup_future_usage: NotRequired["Literal['none']|None"]

        class ModifyParamsPaymentMethodOptionsCustomerBalanceBankTransfer(
            TypedDict,
        ):
            eu_bank_transfer: NotRequired[
                "PaymentIntent.ModifyParamsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer|None"
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

        class ModifyParamsPaymentMethodOptionsCustomerBalanceBankTransferEuBankTransfer(
            TypedDict,
        ):
            country: str

        class ModifyParamsPaymentMethodOptionsCashapp(TypedDict):
            capture_method: NotRequired["Literal['']|Literal['manual']|None"]
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session', 'on_session']|None"
            ]

        class ModifyParamsPaymentMethodOptionsCardPresent(TypedDict):
            request_extended_authorization: NotRequired["bool|None"]
            request_incremental_authorization: NotRequired[
                "Literal['if_available', 'never']|None"
            ]
            request_incremental_authorization_support: NotRequired["bool|None"]

        class ModifyParamsPaymentMethodOptionsCard(TypedDict):
            capture_method: NotRequired["Literal['']|Literal['manual']|None"]
            cvc_token: NotRequired["str|None"]
            installments: NotRequired[
                "PaymentIntent.ModifyParamsPaymentMethodOptionsCardInstallments|None"
            ]
            mandate_options: NotRequired[
                "PaymentIntent.ModifyParamsPaymentMethodOptionsCardMandateOptions|None"
            ]
            moto: NotRequired["bool|None"]
            network: NotRequired[
                "Literal['amex', 'cartes_bancaires', 'diners', 'discover', 'eftpos_au', 'interac', 'jcb', 'mastercard', 'unionpay', 'unknown', 'visa']|None"
            ]
            request_extended_authorization: NotRequired[
                "Literal['if_available', 'never']|None"
            ]
            request_incremental_authorization: NotRequired[
                "Literal['if_available', 'never']|None"
            ]
            request_multicapture: NotRequired[
                "Literal['if_available', 'never']|None"
            ]
            request_overcapture: NotRequired[
                "Literal['if_available', 'never']|None"
            ]
            request_three_d_secure: NotRequired[
                "Literal['any', 'automatic']|None"
            ]
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session', 'on_session']|None"
            ]
            statement_descriptor_suffix_kana: NotRequired[
                "Literal['']|str|None"
            ]
            statement_descriptor_suffix_kanji: NotRequired[
                "Literal['']|str|None"
            ]

        class ModifyParamsPaymentMethodOptionsCardMandateOptions(TypedDict):
            amount: int
            amount_type: Literal["fixed", "maximum"]
            description: NotRequired["str|None"]
            end_date: NotRequired["int|None"]
            interval: Literal["day", "month", "sporadic", "week", "year"]
            interval_count: NotRequired["int|None"]
            reference: str
            start_date: int
            supported_types: NotRequired["List[Literal['india']]|None"]

        class ModifyParamsPaymentMethodOptionsCardInstallments(TypedDict):
            enabled: NotRequired["bool|None"]
            plan: NotRequired[
                "Literal['']|PaymentIntent.ModifyParamsPaymentMethodOptionsCardInstallmentsPlan|None"
            ]

        class ModifyParamsPaymentMethodOptionsCardInstallmentsPlan(TypedDict):
            count: int
            interval: Literal["month"]
            type: Literal["fixed_count"]

        class ModifyParamsPaymentMethodOptionsBoleto(TypedDict):
            expires_after_days: NotRequired["int|None"]
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session', 'on_session']|None"
            ]

        class ModifyParamsPaymentMethodOptionsBlik(TypedDict):
            code: NotRequired["str|None"]

        class ModifyParamsPaymentMethodOptionsBancontact(TypedDict):
            preferred_language: NotRequired[
                "Literal['de', 'en', 'fr', 'nl']|None"
            ]
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session']|None"
            ]

        class ModifyParamsPaymentMethodOptionsBacsDebit(TypedDict):
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session', 'on_session']|None"
            ]

        class ModifyParamsPaymentMethodOptionsAuBecsDebit(TypedDict):
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session', 'on_session']|None"
            ]

        class ModifyParamsPaymentMethodOptionsAlipay(TypedDict):
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session']|None"
            ]

        class ModifyParamsPaymentMethodOptionsAfterpayClearpay(TypedDict):
            capture_method: NotRequired["Literal['']|Literal['manual']|None"]
            reference: NotRequired["str|None"]
            setup_future_usage: NotRequired["Literal['none']|None"]

        class ModifyParamsPaymentMethodOptionsAffirm(TypedDict):
            capture_method: NotRequired["Literal['']|Literal['manual']|None"]
            preferred_locale: NotRequired["str|None"]
            setup_future_usage: NotRequired["Literal['none']|None"]

        class ModifyParamsPaymentMethodOptionsAcssDebit(TypedDict):
            mandate_options: NotRequired[
                "PaymentIntent.ModifyParamsPaymentMethodOptionsAcssDebitMandateOptions|None"
            ]
            setup_future_usage: NotRequired[
                "Literal['']|Literal['none', 'off_session', 'on_session']|None"
            ]
            verification_method: NotRequired[
                "Literal['automatic', 'instant', 'microdeposits']|None"
            ]

        class ModifyParamsPaymentMethodOptionsAcssDebitMandateOptions(
            TypedDict,
        ):
            custom_mandate_url: NotRequired["Literal['']|str|None"]
            interval_description: NotRequired["str|None"]
            payment_schedule: NotRequired[
                "Literal['combined', 'interval', 'sporadic']|None"
            ]
            transaction_type: NotRequired[
                "Literal['business', 'personal']|None"
            ]

        class ModifyParamsPaymentMethodData(TypedDict):
            acss_debit: NotRequired[
                "PaymentIntent.ModifyParamsPaymentMethodDataAcssDebit|None"
            ]
            affirm: NotRequired[
                "PaymentIntent.ModifyParamsPaymentMethodDataAffirm|None"
            ]
            afterpay_clearpay: NotRequired[
                "PaymentIntent.ModifyParamsPaymentMethodDataAfterpayClearpay|None"
            ]
            alipay: NotRequired[
                "PaymentIntent.ModifyParamsPaymentMethodDataAlipay|None"
            ]
            au_becs_debit: NotRequired[
                "PaymentIntent.ModifyParamsPaymentMethodDataAuBecsDebit|None"
            ]
            bacs_debit: NotRequired[
                "PaymentIntent.ModifyParamsPaymentMethodDataBacsDebit|None"
            ]
            bancontact: NotRequired[
                "PaymentIntent.ModifyParamsPaymentMethodDataBancontact|None"
            ]
            billing_details: NotRequired[
                "PaymentIntent.ModifyParamsPaymentMethodDataBillingDetails|None"
            ]
            blik: NotRequired[
                "PaymentIntent.ModifyParamsPaymentMethodDataBlik|None"
            ]
            boleto: NotRequired[
                "PaymentIntent.ModifyParamsPaymentMethodDataBoleto|None"
            ]
            cashapp: NotRequired[
                "PaymentIntent.ModifyParamsPaymentMethodDataCashapp|None"
            ]
            customer_balance: NotRequired[
                "PaymentIntent.ModifyParamsPaymentMethodDataCustomerBalance|None"
            ]
            eps: NotRequired[
                "PaymentIntent.ModifyParamsPaymentMethodDataEps|None"
            ]
            fpx: NotRequired[
                "PaymentIntent.ModifyParamsPaymentMethodDataFpx|None"
            ]
            giropay: NotRequired[
                "PaymentIntent.ModifyParamsPaymentMethodDataGiropay|None"
            ]
            grabpay: NotRequired[
                "PaymentIntent.ModifyParamsPaymentMethodDataGrabpay|None"
            ]
            ideal: NotRequired[
                "PaymentIntent.ModifyParamsPaymentMethodDataIdeal|None"
            ]
            interac_present: NotRequired[
                "PaymentIntent.ModifyParamsPaymentMethodDataInteracPresent|None"
            ]
            klarna: NotRequired[
                "PaymentIntent.ModifyParamsPaymentMethodDataKlarna|None"
            ]
            konbini: NotRequired[
                "PaymentIntent.ModifyParamsPaymentMethodDataKonbini|None"
            ]
            link: NotRequired[
                "PaymentIntent.ModifyParamsPaymentMethodDataLink|None"
            ]
            metadata: NotRequired["Dict[str, str]|None"]
            oxxo: NotRequired[
                "PaymentIntent.ModifyParamsPaymentMethodDataOxxo|None"
            ]
            p24: NotRequired[
                "PaymentIntent.ModifyParamsPaymentMethodDataP24|None"
            ]
            paynow: NotRequired[
                "PaymentIntent.ModifyParamsPaymentMethodDataPaynow|None"
            ]
            paypal: NotRequired[
                "PaymentIntent.ModifyParamsPaymentMethodDataPaypal|None"
            ]
            pix: NotRequired[
                "PaymentIntent.ModifyParamsPaymentMethodDataPix|None"
            ]
            promptpay: NotRequired[
                "PaymentIntent.ModifyParamsPaymentMethodDataPromptpay|None"
            ]
            radar_options: NotRequired[
                "PaymentIntent.ModifyParamsPaymentMethodDataRadarOptions|None"
            ]
            sepa_debit: NotRequired[
                "PaymentIntent.ModifyParamsPaymentMethodDataSepaDebit|None"
            ]
            sofort: NotRequired[
                "PaymentIntent.ModifyParamsPaymentMethodDataSofort|None"
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
                "PaymentIntent.ModifyParamsPaymentMethodDataUsBankAccount|None"
            ]
            wechat_pay: NotRequired[
                "PaymentIntent.ModifyParamsPaymentMethodDataWechatPay|None"
            ]
            zip: NotRequired[
                "PaymentIntent.ModifyParamsPaymentMethodDataZip|None"
            ]

        class ModifyParamsPaymentMethodDataZip(TypedDict):
            pass

        class ModifyParamsPaymentMethodDataWechatPay(TypedDict):
            pass

        class ModifyParamsPaymentMethodDataUsBankAccount(TypedDict):
            account_holder_type: NotRequired[
                "Literal['company', 'individual']|None"
            ]
            account_number: NotRequired["str|None"]
            account_type: NotRequired["Literal['checking', 'savings']|None"]
            financial_connections_account: NotRequired["str|None"]
            routing_number: NotRequired["str|None"]

        class ModifyParamsPaymentMethodDataSofort(TypedDict):
            country: Literal["AT", "BE", "DE", "ES", "IT", "NL"]

        class ModifyParamsPaymentMethodDataSepaDebit(TypedDict):
            iban: str

        class ModifyParamsPaymentMethodDataRadarOptions(TypedDict):
            session: NotRequired["str|None"]

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
                "Literal['alior_bank', 'bank_millennium', 'bank_nowy_bfg_sa', 'bank_pekao_sa', 'banki_spbdzielcze', 'blik', 'bnp_paribas', 'boz', 'citi_handlowy', 'credit_agricole', 'envelobank', 'etransfer_pocztowy24', 'getin_bank', 'ideabank', 'ing', 'inteligo', 'mbank_mtransfer', 'nest_przelew', 'noble_pay', 'pbac_z_ipko', 'plus_bank', 'santander_przelew24', 'tmobile_usbugi_bankowe', 'toyota_bank', 'volkswagen_bank']|None"
            ]

        class ModifyParamsPaymentMethodDataOxxo(TypedDict):
            pass

        class ModifyParamsPaymentMethodDataLink(TypedDict):
            pass

        class ModifyParamsPaymentMethodDataKonbini(TypedDict):
            pass

        class ModifyParamsPaymentMethodDataKlarna(TypedDict):
            dob: NotRequired[
                "PaymentIntent.ModifyParamsPaymentMethodDataKlarnaDob|None"
            ]

        class ModifyParamsPaymentMethodDataKlarnaDob(TypedDict):
            day: int
            month: int
            year: int

        class ModifyParamsPaymentMethodDataInteracPresent(TypedDict):
            pass

        class ModifyParamsPaymentMethodDataIdeal(TypedDict):
            bank: NotRequired[
                "Literal['abn_amro', 'asn_bank', 'bunq', 'handelsbanken', 'ing', 'knab', 'moneyou', 'n26', 'rabobank', 'regiobank', 'revolut', 'sns_bank', 'triodos_bank', 'van_lanschot', 'yoursafe']|None"
            ]

        class ModifyParamsPaymentMethodDataGrabpay(TypedDict):
            pass

        class ModifyParamsPaymentMethodDataGiropay(TypedDict):
            pass

        class ModifyParamsPaymentMethodDataFpx(TypedDict):
            account_holder_type: NotRequired[
                "Literal['company', 'individual']|None"
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
                "Literal['arzte_und_apotheker_bank', 'austrian_anadi_bank_ag', 'bank_austria', 'bankhaus_carl_spangler', 'bankhaus_schelhammer_und_schattera_ag', 'bawag_psk_ag', 'bks_bank_ag', 'brull_kallmus_bank_ag', 'btv_vier_lander_bank', 'capital_bank_grawe_gruppe_ag', 'deutsche_bank_ag', 'dolomitenbank', 'easybank_ag', 'erste_bank_und_sparkassen', 'hypo_alpeadriabank_international_ag', 'hypo_bank_burgenland_aktiengesellschaft', 'hypo_noe_lb_fur_niederosterreich_u_wien', 'hypo_oberosterreich_salzburg_steiermark', 'hypo_tirol_bank_ag', 'hypo_vorarlberg_bank_ag', 'marchfelder_bank', 'oberbank_ag', 'raiffeisen_bankengruppe_osterreich', 'schoellerbank_ag', 'sparda_bank_wien', 'volksbank_gruppe', 'volkskreditbank_ag', 'vr_bank_braunau']|None"
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
                "Literal['']|PaymentIntent.ModifyParamsPaymentMethodDataBillingDetailsAddress|None"
            ]
            email: NotRequired["Literal['']|str|None"]
            name: NotRequired["Literal['']|str|None"]
            phone: NotRequired["Literal['']|str|None"]

        class ModifyParamsPaymentMethodDataBillingDetailsAddress(TypedDict):
            city: NotRequired["str|None"]
            country: NotRequired["str|None"]
            line1: NotRequired["str|None"]
            line2: NotRequired["str|None"]
            postal_code: NotRequired["str|None"]
            state: NotRequired["str|None"]

        class ModifyParamsPaymentMethodDataBancontact(TypedDict):
            pass

        class ModifyParamsPaymentMethodDataBacsDebit(TypedDict):
            account_number: NotRequired["str|None"]
            sort_code: NotRequired["str|None"]

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
            client_secret: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]

        class VerifyMicrodepositsParams(RequestOptions):
            amounts: NotRequired["List[int]|None"]
            descriptor_code: NotRequired["str|None"]
            expand: NotRequired["List[str]|None"]

        class SearchParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            limit: NotRequired["int|None"]
            page: NotRequired["str|None"]
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
    source: Optional[
        ExpandableField[Union["Account", "BankAccount", "Card", "Source"]]
    ]
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
    def search_auto_paging_iter(
        cls, *args, **kwargs: Unpack["PaymentIntent.SearchParams"]
    ):
        return cls.search(*args, **kwargs).auto_paging_iter()
