# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._list_object import ListObject
    from stripe._request_options import RequestOptions
    from stripe.params.product_catalog._trial_offer_create_params import (
        TrialOfferCreateParams,
    )
    from stripe.params.product_catalog._trial_offer_list_params import (
        TrialOfferListParams,
    )
    from stripe.params.product_catalog._trial_offer_retrieve_params import (
        TrialOfferRetrieveParams,
    )
    from stripe.product_catalog._trial_offer import TrialOffer


class TrialOfferService(StripeService):
    def list(
        self,
        params: Optional["TrialOfferListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[TrialOffer]":
        """
        Returns a list of trial offers.
        """
        return cast(
            "ListObject[TrialOffer]",
            self._request(
                "get",
                "/v1/product_catalog/trial_offers",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["TrialOfferListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[TrialOffer]":
        """
        Returns a list of trial offers.
        """
        return cast(
            "ListObject[TrialOffer]",
            await self._request_async(
                "get",
                "/v1/product_catalog/trial_offers",
                base_address="api",
                params=params,
                options=options,
            ),
        )

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

    def retrieve(
        self,
        id: str,
        params: Optional["TrialOfferRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "TrialOffer":
        """
        Retrieves the trial offer with the given ID.
        """
        return cast(
            "TrialOffer",
            self._request(
                "get",
                "/v1/product_catalog/trial_offers/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: Optional["TrialOfferRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "TrialOffer":
        """
        Retrieves the trial offer with the given ID.
        """
        return cast(
            "TrialOffer",
            await self._request_async(
                "get",
                "/v1/product_catalog/trial_offers/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
