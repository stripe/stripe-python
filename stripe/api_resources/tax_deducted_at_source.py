# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.stripe_object import StripeObject
from typing_extensions import Literal


class TaxDeductedAtSource(StripeObject):
    OBJECT_NAME = "tax_deducted_at_source"
    id: str
    object: Literal["tax_deducted_at_source"]
    period_end: str
    period_start: str
    tax_deduction_account_number: str
