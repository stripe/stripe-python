# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class CadenceListParams(TypedDict):
    include: NotRequired[
        List[Literal["invoice_discount_rules", "settings_data"]]
    ]
    """
    Additional resource to include in the response.
    """
    limit: NotRequired[int]
    """
    Optionally set the maximum number of results per page. Defaults to 20.
    """
    lookup_keys: NotRequired[List[str]]
    """
    Only return the cadences with these lookup_keys, if any exist. You can specify up to 10 lookup_keys.
    Mutually exclusive with `test_clock` and `payer`.
    """
    payer: NotRequired["CadenceListParamsPayer"]
    """
    If provided, only cadences that specifically reference the payer will be returned. Mutually exclusive with `test_clock` and `lookup_keys`.
    """
    test_clock: NotRequired[str]
    """
    If provided, only cadences that specifically reference the provided test clock ID (via the
    customer's test clock) will be returned.
    Mutually exclusive with `payer`.
    """


class CadenceListParamsPayer(TypedDict):
    customer: NotRequired[str]
    """
    The ID of the Customer object. If provided, only cadences that specifically reference the provided customer ID will be returned.
    """
    type: Literal["customer"]
    """
    A string identifying the type of the payer. Currently the only supported value is `customer`.
    """
