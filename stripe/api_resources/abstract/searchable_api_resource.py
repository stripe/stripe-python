from __future__ import absolute_import, division, print_function

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
        return cls._static_request(
            "get",
            search_url,
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @classmethod
    def search(cls, *args, **kwargs):
        raise NotImplementedError

    @classmethod
    def search_auto_paging_iter(cls, *args, **kwargs):
        raise NotImplementedError
