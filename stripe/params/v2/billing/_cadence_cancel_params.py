# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class CadenceCancelParams(TypedDict):
    include: NotRequired[
        List[Literal["invoice_discount_rules", "settings_data"]]
    ]
    """
    Additional resource to include in the response.
    """
