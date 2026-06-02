# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._api_resource import APIResource
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, Optional
from typing_extensions import Literal, Unpack, TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.delegated_checkout._order_event import OrderEvent
    from stripe.params.delegated_checkout._order_retrieve_params import (
        OrderRetrieveParams,
    )


class Order(APIResource["Order"]):
    """
    An order represents the post-checkout lifecycle of a delegated checkout purchase.
    """

    OBJECT_NAME: ClassVar[Literal["delegated_checkout.order"]] = (
        "delegated_checkout.order"
    )

    class LineItem(StripeObject):
        class ProductDetails(StripeObject):
            description: Optional[str]
            """
            The item description.
            """
            images: Optional[List[str]]
            """
            The item images.
            """
            title: str
            """
            The item title.
            """

        class Quantity(StripeObject):
            current: int
            """
            The current quantity.
            """
            ordered: int
            """
            The ordered quantity.
            """
            shipped: int
            """
            The shipped quantity.
            """

        class Totals(StripeObject):
            base_amount: Optional[int]
            """
            The base amount for the line item.
            """
            discount: Optional[int]
            """
            The discount amount for the line item.
            """
            subtotal: Optional[int]
            """
            The subtotal amount for the line item.
            """
            tax: Optional[int]
            """
            The tax amount for the line item.
            """
            total: Optional[int]
            """
            The total amount for the line item.
            """

        key: str
        """
        The order line item key.
        """
        product_details: ProductDetails
        quantity: Quantity
        sku_id: str
        """
        The SKU ID of the line item.
        """
        totals: Optional[Totals]
        """
        The totals for this line item.
        """
        unit_amount: int
        """
        The line item unit amount.
        """
        _inner_class_types = {
            "product_details": ProductDetails,
            "quantity": Quantity,
            "totals": Totals,
        }

    class Totals(StripeObject):
        discount: Optional[int]
        """
        The discount amount for the order.
        """
        fulfillment: Optional[int]
        """
        The fulfillment amount for the order.
        """
        subtotal: Optional[int]
        """
        The subtotal amount for the order.
        """
        tax: Optional[int]
        """
        The tax amount for the order.
        """
        total: Optional[int]
        """
        The total amount for the order.
        """

    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    currency: str
    """
    Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
    """
    id: str
    """
    Unique identifier for the object.
    """
    latest_order_event: Optional["OrderEvent"]
    """
    The latest order event for this order.
    """
    line_items: List[LineItem]
    """
    The line items in this order.
    """
    livemode: bool
    """
    If the object exists in live mode, the value is `true`. If the object exists in test mode, the value is `false`.
    """
    object: Literal["delegated_checkout.order"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    permalink_url: Optional[str]
    """
    The permalink URL for this order.
    """
    requested_session: str
    """
    The requested session associated with this order.
    """
    seller_reference: Optional[str]
    """
    The seller reference for this order.
    """
    totals: Optional[Totals]
    """
    The totals for this order.
    """

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["OrderRetrieveParams"]
    ) -> "Order":
        """
        Retrieves a delegated checkout order.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["OrderRetrieveParams"]
    ) -> "Order":
        """
        Retrieves a delegated checkout order.
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    _inner_class_types = {"line_items": LineItem, "totals": Totals}
