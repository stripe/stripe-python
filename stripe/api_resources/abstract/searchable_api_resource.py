from __future__ import absolute_import, division, print_function

from stripe import api_requestor, util
from stripe.api_resources.abstract.api_resource import APIResource


class SearchableAPIResource(APIResource):
    @classmethod
    def _search(
        cls,
        search_url,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        requestor = api_requestor.APIRequestor(
            api_key,
            api_base=cls.api_base(),
            api_version=stripe_version,
            account=stripe_account,
        )
        response, api_key = requestor.request("get", search_url, params)
        stripe_object = util.convert_to_stripe_object(
            response, api_key, stripe_version, stripe_account
        )
        stripe_object._retrieve_params = params
        return stripe_object
