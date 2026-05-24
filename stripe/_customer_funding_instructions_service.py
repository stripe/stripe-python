# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
import json
from stripe._api_version import _ApiVersion
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from uuid import uuid4
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._funding_instructions import FundingInstructions
    from stripe._request_options import RequestOptions
    from stripe.params._customer_funding_instructions_create_funding_instructions_params import (
        CustomerFundingInstructionsCreateFundingInstructionsParams,
    )
    from stripe.params._customer_funding_instructions_create_params import (
        CustomerFundingInstructionsCreateParams,
    )


class CustomerFundingInstructionsService(StripeService):
    def create(
        self,
        customer: str,
        params: "CustomerFundingInstructionsCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "FundingInstructions":
        """
        Retrieve funding instructions for a customer cash balance. If funding instructions do not yet exist for the customer, new
        funding instructions will be created. If funding instructions have already been created for a given customer, the same
        funding instructions will be retrieved. In other words, we will return the same funding instructions each time.
        """
        return cast(
            "FundingInstructions",
            self._request(
                "post",
                "/v1/customers/{customer}/funding_instructions".format(
                    customer=sanitize_id(customer),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        customer: str,
        params: "CustomerFundingInstructionsCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "FundingInstructions":
        """
        Retrieve funding instructions for a customer cash balance. If funding instructions do not yet exist for the customer, new
        funding instructions will be created. If funding instructions have already been created for a given customer, the same
        funding instructions will be retrieved. In other words, we will return the same funding instructions each time.
        """
        return cast(
            "FundingInstructions",
            await self._request_async(
                "post",
                "/v1/customers/{customer}/funding_instructions".format(
                    customer=sanitize_id(customer),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def serialize_batch_create_funding_instructions(
        self,
        customer: str,
        params: Optional[
            "CustomerFundingInstructionsCreateFundingInstructionsParams"
        ] = None,
        options: Optional["RequestOptions"] = None,
    ) -> str:
        """
        Serializes a CustomerFundingInstructions create request into a batch job JSONL line.
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
        }
        if context is not None:
            item["context"] = context
        return json.dumps(item)
