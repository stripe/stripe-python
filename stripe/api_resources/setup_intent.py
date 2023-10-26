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
    from stripe.api_resources.customer import Customer
    from stripe.api_resources.mandate import Mandate
    from stripe.api_resources.payment_method import PaymentMethod
    from stripe.api_resources.setup_attempt import SetupAttempt


class SetupIntent(
    CreateableAPIResource["SetupIntent"],
    ListableAPIResource["SetupIntent"],
    UpdateableAPIResource["SetupIntent"],
):
    """
    A SetupIntent guides you through the process of setting up and saving a customer's payment credentials for future payments.
    For example, you can use a SetupIntent to set up and save your customer's card without immediately collecting a payment.
    Later, you can use [PaymentIntents](https://stripe.com/docs/api#payment_intents) to drive the payment flow.

    Create a SetupIntent when you're ready to collect your customer's payment credentials.
    Don't maintain long-lived, unconfirmed SetupIntents because they might not be valid.
    The SetupIntent transitions through multiple [statuses](https://stripe.com/docs/payments/intents#intent-statuses) as it guides
    you through the setup process.

    Successful SetupIntents result in payment credentials that are optimized for future payments.
    For example, cardholders in [certain regions](https://stripe.com/guides/strong-customer-authentication) might need to be run through
    [Strong Customer Authentication](https://stripe.com/docs/strong-customer-authentication) during payment method collection
    to streamline later [off-session payments](https://stripe.com/docs/payments/setup-intents).
    If you use the SetupIntent with a [Customer](https://stripe.com/docs/api#setup_intent_object-customer),
    it automatically attaches the resulting payment method to that Customer after successful setup.
    We recommend using SetupIntents or [setup_future_usage](https://stripe.com/docs/api#payment_intent_object-setup_future_usage) on
    PaymentIntents to save payment methods to prevent saving invalid or unoptimized payment methods.

    By using SetupIntents, you can reduce friction for your customers, even as regulations change over time.

    Related guide: [Setup Intents API](https://stripe.com/docs/payments/setup-intents)
    """

    OBJECT_NAME: ClassVar[Literal["setup_intent"]] = "setup_intent"
    if TYPE_CHECKING:

        class CancelParams(RequestOptions):
            cancellation_reason: NotRequired[
                "Literal['abandoned', 'duplicate', 'requested_by_customer']|None"
            ]
            """
            Reason for canceling this SetupIntent. Possible values are: `abandoned`, `requested_by_customer`, or `duplicate`
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

        class ConfirmParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            mandate_data: NotRequired[
                "Literal['']|SetupIntent.ConfirmParamsMandateData|SetupIntent.ConfirmParamsMandateData2|None"
            ]
            payment_method: NotRequired["str|None"]
            """
            ID of the payment method (a PaymentMethod, Card, or saved Source object) to attach to this SetupIntent.
            """
            payment_method_data: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodData|None"
            ]
            """
            When included, this hash creates a PaymentMethod that is set as the [`payment_method`](https://stripe.com/docs/api/setup_intents/object#setup_intent_object-payment_method)
            value in the SetupIntent.
            """
            payment_method_options: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodOptions|None"
            ]
            """
            Payment method-specific configuration for this SetupIntent.
            """
            return_url: NotRequired["str|None"]
            """
            The URL to redirect your customer back to after they authenticate on the payment method's app or site.
            If you'd prefer to redirect to a mobile application, you can alternatively supply an application URI scheme.
            This parameter is only used for cards and other redirect-based payment methods.
            """
            use_stripe_sdk: NotRequired["bool|None"]
            """
            Set to `true` when confirming server-side and using Stripe.js, iOS, or Android client-side SDKs to handle the next actions.
            """

        class ConfirmParamsPaymentMethodOptions(TypedDict):
            acss_debit: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodOptionsAcssDebit|None"
            ]
            """
            If this is a `acss_debit` SetupIntent, this sub-hash contains details about the ACSS Debit payment method options.
            """
            card: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodOptionsCard|None"
            ]
            """
            Configuration for any card setup attempted on this SetupIntent.
            """
            link: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodOptionsLink|None"
            ]
            """
            If this is a `link` PaymentMethod, this sub-hash contains details about the Link payment method options.
            """
            paypal: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodOptionsPaypal|None"
            ]
            """
            If this is a `paypal` PaymentMethod, this sub-hash contains details about the PayPal payment method options.
            """
            sepa_debit: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodOptionsSepaDebit|None"
            ]
            """
            If this is a `sepa_debit` SetupIntent, this sub-hash contains details about the SEPA Debit payment method options.
            """
            us_bank_account: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodOptionsUsBankAccount|None"
            ]
            """
            If this is a `us_bank_account` SetupIntent, this sub-hash contains details about the US bank account payment method options.
            """

        class ConfirmParamsPaymentMethodOptionsUsBankAccount(TypedDict):
            financial_connections: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodOptionsUsBankAccountFinancialConnections|None"
            ]
            """
            Additional fields for Financial Connections Session creation
            """
            networks: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodOptionsUsBankAccountNetworks|None"
            ]
            """
            Additional fields for network related functions
            """
            verification_method: NotRequired[
                "Literal['automatic', 'instant', 'microdeposits']|None"
            ]
            """
            Verification method for the intent
            """

        class ConfirmParamsPaymentMethodOptionsUsBankAccountNetworks(
            TypedDict
        ):
            requested: NotRequired[
                "List[Literal['ach', 'us_domestic_wire']]|None"
            ]
            """
            Triggers validations to run across the selected networks
            """

        class ConfirmParamsPaymentMethodOptionsUsBankAccountFinancialConnections(
            TypedDict,
        ):
            permissions: NotRequired[
                "List[Literal['balances', 'ownership', 'payment_method', 'transactions']]|None"
            ]
            """
            The list of permissions to request. If this parameter is passed, the `payment_method` permission must be included. Valid permissions include: `balances`, `ownership`, `payment_method`, and `transactions`.
            """
            prefetch: NotRequired["List[Literal['balances']]|None"]
            """
            List of data features that you would like to retrieve upon account creation.
            """
            return_url: NotRequired["str|None"]
            """
            For webview integrations only. Upon completing OAuth login in the native browser, the user will be redirected to this URL to return to your app.
            """

        class ConfirmParamsPaymentMethodOptionsSepaDebit(TypedDict):
            mandate_options: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodOptionsSepaDebitMandateOptions|None"
            ]
            """
            Additional fields for Mandate creation
            """

        class ConfirmParamsPaymentMethodOptionsSepaDebitMandateOptions(
            TypedDict,
        ):
            pass

        class ConfirmParamsPaymentMethodOptionsPaypal(TypedDict):
            billing_agreement_id: NotRequired["str|None"]
            """
            The PayPal Billing Agreement ID (BAID). This is an ID generated by PayPal which represents the mandate between the merchant and the customer.
            """

        class ConfirmParamsPaymentMethodOptionsLink(TypedDict):
            persistent_token: NotRequired["str|None"]
            """
            [Deprecated] This is a legacy parameter that no longer has any function.
            """

        class ConfirmParamsPaymentMethodOptionsCard(TypedDict):
            mandate_options: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodOptionsCardMandateOptions|None"
            ]
            """
            Configuration options for setting up an eMandate for cards issued in India.
            """
            moto: NotRequired["bool|None"]
            """
            When specified, this parameter signals that a card has been collected
            as MOTO (Mail Order Telephone Order) and thus out of scope for SCA. This
            parameter can only be provided during confirmation.
            """
            network: NotRequired[
                "Literal['amex', 'cartes_bancaires', 'diners', 'discover', 'eftpos_au', 'interac', 'jcb', 'mastercard', 'unionpay', 'unknown', 'visa']|None"
            ]
            """
            Selected network to process this SetupIntent on. Depends on the available networks of the card attached to the SetupIntent. Can be only set confirm-time.
            """
            request_three_d_secure: NotRequired[
                "Literal['any', 'automatic']|None"
            ]
            """
            We strongly recommend that you rely on our SCA Engine to automatically prompt your customers for authentication based on risk level and [other requirements](https://stripe.com/docs/strong-customer-authentication). However, if you wish to request 3D Secure based on logic from your own fraud engine, provide this option. Permitted values include: `automatic` or `any`. If not provided, defaults to `automatic`. Read our guide on [manually requesting 3D Secure](https://stripe.com/docs/payments/3d-secure#manual-three-ds) for more information on how this configuration interacts with Radar and our SCA Engine.
            """

        class ConfirmParamsPaymentMethodOptionsCardMandateOptions(TypedDict):
            amount: int
            """
            Amount to be charged for future payments.
            """
            amount_type: Literal["fixed", "maximum"]
            """
            One of `fixed` or `maximum`. If `fixed`, the `amount` param refers to the exact amount to be charged in future payments. If `maximum`, the amount charged can be up to the value passed for the `amount` param.
            """
            currency: str
            """
            Currency in which future payments will be charged. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """
            description: NotRequired["str|None"]
            """
            A description of the mandate or subscription that is meant to be displayed to the customer.
            """
            end_date: NotRequired["int|None"]
            """
            End date of the mandate or subscription. If not provided, the mandate will be active until canceled. If provided, end date should be after start date.
            """
            interval: Literal["day", "month", "sporadic", "week", "year"]
            """
            Specifies payment frequency. One of `day`, `week`, `month`, `year`, or `sporadic`.
            """
            interval_count: NotRequired["int|None"]
            """
            The number of intervals between payments. For example, `interval=month` and `interval_count=3` indicates one payment every three months. Maximum of one year interval allowed (1 year, 12 months, or 52 weeks). This parameter is optional when `interval=sporadic`.
            """
            reference: str
            """
            Unique identifier for the mandate or subscription.
            """
            start_date: int
            """
            Start date of the mandate or subscription. Start date should not be lesser than yesterday.
            """
            supported_types: NotRequired["List[Literal['india']]|None"]
            """
            Specifies the type of mandates supported. Possible values are `india`.
            """

        class ConfirmParamsPaymentMethodOptionsAcssDebit(TypedDict):
            currency: NotRequired["Literal['cad', 'usd']|None"]
            """
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """
            mandate_options: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodOptionsAcssDebitMandateOptions|None"
            ]
            """
            Additional fields for Mandate creation
            """
            verification_method: NotRequired[
                "Literal['automatic', 'instant', 'microdeposits']|None"
            ]
            """
            Verification method for the intent
            """

        class ConfirmParamsPaymentMethodOptionsAcssDebitMandateOptions(
            TypedDict,
        ):
            custom_mandate_url: NotRequired["Literal['']|str|None"]
            """
            A URL for custom mandate text to render during confirmation step.
            The URL will be rendered with additional GET parameters `payment_intent` and `payment_intent_client_secret` when confirming a Payment Intent,
            or `setup_intent` and `setup_intent_client_secret` when confirming a Setup Intent.
            """
            default_for: NotRequired[
                "List[Literal['invoice', 'subscription']]|None"
            ]
            """
            List of Stripe products where this mandate can be selected automatically.
            """
            interval_description: NotRequired["str|None"]
            """
            Description of the mandate interval. Only required if 'payment_schedule' parameter is 'interval' or 'combined'.
            """
            payment_schedule: NotRequired[
                "Literal['combined', 'interval', 'sporadic']|None"
            ]
            """
            Payment schedule for the mandate.
            """
            transaction_type: NotRequired[
                "Literal['business', 'personal']|None"
            ]
            """
            Transaction type of the mandate.
            """

        class ConfirmParamsPaymentMethodData(TypedDict):
            acss_debit: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataAcssDebit|None"
            ]
            """
            If this is an `acss_debit` PaymentMethod, this hash contains details about the ACSS Debit payment method.
            """
            affirm: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataAffirm|None"
            ]
            """
            If this is an `affirm` PaymentMethod, this hash contains details about the Affirm payment method.
            """
            afterpay_clearpay: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataAfterpayClearpay|None"
            ]
            """
            If this is an `AfterpayClearpay` PaymentMethod, this hash contains details about the AfterpayClearpay payment method.
            """
            alipay: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataAlipay|None"
            ]
            """
            If this is an `Alipay` PaymentMethod, this hash contains details about the Alipay payment method.
            """
            au_becs_debit: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataAuBecsDebit|None"
            ]
            """
            If this is an `au_becs_debit` PaymentMethod, this hash contains details about the bank account.
            """
            bacs_debit: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataBacsDebit|None"
            ]
            """
            If this is a `bacs_debit` PaymentMethod, this hash contains details about the Bacs Direct Debit bank account.
            """
            bancontact: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataBancontact|None"
            ]
            """
            If this is a `bancontact` PaymentMethod, this hash contains details about the Bancontact payment method.
            """
            billing_details: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataBillingDetails|None"
            ]
            """
            Billing information associated with the PaymentMethod that may be used or required by particular types of payment methods.
            """
            blik: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataBlik|None"
            ]
            """
            If this is a `blik` PaymentMethod, this hash contains details about the BLIK payment method.
            """
            boleto: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataBoleto|None"
            ]
            """
            If this is a `boleto` PaymentMethod, this hash contains details about the Boleto payment method.
            """
            cashapp: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataCashapp|None"
            ]
            """
            If this is a `cashapp` PaymentMethod, this hash contains details about the Cash App Pay payment method.
            """
            customer_balance: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataCustomerBalance|None"
            ]
            """
            If this is a `customer_balance` PaymentMethod, this hash contains details about the CustomerBalance payment method.
            """
            eps: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataEps|None"
            ]
            """
            If this is an `eps` PaymentMethod, this hash contains details about the EPS payment method.
            """
            fpx: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataFpx|None"
            ]
            """
            If this is an `fpx` PaymentMethod, this hash contains details about the FPX payment method.
            """
            giropay: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataGiropay|None"
            ]
            """
            If this is a `giropay` PaymentMethod, this hash contains details about the Giropay payment method.
            """
            grabpay: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataGrabpay|None"
            ]
            """
            If this is a `grabpay` PaymentMethod, this hash contains details about the GrabPay payment method.
            """
            ideal: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataIdeal|None"
            ]
            """
            If this is an `ideal` PaymentMethod, this hash contains details about the iDEAL payment method.
            """
            interac_present: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataInteracPresent|None"
            ]
            """
            If this is an `interac_present` PaymentMethod, this hash contains details about the Interac Present payment method.
            """
            klarna: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataKlarna|None"
            ]
            """
            If this is a `klarna` PaymentMethod, this hash contains details about the Klarna payment method.
            """
            konbini: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataKonbini|None"
            ]
            """
            If this is a `konbini` PaymentMethod, this hash contains details about the Konbini payment method.
            """
            link: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataLink|None"
            ]
            """
            If this is an `Link` PaymentMethod, this hash contains details about the Link payment method.
            """
            metadata: NotRequired["Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """
            oxxo: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataOxxo|None"
            ]
            """
            If this is an `oxxo` PaymentMethod, this hash contains details about the OXXO payment method.
            """
            p24: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataP24|None"
            ]
            """
            If this is a `p24` PaymentMethod, this hash contains details about the P24 payment method.
            """
            paynow: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataPaynow|None"
            ]
            """
            If this is a `paynow` PaymentMethod, this hash contains details about the PayNow payment method.
            """
            paypal: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataPaypal|None"
            ]
            """
            If this is a `paypal` PaymentMethod, this hash contains details about the PayPal payment method.
            """
            pix: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataPix|None"
            ]
            """
            If this is a `pix` PaymentMethod, this hash contains details about the Pix payment method.
            """
            promptpay: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataPromptpay|None"
            ]
            """
            If this is a `promptpay` PaymentMethod, this hash contains details about the PromptPay payment method.
            """
            radar_options: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataRadarOptions|None"
            ]
            """
            Options to configure Radar. See [Radar Session](https://stripe.com/docs/radar/radar-session) for more information.
            """
            sepa_debit: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataSepaDebit|None"
            ]
            """
            If this is a `sepa_debit` PaymentMethod, this hash contains details about the SEPA debit bank account.
            """
            sofort: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataSofort|None"
            ]
            """
            If this is a `sofort` PaymentMethod, this hash contains details about the SOFORT payment method.
            """
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
            """
            The type of the PaymentMethod. An additional hash is included on the PaymentMethod with a name matching this value. It contains additional information specific to the PaymentMethod type.
            """
            us_bank_account: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataUsBankAccount|None"
            ]
            """
            If this is an `us_bank_account` PaymentMethod, this hash contains details about the US bank account payment method.
            """
            wechat_pay: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataWechatPay|None"
            ]
            """
            If this is an `wechat_pay` PaymentMethod, this hash contains details about the wechat_pay payment method.
            """
            zip: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataZip|None"
            ]
            """
            If this is a `zip` PaymentMethod, this hash contains details about the Zip payment method.
            """

        class ConfirmParamsPaymentMethodDataZip(TypedDict):
            pass

        class ConfirmParamsPaymentMethodDataWechatPay(TypedDict):
            pass

        class ConfirmParamsPaymentMethodDataUsBankAccount(TypedDict):
            account_holder_type: NotRequired[
                "Literal['company', 'individual']|None"
            ]
            """
            Account holder type: individual or company.
            """
            account_number: NotRequired["str|None"]
            """
            Account number of the bank account.
            """
            account_type: NotRequired["Literal['checking', 'savings']|None"]
            """
            Account type: checkings or savings. Defaults to checking if omitted.
            """
            financial_connections_account: NotRequired["str|None"]
            """
            The ID of a Financial Connections Account to use as a payment method.
            """
            routing_number: NotRequired["str|None"]
            """
            Routing number of the bank account.
            """

        class ConfirmParamsPaymentMethodDataSofort(TypedDict):
            country: Literal["AT", "BE", "DE", "ES", "IT", "NL"]
            """
            Two-letter ISO code representing the country the bank account is located in.
            """

        class ConfirmParamsPaymentMethodDataSepaDebit(TypedDict):
            iban: str
            """
            IBAN of the bank account.
            """

        class ConfirmParamsPaymentMethodDataRadarOptions(TypedDict):
            session: NotRequired["str|None"]
            """
            A [Radar Session](https://stripe.com/docs/radar/radar-session) is a snapshot of the browser metadata and device details that help Radar make more accurate predictions on your payments.
            """

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
            """
            The customer's bank.
            """

        class ConfirmParamsPaymentMethodDataOxxo(TypedDict):
            pass

        class ConfirmParamsPaymentMethodDataLink(TypedDict):
            pass

        class ConfirmParamsPaymentMethodDataKonbini(TypedDict):
            pass

        class ConfirmParamsPaymentMethodDataKlarna(TypedDict):
            dob: NotRequired[
                "SetupIntent.ConfirmParamsPaymentMethodDataKlarnaDob|None"
            ]
            """
            Customer's date of birth
            """

        class ConfirmParamsPaymentMethodDataKlarnaDob(TypedDict):
            day: int
            """
            The day of birth, between 1 and 31.
            """
            month: int
            """
            The month of birth, between 1 and 12.
            """
            year: int
            """
            The four-digit year of birth.
            """

        class ConfirmParamsPaymentMethodDataInteracPresent(TypedDict):
            pass

        class ConfirmParamsPaymentMethodDataIdeal(TypedDict):
            bank: NotRequired[
                "Literal['abn_amro', 'asn_bank', 'bunq', 'handelsbanken', 'ing', 'knab', 'moneyou', 'n26', 'rabobank', 'regiobank', 'revolut', 'sns_bank', 'triodos_bank', 'van_lanschot', 'yoursafe']|None"
            ]
            """
            The customer's bank.
            """

        class ConfirmParamsPaymentMethodDataGrabpay(TypedDict):
            pass

        class ConfirmParamsPaymentMethodDataGiropay(TypedDict):
            pass

        class ConfirmParamsPaymentMethodDataFpx(TypedDict):
            account_holder_type: NotRequired[
                "Literal['company', 'individual']|None"
            ]
            """
            Account holder type for FPX transaction
            """
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
            """
            The customer's bank.
            """

        class ConfirmParamsPaymentMethodDataEps(TypedDict):
            bank: NotRequired[
                "Literal['arzte_und_apotheker_bank', 'austrian_anadi_bank_ag', 'bank_austria', 'bankhaus_carl_spangler', 'bankhaus_schelhammer_und_schattera_ag', 'bawag_psk_ag', 'bks_bank_ag', 'brull_kallmus_bank_ag', 'btv_vier_lander_bank', 'capital_bank_grawe_gruppe_ag', 'deutsche_bank_ag', 'dolomitenbank', 'easybank_ag', 'erste_bank_und_sparkassen', 'hypo_alpeadriabank_international_ag', 'hypo_bank_burgenland_aktiengesellschaft', 'hypo_noe_lb_fur_niederosterreich_u_wien', 'hypo_oberosterreich_salzburg_steiermark', 'hypo_tirol_bank_ag', 'hypo_vorarlberg_bank_ag', 'marchfelder_bank', 'oberbank_ag', 'raiffeisen_bankengruppe_osterreich', 'schoellerbank_ag', 'sparda_bank_wien', 'volksbank_gruppe', 'volkskreditbank_ag', 'vr_bank_braunau']|None"
            ]
            """
            The customer's bank.
            """

        class ConfirmParamsPaymentMethodDataCustomerBalance(TypedDict):
            pass

        class ConfirmParamsPaymentMethodDataCashapp(TypedDict):
            pass

        class ConfirmParamsPaymentMethodDataBoleto(TypedDict):
            tax_id: str
            """
            The tax ID of the customer (CPF for individual consumers or CNPJ for businesses consumers)
            """

        class ConfirmParamsPaymentMethodDataBlik(TypedDict):
            pass

        class ConfirmParamsPaymentMethodDataBillingDetails(TypedDict):
            address: NotRequired[
                "Literal['']|SetupIntent.ConfirmParamsPaymentMethodDataBillingDetailsAddress|None"
            ]
            """
            Billing address.
            """
            email: NotRequired["Literal['']|str|None"]
            """
            Email address.
            """
            name: NotRequired["Literal['']|str|None"]
            """
            Full name.
            """
            phone: NotRequired["Literal['']|str|None"]
            """
            Billing phone number (including extension).
            """

        class ConfirmParamsPaymentMethodDataBillingDetailsAddress(TypedDict):
            city: NotRequired["str|None"]
            """
            City, district, suburb, town, or village.
            """
            country: NotRequired["str|None"]
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            line1: NotRequired["str|None"]
            """
            Address line 1 (e.g., street, PO Box, or company name).
            """
            line2: NotRequired["str|None"]
            """
            Address line 2 (e.g., apartment, suite, unit, or building).
            """
            postal_code: NotRequired["str|None"]
            """
            ZIP or postal code.
            """
            state: NotRequired["str|None"]
            """
            State, county, province, or region.
            """

        class ConfirmParamsPaymentMethodDataBancontact(TypedDict):
            pass

        class ConfirmParamsPaymentMethodDataBacsDebit(TypedDict):
            account_number: NotRequired["str|None"]
            """
            Account number of the bank account that the funds will be debited from.
            """
            sort_code: NotRequired["str|None"]
            """
            Sort code of the bank account. (e.g., `10-20-30`)
            """

        class ConfirmParamsPaymentMethodDataAuBecsDebit(TypedDict):
            account_number: str
            """
            The account number for the bank account.
            """
            bsb_number: str
            """
            Bank-State-Branch number of the bank account.
            """

        class ConfirmParamsPaymentMethodDataAlipay(TypedDict):
            pass

        class ConfirmParamsPaymentMethodDataAfterpayClearpay(TypedDict):
            pass

        class ConfirmParamsPaymentMethodDataAffirm(TypedDict):
            pass

        class ConfirmParamsPaymentMethodDataAcssDebit(TypedDict):
            account_number: str
            """
            Customer's bank account number.
            """
            institution_number: str
            """
            Institution number of the customer's bank.
            """
            transit_number: str
            """
            Transit number of the customer's bank.
            """

        class ConfirmParamsMandateData2(TypedDict):
            customer_acceptance: "SetupIntent.ConfirmParamsMandateDataCustomerAcceptance2"
            """
            This hash contains details about the customer acceptance of the Mandate.
            """

        class ConfirmParamsMandateDataCustomerAcceptance2(TypedDict):
            online: "SetupIntent.ConfirmParamsMandateDataCustomerAcceptanceOnline2"
            """
            If this is a Mandate accepted online, this hash contains details about the online acceptance.
            """
            type: Literal["online"]
            """
            The type of customer acceptance information included with the Mandate.
            """

        class ConfirmParamsMandateDataCustomerAcceptanceOnline2(TypedDict):
            ip_address: NotRequired["str|None"]
            """
            The IP address from which the Mandate was accepted by the customer.
            """
            user_agent: NotRequired["str|None"]
            """
            The user agent of the browser from which the Mandate was accepted by the customer.
            """

        class ConfirmParamsMandateData(TypedDict):
            customer_acceptance: "SetupIntent.ConfirmParamsMandateDataCustomerAcceptance"
            """
            This hash contains details about the customer acceptance of the Mandate.
            """

        class ConfirmParamsMandateDataCustomerAcceptance(TypedDict):
            accepted_at: NotRequired["int|None"]
            """
            The time at which the customer accepted the Mandate.
            """
            offline: NotRequired[
                "SetupIntent.ConfirmParamsMandateDataCustomerAcceptanceOffline|None"
            ]
            """
            If this is a Mandate accepted offline, this hash contains details about the offline acceptance.
            """
            online: NotRequired[
                "SetupIntent.ConfirmParamsMandateDataCustomerAcceptanceOnline|None"
            ]
            """
            If this is a Mandate accepted online, this hash contains details about the online acceptance.
            """
            type: Literal["offline", "online"]
            """
            The type of customer acceptance information included with the Mandate. One of `online` or `offline`.
            """

        class ConfirmParamsMandateDataCustomerAcceptanceOnline(TypedDict):
            ip_address: str
            """
            The IP address from which the Mandate was accepted by the customer.
            """
            user_agent: str
            """
            The user agent of the browser from which the Mandate was accepted by the customer.
            """

        class ConfirmParamsMandateDataCustomerAcceptanceOffline(TypedDict):
            pass

        class CreateParams(RequestOptions):
            attach_to_self: NotRequired["bool|None"]
            """
            If present, the SetupIntent's payment method will be attached to the in-context Stripe Account.

            It can only be used for this Stripe Account's own money movement flows like InboundTransfer and OutboundTransfers. It cannot be set to true when setting up a PaymentMethod for a Customer, and defaults to false when attaching a PaymentMethod to a Customer.
            """
            automatic_payment_methods: NotRequired[
                "SetupIntent.CreateParamsAutomaticPaymentMethods|None"
            ]
            """
            When you enable this parameter, this SetupIntent accepts payment methods that you enable in the Dashboard and that are compatible with its other parameters.
            """
            confirm: NotRequired["bool|None"]
            """
            Set to `true` to attempt to confirm this SetupIntent immediately. This parameter defaults to `false`. If a card is the attached payment method, you can provide a `return_url` in case further authentication is necessary.
            """
            customer: NotRequired["str|None"]
            """
            ID of the Customer this SetupIntent belongs to, if one exists.

            If present, the SetupIntent's payment method will be attached to the Customer on successful setup. Payment methods attached to other Customers cannot be used with this SetupIntent.
            """
            description: NotRequired["str|None"]
            """
            An arbitrary string attached to the object. Often useful for displaying to users.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            flow_directions: NotRequired[
                "List[Literal['inbound', 'outbound']]|None"
            ]
            """
            Indicates the directions of money movement for which this payment method is intended to be used.

            Include `inbound` if you intend to use the payment method as the origin to pull funds from. Include `outbound` if you intend to use the payment method as the destination to send funds to. You can include both if you intend to use the payment method for both purposes.
            """
            mandate_data: NotRequired[
                "Literal['']|SetupIntent.CreateParamsMandateData|None"
            ]
            """
            This hash contains details about the mandate to create. This parameter can only be used with [`confirm=true`](https://stripe.com/docs/api/setup_intents/create#create_setup_intent-confirm).
            """
            metadata: NotRequired["Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """
            on_behalf_of: NotRequired["str|None"]
            """
            The Stripe account ID created for this SetupIntent.
            """
            payment_method: NotRequired["str|None"]
            """
            ID of the payment method (a PaymentMethod, Card, or saved Source object) to attach to this SetupIntent.
            """
            payment_method_configuration: NotRequired["str|None"]
            """
            The ID of the payment method configuration to use with this SetupIntent.
            """
            payment_method_data: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodData|None"
            ]
            """
            When included, this hash creates a PaymentMethod that is set as the [`payment_method`](https://stripe.com/docs/api/setup_intents/object#setup_intent_object-payment_method)
            value in the SetupIntent.
            """
            payment_method_options: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodOptions|None"
            ]
            """
            Payment method-specific configuration for this SetupIntent.
            """
            payment_method_types: NotRequired["List[str]|None"]
            """
            The list of payment method types (for example, card) that this SetupIntent can use. If you don't provide this, it defaults to ["card"].
            """
            return_url: NotRequired["str|None"]
            """
            The URL to redirect your customer back to after they authenticate or cancel their payment on the payment method's app or site. To redirect to a mobile application, you can alternatively supply an application URI scheme. This parameter can only be used with [`confirm=true`](https://stripe.com/docs/api/setup_intents/create#create_setup_intent-confirm).
            """
            single_use: NotRequired["SetupIntent.CreateParamsSingleUse|None"]
            """
            If you populate this hash, this SetupIntent generates a `single_use` mandate after successful completion.
            """
            usage: NotRequired["Literal['off_session', 'on_session']|None"]
            """
            Indicates how the payment method is intended to be used in the future. If not provided, this value defaults to `off_session`.
            """
            use_stripe_sdk: NotRequired["bool|None"]
            """
            Set to `true` when confirming server-side and using Stripe.js, iOS, or Android client-side SDKs to handle the next actions.
            """

        class CreateParamsSingleUse(TypedDict):
            amount: int
            """
            Amount the customer is granting permission to collect later. A positive integer representing how much to charge in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal) (e.g., 100 cents to charge $1.00 or 100 to charge ¥100, a zero-decimal currency). The minimum amount is $0.50 US or [equivalent in charge currency](https://stripe.com/docs/currencies#minimum-and-maximum-charge-amounts). The amount value supports up to eight digits (e.g., a value of 99999999 for a USD charge of $999,999.99).
            """
            currency: str
            """
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """

        class CreateParamsPaymentMethodOptions(TypedDict):
            acss_debit: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodOptionsAcssDebit|None"
            ]
            """
            If this is a `acss_debit` SetupIntent, this sub-hash contains details about the ACSS Debit payment method options.
            """
            card: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodOptionsCard|None"
            ]
            """
            Configuration for any card setup attempted on this SetupIntent.
            """
            link: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodOptionsLink|None"
            ]
            """
            If this is a `link` PaymentMethod, this sub-hash contains details about the Link payment method options.
            """
            paypal: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodOptionsPaypal|None"
            ]
            """
            If this is a `paypal` PaymentMethod, this sub-hash contains details about the PayPal payment method options.
            """
            sepa_debit: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodOptionsSepaDebit|None"
            ]
            """
            If this is a `sepa_debit` SetupIntent, this sub-hash contains details about the SEPA Debit payment method options.
            """
            us_bank_account: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodOptionsUsBankAccount|None"
            ]
            """
            If this is a `us_bank_account` SetupIntent, this sub-hash contains details about the US bank account payment method options.
            """

        class CreateParamsPaymentMethodOptionsUsBankAccount(TypedDict):
            financial_connections: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodOptionsUsBankAccountFinancialConnections|None"
            ]
            """
            Additional fields for Financial Connections Session creation
            """
            networks: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodOptionsUsBankAccountNetworks|None"
            ]
            """
            Additional fields for network related functions
            """
            verification_method: NotRequired[
                "Literal['automatic', 'instant', 'microdeposits']|None"
            ]
            """
            Verification method for the intent
            """

        class CreateParamsPaymentMethodOptionsUsBankAccountNetworks(TypedDict):
            requested: NotRequired[
                "List[Literal['ach', 'us_domestic_wire']]|None"
            ]
            """
            Triggers validations to run across the selected networks
            """

        class CreateParamsPaymentMethodOptionsUsBankAccountFinancialConnections(
            TypedDict,
        ):
            permissions: NotRequired[
                "List[Literal['balances', 'ownership', 'payment_method', 'transactions']]|None"
            ]
            """
            The list of permissions to request. If this parameter is passed, the `payment_method` permission must be included. Valid permissions include: `balances`, `ownership`, `payment_method`, and `transactions`.
            """
            prefetch: NotRequired["List[Literal['balances']]|None"]
            """
            List of data features that you would like to retrieve upon account creation.
            """
            return_url: NotRequired["str|None"]
            """
            For webview integrations only. Upon completing OAuth login in the native browser, the user will be redirected to this URL to return to your app.
            """

        class CreateParamsPaymentMethodOptionsSepaDebit(TypedDict):
            mandate_options: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodOptionsSepaDebitMandateOptions|None"
            ]
            """
            Additional fields for Mandate creation
            """

        class CreateParamsPaymentMethodOptionsSepaDebitMandateOptions(
            TypedDict,
        ):
            pass

        class CreateParamsPaymentMethodOptionsPaypal(TypedDict):
            billing_agreement_id: NotRequired["str|None"]
            """
            The PayPal Billing Agreement ID (BAID). This is an ID generated by PayPal which represents the mandate between the merchant and the customer.
            """

        class CreateParamsPaymentMethodOptionsLink(TypedDict):
            persistent_token: NotRequired["str|None"]
            """
            [Deprecated] This is a legacy parameter that no longer has any function.
            """

        class CreateParamsPaymentMethodOptionsCard(TypedDict):
            mandate_options: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodOptionsCardMandateOptions|None"
            ]
            """
            Configuration options for setting up an eMandate for cards issued in India.
            """
            moto: NotRequired["bool|None"]
            """
            When specified, this parameter signals that a card has been collected
            as MOTO (Mail Order Telephone Order) and thus out of scope for SCA. This
            parameter can only be provided during confirmation.
            """
            network: NotRequired[
                "Literal['amex', 'cartes_bancaires', 'diners', 'discover', 'eftpos_au', 'interac', 'jcb', 'mastercard', 'unionpay', 'unknown', 'visa']|None"
            ]
            """
            Selected network to process this SetupIntent on. Depends on the available networks of the card attached to the SetupIntent. Can be only set confirm-time.
            """
            request_three_d_secure: NotRequired[
                "Literal['any', 'automatic']|None"
            ]
            """
            We strongly recommend that you rely on our SCA Engine to automatically prompt your customers for authentication based on risk level and [other requirements](https://stripe.com/docs/strong-customer-authentication). However, if you wish to request 3D Secure based on logic from your own fraud engine, provide this option. Permitted values include: `automatic` or `any`. If not provided, defaults to `automatic`. Read our guide on [manually requesting 3D Secure](https://stripe.com/docs/payments/3d-secure#manual-three-ds) for more information on how this configuration interacts with Radar and our SCA Engine.
            """

        class CreateParamsPaymentMethodOptionsCardMandateOptions(TypedDict):
            amount: int
            """
            Amount to be charged for future payments.
            """
            amount_type: Literal["fixed", "maximum"]
            """
            One of `fixed` or `maximum`. If `fixed`, the `amount` param refers to the exact amount to be charged in future payments. If `maximum`, the amount charged can be up to the value passed for the `amount` param.
            """
            currency: str
            """
            Currency in which future payments will be charged. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """
            description: NotRequired["str|None"]
            """
            A description of the mandate or subscription that is meant to be displayed to the customer.
            """
            end_date: NotRequired["int|None"]
            """
            End date of the mandate or subscription. If not provided, the mandate will be active until canceled. If provided, end date should be after start date.
            """
            interval: Literal["day", "month", "sporadic", "week", "year"]
            """
            Specifies payment frequency. One of `day`, `week`, `month`, `year`, or `sporadic`.
            """
            interval_count: NotRequired["int|None"]
            """
            The number of intervals between payments. For example, `interval=month` and `interval_count=3` indicates one payment every three months. Maximum of one year interval allowed (1 year, 12 months, or 52 weeks). This parameter is optional when `interval=sporadic`.
            """
            reference: str
            """
            Unique identifier for the mandate or subscription.
            """
            start_date: int
            """
            Start date of the mandate or subscription. Start date should not be lesser than yesterday.
            """
            supported_types: NotRequired["List[Literal['india']]|None"]
            """
            Specifies the type of mandates supported. Possible values are `india`.
            """

        class CreateParamsPaymentMethodOptionsAcssDebit(TypedDict):
            currency: NotRequired["Literal['cad', 'usd']|None"]
            """
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """
            mandate_options: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodOptionsAcssDebitMandateOptions|None"
            ]
            """
            Additional fields for Mandate creation
            """
            verification_method: NotRequired[
                "Literal['automatic', 'instant', 'microdeposits']|None"
            ]
            """
            Verification method for the intent
            """

        class CreateParamsPaymentMethodOptionsAcssDebitMandateOptions(
            TypedDict,
        ):
            custom_mandate_url: NotRequired["Literal['']|str|None"]
            """
            A URL for custom mandate text to render during confirmation step.
            The URL will be rendered with additional GET parameters `payment_intent` and `payment_intent_client_secret` when confirming a Payment Intent,
            or `setup_intent` and `setup_intent_client_secret` when confirming a Setup Intent.
            """
            default_for: NotRequired[
                "List[Literal['invoice', 'subscription']]|None"
            ]
            """
            List of Stripe products where this mandate can be selected automatically.
            """
            interval_description: NotRequired["str|None"]
            """
            Description of the mandate interval. Only required if 'payment_schedule' parameter is 'interval' or 'combined'.
            """
            payment_schedule: NotRequired[
                "Literal['combined', 'interval', 'sporadic']|None"
            ]
            """
            Payment schedule for the mandate.
            """
            transaction_type: NotRequired[
                "Literal['business', 'personal']|None"
            ]
            """
            Transaction type of the mandate.
            """

        class CreateParamsPaymentMethodData(TypedDict):
            acss_debit: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataAcssDebit|None"
            ]
            """
            If this is an `acss_debit` PaymentMethod, this hash contains details about the ACSS Debit payment method.
            """
            affirm: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataAffirm|None"
            ]
            """
            If this is an `affirm` PaymentMethod, this hash contains details about the Affirm payment method.
            """
            afterpay_clearpay: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataAfterpayClearpay|None"
            ]
            """
            If this is an `AfterpayClearpay` PaymentMethod, this hash contains details about the AfterpayClearpay payment method.
            """
            alipay: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataAlipay|None"
            ]
            """
            If this is an `Alipay` PaymentMethod, this hash contains details about the Alipay payment method.
            """
            au_becs_debit: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataAuBecsDebit|None"
            ]
            """
            If this is an `au_becs_debit` PaymentMethod, this hash contains details about the bank account.
            """
            bacs_debit: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataBacsDebit|None"
            ]
            """
            If this is a `bacs_debit` PaymentMethod, this hash contains details about the Bacs Direct Debit bank account.
            """
            bancontact: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataBancontact|None"
            ]
            """
            If this is a `bancontact` PaymentMethod, this hash contains details about the Bancontact payment method.
            """
            billing_details: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataBillingDetails|None"
            ]
            """
            Billing information associated with the PaymentMethod that may be used or required by particular types of payment methods.
            """
            blik: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataBlik|None"
            ]
            """
            If this is a `blik` PaymentMethod, this hash contains details about the BLIK payment method.
            """
            boleto: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataBoleto|None"
            ]
            """
            If this is a `boleto` PaymentMethod, this hash contains details about the Boleto payment method.
            """
            cashapp: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataCashapp|None"
            ]
            """
            If this is a `cashapp` PaymentMethod, this hash contains details about the Cash App Pay payment method.
            """
            customer_balance: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataCustomerBalance|None"
            ]
            """
            If this is a `customer_balance` PaymentMethod, this hash contains details about the CustomerBalance payment method.
            """
            eps: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataEps|None"
            ]
            """
            If this is an `eps` PaymentMethod, this hash contains details about the EPS payment method.
            """
            fpx: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataFpx|None"
            ]
            """
            If this is an `fpx` PaymentMethod, this hash contains details about the FPX payment method.
            """
            giropay: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataGiropay|None"
            ]
            """
            If this is a `giropay` PaymentMethod, this hash contains details about the Giropay payment method.
            """
            grabpay: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataGrabpay|None"
            ]
            """
            If this is a `grabpay` PaymentMethod, this hash contains details about the GrabPay payment method.
            """
            ideal: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataIdeal|None"
            ]
            """
            If this is an `ideal` PaymentMethod, this hash contains details about the iDEAL payment method.
            """
            interac_present: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataInteracPresent|None"
            ]
            """
            If this is an `interac_present` PaymentMethod, this hash contains details about the Interac Present payment method.
            """
            klarna: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataKlarna|None"
            ]
            """
            If this is a `klarna` PaymentMethod, this hash contains details about the Klarna payment method.
            """
            konbini: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataKonbini|None"
            ]
            """
            If this is a `konbini` PaymentMethod, this hash contains details about the Konbini payment method.
            """
            link: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataLink|None"
            ]
            """
            If this is an `Link` PaymentMethod, this hash contains details about the Link payment method.
            """
            metadata: NotRequired["Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """
            oxxo: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataOxxo|None"
            ]
            """
            If this is an `oxxo` PaymentMethod, this hash contains details about the OXXO payment method.
            """
            p24: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataP24|None"
            ]
            """
            If this is a `p24` PaymentMethod, this hash contains details about the P24 payment method.
            """
            paynow: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataPaynow|None"
            ]
            """
            If this is a `paynow` PaymentMethod, this hash contains details about the PayNow payment method.
            """
            paypal: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataPaypal|None"
            ]
            """
            If this is a `paypal` PaymentMethod, this hash contains details about the PayPal payment method.
            """
            pix: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataPix|None"
            ]
            """
            If this is a `pix` PaymentMethod, this hash contains details about the Pix payment method.
            """
            promptpay: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataPromptpay|None"
            ]
            """
            If this is a `promptpay` PaymentMethod, this hash contains details about the PromptPay payment method.
            """
            radar_options: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataRadarOptions|None"
            ]
            """
            Options to configure Radar. See [Radar Session](https://stripe.com/docs/radar/radar-session) for more information.
            """
            sepa_debit: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataSepaDebit|None"
            ]
            """
            If this is a `sepa_debit` PaymentMethod, this hash contains details about the SEPA debit bank account.
            """
            sofort: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataSofort|None"
            ]
            """
            If this is a `sofort` PaymentMethod, this hash contains details about the SOFORT payment method.
            """
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
            """
            The type of the PaymentMethod. An additional hash is included on the PaymentMethod with a name matching this value. It contains additional information specific to the PaymentMethod type.
            """
            us_bank_account: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataUsBankAccount|None"
            ]
            """
            If this is an `us_bank_account` PaymentMethod, this hash contains details about the US bank account payment method.
            """
            wechat_pay: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataWechatPay|None"
            ]
            """
            If this is an `wechat_pay` PaymentMethod, this hash contains details about the wechat_pay payment method.
            """
            zip: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataZip|None"
            ]
            """
            If this is a `zip` PaymentMethod, this hash contains details about the Zip payment method.
            """

        class CreateParamsPaymentMethodDataZip(TypedDict):
            pass

        class CreateParamsPaymentMethodDataWechatPay(TypedDict):
            pass

        class CreateParamsPaymentMethodDataUsBankAccount(TypedDict):
            account_holder_type: NotRequired[
                "Literal['company', 'individual']|None"
            ]
            """
            Account holder type: individual or company.
            """
            account_number: NotRequired["str|None"]
            """
            Account number of the bank account.
            """
            account_type: NotRequired["Literal['checking', 'savings']|None"]
            """
            Account type: checkings or savings. Defaults to checking if omitted.
            """
            financial_connections_account: NotRequired["str|None"]
            """
            The ID of a Financial Connections Account to use as a payment method.
            """
            routing_number: NotRequired["str|None"]
            """
            Routing number of the bank account.
            """

        class CreateParamsPaymentMethodDataSofort(TypedDict):
            country: Literal["AT", "BE", "DE", "ES", "IT", "NL"]
            """
            Two-letter ISO code representing the country the bank account is located in.
            """

        class CreateParamsPaymentMethodDataSepaDebit(TypedDict):
            iban: str
            """
            IBAN of the bank account.
            """

        class CreateParamsPaymentMethodDataRadarOptions(TypedDict):
            session: NotRequired["str|None"]
            """
            A [Radar Session](https://stripe.com/docs/radar/radar-session) is a snapshot of the browser metadata and device details that help Radar make more accurate predictions on your payments.
            """

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
            """
            The customer's bank.
            """

        class CreateParamsPaymentMethodDataOxxo(TypedDict):
            pass

        class CreateParamsPaymentMethodDataLink(TypedDict):
            pass

        class CreateParamsPaymentMethodDataKonbini(TypedDict):
            pass

        class CreateParamsPaymentMethodDataKlarna(TypedDict):
            dob: NotRequired[
                "SetupIntent.CreateParamsPaymentMethodDataKlarnaDob|None"
            ]
            """
            Customer's date of birth
            """

        class CreateParamsPaymentMethodDataKlarnaDob(TypedDict):
            day: int
            """
            The day of birth, between 1 and 31.
            """
            month: int
            """
            The month of birth, between 1 and 12.
            """
            year: int
            """
            The four-digit year of birth.
            """

        class CreateParamsPaymentMethodDataInteracPresent(TypedDict):
            pass

        class CreateParamsPaymentMethodDataIdeal(TypedDict):
            bank: NotRequired[
                "Literal['abn_amro', 'asn_bank', 'bunq', 'handelsbanken', 'ing', 'knab', 'moneyou', 'n26', 'rabobank', 'regiobank', 'revolut', 'sns_bank', 'triodos_bank', 'van_lanschot', 'yoursafe']|None"
            ]
            """
            The customer's bank.
            """

        class CreateParamsPaymentMethodDataGrabpay(TypedDict):
            pass

        class CreateParamsPaymentMethodDataGiropay(TypedDict):
            pass

        class CreateParamsPaymentMethodDataFpx(TypedDict):
            account_holder_type: NotRequired[
                "Literal['company', 'individual']|None"
            ]
            """
            Account holder type for FPX transaction
            """
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
            """
            The customer's bank.
            """

        class CreateParamsPaymentMethodDataEps(TypedDict):
            bank: NotRequired[
                "Literal['arzte_und_apotheker_bank', 'austrian_anadi_bank_ag', 'bank_austria', 'bankhaus_carl_spangler', 'bankhaus_schelhammer_und_schattera_ag', 'bawag_psk_ag', 'bks_bank_ag', 'brull_kallmus_bank_ag', 'btv_vier_lander_bank', 'capital_bank_grawe_gruppe_ag', 'deutsche_bank_ag', 'dolomitenbank', 'easybank_ag', 'erste_bank_und_sparkassen', 'hypo_alpeadriabank_international_ag', 'hypo_bank_burgenland_aktiengesellschaft', 'hypo_noe_lb_fur_niederosterreich_u_wien', 'hypo_oberosterreich_salzburg_steiermark', 'hypo_tirol_bank_ag', 'hypo_vorarlberg_bank_ag', 'marchfelder_bank', 'oberbank_ag', 'raiffeisen_bankengruppe_osterreich', 'schoellerbank_ag', 'sparda_bank_wien', 'volksbank_gruppe', 'volkskreditbank_ag', 'vr_bank_braunau']|None"
            ]
            """
            The customer's bank.
            """

        class CreateParamsPaymentMethodDataCustomerBalance(TypedDict):
            pass

        class CreateParamsPaymentMethodDataCashapp(TypedDict):
            pass

        class CreateParamsPaymentMethodDataBoleto(TypedDict):
            tax_id: str
            """
            The tax ID of the customer (CPF for individual consumers or CNPJ for businesses consumers)
            """

        class CreateParamsPaymentMethodDataBlik(TypedDict):
            pass

        class CreateParamsPaymentMethodDataBillingDetails(TypedDict):
            address: NotRequired[
                "Literal['']|SetupIntent.CreateParamsPaymentMethodDataBillingDetailsAddress|None"
            ]
            """
            Billing address.
            """
            email: NotRequired["Literal['']|str|None"]
            """
            Email address.
            """
            name: NotRequired["Literal['']|str|None"]
            """
            Full name.
            """
            phone: NotRequired["Literal['']|str|None"]
            """
            Billing phone number (including extension).
            """

        class CreateParamsPaymentMethodDataBillingDetailsAddress(TypedDict):
            city: NotRequired["str|None"]
            """
            City, district, suburb, town, or village.
            """
            country: NotRequired["str|None"]
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            line1: NotRequired["str|None"]
            """
            Address line 1 (e.g., street, PO Box, or company name).
            """
            line2: NotRequired["str|None"]
            """
            Address line 2 (e.g., apartment, suite, unit, or building).
            """
            postal_code: NotRequired["str|None"]
            """
            ZIP or postal code.
            """
            state: NotRequired["str|None"]
            """
            State, county, province, or region.
            """

        class CreateParamsPaymentMethodDataBancontact(TypedDict):
            pass

        class CreateParamsPaymentMethodDataBacsDebit(TypedDict):
            account_number: NotRequired["str|None"]
            """
            Account number of the bank account that the funds will be debited from.
            """
            sort_code: NotRequired["str|None"]
            """
            Sort code of the bank account. (e.g., `10-20-30`)
            """

        class CreateParamsPaymentMethodDataAuBecsDebit(TypedDict):
            account_number: str
            """
            The account number for the bank account.
            """
            bsb_number: str
            """
            Bank-State-Branch number of the bank account.
            """

        class CreateParamsPaymentMethodDataAlipay(TypedDict):
            pass

        class CreateParamsPaymentMethodDataAfterpayClearpay(TypedDict):
            pass

        class CreateParamsPaymentMethodDataAffirm(TypedDict):
            pass

        class CreateParamsPaymentMethodDataAcssDebit(TypedDict):
            account_number: str
            """
            Customer's bank account number.
            """
            institution_number: str
            """
            Institution number of the customer's bank.
            """
            transit_number: str
            """
            Transit number of the customer's bank.
            """

        class CreateParamsMandateData(TypedDict):
            customer_acceptance: "SetupIntent.CreateParamsMandateDataCustomerAcceptance"
            """
            This hash contains details about the customer acceptance of the Mandate.
            """

        class CreateParamsMandateDataCustomerAcceptance(TypedDict):
            accepted_at: NotRequired["int|None"]
            """
            The time at which the customer accepted the Mandate.
            """
            offline: NotRequired[
                "SetupIntent.CreateParamsMandateDataCustomerAcceptanceOffline|None"
            ]
            """
            If this is a Mandate accepted offline, this hash contains details about the offline acceptance.
            """
            online: NotRequired[
                "SetupIntent.CreateParamsMandateDataCustomerAcceptanceOnline|None"
            ]
            """
            If this is a Mandate accepted online, this hash contains details about the online acceptance.
            """
            type: Literal["offline", "online"]
            """
            The type of customer acceptance information included with the Mandate. One of `online` or `offline`.
            """

        class CreateParamsMandateDataCustomerAcceptanceOnline(TypedDict):
            ip_address: str
            """
            The IP address from which the Mandate was accepted by the customer.
            """
            user_agent: str
            """
            The user agent of the browser from which the Mandate was accepted by the customer.
            """

        class CreateParamsMandateDataCustomerAcceptanceOffline(TypedDict):
            pass

        class CreateParamsAutomaticPaymentMethods(TypedDict):
            allow_redirects: NotRequired["Literal['always', 'never']|None"]
            """
            Controls whether this SetupIntent will accept redirect-based payment methods.

            Redirect-based payment methods may require your customer to be redirected to a payment method's app or site for authentication or additional steps. To [confirm](https://stripe.com/docs/api/setup_intents/confirm) this SetupIntent, you may be required to provide a `return_url` to redirect customers back to your site after they authenticate or complete the setup.
            """
            enabled: bool
            """
            Whether this feature is enabled.
            """

        class ListParams(RequestOptions):
            attach_to_self: NotRequired["bool|None"]
            """
            If present, the SetupIntent's payment method will be attached to the in-context Stripe Account.

            It can only be used for this Stripe Account's own money movement flows like InboundTransfer and OutboundTransfers. It cannot be set to true when setting up a PaymentMethod for a Customer, and defaults to false when attaching a PaymentMethod to a Customer.
            """
            created: NotRequired["SetupIntent.ListParamsCreated|int|None"]
            """
            A filter on the list, based on the object `created` field. The value can be a string with an integer Unix timestamp, or it can be a dictionary with a number of different query options.
            """
            customer: NotRequired["str|None"]
            """
            Only return SetupIntents for the customer specified by this customer ID.
            """
            ending_before: NotRequired["str|None"]
            """
            A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            limit: NotRequired["int|None"]
            """
            A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
            """
            payment_method: NotRequired["str|None"]
            """
            Only return SetupIntents that associate with the specified payment method.
            """
            starting_after: NotRequired["str|None"]
            """
            A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
            """

        class ListParamsCreated(TypedDict):
            gt: NotRequired["int|None"]
            """
            Minimum value to filter by (exclusive)
            """
            gte: NotRequired["int|None"]
            """
            Minimum value to filter by (inclusive)
            """
            lt: NotRequired["int|None"]
            """
            Maximum value to filter by (exclusive)
            """
            lte: NotRequired["int|None"]
            """
            Maximum value to filter by (inclusive)
            """

        class ModifyParams(RequestOptions):
            attach_to_self: NotRequired["bool|None"]
            """
            If present, the SetupIntent's payment method will be attached to the in-context Stripe Account.

            It can only be used for this Stripe Account's own money movement flows like InboundTransfer and OutboundTransfers. It cannot be set to true when setting up a PaymentMethod for a Customer, and defaults to false when attaching a PaymentMethod to a Customer.
            """
            customer: NotRequired["str|None"]
            """
            ID of the Customer this SetupIntent belongs to, if one exists.

            If present, the SetupIntent's payment method will be attached to the Customer on successful setup. Payment methods attached to other Customers cannot be used with this SetupIntent.
            """
            description: NotRequired["str|None"]
            """
            An arbitrary string attached to the object. Often useful for displaying to users.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            flow_directions: NotRequired[
                "List[Literal['inbound', 'outbound']]|None"
            ]
            """
            Indicates the directions of money movement for which this payment method is intended to be used.

            Include `inbound` if you intend to use the payment method as the origin to pull funds from. Include `outbound` if you intend to use the payment method as the destination to send funds to. You can include both if you intend to use the payment method for both purposes.
            """
            metadata: NotRequired["Literal['']|Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """
            payment_method: NotRequired["str|None"]
            """
            ID of the payment method (a PaymentMethod, Card, or saved Source object) to attach to this SetupIntent.
            """
            payment_method_configuration: NotRequired["str|None"]
            """
            The ID of the payment method configuration to use with this SetupIntent.
            """
            payment_method_data: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodData|None"
            ]
            """
            When included, this hash creates a PaymentMethod that is set as the [`payment_method`](https://stripe.com/docs/api/setup_intents/object#setup_intent_object-payment_method)
            value in the SetupIntent.
            """
            payment_method_options: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodOptions|None"
            ]
            """
            Payment method-specific configuration for this SetupIntent.
            """
            payment_method_types: NotRequired["List[str]|None"]
            """
            The list of payment method types (for example, card) that this SetupIntent can set up. If you don't provide this array, it defaults to ["card"].
            """

        class ModifyParamsPaymentMethodOptions(TypedDict):
            acss_debit: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodOptionsAcssDebit|None"
            ]
            """
            If this is a `acss_debit` SetupIntent, this sub-hash contains details about the ACSS Debit payment method options.
            """
            card: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodOptionsCard|None"
            ]
            """
            Configuration for any card setup attempted on this SetupIntent.
            """
            link: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodOptionsLink|None"
            ]
            """
            If this is a `link` PaymentMethod, this sub-hash contains details about the Link payment method options.
            """
            paypal: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodOptionsPaypal|None"
            ]
            """
            If this is a `paypal` PaymentMethod, this sub-hash contains details about the PayPal payment method options.
            """
            sepa_debit: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodOptionsSepaDebit|None"
            ]
            """
            If this is a `sepa_debit` SetupIntent, this sub-hash contains details about the SEPA Debit payment method options.
            """
            us_bank_account: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodOptionsUsBankAccount|None"
            ]
            """
            If this is a `us_bank_account` SetupIntent, this sub-hash contains details about the US bank account payment method options.
            """

        class ModifyParamsPaymentMethodOptionsUsBankAccount(TypedDict):
            financial_connections: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodOptionsUsBankAccountFinancialConnections|None"
            ]
            """
            Additional fields for Financial Connections Session creation
            """
            networks: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodOptionsUsBankAccountNetworks|None"
            ]
            """
            Additional fields for network related functions
            """
            verification_method: NotRequired[
                "Literal['automatic', 'instant', 'microdeposits']|None"
            ]
            """
            Verification method for the intent
            """

        class ModifyParamsPaymentMethodOptionsUsBankAccountNetworks(TypedDict):
            requested: NotRequired[
                "List[Literal['ach', 'us_domestic_wire']]|None"
            ]
            """
            Triggers validations to run across the selected networks
            """

        class ModifyParamsPaymentMethodOptionsUsBankAccountFinancialConnections(
            TypedDict,
        ):
            permissions: NotRequired[
                "List[Literal['balances', 'ownership', 'payment_method', 'transactions']]|None"
            ]
            """
            The list of permissions to request. If this parameter is passed, the `payment_method` permission must be included. Valid permissions include: `balances`, `ownership`, `payment_method`, and `transactions`.
            """
            prefetch: NotRequired["List[Literal['balances']]|None"]
            """
            List of data features that you would like to retrieve upon account creation.
            """
            return_url: NotRequired["str|None"]
            """
            For webview integrations only. Upon completing OAuth login in the native browser, the user will be redirected to this URL to return to your app.
            """

        class ModifyParamsPaymentMethodOptionsSepaDebit(TypedDict):
            mandate_options: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodOptionsSepaDebitMandateOptions|None"
            ]
            """
            Additional fields for Mandate creation
            """

        class ModifyParamsPaymentMethodOptionsSepaDebitMandateOptions(
            TypedDict,
        ):
            pass

        class ModifyParamsPaymentMethodOptionsPaypal(TypedDict):
            billing_agreement_id: NotRequired["str|None"]
            """
            The PayPal Billing Agreement ID (BAID). This is an ID generated by PayPal which represents the mandate between the merchant and the customer.
            """

        class ModifyParamsPaymentMethodOptionsLink(TypedDict):
            persistent_token: NotRequired["str|None"]
            """
            [Deprecated] This is a legacy parameter that no longer has any function.
            """

        class ModifyParamsPaymentMethodOptionsCard(TypedDict):
            mandate_options: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodOptionsCardMandateOptions|None"
            ]
            """
            Configuration options for setting up an eMandate for cards issued in India.
            """
            moto: NotRequired["bool|None"]
            """
            When specified, this parameter signals that a card has been collected
            as MOTO (Mail Order Telephone Order) and thus out of scope for SCA. This
            parameter can only be provided during confirmation.
            """
            network: NotRequired[
                "Literal['amex', 'cartes_bancaires', 'diners', 'discover', 'eftpos_au', 'interac', 'jcb', 'mastercard', 'unionpay', 'unknown', 'visa']|None"
            ]
            """
            Selected network to process this SetupIntent on. Depends on the available networks of the card attached to the SetupIntent. Can be only set confirm-time.
            """
            request_three_d_secure: NotRequired[
                "Literal['any', 'automatic']|None"
            ]
            """
            We strongly recommend that you rely on our SCA Engine to automatically prompt your customers for authentication based on risk level and [other requirements](https://stripe.com/docs/strong-customer-authentication). However, if you wish to request 3D Secure based on logic from your own fraud engine, provide this option. Permitted values include: `automatic` or `any`. If not provided, defaults to `automatic`. Read our guide on [manually requesting 3D Secure](https://stripe.com/docs/payments/3d-secure#manual-three-ds) for more information on how this configuration interacts with Radar and our SCA Engine.
            """

        class ModifyParamsPaymentMethodOptionsCardMandateOptions(TypedDict):
            amount: int
            """
            Amount to be charged for future payments.
            """
            amount_type: Literal["fixed", "maximum"]
            """
            One of `fixed` or `maximum`. If `fixed`, the `amount` param refers to the exact amount to be charged in future payments. If `maximum`, the amount charged can be up to the value passed for the `amount` param.
            """
            currency: str
            """
            Currency in which future payments will be charged. Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """
            description: NotRequired["str|None"]
            """
            A description of the mandate or subscription that is meant to be displayed to the customer.
            """
            end_date: NotRequired["int|None"]
            """
            End date of the mandate or subscription. If not provided, the mandate will be active until canceled. If provided, end date should be after start date.
            """
            interval: Literal["day", "month", "sporadic", "week", "year"]
            """
            Specifies payment frequency. One of `day`, `week`, `month`, `year`, or `sporadic`.
            """
            interval_count: NotRequired["int|None"]
            """
            The number of intervals between payments. For example, `interval=month` and `interval_count=3` indicates one payment every three months. Maximum of one year interval allowed (1 year, 12 months, or 52 weeks). This parameter is optional when `interval=sporadic`.
            """
            reference: str
            """
            Unique identifier for the mandate or subscription.
            """
            start_date: int
            """
            Start date of the mandate or subscription. Start date should not be lesser than yesterday.
            """
            supported_types: NotRequired["List[Literal['india']]|None"]
            """
            Specifies the type of mandates supported. Possible values are `india`.
            """

        class ModifyParamsPaymentMethodOptionsAcssDebit(TypedDict):
            currency: NotRequired["Literal['cad', 'usd']|None"]
            """
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """
            mandate_options: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodOptionsAcssDebitMandateOptions|None"
            ]
            """
            Additional fields for Mandate creation
            """
            verification_method: NotRequired[
                "Literal['automatic', 'instant', 'microdeposits']|None"
            ]
            """
            Verification method for the intent
            """

        class ModifyParamsPaymentMethodOptionsAcssDebitMandateOptions(
            TypedDict,
        ):
            custom_mandate_url: NotRequired["Literal['']|str|None"]
            """
            A URL for custom mandate text to render during confirmation step.
            The URL will be rendered with additional GET parameters `payment_intent` and `payment_intent_client_secret` when confirming a Payment Intent,
            or `setup_intent` and `setup_intent_client_secret` when confirming a Setup Intent.
            """
            default_for: NotRequired[
                "List[Literal['invoice', 'subscription']]|None"
            ]
            """
            List of Stripe products where this mandate can be selected automatically.
            """
            interval_description: NotRequired["str|None"]
            """
            Description of the mandate interval. Only required if 'payment_schedule' parameter is 'interval' or 'combined'.
            """
            payment_schedule: NotRequired[
                "Literal['combined', 'interval', 'sporadic']|None"
            ]
            """
            Payment schedule for the mandate.
            """
            transaction_type: NotRequired[
                "Literal['business', 'personal']|None"
            ]
            """
            Transaction type of the mandate.
            """

        class ModifyParamsPaymentMethodData(TypedDict):
            acss_debit: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataAcssDebit|None"
            ]
            """
            If this is an `acss_debit` PaymentMethod, this hash contains details about the ACSS Debit payment method.
            """
            affirm: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataAffirm|None"
            ]
            """
            If this is an `affirm` PaymentMethod, this hash contains details about the Affirm payment method.
            """
            afterpay_clearpay: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataAfterpayClearpay|None"
            ]
            """
            If this is an `AfterpayClearpay` PaymentMethod, this hash contains details about the AfterpayClearpay payment method.
            """
            alipay: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataAlipay|None"
            ]
            """
            If this is an `Alipay` PaymentMethod, this hash contains details about the Alipay payment method.
            """
            au_becs_debit: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataAuBecsDebit|None"
            ]
            """
            If this is an `au_becs_debit` PaymentMethod, this hash contains details about the bank account.
            """
            bacs_debit: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataBacsDebit|None"
            ]
            """
            If this is a `bacs_debit` PaymentMethod, this hash contains details about the Bacs Direct Debit bank account.
            """
            bancontact: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataBancontact|None"
            ]
            """
            If this is a `bancontact` PaymentMethod, this hash contains details about the Bancontact payment method.
            """
            billing_details: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataBillingDetails|None"
            ]
            """
            Billing information associated with the PaymentMethod that may be used or required by particular types of payment methods.
            """
            blik: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataBlik|None"
            ]
            """
            If this is a `blik` PaymentMethod, this hash contains details about the BLIK payment method.
            """
            boleto: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataBoleto|None"
            ]
            """
            If this is a `boleto` PaymentMethod, this hash contains details about the Boleto payment method.
            """
            cashapp: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataCashapp|None"
            ]
            """
            If this is a `cashapp` PaymentMethod, this hash contains details about the Cash App Pay payment method.
            """
            customer_balance: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataCustomerBalance|None"
            ]
            """
            If this is a `customer_balance` PaymentMethod, this hash contains details about the CustomerBalance payment method.
            """
            eps: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataEps|None"
            ]
            """
            If this is an `eps` PaymentMethod, this hash contains details about the EPS payment method.
            """
            fpx: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataFpx|None"
            ]
            """
            If this is an `fpx` PaymentMethod, this hash contains details about the FPX payment method.
            """
            giropay: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataGiropay|None"
            ]
            """
            If this is a `giropay` PaymentMethod, this hash contains details about the Giropay payment method.
            """
            grabpay: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataGrabpay|None"
            ]
            """
            If this is a `grabpay` PaymentMethod, this hash contains details about the GrabPay payment method.
            """
            ideal: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataIdeal|None"
            ]
            """
            If this is an `ideal` PaymentMethod, this hash contains details about the iDEAL payment method.
            """
            interac_present: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataInteracPresent|None"
            ]
            """
            If this is an `interac_present` PaymentMethod, this hash contains details about the Interac Present payment method.
            """
            klarna: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataKlarna|None"
            ]
            """
            If this is a `klarna` PaymentMethod, this hash contains details about the Klarna payment method.
            """
            konbini: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataKonbini|None"
            ]
            """
            If this is a `konbini` PaymentMethod, this hash contains details about the Konbini payment method.
            """
            link: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataLink|None"
            ]
            """
            If this is an `Link` PaymentMethod, this hash contains details about the Link payment method.
            """
            metadata: NotRequired["Dict[str, str]|None"]
            """
            Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
            """
            oxxo: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataOxxo|None"
            ]
            """
            If this is an `oxxo` PaymentMethod, this hash contains details about the OXXO payment method.
            """
            p24: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataP24|None"
            ]
            """
            If this is a `p24` PaymentMethod, this hash contains details about the P24 payment method.
            """
            paynow: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataPaynow|None"
            ]
            """
            If this is a `paynow` PaymentMethod, this hash contains details about the PayNow payment method.
            """
            paypal: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataPaypal|None"
            ]
            """
            If this is a `paypal` PaymentMethod, this hash contains details about the PayPal payment method.
            """
            pix: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataPix|None"
            ]
            """
            If this is a `pix` PaymentMethod, this hash contains details about the Pix payment method.
            """
            promptpay: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataPromptpay|None"
            ]
            """
            If this is a `promptpay` PaymentMethod, this hash contains details about the PromptPay payment method.
            """
            radar_options: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataRadarOptions|None"
            ]
            """
            Options to configure Radar. See [Radar Session](https://stripe.com/docs/radar/radar-session) for more information.
            """
            sepa_debit: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataSepaDebit|None"
            ]
            """
            If this is a `sepa_debit` PaymentMethod, this hash contains details about the SEPA debit bank account.
            """
            sofort: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataSofort|None"
            ]
            """
            If this is a `sofort` PaymentMethod, this hash contains details about the SOFORT payment method.
            """
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
            """
            The type of the PaymentMethod. An additional hash is included on the PaymentMethod with a name matching this value. It contains additional information specific to the PaymentMethod type.
            """
            us_bank_account: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataUsBankAccount|None"
            ]
            """
            If this is an `us_bank_account` PaymentMethod, this hash contains details about the US bank account payment method.
            """
            wechat_pay: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataWechatPay|None"
            ]
            """
            If this is an `wechat_pay` PaymentMethod, this hash contains details about the wechat_pay payment method.
            """
            zip: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataZip|None"
            ]
            """
            If this is a `zip` PaymentMethod, this hash contains details about the Zip payment method.
            """

        class ModifyParamsPaymentMethodDataZip(TypedDict):
            pass

        class ModifyParamsPaymentMethodDataWechatPay(TypedDict):
            pass

        class ModifyParamsPaymentMethodDataUsBankAccount(TypedDict):
            account_holder_type: NotRequired[
                "Literal['company', 'individual']|None"
            ]
            """
            Account holder type: individual or company.
            """
            account_number: NotRequired["str|None"]
            """
            Account number of the bank account.
            """
            account_type: NotRequired["Literal['checking', 'savings']|None"]
            """
            Account type: checkings or savings. Defaults to checking if omitted.
            """
            financial_connections_account: NotRequired["str|None"]
            """
            The ID of a Financial Connections Account to use as a payment method.
            """
            routing_number: NotRequired["str|None"]
            """
            Routing number of the bank account.
            """

        class ModifyParamsPaymentMethodDataSofort(TypedDict):
            country: Literal["AT", "BE", "DE", "ES", "IT", "NL"]
            """
            Two-letter ISO code representing the country the bank account is located in.
            """

        class ModifyParamsPaymentMethodDataSepaDebit(TypedDict):
            iban: str
            """
            IBAN of the bank account.
            """

        class ModifyParamsPaymentMethodDataRadarOptions(TypedDict):
            session: NotRequired["str|None"]
            """
            A [Radar Session](https://stripe.com/docs/radar/radar-session) is a snapshot of the browser metadata and device details that help Radar make more accurate predictions on your payments.
            """

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
            """
            The customer's bank.
            """

        class ModifyParamsPaymentMethodDataOxxo(TypedDict):
            pass

        class ModifyParamsPaymentMethodDataLink(TypedDict):
            pass

        class ModifyParamsPaymentMethodDataKonbini(TypedDict):
            pass

        class ModifyParamsPaymentMethodDataKlarna(TypedDict):
            dob: NotRequired[
                "SetupIntent.ModifyParamsPaymentMethodDataKlarnaDob|None"
            ]
            """
            Customer's date of birth
            """

        class ModifyParamsPaymentMethodDataKlarnaDob(TypedDict):
            day: int
            """
            The day of birth, between 1 and 31.
            """
            month: int
            """
            The month of birth, between 1 and 12.
            """
            year: int
            """
            The four-digit year of birth.
            """

        class ModifyParamsPaymentMethodDataInteracPresent(TypedDict):
            pass

        class ModifyParamsPaymentMethodDataIdeal(TypedDict):
            bank: NotRequired[
                "Literal['abn_amro', 'asn_bank', 'bunq', 'handelsbanken', 'ing', 'knab', 'moneyou', 'n26', 'rabobank', 'regiobank', 'revolut', 'sns_bank', 'triodos_bank', 'van_lanschot', 'yoursafe']|None"
            ]
            """
            The customer's bank.
            """

        class ModifyParamsPaymentMethodDataGrabpay(TypedDict):
            pass

        class ModifyParamsPaymentMethodDataGiropay(TypedDict):
            pass

        class ModifyParamsPaymentMethodDataFpx(TypedDict):
            account_holder_type: NotRequired[
                "Literal['company', 'individual']|None"
            ]
            """
            Account holder type for FPX transaction
            """
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
            """
            The customer's bank.
            """

        class ModifyParamsPaymentMethodDataEps(TypedDict):
            bank: NotRequired[
                "Literal['arzte_und_apotheker_bank', 'austrian_anadi_bank_ag', 'bank_austria', 'bankhaus_carl_spangler', 'bankhaus_schelhammer_und_schattera_ag', 'bawag_psk_ag', 'bks_bank_ag', 'brull_kallmus_bank_ag', 'btv_vier_lander_bank', 'capital_bank_grawe_gruppe_ag', 'deutsche_bank_ag', 'dolomitenbank', 'easybank_ag', 'erste_bank_und_sparkassen', 'hypo_alpeadriabank_international_ag', 'hypo_bank_burgenland_aktiengesellschaft', 'hypo_noe_lb_fur_niederosterreich_u_wien', 'hypo_oberosterreich_salzburg_steiermark', 'hypo_tirol_bank_ag', 'hypo_vorarlberg_bank_ag', 'marchfelder_bank', 'oberbank_ag', 'raiffeisen_bankengruppe_osterreich', 'schoellerbank_ag', 'sparda_bank_wien', 'volksbank_gruppe', 'volkskreditbank_ag', 'vr_bank_braunau']|None"
            ]
            """
            The customer's bank.
            """

        class ModifyParamsPaymentMethodDataCustomerBalance(TypedDict):
            pass

        class ModifyParamsPaymentMethodDataCashapp(TypedDict):
            pass

        class ModifyParamsPaymentMethodDataBoleto(TypedDict):
            tax_id: str
            """
            The tax ID of the customer (CPF for individual consumers or CNPJ for businesses consumers)
            """

        class ModifyParamsPaymentMethodDataBlik(TypedDict):
            pass

        class ModifyParamsPaymentMethodDataBillingDetails(TypedDict):
            address: NotRequired[
                "Literal['']|SetupIntent.ModifyParamsPaymentMethodDataBillingDetailsAddress|None"
            ]
            """
            Billing address.
            """
            email: NotRequired["Literal['']|str|None"]
            """
            Email address.
            """
            name: NotRequired["Literal['']|str|None"]
            """
            Full name.
            """
            phone: NotRequired["Literal['']|str|None"]
            """
            Billing phone number (including extension).
            """

        class ModifyParamsPaymentMethodDataBillingDetailsAddress(TypedDict):
            city: NotRequired["str|None"]
            """
            City, district, suburb, town, or village.
            """
            country: NotRequired["str|None"]
            """
            Two-letter country code ([ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2)).
            """
            line1: NotRequired["str|None"]
            """
            Address line 1 (e.g., street, PO Box, or company name).
            """
            line2: NotRequired["str|None"]
            """
            Address line 2 (e.g., apartment, suite, unit, or building).
            """
            postal_code: NotRequired["str|None"]
            """
            ZIP or postal code.
            """
            state: NotRequired["str|None"]
            """
            State, county, province, or region.
            """

        class ModifyParamsPaymentMethodDataBancontact(TypedDict):
            pass

        class ModifyParamsPaymentMethodDataBacsDebit(TypedDict):
            account_number: NotRequired["str|None"]
            """
            Account number of the bank account that the funds will be debited from.
            """
            sort_code: NotRequired["str|None"]
            """
            Sort code of the bank account. (e.g., `10-20-30`)
            """

        class ModifyParamsPaymentMethodDataAuBecsDebit(TypedDict):
            account_number: str
            """
            The account number for the bank account.
            """
            bsb_number: str
            """
            Bank-State-Branch number of the bank account.
            """

        class ModifyParamsPaymentMethodDataAlipay(TypedDict):
            pass

        class ModifyParamsPaymentMethodDataAfterpayClearpay(TypedDict):
            pass

        class ModifyParamsPaymentMethodDataAffirm(TypedDict):
            pass

        class ModifyParamsPaymentMethodDataAcssDebit(TypedDict):
            account_number: str
            """
            Customer's bank account number.
            """
            institution_number: str
            """
            Institution number of the customer's bank.
            """
            transit_number: str
            """
            Transit number of the customer's bank.
            """

        class RetrieveParams(RequestOptions):
            client_secret: NotRequired["str|None"]
            """
            The client secret of the SetupIntent. We require this string if you use a publishable key to retrieve the SetupIntent.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

        class VerifyMicrodepositsParams(RequestOptions):
            amounts: NotRequired["List[int]|None"]
            """
            Two positive integers, in *cents*, equal to the values of the microdeposits sent to the bank account.
            """
            descriptor_code: NotRequired["str|None"]
            """
            A six-character code starting with SM present in the microdeposit sent to the bank account.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

    application: Optional[ExpandableField["Application"]]
    """
    ID of the Connect application that created the SetupIntent.
    """
    attach_to_self: Optional[bool]
    """
    If present, the SetupIntent's payment method will be attached to the in-context Stripe Account.

    It can only be used for this Stripe Account's own money movement flows like InboundTransfer and OutboundTransfers. It cannot be set to true when setting up a PaymentMethod for a Customer, and defaults to false when attaching a PaymentMethod to a Customer.
    """
    automatic_payment_methods: Optional[StripeObject]
    """
    Settings for dynamic payment methods compatible with this Setup Intent
    """
    cancellation_reason: Optional[
        Literal["abandoned", "duplicate", "requested_by_customer"]
    ]
    """
    Reason for cancellation of this SetupIntent, one of `abandoned`, `requested_by_customer`, or `duplicate`.
    """
    client_secret: Optional[str]
    """
    The client secret of this SetupIntent. Used for client-side retrieval using a publishable key.

    The client secret can be used to complete payment setup from your frontend. It should not be stored, logged, or exposed to anyone other than the customer. Make sure that you have TLS enabled on any page that includes the client secret.
    """
    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    customer: Optional[ExpandableField["Customer"]]
    """
    ID of the Customer this SetupIntent belongs to, if one exists.

    If present, the SetupIntent's payment method will be attached to the Customer on successful setup. Payment methods attached to other Customers cannot be used with this SetupIntent.
    """
    description: Optional[str]
    """
    An arbitrary string attached to the object. Often useful for displaying to users.
    """
    flow_directions: Optional[List[Literal["inbound", "outbound"]]]
    """
    Indicates the directions of money movement for which this payment method is intended to be used.

    Include `inbound` if you intend to use the payment method as the origin to pull funds from. Include `outbound` if you intend to use the payment method as the destination to send funds to. You can include both if you intend to use the payment method for both purposes.
    """
    id: str
    """
    Unique identifier for the object.
    """
    last_setup_error: Optional[StripeObject]
    """
    The error encountered in the previous SetupIntent confirmation.
    """
    latest_attempt: Optional[ExpandableField["SetupAttempt"]]
    """
    The most recent SetupAttempt for this SetupIntent.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    mandate: Optional[ExpandableField["Mandate"]]
    """
    ID of the multi use Mandate generated by the SetupIntent.
    """
    metadata: Optional[Dict[str, str]]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    next_action: Optional[StripeObject]
    """
    If present, this property tells you what actions you need to take in order for your customer to continue payment setup.
    """
    object: Literal["setup_intent"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    on_behalf_of: Optional[ExpandableField["Account"]]
    """
    The account (if any) for which the setup is intended.
    """
    payment_method: Optional[ExpandableField["PaymentMethod"]]
    """
    ID of the payment method used with this SetupIntent.
    """
    payment_method_configuration_details: Optional[StripeObject]
    """
    Information about the payment method configuration used for this Setup Intent.
    """
    payment_method_options: Optional[StripeObject]
    """
    Payment method-specific configuration for this SetupIntent.
    """
    payment_method_types: List[str]
    """
    The list of payment method types (e.g. card) that this SetupIntent is allowed to set up.
    """
    single_use_mandate: Optional[ExpandableField["Mandate"]]
    """
    ID of the single_use Mandate generated by the SetupIntent.
    """
    status: Literal[
        "canceled",
        "processing",
        "requires_action",
        "requires_confirmation",
        "requires_payment_method",
        "succeeded",
    ]
    """
    [Status](https://stripe.com/docs/payments/intents#intent-statuses) of this SetupIntent, one of `requires_payment_method`, `requires_confirmation`, `requires_action`, `processing`, `canceled`, or `succeeded`.
    """
    usage: str
    """
    Indicates how the payment method is intended to be used in the future.

    Use `on_session` if you intend to only reuse the payment method when the customer is in your checkout flow. Use `off_session` if your customer may or may not be in your checkout flow. If not provided, this value defaults to `off_session`.
    """

    @classmethod
    def _cls_cancel(
        cls,
        intent: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["SetupIntent.CancelParams"]
    ) -> "SetupIntent":
        return cast(
            "SetupIntent",
            cls._static_request(
                "post",
                "/v1/setup_intents/{intent}/cancel".format(
                    intent=util.sanitize_id(intent)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @overload
    @classmethod
    def cancel(
        cls,
        intent: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["SetupIntent.CancelParams"]
    ) -> "SetupIntent":
        ...

    @overload
    def cancel(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["SetupIntent.CancelParams"]
    ) -> "SetupIntent":
        ...

    @class_method_variant("_cls_cancel")
    def cancel(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["SetupIntent.CancelParams"]
    ) -> "SetupIntent":
        return cast(
            "SetupIntent",
            self._request(
                "post",
                "/v1/setup_intents/{intent}/cancel".format(
                    intent=util.sanitize_id(self.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
        )

    @classmethod
    def _cls_confirm(
        cls,
        intent: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["SetupIntent.ConfirmParams"]
    ) -> "SetupIntent":
        return cast(
            "SetupIntent",
            cls._static_request(
                "post",
                "/v1/setup_intents/{intent}/confirm".format(
                    intent=util.sanitize_id(intent)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @overload
    @classmethod
    def confirm(
        cls,
        intent: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["SetupIntent.ConfirmParams"]
    ) -> "SetupIntent":
        ...

    @overload
    def confirm(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["SetupIntent.ConfirmParams"]
    ) -> "SetupIntent":
        ...

    @class_method_variant("_cls_confirm")
    def confirm(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["SetupIntent.ConfirmParams"]
    ) -> "SetupIntent":
        return cast(
            "SetupIntent",
            self._request(
                "post",
                "/v1/setup_intents/{intent}/confirm".format(
                    intent=util.sanitize_id(self.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
        )

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["SetupIntent.CreateParams"]
    ) -> "SetupIntent":
        return cast(
            "SetupIntent",
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
        **params: Unpack["SetupIntent.ListParams"]
    ) -> ListObject["SetupIntent"]:
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
        cls, id: str, **params: Unpack["SetupIntent.ModifyParams"]
    ) -> "SetupIntent":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "SetupIntent",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["SetupIntent.RetrieveParams"]
    ) -> "SetupIntent":
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
        **params: Unpack["SetupIntent.VerifyMicrodepositsParams"]
    ) -> "SetupIntent":
        return cast(
            "SetupIntent",
            cls._static_request(
                "post",
                "/v1/setup_intents/{intent}/verify_microdeposits".format(
                    intent=util.sanitize_id(intent)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            ),
        )

    @overload
    @classmethod
    def verify_microdeposits(
        cls,
        intent: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["SetupIntent.VerifyMicrodepositsParams"]
    ) -> "SetupIntent":
        ...

    @overload
    def verify_microdeposits(
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["SetupIntent.VerifyMicrodepositsParams"]
    ) -> "SetupIntent":
        ...

    @class_method_variant("_cls_verify_microdeposits")
    def verify_microdeposits(  # pyright: ignore[reportGeneralTypeIssues]
        self,
        idempotency_key: Optional[str] = None,
        **params: Unpack["SetupIntent.VerifyMicrodepositsParams"]
    ) -> "SetupIntent":
        return cast(
            "SetupIntent",
            self._request(
                "post",
                "/v1/setup_intents/{intent}/verify_microdeposits".format(
                    intent=util.sanitize_id(self.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            ),
        )
