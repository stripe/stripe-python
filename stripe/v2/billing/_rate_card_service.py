# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2._list_object import ListObject
from stripe.v2.billing._rate_card import RateCard
from stripe.v2.billing.rate_cards._rate_service import RateService
from stripe.v2.billing.rate_cards._version_service import VersionService
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.v2.billing._rate_card_create_params import (
        RateCardCreateParams,
    )
    from stripe.params.v2.billing._rate_card_list_params import (
        RateCardListParams,
    )
    from stripe.params.v2.billing._rate_card_retrieve_params import (
        RateCardRetrieveParams,
    )
    from stripe.params.v2.billing._rate_card_update_params import (
        RateCardUpdateParams,
    )


class RateCardService(StripeService):
    def __init__(self, requestor):
        super().__init__(requestor)
        self.rates = RateService(self._requestor)
        self.versions = VersionService(self._requestor)

    def list(
        self,
        params: Optional["RateCardListParams"] = None,
        options: Optional[RequestOptions] = None,
    ) -> ListObject[RateCard]:
        """
        List all Rate Card objects.
        """
        return cast(
            ListObject[RateCard],
            self._request(
                "get",
                "/v2/billing/rate_cards",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["RateCardListParams"] = None,
        options: Optional[RequestOptions] = None,
    ) -> ListObject[RateCard]:
        """
        List all Rate Card objects.
        """
        return cast(
            ListObject[RateCard],
            await self._request_async(
                "get",
                "/v2/billing/rate_cards",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "RateCardCreateParams",
        options: Optional[RequestOptions] = None,
    ) -> RateCard:
        """
        Create a Rate Card object.
        """
        return cast(
            RateCard,
            self._request(
                "post",
                "/v2/billing/rate_cards",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "RateCardCreateParams",
        options: Optional[RequestOptions] = None,
    ) -> RateCard:
        """
        Create a Rate Card object.
        """
        return cast(
            RateCard,
            await self._request_async(
                "post",
                "/v2/billing/rate_cards",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["RateCardRetrieveParams"] = None,
        options: Optional[RequestOptions] = None,
    ) -> RateCard:
        """
        Retrieve the latest version of a Rate Card object.
        """
        return cast(
            RateCard,
            self._request(
                "get",
                "/v2/billing/rate_cards/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: Optional["RateCardRetrieveParams"] = None,
        options: Optional[RequestOptions] = None,
    ) -> RateCard:
        """
        Retrieve the latest version of a Rate Card object.
        """
        return cast(
            RateCard,
            await self._request_async(
                "get",
                "/v2/billing/rate_cards/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        id: str,
        params: Optional["RateCardUpdateParams"] = None,
        options: Optional[RequestOptions] = None,
    ) -> RateCard:
        """
        Update a Rate Card object.
        """
        return cast(
            RateCard,
            self._request(
                "post",
                "/v2/billing/rate_cards/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        id: str,
        params: Optional["RateCardUpdateParams"] = None,
        options: Optional[RequestOptions] = None,
    ) -> RateCard:
        """
        Update a Rate Card object.
        """
        return cast(
            RateCard,
            await self._request_async(
                "post",
                "/v2/billing/rate_cards/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
