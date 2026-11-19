# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import UntypedStripeObject
from stripe.v2._amount import AmountParam
from typing import Dict, Optional
from typing_extensions import Literal, NotRequired, TypedDict


class FundingIntentUpdateParams(TypedDict):
    amount: NotRequired[AmountParam]
    """
    The updated amount to add to the destination.
    """
    check: NotRequired["FundingIntentUpdateParamsCheck"]
    """
    Updated details for a check FundingIntent.
    """
    confirmation_method: NotRequired["Literal['automatic', 'manual']|str"]
    """
    The updated confirmation method.
    """
    description: NotRequired[str]
    """
    The updated description.
    """
    metadata: NotRequired[
        "Dict[str, Optional[str]]|UntypedStripeObject[Optional[str]]"
    ]
    """
    Updates to the key-value pairs attached to the FundingIntent.
    """
    settlement_timing: NotRequired["FundingIntentUpdateParamsSettlementTiming"]
    """
    The updated settlement timing. Omit to retain the existing timing.
    """


class FundingIntentUpdateParamsCheck(TypedDict):
    back_image: NotRequired[str]
    """
    The ID of a File containing the back image of the check.
    """
    front_image: NotRequired[str]
    """
    The ID of a File containing the front image of the check.
    """


class FundingIntentUpdateParamsSettlementTiming(TypedDict):
    delay_days_override: NotRequired[int]
    """
    The number of days to delay the availability of funds after processing completes.
    """
