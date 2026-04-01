# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_object import UntypedStripeObject
from typing import Dict, List
from typing_extensions import Literal, NotRequired, TypedDict


class RequestedSessionConfirmParams(RequestOptions):
    affiliate_attribution: NotRequired[
        "RequestedSessionConfirmParamsAffiliateAttribution"
    ]
    """
    Affiliate attribution data associated with this requested session.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    payment_method: NotRequired[str]
    """
    The PaymentMethod to use with the requested session.
    """
    risk_details: NotRequired["RequestedSessionConfirmParamsRiskDetails"]
    """
    Risk details/signals associated with the requested session
    """


class RequestedSessionConfirmParamsAffiliateAttribution(TypedDict):
    campaign_id: NotRequired[str]
    """
    Agent-scoped campaign identifier.
    """
    creative_id: NotRequired[str]
    """
    Agent-scoped creative identifier.
    """
    expires_at: int
    """
    Timestamp when the attribution token expires.
    """
    identification_token: str
    """
    Agent-issued secret to validate the legitimacy of the source of this data.
    """
    issued_at: int
    """
    Timestamp for when the attribution token was issued.
    """
    provider: str
    """
    Identifier for the attribution agent / affiliate network namespace.
    """
    publisher_id: NotRequired[str]
    """
    Agent-scoped affiliate/publisher identifier.
    """
    shared_metadata: NotRequired["Dict[str, str]|UntypedStripeObject[str]"]
    """
    Freeform key/value pairs for additional non-sensitive per-agent data.
    """
    source: NotRequired[
        "RequestedSessionConfirmParamsAffiliateAttributionSource"
    ]
    """
    Context about where the attribution originated.
    """
    sub_id: NotRequired[str]
    """
    Agent-scoped sub-tracking identifier.
    """
    touchpoint: Literal["first", "last"]
    """
    Whether this is the first or last touchpoint.
    """


class RequestedSessionConfirmParamsAffiliateAttributionSource(TypedDict):
    platform: NotRequired[str]
    """
    The platform where the attribution originated.
    """
    type: Literal["platform", "url"]
    """
    The type of the attribution source.
    """
    url: NotRequired[str]
    """
    The URL where the attribution originated.
    """


class RequestedSessionConfirmParamsRiskDetails(TypedDict):
    client_device_metadata_details: NotRequired[
        "RequestedSessionConfirmParamsRiskDetailsClientDeviceMetadataDetails"
    ]
    """
    The client device metadata details for this requested session.
    """


class RequestedSessionConfirmParamsRiskDetailsClientDeviceMetadataDetails(
    TypedDict,
):
    radar_session: NotRequired[str]
    """
    The radar session.
    """
    referrer: NotRequired[str]
    """
    The referrer of the client device.
    """
    remote_ip: NotRequired[str]
    """
    The remote IP address of the client device.
    """
    time_on_page_ms: NotRequired[int]
    """
    The time on page in milliseconds.
    """
    user_agent: NotRequired[str]
    """
    The user agent of the client device.
    """
