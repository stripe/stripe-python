# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import Dict, List
from typing_extensions import Literal, NotRequired


class PlanModifyParams(RequestOptions):
    active: NotRequired[bool]
    """
    Whether the plan is currently available for new subscriptions.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    metadata: NotRequired["Literal['']|Dict[str, str]"]
    """
    Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """
    nickname: NotRequired[str]
    """
    A brief description of the plan, hidden from customers.
    """
    product: NotRequired[str]
    """
    The product the plan belongs to. This cannot be changed once it has been used in a subscription or subscription schedule.
    """
    trial_period_days: NotRequired[int]
    """
    Default number of trial days when subscribing a customer to this plan using [`trial_from_plan=true`](https://stripe.com/docs/api#create_subscription-trial_from_plan).
    """
