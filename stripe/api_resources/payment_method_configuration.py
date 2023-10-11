# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.list_object import ListObject
from stripe.request_options import RequestOptions
from stripe.stripe_object import StripeObject
from typing import List, Optional, Union, cast
from typing_extensions import Literal, NotRequired, TypedDict, Unpack
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
    - [Multiple payment method configurations on dynamic payment methods](https://stripe.com/docs/payments/multiple-payment-method-configs)
    - [Multiple configurations for your Connect accounts](https://stripe.com/docs/connect/multiple-payment-method-configurations)
    """

    OBJECT_NAME = "payment_method_configuration"

    class CreateParams(RequestOptions):
        acss_debit: NotRequired[
            Optional["PaymentMethodConfiguration.CreateParamsAcssDebit"]
        ]
        affirm: NotRequired[
            Optional["PaymentMethodConfiguration.CreateParamsAffirm"]
        ]
        afterpay_clearpay: NotRequired[
            Optional["PaymentMethodConfiguration.CreateParamsAfterpayClearpay"]
        ]
        alipay: NotRequired[
            Optional["PaymentMethodConfiguration.CreateParamsAlipay"]
        ]
        apple_pay: NotRequired[
            Optional["PaymentMethodConfiguration.CreateParamsApplePay"]
        ]
        apple_pay_later: NotRequired[
            Optional["PaymentMethodConfiguration.CreateParamsApplePayLater"]
        ]
        au_becs_debit: NotRequired[
            Optional["PaymentMethodConfiguration.CreateParamsAuBecsDebit"]
        ]
        bacs_debit: NotRequired[
            Optional["PaymentMethodConfiguration.CreateParamsBacsDebit"]
        ]
        bancontact: NotRequired[
            Optional["PaymentMethodConfiguration.CreateParamsBancontact"]
        ]
        blik: NotRequired[
            Optional["PaymentMethodConfiguration.CreateParamsBlik"]
        ]
        boleto: NotRequired[
            Optional["PaymentMethodConfiguration.CreateParamsBoleto"]
        ]
        card: NotRequired[
            Optional["PaymentMethodConfiguration.CreateParamsCard"]
        ]
        cartes_bancaires: NotRequired[
            Optional["PaymentMethodConfiguration.CreateParamsCartesBancaires"]
        ]
        cashapp: NotRequired[
            Optional["PaymentMethodConfiguration.CreateParamsCashapp"]
        ]
        eps: NotRequired[
            Optional["PaymentMethodConfiguration.CreateParamsEps"]
        ]
        expand: NotRequired[Optional[List[str]]]
        fpx: NotRequired[
            Optional["PaymentMethodConfiguration.CreateParamsFpx"]
        ]
        giropay: NotRequired[
            Optional["PaymentMethodConfiguration.CreateParamsGiropay"]
        ]
        google_pay: NotRequired[
            Optional["PaymentMethodConfiguration.CreateParamsGooglePay"]
        ]
        grabpay: NotRequired[
            Optional["PaymentMethodConfiguration.CreateParamsGrabpay"]
        ]
        ideal: NotRequired[
            Optional["PaymentMethodConfiguration.CreateParamsIdeal"]
        ]
        jcb: NotRequired[
            Optional["PaymentMethodConfiguration.CreateParamsJcb"]
        ]
        klarna: NotRequired[
            Optional["PaymentMethodConfiguration.CreateParamsKlarna"]
        ]
        konbini: NotRequired[
            Optional["PaymentMethodConfiguration.CreateParamsKonbini"]
        ]
        link: NotRequired[
            Optional["PaymentMethodConfiguration.CreateParamsLink"]
        ]
        name: NotRequired[Optional[str]]
        oxxo: NotRequired[
            Optional["PaymentMethodConfiguration.CreateParamsOxxo"]
        ]
        p24: NotRequired[
            Optional["PaymentMethodConfiguration.CreateParamsP24"]
        ]
        parent: NotRequired[Optional[str]]
        paynow: NotRequired[
            Optional["PaymentMethodConfiguration.CreateParamsPaynow"]
        ]
        paypal: NotRequired[
            Optional["PaymentMethodConfiguration.CreateParamsPaypal"]
        ]
        promptpay: NotRequired[
            Optional["PaymentMethodConfiguration.CreateParamsPromptpay"]
        ]
        sepa_debit: NotRequired[
            Optional["PaymentMethodConfiguration.CreateParamsSepaDebit"]
        ]
        sofort: NotRequired[
            Optional["PaymentMethodConfiguration.CreateParamsSofort"]
        ]
        us_bank_account: NotRequired[
            Optional["PaymentMethodConfiguration.CreateParamsUsBankAccount"]
        ]
        wechat_pay: NotRequired[
            Optional["PaymentMethodConfiguration.CreateParamsWechatPay"]
        ]

    class CreateParamsWechatPay(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateParamsWechatPayDisplayPreference"
            ]
        ]

    class CreateParamsWechatPayDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateParamsUsBankAccount(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateParamsUsBankAccountDisplayPreference"
            ]
        ]

    class CreateParamsUsBankAccountDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateParamsSofort(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateParamsSofortDisplayPreference"
            ]
        ]

    class CreateParamsSofortDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateParamsSepaDebit(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateParamsSepaDebitDisplayPreference"
            ]
        ]

    class CreateParamsSepaDebitDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateParamsPromptpay(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateParamsPromptpayDisplayPreference"
            ]
        ]

    class CreateParamsPromptpayDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateParamsPaypal(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateParamsPaypalDisplayPreference"
            ]
        ]

    class CreateParamsPaypalDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateParamsPaynow(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateParamsPaynowDisplayPreference"
            ]
        ]

    class CreateParamsPaynowDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateParamsP24(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateParamsP24DisplayPreference"
            ]
        ]

    class CreateParamsP24DisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateParamsOxxo(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateParamsOxxoDisplayPreference"
            ]
        ]

    class CreateParamsOxxoDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateParamsLink(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateParamsLinkDisplayPreference"
            ]
        ]

    class CreateParamsLinkDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateParamsKonbini(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateParamsKonbiniDisplayPreference"
            ]
        ]

    class CreateParamsKonbiniDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateParamsKlarna(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateParamsKlarnaDisplayPreference"
            ]
        ]

    class CreateParamsKlarnaDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateParamsJcb(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateParamsJcbDisplayPreference"
            ]
        ]

    class CreateParamsJcbDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateParamsIdeal(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateParamsIdealDisplayPreference"
            ]
        ]

    class CreateParamsIdealDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateParamsGrabpay(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateParamsGrabpayDisplayPreference"
            ]
        ]

    class CreateParamsGrabpayDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateParamsGooglePay(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateParamsGooglePayDisplayPreference"
            ]
        ]

    class CreateParamsGooglePayDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateParamsGiropay(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateParamsGiropayDisplayPreference"
            ]
        ]

    class CreateParamsGiropayDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateParamsFpx(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateParamsFpxDisplayPreference"
            ]
        ]

    class CreateParamsFpxDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateParamsEps(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateParamsEpsDisplayPreference"
            ]
        ]

    class CreateParamsEpsDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateParamsCashapp(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateParamsCashappDisplayPreference"
            ]
        ]

    class CreateParamsCashappDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateParamsCartesBancaires(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateParamsCartesBancairesDisplayPreference"
            ]
        ]

    class CreateParamsCartesBancairesDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateParamsCard(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateParamsCardDisplayPreference"
            ]
        ]

    class CreateParamsCardDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateParamsBoleto(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateParamsBoletoDisplayPreference"
            ]
        ]

    class CreateParamsBoletoDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateParamsBlik(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateParamsBlikDisplayPreference"
            ]
        ]

    class CreateParamsBlikDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateParamsBancontact(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateParamsBancontactDisplayPreference"
            ]
        ]

    class CreateParamsBancontactDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateParamsBacsDebit(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateParamsBacsDebitDisplayPreference"
            ]
        ]

    class CreateParamsBacsDebitDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateParamsAuBecsDebit(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateParamsAuBecsDebitDisplayPreference"
            ]
        ]

    class CreateParamsAuBecsDebitDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateParamsApplePayLater(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateParamsApplePayLaterDisplayPreference"
            ]
        ]

    class CreateParamsApplePayLaterDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateParamsApplePay(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateParamsApplePayDisplayPreference"
            ]
        ]

    class CreateParamsApplePayDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateParamsAlipay(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateParamsAlipayDisplayPreference"
            ]
        ]

    class CreateParamsAlipayDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateParamsAfterpayClearpay(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateParamsAfterpayClearpayDisplayPreference"
            ]
        ]

    class CreateParamsAfterpayClearpayDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateParamsAffirm(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateParamsAffirmDisplayPreference"
            ]
        ]

    class CreateParamsAffirmDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateParamsAcssDebit(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateParamsAcssDebitDisplayPreference"
            ]
        ]

    class CreateParamsAcssDebitDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ListParams(RequestOptions):
        application: NotRequired[Optional[Union[Literal[""], str]]]
        expand: NotRequired[Optional[List[str]]]

    class ModifyParams(RequestOptions):
        acss_debit: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyParamsAcssDebit"]
        ]
        active: NotRequired[Optional[bool]]
        affirm: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyParamsAffirm"]
        ]
        afterpay_clearpay: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyParamsAfterpayClearpay"]
        ]
        alipay: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyParamsAlipay"]
        ]
        apple_pay: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyParamsApplePay"]
        ]
        apple_pay_later: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyParamsApplePayLater"]
        ]
        au_becs_debit: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyParamsAuBecsDebit"]
        ]
        bacs_debit: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyParamsBacsDebit"]
        ]
        bancontact: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyParamsBancontact"]
        ]
        blik: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyParamsBlik"]
        ]
        boleto: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyParamsBoleto"]
        ]
        card: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyParamsCard"]
        ]
        cartes_bancaires: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyParamsCartesBancaires"]
        ]
        cashapp: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyParamsCashapp"]
        ]
        eps: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyParamsEps"]
        ]
        expand: NotRequired[Optional[List[str]]]
        fpx: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyParamsFpx"]
        ]
        giropay: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyParamsGiropay"]
        ]
        google_pay: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyParamsGooglePay"]
        ]
        grabpay: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyParamsGrabpay"]
        ]
        ideal: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyParamsIdeal"]
        ]
        jcb: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyParamsJcb"]
        ]
        klarna: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyParamsKlarna"]
        ]
        konbini: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyParamsKonbini"]
        ]
        link: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyParamsLink"]
        ]
        name: NotRequired[Optional[str]]
        oxxo: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyParamsOxxo"]
        ]
        p24: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyParamsP24"]
        ]
        paynow: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyParamsPaynow"]
        ]
        paypal: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyParamsPaypal"]
        ]
        promptpay: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyParamsPromptpay"]
        ]
        sepa_debit: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyParamsSepaDebit"]
        ]
        sofort: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyParamsSofort"]
        ]
        us_bank_account: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyParamsUsBankAccount"]
        ]
        wechat_pay: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyParamsWechatPay"]
        ]

    class ModifyParamsWechatPay(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyParamsWechatPayDisplayPreference"
            ]
        ]

    class ModifyParamsWechatPayDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyParamsUsBankAccount(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyParamsUsBankAccountDisplayPreference"
            ]
        ]

    class ModifyParamsUsBankAccountDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyParamsSofort(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyParamsSofortDisplayPreference"
            ]
        ]

    class ModifyParamsSofortDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyParamsSepaDebit(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyParamsSepaDebitDisplayPreference"
            ]
        ]

    class ModifyParamsSepaDebitDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyParamsPromptpay(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyParamsPromptpayDisplayPreference"
            ]
        ]

    class ModifyParamsPromptpayDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyParamsPaypal(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyParamsPaypalDisplayPreference"
            ]
        ]

    class ModifyParamsPaypalDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyParamsPaynow(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyParamsPaynowDisplayPreference"
            ]
        ]

    class ModifyParamsPaynowDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyParamsP24(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyParamsP24DisplayPreference"
            ]
        ]

    class ModifyParamsP24DisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyParamsOxxo(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyParamsOxxoDisplayPreference"
            ]
        ]

    class ModifyParamsOxxoDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyParamsLink(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyParamsLinkDisplayPreference"
            ]
        ]

    class ModifyParamsLinkDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyParamsKonbini(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyParamsKonbiniDisplayPreference"
            ]
        ]

    class ModifyParamsKonbiniDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyParamsKlarna(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyParamsKlarnaDisplayPreference"
            ]
        ]

    class ModifyParamsKlarnaDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyParamsJcb(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyParamsJcbDisplayPreference"
            ]
        ]

    class ModifyParamsJcbDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyParamsIdeal(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyParamsIdealDisplayPreference"
            ]
        ]

    class ModifyParamsIdealDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyParamsGrabpay(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyParamsGrabpayDisplayPreference"
            ]
        ]

    class ModifyParamsGrabpayDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyParamsGooglePay(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyParamsGooglePayDisplayPreference"
            ]
        ]

    class ModifyParamsGooglePayDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyParamsGiropay(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyParamsGiropayDisplayPreference"
            ]
        ]

    class ModifyParamsGiropayDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyParamsFpx(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyParamsFpxDisplayPreference"
            ]
        ]

    class ModifyParamsFpxDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyParamsEps(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyParamsEpsDisplayPreference"
            ]
        ]

    class ModifyParamsEpsDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyParamsCashapp(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyParamsCashappDisplayPreference"
            ]
        ]

    class ModifyParamsCashappDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyParamsCartesBancaires(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyParamsCartesBancairesDisplayPreference"
            ]
        ]

    class ModifyParamsCartesBancairesDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyParamsCard(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyParamsCardDisplayPreference"
            ]
        ]

    class ModifyParamsCardDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyParamsBoleto(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyParamsBoletoDisplayPreference"
            ]
        ]

    class ModifyParamsBoletoDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyParamsBlik(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyParamsBlikDisplayPreference"
            ]
        ]

    class ModifyParamsBlikDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyParamsBancontact(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyParamsBancontactDisplayPreference"
            ]
        ]

    class ModifyParamsBancontactDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyParamsBacsDebit(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyParamsBacsDebitDisplayPreference"
            ]
        ]

    class ModifyParamsBacsDebitDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyParamsAuBecsDebit(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyParamsAuBecsDebitDisplayPreference"
            ]
        ]

    class ModifyParamsAuBecsDebitDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyParamsApplePayLater(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyParamsApplePayLaterDisplayPreference"
            ]
        ]

    class ModifyParamsApplePayLaterDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyParamsApplePay(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyParamsApplePayDisplayPreference"
            ]
        ]

    class ModifyParamsApplePayDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyParamsAlipay(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyParamsAlipayDisplayPreference"
            ]
        ]

    class ModifyParamsAlipayDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyParamsAfterpayClearpay(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyParamsAfterpayClearpayDisplayPreference"
            ]
        ]

    class ModifyParamsAfterpayClearpayDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyParamsAffirm(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyParamsAffirmDisplayPreference"
            ]
        ]

    class ModifyParamsAffirmDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyParamsAcssDebit(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyParamsAcssDebitDisplayPreference"
            ]
        ]

    class ModifyParamsAcssDebitDisplayPreference(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class RetrieveParams(RequestOptions):
        expand: NotRequired[Optional[List[str]]]

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
