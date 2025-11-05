# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.capital._financing_offer import FinancingOffer
    from stripe.params.test_helpers.capital._financing_offer_create_params import (
        FinancingOfferCreateParams,
    )
    from stripe.params.test_helpers.capital._financing_offer_refill_params import (
        FinancingOfferRefillParams,
    )


class FinancingOfferService(StripeService):
    def create(
        self,
        params: "FinancingOfferCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "FinancingOffer":
        """
        Creates a test financing offer for a connected account.
        """
        return cast(
            "FinancingOffer",
            self._request(
                "post",
                "/v1/test_helpers/capital/financing_offers",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "FinancingOfferCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "FinancingOffer":
        """
        Creates a test financing offer for a connected account.
        """
        return cast(
            "FinancingOffer",
            await self._request_async(
                "post",
                "/v1/test_helpers/capital/financing_offers",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def refill(
        self,
        financing_offer: str,
        params: "FinancingOfferRefillParams",
        options: Optional["RequestOptions"] = None,
    ) -> "FinancingOffer":
        """
        Refills a test financing offer for a connected account.
        """
        return cast(
            "FinancingOffer",
            self._request(
                "post",
                "/v1/test_helpers/capital/financing_offers/{financing_offer}/refill".format(
                    financing_offer=sanitize_id(financing_offer),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def refill_async(
        self,
        financing_offer: str,
        params: "FinancingOfferRefillParams",
        options: Optional["RequestOptions"] = None,
    ) -> "FinancingOffer":
        """
        Refills a test financing offer for a connected account.
        """
        return cast(
            "FinancingOffer",
            await self._request_async(
                "post",
                "/v1/test_helpers/capital/financing_offers/{financing_offer}/refill".format(
                    financing_offer=sanitize_id(financing_offer),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
