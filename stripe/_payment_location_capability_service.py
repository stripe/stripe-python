# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._list_object import ListObject
    from stripe._payment_location_capability import PaymentLocationCapability
    from stripe._request_options import RequestOptions
    from stripe.params._payment_location_capability_list_params import (
        PaymentLocationCapabilityListParams,
    )
    from stripe.params._payment_location_capability_retrieve_params import (
        PaymentLocationCapabilityRetrieveParams,
    )
    from stripe.params._payment_location_capability_update_params import (
        PaymentLocationCapabilityUpdateParams,
    )


class PaymentLocationCapabilityService(StripeService):
    def list(
        self,
        params: "PaymentLocationCapabilityListParams",
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[PaymentLocationCapability]":
        """
        List all payment location capabilities associated with the payment location.
        """
        return cast(
            "ListObject[PaymentLocationCapability]",
            self._request(
                "get",
                "/v1/payment_location_capabilities",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "PaymentLocationCapabilityListParams",
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[PaymentLocationCapability]":
        """
        List all payment location capabilities associated with the payment location.
        """
        return cast(
            "ListObject[PaymentLocationCapability]",
            await self._request_async(
                "get",
                "/v1/payment_location_capabilities",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        capability: str,
        params: "PaymentLocationCapabilityRetrieveParams",
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentLocationCapability":
        """
        Retrieves a payment_location capability
        """
        return cast(
            "PaymentLocationCapability",
            self._request(
                "get",
                "/v1/payment_location_capabilities/{capability}".format(
                    capability=sanitize_id(capability),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        capability: str,
        params: "PaymentLocationCapabilityRetrieveParams",
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentLocationCapability":
        """
        Retrieves a payment_location capability
        """
        return cast(
            "PaymentLocationCapability",
            await self._request_async(
                "get",
                "/v1/payment_location_capabilities/{capability}".format(
                    capability=sanitize_id(capability),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        capability: str,
        params: "PaymentLocationCapabilityUpdateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentLocationCapability":
        """
        Updates a payment_location capability. Request or remove a payment_location capability by updating its requested parameter.
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
        Updates a payment_location capability. Request or remove a payment_location capability by updating its requested parameter.
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
