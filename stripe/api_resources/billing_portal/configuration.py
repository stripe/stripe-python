# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import (
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
)
from stripe.api_resources.expandable_field import ExpandableField
from stripe.stripe_object import StripeObject
from typing import Any, Dict, Optional
from typing_extensions import Literal


class Configuration(
    CreateableAPIResource["Configuration"],
    ListableAPIResource["Configuration"],
    UpdateableAPIResource["Configuration"],
):
    """
    A portal configuration describes the functionality and behavior of a portal session.
    """

    OBJECT_NAME = "billing_portal.configuration"
    active: bool
    application: Optional[ExpandableField[Any]]
    business_profile: StripeObject
    created: str
    default_return_url: Optional[str]
    features: StripeObject
    id: str
    is_default: bool
    livemode: bool
    login_page: StripeObject
    metadata: Optional[Dict[str, str]]
    object: Literal["billing_portal.configuration"]
    updated: str
