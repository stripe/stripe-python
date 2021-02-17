# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.customer import Customer
from urllib.parse import quote_plus


class BitcoinReceiver(ListableAPIResource):
    OBJECT_NAME = "bitcoin_receiver"

    def instance_url(self):
        extn = quote_plus(self.id)

        if hasattr(self, "customer"):
            base = Customer.class_url()
            cust_extn = quote_plus(self.customer)
            return "%s/%s/sources/%s" % (base, cust_extn, extn)
        else:
            base = BitcoinReceiver.class_url()
            return "%s/%s" % (base, extn)

    @classmethod
    def class_url(cls):
        return "/v1/bitcoin/receivers"
