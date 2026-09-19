# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.issuing._authorization import Authorization
    from stripe.params.test_helpers.issuing._authorization_capture_params import (
        AuthorizationCaptureParams,
    )
    from stripe.params.test_helpers.issuing._authorization_create_params import (
        AuthorizationCreateParams,
    )
    from stripe.params.test_helpers.issuing._authorization_expire_params import (
        AuthorizationExpireParams,
    )
    from stripe.params.test_helpers.issuing._authorization_finalize_amount_params import (
        AuthorizationFinalizeAmountParams,
    )
    from stripe.params.test_helpers.issuing._authorization_increment_params import (
        AuthorizationIncrementParams,
    )
    from stripe.params.test_helpers.issuing._authorization_respond_params import (
        AuthorizationRespondParams,
    )
    from stripe.params.test_helpers.issuing._authorization_reverse_params import (
        AuthorizationReverseParams,
    )


class AuthorizationService(StripeService):
    def create(
        self,
        params: "AuthorizationCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Authorization":
        """
        Create a test-mode authorization.
        """
        return cast(
            "Authorization",
            self._request(
                "post",
                "/v1/test_helpers/issuing/authorizations",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "AuthorizationCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Authorization":
        """
        Create a test-mode authorization.
        """
        return cast(
            "Authorization",
            await self._request_async(
                "post",
                "/v1/test_helpers/issuing/authorizations",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def capture(
        self,
        id: str,
        /,
        params: Optional["AuthorizationCaptureParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Authorization":
        """
        Capture a test-mode authorization.
        """
        return cast(
            "Authorization",
            self._request(
                "post",
                "/v1/test_helpers/issuing/authorizations/{id}/capture".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def capture_async(
        self,
        id: str,
        /,
        params: Optional["AuthorizationCaptureParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Authorization":
        """
        Capture a test-mode authorization.
        """
        return cast(
            "Authorization",
            await self._request_async(
                "post",
                "/v1/test_helpers/issuing/authorizations/{id}/capture".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def expire(
        self,
        id: str,
        /,
        params: Optional["AuthorizationExpireParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Authorization":
        """
        Expire a test-mode Authorization.
        """
        return cast(
            "Authorization",
            self._request(
                "post",
                "/v1/test_helpers/issuing/authorizations/{id}/expire".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def expire_async(
        self,
        id: str,
        /,
        params: Optional["AuthorizationExpireParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Authorization":
        """
        Expire a test-mode Authorization.
        """
        return cast(
            "Authorization",
            await self._request_async(
                "post",
                "/v1/test_helpers/issuing/authorizations/{id}/expire".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def finalize_amount(
        self,
        id: str,
        /,
        params: "AuthorizationFinalizeAmountParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Authorization":
        """
        Finalize the amount on an Authorization prior to capture, when the initial authorization was for an estimated amount.
        """
        return cast(
            "Authorization",
            self._request(
                "post",
                "/v1/test_helpers/issuing/authorizations/{id}/finalize_amount".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def finalize_amount_async(
        self,
        id: str,
        /,
        params: "AuthorizationFinalizeAmountParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Authorization":
        """
        Finalize the amount on an Authorization prior to capture, when the initial authorization was for an estimated amount.
        """
        return cast(
            "Authorization",
            await self._request_async(
                "post",
                "/v1/test_helpers/issuing/authorizations/{id}/finalize_amount".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def respond(
        self,
        id: str,
        /,
        params: "AuthorizationRespondParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Authorization":
        """
        Respond to a fraud challenge on a testmode Issuing authorization, simulating either a confirmation of fraud or a correction of legitimacy.
        """
        return cast(
            "Authorization",
            self._request(
                "post",
                "/v1/test_helpers/issuing/authorizations/{id}/fraud_challenges/respond".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def respond_async(
        self,
        id: str,
        /,
        params: "AuthorizationRespondParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Authorization":
        """
        Respond to a fraud challenge on a testmode Issuing authorization, simulating either a confirmation of fraud or a correction of legitimacy.
        """
        return cast(
            "Authorization",
            await self._request_async(
                "post",
                "/v1/test_helpers/issuing/authorizations/{id}/fraud_challenges/respond".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def increment(
        self,
        id: str,
        /,
        params: "AuthorizationIncrementParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Authorization":
        """
        Increment a test-mode Authorization.
        """
        return cast(
            "Authorization",
            self._request(
                "post",
                "/v1/test_helpers/issuing/authorizations/{id}/increment".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def increment_async(
        self,
        id: str,
        /,
        params: "AuthorizationIncrementParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Authorization":
        """
        Increment a test-mode Authorization.
        """
        return cast(
            "Authorization",
            await self._request_async(
                "post",
                "/v1/test_helpers/issuing/authorizations/{id}/increment".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def reverse(
        self,
        id: str,
        /,
        params: Optional["AuthorizationReverseParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Authorization":
        """
        Reverse a test-mode Authorization.
        """
        return cast(
            "Authorization",
            self._request(
                "post",
                "/v1/test_helpers/issuing/authorizations/{id}/reverse".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def reverse_async(
        self,
        id: str,
        /,
        params: Optional["AuthorizationReverseParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Authorization":
        """
        Reverse a test-mode Authorization.
        """
        return cast(
            "Authorization",
            await self._request_async(
                "post",
                "/v1/test_helpers/issuing/authorizations/{id}/reverse".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
