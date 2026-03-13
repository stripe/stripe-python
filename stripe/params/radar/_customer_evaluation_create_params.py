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
    event_type: Literal["registration"]
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
    radar_session: str
    """
    ID for the Radar Session associated with the customer evaluation.
    """


class CustomerEvaluationCreateParamsEvaluationContextCustomerDetails(
    TypedDict
):
    customer: NotRequired[str]
    """
    Stripe customer ID
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
