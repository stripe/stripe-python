# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import DeletableAPIResource
from stripe.api_resources.abstract import ListableAPIResource


class TestClock(
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
):
    OBJECT_NAME = "test_helpers.test_clock"

    @classmethod
    def _cls_advance(
        cls,
        test_clock,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "post",
            "/v1/test_helpers/test_clocks/{test_clock}/advance".format(
                test_clock=util.sanitize_id(test_clock)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_advance")
    def advance(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/test_helpers/test_clocks/{test_clock}/advance".format(
                test_clock=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )
