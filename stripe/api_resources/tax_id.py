# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import APIResource
from stripe.api_resources.customer import Customer
from stripe.api_resources.expandable_field import ExpandableField
from stripe.stripe_object import StripeObject
from typing import Optional
from typing_extensions import Literal
from urllib.parse import quote_plus


class TaxId(APIResource["TaxId"]):
    """
    You can add one or multiple tax IDs to a [customer](https://stripe.com/docs/api/customers).
    A customer's tax IDs are displayed on invoices and credit notes issued for the customer.

    Related guide: [Customer tax identification numbers](https://stripe.com/docs/billing/taxes/tax-ids)
    """

    OBJECT_NAME = "tax_id"
    country: Optional[str]
    created: str
    customer: Optional[ExpandableField["Customer"]]
    id: str
    livemode: bool
    object: Literal["tax_id"]
    type: str
    value: str
    verification: Optional[StripeObject]

    def instance_url(self):
        token = self.id
        customer = self.customer
        base = Customer.class_url()
        assert customer is not None
        if isinstance(customer, Customer):
            customer = customer.id
        cust_extn = quote_plus(customer)
        extn = quote_plus(token)
        return "%s/%s/tax_ids/%s" % (base, cust_extn, extn)

    @classmethod
    def retrieve(cls, id, api_key=None, **params):
        raise NotImplementedError(
            "Can't retrieve a tax id without a customer ID. Use customer.retrieve_tax_id('tax_id')"
        )
