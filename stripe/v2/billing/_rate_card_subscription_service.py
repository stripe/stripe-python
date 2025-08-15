# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2._list_object import ListObject
from stripe.v2.billing._rate_card_subscription import RateCardSubscription
from typing import Dict, Optional, cast
from typing_extensions import Literal, NotRequired, TypedDict


class RateCardSubscriptionService(StripeService):
    class CancelParams(TypedDict):
        pass

    class CreateParams(TypedDict):
        billing_cadence: str
        """
        The ID of the billing Cadence.
        """
        metadata: NotRequired[Dict[str, str]]
        """
        Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
        """
        rate_card: str
        """
        The ID of the RateCard.
        """
        rate_card_version: NotRequired[str]
        """
        The ID of the RateCardVersion. If not specified, defaults to the "live_version" of the RateCard at the time of creation.
        """

    class ListParams(TypedDict):
        billing_cadence: NotRequired[str]
        """
        Optionally filter by a BillingCadence. Mutually exclusive with `payers`, `rate_card`, and `rate_card_version`.
        """
        limit: NotRequired[int]
        """
        The page size limit, if not provided the default is 20.
        """
        payer: NotRequired["RateCardSubscriptionService.ListParamsPayer"]
        """
        Optionally filter by the payer associated with Cadences which the RateCardSubscriptions are subscribed to.
        Mutually exclusive with `billing_cadence`, `rate_card`, and `rate_card_version`.
        """
        rate_card: NotRequired[str]
        """
        Optionally filter by a RateCard. Mutually exclusive with `billing_cadence`, `payers`, and `rate_card_version`.
        """
        rate_card_version: NotRequired[str]
        """
        Optionally filter by a RateCard version. Mutually exclusive with `billing_cadence`, `payers`, and `rate_card`.
        """
        servicing_status: NotRequired[
            Literal["active", "canceled", "paused", "pending"]
        ]
        """
        Optionally filter by servicing status.
        """

    class ListParamsPayer(TypedDict):
        customer: NotRequired[str]
        """
        The ID of the Customer object. If provided, only RateCardSubscriptions that are subscribed on the Cadences with the specified Payer will be returned.
        """
        type: Literal["customer"]
        """
        A string identifying the type of the payer. Currently the only supported value is `customer`.
        """

    class RetrieveParams(TypedDict):
        pass

    class UpdateParams(TypedDict):
        metadata: NotRequired[Dict[str, Optional[str]]]
        """
        Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
        """

    def list(
        self,
        params: "RateCardSubscriptionService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[RateCardSubscription]:
        """
        List all RateCardSubscription objects.
        """
        return cast(
            ListObject[RateCardSubscription],
            self._request(
                "get",
                "/v2/billing/rate_card_subscriptions",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "RateCardSubscriptionService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[RateCardSubscription]:
        """
        List all RateCardSubscription objects.
        """
        return cast(
            ListObject[RateCardSubscription],
            await self._request_async(
                "get",
                "/v2/billing/rate_card_subscriptions",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "RateCardSubscriptionService.CreateParams",
        options: RequestOptions = {},
    ) -> RateCardSubscription:
        """
        Create a RateCardSubscription to bill a RateCard on a specified billing Cadence.
        """
        return cast(
            RateCardSubscription,
            self._request(
                "post",
                "/v2/billing/rate_card_subscriptions",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "RateCardSubscriptionService.CreateParams",
        options: RequestOptions = {},
    ) -> RateCardSubscription:
        """
        Create a RateCardSubscription to bill a RateCard on a specified billing Cadence.
        """
        return cast(
            RateCardSubscription,
            await self._request_async(
                "post",
                "/v2/billing/rate_card_subscriptions",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: "RateCardSubscriptionService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> RateCardSubscription:
        """
        Retrieve a RateCardSubscription by ID.
        """
        return cast(
            RateCardSubscription,
            self._request(
                "get",
                "/v2/billing/rate_card_subscriptions/{id}".format(
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
        params: "RateCardSubscriptionService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> RateCardSubscription:
        """
        Retrieve a RateCardSubscription by ID.
        """
        return cast(
            RateCardSubscription,
            await self._request_async(
                "get",
                "/v2/billing/rate_card_subscriptions/{id}".format(
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
        params: "RateCardSubscriptionService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> RateCardSubscription:
        """
        Update fields on an existing, active RateCardSubscription.
        """
        return cast(
            RateCardSubscription,
            self._request(
                "post",
                "/v2/billing/rate_card_subscriptions/{id}".format(
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
        params: "RateCardSubscriptionService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> RateCardSubscription:
        """
        Update fields on an existing, active RateCardSubscription.
        """
        return cast(
            RateCardSubscription,
            await self._request_async(
                "post",
                "/v2/billing/rate_card_subscriptions/{id}".format(
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
        params: "RateCardSubscriptionService.CancelParams" = {},
        options: RequestOptions = {},
    ) -> RateCardSubscription:
        """
        Cancel an existing, active RateCardSubscription.
        """
        return cast(
            RateCardSubscription,
            self._request(
                "post",
                "/v2/billing/rate_card_subscriptions/{id}/cancel".format(
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
        params: "RateCardSubscriptionService.CancelParams" = {},
        options: RequestOptions = {},
    ) -> RateCardSubscription:
        """
        Cancel an existing, active RateCardSubscription.
        """
        return cast(
            RateCardSubscription,
            await self._request_async(
                "post",
                "/v2/billing/rate_card_subscriptions/{id}/cancel".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
