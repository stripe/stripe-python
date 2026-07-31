# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class SessionCreateParams(RequestOptions):
    account_holder: "SessionCreateParamsAccountHolder"
    """
    The account holder to link accounts for.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    filters: NotRequired["SessionCreateParamsFilters"]
    """
    Filters to restrict the kinds of accounts to collect.
    """
    limits: NotRequired["SessionCreateParamsLimits"]
    """
    Settings for configuring Session-specific limits.
    """
    manual_entry: NotRequired["SessionCreateParamsManualEntry"]
    """
    Customize manual entry behavior
    """
    permissions: List[
        Literal["balances", "ownership", "payment_method", "transactions"]
    ]
    """
    List of data features that you would like to request access to.

    Possible values are `balances`, `transactions`, `ownership`, and `payment_method`.
    """
    prefetch: NotRequired[
        List[Union[Literal["balances", "ownership", "transactions"], str]]
    ]
    """
    List of data features that you would like to retrieve upon account creation.
    """
    return_url: NotRequired[str]
    """
    For webview integrations only. Upon completing OAuth login in the native browser, the user will be redirected to this URL to return to your app.
    """


class SessionCreateParamsAccountHolder(TypedDict):
    account: NotRequired[str]
    """
    The ID of the Stripe account whose accounts you will retrieve. Only available when `type` is `account`.
    """
    customer: NotRequired[str]
    """
    The ID of the Stripe customer whose accounts you will retrieve. Only available when `type` is `customer`.
    """
    customer_account: NotRequired[str]
    """
    The ID of Account representing a customer whose accounts you will retrieve. Only available when `type` is `customer`.
    """
    type: Union[Literal["account", "customer"], str]
    """
    Type of account holder to collect accounts for.
    """


class SessionCreateParamsFilters(TypedDict):
    account_subcategories: NotRequired[
        List[
            Union[
                Literal[
                    "checking",
                    "credit_card",
                    "line_of_credit",
                    "mortgage",
                    "savings",
                ],
                str,
            ]
        ]
    ]
    """
    Restricts the Session to subcategories of accounts that can be linked. Valid subcategories are: `checking`, `savings`, `mortgage`, `line_of_credit`, `credit_card`.
    """
    countries: NotRequired[List[str]]
    """
    List of countries from which to collect accounts.
    """
    require_payment_method_support: NotRequired[
        Literal["all", "at_least_one", "none"]
    ]
    """
    Whether the session should require payment method support and successful account number retrieval before completion.
    """


class SessionCreateParamsLimits(TypedDict):
    accounts: Union[Literal[""], int]
    """
    The number of accounts that can be linked in this Session. Pass an empty value to allow any number of accounts.
    """


class SessionCreateParamsManualEntry(TypedDict):
    mode: NotRequired["Literal['automatic', 'disabled']|str"]
    """
    How manual entry should be handled.
    """
