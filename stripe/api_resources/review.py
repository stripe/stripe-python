# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import ListableAPIResource


class Review(ListableAPIResource):
    OBJECT_NAME = "review"

    @classmethod
    def _cls_approve(
        cls,
        review,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "post",
            "/v1/reviews/{review}/approve".format(
                review=util.sanitize_id(review)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_approve")
    def approve(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/reviews/{review}/approve".format(
                review=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )
