# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.money_management._debit_dispute_create_params import (
        DebitDisputeCreateParams,
    )
    from stripe.params.v2.money_management._debit_dispute_list_params import (
        DebitDisputeListParams,
    )
    from stripe.params.v2.money_management._debit_dispute_retrieve_params import (
        DebitDisputeRetrieveParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.money_management._debit_dispute import DebitDispute


class DebitDisputeService(StripeService):
    def list(
        self,
        params: Optional["DebitDisputeListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[DebitDispute]":
        """
        Retrieves a list of DebitDisputes.
        """
        return cast(
            "ListObject[DebitDispute]",
            self._request(
                "get",
                "/v2/money_management/debit_disputes",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["DebitDisputeListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[DebitDispute]":
        """
        Retrieves a list of DebitDisputes.
        """
        return cast(
            "ListObject[DebitDispute]",
            await self._request_async(
                "get",
                "/v2/money_management/debit_disputes",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "DebitDisputeCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "DebitDispute":
        """
        Creates a new DebitDispute for a ReceivedDebit.
        """
        return cast(
            "DebitDispute",
            self._request(
                "post",
                "/v2/money_management/debit_disputes",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "DebitDisputeCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "DebitDispute":
        """
        Creates a new DebitDispute for a ReceivedDebit.
        """
        return cast(
            "DebitDispute",
            await self._request_async(
                "post",
                "/v2/money_management/debit_disputes",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["DebitDisputeRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "DebitDispute":
        """
        Retrieves the details of an existing DebitDispute.
        """
        return cast(
            "DebitDispute",
            self._request(
                "get",
                "/v2/money_management/debit_disputes/{id}".format(
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
        params: Optional["DebitDisputeRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "DebitDispute":
        """
        Retrieves the details of an existing DebitDispute.
        """
        return cast(
            "DebitDispute",
            await self._request_async(
                "get",
                "/v2/money_management/debit_disputes/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
