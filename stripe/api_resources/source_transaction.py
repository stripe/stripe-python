# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.stripe_object import StripeObject


class SourceTransaction(StripeObject):
    """
    Some payment methods have no required amount that a customer must send.
    Customers can be instructed to send any amount, and it can be made up of
    multiple transactions. As such, sources can have multiple associated
    transactions.
    """

    OBJECT_NAME = "source_transaction"
