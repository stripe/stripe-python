# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import List, Optional, cast
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)
from urllib.parse import quote_plus


class PaymentMethodConfiguration(
    CreateableAPIResource["PaymentMethodConfiguration"],
    ListableAPIResource["PaymentMethodConfiguration"],
    UpdateableAPIResource["PaymentMethodConfiguration"],
):
    """
    PaymentMethodConfigurations control which payment methods are displayed to your customers when you don't explicitly specify payment method types. You can have multiple configurations with different sets of payment methods for different scenarios.

    There are two types of PaymentMethodConfigurations. Which is used depends on the [charge type](https://stripe.com/docs/connect/charges):

    **Direct** configurations apply to payments created on your account, including Connect destination charges, Connect separate charges and transfers, and payments not involving Connect.

    **Child** configurations apply to payments created on your connected accounts using direct charges, and charges with the on_behalf_of parameter.

    Child configurations have a `parent` that sets default values and controls which settings connected accounts may override. You can specify a parent ID at payment time, and Stripe will automatically resolve the connected account's associated child configuration. Parent configurations are [managed in the dashboard](https://dashboard.stripe.com/settings/payment_methods/connected_accounts) and are not available in this API.

    Related guides:
    - [Payment Method Configurations API](https://stripe.com/docs/connect/payment-method-configurations)
    - [Multiple configurations on dynamic payment methods](https://stripe.com/docs/payments/multiple-payment-method-configs)
    - [Multiple configurations for your Connect accounts](https://stripe.com/docs/connect/multiple-payment-method-configurations)
    """

    OBJECT_NAME = "payment_method_configuration"
    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            acss_debit: NotRequired[
                "PaymentMethodConfiguration.CreateParamsAcssDebit|None"
            ]
            affirm: NotRequired[
                "PaymentMethodConfiguration.CreateParamsAffirm|None"
            ]
            afterpay_clearpay: NotRequired[
                "PaymentMethodConfiguration.CreateParamsAfterpayClearpay|None"
            ]
            alipay: NotRequired[
                "PaymentMethodConfiguration.CreateParamsAlipay|None"
            ]
            apple_pay: NotRequired[
                "PaymentMethodConfiguration.CreateParamsApplePay|None"
            ]
            apple_pay_later: NotRequired[
                "PaymentMethodConfiguration.CreateParamsApplePayLater|None"
            ]
            au_becs_debit: NotRequired[
                "PaymentMethodConfiguration.CreateParamsAuBecsDebit|None"
            ]
            bacs_debit: NotRequired[
                "PaymentMethodConfiguration.CreateParamsBacsDebit|None"
            ]
            bancontact: NotRequired[
                "PaymentMethodConfiguration.CreateParamsBancontact|None"
            ]
            blik: NotRequired[
                "PaymentMethodConfiguration.CreateParamsBlik|None"
            ]
            boleto: NotRequired[
                "PaymentMethodConfiguration.CreateParamsBoleto|None"
            ]
            card: NotRequired[
                "PaymentMethodConfiguration.CreateParamsCard|None"
            ]
            cartes_bancaires: NotRequired[
                "PaymentMethodConfiguration.CreateParamsCartesBancaires|None"
            ]
            cashapp: NotRequired[
                "PaymentMethodConfiguration.CreateParamsCashapp|None"
            ]
            eps: NotRequired["PaymentMethodConfiguration.CreateParamsEps|None"]
            expand: NotRequired["List[str]|None"]
            fpx: NotRequired["PaymentMethodConfiguration.CreateParamsFpx|None"]
            giropay: NotRequired[
                "PaymentMethodConfiguration.CreateParamsGiropay|None"
            ]
            google_pay: NotRequired[
                "PaymentMethodConfiguration.CreateParamsGooglePay|None"
            ]
            grabpay: NotRequired[
                "PaymentMethodConfiguration.CreateParamsGrabpay|None"
            ]
            ideal: NotRequired[
                "PaymentMethodConfiguration.CreateParamsIdeal|None"
            ]
            jcb: NotRequired["PaymentMethodConfiguration.CreateParamsJcb|None"]
            klarna: NotRequired[
                "PaymentMethodConfiguration.CreateParamsKlarna|None"
            ]
            konbini: NotRequired[
                "PaymentMethodConfiguration.CreateParamsKonbini|None"
            ]
            link: NotRequired[
                "PaymentMethodConfiguration.CreateParamsLink|None"
            ]
            name: NotRequired["str|None"]
            oxxo: NotRequired[
                "PaymentMethodConfiguration.CreateParamsOxxo|None"
            ]
            p24: NotRequired["PaymentMethodConfiguration.CreateParamsP24|None"]
            parent: NotRequired["str|None"]
            paynow: NotRequired[
                "PaymentMethodConfiguration.CreateParamsPaynow|None"
            ]
            paypal: NotRequired[
                "PaymentMethodConfiguration.CreateParamsPaypal|None"
            ]
            promptpay: NotRequired[
                "PaymentMethodConfiguration.CreateParamsPromptpay|None"
            ]
            sepa_debit: NotRequired[
                "PaymentMethodConfiguration.CreateParamsSepaDebit|None"
            ]
            sofort: NotRequired[
                "PaymentMethodConfiguration.CreateParamsSofort|None"
            ]
            us_bank_account: NotRequired[
                "PaymentMethodConfiguration.CreateParamsUsBankAccount|None"
            ]
            wechat_pay: NotRequired[
                "PaymentMethodConfiguration.CreateParamsWechatPay|None"
            ]

        class CreateParamsWechatPay(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsWechatPayDisplayPreference|None"
            ]

        class CreateParamsWechatPayDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class CreateParamsUsBankAccount(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsUsBankAccountDisplayPreference|None"
            ]

        class CreateParamsUsBankAccountDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class CreateParamsSofort(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsSofortDisplayPreference|None"
            ]

        class CreateParamsSofortDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class CreateParamsSepaDebit(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsSepaDebitDisplayPreference|None"
            ]

        class CreateParamsSepaDebitDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class CreateParamsPromptpay(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsPromptpayDisplayPreference|None"
            ]

        class CreateParamsPromptpayDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class CreateParamsPaypal(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsPaypalDisplayPreference|None"
            ]

        class CreateParamsPaypalDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class CreateParamsPaynow(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsPaynowDisplayPreference|None"
            ]

        class CreateParamsPaynowDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class CreateParamsP24(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsP24DisplayPreference|None"
            ]

        class CreateParamsP24DisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class CreateParamsOxxo(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsOxxoDisplayPreference|None"
            ]

        class CreateParamsOxxoDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class CreateParamsLink(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsLinkDisplayPreference|None"
            ]

        class CreateParamsLinkDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class CreateParamsKonbini(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsKonbiniDisplayPreference|None"
            ]

        class CreateParamsKonbiniDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class CreateParamsKlarna(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsKlarnaDisplayPreference|None"
            ]

        class CreateParamsKlarnaDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class CreateParamsJcb(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsJcbDisplayPreference|None"
            ]

        class CreateParamsJcbDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class CreateParamsIdeal(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsIdealDisplayPreference|None"
            ]

        class CreateParamsIdealDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class CreateParamsGrabpay(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsGrabpayDisplayPreference|None"
            ]

        class CreateParamsGrabpayDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class CreateParamsGooglePay(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsGooglePayDisplayPreference|None"
            ]

        class CreateParamsGooglePayDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class CreateParamsGiropay(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsGiropayDisplayPreference|None"
            ]

        class CreateParamsGiropayDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class CreateParamsFpx(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsFpxDisplayPreference|None"
            ]

        class CreateParamsFpxDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class CreateParamsEps(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsEpsDisplayPreference|None"
            ]

        class CreateParamsEpsDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class CreateParamsCashapp(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsCashappDisplayPreference|None"
            ]

        class CreateParamsCashappDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class CreateParamsCartesBancaires(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsCartesBancairesDisplayPreference|None"
            ]

        class CreateParamsCartesBancairesDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class CreateParamsCard(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsCardDisplayPreference|None"
            ]

        class CreateParamsCardDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class CreateParamsBoleto(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsBoletoDisplayPreference|None"
            ]

        class CreateParamsBoletoDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class CreateParamsBlik(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsBlikDisplayPreference|None"
            ]

        class CreateParamsBlikDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class CreateParamsBancontact(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsBancontactDisplayPreference|None"
            ]

        class CreateParamsBancontactDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class CreateParamsBacsDebit(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsBacsDebitDisplayPreference|None"
            ]

        class CreateParamsBacsDebitDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class CreateParamsAuBecsDebit(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsAuBecsDebitDisplayPreference|None"
            ]

        class CreateParamsAuBecsDebitDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class CreateParamsApplePayLater(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsApplePayLaterDisplayPreference|None"
            ]

        class CreateParamsApplePayLaterDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class CreateParamsApplePay(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsApplePayDisplayPreference|None"
            ]

        class CreateParamsApplePayDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class CreateParamsAlipay(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsAlipayDisplayPreference|None"
            ]

        class CreateParamsAlipayDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class CreateParamsAfterpayClearpay(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsAfterpayClearpayDisplayPreference|None"
            ]

        class CreateParamsAfterpayClearpayDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class CreateParamsAffirm(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsAffirmDisplayPreference|None"
            ]

        class CreateParamsAffirmDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class CreateParamsAcssDebit(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsAcssDebitDisplayPreference|None"
            ]

        class CreateParamsAcssDebitDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class ListParams(RequestOptions):
            application: NotRequired["Literal['']|str|None"]
            expand: NotRequired["List[str]|None"]

        class ModifyParams(RequestOptions):
            acss_debit: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsAcssDebit|None"
            ]
            active: NotRequired["bool|None"]
            affirm: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsAffirm|None"
            ]
            afterpay_clearpay: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsAfterpayClearpay|None"
            ]
            alipay: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsAlipay|None"
            ]
            apple_pay: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsApplePay|None"
            ]
            apple_pay_later: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsApplePayLater|None"
            ]
            au_becs_debit: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsAuBecsDebit|None"
            ]
            bacs_debit: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsBacsDebit|None"
            ]
            bancontact: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsBancontact|None"
            ]
            blik: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsBlik|None"
            ]
            boleto: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsBoleto|None"
            ]
            card: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsCard|None"
            ]
            cartes_bancaires: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsCartesBancaires|None"
            ]
            cashapp: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsCashapp|None"
            ]
            eps: NotRequired["PaymentMethodConfiguration.ModifyParamsEps|None"]
            expand: NotRequired["List[str]|None"]
            fpx: NotRequired["PaymentMethodConfiguration.ModifyParamsFpx|None"]
            giropay: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsGiropay|None"
            ]
            google_pay: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsGooglePay|None"
            ]
            grabpay: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsGrabpay|None"
            ]
            ideal: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsIdeal|None"
            ]
            jcb: NotRequired["PaymentMethodConfiguration.ModifyParamsJcb|None"]
            klarna: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsKlarna|None"
            ]
            konbini: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsKonbini|None"
            ]
            link: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsLink|None"
            ]
            name: NotRequired["str|None"]
            oxxo: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsOxxo|None"
            ]
            p24: NotRequired["PaymentMethodConfiguration.ModifyParamsP24|None"]
            paynow: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsPaynow|None"
            ]
            paypal: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsPaypal|None"
            ]
            promptpay: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsPromptpay|None"
            ]
            sepa_debit: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsSepaDebit|None"
            ]
            sofort: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsSofort|None"
            ]
            us_bank_account: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsUsBankAccount|None"
            ]
            wechat_pay: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsWechatPay|None"
            ]

        class ModifyParamsWechatPay(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsWechatPayDisplayPreference|None"
            ]

        class ModifyParamsWechatPayDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class ModifyParamsUsBankAccount(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsUsBankAccountDisplayPreference|None"
            ]

        class ModifyParamsUsBankAccountDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class ModifyParamsSofort(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsSofortDisplayPreference|None"
            ]

        class ModifyParamsSofortDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class ModifyParamsSepaDebit(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsSepaDebitDisplayPreference|None"
            ]

        class ModifyParamsSepaDebitDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class ModifyParamsPromptpay(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsPromptpayDisplayPreference|None"
            ]

        class ModifyParamsPromptpayDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class ModifyParamsPaypal(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsPaypalDisplayPreference|None"
            ]

        class ModifyParamsPaypalDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class ModifyParamsPaynow(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsPaynowDisplayPreference|None"
            ]

        class ModifyParamsPaynowDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class ModifyParamsP24(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsP24DisplayPreference|None"
            ]

        class ModifyParamsP24DisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class ModifyParamsOxxo(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsOxxoDisplayPreference|None"
            ]

        class ModifyParamsOxxoDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class ModifyParamsLink(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsLinkDisplayPreference|None"
            ]

        class ModifyParamsLinkDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class ModifyParamsKonbini(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsKonbiniDisplayPreference|None"
            ]

        class ModifyParamsKonbiniDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class ModifyParamsKlarna(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsKlarnaDisplayPreference|None"
            ]

        class ModifyParamsKlarnaDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class ModifyParamsJcb(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsJcbDisplayPreference|None"
            ]

        class ModifyParamsJcbDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class ModifyParamsIdeal(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsIdealDisplayPreference|None"
            ]

        class ModifyParamsIdealDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class ModifyParamsGrabpay(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsGrabpayDisplayPreference|None"
            ]

        class ModifyParamsGrabpayDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class ModifyParamsGooglePay(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsGooglePayDisplayPreference|None"
            ]

        class ModifyParamsGooglePayDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class ModifyParamsGiropay(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsGiropayDisplayPreference|None"
            ]

        class ModifyParamsGiropayDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class ModifyParamsFpx(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsFpxDisplayPreference|None"
            ]

        class ModifyParamsFpxDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class ModifyParamsEps(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsEpsDisplayPreference|None"
            ]

        class ModifyParamsEpsDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class ModifyParamsCashapp(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsCashappDisplayPreference|None"
            ]

        class ModifyParamsCashappDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class ModifyParamsCartesBancaires(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsCartesBancairesDisplayPreference|None"
            ]

        class ModifyParamsCartesBancairesDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class ModifyParamsCard(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsCardDisplayPreference|None"
            ]

        class ModifyParamsCardDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class ModifyParamsBoleto(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsBoletoDisplayPreference|None"
            ]

        class ModifyParamsBoletoDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class ModifyParamsBlik(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsBlikDisplayPreference|None"
            ]

        class ModifyParamsBlikDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class ModifyParamsBancontact(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsBancontactDisplayPreference|None"
            ]

        class ModifyParamsBancontactDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class ModifyParamsBacsDebit(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsBacsDebitDisplayPreference|None"
            ]

        class ModifyParamsBacsDebitDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class ModifyParamsAuBecsDebit(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsAuBecsDebitDisplayPreference|None"
            ]

        class ModifyParamsAuBecsDebitDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class ModifyParamsApplePayLater(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsApplePayLaterDisplayPreference|None"
            ]

        class ModifyParamsApplePayLaterDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class ModifyParamsApplePay(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsApplePayDisplayPreference|None"
            ]

        class ModifyParamsApplePayDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class ModifyParamsAlipay(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsAlipayDisplayPreference|None"
            ]

        class ModifyParamsAlipayDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class ModifyParamsAfterpayClearpay(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsAfterpayClearpayDisplayPreference|None"
            ]

        class ModifyParamsAfterpayClearpayDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class ModifyParamsAffirm(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsAffirmDisplayPreference|None"
            ]

        class ModifyParamsAffirmDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class ModifyParamsAcssDebit(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsAcssDebitDisplayPreference|None"
            ]

        class ModifyParamsAcssDebitDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]

    acss_debit: Optional[StripeObject]
    active: bool
    affirm: Optional[StripeObject]
    afterpay_clearpay: Optional[StripeObject]
    alipay: Optional[StripeObject]
    apple_pay: Optional[StripeObject]
    application: Optional[str]
    au_becs_debit: Optional[StripeObject]
    bacs_debit: Optional[StripeObject]
    bancontact: Optional[StripeObject]
    blik: Optional[StripeObject]
    boleto: Optional[StripeObject]
    card: Optional[StripeObject]
    cartes_bancaires: Optional[StripeObject]
    cashapp: Optional[StripeObject]
    eps: Optional[StripeObject]
    fpx: Optional[StripeObject]
    giropay: Optional[StripeObject]
    google_pay: Optional[StripeObject]
    grabpay: Optional[StripeObject]
    id: str
    id_bank_transfer: Optional[StripeObject]
    ideal: Optional[StripeObject]
    is_default: bool
    jcb: Optional[StripeObject]
    klarna: Optional[StripeObject]
    konbini: Optional[StripeObject]
    link: Optional[StripeObject]
    livemode: bool
    multibanco: Optional[StripeObject]
    name: str
    netbanking: Optional[StripeObject]
    object: Literal["payment_method_configuration"]
    oxxo: Optional[StripeObject]
    p24: Optional[StripeObject]
    parent: Optional[str]
    pay_by_bank: Optional[StripeObject]
    paynow: Optional[StripeObject]
    paypal: Optional[StripeObject]
    promptpay: Optional[StripeObject]
    sepa_debit: Optional[StripeObject]
    sofort: Optional[StripeObject]
    upi: Optional[StripeObject]
    us_bank_account: Optional[StripeObject]
    wechat_pay: Optional[StripeObject]

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Unpack["PaymentMethodConfiguration.CreateParams"]
    ) -> "PaymentMethodConfiguration":
        return cast(
            "PaymentMethodConfiguration",
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
        **params: Unpack["PaymentMethodConfiguration.ListParams"]
    ) -> ListObject["PaymentMethodConfiguration"]:
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
        cls, id, **params: Unpack["PaymentMethodConfiguration.ModifyParams"]
    ) -> "PaymentMethodConfiguration":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "PaymentMethodConfiguration",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls,
        id: str,
        **params: Unpack["PaymentMethodConfiguration.RetrieveParams"]
    ) -> "PaymentMethodConfiguration":
        instance = cls(id, **params)
        instance.refresh()
        return instance
