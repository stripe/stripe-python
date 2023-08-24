# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.stripe_object import StripeObject
from typing import Any
from typing_extensions import Literal


class SourceTransaction(StripeObject):
    """
    Some payment methods have no required amount that a customer must send.
    Customers can be instructed to send any amount, and it can be made up of
    multiple transactions. As such, sources can have multiple associated
    transactions.
    """

    OBJECT_NAME = "source_transaction"
    ach_credit_transfer: Any
    amount: int
    chf_credit_transfer: Any
    created: str
    currency: str
    gbp_credit_transfer: Any
    id: str
    livemode: bool
    object: Literal["source_transaction"]
    paper_check: Any
    sepa_credit_transfer: Any
    source: str
    status: str
    type: str
