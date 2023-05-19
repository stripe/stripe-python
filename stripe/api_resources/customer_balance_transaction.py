# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import APIResource
from stripe.api_resources.customer import Customer
from stripe.six.moves.urllib.parse import quote_plus


class CustomerBalanceTransaction(APIResource):
    """
    Each customer has a [Balance](https://stripe.com/docs/api/customers/object#customer_object-balance) value,
    which denotes a debit or credit that's automatically applied to their next invoice upon finalization.
    You may modify the value directly by using the [update customer API](https://stripe.com/docs/api/customers/update),
    or by creating a Customer Balance Transaction, which increments or decrements the customer's `balance` by the specified `amount`.

    Related guide: [Customer balance](https://stripe.com/docs/billing/customer/balance)
    """

    OBJECT_NAME = "customer_balance_transaction"

    def instance_url(self):
        token = util.utf8(self.id)
        customer = util.utf8(self.customer)
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
