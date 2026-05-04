# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._payment_location import PaymentLocation
    from stripe._request_options import RequestOptions
    from stripe.params._payment_location_create_params import (
        PaymentLocationCreateParams,
    )


class PaymentLocationService(StripeService):
    def create(
        self,
        params: "PaymentLocationCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentLocation":
        """
        Create a Payment Location.
        """
        return cast(
            "PaymentLocation",
            self._request(
                "post",
                "/v1/payment_locations",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "PaymentLocationCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentLocation":
        """
        Create a Payment Location.
        """
        return cast(
            "PaymentLocation",
            await self._request_async(
                "post",
                "/v1/payment_locations",
                base_address="api",
                params=params,
                options=options,
            ),
        )
