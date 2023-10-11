# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Any, Optional
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.customer import Customer


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
    adjusted_for_overdraft: Optional[StripeObject]
    applied_to_payment: Optional[StripeObject]
    created: int
    currency: str
    customer: ExpandableField["Customer"]
    ending_balance: int
    funded: Optional[StripeObject]
    id: str
    livemode: bool
    net_amount: int
    object: Literal["customer_cash_balance_transaction"]
    refunded_from_payment: Optional[StripeObject]
    type: Literal[
        "adjusted_for_overdraft",
        "applied_to_payment",
        "funded",
        "funding_reversed",
        "refunded_from_payment",
        "return_canceled",
        "return_initiated",
        "unapplied_from_payment",
    ]
    unapplied_from_payment: Optional[StripeObject]

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> ListObject["CustomerCashBalanceTransaction"]:
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
    def retrieve(
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "CustomerCashBalanceTransaction":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance
