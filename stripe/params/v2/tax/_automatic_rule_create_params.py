# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import TypedDict


class AutomaticRuleCreateParams(TypedDict):
    billable_item: str
    """
    The BillableItem ID to set automatic Tax configuration for.
    """
    tax_code: str
    """
    The TaxCode object to be used for automatic tax calculations.
    """
