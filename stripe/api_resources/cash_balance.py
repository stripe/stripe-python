# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.customer import Customer
from stripe.stripe_object import StripeObject
from typing import ClassVar, Dict, Optional
from typing_extensions import Literal
from urllib.parse import quote_plus


class CashBalance(StripeObject):
    """
    A customer's `Cash balance` represents real funds. Customers can add funds to their cash balance by sending a bank transfer. These funds can be used for payment and can eventually be paid out to your bank account.
    """

    OBJECT_NAME: ClassVar[Literal["cash_balance"]] = "cash_balance"
    available: Optional[Dict[str, int]]
    """
    A hash of all cash balances available to this customer. You cannot delete a customer with any cash balances, even if the balance is 0. Amounts are represented in the [smallest currency unit](https://stripe.com/docs/currencies#zero-decimal).
    """
    customer: str
    """
    The ID of the customer whose cash balance this object represents.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["cash_balance"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    settings: StripeObject

    def instance_url(self):
        customer = self.customer
        base = Customer.class_url()
        cust_extn = quote_plus(customer)
        return "%s/%s/cash_balance" % (base, cust_extn)

    @classmethod
    def retrieve(cls, id, api_key=None, **params):
        raise NotImplementedError(
            "Can't retrieve a Customer Cash Balance without a Customer ID. "
            "Use Customer.retrieve_cash_balance('cus_123')"
        )
