# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional
from typing_extensions import Literal


class CurrencyConversion(StripeObject):
    """
    The CurrencyConversion object. Contains details such as the amount debited and credited and the FinancialAccount the CurrencyConversion was performed on.
    """

    OBJECT_NAME: ClassVar[
        Literal["v2.money_management.currency_conversion"]
    ] = "v2.money_management.currency_conversion"

    class From(StripeObject):
        class Amount(StripeObject):
            currency: Optional[str]
            """
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """
            value: Optional[int]
            """
            A non-negative integer representing how much to charge in the [smallest currency unit](https://docs.stripe.com/currencies#minor-units).
            """

        amount: Amount
        """
        Amount object.
        """
        _inner_class_types = {"amount": Amount}

    class To(StripeObject):
        class Amount(StripeObject):
            currency: Optional[str]
            """
            Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
            """
            value: Optional[int]
            """
            A non-negative integer representing how much to charge in the [smallest currency unit](https://docs.stripe.com/currencies#minor-units).
            """

        amount: Amount
        """
        Amount object.
        """
        _inner_class_types = {"amount": Amount}

    created: str
    """
    The time the CurrencyConversion was created at.
    """
    exchange_rate: str
    """
    The exchange rate used when processing the CurrencyConversion.
    """
    financial_account: str
    """
    The FinancialAccount the CurrencyConversion was performed on.
    """
    from_: From
    """
    The from block containing what was debited.
    """
    id: str
    """
    The id of the CurrencyConversion.
    """
    livemode: bool
    """
    If the CurrencyConversion was performed in livemode or not.
    """
    object: Literal["v2.money_management.currency_conversion"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    to: To
    """
    The to block containing what was credited.
    """
    _inner_class_types = {"from": From, "to": To}
    _field_remappings = {"from_": "from"}
