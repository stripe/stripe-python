# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import UntypedStripeObject
from typing import Dict
from typing_extensions import Literal, TypedDict


class ImportCreateParams(TypedDict):
    feed_type: Literal["inventory", "pricing", "product"]
    """
    The type of catalog data to import.
    """
    metadata: "Dict[str, str]|UntypedStripeObject[str]"
    """
    Additional information about the import in a structured format.
    """
    mode: Literal["replace", "upsert"]
    """
    The strategy for handling existing catalog data during import.
    """
