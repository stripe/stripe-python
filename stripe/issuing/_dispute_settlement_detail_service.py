# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.issuing._dispute_settlement_detail import DisputeSettlementDetail
from typing import List, cast
from typing_extensions import NotRequired, TypedDict


class DisputeSettlementDetailService(StripeService):
    class RetrieveParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

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
                api_mode="V1",
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
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )
