# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.money_management._spending_mandate_cancel_params import (
        SpendingMandateCancelParams,
    )
    from stripe.params.v2.money_management._spending_mandate_list_params import (
        SpendingMandateListParams,
    )
    from stripe.params.v2.money_management._spending_mandate_retrieve_params import (
        SpendingMandateRetrieveParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.money_management._spending_mandate import SpendingMandate


class SpendingMandateService(StripeService):
    def list(
        self,
        params: Optional["SpendingMandateListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[SpendingMandate]":
        """
        Returns a list of SpendingMandates.
        """
        return cast(
            "ListObject[SpendingMandate]",
            self._request(
                "get",
                "/v2/money_management/spending_mandates",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["SpendingMandateListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[SpendingMandate]":
        """
        Returns a list of SpendingMandates.
        """
        return cast(
            "ListObject[SpendingMandate]",
            await self._request_async(
                "get",
                "/v2/money_management/spending_mandates",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        /,
        params: Optional["SpendingMandateRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "SpendingMandate":
        """
        Retrieves the details of an existing SpendingMandate.
        """
        return cast(
            "SpendingMandate",
            self._request(
                "get",
                "/v2/money_management/spending_mandates/{id}".format(
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
        /,
        params: Optional["SpendingMandateRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "SpendingMandate":
        """
        Retrieves the details of an existing SpendingMandate.
        """
        return cast(
            "SpendingMandate",
            await self._request_async(
                "get",
                "/v2/money_management/spending_mandates/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def cancel(
        self,
        id: str,
        /,
        params: Optional["SpendingMandateCancelParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "SpendingMandate":
        """
        Cancels an active SpendingMandate.
        """
        return cast(
            "SpendingMandate",
            self._request(
                "post",
                "/v2/money_management/spending_mandates/{id}/cancel".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def cancel_async(
        self,
        id: str,
        /,
        params: Optional["SpendingMandateCancelParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "SpendingMandate":
        """
        Cancels an active SpendingMandate.
        """
        return cast(
            "SpendingMandate",
            await self._request_async(
                "post",
                "/v2/money_management/spending_mandates/{id}/cancel".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
