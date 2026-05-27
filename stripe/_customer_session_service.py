# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
import json
from stripe._api_version import _ApiVersion
from stripe._stripe_service import StripeService
from typing import Optional, cast
from uuid import uuid4
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._customer_session import CustomerSession
    from stripe._request_options import RequestOptions
    from stripe.params._customer_session_create_params import (
        CustomerSessionCreateParams,
    )


class CustomerSessionService(StripeService):
    def create(
        self,
        params: "CustomerSessionCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "CustomerSession":
        """
        Creates a Customer Session object that includes a single-use client secret that you can use on your front-end to grant client-side API access for certain customer resources.
        """
        return cast(
            "CustomerSession",
            self._request(
                "post",
                "/v1/customer_sessions",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "CustomerSessionCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "CustomerSession":
        """
        Creates a Customer Session object that includes a single-use client secret that you can use on your front-end to grant client-side API access for certain customer resources.
        """
        return cast(
            "CustomerSession",
            await self._request_async(
                "post",
                "/v1/customer_sessions",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def serialize_batch_create(
        self,
        params: Optional["CustomerSessionCreateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> str:
        """
        Serializes a CustomerSession create request into a batch job JSONL line.
        """
        item_id = str(uuid4())
        stripe_version = (
            options.get("stripe_version") if options else None
        ) or _ApiVersion.CURRENT
        context = options.get("stripe_context") if options else None
        batch_request = {
            "id": item_id,
            "params": params,
            "stripe_version": stripe_version,
        }
        if context is not None:
            batch_request["context"] = context
        return json.dumps(batch_request)
