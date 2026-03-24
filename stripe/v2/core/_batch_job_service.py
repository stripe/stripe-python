# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.core._batch_job_cancel_params import (
        BatchJobCancelParams,
    )
    from stripe.params.v2.core._batch_job_create_params import (
        BatchJobCreateParams,
    )
    from stripe.params.v2.core._batch_job_retrieve_params import (
        BatchJobRetrieveParams,
    )
    from stripe.v2.core._batch_job import BatchJob


class BatchJobService(StripeService):
    def create(
        self,
        params: "BatchJobCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "BatchJob":
        """
        Creates a new batch job.
        """
        return cast(
            "BatchJob",
            self._request(
                "post",
                "/v2/core/batch_jobs",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "BatchJobCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "BatchJob":
        """
        Creates a new batch job.
        """
        return cast(
            "BatchJob",
            await self._request_async(
                "post",
                "/v2/core/batch_jobs",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["BatchJobRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "BatchJob":
        """
        Retrieves an existing batch job.
        """
        return cast(
            "BatchJob",
            self._request(
                "get",
                "/v2/core/batch_jobs/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: Optional["BatchJobRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "BatchJob":
        """
        Retrieves an existing batch job.
        """
        return cast(
            "BatchJob",
            await self._request_async(
                "get",
                "/v2/core/batch_jobs/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def cancel(
        self,
        id: str,
        params: Optional["BatchJobCancelParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "BatchJob":
        """
        Cancels an existing batch job.
        """
        return cast(
            "BatchJob",
            self._request(
                "post",
                "/v2/core/batch_jobs/{id}/cancel".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def cancel_async(
        self,
        id: str,
        params: Optional["BatchJobCancelParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "BatchJob":
        """
        Cancels an existing batch job.
        """
        return cast(
            "BatchJob",
            await self._request_async(
                "post",
                "/v2/core/batch_jobs/{id}/cancel".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
