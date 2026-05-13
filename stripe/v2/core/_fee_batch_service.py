# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.core._fee_batch_list_params import FeeBatchListParams
    from stripe.params.v2.core._fee_batch_retrieve_params import (
        FeeBatchRetrieveParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.core._fee_batch import FeeBatch


class FeeBatchService(StripeService):
    def list(
        self,
        params: Optional["FeeBatchListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[FeeBatch]":
        """
        List FeeBatches optionally filtered by collection_record.
        """
        return cast(
            "ListObject[FeeBatch]",
            self._request(
                "get",
                "/v2/core/fee_batches",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["FeeBatchListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[FeeBatch]":
        """
        List FeeBatches optionally filtered by collection_record.
        """
        return cast(
            "ListObject[FeeBatch]",
            await self._request_async(
                "get",
                "/v2/core/fee_batches",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["FeeBatchRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "FeeBatch":
        """
        Retrieve a FeeBatch by id.
        """
        return cast(
            "FeeBatch",
            self._request(
                "get",
                "/v2/core/fee_batches/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: Optional["FeeBatchRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "FeeBatch":
        """
        Retrieve a FeeBatch by id.
        """
        return cast(
            "FeeBatch",
            await self._request_async(
                "get",
                "/v2/core/fee_batches/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
