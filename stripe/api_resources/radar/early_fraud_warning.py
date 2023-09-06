# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.expandable_field import ExpandableField
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.charge import Charge
    from stripe.api_resources.payment_intent import PaymentIntent


class EarlyFraudWarning(ListableAPIResource["EarlyFraudWarning"]):
    """
    An early fraud warning indicates that the card issuer has notified us that a
    charge may be fraudulent.

    Related guide: [Early fraud warnings](https://stripe.com/docs/disputes/measuring#early-fraud-warnings)
    """

    OBJECT_NAME = "radar.early_fraud_warning"
    actionable: bool
    charge: ExpandableField["Charge"]
    created: str
    fraud_type: str
    id: str
    livemode: bool
    object: Literal["radar.early_fraud_warning"]
    payment_intent: ExpandableField["PaymentIntent"]
