# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import ListableAPIResource
from typing_extensions import Literal


class TaxCode(ListableAPIResource["TaxCode"]):
    """
    [Tax codes](https://stripe.com/docs/tax/tax-categories) classify goods and services for tax purposes.
    """

    OBJECT_NAME = "tax_code"
    description: str
    id: str
    name: str
    object: Literal["tax_code"]
