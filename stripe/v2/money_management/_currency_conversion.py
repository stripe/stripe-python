# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from stripe.v2._amount import Amount
from typing import ClassVar, Optional
from typing_extensions import Literal


class CurrencyConversion(StripeObject):
    """
    A Currency Conversion represents a standalone conversion between currencies in a [Financial Account](https://docs.stripe.com/api/v2/money-management/financial-accounts) or the payments balance.
    """

    OBJECT_NAME: ClassVar[
        Literal["v2.money_management.currency_conversion"]
    ] = "v2.money_management.currency_conversion"

    class From(StripeObject):
        amount: Amount
        """
        A specific amount.
        """

    class To(StripeObject):
        amount: Amount
        """
        A specific amount.
        """

    created: str
    """
    The time the Currency Conversion was created at.
    """
    exchange_rate: str
    """
    The exchange rate used, excluding applicable fees.
    """
    financial_account: Optional[str]
    """
    The ID of the Financial Account the Currency Conversion was created in. If `null`, it was created in the payments balance.
    """
    from_: From
    """
    The amount that was debited from the source currency.
    """
    id: str
    """
    The ID of the Currency Conversion.
    """
    livemode: bool
    """
    If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.
    """
    object: Literal["v2.money_management.currency_conversion"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    to: To
    """
    The amount that was credited to the destination currency.
    """
    _inner_class_types = {"from": From, "to": To}
    _field_remappings = {"from_": "from"}
