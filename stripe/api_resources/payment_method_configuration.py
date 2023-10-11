# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Any, Optional, cast
from typing_extensions import Literal
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

    class AcssDebit(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            preference: Literal["none", "off", "on"]
            value: Literal["off", "on"]

        available: bool
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class Affirm(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            preference: Literal["none", "off", "on"]
            value: Literal["off", "on"]

        available: bool
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class AfterpayClearpay(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            preference: Literal["none", "off", "on"]
            value: Literal["off", "on"]

        available: bool
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class Alipay(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            preference: Literal["none", "off", "on"]
            value: Literal["off", "on"]

        available: bool
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class ApplePay(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            preference: Literal["none", "off", "on"]
            value: Literal["off", "on"]

        available: bool
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class AuBecsDebit(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            preference: Literal["none", "off", "on"]
            value: Literal["off", "on"]

        available: bool
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class BacsDebit(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            preference: Literal["none", "off", "on"]
            value: Literal["off", "on"]

        available: bool
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class Bancontact(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            preference: Literal["none", "off", "on"]
            value: Literal["off", "on"]

        available: bool
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class Blik(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            preference: Literal["none", "off", "on"]
            value: Literal["off", "on"]

        available: bool
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class Boleto(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            preference: Literal["none", "off", "on"]
            value: Literal["off", "on"]

        available: bool
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class Card(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            preference: Literal["none", "off", "on"]
            value: Literal["off", "on"]

        available: bool
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class CartesBancaires(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            preference: Literal["none", "off", "on"]
            value: Literal["off", "on"]

        available: bool
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class Cashapp(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            preference: Literal["none", "off", "on"]
            value: Literal["off", "on"]

        available: bool
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class Eps(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            preference: Literal["none", "off", "on"]
            value: Literal["off", "on"]

        available: bool
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class Fpx(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            preference: Literal["none", "off", "on"]
            value: Literal["off", "on"]

        available: bool
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class Giropay(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            preference: Literal["none", "off", "on"]
            value: Literal["off", "on"]

        available: bool
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class GooglePay(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            preference: Literal["none", "off", "on"]
            value: Literal["off", "on"]

        available: bool
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class Grabpay(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            preference: Literal["none", "off", "on"]
            value: Literal["off", "on"]

        available: bool
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class IdBankTransfer(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            preference: Literal["none", "off", "on"]
            value: Literal["off", "on"]

        available: bool
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class Ideal(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            preference: Literal["none", "off", "on"]
            value: Literal["off", "on"]

        available: bool
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class Jcb(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            preference: Literal["none", "off", "on"]
            value: Literal["off", "on"]

        available: bool
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class Klarna(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            preference: Literal["none", "off", "on"]
            value: Literal["off", "on"]

        available: bool
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class Konbini(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            preference: Literal["none", "off", "on"]
            value: Literal["off", "on"]

        available: bool
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class Link(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            preference: Literal["none", "off", "on"]
            value: Literal["off", "on"]

        available: bool
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class Multibanco(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            preference: Literal["none", "off", "on"]
            value: Literal["off", "on"]

        available: bool
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class Netbanking(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            preference: Literal["none", "off", "on"]
            value: Literal["off", "on"]

        available: bool
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class Oxxo(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            preference: Literal["none", "off", "on"]
            value: Literal["off", "on"]

        available: bool
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class P24(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            preference: Literal["none", "off", "on"]
            value: Literal["off", "on"]

        available: bool
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class PayByBank(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            preference: Literal["none", "off", "on"]
            value: Literal["off", "on"]

        available: bool
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class Paynow(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            preference: Literal["none", "off", "on"]
            value: Literal["off", "on"]

        available: bool
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class Paypal(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            preference: Literal["none", "off", "on"]
            value: Literal["off", "on"]

        available: bool
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class Promptpay(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            preference: Literal["none", "off", "on"]
            value: Literal["off", "on"]

        available: bool
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class SepaDebit(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            preference: Literal["none", "off", "on"]
            value: Literal["off", "on"]

        available: bool
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class Sofort(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            preference: Literal["none", "off", "on"]
            value: Literal["off", "on"]

        available: bool
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class Upi(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            preference: Literal["none", "off", "on"]
            value: Literal["off", "on"]

        available: bool
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class UsBankAccount(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            preference: Literal["none", "off", "on"]
            value: Literal["off", "on"]

        available: bool
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class WechatPay(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            preference: Literal["none", "off", "on"]
            value: Literal["off", "on"]

        available: bool
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    acss_debit: Optional[AcssDebit]
    active: bool
    affirm: Optional[Affirm]
    afterpay_clearpay: Optional[AfterpayClearpay]
    alipay: Optional[Alipay]
    apple_pay: Optional[ApplePay]
    application: Optional[str]
    au_becs_debit: Optional[AuBecsDebit]
    bacs_debit: Optional[BacsDebit]
    bancontact: Optional[Bancontact]
    blik: Optional[Blik]
    boleto: Optional[Boleto]
    card: Optional[Card]
    cartes_bancaires: Optional[CartesBancaires]
    cashapp: Optional[Cashapp]
    eps: Optional[Eps]
    fpx: Optional[Fpx]
    giropay: Optional[Giropay]
    google_pay: Optional[GooglePay]
    grabpay: Optional[Grabpay]
    id: str
    id_bank_transfer: Optional[IdBankTransfer]
    ideal: Optional[Ideal]
    is_default: bool
    jcb: Optional[Jcb]
    klarna: Optional[Klarna]
    konbini: Optional[Konbini]
    link: Optional[Link]
    livemode: bool
    multibanco: Optional[Multibanco]
    name: str
    netbanking: Optional[Netbanking]
    object: Literal["payment_method_configuration"]
    oxxo: Optional[Oxxo]
    p24: Optional[P24]
    parent: Optional[str]
    pay_by_bank: Optional[PayByBank]
    paynow: Optional[Paynow]
    paypal: Optional[Paypal]
    promptpay: Optional[Promptpay]
    sepa_debit: Optional[SepaDebit]
    sofort: Optional[Sofort]
    upi: Optional[Upi]
    us_bank_account: Optional[UsBankAccount]
    wechat_pay: Optional[WechatPay]

    @classmethod
    def create(
        cls,
        api_key: Optional[str] = None,
        idempotency_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
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
        **params: Any
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
    def modify(cls, id, **params: Any) -> "PaymentMethodConfiguration":
        url = "%s/%s" % (cls.class_url(), quote_plus(id))
        return cast(
            "PaymentMethodConfiguration",
            cls._static_request("post", url, params=params),
        )

    @classmethod
    def retrieve(
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "PaymentMethodConfiguration":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance

    _inner_class_types = {
        "acss_debit": AcssDebit,
        "affirm": Affirm,
        "afterpay_clearpay": AfterpayClearpay,
        "alipay": Alipay,
        "apple_pay": ApplePay,
        "au_becs_debit": AuBecsDebit,
        "bacs_debit": BacsDebit,
        "bancontact": Bancontact,
        "blik": Blik,
        "boleto": Boleto,
        "card": Card,
        "cartes_bancaires": CartesBancaires,
        "cashapp": Cashapp,
        "eps": Eps,
        "fpx": Fpx,
        "giropay": Giropay,
        "google_pay": GooglePay,
        "grabpay": Grabpay,
        "id_bank_transfer": IdBankTransfer,
        "ideal": Ideal,
        "jcb": Jcb,
        "klarna": Klarna,
        "konbini": Konbini,
        "link": Link,
        "multibanco": Multibanco,
        "netbanking": Netbanking,
        "oxxo": Oxxo,
        "p24": P24,
        "pay_by_bank": PayByBank,
        "paynow": Paynow,
        "paypal": Paypal,
        "promptpay": Promptpay,
        "sepa_debit": SepaDebit,
        "sofort": Sofort,
        "upi": Upi,
        "us_bank_account": UsBankAccount,
        "wechat_pay": WechatPay,
    }
