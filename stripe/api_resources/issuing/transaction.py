# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource


class Transaction(ListableAPIResource, UpdateableAPIResource):
    """
    Any use of an [issued card](https://stripe.com/docs/issuing) that results in funds entering or leaving
    your Stripe account, such as a completed purchase or refund, is represented by an Issuing
    `Transaction` object.

    Related guide: [Issued Card Transactions](https://stripe.com/docs/issuing/purchases/transactions).
    """

    OBJECT_NAME = "issuing.transaction"
