# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._createable_api_resource import CreateableAPIResource
from stripe._expandable_field import ExpandableField
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional, cast
from typing_extensions import Literal, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._price import Price
    from stripe.params.product_catalog._trial_offer_create_params import (
        TrialOfferCreateParams,
    )


class TrialOffer(CreateableAPIResource["TrialOffer"]):
    """
    Resource for the TrialOffer API, used to describe a subscription item's trial period settings.
    Renders a TrialOffer object that describes the price, duration, end_behavior of a trial offer.
    """

    OBJECT_NAME: ClassVar[Literal["product_catalog.trial_offer"]] = (
        "product_catalog.trial_offer"
    )

    class Duration(StripeObject):
        class Relative(StripeObject):
            iterations: int
            """
            The number of iterations of the price's interval for this trial offer.
            """

        relative: Optional[Relative]
        type: Literal["relative", "timestamp"]
        """
        The type of trial offer duration.
        """
        _inner_class_types = {"relative": Relative}

    class EndBehavior(StripeObject):
        class Transition(StripeObject):
            price: str
            """
            The new price to use at the end of the trial offer period.
            """

        transition: Transition
        type: Literal["transition"]
        """
        The type of behavior when the trial offer ends.
        """
        _inner_class_types = {"transition": Transition}

    duration: Duration
    end_behavior: EndBehavior
    id: str
    """
    Unique identifier for the object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["product_catalog.trial_offer"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    price: ExpandableField["Price"]
    """
    The price during the trial offer.
    """

    @classmethod
    def create(
        cls, **params: Unpack["TrialOfferCreateParams"]
    ) -> "TrialOffer":
        """
        Creates a trial offer.
        """
        return cast(
            "TrialOffer",
            cls._static_request(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    async def create_async(
        cls, **params: Unpack["TrialOfferCreateParams"]
    ) -> "TrialOffer":
        """
        Creates a trial offer.
        """
        return cast(
            "TrialOffer",
            await cls._static_request_async(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    _inner_class_types = {"duration": Duration, "end_behavior": EndBehavior}
