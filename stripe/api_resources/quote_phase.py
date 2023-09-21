# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe import util
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Any, List, Optional
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.discount import Discount
    from stripe.api_resources.line_item import LineItem
    from stripe.api_resources.tax_rate import TaxRate


class QuotePhase(ListableAPIResource["QuotePhase"]):
    """
    A quote phase describes the line items, coupons, and trialing status of a subscription for a predefined time period.
    """

    OBJECT_NAME = "quote_phase"
    amount_subtotal: int
    amount_total: int
    billing_cycle_anchor: Optional[Literal["reset"]]
    collection_method: Optional[
        Literal["charge_automatically", "send_invoice"]
    ]
    default_tax_rates: Optional[List[ExpandableField["TaxRate"]]]
    discounts: List[ExpandableField["Discount"]]
    end_date: Optional[int]
    id: str
    invoice_settings: Optional[StripeObject]
    iterations: Optional[int]
    line_items: Optional[ListObject["LineItem"]]
    object: Literal["quote_phase"]
    proration_behavior: Literal["always_invoice", "create_prorations", "none"]
    total_details: StripeObject
    trial: Optional[bool]
    trial_end: Optional[int]

    @classmethod
    def list(
        cls,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ) -> ListObject["QuotePhase"]:
        result = cls._static_request(
            "get",
            cls.class_url(),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )
        if not isinstance(result, ListObject):

            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    def _cls_list_line_items(
        cls,
        quote_phase: str,
        api_key: Optional[str] = None,
        stripe_version: Optional[str] = None,
        stripe_account: Optional[str] = None,
        **params: Any
    ):
        return cls._static_request(
            "get",
            "/v1/quote_phases/{quote_phase}/line_items".format(
                quote_phase=util.sanitize_id(quote_phase)
            ),
            api_key=api_key,
            stripe_version=stripe_version,
            stripe_account=stripe_account,
            params=params,
        )

    @util.class_method_variant("_cls_list_line_items")
    def list_line_items(
        self, idempotency_key: Optional[str] = None, **params: Any
    ):
        return self._request(
            "get",
            "/v1/quote_phases/{quote_phase}/line_items".format(
                quote_phase=util.sanitize_id(self.get("id"))
            ),
            idempotency_key=idempotency_key,
            params=params,
        )

    @classmethod
    def retrieve(
        cls, id: str, api_key: Optional[str] = None, **params: Any
    ) -> "QuotePhase":
        instance = cls(id, api_key, **params)
        instance.refresh()
        return instance
