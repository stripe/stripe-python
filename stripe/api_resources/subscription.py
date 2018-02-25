from __future__ import absolute_import, division, print_function

from stripe import api_requestor, util
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import DeletableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource


class Subscription(CreateableAPIResource, DeletableAPIResource,
                   UpdateableAPIResource, ListableAPIResource):
    OBJECT_NAME = 'subscription'

    def delete_discount(self, **params):
        requestor = api_requestor.APIRequestor(self.api_key,
                                               api_version=self.stripe_version,
                                               account=self.stripe_account)
        url = self.instance_url() + '/discount'
        _, api_key = requestor.request('delete', url, params)
        self.refresh_from({'discount': None}, api_key, True)

    @classmethod
    def modify(cls, sid, **params):
        if "items" in params:
            params["items"] = util.convert_array_to_dict(params["items"])
        return super(Subscription, cls).modify(sid, **params)

    @classmethod
    def create(cls, **params):
        if "items" in params:
            params["items"] = util.convert_array_to_dict(params["items"])
        return super(Subscription, cls).create(**params)

    def serialize(self, previous):
        updated_params = super(UpdateableAPIResource, self).serialize(previous)
        if "items" in updated_params:
            updated_params["items"] = util.convert_array_to_dict(
                updated_params["items"])
        return updated_params
