# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class CustomerTaxExemptionCreateParams(TypedDict):
    ca: NotRequired["CustomerTaxExemptionCreateParamsCa"]
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
    es: NotRequired["CustomerTaxExemptionCreateParamsEs"]
    """
    Spain-specific exemption details. Optional when country is ES; must be absent otherwise.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    expiration_date: NotRequired[str]
    """
    ISO 8601 date (YYYY-MM-DD) when the exemption expires.
    """
    reason: NotRequired[
        "Literal['direct_pay_permit', 'legacy_contract', 'other']|str"
    ]
    """
    The reason the customer is exempt. Required when `us.tax_code_group` is `saas`.
    """
    reason_details: NotRequired[
        "CustomerTaxExemptionCreateParamsReasonDetails"
    ]
    """
    Additional details about the exemption reason.
    """
    us: NotRequired["CustomerTaxExemptionCreateParamsUs"]
    """
    US-specific exemption details. Required when country is US; must be absent otherwise.
    """


class CustomerTaxExemptionCreateParamsCa(TypedDict):
    state: NotRequired[str]
    """
    Two-letter Canadian province code (ISO 3166-2). Required when tax_type is pst, qst, or rst.
    """
    tax_type: Union[Literal["gst_hst", "pst", "qst", "rst"], str]
    """
    The type of Canadian tax (gst_hst, PST, QST, RST).
    """


class CustomerTaxExemptionCreateParamsEs(TypedDict):
    state: str
    """
    Two-letter Spanish subdivision code (ISO 3166-2).
    """


class CustomerTaxExemptionCreateParamsReasonDetails(TypedDict):
    other: NotRequired["CustomerTaxExemptionCreateParamsReasonDetailsOther"]
    """
    Details for the `other` exemption reason.
    """


class CustomerTaxExemptionCreateParamsReasonDetailsOther(TypedDict):
    reason_text: str
    """
    A free-text description of the exemption reason. Maximum 5000 characters.
    """


class CustomerTaxExemptionCreateParamsUs(TypedDict):
    state: str
    """
    Two-letter US state code (ISO 3166-2).
    """
    tax_code_group: NotRequired["Literal['all', 'saas']|str"]
    """
    The group of tax codes this exemption applies to. Defaults to `all`. `saas` is only available when `state` is `CA`.
    """
