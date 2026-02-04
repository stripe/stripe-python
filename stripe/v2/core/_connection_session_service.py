# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.core._connection_session_create_params import (
        ConnectionSessionCreateParams,
    )
    from stripe.params.v2.core._connection_session_retrieve_params import (
        ConnectionSessionRetrieveParams,
    )
    from stripe.v2.core._connection_session import ConnectionSession


class ConnectionSessionService(StripeService):
    def create(
        self,
        params: "ConnectionSessionCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "ConnectionSession":
        """
        Create a new ConnectionSession.
        """
        return cast(
            "ConnectionSession",
            self._request(
                "post",
                "/v2/core/connection_sessions",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "ConnectionSessionCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "ConnectionSession":
        """
        Create a new ConnectionSession.
        """
        return cast(
            "ConnectionSession",
            await self._request_async(
                "post",
                "/v2/core/connection_sessions",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["ConnectionSessionRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ConnectionSession":
        """
        Retrieve a ConnectionSession.
        """
        return cast(
            "ConnectionSession",
            self._request(
                "get",
                "/v2/core/connection_sessions/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: Optional["ConnectionSessionRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ConnectionSession":
        """
        Retrieve a ConnectionSession.
        """
        return cast(
            "ConnectionSession",
            await self._request_async(
                "get",
                "/v2/core/connection_sessions/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
