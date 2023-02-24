# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import CreateableAPIResource


class Calculation(CreateableAPIResource):
    """
    A Tax `Calculation` allows you to calculate the tax to collect from your customer.
    """

    OBJECT_NAME = "tax.calculation"

    @classmethod
    def _cls_list_line_items(
        cls,
        calculation,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "get",
            "/v1/tax/calculations/{calculation}/line_items".format(
                calculation=util.sanitize_id(calculation)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_list_line_items")
    def list_line_items(self, idempotency_key=None, **params):
        return self._request(
            "get",
            "/v1/tax/calculations/{calculation}/line_items".format(
                calculation=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )
