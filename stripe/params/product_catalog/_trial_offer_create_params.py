# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class TrialOfferCreateParams(RequestOptions):
    duration: "TrialOfferCreateParamsDuration"
    """
    Duration of one service period of the trial.
    """
    end_behavior: "TrialOfferCreateParamsEndBehavior"
    """
    Define behavior that occurs at the end of the trial.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    price: str
    """
    Price configuration during the trial period (amount, billing scheme, etc).
    """


class TrialOfferCreateParamsDuration(TypedDict):
    relative: NotRequired["TrialOfferCreateParamsDurationRelative"]
    """
    The relative duration of the trial period computed as the number of recurring price intervals.
    """
    type: Literal["relative", "timestamp"]
    """
    Specifies how the trial offer duration is determined.
    """


class TrialOfferCreateParamsDurationRelative(TypedDict):
    iterations: int
    """
    The number of recurring price's interval to apply for the trial period.
    """


class TrialOfferCreateParamsEndBehavior(TypedDict):
    transition: "TrialOfferCreateParamsEndBehaviorTransition"
    """
    The transition to apply when the trial offer ends.
    """


class TrialOfferCreateParamsEndBehaviorTransition(TypedDict):
    price: str
    """
    The price to transition the recurring item to when the trial offer ends.
    """
