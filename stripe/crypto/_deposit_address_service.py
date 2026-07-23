# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._list_object import ListObject
    from stripe._request_options import RequestOptions
    from stripe.crypto._deposit_address import DepositAddress
    from stripe.params.crypto._deposit_address_create_params import (
        DepositAddressCreateParams,
    )
    from stripe.params.crypto._deposit_address_list_params import (
        DepositAddressListParams,
    )
    from stripe.params.crypto._deposit_address_retrieve_params import (
        DepositAddressRetrieveParams,
    )


class DepositAddressService(StripeService):
    def list(
        self,
        params: Optional["DepositAddressListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[DepositAddress]":
        """
        Lists crypto deposit addresses for the authenticated merchant.
        Supports cursor-based pagination and optional filtering by customer, network, or on-chain address.
        """
        return cast(
            "ListObject[DepositAddress]",
            self._request(
                "get",
                "/v1/crypto/deposit_addresses",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["DepositAddressListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[DepositAddress]":
        """
        Lists crypto deposit addresses for the authenticated merchant.
        Supports cursor-based pagination and optional filtering by customer, network, or on-chain address.
        """
        return cast(
            "ListObject[DepositAddress]",
            await self._request_async(
                "get",
                "/v1/crypto/deposit_addresses",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "DepositAddressCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "DepositAddress":
        """
        Creates a new crypto deposit address for the authenticated merchant on the specified network.
        The returned address can be used across multiple PaymentIntents.
        """
        return cast(
            "DepositAddress",
            self._request(
                "post",
                "/v1/crypto/deposit_addresses",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "DepositAddressCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "DepositAddress":
        """
        Creates a new crypto deposit address for the authenticated merchant on the specified network.
        The returned address can be used across multiple PaymentIntents.
        """
        return cast(
            "DepositAddress",
            await self._request_async(
                "post",
                "/v1/crypto/deposit_addresses",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["DepositAddressRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "DepositAddress":
        """
        Retrieves the details of an existing crypto deposit address by ID.
        """
        return cast(
            "DepositAddress",
            self._request(
                "get",
                "/v1/crypto/deposit_addresses/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: Optional["DepositAddressRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "DepositAddress":
        """
        Retrieves the details of an existing crypto deposit address by ID.
        """
        return cast(
            "DepositAddress",
            await self._request_async(
                "get",
                "/v1/crypto/deposit_addresses/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
