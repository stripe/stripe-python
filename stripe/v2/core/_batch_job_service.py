# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from json import dumps
from stripe._api_version import _ApiVersion
from stripe._stripe_service import StripeService
from typing import Optional, cast
from uuid import uuid4
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._customer import CustomerUpdateParams
    from stripe._request_options import RequestOptions
    from stripe._subscription import SubscriptionUpdateParams
    from stripe._subscription_schedule import SubscriptionScheduleCreateParams
    from stripe.params.v2.core._batch_job_create_params import (
        BatchJobCreateParams,
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

    def serialize_v1_customer_update(
        self,
        customer: str,
        params: Optional["CustomerUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> str:
        """
        Serializes a Customer update request into a batch job JSONL line.
        """
        item_id = str(uuid4())
        stripe_version = (
            options.get("stripe_version") if options else None
        ) or _ApiVersion.CURRENT
        context = options.get("stripe_context") if options else None
        item = {
            "id": item_id,
            "path_params": {"customer": customer},
            "params": params,
            "stripe_version": stripe_version,
            "context": context,
        }
        return dumps(item)

    def serialize_v1_subscription_update(
        self,
        subscription_exposed_id: str,
        params: Optional["SubscriptionUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> str:
        """
        Serializes a Subscription update request into a batch job JSONL line.
        """
        item_id = str(uuid4())
        stripe_version = (
            options.get("stripe_version") if options else None
        ) or _ApiVersion.CURRENT
        context = options.get("stripe_context") if options else None
        item = {
            "id": item_id,
            "path_params": {
                "subscription_exposed_id": subscription_exposed_id
            },
            "params": params,
            "stripe_version": stripe_version,
            "context": context,
        }
        return dumps(item)

    def serialize_v1_subscription_schedule_create(
        self,
        params: Optional["SubscriptionScheduleCreateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> str:
        """
        Serializes a SubscriptionSchedule create request into a batch job JSONL line.
        """
        item_id = str(uuid4())
        stripe_version = (
            options.get("stripe_version") if options else None
        ) or _ApiVersion.CURRENT
        context = options.get("stripe_context") if options else None
        item = {
            "id": item_id,
            "path_params": None,
            "params": params,
            "stripe_version": stripe_version,
            "context": context,
        }
        return dumps(item)
