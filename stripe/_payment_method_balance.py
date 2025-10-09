# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, Optional
from typing_extensions import Literal


class PaymentMethodBalance(StripeObject):
    """
    PaymentMethodBalance objects represent balances available on a payment method.
    You can use v1/payment_methods/:id/check_balance to check the balance of a payment method.
    """

    OBJECT_NAME: ClassVar[Literal["payment_method_balance"]] = (
        "payment_method_balance"
    )

    class Balance(StripeObject):
        class FrMealVoucher(StripeObject):
            class Available(StripeObject):
                amount: int
                """
                The amount of the balance.
                """
                currency: str
                """
                The currency of the balance.
                """

            available: Optional[List[Available]]
            """
            The hashes of balances and amounts for available balances.
            """
            _inner_class_types = {"available": Available}

        fr_meal_voucher: Optional[FrMealVoucher]
        """
        The available FR Meal Voucher balances.
        """
        _inner_class_types = {"fr_meal_voucher": FrMealVoucher}

    as_of: int
    """
    The time at which the balance was calculated. Measured in seconds since the Unix epoch.
    """
    balance: Balance
    """
    BalanceEntry contain information about every individual balance type of a card.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["payment_method_balance"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    _inner_class_types = {"balance": Balance}
