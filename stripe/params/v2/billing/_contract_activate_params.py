# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class ContractActivateParams(TypedDict):
    include: NotRequired[
        List[
            Literal[
                "contract_line_details",
                "license_quantities",
                "one_time_fees",
                "pricing_lines",
                "pricing_overrides",
            ]
        ]
    ]
    """
    Additional fields to include in the response.
    """
