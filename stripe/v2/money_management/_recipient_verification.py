# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional, Union
from typing_extensions import Literal


class RecipientVerification(StripeObject):
    """
    RecipientVerification represents a verification of recipient you intend to send funds to.
    """

    OBJECT_NAME: ClassVar[
        Literal["v2.money_management.recipient_verification"]
    ] = "v2.money_management.recipient_verification"

    class ConsumedBy(StripeObject):
        outbound_payment: Optional[str]
        """
        The ID of the OutboundPayment that consumed the RecipientVerification.
        """
        type: Union[Literal["outbound_payment"], str]
        """
        The type of resource that consumed the RecipientVerification.
        """

    class MatchResultDetails(StripeObject):
        matched_business_type: Optional[Literal["business", "personal"]]
        """
        The business type matched by the provider. Only present for Confirmation of Payee (CoP) verifications.
        """
        matched_name: Optional[str]
        """
        The account name associated with the bank account as provided by the VoP provider, only present if there is a match or close match.
        """
        message: str
        """
        A message describing the match result.
        """
        provided_business_type: Optional[Literal["business", "personal"]]
        """
        The business type provided by the user. Only present for Confirmation of Payee (CoP) verifications.
        """
        provided_name: str
        """
        The name associated with the provided recipient.
        """

    class StatusTransitions(StripeObject):
        acknowledged_at: Optional[str]
        """
        Timestamp describing when a RecipientVerification changed status to `acknowledged`.
        Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
        """
        consumed_at: Optional[str]
        """
        Timestamp describing when a RecipientVerification changed status to `consumed`.
        Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
        """

    consumed_by: Optional[ConsumedBy]
    """
    The resource that consumed this verification.
    """
    created: str
    """
    Time at which the RecipientVerification was created.
    Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    expires_at: Optional[str]
    """
    Time at which the RecipientVerification expires, 5 minutes after the creation. Only applicable for Verification of Payee (VoP) verifications.
    Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    id: str
    """
    The ID of the RecipientVerification.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    match_result: Literal["close_match", "match", "no_match", "unavailable"]
    """
    Closed Enum. Match level of the RecipientVerification: `match`, `close_match`, `no_match`, `unavailable`.
    """
    match_result_details: MatchResultDetails
    """
    Details for the match result.
    """
    object: Literal["v2.money_management.recipient_verification"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    payout_method: str
    """
    ID of the payout method that was verified.
    """
    recipient: Optional[str]
    """
    ID of the recipient account. Omitted for same-entity payouts.
    """
    status: Literal[
        "acknowledged",
        "awaiting_acknowledgement",
        "consumed",
        "expired",
        "verified",
    ]
    """
    Current status of the recipient verification.
    """
    status_transitions: Optional[StatusTransitions]
    """
    Hash containing timestamps of when the object transitioned to a particular status.
    """
    verification_type: Union[
        Literal["confirmation_of_payee", "verification_of_payee"], str
    ]
    """
    Open Enum. The type of verification performed: `verification_of_payee`, `confirmation_of_payee`.
    """
    _inner_class_types = {
        "consumed_by": ConsumedBy,
        "match_result_details": MatchResultDetails,
        "status_transitions": StatusTransitions,
    }
