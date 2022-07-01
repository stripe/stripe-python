from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract.api_resource import APIResource


class CreateableAPIResource(APIResource):
    @classmethod
    def create(
        cls,
        api_key=None,
        idempotency_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "post",
            cls.class_url(),
            api_key,
            idempotency_key,
            stripe_version,
            stripe_account,
            params,
        )
