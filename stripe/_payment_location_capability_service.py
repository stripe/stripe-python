# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._payment_location_capability import PaymentLocationCapability
    from stripe._request_options import RequestOptions
    from stripe.params._payment_location_capability_update_params import (
        PaymentLocationCapabilityUpdateParams,
    )


class PaymentLocationCapabilityService(StripeService):
    def update(
        self,
        capability: str,
        params: "PaymentLocationCapabilityUpdateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentLocationCapability":
        """
        Updates a specified Payment Location Capability. Request or remove a payment location capability by updating its requested parameter.
        """
        return cast(
            "PaymentLocationCapability",
            self._request(
                "post",
                "/v1/payment_location_capabilities/{capability}".format(
                    capability=sanitize_id(capability),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        capability: str,
        params: "PaymentLocationCapabilityUpdateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentLocationCapability":
        """
        Updates a specified Payment Location Capability. Request or remove a payment location capability by updating its requested parameter.
        """
        return cast(
            "PaymentLocationCapability",
            await self._request_async(
                "post",
                "/v1/payment_location_capabilities/{capability}".format(
                    capability=sanitize_id(capability),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
