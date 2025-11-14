# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.money_management._received_credit_list_params import (
        ReceivedCreditListParams,
    )
    from stripe.params.v2.money_management._received_credit_retrieve_params import (
        ReceivedCreditRetrieveParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.money_management._received_credit import ReceivedCredit


class ReceivedCreditService(StripeService):
    def list(
        self,
        params: Optional["ReceivedCreditListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[ReceivedCredit]":
        """
        Retrieves a list of ReceivedCredits.
        """
        return cast(
            "ListObject[ReceivedCredit]",
            self._request(
                "get",
                "/v2/money_management/received_credits",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["ReceivedCreditListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[ReceivedCredit]":
        """
        Retrieves a list of ReceivedCredits.
        """
        return cast(
            "ListObject[ReceivedCredit]",
            await self._request_async(
                "get",
                "/v2/money_management/received_credits",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["ReceivedCreditRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ReceivedCredit":
        """
        Retrieve a ReceivedCredit by ID.
        """
        return cast(
            "ReceivedCredit",
            self._request(
                "get",
                "/v2/money_management/received_credits/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: Optional["ReceivedCreditRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ReceivedCredit":
        """
        Retrieve a ReceivedCredit by ID.
        """
        return cast(
            "ReceivedCredit",
            await self._request_async(
                "get",
                "/v2/money_management/received_credits/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
