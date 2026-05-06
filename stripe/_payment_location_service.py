# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._payment_location import PaymentLocation
    from stripe._request_options import RequestOptions
    from stripe.params._payment_location_create_params import (
        PaymentLocationCreateParams,
    )
    from stripe.params._payment_location_delete_params import (
        PaymentLocationDeleteParams,
    )
    from stripe.params._payment_location_retrieve_params import (
        PaymentLocationRetrieveParams,
    )
    from stripe.params._payment_location_update_params import (
        PaymentLocationUpdateParams,
    )


class PaymentLocationService(StripeService):
    def delete(
        self,
        id: str,
        params: Optional["PaymentLocationDeleteParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentLocation":
        """
        Delete a Payment Location.
        """
        return cast(
            "PaymentLocation",
            self._request(
                "delete",
                "/v1/payment_locations/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def delete_async(
        self,
        id: str,
        params: Optional["PaymentLocationDeleteParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentLocation":
        """
        Delete a Payment Location.
        """
        return cast(
            "PaymentLocation",
            await self._request_async(
                "delete",
                "/v1/payment_locations/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["PaymentLocationRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentLocation":
        """
        Retrieve a Payment Location.
        """
        return cast(
            "PaymentLocation",
            self._request(
                "get",
                "/v1/payment_locations/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: Optional["PaymentLocationRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentLocation":
        """
        Retrieve a Payment Location.
        """
        return cast(
            "PaymentLocation",
            await self._request_async(
                "get",
                "/v1/payment_locations/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        id: str,
        params: Optional["PaymentLocationUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentLocation":
        """
        Update a Payment Location.
        """
        return cast(
            "PaymentLocation",
            self._request(
                "post",
                "/v1/payment_locations/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        id: str,
        params: Optional["PaymentLocationUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentLocation":
        """
        Update a Payment Location.
        """
        return cast(
            "PaymentLocation",
            await self._request_async(
                "post",
                "/v1/payment_locations/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

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
