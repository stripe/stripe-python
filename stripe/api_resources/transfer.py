# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.abstract import nested_resource_class_methods
from typing import Any
from typing import Dict
from typing import Optional
from typing_extensions import Literal


@nested_resource_class_methods(
    "reversal",
    operations=["create", "retrieve", "update", "list"],
)
class Transfer(
    CreateableAPIResource["Transfer"],
    ListableAPIResource["Transfer"],
    UpdateableAPIResource["Transfer"],
):
    """
    A `Transfer` object is created when you move funds between Stripe accounts as
    part of Connect.

    Before April 6, 2017, transfers also represented movement of funds from a
    Stripe account to a card or bank account. This behavior has since been split
    out into a [Payout](https://stripe.com/docs/api#payout_object) object, with corresponding payout endpoints. For more
    information, read about the
    [transfer/payout split](https://stripe.com/docs/transfer-payout-split).

    Related guide: [Creating separate charges and transfers](https://stripe.com/docs/connect/separate-charges-and-transfers)
    """

    OBJECT_NAME = "transfer"
    amount: int
    amount_reversed: int
    balance_transaction: Optional[Any]
    created: str
    currency: str
    description: Optional[str]
    destination: Optional[Any]
    destination_payment: Any
    id: str
    livemode: bool
    metadata: Dict[str, str]
    object: Literal["transfer"]
    reversals: Any
    reversed: bool
    source_transaction: Optional[Any]
    source_type: str
    transfer_group: Optional[str]
