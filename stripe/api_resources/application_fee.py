# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import nested_resource_class_methods


@nested_resource_class_methods(
    "refund",
    operations=["create", "retrieve", "update", "list"],
)
class ApplicationFee(ListableAPIResource):
    OBJECT_NAME = "application_fee"

    @classmethod
    def _cls_refund(
        cls,
        id,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "post",
            "/v1/application_fees/{id}/refunds".format(
                id=util.sanitize_id(id)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_refund")
    def refund(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/application_fees/{id}/refunds".format(
                id=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )
