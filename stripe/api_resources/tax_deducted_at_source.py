# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.stripe_object import StripeObject
from typing_extensions import Literal


class TaxDeductedAtSource(StripeObject):
    OBJECT_NAME = "tax_deducted_at_source"
    id: str
    object: Literal["tax_deducted_at_source"]
    period_end: int
    period_start: int
    tax_deduction_account_number: str
