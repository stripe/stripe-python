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

    class AcssDebit(StripeObject):
        statement_descriptor: Optional[str]

    class BacsDebit(StripeObject):
        last4: Optional[str]

    class SepaDebit(StripeObject):
        creditor_identifier: Optional[str]
        last4: Optional[str]
        mandate_reference: Optional[str]

    acss_debit: Optional[AcssDebit]
    amount: Optional[int]
    bacs_debit: Optional[BacsDebit]
    created: int
    id: str
    livemode: bool
    object: Literal["source_mandate_notification"]
    reason: str
    sepa_debit: Optional[SepaDebit]
    source: "Source"
    status: str
    type: str

    _inner_class_types = {
        "acss_debit": AcssDebit,
        "bacs_debit": BacsDebit,
        "sepa_debit": SepaDebit,
    }
