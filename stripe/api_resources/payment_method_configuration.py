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
from typing import ClassVar, List, Optional, cast
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

    OBJECT_NAME: ClassVar[
        Literal["payment_method_configuration"]
    ] = "payment_method_configuration"

    class AcssDebit(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            """
            For child configs, whether or not the account's preference will be observed. If `false`, the parent configuration's default is used.
            """
            preference: Literal["none", "off", "on"]
            """
            The account's display preference.
            """
            value: Literal["off", "on"]
            """
            The effective display preference value.
            """

        available: bool
        """
        Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method's capability is active.
        """
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class Affirm(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            """
            For child configs, whether or not the account's preference will be observed. If `false`, the parent configuration's default is used.
            """
            preference: Literal["none", "off", "on"]
            """
            The account's display preference.
            """
            value: Literal["off", "on"]
            """
            The effective display preference value.
            """

        available: bool
        """
        Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method's capability is active.
        """
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class AfterpayClearpay(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            """
            For child configs, whether or not the account's preference will be observed. If `false`, the parent configuration's default is used.
            """
            preference: Literal["none", "off", "on"]
            """
            The account's display preference.
            """
            value: Literal["off", "on"]
            """
            The effective display preference value.
            """

        available: bool
        """
        Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method's capability is active.
        """
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class Alipay(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            """
            For child configs, whether or not the account's preference will be observed. If `false`, the parent configuration's default is used.
            """
            preference: Literal["none", "off", "on"]
            """
            The account's display preference.
            """
            value: Literal["off", "on"]
            """
            The effective display preference value.
            """

        available: bool
        """
        Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method's capability is active.
        """
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class ApplePay(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            """
            For child configs, whether or not the account's preference will be observed. If `false`, the parent configuration's default is used.
            """
            preference: Literal["none", "off", "on"]
            """
            The account's display preference.
            """
            value: Literal["off", "on"]
            """
            The effective display preference value.
            """

        available: bool
        """
        Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method's capability is active.
        """
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class AuBecsDebit(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            """
            For child configs, whether or not the account's preference will be observed. If `false`, the parent configuration's default is used.
            """
            preference: Literal["none", "off", "on"]
            """
            The account's display preference.
            """
            value: Literal["off", "on"]
            """
            The effective display preference value.
            """

        available: bool
        """
        Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method's capability is active.
        """
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class BacsDebit(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            """
            For child configs, whether or not the account's preference will be observed. If `false`, the parent configuration's default is used.
            """
            preference: Literal["none", "off", "on"]
            """
            The account's display preference.
            """
            value: Literal["off", "on"]
            """
            The effective display preference value.
            """

        available: bool
        """
        Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method's capability is active.
        """
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class Bancontact(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            """
            For child configs, whether or not the account's preference will be observed. If `false`, the parent configuration's default is used.
            """
            preference: Literal["none", "off", "on"]
            """
            The account's display preference.
            """
            value: Literal["off", "on"]
            """
            The effective display preference value.
            """

        available: bool
        """
        Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method's capability is active.
        """
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class Blik(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            """
            For child configs, whether or not the account's preference will be observed. If `false`, the parent configuration's default is used.
            """
            preference: Literal["none", "off", "on"]
            """
            The account's display preference.
            """
            value: Literal["off", "on"]
            """
            The effective display preference value.
            """

        available: bool
        """
        Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method's capability is active.
        """
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class Boleto(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            """
            For child configs, whether or not the account's preference will be observed. If `false`, the parent configuration's default is used.
            """
            preference: Literal["none", "off", "on"]
            """
            The account's display preference.
            """
            value: Literal["off", "on"]
            """
            The effective display preference value.
            """

        available: bool
        """
        Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method's capability is active.
        """
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class Card(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            """
            For child configs, whether or not the account's preference will be observed. If `false`, the parent configuration's default is used.
            """
            preference: Literal["none", "off", "on"]
            """
            The account's display preference.
            """
            value: Literal["off", "on"]
            """
            The effective display preference value.
            """

        available: bool
        """
        Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method's capability is active.
        """
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class CartesBancaires(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            """
            For child configs, whether or not the account's preference will be observed. If `false`, the parent configuration's default is used.
            """
            preference: Literal["none", "off", "on"]
            """
            The account's display preference.
            """
            value: Literal["off", "on"]
            """
            The effective display preference value.
            """

        available: bool
        """
        Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method's capability is active.
        """
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class Cashapp(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            """
            For child configs, whether or not the account's preference will be observed. If `false`, the parent configuration's default is used.
            """
            preference: Literal["none", "off", "on"]
            """
            The account's display preference.
            """
            value: Literal["off", "on"]
            """
            The effective display preference value.
            """

        available: bool
        """
        Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method's capability is active.
        """
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class Eps(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            """
            For child configs, whether or not the account's preference will be observed. If `false`, the parent configuration's default is used.
            """
            preference: Literal["none", "off", "on"]
            """
            The account's display preference.
            """
            value: Literal["off", "on"]
            """
            The effective display preference value.
            """

        available: bool
        """
        Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method's capability is active.
        """
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class Fpx(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            """
            For child configs, whether or not the account's preference will be observed. If `false`, the parent configuration's default is used.
            """
            preference: Literal["none", "off", "on"]
            """
            The account's display preference.
            """
            value: Literal["off", "on"]
            """
            The effective display preference value.
            """

        available: bool
        """
        Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method's capability is active.
        """
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class Giropay(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            """
            For child configs, whether or not the account's preference will be observed. If `false`, the parent configuration's default is used.
            """
            preference: Literal["none", "off", "on"]
            """
            The account's display preference.
            """
            value: Literal["off", "on"]
            """
            The effective display preference value.
            """

        available: bool
        """
        Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method's capability is active.
        """
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class GooglePay(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            """
            For child configs, whether or not the account's preference will be observed. If `false`, the parent configuration's default is used.
            """
            preference: Literal["none", "off", "on"]
            """
            The account's display preference.
            """
            value: Literal["off", "on"]
            """
            The effective display preference value.
            """

        available: bool
        """
        Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method's capability is active.
        """
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class Grabpay(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            """
            For child configs, whether or not the account's preference will be observed. If `false`, the parent configuration's default is used.
            """
            preference: Literal["none", "off", "on"]
            """
            The account's display preference.
            """
            value: Literal["off", "on"]
            """
            The effective display preference value.
            """

        available: bool
        """
        Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method's capability is active.
        """
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class IdBankTransfer(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            """
            For child configs, whether or not the account's preference will be observed. If `false`, the parent configuration's default is used.
            """
            preference: Literal["none", "off", "on"]
            """
            The account's display preference.
            """
            value: Literal["off", "on"]
            """
            The effective display preference value.
            """

        available: bool
        """
        Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method's capability is active.
        """
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class Ideal(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            """
            For child configs, whether or not the account's preference will be observed. If `false`, the parent configuration's default is used.
            """
            preference: Literal["none", "off", "on"]
            """
            The account's display preference.
            """
            value: Literal["off", "on"]
            """
            The effective display preference value.
            """

        available: bool
        """
        Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method's capability is active.
        """
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class Jcb(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            """
            For child configs, whether or not the account's preference will be observed. If `false`, the parent configuration's default is used.
            """
            preference: Literal["none", "off", "on"]
            """
            The account's display preference.
            """
            value: Literal["off", "on"]
            """
            The effective display preference value.
            """

        available: bool
        """
        Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method's capability is active.
        """
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class Klarna(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            """
            For child configs, whether or not the account's preference will be observed. If `false`, the parent configuration's default is used.
            """
            preference: Literal["none", "off", "on"]
            """
            The account's display preference.
            """
            value: Literal["off", "on"]
            """
            The effective display preference value.
            """

        available: bool
        """
        Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method's capability is active.
        """
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class Konbini(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            """
            For child configs, whether or not the account's preference will be observed. If `false`, the parent configuration's default is used.
            """
            preference: Literal["none", "off", "on"]
            """
            The account's display preference.
            """
            value: Literal["off", "on"]
            """
            The effective display preference value.
            """

        available: bool
        """
        Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method's capability is active.
        """
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class Link(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            """
            For child configs, whether or not the account's preference will be observed. If `false`, the parent configuration's default is used.
            """
            preference: Literal["none", "off", "on"]
            """
            The account's display preference.
            """
            value: Literal["off", "on"]
            """
            The effective display preference value.
            """

        available: bool
        """
        Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method's capability is active.
        """
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class Multibanco(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            """
            For child configs, whether or not the account's preference will be observed. If `false`, the parent configuration's default is used.
            """
            preference: Literal["none", "off", "on"]
            """
            The account's display preference.
            """
            value: Literal["off", "on"]
            """
            The effective display preference value.
            """

        available: bool
        """
        Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method's capability is active.
        """
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class Netbanking(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            """
            For child configs, whether or not the account's preference will be observed. If `false`, the parent configuration's default is used.
            """
            preference: Literal["none", "off", "on"]
            """
            The account's display preference.
            """
            value: Literal["off", "on"]
            """
            The effective display preference value.
            """

        available: bool
        """
        Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method's capability is active.
        """
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class Oxxo(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            """
            For child configs, whether or not the account's preference will be observed. If `false`, the parent configuration's default is used.
            """
            preference: Literal["none", "off", "on"]
            """
            The account's display preference.
            """
            value: Literal["off", "on"]
            """
            The effective display preference value.
            """

        available: bool
        """
        Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method's capability is active.
        """
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class P24(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            """
            For child configs, whether or not the account's preference will be observed. If `false`, the parent configuration's default is used.
            """
            preference: Literal["none", "off", "on"]
            """
            The account's display preference.
            """
            value: Literal["off", "on"]
            """
            The effective display preference value.
            """

        available: bool
        """
        Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method's capability is active.
        """
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class PayByBank(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            """
            For child configs, whether or not the account's preference will be observed. If `false`, the parent configuration's default is used.
            """
            preference: Literal["none", "off", "on"]
            """
            The account's display preference.
            """
            value: Literal["off", "on"]
            """
            The effective display preference value.
            """

        available: bool
        """
        Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method's capability is active.
        """
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class Paynow(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            """
            For child configs, whether or not the account's preference will be observed. If `false`, the parent configuration's default is used.
            """
            preference: Literal["none", "off", "on"]
            """
            The account's display preference.
            """
            value: Literal["off", "on"]
            """
            The effective display preference value.
            """

        available: bool
        """
        Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method's capability is active.
        """
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class Paypal(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            """
            For child configs, whether or not the account's preference will be observed. If `false`, the parent configuration's default is used.
            """
            preference: Literal["none", "off", "on"]
            """
            The account's display preference.
            """
            value: Literal["off", "on"]
            """
            The effective display preference value.
            """

        available: bool
        """
        Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method's capability is active.
        """
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class Promptpay(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            """
            For child configs, whether or not the account's preference will be observed. If `false`, the parent configuration's default is used.
            """
            preference: Literal["none", "off", "on"]
            """
            The account's display preference.
            """
            value: Literal["off", "on"]
            """
            The effective display preference value.
            """

        available: bool
        """
        Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method's capability is active.
        """
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class SepaDebit(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            """
            For child configs, whether or not the account's preference will be observed. If `false`, the parent configuration's default is used.
            """
            preference: Literal["none", "off", "on"]
            """
            The account's display preference.
            """
            value: Literal["off", "on"]
            """
            The effective display preference value.
            """

        available: bool
        """
        Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method's capability is active.
        """
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class Sofort(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            """
            For child configs, whether or not the account's preference will be observed. If `false`, the parent configuration's default is used.
            """
            preference: Literal["none", "off", "on"]
            """
            The account's display preference.
            """
            value: Literal["off", "on"]
            """
            The effective display preference value.
            """

        available: bool
        """
        Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method's capability is active.
        """
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class Upi(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            """
            For child configs, whether or not the account's preference will be observed. If `false`, the parent configuration's default is used.
            """
            preference: Literal["none", "off", "on"]
            """
            The account's display preference.
            """
            value: Literal["off", "on"]
            """
            The effective display preference value.
            """

        available: bool
        """
        Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method's capability is active.
        """
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class UsBankAccount(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            """
            For child configs, whether or not the account's preference will be observed. If `false`, the parent configuration's default is used.
            """
            preference: Literal["none", "off", "on"]
            """
            The account's display preference.
            """
            value: Literal["off", "on"]
            """
            The effective display preference value.
            """

        available: bool
        """
        Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method's capability is active.
        """
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    class WechatPay(StripeObject):
        class DisplayPreference(StripeObject):
            overridable: Optional[bool]
            """
            For child configs, whether or not the account's preference will be observed. If `false`, the parent configuration's default is used.
            """
            preference: Literal["none", "off", "on"]
            """
            The account's display preference.
            """
            value: Literal["off", "on"]
            """
            The effective display preference value.
            """

        available: bool
        """
        Whether this payment method may be offered at checkout. True if `display_preference` is `on` and the payment method's capability is active.
        """
        display_preference: DisplayPreference
        _inner_class_types = {"display_preference": DisplayPreference}

    if TYPE_CHECKING:

        class CreateParams(RequestOptions):
            acss_debit: NotRequired[
                "PaymentMethodConfiguration.CreateParamsAcssDebit|None"
            ]
            """
            Canadian pre-authorized debit payments, check this [page](https://stripe.com/docs/payments/acss-debit) for more details like country availability.
            """
            affirm: NotRequired[
                "PaymentMethodConfiguration.CreateParamsAffirm|None"
            ]
            """
            [Affirm](https://www.affirm.com/) gives your customers a way to split purchases over a series of payments. Depending on the purchase, they can pay with four interest-free payments (Split Pay) or pay over a longer term (Installments), which might include interest. Check this [page](https://stripe.com/docs/payments/affirm) for more details like country availability.
            """
            afterpay_clearpay: NotRequired[
                "PaymentMethodConfiguration.CreateParamsAfterpayClearpay|None"
            ]
            """
            Afterpay gives your customers a way to pay for purchases in installments, check this [page](https://stripe.com/docs/payments/afterpay-clearpay) for more details like country availability. Afterpay is particularly popular among businesses selling fashion, beauty, and sports products.
            """
            alipay: NotRequired[
                "PaymentMethodConfiguration.CreateParamsAlipay|None"
            ]
            """
            Alipay is a digital wallet in China that has more than a billion active users worldwide. Alipay users can pay on the web or on a mobile device using login credentials or their Alipay app. Alipay has a low dispute rate and reduces fraud by authenticating payments using the customer's login credentials. Check this [page](https://stripe.com/docs/payments/alipay) for more details.
            """
            apple_pay: NotRequired[
                "PaymentMethodConfiguration.CreateParamsApplePay|None"
            ]
            """
            Stripe users can accept [Apple Pay](https://stripe.com/payments/apple-pay) in iOS applications in iOS 9 and later, and on the web in Safari starting with iOS 10 or macOS Sierra. There are no additional fees to process Apple Pay payments, and the [pricing](https://stripe.com/pricing) is the same as other card transactions. Check this [page](https://stripe.com/docs/apple-pay) for more details.
            """
            apple_pay_later: NotRequired[
                "PaymentMethodConfiguration.CreateParamsApplePayLater|None"
            ]
            """
            Apple Pay Later, a payment method for customers to buy now and pay later, gives your customers a way to split purchases into four installments across six weeks.
            """
            au_becs_debit: NotRequired[
                "PaymentMethodConfiguration.CreateParamsAuBecsDebit|None"
            ]
            """
            Stripe users in Australia can accept Bulk Electronic Clearing System (BECS) direct debit payments from customers with an Australian bank account. Check this [page](https://stripe.com/docs/payments/au-becs-debit) for more details.
            """
            bacs_debit: NotRequired[
                "PaymentMethodConfiguration.CreateParamsBacsDebit|None"
            ]
            """
            Stripe users in the UK can accept Bacs Direct Debit payments from customers with a UK bank account, check this [page](https://stripe.com/docs/payments/payment-methods/bacs-debit) for more details.
            """
            bancontact: NotRequired[
                "PaymentMethodConfiguration.CreateParamsBancontact|None"
            ]
            """
            Bancontact is the most popular online payment method in Belgium, with over 15 million cards in circulation. [Customers](https://stripe.com/docs/api/customers) use a Bancontact card or mobile app linked to a Belgian bank account to make online payments that are secure, guaranteed, and confirmed immediately. Check this [page](https://stripe.com/docs/payments/bancontact) for more details.
            """
            blik: NotRequired[
                "PaymentMethodConfiguration.CreateParamsBlik|None"
            ]
            """
            BLIK is a [single use](https://stripe.com/docs/payments/payment-methods#usage) payment method that requires customers to authenticate their payments. When customers want to pay online using BLIK, they request a six-digit code from their banking application and enter it into the payment collection form. Check this [page](https://stripe.com/docs/payments/blik) for more details.
            """
            boleto: NotRequired[
                "PaymentMethodConfiguration.CreateParamsBoleto|None"
            ]
            """
            Boleto is an official (regulated by the Central Bank of Brazil) payment method in Brazil. Check this [page](https://stripe.com/docs/payments/boleto) for more details.
            """
            card: NotRequired[
                "PaymentMethodConfiguration.CreateParamsCard|None"
            ]
            """
            Cards are a popular way for consumers and businesses to pay online or in person. Stripe supports global and local card networks.
            """
            cartes_bancaires: NotRequired[
                "PaymentMethodConfiguration.CreateParamsCartesBancaires|None"
            ]
            """
            Cartes Bancaires is France's local card network. More than 95% of these cards are co-branded with either Visa or Mastercard, meaning you can process these cards over either Cartes Bancaires or the Visa or Mastercard networks. Check this [page](https://stripe.com/docs/payments/cartes-bancaires) for more details.
            """
            cashapp: NotRequired[
                "PaymentMethodConfiguration.CreateParamsCashapp|None"
            ]
            """
            Cash App is a popular consumer app in the US that allows customers to bank, invest, send, and receive money using their digital wallet. Check this [page](https://stripe.com/docs/payments/cash-app-pay) for more details.
            """
            eps: NotRequired["PaymentMethodConfiguration.CreateParamsEps|None"]
            """
            EPS is an Austria-based payment method that allows customers to complete transactions online using their bank credentials. EPS is supported by all Austrian banks and is accepted by over 80% of Austrian online retailers. Check this [page](https://stripe.com/docs/payments/eps) for more details.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            fpx: NotRequired["PaymentMethodConfiguration.CreateParamsFpx|None"]
            """
            Financial Process Exchange (FPX) is a Malaysia-based payment method that allows customers to complete transactions online using their bank credentials. Bank Negara Malaysia (BNM), the Central Bank of Malaysia, and eleven other major Malaysian financial institutions are members of the PayNet Group, which owns and operates FPX. It is one of the most popular online payment methods in Malaysia, with nearly 90 million transactions in 2018 according to BNM. Check this [page](https://stripe.com/docs/payments/fpx) for more details.
            """
            giropay: NotRequired[
                "PaymentMethodConfiguration.CreateParamsGiropay|None"
            ]
            """
            giropay is a German payment method based on online banking, introduced in 2006. It allows customers to complete transactions online using their online banking environment, with funds debited from their bank account. Depending on their bank, customers confirm payments on giropay using a second factor of authentication or a PIN. giropay accounts for 10% of online checkouts in Germany. Check this [page](https://stripe.com/docs/payments/giropay) for more details.
            """
            google_pay: NotRequired[
                "PaymentMethodConfiguration.CreateParamsGooglePay|None"
            ]
            """
            Google Pay allows customers to make payments in your app or website using any credit or debit card saved to their Google Account, including those from Google Play, YouTube, Chrome, or an Android device. Use the Google Pay API to request any credit or debit card stored in your customer's Google account. Check this [page](https://stripe.com/docs/google-pay) for more details.
            """
            grabpay: NotRequired[
                "PaymentMethodConfiguration.CreateParamsGrabpay|None"
            ]
            """
            GrabPay is a payment method developed by [Grab](https://www.grab.com/sg/consumer/finance/pay/). GrabPay is a digital wallet - customers maintain a balance in their wallets that they pay out with. Check this [page](https://stripe.com/docs/payments/grabpay) for more details.
            """
            ideal: NotRequired[
                "PaymentMethodConfiguration.CreateParamsIdeal|None"
            ]
            """
            iDEAL is a Netherlands-based payment method that allows customers to complete transactions online using their bank credentials. All major Dutch banks are members of Currence, the scheme that operates iDEAL, making it the most popular online payment method in the Netherlands with a share of online transactions close to 55%. Check this [page](https://stripe.com/docs/payments/ideal) for more details.
            """
            jcb: NotRequired["PaymentMethodConfiguration.CreateParamsJcb|None"]
            """
            JCB is a credit card company based in Japan. JCB is currently available in Japan to businesses approved by JCB, and available to all businesses in Australia, Canada, Hong Kong, Japan, New Zealand, Singapore, Switzerland, United Kingdom, United States, and all countries in the European Economic Area except Iceland. Check this [page](https://support.stripe.com/questions/accepting-japan-credit-bureau-%28jcb%29-payments) for more details.
            """
            klarna: NotRequired[
                "PaymentMethodConfiguration.CreateParamsKlarna|None"
            ]
            """
            Klarna gives customers a range of [payment options](https://stripe.com/docs/payments/klarna#payment-options) during checkout. Available payment options vary depending on the customer's billing address and the transaction amount. These payment options make it convenient for customers to purchase items in all price ranges. Check this [page](https://stripe.com/docs/payments/klarna) for more details.
            """
            konbini: NotRequired[
                "PaymentMethodConfiguration.CreateParamsKonbini|None"
            ]
            """
            Konbini allows customers in Japan to pay for bills and online purchases at convenience stores with cash. Check this [page](https://stripe.com/docs/payments/konbini) for more details.
            """
            link: NotRequired[
                "PaymentMethodConfiguration.CreateParamsLink|None"
            ]
            """
            [Link](https://stripe.com/docs/payments/link) is a payment method network. With Link, users save their payment details once, then reuse that information to pay with one click for any business on the network.
            """
            name: NotRequired["str|None"]
            """
            Configuration name.
            """
            oxxo: NotRequired[
                "PaymentMethodConfiguration.CreateParamsOxxo|None"
            ]
            """
            OXXO is a Mexican chain of convenience stores with thousands of locations across Latin America and represents nearly 20% of online transactions in Mexico. OXXO allows customers to pay bills and online purchases in-store with cash. Check this [page](https://stripe.com/docs/payments/oxxo) for more details.
            """
            p24: NotRequired["PaymentMethodConfiguration.CreateParamsP24|None"]
            """
            Przelewy24 is a Poland-based payment method aggregator that allows customers to complete transactions online using bank transfers and other methods. Bank transfers account for 30% of online payments in Poland and Przelewy24 provides a way for customers to pay with over 165 banks. Check this [page](https://stripe.com/docs/payments/p24) for more details.
            """
            parent: NotRequired["str|None"]
            """
            Configuration's parent configuration. Specify to create a child configuration.
            """
            paynow: NotRequired[
                "PaymentMethodConfiguration.CreateParamsPaynow|None"
            ]
            """
            PayNow is a Singapore-based payment method that allows customers to make a payment using their preferred app from participating banks and participating non-bank financial institutions. Check this [page](https://stripe.com/docs/payments/paynow) for more details.
            """
            paypal: NotRequired[
                "PaymentMethodConfiguration.CreateParamsPaypal|None"
            ]
            """
            PayPal, a digital wallet popular with customers in Europe, allows your customers worldwide to pay using their PayPal account. Check this [page](https://stripe.com/docs/payments/paypal) for more details.
            """
            promptpay: NotRequired[
                "PaymentMethodConfiguration.CreateParamsPromptpay|None"
            ]
            """
            PromptPay is a Thailand-based payment method that allows customers to make a payment using their preferred app from participating banks. Check this [page](https://stripe.com/docs/payments/promptpay) for more details.
            """
            sepa_debit: NotRequired[
                "PaymentMethodConfiguration.CreateParamsSepaDebit|None"
            ]
            """
            The [Single Euro Payments Area (SEPA)](https://en.wikipedia.org/wiki/Single_Euro_Payments_Area) is an initiative of the European Union to simplify payments within and across member countries. SEPA established and enforced banking standards to allow for the direct debiting of every EUR-denominated bank account within the SEPA region, check this [page](https://stripe.com/docs/payments/sepa-debit) for more details.
            """
            sofort: NotRequired[
                "PaymentMethodConfiguration.CreateParamsSofort|None"
            ]
            """
            Stripe users in Europe and the United States can use the [Payment Intents API](https://stripe.com/docs/payments/payment-intents)—a single integration path for creating payments using any supported method—to accept [Sofort](https://www.sofort.com/) payments from customers. Check this [page](https://stripe.com/docs/payments/sofort) for more details.
            """
            us_bank_account: NotRequired[
                "PaymentMethodConfiguration.CreateParamsUsBankAccount|None"
            ]
            """
            Stripe users in the United States can accept ACH direct debit payments from customers with a US bank account using the Automated Clearing House (ACH) payments system operated by Nacha. Check this [page](https://stripe.com/docs/payments/ach-debit) for more details.
            """
            wechat_pay: NotRequired[
                "PaymentMethodConfiguration.CreateParamsWechatPay|None"
            ]
            """
            WeChat, owned by Tencent, is China's leading mobile app with over 1 billion monthly active users. Chinese consumers can use WeChat Pay to pay for goods and services inside of businesses' apps and websites. WeChat Pay users buy most frequently in gaming, e-commerce, travel, online education, and food/nutrition. Check this [page](https://stripe.com/docs/payments/wechat-pay) for more details.
            """

        class CreateParamsWechatPay(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsWechatPayDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class CreateParamsWechatPayDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class CreateParamsUsBankAccount(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsUsBankAccountDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class CreateParamsUsBankAccountDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class CreateParamsSofort(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsSofortDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class CreateParamsSofortDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class CreateParamsSepaDebit(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsSepaDebitDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class CreateParamsSepaDebitDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class CreateParamsPromptpay(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsPromptpayDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class CreateParamsPromptpayDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class CreateParamsPaypal(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsPaypalDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class CreateParamsPaypalDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class CreateParamsPaynow(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsPaynowDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class CreateParamsPaynowDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class CreateParamsP24(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsP24DisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class CreateParamsP24DisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class CreateParamsOxxo(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsOxxoDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class CreateParamsOxxoDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class CreateParamsLink(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsLinkDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class CreateParamsLinkDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class CreateParamsKonbini(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsKonbiniDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class CreateParamsKonbiniDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class CreateParamsKlarna(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsKlarnaDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class CreateParamsKlarnaDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class CreateParamsJcb(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsJcbDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class CreateParamsJcbDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class CreateParamsIdeal(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsIdealDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class CreateParamsIdealDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class CreateParamsGrabpay(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsGrabpayDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class CreateParamsGrabpayDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class CreateParamsGooglePay(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsGooglePayDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class CreateParamsGooglePayDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class CreateParamsGiropay(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsGiropayDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class CreateParamsGiropayDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class CreateParamsFpx(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsFpxDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class CreateParamsFpxDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class CreateParamsEps(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsEpsDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class CreateParamsEpsDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class CreateParamsCashapp(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsCashappDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class CreateParamsCashappDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class CreateParamsCartesBancaires(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsCartesBancairesDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class CreateParamsCartesBancairesDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class CreateParamsCard(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsCardDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class CreateParamsCardDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class CreateParamsBoleto(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsBoletoDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class CreateParamsBoletoDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class CreateParamsBlik(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsBlikDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class CreateParamsBlikDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class CreateParamsBancontact(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsBancontactDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class CreateParamsBancontactDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class CreateParamsBacsDebit(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsBacsDebitDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class CreateParamsBacsDebitDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class CreateParamsAuBecsDebit(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsAuBecsDebitDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class CreateParamsAuBecsDebitDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class CreateParamsApplePayLater(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsApplePayLaterDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class CreateParamsApplePayLaterDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class CreateParamsApplePay(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsApplePayDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class CreateParamsApplePayDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class CreateParamsAlipay(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsAlipayDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class CreateParamsAlipayDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class CreateParamsAfterpayClearpay(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsAfterpayClearpayDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class CreateParamsAfterpayClearpayDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class CreateParamsAffirm(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsAffirmDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class CreateParamsAffirmDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class CreateParamsAcssDebit(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.CreateParamsAcssDebitDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class CreateParamsAcssDebitDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class ListParams(RequestOptions):
            application: NotRequired["Literal['']|str|None"]
            """
            The Connect application to filter by.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

        class ModifyParams(RequestOptions):
            acss_debit: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsAcssDebit|None"
            ]
            """
            Canadian pre-authorized debit payments, check this [page](https://stripe.com/docs/payments/acss-debit) for more details like country availability.
            """
            active: NotRequired["bool|None"]
            """
            Whether the configuration can be used for new payments.
            """
            affirm: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsAffirm|None"
            ]
            """
            [Affirm](https://www.affirm.com/) gives your customers a way to split purchases over a series of payments. Depending on the purchase, they can pay with four interest-free payments (Split Pay) or pay over a longer term (Installments), which might include interest. Check this [page](https://stripe.com/docs/payments/affirm) for more details like country availability.
            """
            afterpay_clearpay: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsAfterpayClearpay|None"
            ]
            """
            Afterpay gives your customers a way to pay for purchases in installments, check this [page](https://stripe.com/docs/payments/afterpay-clearpay) for more details like country availability. Afterpay is particularly popular among businesses selling fashion, beauty, and sports products.
            """
            alipay: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsAlipay|None"
            ]
            """
            Alipay is a digital wallet in China that has more than a billion active users worldwide. Alipay users can pay on the web or on a mobile device using login credentials or their Alipay app. Alipay has a low dispute rate and reduces fraud by authenticating payments using the customer's login credentials. Check this [page](https://stripe.com/docs/payments/alipay) for more details.
            """
            apple_pay: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsApplePay|None"
            ]
            """
            Stripe users can accept [Apple Pay](https://stripe.com/payments/apple-pay) in iOS applications in iOS 9 and later, and on the web in Safari starting with iOS 10 or macOS Sierra. There are no additional fees to process Apple Pay payments, and the [pricing](https://stripe.com/pricing) is the same as other card transactions. Check this [page](https://stripe.com/docs/apple-pay) for more details.
            """
            apple_pay_later: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsApplePayLater|None"
            ]
            """
            Apple Pay Later, a payment method for customers to buy now and pay later, gives your customers a way to split purchases into four installments across six weeks.
            """
            au_becs_debit: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsAuBecsDebit|None"
            ]
            """
            Stripe users in Australia can accept Bulk Electronic Clearing System (BECS) direct debit payments from customers with an Australian bank account. Check this [page](https://stripe.com/docs/payments/au-becs-debit) for more details.
            """
            bacs_debit: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsBacsDebit|None"
            ]
            """
            Stripe users in the UK can accept Bacs Direct Debit payments from customers with a UK bank account, check this [page](https://stripe.com/docs/payments/payment-methods/bacs-debit) for more details.
            """
            bancontact: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsBancontact|None"
            ]
            """
            Bancontact is the most popular online payment method in Belgium, with over 15 million cards in circulation. [Customers](https://stripe.com/docs/api/customers) use a Bancontact card or mobile app linked to a Belgian bank account to make online payments that are secure, guaranteed, and confirmed immediately. Check this [page](https://stripe.com/docs/payments/bancontact) for more details.
            """
            blik: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsBlik|None"
            ]
            """
            BLIK is a [single use](https://stripe.com/docs/payments/payment-methods#usage) payment method that requires customers to authenticate their payments. When customers want to pay online using BLIK, they request a six-digit code from their banking application and enter it into the payment collection form. Check this [page](https://stripe.com/docs/payments/blik) for more details.
            """
            boleto: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsBoleto|None"
            ]
            """
            Boleto is an official (regulated by the Central Bank of Brazil) payment method in Brazil. Check this [page](https://stripe.com/docs/payments/boleto) for more details.
            """
            card: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsCard|None"
            ]
            """
            Cards are a popular way for consumers and businesses to pay online or in person. Stripe supports global and local card networks.
            """
            cartes_bancaires: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsCartesBancaires|None"
            ]
            """
            Cartes Bancaires is France's local card network. More than 95% of these cards are co-branded with either Visa or Mastercard, meaning you can process these cards over either Cartes Bancaires or the Visa or Mastercard networks. Check this [page](https://stripe.com/docs/payments/cartes-bancaires) for more details.
            """
            cashapp: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsCashapp|None"
            ]
            """
            Cash App is a popular consumer app in the US that allows customers to bank, invest, send, and receive money using their digital wallet. Check this [page](https://stripe.com/docs/payments/cash-app-pay) for more details.
            """
            eps: NotRequired["PaymentMethodConfiguration.ModifyParamsEps|None"]
            """
            EPS is an Austria-based payment method that allows customers to complete transactions online using their bank credentials. EPS is supported by all Austrian banks and is accepted by over 80% of Austrian online retailers. Check this [page](https://stripe.com/docs/payments/eps) for more details.
            """
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """
            fpx: NotRequired["PaymentMethodConfiguration.ModifyParamsFpx|None"]
            """
            Financial Process Exchange (FPX) is a Malaysia-based payment method that allows customers to complete transactions online using their bank credentials. Bank Negara Malaysia (BNM), the Central Bank of Malaysia, and eleven other major Malaysian financial institutions are members of the PayNet Group, which owns and operates FPX. It is one of the most popular online payment methods in Malaysia, with nearly 90 million transactions in 2018 according to BNM. Check this [page](https://stripe.com/docs/payments/fpx) for more details.
            """
            giropay: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsGiropay|None"
            ]
            """
            giropay is a German payment method based on online banking, introduced in 2006. It allows customers to complete transactions online using their online banking environment, with funds debited from their bank account. Depending on their bank, customers confirm payments on giropay using a second factor of authentication or a PIN. giropay accounts for 10% of online checkouts in Germany. Check this [page](https://stripe.com/docs/payments/giropay) for more details.
            """
            google_pay: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsGooglePay|None"
            ]
            """
            Google Pay allows customers to make payments in your app or website using any credit or debit card saved to their Google Account, including those from Google Play, YouTube, Chrome, or an Android device. Use the Google Pay API to request any credit or debit card stored in your customer's Google account. Check this [page](https://stripe.com/docs/google-pay) for more details.
            """
            grabpay: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsGrabpay|None"
            ]
            """
            GrabPay is a payment method developed by [Grab](https://www.grab.com/sg/consumer/finance/pay/). GrabPay is a digital wallet - customers maintain a balance in their wallets that they pay out with. Check this [page](https://stripe.com/docs/payments/grabpay) for more details.
            """
            ideal: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsIdeal|None"
            ]
            """
            iDEAL is a Netherlands-based payment method that allows customers to complete transactions online using their bank credentials. All major Dutch banks are members of Currence, the scheme that operates iDEAL, making it the most popular online payment method in the Netherlands with a share of online transactions close to 55%. Check this [page](https://stripe.com/docs/payments/ideal) for more details.
            """
            jcb: NotRequired["PaymentMethodConfiguration.ModifyParamsJcb|None"]
            """
            JCB is a credit card company based in Japan. JCB is currently available in Japan to businesses approved by JCB, and available to all businesses in Australia, Canada, Hong Kong, Japan, New Zealand, Singapore, Switzerland, United Kingdom, United States, and all countries in the European Economic Area except Iceland. Check this [page](https://support.stripe.com/questions/accepting-japan-credit-bureau-%28jcb%29-payments) for more details.
            """
            klarna: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsKlarna|None"
            ]
            """
            Klarna gives customers a range of [payment options](https://stripe.com/docs/payments/klarna#payment-options) during checkout. Available payment options vary depending on the customer's billing address and the transaction amount. These payment options make it convenient for customers to purchase items in all price ranges. Check this [page](https://stripe.com/docs/payments/klarna) for more details.
            """
            konbini: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsKonbini|None"
            ]
            """
            Konbini allows customers in Japan to pay for bills and online purchases at convenience stores with cash. Check this [page](https://stripe.com/docs/payments/konbini) for more details.
            """
            link: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsLink|None"
            ]
            """
            [Link](https://stripe.com/docs/payments/link) is a payment method network. With Link, users save their payment details once, then reuse that information to pay with one click for any business on the network.
            """
            name: NotRequired["str|None"]
            """
            Configuration name.
            """
            oxxo: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsOxxo|None"
            ]
            """
            OXXO is a Mexican chain of convenience stores with thousands of locations across Latin America and represents nearly 20% of online transactions in Mexico. OXXO allows customers to pay bills and online purchases in-store with cash. Check this [page](https://stripe.com/docs/payments/oxxo) for more details.
            """
            p24: NotRequired["PaymentMethodConfiguration.ModifyParamsP24|None"]
            """
            Przelewy24 is a Poland-based payment method aggregator that allows customers to complete transactions online using bank transfers and other methods. Bank transfers account for 30% of online payments in Poland and Przelewy24 provides a way for customers to pay with over 165 banks. Check this [page](https://stripe.com/docs/payments/p24) for more details.
            """
            paynow: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsPaynow|None"
            ]
            """
            PayNow is a Singapore-based payment method that allows customers to make a payment using their preferred app from participating banks and participating non-bank financial institutions. Check this [page](https://stripe.com/docs/payments/paynow) for more details.
            """
            paypal: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsPaypal|None"
            ]
            """
            PayPal, a digital wallet popular with customers in Europe, allows your customers worldwide to pay using their PayPal account. Check this [page](https://stripe.com/docs/payments/paypal) for more details.
            """
            promptpay: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsPromptpay|None"
            ]
            """
            PromptPay is a Thailand-based payment method that allows customers to make a payment using their preferred app from participating banks. Check this [page](https://stripe.com/docs/payments/promptpay) for more details.
            """
            sepa_debit: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsSepaDebit|None"
            ]
            """
            The [Single Euro Payments Area (SEPA)](https://en.wikipedia.org/wiki/Single_Euro_Payments_Area) is an initiative of the European Union to simplify payments within and across member countries. SEPA established and enforced banking standards to allow for the direct debiting of every EUR-denominated bank account within the SEPA region, check this [page](https://stripe.com/docs/payments/sepa-debit) for more details.
            """
            sofort: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsSofort|None"
            ]
            """
            Stripe users in Europe and the United States can use the [Payment Intents API](https://stripe.com/docs/payments/payment-intents)—a single integration path for creating payments using any supported method—to accept [Sofort](https://www.sofort.com/) payments from customers. Check this [page](https://stripe.com/docs/payments/sofort) for more details.
            """
            us_bank_account: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsUsBankAccount|None"
            ]
            """
            Stripe users in the United States can accept ACH direct debit payments from customers with a US bank account using the Automated Clearing House (ACH) payments system operated by Nacha. Check this [page](https://stripe.com/docs/payments/ach-debit) for more details.
            """
            wechat_pay: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsWechatPay|None"
            ]
            """
            WeChat, owned by Tencent, is China's leading mobile app with over 1 billion monthly active users. Chinese consumers can use WeChat Pay to pay for goods and services inside of businesses' apps and websites. WeChat Pay users buy most frequently in gaming, e-commerce, travel, online education, and food/nutrition. Check this [page](https://stripe.com/docs/payments/wechat-pay) for more details.
            """

        class ModifyParamsWechatPay(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsWechatPayDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class ModifyParamsWechatPayDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class ModifyParamsUsBankAccount(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsUsBankAccountDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class ModifyParamsUsBankAccountDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class ModifyParamsSofort(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsSofortDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class ModifyParamsSofortDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class ModifyParamsSepaDebit(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsSepaDebitDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class ModifyParamsSepaDebitDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class ModifyParamsPromptpay(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsPromptpayDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class ModifyParamsPromptpayDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class ModifyParamsPaypal(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsPaypalDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class ModifyParamsPaypalDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class ModifyParamsPaynow(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsPaynowDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class ModifyParamsPaynowDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class ModifyParamsP24(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsP24DisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class ModifyParamsP24DisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class ModifyParamsOxxo(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsOxxoDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class ModifyParamsOxxoDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class ModifyParamsLink(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsLinkDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class ModifyParamsLinkDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class ModifyParamsKonbini(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsKonbiniDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class ModifyParamsKonbiniDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class ModifyParamsKlarna(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsKlarnaDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class ModifyParamsKlarnaDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class ModifyParamsJcb(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsJcbDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class ModifyParamsJcbDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class ModifyParamsIdeal(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsIdealDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class ModifyParamsIdealDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class ModifyParamsGrabpay(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsGrabpayDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class ModifyParamsGrabpayDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class ModifyParamsGooglePay(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsGooglePayDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class ModifyParamsGooglePayDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class ModifyParamsGiropay(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsGiropayDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class ModifyParamsGiropayDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class ModifyParamsFpx(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsFpxDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class ModifyParamsFpxDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class ModifyParamsEps(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsEpsDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class ModifyParamsEpsDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class ModifyParamsCashapp(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsCashappDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class ModifyParamsCashappDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class ModifyParamsCartesBancaires(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsCartesBancairesDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class ModifyParamsCartesBancairesDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class ModifyParamsCard(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsCardDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class ModifyParamsCardDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class ModifyParamsBoleto(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsBoletoDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class ModifyParamsBoletoDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class ModifyParamsBlik(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsBlikDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class ModifyParamsBlikDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class ModifyParamsBancontact(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsBancontactDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class ModifyParamsBancontactDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class ModifyParamsBacsDebit(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsBacsDebitDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class ModifyParamsBacsDebitDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class ModifyParamsAuBecsDebit(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsAuBecsDebitDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class ModifyParamsAuBecsDebitDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class ModifyParamsApplePayLater(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsApplePayLaterDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class ModifyParamsApplePayLaterDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class ModifyParamsApplePay(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsApplePayDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class ModifyParamsApplePayDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class ModifyParamsAlipay(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsAlipayDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class ModifyParamsAlipayDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class ModifyParamsAfterpayClearpay(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsAfterpayClearpayDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class ModifyParamsAfterpayClearpayDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class ModifyParamsAffirm(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsAffirmDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class ModifyParamsAffirmDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class ModifyParamsAcssDebit(TypedDict):
            display_preference: NotRequired[
                "PaymentMethodConfiguration.ModifyParamsAcssDebitDisplayPreference|None"
            ]
            """
            Whether or not the payment method should be displayed.
            """

        class ModifyParamsAcssDebitDisplayPreference(TypedDict):
            preference: NotRequired["Literal['none', 'off', 'on']|None"]
            """
            The account's preference for whether or not to display this payment method.
            """

        class RetrieveParams(RequestOptions):
            expand: NotRequired["List[str]|None"]
            """
            Specifies which fields in the response should be expanded.
            """

    acss_debit: Optional[AcssDebit]
    active: bool
    """
    Whether the configuration can be used for new payments.
    """
    affirm: Optional[Affirm]
    afterpay_clearpay: Optional[AfterpayClearpay]
    alipay: Optional[Alipay]
    apple_pay: Optional[ApplePay]
    application: Optional[str]
    """
    For child configs, the Connect application associated with the configuration.
    """
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
    """
    Unique identifier for the object.
    """
    id_bank_transfer: Optional[IdBankTransfer]
    ideal: Optional[Ideal]
    is_default: bool
    """
    The default configuration is used whenever a payment method configuration is not specified.
    """
    jcb: Optional[Jcb]
    klarna: Optional[Klarna]
    konbini: Optional[Konbini]
    link: Optional[Link]
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    multibanco: Optional[Multibanco]
    name: str
    """
    The configuration's name.
    """
    netbanking: Optional[Netbanking]
    object: Literal["payment_method_configuration"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    oxxo: Optional[Oxxo]
    p24: Optional[P24]
    parent: Optional[str]
    """
    For child configs, the configuration's parent configuration.
    """
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
        **params: Unpack["PaymentMethodConfiguration.CreateParams"]
    ) -> "PaymentMethodConfiguration":
        """
        Creates a payment method configuration
        """
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
        """
        List payment method configurations
        """
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
        cls,
        id: str,
        **params: Unpack["PaymentMethodConfiguration.ModifyParams"]
    ) -> "PaymentMethodConfiguration":
        """
        Update payment method configuration
        """
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
        """
        Retrieve payment method configuration
        """
        instance = cls(id, **params)
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
