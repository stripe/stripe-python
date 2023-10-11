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
            Optional["PaymentMethodConfiguration.CreateAcssDebitParams"]
        ]
        affirm: NotRequired[
            Optional["PaymentMethodConfiguration.CreateAffirmParams"]
        ]
        afterpay_clearpay: NotRequired[
            Optional["PaymentMethodConfiguration.CreateAfterpayClearpayParams"]
        ]
        alipay: NotRequired[
            Optional["PaymentMethodConfiguration.CreateAlipayParams"]
        ]
        apple_pay: NotRequired[
            Optional["PaymentMethodConfiguration.CreateApplePayParams"]
        ]
        apple_pay_later: NotRequired[
            Optional["PaymentMethodConfiguration.CreateApplePayLaterParams"]
        ]
        au_becs_debit: NotRequired[
            Optional["PaymentMethodConfiguration.CreateAuBecsDebitParams"]
        ]
        bacs_debit: NotRequired[
            Optional["PaymentMethodConfiguration.CreateBacsDebitParams"]
        ]
        bancontact: NotRequired[
            Optional["PaymentMethodConfiguration.CreateBancontactParams"]
        ]
        blik: NotRequired[
            Optional["PaymentMethodConfiguration.CreateBlikParams"]
        ]
        boleto: NotRequired[
            Optional["PaymentMethodConfiguration.CreateBoletoParams"]
        ]
        card: NotRequired[
            Optional["PaymentMethodConfiguration.CreateCardParams"]
        ]
        cartes_bancaires: NotRequired[
            Optional["PaymentMethodConfiguration.CreateCartesBancairesParams"]
        ]
        cashapp: NotRequired[
            Optional["PaymentMethodConfiguration.CreateCashappParams"]
        ]
        eps: NotRequired[
            Optional["PaymentMethodConfiguration.CreateEpsParams"]
        ]
        expand: NotRequired[Optional[List[str]]]
        fpx: NotRequired[
            Optional["PaymentMethodConfiguration.CreateFpxParams"]
        ]
        giropay: NotRequired[
            Optional["PaymentMethodConfiguration.CreateGiropayParams"]
        ]
        google_pay: NotRequired[
            Optional["PaymentMethodConfiguration.CreateGooglePayParams"]
        ]
        grabpay: NotRequired[
            Optional["PaymentMethodConfiguration.CreateGrabpayParams"]
        ]
        ideal: NotRequired[
            Optional["PaymentMethodConfiguration.CreateIdealParams"]
        ]
        jcb: NotRequired[
            Optional["PaymentMethodConfiguration.CreateJcbParams"]
        ]
        klarna: NotRequired[
            Optional["PaymentMethodConfiguration.CreateKlarnaParams"]
        ]
        konbini: NotRequired[
            Optional["PaymentMethodConfiguration.CreateKonbiniParams"]
        ]
        link: NotRequired[
            Optional["PaymentMethodConfiguration.CreateLinkParams"]
        ]
        name: NotRequired[Optional[str]]
        oxxo: NotRequired[
            Optional["PaymentMethodConfiguration.CreateOxxoParams"]
        ]
        p24: NotRequired[
            Optional["PaymentMethodConfiguration.CreateP24Params"]
        ]
        parent: NotRequired[Optional[str]]
        paynow: NotRequired[
            Optional["PaymentMethodConfiguration.CreatePaynowParams"]
        ]
        paypal: NotRequired[
            Optional["PaymentMethodConfiguration.CreatePaypalParams"]
        ]
        promptpay: NotRequired[
            Optional["PaymentMethodConfiguration.CreatePromptpayParams"]
        ]
        sepa_debit: NotRequired[
            Optional["PaymentMethodConfiguration.CreateSepaDebitParams"]
        ]
        sofort: NotRequired[
            Optional["PaymentMethodConfiguration.CreateSofortParams"]
        ]
        us_bank_account: NotRequired[
            Optional["PaymentMethodConfiguration.CreateUsBankAccountParams"]
        ]
        wechat_pay: NotRequired[
            Optional["PaymentMethodConfiguration.CreateWechatPayParams"]
        ]

    class CreateWechatPayParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateWechatPayDisplayPreferenceParams"
            ]
        ]

    class CreateWechatPayDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateUsBankAccountParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateUsBankAccountDisplayPreferenceParams"
            ]
        ]

    class CreateUsBankAccountDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateSofortParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateSofortDisplayPreferenceParams"
            ]
        ]

    class CreateSofortDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateSepaDebitParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateSepaDebitDisplayPreferenceParams"
            ]
        ]

    class CreateSepaDebitDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreatePromptpayParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreatePromptpayDisplayPreferenceParams"
            ]
        ]

    class CreatePromptpayDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreatePaypalParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreatePaypalDisplayPreferenceParams"
            ]
        ]

    class CreatePaypalDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreatePaynowParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreatePaynowDisplayPreferenceParams"
            ]
        ]

    class CreatePaynowDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateP24Params(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateP24DisplayPreferenceParams"
            ]
        ]

    class CreateP24DisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateOxxoParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateOxxoDisplayPreferenceParams"
            ]
        ]

    class CreateOxxoDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateLinkParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateLinkDisplayPreferenceParams"
            ]
        ]

    class CreateLinkDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateKonbiniParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateKonbiniDisplayPreferenceParams"
            ]
        ]

    class CreateKonbiniDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateKlarnaParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateKlarnaDisplayPreferenceParams"
            ]
        ]

    class CreateKlarnaDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateJcbParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateJcbDisplayPreferenceParams"
            ]
        ]

    class CreateJcbDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateIdealParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateIdealDisplayPreferenceParams"
            ]
        ]

    class CreateIdealDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateGrabpayParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateGrabpayDisplayPreferenceParams"
            ]
        ]

    class CreateGrabpayDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateGooglePayParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateGooglePayDisplayPreferenceParams"
            ]
        ]

    class CreateGooglePayDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateGiropayParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateGiropayDisplayPreferenceParams"
            ]
        ]

    class CreateGiropayDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateFpxParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateFpxDisplayPreferenceParams"
            ]
        ]

    class CreateFpxDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateEpsParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateEpsDisplayPreferenceParams"
            ]
        ]

    class CreateEpsDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateCashappParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateCashappDisplayPreferenceParams"
            ]
        ]

    class CreateCashappDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateCartesBancairesParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateCartesBancairesDisplayPreferenceParams"
            ]
        ]

    class CreateCartesBancairesDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateCardParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateCardDisplayPreferenceParams"
            ]
        ]

    class CreateCardDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateBoletoParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateBoletoDisplayPreferenceParams"
            ]
        ]

    class CreateBoletoDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateBlikParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateBlikDisplayPreferenceParams"
            ]
        ]

    class CreateBlikDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateBancontactParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateBancontactDisplayPreferenceParams"
            ]
        ]

    class CreateBancontactDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateBacsDebitParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateBacsDebitDisplayPreferenceParams"
            ]
        ]

    class CreateBacsDebitDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateAuBecsDebitParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateAuBecsDebitDisplayPreferenceParams"
            ]
        ]

    class CreateAuBecsDebitDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateApplePayLaterParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateApplePayLaterDisplayPreferenceParams"
            ]
        ]

    class CreateApplePayLaterDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateApplePayParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateApplePayDisplayPreferenceParams"
            ]
        ]

    class CreateApplePayDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateAlipayParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateAlipayDisplayPreferenceParams"
            ]
        ]

    class CreateAlipayDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateAfterpayClearpayParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateAfterpayClearpayDisplayPreferenceParams"
            ]
        ]

    class CreateAfterpayClearpayDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateAffirmParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateAffirmDisplayPreferenceParams"
            ]
        ]

    class CreateAffirmDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class CreateAcssDebitParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.CreateAcssDebitDisplayPreferenceParams"
            ]
        ]

    class CreateAcssDebitDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ListParams(RequestOptions):
        application: NotRequired[Optional[Union[Literal[""], str]]]
        expand: NotRequired[Optional[List[str]]]

    class ModifyParams(RequestOptions):
        acss_debit: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyAcssDebitParams"]
        ]
        active: NotRequired[Optional[bool]]
        affirm: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyAffirmParams"]
        ]
        afterpay_clearpay: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyAfterpayClearpayParams"]
        ]
        alipay: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyAlipayParams"]
        ]
        apple_pay: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyApplePayParams"]
        ]
        apple_pay_later: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyApplePayLaterParams"]
        ]
        au_becs_debit: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyAuBecsDebitParams"]
        ]
        bacs_debit: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyBacsDebitParams"]
        ]
        bancontact: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyBancontactParams"]
        ]
        blik: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyBlikParams"]
        ]
        boleto: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyBoletoParams"]
        ]
        card: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyCardParams"]
        ]
        cartes_bancaires: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyCartesBancairesParams"]
        ]
        cashapp: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyCashappParams"]
        ]
        eps: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyEpsParams"]
        ]
        expand: NotRequired[Optional[List[str]]]
        fpx: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyFpxParams"]
        ]
        giropay: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyGiropayParams"]
        ]
        google_pay: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyGooglePayParams"]
        ]
        grabpay: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyGrabpayParams"]
        ]
        ideal: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyIdealParams"]
        ]
        jcb: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyJcbParams"]
        ]
        klarna: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyKlarnaParams"]
        ]
        konbini: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyKonbiniParams"]
        ]
        link: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyLinkParams"]
        ]
        name: NotRequired[Optional[str]]
        oxxo: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyOxxoParams"]
        ]
        p24: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyP24Params"]
        ]
        paynow: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyPaynowParams"]
        ]
        paypal: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyPaypalParams"]
        ]
        promptpay: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyPromptpayParams"]
        ]
        sepa_debit: NotRequired[
            Optional["PaymentMethodConfiguration.ModifySepaDebitParams"]
        ]
        sofort: NotRequired[
            Optional["PaymentMethodConfiguration.ModifySofortParams"]
        ]
        us_bank_account: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyUsBankAccountParams"]
        ]
        wechat_pay: NotRequired[
            Optional["PaymentMethodConfiguration.ModifyWechatPayParams"]
        ]

    class ModifyWechatPayParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyWechatPayDisplayPreferenceParams"
            ]
        ]

    class ModifyWechatPayDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyUsBankAccountParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyUsBankAccountDisplayPreferenceParams"
            ]
        ]

    class ModifyUsBankAccountDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifySofortParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifySofortDisplayPreferenceParams"
            ]
        ]

    class ModifySofortDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifySepaDebitParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifySepaDebitDisplayPreferenceParams"
            ]
        ]

    class ModifySepaDebitDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyPromptpayParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyPromptpayDisplayPreferenceParams"
            ]
        ]

    class ModifyPromptpayDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyPaypalParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyPaypalDisplayPreferenceParams"
            ]
        ]

    class ModifyPaypalDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyPaynowParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyPaynowDisplayPreferenceParams"
            ]
        ]

    class ModifyPaynowDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyP24Params(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyP24DisplayPreferenceParams"
            ]
        ]

    class ModifyP24DisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyOxxoParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyOxxoDisplayPreferenceParams"
            ]
        ]

    class ModifyOxxoDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyLinkParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyLinkDisplayPreferenceParams"
            ]
        ]

    class ModifyLinkDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyKonbiniParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyKonbiniDisplayPreferenceParams"
            ]
        ]

    class ModifyKonbiniDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyKlarnaParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyKlarnaDisplayPreferenceParams"
            ]
        ]

    class ModifyKlarnaDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyJcbParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyJcbDisplayPreferenceParams"
            ]
        ]

    class ModifyJcbDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyIdealParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyIdealDisplayPreferenceParams"
            ]
        ]

    class ModifyIdealDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyGrabpayParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyGrabpayDisplayPreferenceParams"
            ]
        ]

    class ModifyGrabpayDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyGooglePayParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyGooglePayDisplayPreferenceParams"
            ]
        ]

    class ModifyGooglePayDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyGiropayParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyGiropayDisplayPreferenceParams"
            ]
        ]

    class ModifyGiropayDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyFpxParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyFpxDisplayPreferenceParams"
            ]
        ]

    class ModifyFpxDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyEpsParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyEpsDisplayPreferenceParams"
            ]
        ]

    class ModifyEpsDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyCashappParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyCashappDisplayPreferenceParams"
            ]
        ]

    class ModifyCashappDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyCartesBancairesParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyCartesBancairesDisplayPreferenceParams"
            ]
        ]

    class ModifyCartesBancairesDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyCardParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyCardDisplayPreferenceParams"
            ]
        ]

    class ModifyCardDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyBoletoParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyBoletoDisplayPreferenceParams"
            ]
        ]

    class ModifyBoletoDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyBlikParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyBlikDisplayPreferenceParams"
            ]
        ]

    class ModifyBlikDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyBancontactParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyBancontactDisplayPreferenceParams"
            ]
        ]

    class ModifyBancontactDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyBacsDebitParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyBacsDebitDisplayPreferenceParams"
            ]
        ]

    class ModifyBacsDebitDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyAuBecsDebitParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyAuBecsDebitDisplayPreferenceParams"
            ]
        ]

    class ModifyAuBecsDebitDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyApplePayLaterParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyApplePayLaterDisplayPreferenceParams"
            ]
        ]

    class ModifyApplePayLaterDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyApplePayParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyApplePayDisplayPreferenceParams"
            ]
        ]

    class ModifyApplePayDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyAlipayParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyAlipayDisplayPreferenceParams"
            ]
        ]

    class ModifyAlipayDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyAfterpayClearpayParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyAfterpayClearpayDisplayPreferenceParams"
            ]
        ]

    class ModifyAfterpayClearpayDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyAffirmParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyAffirmDisplayPreferenceParams"
            ]
        ]

    class ModifyAffirmDisplayPreferenceParams(TypedDict):
        preference: NotRequired[Optional[Literal["none", "off", "on"]]]

    class ModifyAcssDebitParams(TypedDict):
        display_preference: NotRequired[
            Optional[
                "PaymentMethodConfiguration.ModifyAcssDebitDisplayPreferenceParams"
            ]
        ]

    class ModifyAcssDebitDisplayPreferenceParams(TypedDict):
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
