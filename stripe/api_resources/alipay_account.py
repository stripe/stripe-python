# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import DeletableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.customer import Customer
from urllib.parse import quote_plus


class AlipayAccount(DeletableAPIResource, UpdateableAPIResource):
    OBJECT_NAME = "alipay_account"

    @classmethod
    def _build_instance_url(cls, customer, sid):
        extn = quote_plus(sid)

        base = Customer.class_url()
        owner_extn = quote_plus(customer)

        return "%s/%s/sources/%s" % (base, owner_extn, extn)

    def instance_url(self):
        return self._build_instance_url(self.customer, self.id)

    @classmethod
    def modify(cls, customer, id, **params):
        url = cls._build_instance_url(customer, id)
        return cls._static_request("post", url, **params)

    @classmethod
    def retrieve(
        cls,
        id,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        raise NotImplementedError(
            "Can't retrieve an Alipay account without a customer ID. "
            "Use customer.sources.retrieve('alipay_account_id') instead."
        )
