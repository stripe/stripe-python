# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.stripe_object import StripeObject
from typing import Dict, Optional
from typing_extensions import Literal


class Margin(StripeObject):
    """
    A (partner) margin represents a specific discount distributed in partner reseller programs to business partners who
    resell products and services and earn a discount (margin) for doing so.
    """

    OBJECT_NAME = "margin"
    active: bool
    created: int
    id: str
    livemode: bool
    metadata: Optional[Dict[str, str]]
    name: Optional[str]
    object: Literal["margin"]
    percent_off: float
    updated: int
