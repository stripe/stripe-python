# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import ListableAPIResource
from stripe.stripe_object import StripeObject
from typing import Any
from typing_extensions import Literal


class CustomerCashBalanceTransaction(
    ListableAPIResource["CustomerCashBalanceTransaction"],
):
    """
    Customers with certain payments enabled have a cash balance, representing funds that were paid
    by the customer to a merchant, but have not yet been allocated to a payment. Cash Balance Transactions
    represent when funds are moved into or out of this balance. This includes funding by the customer, allocation
    to payments, and refunds to the customer.
    """

    OBJECT_NAME = "customer_cash_balance_transaction"
    adjusted_for_overdraft: StripeObject
    applied_to_payment: StripeObject
    created: str
    currency: str
    customer: Any
    ending_balance: int
    funded: StripeObject
    id: str
    livemode: bool
    net_amount: int
    object: Literal["customer_cash_balance_transaction"]
    refunded_from_payment: StripeObject
    type: str
    unapplied_from_payment: StripeObject
