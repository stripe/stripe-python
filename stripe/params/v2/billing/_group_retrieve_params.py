# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class GroupRetrieveParams(TypedDict):
    include: NotRequired[
        List[Union[Literal["billing_settings", "invoice_discount_rules"], str]]
    ]
    """
    Additional fields to include in the response.
    """
