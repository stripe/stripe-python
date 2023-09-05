# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import List
from typing import Optional
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.tax.calculation_line_item import (
        CalculationLineItem,
    )


class Calculation(CreateableAPIResource["Calculation"]):
    """
    A Tax Calculation allows you to calculate the tax to collect from your customer.

    Related guide: [Calculate tax in your custom payment flow](https://stripe.com/docs/tax/custom)
    """

    OBJECT_NAME = "tax.calculation"
    amount_total: int
    currency: str
    customer: Optional[str]
    customer_details: StripeObject
    expires_at: Optional[str]
    id: Optional[str]
    line_items: Optional[ListObject["CalculationLineItem"]]
    livemode: bool
    object: Literal["tax.calculation"]
    shipping_cost: Optional[StripeObject]
    tax_amount_exclusive: int
    tax_amount_inclusive: int
    tax_breakdown: List[StripeObject]
    tax_date: str

    @classmethod
    def _cls_list_line_items(
        cls,
        calculation,
        api_key=None,
        stripe_version=None,
        stripe_account=None,
        **params
    ):
        return cls._static_request(
            "get",
            "/v1/tax/calculations/{calculation}/line_items".format(
                calculation=util.sanitize_id(calculation)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_list_line_items")
    def list_line_items(self, idempotency_key=None, **params):
        return self._request(
            "get",
            "/v1/tax/calculations/{calculation}/line_items".format(
                calculation=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )
