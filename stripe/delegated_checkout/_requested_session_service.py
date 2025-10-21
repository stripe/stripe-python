# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.delegated_checkout._requested_session import RequestedSession
    from stripe.params.delegated_checkout._requested_session_confirm_params import (
        RequestedSessionConfirmParams,
    )
    from stripe.params.delegated_checkout._requested_session_create_params import (
        RequestedSessionCreateParams,
    )
    from stripe.params.delegated_checkout._requested_session_expire_params import (
        RequestedSessionExpireParams,
    )
    from stripe.params.delegated_checkout._requested_session_retrieve_params import (
        RequestedSessionRetrieveParams,
    )
    from stripe.params.delegated_checkout._requested_session_update_params import (
        RequestedSessionUpdateParams,
    )


class RequestedSessionService(StripeService):
    def retrieve(
        self,
        requested_session: str,
        params: Optional["RequestedSessionRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RequestedSession":
        """
        Retrieves a requested session
        """
        return cast(
            "RequestedSession",
            self._request(
                "get",
                "/v1/delegated_checkout/requested_sessions/{requested_session}".format(
                    requested_session=sanitize_id(requested_session),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        requested_session: str,
        params: Optional["RequestedSessionRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RequestedSession":
        """
        Retrieves a requested session
        """
        return cast(
            "RequestedSession",
            await self._request_async(
                "get",
                "/v1/delegated_checkout/requested_sessions/{requested_session}".format(
                    requested_session=sanitize_id(requested_session),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        requested_session: str,
        params: Optional["RequestedSessionUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RequestedSession":
        """
        Updates a requested session
        """
        return cast(
            "RequestedSession",
            self._request(
                "post",
                "/v1/delegated_checkout/requested_sessions/{requested_session}".format(
                    requested_session=sanitize_id(requested_session),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        requested_session: str,
        params: Optional["RequestedSessionUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RequestedSession":
        """
        Updates a requested session
        """
        return cast(
            "RequestedSession",
            await self._request_async(
                "post",
                "/v1/delegated_checkout/requested_sessions/{requested_session}".format(
                    requested_session=sanitize_id(requested_session),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "RequestedSessionCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "RequestedSession":
        """
        Creates a requested session
        """
        return cast(
            "RequestedSession",
            self._request(
                "post",
                "/v1/delegated_checkout/requested_sessions",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "RequestedSessionCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "RequestedSession":
        """
        Creates a requested session
        """
        return cast(
            "RequestedSession",
            await self._request_async(
                "post",
                "/v1/delegated_checkout/requested_sessions",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def confirm(
        self,
        requested_session: str,
        params: Optional["RequestedSessionConfirmParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RequestedSession":
        """
        Confirms a requested session
        """
        return cast(
            "RequestedSession",
            self._request(
                "post",
                "/v1/delegated_checkout/requested_sessions/{requested_session}/confirm".format(
                    requested_session=sanitize_id(requested_session),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def confirm_async(
        self,
        requested_session: str,
        params: Optional["RequestedSessionConfirmParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RequestedSession":
        """
        Confirms a requested session
        """
        return cast(
            "RequestedSession",
            await self._request_async(
                "post",
                "/v1/delegated_checkout/requested_sessions/{requested_session}/confirm".format(
                    requested_session=sanitize_id(requested_session),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def expire(
        self,
        requested_session: str,
        params: Optional["RequestedSessionExpireParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RequestedSession":
        """
        Expires a requested session
        """
        return cast(
            "RequestedSession",
            self._request(
                "post",
                "/v1/delegated_checkout/requested_sessions/{requested_session}/expire".format(
                    requested_session=sanitize_id(requested_session),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def expire_async(
        self,
        requested_session: str,
        params: Optional["RequestedSessionExpireParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RequestedSession":
        """
        Expires a requested session
        """
        return cast(
            "RequestedSession",
            await self._request_async(
                "post",
                "/v1/delegated_checkout/requested_sessions/{requested_session}/expire".format(
                    requested_session=sanitize_id(requested_session),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
