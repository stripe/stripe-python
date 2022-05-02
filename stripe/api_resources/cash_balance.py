# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import APIResource


class CashBalance(APIResource):
    OBJECT_NAME = "cash_balance"

    def instance_url(self):
        token = util.utf8(self.id)
        customer = util.utf8(self.customer)
        base = Customer.class_url()
        return "%s/%s/cash_balance" % (base, cust_extn)

    @classmethod
    def retrieve(cls, id, api_key=None, **params):
        raise NotImplementedError(
            "Can't retrieve a Customer Cash Balance without a Customer ID. "
            "Use Customer.retrieve_cash_balance('cus_123')"
        )
