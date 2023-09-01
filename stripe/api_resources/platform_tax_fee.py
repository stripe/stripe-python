# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.stripe_object import StripeObject
from typing_extensions import Literal


class PlatformTaxFee(StripeObject):
    OBJECT_NAME = "platform_tax_fee"
    account: str
    id: str
    object: Literal["platform_tax_fee"]
    source_transaction: str
    type: str
