# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import APIResource


class Mandate(APIResource):
    """
    A Mandate is a record of the permission a customer has given you to debit their payment method.
    """

    OBJECT_NAME = "mandate"
