# File generated from our OpenAPI spec
from __future__ import absolute_import, division, print_function

from stripe.api_resources.abstract import CreateableAPIResource
from stripe.api_resources.abstract import ListableAPIResource
from stripe.api_resources.abstract import UpdateableAPIResource


class ShippingRate(
    CreateableAPIResource,
    ListableAPIResource,
    UpdateableAPIResource,
):
    """
    Shipping rates describe the price of shipping presented to your customers and can be
    applied to [Checkout Sessions](https://stripe.com/docs/payments/checkout/shipping)
    and [Orders](https://stripe.com/docs/orders/shipping) to collect shipping costs.
    """

    OBJECT_NAME = "shipping_rate"
