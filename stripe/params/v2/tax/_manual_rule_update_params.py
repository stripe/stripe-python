# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class ManualRuleUpdateParams(TypedDict):
    location: NotRequired["ManualRuleUpdateParamsLocation"]
    """
    Location where the rule applies.
    """
    products: NotRequired[List["ManualRuleUpdateParamsProduct"]]
    """
    Products associated with the rule.
    """
    scheduled_tax_rates: List["ManualRuleUpdateParamsScheduledTaxRate"]
    """
    Tax rates to be applied.
    """


class ManualRuleUpdateParamsLocation(TypedDict):
    country: str
    """
    Country ISO-3166.
    """
    state: NotRequired[str]
    """
    State ISO-3166.
    """


class ManualRuleUpdateParamsProduct(TypedDict):
    type: Literal["licensed_item", "metered_item", "tax_code"]
    """
    The type of the product.
    """
    licensed_item: NotRequired[str]
    """
    The licensed item identifier.
    """
    metered_item: NotRequired[str]
    """
    The metered item identifier.
    """
    tax_code: NotRequired[str]
    """
    The tax code for the product.
    """


class ManualRuleUpdateParamsScheduledTaxRate(TypedDict):
    rates: List["ManualRuleUpdateParamsScheduledTaxRateRate"]
    """
    The tax rates to be applied.
    """
    starts_at: NotRequired[str]
    """
    The start time for the tax rate.
    """


class ManualRuleUpdateParamsScheduledTaxRateRate(TypedDict):
    country: NotRequired[str]
    """
    Country of the tax rate.
    """
    description: NotRequired[str]
    """
    Description of the tax rate.
    """
    display_name: str
    """
    Display name of the tax rate as it will be shown on the invoice.
    """
    jurisdiction: NotRequired[str]
    """
    Jurisdiction of the tax rate should apply as it will be shown on the invoice.
    """
    percentage: str
    """
    Percentage of the tax rate. Must be positive and maximum of 4 decimal points.
    """
    state: NotRequired[str]
    """
    State of the tax rate.
    """
