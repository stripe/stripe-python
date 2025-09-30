# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import Dict
from typing_extensions import NotRequired, TypedDict


class RateCardSubscriptionCreateParams(TypedDict):
    billing_cadence: str
    """
    The ID of the Billing Cadence.
    """
    metadata: NotRequired[Dict[str, str]]
    """
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    rate_card: str
    """
    The ID of the Rate Card.
    """
    rate_card_version: NotRequired[str]
    """
    The ID of the Rate Card Version. If not specified, defaults to the "live_version" of the Rate Card at the time of creation.
    """
