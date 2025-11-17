# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class AccountEvaluationCreateParams(RequestOptions):
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    login_initiated: NotRequired["AccountEvaluationCreateParamsLoginInitiated"]
    """
    Event payload for login_initiated.
    """
    registration_initiated: NotRequired[
        "AccountEvaluationCreateParamsRegistrationInitiated"
    ]
    """
    Event payload for registration_initiated.
    """
    type: Literal["login_initiated", "registration_initiated"]
    """
    The type of evaluation requested.
    """


class AccountEvaluationCreateParamsLoginInitiated(TypedDict):
    client_device_metadata_details: "AccountEvaluationCreateParamsLoginInitiatedClientDeviceMetadataDetails"
    """
    Client device metadata details (e.g., radar_session).
    """
    customer: str
    """
    Stripe customer ID
    """


class AccountEvaluationCreateParamsLoginInitiatedClientDeviceMetadataDetails(
    TypedDict,
):
    radar_session: str
    """
    ID for the Radar Session associated with the account evaluation.
    """


class AccountEvaluationCreateParamsRegistrationInitiated(TypedDict):
    client_device_metadata_details: "AccountEvaluationCreateParamsRegistrationInitiatedClientDeviceMetadataDetails"
    """
    Client device metadata details (e.g., radar_session).
    """
    customer: NotRequired[str]
    """
    Stripe customer ID
    """
    customer_data: NotRequired[
        "AccountEvaluationCreateParamsRegistrationInitiatedCustomerData"
    ]
    """
    Customer data
    """


class AccountEvaluationCreateParamsRegistrationInitiatedClientDeviceMetadataDetails(
    TypedDict,
):
    radar_session: str
    """
    ID for the Radar Session associated with the account evaluation.
    """


class AccountEvaluationCreateParamsRegistrationInitiatedCustomerData(
    TypedDict
):
    email: NotRequired[str]
    """
    Customer email
    """
    name: NotRequired[str]
    """
    Customer name
    """
    phone: NotRequired[str]
    """
    Customer phone
    """
