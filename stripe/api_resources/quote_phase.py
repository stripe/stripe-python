# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import ListableAPIResource


class QuotePhase(ListableAPIResource):
    """
    A quote phase describes the line items, coupons, and trialing status of a subscription for a predefined time period.
    """

    OBJECT_NAME = "quote_phase"

    @classmethod
    def _cls_list_line_items(
        cls,
        quote_phase,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "get",
            "/v1/quote_phases/{quote_phase}/line_items".format(
                quote_phase=util.sanitize_id(quote_phase)
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
            "/v1/quote_phases/{quote_phase}/line_items".format(
                quote_phase=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )
