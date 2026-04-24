# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.network._business_profile_me_params import (
        BusinessProfileMeParams,
    )
    from stripe.params.v2.network._business_profile_retrieve_params import (
        BusinessProfileRetrieveParams,
    )
    from stripe.v2.network._business_profile import BusinessProfile


class BusinessProfileService(StripeService):
    def me(
        self,
        params: Optional["BusinessProfileMeParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "BusinessProfile":
        """
        Retrieve the Stripe profile associated with the requesting merchant and livemode.
        """
        return cast(
            "BusinessProfile",
            self._request(
                "get",
                "/v2/network/business_profiles/me",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def me_async(
        self,
        params: Optional["BusinessProfileMeParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "BusinessProfile":
        """
        Retrieve the Stripe profile associated with the requesting merchant and livemode.
        """
        return cast(
            "BusinessProfile",
            await self._request_async(
                "get",
                "/v2/network/business_profiles/me",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["BusinessProfileRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "BusinessProfile":
        """
        Retrieve a Stripe profile by its Network ID.
        """
        return cast(
            "BusinessProfile",
            self._request(
                "get",
                "/v2/network/business_profiles/{id}".format(
                    id=sanitize_id(id)
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: Optional["BusinessProfileRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "BusinessProfile":
        """
        Retrieve a Stripe profile by its Network ID.
        """
        return cast(
            "BusinessProfile",
            await self._request_async(
                "get",
                "/v2/network/business_profiles/{id}".format(
                    id=sanitize_id(id)
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
