# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._list_object import ListObject
    from stripe._request_options import RequestOptions
    from stripe._source_transaction import SourceTransaction
    from stripe.params._source_transaction_list_params import (
        SourceTransactionListParams,
    )


class SourceTransactionService(StripeService):
    def list(
        self,
        id: str,
        /,
        params: Optional["SourceTransactionListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[SourceTransaction]":
        """
        List source transactions for a given source.
        """
        return cast(
            "ListObject[SourceTransaction]",
            self._request(
                "get",
                "/v1/sources/{id}/source_transactions".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        id: str,
        /,
        params: Optional["SourceTransactionListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[SourceTransaction]":
        """
        List source transactions for a given source.
        """
        return cast(
            "ListObject[SourceTransaction]",
            await self._request_async(
                "get",
                "/v1/sources/{id}/source_transactions".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
