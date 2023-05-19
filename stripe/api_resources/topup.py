# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource


class Topup(CreateableAPIResource, ListableAPIResource, UpdateableAPIResource):
    """
    To top up your Stripe balance, you create a top-up object. You can retrieve
    individual top-ups, as well as list all top-ups. Top-ups are identified by a
    unique, random ID.

    Related guide: [Topping up your platform account](https://stripe.com/docs/connect/top-ups)
    """

    OBJECT_NAME = "topup"

    @classmethod
    def _cls_cancel(
        cls,
        topup,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "post",
            "/v1/topups/{topup}/cancel".format(topup=util.sanitize_id(topup)),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_cancel")
    def cancel(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/topups/{topup}/cancel".format(
                topup=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )
