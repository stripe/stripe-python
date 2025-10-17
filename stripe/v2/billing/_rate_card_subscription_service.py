# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.billing._rate_card_subscription_cancel_params import (
        RateCardSubscriptionCancelParams,
    )
    from stripe.params.v2.billing._rate_card_subscription_create_params import (
        RateCardSubscriptionCreateParams,
    )
    from stripe.params.v2.billing._rate_card_subscription_list_params import (
        RateCardSubscriptionListParams,
    )
    from stripe.params.v2.billing._rate_card_subscription_retrieve_params import (
        RateCardSubscriptionRetrieveParams,
    )
    from stripe.params.v2.billing._rate_card_subscription_update_params import (
        RateCardSubscriptionUpdateParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.billing._rate_card_subscription import RateCardSubscription


class RateCardSubscriptionService(StripeService):
    def list(
        self,
        params: Optional["RateCardSubscriptionListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[RateCardSubscription]":
        """
        List all Rate Card Subscription objects.
        """
        return cast(
            "ListObject[RateCardSubscription]",
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
        params: Optional["RateCardSubscriptionListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[RateCardSubscription]":
        """
        List all Rate Card Subscription objects.
        """
        return cast(
            "ListObject[RateCardSubscription]",
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
        params: "RateCardSubscriptionCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "RateCardSubscription":
        """
        Create a Rate Card Subscription to bill a Rate Card on a specified Billing Cadence.
        """
        return cast(
            "RateCardSubscription",
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
        params: "RateCardSubscriptionCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "RateCardSubscription":
        """
        Create a Rate Card Subscription to bill a Rate Card on a specified Billing Cadence.
        """
        return cast(
            "RateCardSubscription",
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
        params: Optional["RateCardSubscriptionRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RateCardSubscription":
        """
        Retrieve a Rate Card Subscription by ID.
        """
        return cast(
            "RateCardSubscription",
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
        params: Optional["RateCardSubscriptionRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RateCardSubscription":
        """
        Retrieve a Rate Card Subscription by ID.
        """
        return cast(
            "RateCardSubscription",
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
        params: Optional["RateCardSubscriptionUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RateCardSubscription":
        """
        Update fields on an existing, active Rate Card Subscription.
        """
        return cast(
            "RateCardSubscription",
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
        params: Optional["RateCardSubscriptionUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RateCardSubscription":
        """
        Update fields on an existing, active Rate Card Subscription.
        """
        return cast(
            "RateCardSubscription",
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
        params: Optional["RateCardSubscriptionCancelParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RateCardSubscription":
        """
        Cancel an existing, active Rate Card Subscription.
        """
        return cast(
            "RateCardSubscription",
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
        params: Optional["RateCardSubscriptionCancelParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RateCardSubscription":
        """
        Cancel an existing, active Rate Card Subscription.
        """
        return cast(
            "RateCardSubscription",
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
