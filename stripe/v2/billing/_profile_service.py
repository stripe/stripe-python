# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.billing._profile_create_params import (
        ProfileCreateParams,
    )
    from stripe.params.v2.billing._profile_list_params import ProfileListParams
    from stripe.params.v2.billing._profile_retrieve_params import (
        ProfileRetrieveParams,
    )
    from stripe.params.v2.billing._profile_update_params import (
        ProfileUpdateParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.billing._profile import Profile


class ProfileService(StripeService):
    def list(
        self,
        params: "ProfileListParams",
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Profile]":
        """
        List Billing Profiles.
        """
        return cast(
            "ListObject[Profile]",
            self._request(
                "get",
                "/v2/billing/profiles",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "ProfileListParams",
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Profile]":
        """
        List Billing Profiles.
        """
        return cast(
            "ListObject[Profile]",
            await self._request_async(
                "get",
                "/v2/billing/profiles",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "ProfileCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Profile":
        """
        Create a BillingProfile object.
        """
        return cast(
            "Profile",
            self._request(
                "post",
                "/v2/billing/profiles",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "ProfileCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Profile":
        """
        Create a BillingProfile object.
        """
        return cast(
            "Profile",
            await self._request_async(
                "post",
                "/v2/billing/profiles",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["ProfileRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Profile":
        """
        Retrieve a BillingProfile object.
        """
        return cast(
            "Profile",
            self._request(
                "get",
                "/v2/billing/profiles/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: Optional["ProfileRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Profile":
        """
        Retrieve a BillingProfile object.
        """
        return cast(
            "Profile",
            await self._request_async(
                "get",
                "/v2/billing/profiles/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        id: str,
        params: Optional["ProfileUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Profile":
        """
        Update a BillingProfile object.
        """
        return cast(
            "Profile",
            self._request(
                "post",
                "/v2/billing/profiles/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        id: str,
        params: Optional["ProfileUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Profile":
        """
        Update a BillingProfile object.
        """
        return cast(
            "Profile",
            await self._request_async(
                "post",
                "/v2/billing/profiles/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
