# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import DeletableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource


class SKU(
    CreateableAPIResource,
    DeletableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    """
    Stores representations of [stock keeping units](http://en.wikipedia.org/wiki/Stock_keeping_unit).
    SKUs describe specific product variations, taking into account any combination of: attributes,
    currency, and cost. For example, a product may be a T-shirt, whereas a specific SKU represents
    the `size: large`, `color: red` version of that shirt.

    Can also be used to manage inventory.
    """

    OBJECT_NAME = "sku"
