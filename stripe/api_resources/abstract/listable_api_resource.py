from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract.api_resource import APIResource


class ListableAPIResource(APIResource):
    @classmethod
    def auto_paging_iter(cls, *args, **params):
        return cls.list(*args, **params).auto_paging_iter()  # type: ignore

    @classmethod
    def list(
        cls, api_key=None, stripe_version=None, stripe_account=None, **params
    ):
        return cls._static_request(
            "get",
            cls.class_url(),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )
