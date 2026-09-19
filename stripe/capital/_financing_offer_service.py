# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._list_object import ListObject
    from stripe._request_options import RequestOptions
    from stripe.capital._financing_offer import FinancingOffer
    from stripe.params.capital._financing_offer_list_params import (
        FinancingOfferListParams,
    )
    from stripe.params.capital._financing_offer_mark_delivered_params import (
        FinancingOfferMarkDeliveredParams,
    )
    from stripe.params.capital._financing_offer_retrieve_params import (
        FinancingOfferRetrieveParams,
    )


class FinancingOfferService(StripeService):
    def list(
        self,
        params: Optional["FinancingOfferListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[FinancingOffer]":
        """
        Retrieves the financing offers available for Connected accounts that belong to your platform.
        """
        return cast(
            "ListObject[FinancingOffer]",
            self._request(
                "get",
                "/v1/capital/financing_offers",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["FinancingOfferListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[FinancingOffer]":
        """
        Retrieves the financing offers available for Connected accounts that belong to your platform.
        """
        return cast(
            "ListObject[FinancingOffer]",
            await self._request_async(
                "get",
                "/v1/capital/financing_offers",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        /,
        params: Optional["FinancingOfferRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "FinancingOffer":
        """
        Get the details of the financing offer
        """
        return cast(
            "FinancingOffer",
            self._request(
                "get",
                "/v1/capital/financing_offers/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        /,
        params: Optional["FinancingOfferRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "FinancingOffer":
        """
        Get the details of the financing offer
        """
        return cast(
            "FinancingOffer",
            await self._request_async(
                "get",
                "/v1/capital/financing_offers/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def mark_delivered(
        self,
        id: str,
        /,
        params: Optional["FinancingOfferMarkDeliveredParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "FinancingOffer":
        """
        Acknowledges that platform has received and delivered the financing_offer to
        the intended merchant recipient.
        """
        return cast(
            "FinancingOffer",
            self._request(
                "post",
                "/v1/capital/financing_offers/{id}/mark_delivered".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def mark_delivered_async(
        self,
        id: str,
        /,
        params: Optional["FinancingOfferMarkDeliveredParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "FinancingOffer":
        """
        Acknowledges that platform has received and delivered the financing_offer to
        the intended merchant recipient.
        """
        return cast(
            "FinancingOffer",
            await self._request_async(
                "post",
                "/v1/capital/financing_offers/{id}/mark_delivered".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
