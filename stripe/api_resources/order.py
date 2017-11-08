from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource


class Order(CreateableAPIResource, UpdateableAPIResource,
            ListableAPIResource):
    OBJECT_NAME = 'order'

    @classmethod
    def create(cls, **params):
        if "items" in params:
            params["items"] = util.convert_array_to_dict(params["items"])
        return super(Order, cls).create(**params)

    def pay(self, idempotency_key=None, **params):
        url = self.instance_url() + '/pay'
        headers = util.populate_headers(idempotency_key)
        self.refresh_from(self.request('post', url, params, headers))
        return self

    def return_order(self, idempotency_key=None, **params):
        if "items" in params:
            params["items"] = util.convert_array_to_dict(params["items"])
        headers = util.populate_headers(idempotency_key)
        return self.request(
            'post', self.instance_url() + '/returns', params, headers)
