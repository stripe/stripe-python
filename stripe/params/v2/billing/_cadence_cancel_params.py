# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class CadenceCancelParams(TypedDict):
    include: NotRequired[
        List[Union[Literal["invoice_discount_rules", "settings_data"], str]]
    ]
    """
    Additional resource to include in the response.
    """
