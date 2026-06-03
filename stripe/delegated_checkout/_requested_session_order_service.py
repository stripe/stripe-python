# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._list_object import ListObject
    from stripe._request_options import RequestOptions
    from stripe.delegated_checkout._order import Order
    from stripe.params.delegated_checkout._requested_session_order_list_params import (
        RequestedSessionOrderListParams,
    )


class RequestedSessionOrderService(StripeService):
    def list(
        self,
        requested_session: str,
        params: Optional["RequestedSessionOrderListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Order]":
        """
        Lists orders for a delegated checkout requested session.
        """
        return cast(
            "ListObject[Order]",
            self._request(
                "get",
                "/v1/delegated_checkout/requested_sessions/{requested_session}/orders".format(
                    requested_session=sanitize_id(requested_session),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        requested_session: str,
        params: Optional["RequestedSessionOrderListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Order]":
        """
        Lists orders for a delegated checkout requested session.
        """
        return cast(
            "ListObject[Order]",
            await self._request_async(
                "get",
                "/v1/delegated_checkout/requested_sessions/{requested_session}/orders".format(
                    requested_session=sanitize_id(requested_session),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
