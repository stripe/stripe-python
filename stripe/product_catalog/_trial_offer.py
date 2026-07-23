# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._createable_api_resource import CreateableAPIResource
from stripe._expandable_field import ExpandableField
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional, Union, cast
from typing_extensions import Literal, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._price import Price
    from stripe.params.product_catalog._trial_offer_create_params import (
        TrialOfferCreateParams,
    )


class TrialOffer(CreateableAPIResource["TrialOffer"]):
    """
    Trial offers let you define free or paid introductory pricing for a subscription item.
    A TrialOffer specifies the price to charge during the trial, how long the trial lasts
    (a fixed end timestamp or a number of billing intervals), and what price the subscription
    item transitions to when the trial ends. You attach a TrialOffer to a subscription item
    using `items[current_trial][trial_offer]` when creating or updating a subscription.
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
        type: Union[Literal["relative", "timestamp"], str]
        """
        The type of trial offer duration.
        """
        _inner_class_types = {"relative": Relative}

    class EndBehavior(StripeObject):
        class Transition(StripeObject):
            price: ExpandableField["Price"]
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
    If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.
    """
    name: Optional[str]
    """
    A brief, user-friendly name for the trial offer-for identification purposes.
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
