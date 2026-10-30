# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.money_management._funding_intent_cancel_params import (
        FundingIntentCancelParams,
    )
    from stripe.params.v2.money_management._funding_intent_confirm_params import (
        FundingIntentConfirmParams,
    )
    from stripe.params.v2.money_management._funding_intent_create_params import (
        FundingIntentCreateParams,
    )
    from stripe.params.v2.money_management._funding_intent_list_params import (
        FundingIntentListParams,
    )
    from stripe.params.v2.money_management._funding_intent_retrieve_params import (
        FundingIntentRetrieveParams,
    )
    from stripe.params.v2.money_management._funding_intent_update_params import (
        FundingIntentUpdateParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.money_management._funding_intent import FundingIntent


class FundingIntentService(StripeService):
    def list(
        self,
        params: Optional["FundingIntentListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[FundingIntent]":
        """
        Lists FundingIntents.
        """
        return cast(
            "ListObject[FundingIntent]",
            self._request(
                "get",
                "/v2/money_management/funding_intents",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["FundingIntentListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[FundingIntent]":
        """
        Lists FundingIntents.
        """
        return cast(
            "ListObject[FundingIntent]",
            await self._request_async(
                "get",
                "/v2/money_management/funding_intents",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "FundingIntentCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "FundingIntent":
        """
        Creates a FundingIntent that adds funds to a FinancialAccount.
        """
        return cast(
            "FundingIntent",
            self._request(
                "post",
                "/v2/money_management/funding_intents",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "FundingIntentCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "FundingIntent":
        """
        Creates a FundingIntent that adds funds to a FinancialAccount.
        """
        return cast(
            "FundingIntent",
            await self._request_async(
                "post",
                "/v2/money_management/funding_intents",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        /,
        params: Optional["FundingIntentRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "FundingIntent":
        """
        Retrieves a FundingIntent by ID.
        """
        return cast(
            "FundingIntent",
            self._request(
                "get",
                "/v2/money_management/funding_intents/{id}".format(
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
        params: Optional["FundingIntentRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "FundingIntent":
        """
        Retrieves a FundingIntent by ID.
        """
        return cast(
            "FundingIntent",
            await self._request_async(
                "get",
                "/v2/money_management/funding_intents/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        id: str,
        /,
        params: Optional["FundingIntentUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "FundingIntent":
        """
        Updates the mutable details of a FundingIntent.
        """
        return cast(
            "FundingIntent",
            self._request(
                "post",
                "/v2/money_management/funding_intents/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        id: str,
        /,
        params: Optional["FundingIntentUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "FundingIntent":
        """
        Updates the mutable details of a FundingIntent.
        """
        return cast(
            "FundingIntent",
            await self._request_async(
                "post",
                "/v2/money_management/funding_intents/{id}".format(
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
        params: Optional["FundingIntentCancelParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "FundingIntent":
        """
        Cancels a FundingIntent that can still be canceled.
        """
        return cast(
            "FundingIntent",
            self._request(
                "post",
                "/v2/money_management/funding_intents/{id}/cancel".format(
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
        params: Optional["FundingIntentCancelParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "FundingIntent":
        """
        Cancels a FundingIntent that can still be canceled.
        """
        return cast(
            "FundingIntent",
            await self._request_async(
                "post",
                "/v2/money_management/funding_intents/{id}/cancel".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def confirm(
        self,
        id: str,
        /,
        params: Optional["FundingIntentConfirmParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "FundingIntent":
        """
        Confirms a FundingIntent that is ready for processing.
        """
        return cast(
            "FundingIntent",
            self._request(
                "post",
                "/v2/money_management/funding_intents/{id}/confirm".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def confirm_async(
        self,
        id: str,
        /,
        params: Optional["FundingIntentConfirmParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "FundingIntent":
        """
        Confirms a FundingIntent that is ready for processing.
        """
        return cast(
            "FundingIntent",
            await self._request_async(
                "post",
                "/v2/money_management/funding_intents/{id}/confirm".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
