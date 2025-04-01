# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.v2._event import Event
from typing_extensions import Literal


class V2CoreAccountRequirementsUpdatedEvent(Event):
    LOOKUP_TYPE = "v2.core.account[requirements].updated"
    type: Literal["v2.core.account[requirements].updated"]
