# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import Dict, List
from typing_extensions import NotRequired, TypedDict


class MeteredItemCreateParams(TypedDict):
    display_name: str
    """
    Description that customers will see in the invoice line item.
    Maximum length of 250 characters.
    """
    invoice_presentation_dimensions: NotRequired[List[str]]
    """
    Optional array of Meter dimensions to group event dimension keys for invoice line items.
    """
    lookup_key: NotRequired[str]
    """
    An internal key you can use to search for a particular billable item.
    Must be unique among billable items.
    Maximum length of 200 characters.
    """
    metadata: NotRequired[Dict[str, str]]
    """
    Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
    """
    meter: str
    """
    ID of the Meter that measures usage for this Metered Item.
    """
    meter_segment_conditions: NotRequired[
        List["MeteredItemCreateParamsMeterSegmentCondition"]
    ]
    """
    Optional array of Meter segments to filter event dimension keys for billing.
    """
    tax_details: NotRequired["MeteredItemCreateParamsTaxDetails"]
    """
    Stripe Tax details.
    """
    unit_label: NotRequired[str]
    """
    The unit to use when displaying prices for this billable item in places like Checkout. For example, set this field
    to "CPU-hour" for Checkout to display "(price) per CPU-hour", or "1 million events" to display "(price) per 1
    million events".
    Maximum length of 100 characters.
    """


class MeteredItemCreateParamsMeterSegmentCondition(TypedDict):
    dimension: str
    """
    A Meter dimension.
    """
    value: str
    """
    To count usage towards this metered item, the dimension must have this value.
    """


class MeteredItemCreateParamsTaxDetails(TypedDict):
    tax_code: str
    """
    Product tax code (PTC).
    """
