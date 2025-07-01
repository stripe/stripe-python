# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional
from typing_extensions import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.v2.money_management._payout_method import PayoutMethod


class OutboundSetupIntent(StripeObject):
    """
    Use the OutboundSetupIntent API to create and setup usable payout methods.
    """

    OBJECT_NAME: ClassVar[
        Literal["v2.money_management.outbound_setup_intent"]
    ] = "v2.money_management.outbound_setup_intent"

    class NextAction(StripeObject):
        class ConfirmationOfPayee(StripeObject):
            object: str
            """
            The type of the credential.
            """
            status: Literal[
                "awaiting_acknowledgement", "confirmed", "uninitiated"
            ]
            """
            The Confirmation of Payee status.
            """

        confirmation_of_payee: Optional[ConfirmationOfPayee]
        """
        Confirmation of Payee details.
        """
        type: Literal["confirmation_of_payee"]
        """
        The type of next action.
        """
        _inner_class_types = {"confirmation_of_payee": ConfirmationOfPayee}

    created: str
    """
    Created timestamp.
    """
    id: str
    """
    ID of the outbound setup intent.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    next_action: Optional[NextAction]
    """
    Specifies which actions needs to be taken next to continue setup of the credential.
    """
    object: Literal["v2.money_management.outbound_setup_intent"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    payout_method: "PayoutMethod"
    """
    Information about the payout method that's created and linked to this outbound setup intent.
    """
    status: Literal[
        "canceled", "requires_action", "requires_payout_method", "succeeded"
    ]
    """
    Closed Enum. Status of the outbound setup intent.
    """
    usage_intent: Literal["payment", "transfer"]
    """
    The intended money movement flow this payout method should be set up for, specified in params.
    """
    _inner_class_types = {"next_action": NextAction}
