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
    invoices: NotRequired["IntegrationConfigurationUpdateParamsInvoices"]
    """
    Configuration for standalone Invoices automatic tax behavior.
    """
    subscriptions: NotRequired[
        "IntegrationConfigurationUpdateParamsSubscriptions"
    ]
    """
    Configuration for Subscriptions automatic tax behavior.
    """


class IntegrationConfigurationUpdateParamsCheckoutSessions(TypedDict):
    automatic_tax_default_value: Literal["disabled", "enabled_when_possible"]
    """
    Controls the default value of automatic_tax[enabled] on new Checkout Sessions.
    """


class IntegrationConfigurationUpdateParamsInvoices(TypedDict):
    automatic_tax_default_value: Literal["disabled", "enabled_when_possible"]
    """
    Controls the default value of automatic_tax[enabled] on new standalone Invoices.
    """


class IntegrationConfigurationUpdateParamsSubscriptions(TypedDict):
    automatic_tax_default_value: Literal["disabled", "enabled_when_possible"]
    """
    Controls the default value of automatic_tax[enabled] on new Subscriptions.
    """
