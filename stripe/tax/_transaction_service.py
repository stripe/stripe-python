# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
import json
from stripe._api_version import _ApiVersion
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from uuid import uuid4
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.tax._transaction_create_from_calculation_params import (
        TransactionCreateFromCalculationParams,
    )
    from stripe.params.tax._transaction_create_reversal_params import (
        TransactionCreateReversalParams,
    )
    from stripe.params.tax._transaction_retrieve_params import (
        TransactionRetrieveParams,
    )
    from stripe.tax._transaction import Transaction
    from stripe.tax._transaction_line_item_service import (
        TransactionLineItemService,
    )

_subservices = {
    "line_items": [
        "stripe.tax._transaction_line_item_service",
        "TransactionLineItemService",
    ],
}


class TransactionService(StripeService):
    line_items: "TransactionLineItemService"

    def __init__(self, requestor):
        super().__init__(requestor)

    def __getattr__(self, name):
        try:
            import_from, service = _subservices[name]
            service_class = getattr(
                import_module(import_from),
                service,
            )
            setattr(
                self,
                name,
                service_class(self._requestor),
            )
            return getattr(self, name)
        except KeyError:
            raise AttributeError()

    def retrieve(
        self,
        transaction: str,
        params: Optional["TransactionRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Transaction":
        """
        Retrieves a Tax Transaction object.
        """
        return cast(
            "Transaction",
            self._request(
                "get",
                "/v1/tax/transactions/{transaction}".format(
                    transaction=sanitize_id(transaction),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        transaction: str,
        params: Optional["TransactionRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Transaction":
        """
        Retrieves a Tax Transaction object.
        """
        return cast(
            "Transaction",
            await self._request_async(
                "get",
                "/v1/tax/transactions/{transaction}".format(
                    transaction=sanitize_id(transaction),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create_from_calculation(
        self,
        params: "TransactionCreateFromCalculationParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Transaction":
        """
        Creates a Tax Transaction from a calculation, if that calculation hasn't expired. Calculations expire after 90 days.
        """
        return cast(
            "Transaction",
            self._request(
                "post",
                "/v1/tax/transactions/create_from_calculation",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_from_calculation_async(
        self,
        params: "TransactionCreateFromCalculationParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Transaction":
        """
        Creates a Tax Transaction from a calculation, if that calculation hasn't expired. Calculations expire after 90 days.
        """
        return cast(
            "Transaction",
            await self._request_async(
                "post",
                "/v1/tax/transactions/create_from_calculation",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create_reversal(
        self,
        params: "TransactionCreateReversalParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Transaction":
        """
        Partially or fully reverses a previously created Transaction.
        """
        return cast(
            "Transaction",
            self._request(
                "post",
                "/v1/tax/transactions/create_reversal",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_reversal_async(
        self,
        params: "TransactionCreateReversalParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Transaction":
        """
        Partially or fully reverses a previously created Transaction.
        """
        return cast(
            "Transaction",
            await self._request_async(
                "post",
                "/v1/tax/transactions/create_reversal",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def serialize_batch_create_reversal(
        self,
        params: Optional["TransactionCreateReversalParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> str:
        """
        Serializes a Transaction create_reversal request into a batch job JSONL line.
        """
        item_id = str(uuid4())
        stripe_version = (
            options.get("stripe_version") if options else None
        ) or _ApiVersion.CURRENT
        context = options.get("stripe_context") if options else None
        item = {
            "id": item_id,
            "params": params,
            "stripe_version": stripe_version,
        }
        if context is not None:
            item["context"] = context
        return json.dumps(item)
