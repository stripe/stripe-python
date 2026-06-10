# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class CustomerEvaluationCreateParams(RequestOptions):
    evaluation_context: List["CustomerEvaluationCreateParamsEvaluationContext"]
    """
    Array of context entries for the evaluation.
    """
    event_type: Literal["login", "registration"]
    """
    The type of evaluation event.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """


class CustomerEvaluationCreateParamsEvaluationContext(TypedDict):
    client_details: NotRequired[
        "CustomerEvaluationCreateParamsEvaluationContextClientDetails"
    ]
    """
    Client details context.
    """
    customer_details: NotRequired[
        "CustomerEvaluationCreateParamsEvaluationContextCustomerDetails"
    ]
    """
    Customer details context.
    """
    type: Literal["client_details", "customer_details"]
    """
    The type of context entry.
    """


class CustomerEvaluationCreateParamsEvaluationContextClientDetails(TypedDict):
    data: NotRequired[
        "CustomerEvaluationCreateParamsEvaluationContextClientDetailsData"
    ]
    """
    Raw client metadata fallback in case a Radar Session is unavailable.
    """
    radar_session: NotRequired[str]
    """
    ID for the Radar Session. Required unless data is provided.
    """


class CustomerEvaluationCreateParamsEvaluationContextClientDetailsData(
    TypedDict,
):
    ip: str
    """
    The end user's IP address. Used for proxy detection and IP-clustering signals.
    """
    referrer: NotRequired[str]
    """
    The referring URL of the login or registration page.
    """
    user_agent: NotRequired[str]
    """
    The User-Agent HTTP header.
    """


class CustomerEvaluationCreateParamsEvaluationContextCustomerDetails(
    TypedDict
):
    customer: NotRequired[str]
    """
    The ID of an existing Customer.
    """
    customer_data: NotRequired[
        "CustomerEvaluationCreateParamsEvaluationContextCustomerDetailsCustomerData"
    ]
    """
    Customer data
    """


class CustomerEvaluationCreateParamsEvaluationContextCustomerDetailsCustomerData(
    TypedDict,
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
