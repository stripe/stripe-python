# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import APIResourceTestHelpers
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource


class Refund(
    CreateableAPIResource, ListableAPIResource, UpdateableAPIResource
):
    """
    `Refund` objects allow you to refund a charge that has previously been created
    but not yet refunded. Funds will be refunded to the credit or debit card that
    was originally charged.

    Related guide: [Refunds](https://stripe.com/docs/refunds)
    """

    OBJECT_NAME = "refund"

    @classmethod
    def _cls_cancel(
        cls,
        refund,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "post",
            "/v1/refunds/{refund}/cancel".format(
                refund=util.sanitize_id(refund)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_cancel")
    def cancel(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/refunds/{refund}/cancel".format(
                refund=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    class TestHelpers(APIResourceTestHelpers):
        @classmethod
        def _cls_expire(
            cls,
            refund,
            api_key=None,
            stripe_version=None,
            stripe_account=None,
            **params
        ):
            return cls._static_request(
                "post",
                "/v1/test_helpers/refunds/{refund}/expire".format(
                    refund=util.sanitize_id(refund)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            )

        @util.class_method_variant("_cls_expire")
        def expire(self, idempotency_key=None, **params):
            return self.resource._request(
                "post",
                "/v1/test_helpers/refunds/{refund}/expire".format(
                    refund=util.sanitize_id(self.resource.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            )

    @property
    def test_helpers(self):
        return self.TestHelpers(self)


Refund.TestHelpers._resource_cls = Refund
