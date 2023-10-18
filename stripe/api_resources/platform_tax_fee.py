# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.stripe_object import StripeObject
from typing import ClassVar
from typing_extensions import Literal


class PlatformTaxFee(StripeObject):
    OBJECT_NAME: ClassVar[Literal["platform_tax_fee"]] = "platform_tax_fee"
    account: str
    id: str
    object: Literal["platform_tax_fee"]
    source_transaction: str
    type: str
