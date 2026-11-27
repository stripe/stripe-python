# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class AccountSignalListParams(TypedDict):
    account_details: NotRequired["AccountSignalListParamsAccountDetails"]
    """
    The account or customer to list signals for. Exactly one of account_details.account or
    account_details.customer must be provided.
    """
    created: NotRequired["AccountSignalListParamsCreated"]
    """
    Filter signals by their creation timestamp before latest-per-type selection and pagination.
    """
    latest_per_type: NotRequired[bool]
    """
    Whether to return only the latest matching signal for each requested type. Defaults to true.
    Set to false to include matching historical signals.
    """
    limit: NotRequired[int]
    """
    Maximum number of results to return per page. Defaults to 10.
    """
    type: List[
        Union[
            Literal[
                "fraudulent_merchant",
                "fraudulent_website",
                "user_account_sharing",
                "user_multi_accounting",
            ],
            str,
        ]
    ]
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


class AccountSignalListParamsCreated(TypedDict):
    gt: NotRequired[str]
    """
    Only return signals created after this RFC 3339 timestamp.
    """
    gte: NotRequired[str]
    """
    Only return signals created at or after this RFC 3339 timestamp.
    """
    lt: NotRequired[str]
    """
    Only return signals created before this RFC 3339 timestamp.
    """
    lte: NotRequired[str]
    """
    Only return signals created at or before this RFC 3339 timestamp.
    """
