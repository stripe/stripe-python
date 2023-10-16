# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.stripe_object import StripeObject
from typing import Optional
from typing_extensions import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.source import Source


class SourceMandateNotification(StripeObject):
    """
    Source mandate notifications should be created when a notification related to
    a source mandate must be sent to the payer. They will trigger a webhook or
    deliver an email to the customer.
    """

    OBJECT_NAME = "source_mandate_notification"
    acss_debit: Optional[StripeObject]
    amount: Optional[int]
    bacs_debit: Optional[StripeObject]
    created: int
    id: str
    livemode: bool
    object: Literal["source_mandate_notification"]
    reason: str
    sepa_debit: Optional[StripeObject]
    source: "Source"
    status: str
    type: str
