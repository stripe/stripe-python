# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.iam._api_key_create_params import ApiKeyCreateParams
    from stripe.params.v2.iam._api_key_expire_params import ApiKeyExpireParams
    from stripe.params.v2.iam._api_key_list_params import ApiKeyListParams
    from stripe.params.v2.iam._api_key_retrieve_params import (
        ApiKeyRetrieveParams,
    )
    from stripe.params.v2.iam._api_key_rotate_params import ApiKeyRotateParams
    from stripe.params.v2.iam._api_key_update_params import ApiKeyUpdateParams
    from stripe.v2._list_object import ListObject
    from stripe.v2.iam._api_key import ApiKey


class ApiKeyService(StripeService):
    def list(
        self,
        params: Optional["ApiKeyListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[ApiKey]":
        """
        List all API keys of an account.
        """
        return cast(
            "ListObject[ApiKey]",
            self._request(
                "get",
                "/v2/iam/api_keys",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["ApiKeyListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[ApiKey]":
        """
        List all API keys of an account.
        """
        return cast(
            "ListObject[ApiKey]",
            await self._request_async(
                "get",
                "/v2/iam/api_keys",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "ApiKeyCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "ApiKey":
        """
        Create an API key. To create a secret key in livemode, a public key for encryption must be provided.
        """
        return cast(
            "ApiKey",
            self._request(
                "post",
                "/v2/iam/api_keys",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "ApiKeyCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "ApiKey":
        """
        Create an API key. To create a secret key in livemode, a public key for encryption must be provided.
        """
        return cast(
            "ApiKey",
            await self._request_async(
                "post",
                "/v2/iam/api_keys",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["ApiKeyRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ApiKey":
        """
        Retrieve an API key. For livemode secret keys, secret tokens are only returned on creation, and never returned here.
        """
        return cast(
            "ApiKey",
            self._request(
                "get",
                "/v2/iam/api_keys/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: Optional["ApiKeyRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ApiKey":
        """
        Retrieve an API key. For livemode secret keys, secret tokens are only returned on creation, and never returned here.
        """
        return cast(
            "ApiKey",
            await self._request_async(
                "get",
                "/v2/iam/api_keys/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        id: str,
        params: Optional["ApiKeyUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ApiKey":
        """
        Update an API key. Only parameters that are specified in the request will be updated.
        """
        return cast(
            "ApiKey",
            self._request(
                "post",
                "/v2/iam/api_keys/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        id: str,
        params: Optional["ApiKeyUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ApiKey":
        """
        Update an API key. Only parameters that are specified in the request will be updated.
        """
        return cast(
            "ApiKey",
            await self._request_async(
                "post",
                "/v2/iam/api_keys/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def expire(
        self,
        id: str,
        params: Optional["ApiKeyExpireParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ApiKey":
        """
        Expire an API key. The specified key becomes invalid immediately.
        """
        return cast(
            "ApiKey",
            self._request(
                "post",
                "/v2/iam/api_keys/{id}/expire".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def expire_async(
        self,
        id: str,
        params: Optional["ApiKeyExpireParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ApiKey":
        """
        Expire an API key. The specified key becomes invalid immediately.
        """
        return cast(
            "ApiKey",
            await self._request_async(
                "post",
                "/v2/iam/api_keys/{id}/expire".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def rotate(
        self,
        id: str,
        params: Optional["ApiKeyRotateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ApiKey":
        """
        Rotate an API key. A new key with the same properties is created and returned. The existing key is expired immediately, unless an expiry time is specified.
        """
        return cast(
            "ApiKey",
            self._request(
                "post",
                "/v2/iam/api_keys/{id}/rotate".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def rotate_async(
        self,
        id: str,
        params: Optional["ApiKeyRotateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ApiKey":
        """
        Rotate an API key. A new key with the same properties is created and returned. The existing key is expired immediately, unless an expiry time is specified.
        """
        return cast(
            "ApiKey",
            await self._request_async(
                "post",
                "/v2/iam/api_keys/{id}/rotate".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
