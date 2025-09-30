# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import NotRequired, TypedDict


class PayoutMethodsBankAccountSpecRetrieveParams(TypedDict):
    countries: NotRequired[List[str]]
    """
    The countries to fetch the bank account spec for.
    """
