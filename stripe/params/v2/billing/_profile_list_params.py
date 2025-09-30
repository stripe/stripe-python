# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class ProfileListParams(TypedDict):
    customer: NotRequired[str]
    """
    Filter billing profiles by a customer. Mutually exclusive
    with `lookup_keys` and `default_payment_method`.
    """
    default_payment_method: NotRequired[str]
    """
    Filter billing profiles by a default payment method. Mutually exclusive
    with `customer` and `lookup_keys`.
    """
    limit: NotRequired[int]
    """
    Optionally set the maximum number of results per page. Defaults to 10.
    """
    lookup_keys: List[str]
    """
    Filter billing profiles by lookup keys. Mutually exclusive
    with `customer` and `default_payment_method`.
    You can specify up to 10 lookup_keys.
    """
    status: NotRequired[Literal["active", "inactive"]]
    """
    Filter billing profiles by status. Can be combined
    with all other filters. If not provided, all billing profiles will be returned.
    """
