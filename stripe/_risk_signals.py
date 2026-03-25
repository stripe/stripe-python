# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar
from typing_extensions import Literal


class RiskSignals(StripeObject):
    OBJECT_NAME: ClassVar[Literal["risk_signals"]] = "risk_signals"
    object: Literal["risk_signals"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    session_metadata: bool
    """
    Represents the status of risk signal session metadata collection. When false, the account has payouts and payments disabled.
    """
