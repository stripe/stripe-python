# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import NotRequired, TypedDict


class UsBankAccountConfirmMicrodepositsParams(TypedDict):
    amounts: NotRequired[List[int]]
    """
    Two amounts received through Send Microdeposits must match the input to Confirm Microdeposits to verify US Bank Account.
    """
    descriptor_code: NotRequired[str]
    """
    Descriptor code received through Send Microdeposits must match the input to Confirm Microdeposits to verify US Bank Account.
    """
