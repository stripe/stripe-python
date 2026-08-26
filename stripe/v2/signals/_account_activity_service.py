# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.signals._account_activity_create_params import (
        AccountActivityCreateParams,
    )
    from stripe.params.v2.signals._account_activity_delete_params import (
        AccountActivityDeleteParams,
    )
    from stripe.params.v2.signals._account_activity_retrieve_params import (
        AccountActivityRetrieveParams,
    )
    from stripe.v2._deleted_object import DeletedObject
    from stripe.v2.signals._account_activity import AccountActivity


class AccountActivityService(StripeService):
    def create(
        self,
        params: "AccountActivityCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "AccountActivity":
        """
        Creates a new account activity to report account registration, login, or evaluation follow-up activity.
        """
        return cast(
            "AccountActivity",
            self._request(
                "post",
                "/v2/signals/account_activity",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "AccountActivityCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "AccountActivity":
        """
        Creates a new account activity to report account registration, login, or evaluation follow-up activity.
        """
        return cast(
            "AccountActivity",
            await self._request_async(
                "post",
                "/v2/signals/account_activity",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def delete(
        self,
        id: str,
        params: Optional["AccountActivityDeleteParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "DeletedObject":
        """
        Deletes an AccountActivity by its ID.
        """
        return cast(
            "DeletedObject",
            self._request(
                "delete",
                "/v2/signals/account_activity/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def delete_async(
        self,
        id: str,
        params: Optional["AccountActivityDeleteParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "DeletedObject":
        """
        Deletes an AccountActivity by its ID.
        """
        return cast(
            "DeletedObject",
            await self._request_async(
                "delete",
                "/v2/signals/account_activity/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["AccountActivityRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "AccountActivity":
        """
        Retrieves an AccountActivity by its ID.
        """
        return cast(
            "AccountActivity",
            self._request(
                "get",
                "/v2/signals/account_activity/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: Optional["AccountActivityRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "AccountActivity":
        """
        Retrieves an AccountActivity by its ID.
        """
        return cast(
            "AccountActivity",
            await self._request_async(
                "get",
                "/v2/signals/account_activity/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
