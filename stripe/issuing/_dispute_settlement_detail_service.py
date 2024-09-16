# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._list_object import ListObject
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.issuing._dispute_settlement_detail import DisputeSettlementDetail
from typing import List, cast
from typing_extensions import NotRequired, TypedDict


class DisputeSettlementDetailService(StripeService):
    class ListParams(TypedDict):
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
        settlement: NotRequired[str]
        """
        Select the Issuing dispute settlement details for the given settlement.
        """
        starting_after: NotRequired[str]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """

    class RetrieveParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    def list(
        self,
        params: "DisputeSettlementDetailService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[DisputeSettlementDetail]:
        """
        Returns a list of Issuing DisputeSettlementDetail objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.
        """
        return cast(
            ListObject[DisputeSettlementDetail],
            self._request(
                "get",
                "/v1/issuing/dispute_settlement_details",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "DisputeSettlementDetailService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[DisputeSettlementDetail]:
        """
        Returns a list of Issuing DisputeSettlementDetail objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.
        """
        return cast(
            ListObject[DisputeSettlementDetail],
            await self._request_async(
                "get",
                "/v1/issuing/dispute_settlement_details",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        dispute_settlement_detail: str,
        params: "DisputeSettlementDetailService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> DisputeSettlementDetail:
        """
        Retrieves an Issuing DisputeSettlementDetail object.
        """
        return cast(
            DisputeSettlementDetail,
            self._request(
                "get",
                "/v1/issuing/dispute_settlement_details/{dispute_settlement_detail}".format(
                    dispute_settlement_detail=sanitize_id(
                        dispute_settlement_detail
                    ),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        dispute_settlement_detail: str,
        params: "DisputeSettlementDetailService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> DisputeSettlementDetail:
        """
        Retrieves an Issuing DisputeSettlementDetail object.
        """
        return cast(
            DisputeSettlementDetail,
            await self._request_async(
                "get",
                "/v1/issuing/dispute_settlement_details/{dispute_settlement_detail}".format(
                    dispute_settlement_detail=sanitize_id(
                        dispute_settlement_detail
                    ),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
