# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.expandable_field import ExpandableField
from stripe.stripe_object import StripeObject
from typing import Any
from typing import List
from typing import Optional
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.application import Application
    from stripe.api_resources.account import Account
    from stripe.api_resources.payment_method import PaymentMethod
    from stripe.api_resources.setup_intent import SetupIntent


class SetupAttempt(ListableAPIResource["SetupAttempt"]):
    """
    A SetupAttempt describes one attempted confirmation of a SetupIntent,
    whether that confirmation was successful or unsuccessful. You can use
    SetupAttempts to inspect details of a specific attempt at setting up a
    payment method using a SetupIntent.
    """

    OBJECT_NAME = "setup_attempt"
    application: Optional[ExpandableField["Application"]]
    attach_to_self: bool
    created: str
    customer: Optional[ExpandableField[Any]]
    flow_directions: Optional[List[str]]
    id: str
    livemode: bool
    object: Literal["setup_attempt"]
    on_behalf_of: Optional[ExpandableField["Account"]]
    payment_method: ExpandableField["PaymentMethod"]
    payment_method_details: StripeObject
    setup_error: Optional[StripeObject]
    setup_intent: ExpandableField["SetupIntent"]
    status: str
    usage: str
