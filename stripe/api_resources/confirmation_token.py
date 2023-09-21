# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import APIResource
from stripe.api_resources.expandable_field import ExpandableField
from stripe.stripe_object import StripeObject
from typing import Any, Optional
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.payment_method import PaymentMethod


class ConfirmationToken(APIResource["ConfirmationToken"]):
    """
    ConfirmationTokens help transport client side data collected by Stripe JS over
    to your server for confirming a PaymentIntent or SetupIntent. If the confirmation
    is successful, values present on the ConfirmationToken are written onto the Intent.
    """

    OBJECT_NAME = "confirmation_token"
    created: int
    expires_at: Optional[int]
    id: str
    livemode: bool
    mandate_data: Optional[StripeObject]
    object: Literal["confirmation_token"]
    payment_intent: Optional[str]
    payment_method: Optional[ExpandableField["PaymentMethod"]]
    payment_method_preview: Optional[StripeObject]
    return_url: Optional[str]
    setup_future_usage: Optional[Literal["off_session", "on_session"]]
    setup_intent: Optional[str]
    shipping: Optional[StripeObject]

    @classmethod
    def retrieve(
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "ConfirmationToken":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance
