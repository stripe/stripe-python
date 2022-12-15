# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from stripe.api_resources.abstract import nested_resource_class_methods


@nested_resource_class_methods(
    "reversal",
    operations=["create", "retrieve", "update", "list"],
)
class Transfer(
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    """
    A `Transfer` object is created when you move funds between Stripe accounts as
    part of Connect.

    Before April 6, 2017, transfers also represented movement of funds from a
    Stripe account to a card or bank account. This behavior has since been split
    out into a [Payout](https://stripe.com/docs/api#payout_object) object, with corresponding payout endpoints. For more
    information, read about the
    [transfer/payout split](https://stripe.com/docs/transfer-payout-split).

    Related guide: [Creating Separate Charges and Transfers](https://stripe.com/docs/connect/charges-transfers).
    """

    OBJECT_NAME = "transfer"
