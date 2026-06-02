# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class AccountSignalListParams(TypedDict):
    account_details: NotRequired["AccountSignalListParamsAccountDetails"]
    """
    The account or customer to list signals for. Exactly one of account_details.account or
    account_details.customer must be provided.
    """
    limit: NotRequired[int]
    """
    Maximum number of results to return per page. Defaults to 20.
    """
    type: List[Literal["fraudulent_merchant", "merchant_delinquency"]]
    """
    Signal types to filter by.
    """


class AccountSignalListParamsAccountDetails(TypedDict):
    account: NotRequired[str]
    """
    The v2 account ID of the account.
    """
    customer: NotRequired[str]
    """
    The v1 customer ID of the account, for users not yet migrated to v2/accounts.
    """
