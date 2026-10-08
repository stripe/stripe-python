# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import Union
from typing_extensions import Literal, NotRequired, TypedDict


class InboundTransferMandateCreateParams(TypedDict):
    au_becs: NotRequired["InboundTransferMandateCreateParamsAuBecs"]
    """
    Optional Australian BECS-specific parameters.
    """
    bacs: NotRequired["InboundTransferMandateCreateParamsBacs"]
    """
    Optional Bacs-specific parameters.
    """
    credential: str
    """
    The v2 credential (GB Bank Account or equivalent) this mandate is created
    for. Must belong to the authenticated compartment.
    """
    type: Union[Literal["au_becs", "bacs", "nz_becs", "sepa"], str]
    """
    The mandate scheme type.
    """
    user_accepted_details: NotRequired[
        "InboundTransferMandateCreateParamsUserAcceptedDetails"
    ]
    """
    Optional acceptance evidence collected from the merchant. Direct account calls can omit
    details that are derived from request metadata. Platform calls creating a mandate for a
    connected account must provide accepted_at, online.ip_address, and online.user_agent.
    """


class InboundTransferMandateCreateParamsAuBecs(TypedDict):
    lodgement_reference_prefix: NotRequired[str]
    """
    Optional prefix for the generated 18-character lodgement reference. The prefix is
    normalized to uppercase and must be empty or contain 1-10 letters, digits, or underscores.
    """


class InboundTransferMandateCreateParamsBacs(TypedDict):
    reference_prefix: NotRequired[str]
    """
    Optional prefix for the generated mandate reference (max 10 chars).
    """


class InboundTransferMandateCreateParamsUserAcceptedDetails(TypedDict):
    accepted_at: NotRequired[str]
    """
    When the merchant accepted the mandate. Must be a past timestamp. For direct account
    requests, defaults to the mandate's creation time when not supplied.
    """
    online: NotRequired[
        "InboundTransferMandateCreateParamsUserAcceptedDetailsOnline"
    ]
    """
    Optional details for online acceptance.
    """
    type: NotRequired[Literal["online"]]
    """
    Channel through which acceptance was obtained.
    """


class InboundTransferMandateCreateParamsUserAcceptedDetailsOnline(TypedDict):
    ip_address: NotRequired[str]
    """
    The IP address from which the merchant accepted the mandate. For direct account requests,
    derived from the request when not supplied; rejected if obtainable from neither.
    """
    user_agent: NotRequired[str]
    """
    The user agent of the browser from which the merchant accepted the mandate. For direct
    account requests, derived from the request when not supplied.
    """
