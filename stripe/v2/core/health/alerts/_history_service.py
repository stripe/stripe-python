# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.core.health.alerts._history_list_params import (
        HistoryListParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.core.health._alert_history_entry import AlertHistoryEntry


class HistoryService(StripeService):
    def list(
        self,
        id: str,
        params: Optional["HistoryListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[AlertHistoryEntry]":
        """
        Retrieves a list of alert history entries for a health alert.
        """
        return cast(
            "ListObject[AlertHistoryEntry]",
            self._request(
                "get",
                "/v2/core/health/alerts/{id}/history".format(
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
        params: Optional["HistoryListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[AlertHistoryEntry]":
        """
        Retrieves a list of alert history entries for a health alert.
        """
        return cast(
            "ListObject[AlertHistoryEntry]",
            await self._request_async(
                "get",
                "/v2/core/health/alerts/{id}/history".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
