# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List
from typing_extensions import NotRequired


class ProductCreateFeatureParams(RequestOptions):
    entitlement_feature: str
    """
    The ID of the [Feature](https://stripe.com/docs/api/entitlements/feature) object attached to this product.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
