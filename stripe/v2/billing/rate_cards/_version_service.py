# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.billing.rate_cards._version_list_params import (
        VersionListParams,
    )
    from stripe.params.v2.billing.rate_cards._version_retrieve_params import (
        VersionRetrieveParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.billing._rate_card_version import RateCardVersion


class VersionService(StripeService):
    def list(
        self,
        rate_card_id: str,
        params: Optional["VersionListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[RateCardVersion]":
        """
        List the versions of a Rate Card object. Results are sorted in reverse chronological order (most recent first).
        """
        return cast(
            "ListObject[RateCardVersion]",
            self._request(
                "get",
                "/v2/billing/rate_cards/{rate_card_id}/versions".format(
                    rate_card_id=sanitize_id(rate_card_id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        rate_card_id: str,
        params: Optional["VersionListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[RateCardVersion]":
        """
        List the versions of a Rate Card object. Results are sorted in reverse chronological order (most recent first).
        """
        return cast(
            "ListObject[RateCardVersion]",
            await self._request_async(
                "get",
                "/v2/billing/rate_cards/{rate_card_id}/versions".format(
                    rate_card_id=sanitize_id(rate_card_id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        rate_card_id: str,
        id: str,
        params: Optional["VersionRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RateCardVersion":
        """
        Retrieve a specific version of a Rate Card object.
        """
        return cast(
            "RateCardVersion",
            self._request(
                "get",
                "/v2/billing/rate_cards/{rate_card_id}/versions/{id}".format(
                    rate_card_id=sanitize_id(rate_card_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        rate_card_id: str,
        id: str,
        params: Optional["VersionRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RateCardVersion":
        """
        Retrieve a specific version of a Rate Card object.
        """
        return cast(
            "RateCardVersion",
            await self._request_async(
                "get",
                "/v2/billing/rate_cards/{rate_card_id}/versions/{id}".format(
                    rate_card_id=sanitize_id(rate_card_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
