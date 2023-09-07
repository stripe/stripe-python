# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import APIResource
from stripe.api_resources.customer import Customer
from stripe.api_resources.expandable_field import ExpandableField
from typing import Dict
from typing import Optional
from typing_extensions import Literal
from urllib.parse import quote_plus

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.credit_note import CreditNote
    from stripe.api_resources.invoice import Invoice


class CustomerBalanceTransaction(APIResource["CustomerBalanceTransaction"]):
    """
    Each customer has a [Balance](https://stripe.com/docs/api/customers/object#customer_object-balance) value,
    which denotes a debit or credit that's automatically applied to their next invoice upon finalization.
    You may modify the value directly by using the [update customer API](https://stripe.com/docs/api/customers/update),
    or by creating a Customer Balance Transaction, which increments or decrements the customer's `balance` by the specified `amount`.

    Related guide: [Customer balance](https://stripe.com/docs/billing/customer/balance)
    """

    OBJECT_NAME = "customer_balance_transaction"
    amount: int
    created: str
    credit_note: Optional[ExpandableField["CreditNote"]]
    currency: str
    customer: ExpandableField["Customer"]
    description: Optional[str]
    ending_balance: int
    id: str
    invoice: Optional[ExpandableField["Invoice"]]
    livemode: bool
    metadata: Optional[Dict[str, str]]
    object: Literal["customer_balance_transaction"]
    type: str

    def instance_url(self):
        token = self.id
        customer = self.customer
        if isinstance(customer, Customer):
            customer = customer.id
        base = Customer.class_url()
        cust_extn = quote_plus(customer)
        extn = quote_plus(token)
        return "%s/%s/balance_transactions/%s" % (base, cust_extn, extn)

    @classmethod
    def retrieve(cls, id, api_key=None, **params):
        raise NotImplementedError(
            "Can't retrieve a Customer Balance Transaction without a Customer ID. "
            "Use Customer.retrieve_customer_balance_transaction('cus_123', 'cbtxn_123')"
        )
