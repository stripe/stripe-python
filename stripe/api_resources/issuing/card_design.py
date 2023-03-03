# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import APIResourceTestHelpers
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.abstract import test_helpers


@test_helpers
class CardDesign(ListableAPIResource, UpdateableAPIResource):
    """
    A Card Design is a logical grouping of a Card Bundle, card logo, and carrier text that represents a product line.
    """

    OBJECT_NAME = "issuing.card_design"

    class TestHelpers(APIResourceTestHelpers):
        @classmethod
        def _cls_activate_testmode(
            cls,
            card_design,
            api_key=None,
            stripe_version=None,
            stripe_account=None,
            **params
        ):
            return cls._static_request(
                "post",
                "/v1/test_helpers/issuing/card_designs/{card_design}/status/activate".format(
                    card_design=util.sanitize_id(card_design)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            )

        @util.class_method_variant("_cls_activate_testmode")
        def activate_testmode(self, idempotency_key=None, **params):
            return self.resource._request(
                "post",
                "/v1/test_helpers/issuing/card_designs/{card_design}/status/activate".format(
                    card_design=util.sanitize_id(self.resource.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            )

        @classmethod
        def _cls_deactivate_testmode(
            cls,
            card_design,
            api_key=None,
            stripe_version=None,
            stripe_account=None,
            **params
        ):
            return cls._static_request(
                "post",
                "/v1/test_helpers/issuing/card_designs/{card_design}/status/deactivate".format(
                    card_design=util.sanitize_id(card_design)
                ),
                api_key=api_key,
                stripe_version=stripe_version,
                stripe_account=stripe_account,
                params=params,
            )

        @util.class_method_variant("_cls_deactivate_testmode")
        def deactivate_testmode(self, idempotency_key=None, **params):
            return self.resource._request(
                "post",
                "/v1/test_helpers/issuing/card_designs/{card_design}/status/deactivate".format(
                    card_design=util.sanitize_id(self.resource.get("id"))
                ),
                idempotency_key=idempotency_key,
                params=params,
            )
