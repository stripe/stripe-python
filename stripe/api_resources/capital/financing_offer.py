# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import ListableAPIResource
from stripe.stripe_object import StripeObject
from typing import Dict
from typing_extensions import Literal


class FinancingOffer(ListableAPIResource["FinancingOffer"]):
    """
    This is an object representing an offer of financing from
    Stripe Capital to a Connect subaccount.
    """

    OBJECT_NAME = "capital.financing_offer"
    accepted_terms: StripeObject
    account: str
    created: int
    expires_after: float
    financing_type: str
    id: str
    livemode: bool
    metadata: Dict[str, str]
    object: Literal["capital.financing_offer"]
    offered_terms: StripeObject
    product_type: str
    replacement: str
    replacement_for: str
    status: str
    type: str

    @classmethod
    def _cls_mark_delivered(
        cls,
        financing_offer,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "post",
            "/v1/capital/financing_offers/{financing_offer}/mark_delivered".format(
                financing_offer=util.sanitize_id(financing_offer)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_mark_delivered")
    def mark_delivered(self, idempotency_key=None, **params):
        return self._request(
            "post",
            "/v1/capital/financing_offers/{financing_offer}/mark_delivered".format(
                financing_offer=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )
