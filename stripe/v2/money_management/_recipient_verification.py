# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional
from typing_extensions import Literal


class RecipientVerification(StripeObject):
    """
    RecipientVerification represents a verification of recipient you intend to send funds to.
    """

    OBJECT_NAME: ClassVar[
        Literal["v2.money_management.recipient_verification"]
    ] = "v2.money_management.recipient_verification"

    class MatchResultDetails(StripeObject):
        matched_name: Optional[str]
        """
        The account name associated with the bank account as provided by the VoP provider, only present if there is a match or close match.
        """
        message: str
        """
        A message describing the match result.
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

    consumed_by: Optional[str]
    """
    The OBP/OBT ID that consumed this verification, present if one is successfully created.
    """
    created: str
    """
    Time at which the RecipientVerification was created.
    Represented as a RFC 3339 date & time UTC value in millisecond precision, for example: 2022-09-18T13:22:18.123Z.
    """
    expires_at: str
    """
    Time at which the RecipientVerification expires, 5 minutes after the creation.
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
    status: Literal[
        "acknowledged",
        "awaiting_acknowledgement",
        "consumed",
        "expired",
        "verified",
    ]
    """
    Closed Enum. Current status of the RecipientVerification: `verified`, `consumed`, `expired`, `awaiting_acknowledgement`, `acknowledged`.
    """
    status_transitions: Optional[StatusTransitions]
    """
    Hash containing timestamps of when the object transitioned to a particular status.
    """
    _inner_class_types = {
        "match_result_details": MatchResultDetails,
        "status_transitions": StatusTransitions,
    }
