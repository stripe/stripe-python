# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar
from typing_extensions import Literal


class IntegrationConfiguration(StripeObject):
    """
    Per-account configuration controlling implicit behavior of Stripe Tax
    across supported integration surfaces.
    """

    OBJECT_NAME: ClassVar[Literal["v2.tax.integration_configuration"]] = (
        "v2.tax.integration_configuration"
    )

    class CheckoutSessions(StripeObject):
        automatic_tax_default_value: Literal[
            "disabled", "enabled_when_possible"
        ]
        """
        Controls the default value of automatic_tax[enabled] on new Checkout Sessions.
        """

    checkout_sessions: CheckoutSessions
    """
    Configuration for Checkout Sessions automatic tax behavior.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.tax.integration_configuration"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    _inner_class_types = {"checkout_sessions": CheckoutSessions}
