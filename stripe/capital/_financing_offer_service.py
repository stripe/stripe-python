# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._list_object import ListObject
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.capital._financing_offer import FinancingOffer
from typing import List, cast
from typing_extensions import Literal, NotRequired, TypedDict


class FinancingOfferService(StripeService):
    class ListParams(TypedDict):
        connected_account: NotRequired[str]
        """
        limit list to offers belonging to given connected account
        """
        created: NotRequired["FinancingOfferService.ListParamsCreated|int"]
        """
        Only return offers that were created during the given date interval.
        """
        ending_before: NotRequired[str]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        limit: NotRequired[int]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        starting_after: NotRequired[str]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """
        status: NotRequired[
            Literal[
                "accepted",
                "canceled",
                "completed",
                "delivered",
                "expired",
                "fully_repaid",
                "paid_out",
                "rejected",
                "revoked",
                "undelivered",
            ]
        ]
        """
        limit list to offers with given status
        """

    class ListParamsCreated(TypedDict):
        gt: NotRequired[int]
        """
        Minimum value to filter by (exclusive)
        """
        gte: NotRequired[int]
        """
        Minimum value to filter by (inclusive)
        """
        lt: NotRequired[int]
        """
        Maximum value to filter by (exclusive)
        """
        lte: NotRequired[int]
        """
        Maximum value to filter by (inclusive)
        """

    class MarkDeliveredParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    class RetrieveParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    def list(
        self,
        params: "FinancingOfferService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[FinancingOffer]:
        """
        Retrieves the financing offers available for Connected accounts that belong to your platform.
        """
        return cast(
            ListObject[FinancingOffer],
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
        params: "FinancingOfferService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[FinancingOffer]:
        """
        Retrieves the financing offers available for Connected accounts that belong to your platform.
        """
        return cast(
            ListObject[FinancingOffer],
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
        financing_offer: str,
        params: "FinancingOfferService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> FinancingOffer:
        """
        Get the details of the financing offer
        """
        return cast(
            FinancingOffer,
            self._request(
                "get",
                "/v1/capital/financing_offers/{financing_offer}".format(
                    financing_offer=sanitize_id(financing_offer),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        financing_offer: str,
        params: "FinancingOfferService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> FinancingOffer:
        """
        Get the details of the financing offer
        """
        return cast(
            FinancingOffer,
            await self._request_async(
                "get",
                "/v1/capital/financing_offers/{financing_offer}".format(
                    financing_offer=sanitize_id(financing_offer),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def mark_delivered(
        self,
        financing_offer: str,
        params: "FinancingOfferService.MarkDeliveredParams" = {},
        options: RequestOptions = {},
    ) -> FinancingOffer:
        """
        Acknowledges that platform has received and delivered the financing_offer to
        the intended merchant recipient.
        """
        return cast(
            FinancingOffer,
            self._request(
                "post",
                "/v1/capital/financing_offers/{financing_offer}/mark_delivered".format(
                    financing_offer=sanitize_id(financing_offer),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def mark_delivered_async(
        self,
        financing_offer: str,
        params: "FinancingOfferService.MarkDeliveredParams" = {},
        options: RequestOptions = {},
    ) -> FinancingOffer:
        """
        Acknowledges that platform has received and delivered the financing_offer to
        the intended merchant recipient.
        """
        return cast(
            FinancingOffer,
            await self._request_async(
                "post",
                "/v1/capital/financing_offers/{financing_offer}/mark_delivered".format(
                    financing_offer=sanitize_id(financing_offer),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
