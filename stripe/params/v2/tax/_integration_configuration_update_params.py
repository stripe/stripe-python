# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import Literal, NotRequired, TypedDict


class IntegrationConfigurationUpdateParams(TypedDict):
    checkout_sessions: NotRequired[
        "IntegrationConfigurationUpdateParamsCheckoutSessions"
    ]
    """
    Configuration for Checkout Sessions automatic tax behavior.
    """


class IntegrationConfigurationUpdateParamsCheckoutSessions(TypedDict):
    automatic_tax_default_value: Literal["disabled", "enabled_when_possible"]
    """
    Controls the default value of automatic_tax[enabled] on new Checkout Sessions.
    """
