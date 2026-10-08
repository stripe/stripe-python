# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional, Union
from typing_extensions import Literal


class InboundTransferMandate(StripeObject):
    """
    An InboundTransferMandate represents Stripe's authorization to debit a
    merchant's external bank account (v2 credential) on their behalf.
    """

    OBJECT_NAME: ClassVar[
        Literal["v2.money_management.inbound_transfer_mandate"]
    ] = "v2.money_management.inbound_transfer_mandate"

    class AuBecs(StripeObject):
        lodgement_reference: str
        """
        The generated AU BECS lodgement reference. It is 18 uppercase alphanumeric or underscore
        characters and incorporates lodgement_reference_prefix when one was supplied at creation.
        """

    class Bacs(StripeObject):
        reference: str
        """
        The generated Bacs mandate reference. May incorporate the optional
        reference_prefix supplied at creation time.
        """

    class StatusDetails(StripeObject):
        class Canceled(StripeObject):
            reason: Literal[
                "canceled_by_network",
                "canceled_by_user",
                "refused_by_network",
                "revoked_by_stripe",
            ]
            """
            The reason the mandate was canceled.
            """

        canceled: Optional[Canceled]
        """
        Present when the mandate is in the CANCELED state.
        """
        _inner_class_types = {"canceled": Canceled}

    class StatusTransitions(StripeObject):
        activated_at: Optional[str]
        """
        When the mandate became active.
        """
        canceled_at: Optional[str]
        """
        When the mandate was canceled.
        """
        expired_at: Optional[str]
        """
        When the mandate expired.
        """

    class UserAcceptedDetails(StripeObject):
        class Online(StripeObject):
            ip_address: Optional[str]
            """
            The IP address from which the merchant accepted the mandate. For direct account requests,
            derived from the request when not supplied; rejected if obtainable from neither.
            """
            user_agent: Optional[str]
            """
            The user agent of the browser from which the merchant accepted the mandate. For direct
            account requests, derived from the request when not supplied.
            """

        accepted_at: Optional[str]
        """
        When the merchant accepted the mandate. Must be a past timestamp. For direct account
        requests, defaults to the mandate's creation time when not supplied.
        """
        online: Optional[Online]
        """
        Optional details for online acceptance.
        """
        type: Optional[Literal["online"]]
        """
        Channel through which acceptance was obtained.
        """
        _inner_class_types = {"online": Online}

    au_becs: Optional[AuBecs]
    """
    Australian BECS-specific details. Present when type is AU_BECS.
    """
    bacs: Optional[Bacs]
    """
    Bacs-specific details. Present when type is BACS.
    """
    created: str
    """
    Creation time of the mandate. RFC 3339 UTC, millisecond precision.
    """
    credential: str
    """
    The v2 credential (e.g. GB Bank Account) this mandate authorizes debits for.
    """
    id: str
    """
    Unique identifier for the InboundTransferMandate.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.money_management.inbound_transfer_mandate"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    status: Literal["active", "canceled", "expired", "pending"]
    """
    The current lifecycle status of the mandate.
    """
    status_details: StatusDetails
    """
    Additional details about the current status (e.g. cancelation reason).
    """
    status_transitions: StatusTransitions
    """
    Timestamps for each state transition.
    """
    type: Union[Literal["au_becs", "bacs", "nz_becs", "sepa"], str]
    """
    The mandate scheme type.
    """
    user_accepted_details: UserAcceptedDetails
    """
    Evidence of the merchant's acceptance of the mandate.
    """
    _inner_class_types = {
        "au_becs": AuBecs,
        "bacs": Bacs,
        "status_details": StatusDetails,
        "status_transitions": StatusTransitions,
        "user_accepted_details": UserAcceptedDetails,
    }
