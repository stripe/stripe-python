# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from stripe.v2._amount import Amount
from typing import ClassVar
from typing_extensions import Literal


class CurrencyConversion(StripeObject):
    """
    The CurrencyConversion object. Contains details such as the amount debited and credited and the FinancialAccount the CurrencyConversion was performed on.
    """

    OBJECT_NAME: ClassVar[
        Literal["v2.money_management.currency_conversion"]
    ] = "v2.money_management.currency_conversion"

    class From(StripeObject):
        amount: Amount
        """
        Amount object.
        """

    class To(StripeObject):
        amount: Amount
        """
        Amount object.
        """

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
