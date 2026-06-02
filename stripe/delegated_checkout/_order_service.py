# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.delegated_checkout._order import Order
    from stripe.params.delegated_checkout._order_retrieve_params import (
        OrderRetrieveParams,
    )


class OrderService(StripeService):
    def retrieve(
        self,
        order_id: str,
        params: Optional["OrderRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Order":
        """
        Retrieves a delegated checkout order.
        """
        return cast(
            "Order",
            self._request(
                "get",
                "/v1/delegated_checkout/orders/{order_id}".format(
                    order_id=sanitize_id(order_id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        order_id: str,
        params: Optional["OrderRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Order":
        """
        Retrieves a delegated checkout order.
        """
        return cast(
            "Order",
            await self._request_async(
                "get",
                "/v1/delegated_checkout/orders/{order_id}".format(
                    order_id=sanitize_id(order_id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
