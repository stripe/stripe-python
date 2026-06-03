# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.signals._account_signal_list_params import (
        AccountSignalListParams,
    )
    from stripe.params.v2.signals._account_signal_retrieve_params import (
        AccountSignalRetrieveParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.signals._account_signal import AccountSignal


class AccountSignalService(StripeService):
    def list(
        self,
        params: "AccountSignalListParams",
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[AccountSignal]":
        """
        Lists AccountSignals for a given account or customer, filtered by signal type.
        """
        return cast(
            "ListObject[AccountSignal]",
            self._request(
                "get",
                "/v2/signals/account_signals",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "AccountSignalListParams",
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[AccountSignal]":
        """
        Lists AccountSignals for a given account or customer, filtered by signal type.
        """
        return cast(
            "ListObject[AccountSignal]",
            await self._request_async(
                "get",
                "/v2/signals/account_signals",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["AccountSignalRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "AccountSignal":
        """
        Retrieves an AccountSignal by its ID.
        """
        return cast(
            "AccountSignal",
            self._request(
                "get",
                "/v2/signals/account_signals/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: Optional["AccountSignalRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "AccountSignal":
        """
        Retrieves an AccountSignal by its ID.
        """
        return cast(
            "AccountSignal",
            await self._request_async(
                "get",
                "/v2/signals/account_signals/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
