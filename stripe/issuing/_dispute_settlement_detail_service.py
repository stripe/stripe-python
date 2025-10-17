# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._list_object import ListObject
    from stripe._request_options import RequestOptions
    from stripe.issuing._dispute_settlement_detail import (
        DisputeSettlementDetail,
    )
    from stripe.params.issuing._dispute_settlement_detail_list_params import (
        DisputeSettlementDetailListParams,
    )
    from stripe.params.issuing._dispute_settlement_detail_retrieve_params import (
        DisputeSettlementDetailRetrieveParams,
    )


class DisputeSettlementDetailService(StripeService):
    def list(
        self,
        params: Optional["DisputeSettlementDetailListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[DisputeSettlementDetail]":
        """
        Returns a list of Issuing DisputeSettlementDetail objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.
        """
        return cast(
            "ListObject[DisputeSettlementDetail]",
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
        params: Optional["DisputeSettlementDetailListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[DisputeSettlementDetail]":
        """
        Returns a list of Issuing DisputeSettlementDetail objects. The objects are sorted in descending order by creation date, with the most recently created object appearing first.
        """
        return cast(
            "ListObject[DisputeSettlementDetail]",
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
        params: Optional["DisputeSettlementDetailRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "DisputeSettlementDetail":
        """
        Retrieves an Issuing DisputeSettlementDetail object.
        """
        return cast(
            "DisputeSettlementDetail",
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
        params: Optional["DisputeSettlementDetailRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "DisputeSettlementDetail":
        """
        Retrieves an Issuing DisputeSettlementDetail object.
        """
        return cast(
            "DisputeSettlementDetail",
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
