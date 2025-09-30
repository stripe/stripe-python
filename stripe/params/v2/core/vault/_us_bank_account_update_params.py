# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import NotRequired, TypedDict


class UsBankAccountUpdateParams(TypedDict):
    fedwire_routing_number: NotRequired[str]
    """
    The bank account's fedwire routing number can be provided for update it was were empty previously.
    """
    routing_number: NotRequired[str]
    """
    The bank account's ACH routing number can be provided for update if it was empty previously.
    """
