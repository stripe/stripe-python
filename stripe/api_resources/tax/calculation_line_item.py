# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.stripe_object import StripeObject
from typing import List, Optional
from typing_extensions import Literal


class CalculationLineItem(StripeObject):
    OBJECT_NAME = "tax.calculation_line_item"

    class TaxBreakdown(StripeObject):
        class Jurisdiction(StripeObject):
            country: str
            display_name: str
            level: Literal["city", "country", "county", "district", "state"]
            state: Optional[str]

        class TaxRateDetails(StripeObject):
            display_name: str
            percentage_decimal: str
            tax_type: Literal[
                "amusement_tax",
                "communications_tax",
                "gst",
                "hst",
                "igst",
                "jct",
                "lease_tax",
                "pst",
                "qst",
                "rst",
                "sales_tax",
                "vat",
            ]

        amount: int
        jurisdiction: Jurisdiction
        sourcing: Literal["destination", "origin"]
        tax_rate_details: Optional[TaxRateDetails]
        taxability_reason: Literal[
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
        taxable_amount: int
        _inner_class_types = {
            "jurisdiction": Jurisdiction,
            "tax_rate_details": TaxRateDetails,
        }

    amount: int
    amount_tax: int
    id: str
    livemode: bool
    object: Literal["tax.calculation_line_item"]
    product: Optional[str]
    quantity: int
    reference: Optional[str]
    tax_behavior: Literal["exclusive", "inclusive"]
    tax_breakdown: Optional[List[TaxBreakdown]]
    tax_code: str

    _inner_class_types = {"tax_breakdown": TaxBreakdown}
