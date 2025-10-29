# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List
from typing_extensions import NotRequired, TypedDict


class RequestedSessionConfirmParams(RequestOptions):
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
