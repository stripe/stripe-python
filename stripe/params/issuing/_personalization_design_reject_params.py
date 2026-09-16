# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class PersonalizationDesignRejectParams(RequestOptions):
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    rejection_reasons: "PersonalizationDesignRejectParamsRejectionReasons"
    """
    The reason(s) the personalization design was rejected.
    """


class PersonalizationDesignRejectParamsRejectionReasons(TypedDict):
    card_logo: NotRequired[
        List[
            Union[
                Literal[
                    "geographic_location",
                    "inappropriate",
                    "network_name",
                    "non_binary_image",
                    "non_fiat_currency",
                    "other",
                    "other_entity",
                    "promotional_material",
                ],
                str,
            ]
        ]
    ]
    """
    The reason(s) the card logo was rejected.
    """
    carrier_text: NotRequired[
        List[
            Union[
                Literal[
                    "geographic_location",
                    "inappropriate",
                    "network_name",
                    "non_fiat_currency",
                    "other",
                    "other_entity",
                    "promotional_material",
                ],
                str,
            ]
        ]
    ]
    """
    The reason(s) the carrier text was rejected.
    """
