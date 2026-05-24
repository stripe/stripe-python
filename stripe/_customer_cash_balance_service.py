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
    from stripe._cash_balance import CashBalance
    from stripe._request_options import RequestOptions
    from stripe.params._customer_cash_balance_retrieve_params import (
        CustomerCashBalanceRetrieveParams,
    )
    from stripe.params._customer_cash_balance_update_params import (
        CustomerCashBalanceUpdateParams,
    )


class CustomerCashBalanceService(StripeService):
    def retrieve(
        self,
        customer: str,
        params: Optional["CustomerCashBalanceRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "CashBalance":
        """
        Retrieves a customer's cash balance.
        """
        return cast(
            "CashBalance",
            self._request(
                "get",
                "/v1/customers/{customer}/cash_balance".format(
                    customer=sanitize_id(customer),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        customer: str,
        params: Optional["CustomerCashBalanceRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "CashBalance":
        """
        Retrieves a customer's cash balance.
        """
        return cast(
            "CashBalance",
            await self._request_async(
                "get",
                "/v1/customers/{customer}/cash_balance".format(
                    customer=sanitize_id(customer),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        customer: str,
        params: Optional["CustomerCashBalanceUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "CashBalance":
        """
        Changes the settings on a customer's cash balance.
        """
        return cast(
            "CashBalance",
            self._request(
                "post",
                "/v1/customers/{customer}/cash_balance".format(
                    customer=sanitize_id(customer),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        customer: str,
        params: Optional["CustomerCashBalanceUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "CashBalance":
        """
        Changes the settings on a customer's cash balance.
        """
        return cast(
            "CashBalance",
            await self._request_async(
                "post",
                "/v1/customers/{customer}/cash_balance".format(
                    customer=sanitize_id(customer),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def serialize_batch_update(
        self,
        customer: str,
        params: Optional["CustomerCashBalanceUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> str:
        """
        Serializes a CustomerCashBalance update request into a batch job JSONL line.
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
