# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._list_object import ListObject
    from stripe._request_options import RequestOptions
    from stripe.params.three_d_secure._authentication_cancel_params import (
        AuthenticationCancelParams,
    )
    from stripe.params.three_d_secure._authentication_create_params import (
        AuthenticationCreateParams,
    )
    from stripe.params.three_d_secure._authentication_list_params import (
        AuthenticationListParams,
    )
    from stripe.params.three_d_secure._authentication_retrieve_params import (
        AuthenticationRetrieveParams,
    )
    from stripe.params.three_d_secure._authentication_submit_params import (
        AuthenticationSubmitParams,
    )
    from stripe.three_d_secure._authentication import Authentication


class AuthenticationService(StripeService):
    def list(
        self,
        params: Optional["AuthenticationListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Authentication]":
        """
        Returns a list of 3D Secure Authentications.
        """
        return cast(
            "ListObject[Authentication]",
            self._request(
                "get",
                "/v1/three_d_secure/authentications",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["AuthenticationListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Authentication]":
        """
        Returns a list of 3D Secure Authentications.
        """
        return cast(
            "ListObject[Authentication]",
            await self._request_async(
                "get",
                "/v1/three_d_secure/authentications",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "AuthenticationCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Authentication":
        """
        This endpoint creates a 3DS Authentication. Refer to the [Create a 3DS Authentication object section of the Standalone 3DS guide](https://docs.stripe.com/payments/3d-secure/standalone-3d-secure#create-a-3ds-authentication-object) for more information.

        You can pass the submit parameter to automatically submit the 3DS Authentication object when you create it. Refer to the [Submit at creation section of the Standalone 3DS guide](https://docs.stripe.com/payments/3d-secure/standalone-3d-secure#submit-at-creation) for more information.
        """
        return cast(
            "Authentication",
            self._request(
                "post",
                "/v1/three_d_secure/authentications",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "AuthenticationCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Authentication":
        """
        This endpoint creates a 3DS Authentication. Refer to the [Create a 3DS Authentication object section of the Standalone 3DS guide](https://docs.stripe.com/payments/3d-secure/standalone-3d-secure#create-a-3ds-authentication-object) for more information.

        You can pass the submit parameter to automatically submit the 3DS Authentication object when you create it. Refer to the [Submit at creation section of the Standalone 3DS guide](https://docs.stripe.com/payments/3d-secure/standalone-3d-secure#submit-at-creation) for more information.
        """
        return cast(
            "Authentication",
            await self._request_async(
                "post",
                "/v1/three_d_secure/authentications",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        authentication: str,
        /,
        params: Optional["AuthenticationRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Authentication":
        """
        This endpoint retrieves a 3DS Authentication.
        """
        return cast(
            "Authentication",
            self._request(
                "get",
                "/v1/three_d_secure/authentications/{authentication}".format(
                    authentication=sanitize_id(authentication),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        authentication: str,
        /,
        params: Optional["AuthenticationRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Authentication":
        """
        This endpoint retrieves a 3DS Authentication.
        """
        return cast(
            "Authentication",
            await self._request_async(
                "get",
                "/v1/three_d_secure/authentications/{authentication}".format(
                    authentication=sanitize_id(authentication),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def cancel(
        self,
        authentication: str,
        /,
        params: Optional["AuthenticationCancelParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Authentication":
        """
        This endpoint cancels a 3DS Authentication. You can cancel a 3DS Authentication object when it's in a non-final status:
        requires_submission or requires_challenge.
        """
        return cast(
            "Authentication",
            self._request(
                "post",
                "/v1/three_d_secure/authentications/{authentication}/cancel".format(
                    authentication=sanitize_id(authentication),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def cancel_async(
        self,
        authentication: str,
        /,
        params: Optional["AuthenticationCancelParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Authentication":
        """
        This endpoint cancels a 3DS Authentication. You can cancel a 3DS Authentication object when it's in a non-final status:
        requires_submission or requires_challenge.
        """
        return cast(
            "Authentication",
            await self._request_async(
                "post",
                "/v1/three_d_secure/authentications/{authentication}/cancel".format(
                    authentication=sanitize_id(authentication),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def submit(
        self,
        authentication: str,
        /,
        params: Optional["AuthenticationSubmitParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Authentication":
        """
        This endpoint submits a 3DS Authentication. You can submit a 3DS Authentication object when it has status requires_submission. Refer to the [Submit the 3DS Authentication object section of the Standalone 3DS guide](https://docs.stripe.com/payments/3d-secure/standalone-3d-secure#submit-the-3ds-authentication-object) for more information.
        """
        return cast(
            "Authentication",
            self._request(
                "post",
                "/v1/three_d_secure/authentications/{authentication}/submit".format(
                    authentication=sanitize_id(authentication),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def submit_async(
        self,
        authentication: str,
        /,
        params: Optional["AuthenticationSubmitParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Authentication":
        """
        This endpoint submits a 3DS Authentication. You can submit a 3DS Authentication object when it has status requires_submission. Refer to the [Submit the 3DS Authentication object section of the Standalone 3DS guide](https://docs.stripe.com/payments/3d-secure/standalone-3d-secure#submit-the-3ds-authentication-object) for more information.
        """
        return cast(
            "Authentication",
            await self._request_async(
                "post",
                "/v1/three_d_secure/authentications/{authentication}/submit".format(
                    authentication=sanitize_id(authentication),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
