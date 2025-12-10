# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import Dict, List
from typing_extensions import Literal, NotRequired, TypedDict


class CreditUnderwritingRecordCreateFromApplicationParams(RequestOptions):
    application: (
        "CreditUnderwritingRecordCreateFromApplicationParamsApplication"
    )
    """
    Details about the application submission.
    """
    credit_user: (
        "CreditUnderwritingRecordCreateFromApplicationParamsCreditUser"
    )
    """
    Information about the company or person applying or holding the account.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    metadata: NotRequired[Dict[str, str]]
    """
    Set of [key-value pairs](https://docs.stripe.com/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
    """


class CreditUnderwritingRecordCreateFromApplicationParamsApplication(
    TypedDict
):
    application_method: NotRequired[
        Literal["in_person", "mail", "online", "phone"]
    ]
    """
    The channel through which the applicant has submitted their application. Defaults to `online`.
    """
    purpose: Literal["credit_limit_increase", "credit_line_opening"]
    """
    Scope of demand made by the applicant.
    """
    submitted_at: int
    """
    Date when the applicant submitted their application.
    """


class CreditUnderwritingRecordCreateFromApplicationParamsCreditUser(TypedDict):
    email: str
    """
    Email of the applicant or accountholder.
    """
    name: str
    """
    Full name of the company or person.
    """
