# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class CustomerCreateTaxExemptionParams(RequestOptions):
    ca: NotRequired["CustomerCreateTaxExemptionParamsCa"]
    """
    Canada-specific exemption details. Required when country is CA; must be absent otherwise.
    """
    country: str
    """
    Two-letter ISO country code for the exemption location.
    """
    effective_date: str
    """
    ISO 8601 date (YYYY-MM-DD) when the exemption becomes effective. Must be no more than one year after today's UTC date (inclusive).
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    expiration_date: NotRequired[str]
    """
    ISO 8601 date (YYYY-MM-DD) when the exemption expires.
    """
    us: NotRequired["CustomerCreateTaxExemptionParamsUs"]
    """
    US-specific exemption details. Required when country is US; must be absent otherwise.
    """


class CustomerCreateTaxExemptionParamsCa(TypedDict):
    state: NotRequired[str]
    """
    Two-letter Canadian province code (ISO 3166-2). Required when tax_type is pst, qst, or rst.
    """
    tax_type: Union[Literal["gst_hst", "pst", "qst", "rst"], str]
    """
    The type of Canadian tax (gst_hst, PST, QST, RST).
    """


class CustomerCreateTaxExemptionParamsUs(TypedDict):
    state: str
    """
    Two-letter US state code (ISO 3166-2).
    """
