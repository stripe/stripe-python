# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class CreditBalanceSummaryRetrieveParams(RequestOptions):
    customer: NotRequired[str]
    """
    The customer for which to fetch credit balance summary.
    """
    customer_account: NotRequired[str]
    """
    The account for which to fetch credit balance summary.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    filter: "CreditBalanceSummaryRetrieveParamsFilter"
    """
    The filter criteria for the credit balance summary.
    """


class CreditBalanceSummaryRetrieveParamsFilter(TypedDict):
    applicability_scope: NotRequired[
        "CreditBalanceSummaryRetrieveParamsFilterApplicabilityScope"
    ]
    """
    The billing credit applicability scope for which to fetch credit balance summary.
    """
    credit_grant: NotRequired[str]
    """
    The credit grant for which to fetch credit balance summary.
    """
    type: Literal["applicability_scope", "credit_grant"]
    """
    Specify the type of this filter.
    """


class CreditBalanceSummaryRetrieveParamsFilterApplicabilityScope(TypedDict):
    billable_items: NotRequired[
        List[
            "CreditBalanceSummaryRetrieveParamsFilterApplicabilityScopeBillableItem"
        ]
    ]
    """
    A list of billable items that the credit grant can apply to. We currently only support metered billable items. Cannot be used in combination with `price_type` or `prices`.
    """
    price_type: NotRequired[Literal["metered"]]
    """
    The price type that credit grants can apply to. We currently only support the `metered` price type. Cannot be used in combination with `prices`.
    """
    prices: NotRequired[
        List["CreditBalanceSummaryRetrieveParamsFilterApplicabilityScopePrice"]
    ]
    """
    A list of prices that the credit grant can apply to. We currently only support the `metered` prices. Cannot be used in combination with `price_type`.
    """


class CreditBalanceSummaryRetrieveParamsFilterApplicabilityScopeBillableItem(
    TypedDict,
):
    id: str
    """
    The billable item ID this credit grant should apply to.
    """


class CreditBalanceSummaryRetrieveParamsFilterApplicabilityScopePrice(
    TypedDict,
):
    id: str
    """
    The price ID this credit grant should apply to.
    """
