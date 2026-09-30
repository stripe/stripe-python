# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List, Union
from typing_extensions import Literal, NotRequired, TypedDict


class CadenceRetrieveParams(TypedDict):
    include: NotRequired[List[Union[Literal["settings_data"], str]]]
    """
    Additional resource to include in the response.
    """
