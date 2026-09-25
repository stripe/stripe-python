# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.money_management._earned_credit_list_params import (
        EarnedCreditListParams,
    )
    from stripe.params.v2.money_management._earned_credit_retrieve_params import (
        EarnedCreditRetrieveParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.money_management._earned_credit import EarnedCredit


class EarnedCreditService(StripeService):
    def list(
        self,
        params: Optional["EarnedCreditListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[EarnedCredit]":
        """
        Returns a list of EarnedCredits.
        """
        return cast(
            "ListObject[EarnedCredit]",
            self._request(
                "get",
                "/v2/money_management/earned_credits",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["EarnedCreditListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[EarnedCredit]":
        """
        Returns a list of EarnedCredits.
        """
        return cast(
            "ListObject[EarnedCredit]",
            await self._request_async(
                "get",
                "/v2/money_management/earned_credits",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        /,
        params: Optional["EarnedCreditRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "EarnedCredit":
        """
        Retrieves an EarnedCredit.
        """
        return cast(
            "EarnedCredit",
            self._request(
                "get",
                "/v2/money_management/earned_credits/{id}".format(
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
        params: Optional["EarnedCreditRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "EarnedCredit":
        """
        Retrieves an EarnedCredit.
        """
        return cast(
            "EarnedCredit",
            await self._request_async(
                "get",
                "/v2/money_management/earned_credits/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
