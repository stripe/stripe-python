# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.billing._service_action_create_params import (
        ServiceActionCreateParams,
    )
    from stripe.params.v2.billing._service_action_retrieve_params import (
        ServiceActionRetrieveParams,
    )
    from stripe.params.v2.billing._service_action_update_params import (
        ServiceActionUpdateParams,
    )
    from stripe.v2.billing._service_action import ServiceAction


class ServiceActionService(StripeService):
    def create(
        self,
        params: "ServiceActionCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "ServiceAction":
        """
        Create a Service Action object.
        """
        return cast(
            "ServiceAction",
            self._request(
                "post",
                "/v2/billing/service_actions",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "ServiceActionCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "ServiceAction":
        """
        Create a Service Action object.
        """
        return cast(
            "ServiceAction",
            await self._request_async(
                "post",
                "/v2/billing/service_actions",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["ServiceActionRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ServiceAction":
        """
        Retrieve a Service Action object.
        """
        return cast(
            "ServiceAction",
            self._request(
                "get",
                "/v2/billing/service_actions/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: Optional["ServiceActionRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ServiceAction":
        """
        Retrieve a Service Action object.
        """
        return cast(
            "ServiceAction",
            await self._request_async(
                "get",
                "/v2/billing/service_actions/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        id: str,
        params: Optional["ServiceActionUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ServiceAction":
        """
        Update a ServiceAction object.
        """
        return cast(
            "ServiceAction",
            self._request(
                "post",
                "/v2/billing/service_actions/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        id: str,
        params: Optional["ServiceActionUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ServiceAction":
        """
        Update a ServiceAction object.
        """
        return cast(
            "ServiceAction",
            await self._request_async(
                "post",
                "/v2/billing/service_actions/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
