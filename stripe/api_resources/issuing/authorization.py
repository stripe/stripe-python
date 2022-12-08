# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource


class Authorization(ListableAPIResource, UpdateableAPIResource):
    """
    When an [issued card](https://stripe.com/docs/issuing) is used to make a purchase, an Issuing `Authorization`
    object is created. [Authorizations](https://stripe.com/docs/issuing/purchases/authorizations) must be approved for the
    purchase to be completed successfully.

    Related guide: [Issued Card Authorizations](https://stripe.com/docs/issuing/purchases/authorizations).
    """

    OBJECT_NAME = "issuing.authorization"

    @classmethod
    def _cls_approve(
        cls,
        authorization,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "post",
            "/v1/issuing/authorizations/{authorization}/approve".format(
                authorization=util.sanitize_id(authorization)
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
            "/v1/issuing/authorizations/{authorization}/approve".format(
                authorization=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def _cls_decline(
        cls,
        authorization,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "post",
            "/v1/issuing/authorizations/{authorization}/decline".format(
                authorization=util.sanitize_id(authorization)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_decline")
    def decline(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/issuing/authorizations/{authorization}/decline".format(
                authorization=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )
