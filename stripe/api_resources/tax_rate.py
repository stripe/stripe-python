# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource
from typing import Dict
from typing import Optional
from typing_extensions import Literal


class TaxRate(
    CreateableAPIResource["TaxRate"],
    ListableAPIResource["TaxRate"],
    UpdateableAPIResource["TaxRate"],
):
    """
    Tax rates can be applied to [invoices](https://stripe.com/docs/billing/invoices/tax-rates), [subscriptions](https://stripe.com/docs/billing/subscriptions/taxes) and [Checkout Sessions](https://stripe.com/docs/payments/checkout/set-up-a-subscription#tax-rates) to collect tax.

    Related guide: [Tax rates](https://stripe.com/docs/billing/taxes/tax-rates)
    """

    OBJECT_NAME = "tax_rate"
    active: bool
    country: Optional[str]
    created: str
    description: Optional[str]
    display_name: str
    effective_percentage: Optional[float]
    id: str
    inclusive: bool
    jurisdiction: Optional[str]
    livemode: bool
    metadata: Optional[Dict[str, str]]
    object: Literal["tax_rate"]
    percentage: float
    state: Optional[str]
    tax_type: Optional[str]
