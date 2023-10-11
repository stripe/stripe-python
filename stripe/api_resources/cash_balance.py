# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.api_resources.customer import Customer
from stripe.stripe_object import StripeObject
from typing import Dict, Optional
from typing_extensions import Literal
from urllib.parse import quote_plus


class CashBalance(StripeObject):
    """
    A customer's `Cash balance` represents real funds. Customers can add funds to their cash balance by sending a bank transfer. These funds can be used for payment and can eventually be paid out to your bank account.
    """

    OBJECT_NAME = "cash_balance"
    available: Optional[Dict[str, int]]
    customer: str
    livemode: bool
    object: Literal["cash_balance"]
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
