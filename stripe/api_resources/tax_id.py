# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import APIResource
from stripe.api_resources.customer import Customer
from stripe.six.moves.urllib.parse import quote_plus


class TaxId(APIResource):
    """
    You can add one or multiple tax IDs to a [customer](https://stripe.com/docs/api/customers).
    A customer's tax IDs are displayed on invoices and credit notes issued for the customer.

    Related guide: [Customer Tax Identification Numbers](https://stripe.com/docs/billing/taxes/tax-ids).
    """

    OBJECT_NAME = "tax_id"

    def instance_url(self):
        token = util.utf8(self.id)
        customer = util.utf8(self.customer)
        base = Customer.class_url()
        cust_extn = quote_plus(customer)
        extn = quote_plus(token)
        return "%s/%s/tax_ids/%s" % (base, cust_extn, extn)

    @classmethod
    def retrieve(cls, id, api_key=None, **params):
        raise NotImplementedError(
            "Can't retrieve a tax id without a customer ID. Use customer.retrieve_tax_id('tax_id')"
        )
