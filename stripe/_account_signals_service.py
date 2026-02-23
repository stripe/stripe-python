# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._account_signals import AccountSignals
    from stripe._request_options import RequestOptions
    from stripe.params._account_signals_retrieve_params import (
        AccountSignalsRetrieveParams,
    )


class AccountSignalsService(StripeService):
    def retrieve(
        self,
        account_id: str,
        params: Optional["AccountSignalsRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "AccountSignals":
        """
        Retrieves the account's Signal objects
        """
        return cast(
            "AccountSignals",
            self._request(
                "get",
                "/v1/accounts/{account_id}/signals".format(
                    account_id=sanitize_id(account_id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        account_id: str,
        params: Optional["AccountSignalsRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "AccountSignals":
        """
        Retrieves the account's Signal objects
        """
        return cast(
            "AccountSignals",
            await self._request_async(
                "get",
                "/v1/accounts/{account_id}/signals".format(
                    account_id=sanitize_id(account_id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
