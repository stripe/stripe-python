# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2._list_object import ListObject
from stripe.v2.billing._rate_card_version import RateCardVersion
from typing import cast
from typing_extensions import NotRequired, TypedDict


class VersionService(StripeService):
    class ListParams(TypedDict):
        limit: NotRequired[int]
        """
        Optionally set the maximum number of results per page. Defaults to 20.
        """

    class RetrieveParams(TypedDict):
        pass

    def list(
        self,
        rate_card_id: str,
        params: "VersionService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[RateCardVersion]:
        """
        List the versions of a Rate Card object. Results are sorted in reverse chronological order (most recent first).
        """
        return cast(
            ListObject[RateCardVersion],
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
        params: "VersionService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[RateCardVersion]:
        """
        List the versions of a Rate Card object. Results are sorted in reverse chronological order (most recent first).
        """
        return cast(
            ListObject[RateCardVersion],
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
        params: "VersionService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> RateCardVersion:
        """
        Retrieve a specific version of a Rate Card object.
        """
        return cast(
            RateCardVersion,
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
        params: "VersionService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> RateCardVersion:
        """
        Retrieve a specific version of a Rate Card object.
        """
        return cast(
            RateCardVersion,
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
