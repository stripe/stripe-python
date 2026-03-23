# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.product_catalog._trial_offer_create_params import (
        TrialOfferCreateParams,
    )
    from stripe.product_catalog._trial_offer import TrialOffer


class TrialOfferService(StripeService):
    def create(
        self,
        params: "TrialOfferCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "TrialOffer":
        """
        Creates a trial offer.
        """
        return cast(
            "TrialOffer",
            self._request(
                "post",
                "/v1/product_catalog/trial_offers",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "TrialOfferCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "TrialOffer":
        """
        Creates a trial offer.
        """
        return cast(
            "TrialOffer",
            await self._request_async(
                "post",
                "/v1/product_catalog/trial_offers",
                base_address="api",
                params=params,
                options=options,
            ),
        )
