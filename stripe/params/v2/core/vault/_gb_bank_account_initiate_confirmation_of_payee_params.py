# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import Literal, NotRequired, TypedDict


class GbBankAccountInitiateConfirmationOfPayeeParams(TypedDict):
    business_type: NotRequired[Literal["business", "personal"]]
    """
    The business type to be checked against. Legal entity information will be used if unspecified.
    """
    name: NotRequired[str]
    """
    The name of the user to be checked against. Legal entity information will be used if unspecified.
    """
