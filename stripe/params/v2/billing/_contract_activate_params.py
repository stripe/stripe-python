# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class ContractActivateParams(TypedDict):
    include: NotRequired[
        List[
            Union[
                Literal[
                    "billing_settings", "pricing_lines", "pricing_overrides"
                ],
                str,
            ]
        ]
    ]
    """
    Additional fields to include in the response.
    """
