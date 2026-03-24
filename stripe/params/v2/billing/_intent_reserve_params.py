# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class IntentReserveParams(TypedDict):
    include: NotRequired[List[Literal["invoice_resources.preview_invoice"]]]
    """
    Select additional fields to include in the response.
    """
