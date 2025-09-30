# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import NotRequired, TypedDict


class ProductFeatureCreateParams(TypedDict):
    entitlement_feature: str
    """
    The ID of the [Feature](https://stripe.com/docs/api/entitlements/feature) object attached to this product.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
