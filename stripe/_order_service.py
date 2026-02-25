# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._list_object import ListObject
    from stripe._order import Order
    from stripe._request_options import RequestOptions
    from stripe.params._order_create_params import OrderCreateParams
    from stripe.params._order_list_params import OrderListParams
    from stripe.params._order_retrieve_params import OrderRetrieveParams
    from stripe.params._order_submit_params import OrderSubmitParams
    from stripe.params._order_update_params import OrderUpdateParams


class OrderService(StripeService):
    def list(
        self,
        params: Optional["OrderListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Order]":
        """
        Returns a list of your orders. The orders are returned sorted by creation date, with the most recently created orders appearing first.
        """
        return cast(
            "ListObject[Order]",
            self._request(
                "get",
                "/v1/orders",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["OrderListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Order]":
        """
        Returns a list of your orders. The orders are returned sorted by creation date, with the most recently created orders appearing first.
        """
        return cast(
            "ListObject[Order]",
            await self._request_async(
                "get",
                "/v1/orders",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "OrderCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Order":
        """
        Creates a new open order object.
        """
        return cast(
            "Order",
            self._request(
                "post",
                "/v1/orders",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "OrderCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Order":
        """
        Creates a new open order object.
        """
        return cast(
            "Order",
            await self._request_async(
                "post",
                "/v1/orders",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["OrderRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Order":
        """
        Retrieves the details of an existing order. Supply the unique order ID from either an order creation request or the order list, and Stripe will return the corresponding order information.
        """
        return cast(
            "Order",
            self._request(
                "get",
                "/v1/orders/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: Optional["OrderRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Order":
        """
        Retrieves the details of an existing order. Supply the unique order ID from either an order creation request or the order list, and Stripe will return the corresponding order information.
        """
        return cast(
            "Order",
            await self._request_async(
                "get",
                "/v1/orders/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        id: str,
        params: Optional["OrderUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Order":
        """
        Updates the specific order by setting the values of the parameters passed. Any parameters not provided will be left unchanged.
        """
        return cast(
            "Order",
            self._request(
                "post",
                "/v1/orders/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        id: str,
        params: Optional["OrderUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Order":
        """
        Updates the specific order by setting the values of the parameters passed. Any parameters not provided will be left unchanged.
        """
        return cast(
            "Order",
            await self._request_async(
                "post",
                "/v1/orders/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def submit(
        self,
        id: str,
        params: "OrderSubmitParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Order":
        """
        Submitting an Order transitions the status to processing and creates a PaymentIntent object so the order can be paid. If the Order has an amount_total of 0, no PaymentIntent object will be created. Once the order is submitted, its contents cannot be changed, unless the [reopen](https://docs.stripe.com/api#reopen_order) method is called.
        """
        return cast(
            "Order",
            self._request(
                "post",
                "/v1/orders/{id}/submit".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def submit_async(
        self,
        id: str,
        params: "OrderSubmitParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Order":
        """
        Submitting an Order transitions the status to processing and creates a PaymentIntent object so the order can be paid. If the Order has an amount_total of 0, no PaymentIntent object will be created. Once the order is submitted, its contents cannot be changed, unless the [reopen](https://docs.stripe.com/api#reopen_order) method is called.
        """
        return cast(
            "Order",
            await self._request_async(
                "post",
                "/v1/orders/{id}/submit".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
