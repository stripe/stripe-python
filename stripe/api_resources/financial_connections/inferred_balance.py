# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import ListableAPIResource
from typing import Dict
from typing_extensions import Literal


class InferredBalance(ListableAPIResource["InferredBalance"]):
    """
    A historical balance for the account on a particular day. It may be sourced from a balance snapshot provided by a financial institution, or inferred using transactions data.
    """

    OBJECT_NAME = "financial_connections.account_inferred_balance"
    as_of: str
    current: Dict[str, int]
    id: str
    object: Literal["financial_connections.account_inferred_balance"]
