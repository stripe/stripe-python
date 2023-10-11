# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe import util
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.expandable_field import ExpandableField
from stripe.api_resources.list_object import ListObject
from stripe.stripe_object import StripeObject
from typing import Any, List, Optional
from typing_extensions import Literal

from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.api_resources.discount import Discount as DiscountResource
    from stripe.api_resources.line_item import LineItem
    from stripe.api_resources.tax_rate import TaxRate


class QuotePhase(ListableAPIResource["QuotePhase"]):
    """
    A quote phase describes the line items, coupons, and trialing status of a subscription for a predefined time period.
    """

    OBJECT_NAME = "quote_phase"

    class InvoiceSettings(StripeObject):
        days_until_due: Optional[int]

    class TotalDetails(StripeObject):
        class Breakdown(StripeObject):
            class Discount(StripeObject):
                amount: int
                discount: "DiscountResource"

            class Tax(StripeObject):
                amount: int
                rate: "TaxRate"
                taxability_reason: Optional[
                    Literal[
                        "customer_exempt",
                        "not_collecting",
                        "not_subject_to_tax",
                        "not_supported",
                        "portion_product_exempt",
                        "portion_reduced_rated",
                        "portion_standard_rated",
                        "product_exempt",
                        "product_exempt_holiday",
                        "proportionally_rated",
                        "reduced_rated",
                        "reverse_charge",
                        "standard_rated",
                        "taxable_basis_reduced",
                        "zero_rated",
                    ]
                ]
                taxable_amount: Optional[int]

            discounts: List[Discount]
            taxes: List[Tax]
            _inner_class_types = {"discounts": Discount, "taxes": Tax}

        amount_discount: int
        amount_shipping: Optional[int]
        amount_tax: int
        breakdown: Optional[Breakdown]
        _inner_class_types = {"breakdown": Breakdown}

    amount_subtotal: int
    amount_total: int
    billing_cycle_anchor: Optional[Literal["reset"]]
    collection_method: Optional[
        Literal["charge_automatically", "send_invoice"]
    ]
    default_tax_rates: Optional[List[ExpandableField["TaxRate"]]]
    discounts: List[ExpandableField["DiscountResource"]]
    end_date: Optional[int]
    id: str
    invoice_settings: Optional[InvoiceSettings]
    iterations: Optional[int]
    line_items: Optional[ListObject["LineItem"]]
    object: Literal["quote_phase"]
    proration_behavior: Literal["always_invoice", "create_prorations", "none"]
    total_details: TotalDetails
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

    _inner_class_types = {
        "invoice_settings": InvoiceSettings,
        "total_details": TotalDetails,
    }
