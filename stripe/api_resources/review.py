# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.expandable_field import ExpandableField
from stripe.stripe_object import StripeObject
from typing import Optional
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.charge import Charge
    from stripe.api_resources.payment_intent import PaymentIntent


class Review(ListableAPIResource["Review"]):
    """
    Reviews can be used to supplement automated fraud detection with human expertise.

    Learn more about [Radar](https://stripe.com/radar) and reviewing payments
    [here](https://stripe.com/docs/radar/reviews).
    """

    OBJECT_NAME = "review"
    billing_zip: Optional[str]
    charge: Optional[ExpandableField["Charge"]]
    closed_reason: Optional[str]
    created: str
    id: str
    ip_address: Optional[str]
    ip_address_location: Optional[StripeObject]
    livemode: bool
    object: Literal["review"]
    open: bool
    opened_reason: str
    payment_intent: ExpandableField["PaymentIntent"]
    reason: str
    session: Optional[StripeObject]

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
