# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2._list_object import ListObject
from stripe.v2.billing._pricing_plan_subscription import (
    PricingPlanSubscription,
)
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.v2.billing._pricing_plan_subscription_list_params import (
        PricingPlanSubscriptionListParams,
    )
    from stripe.params.v2.billing._pricing_plan_subscription_retrieve_params import (
        PricingPlanSubscriptionRetrieveParams,
    )
    from stripe.params.v2.billing._pricing_plan_subscription_update_params import (
        PricingPlanSubscriptionUpdateParams,
    )


class PricingPlanSubscriptionService(StripeService):
    def list(
        self,
        params: Optional["PricingPlanSubscriptionListParams"] = None,
        options: Optional[RequestOptions] = None,
    ) -> ListObject[PricingPlanSubscription]:
        """
        List all Pricing Plan Subscription objects.
        """
        return cast(
            ListObject[PricingPlanSubscription],
            self._request(
                "get",
                "/v2/billing/pricing_plan_subscriptions",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["PricingPlanSubscriptionListParams"] = None,
        options: Optional[RequestOptions] = None,
    ) -> ListObject[PricingPlanSubscription]:
        """
        List all Pricing Plan Subscription objects.
        """
        return cast(
            ListObject[PricingPlanSubscription],
            await self._request_async(
                "get",
                "/v2/billing/pricing_plan_subscriptions",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["PricingPlanSubscriptionRetrieveParams"] = None,
        options: Optional[RequestOptions] = None,
    ) -> PricingPlanSubscription:
        """
        Retrieve a Pricing Plan Subscription object.
        """
        return cast(
            PricingPlanSubscription,
            self._request(
                "get",
                "/v2/billing/pricing_plan_subscriptions/{id}".format(
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
        params: Optional["PricingPlanSubscriptionRetrieveParams"] = None,
        options: Optional[RequestOptions] = None,
    ) -> PricingPlanSubscription:
        """
        Retrieve a Pricing Plan Subscription object.
        """
        return cast(
            PricingPlanSubscription,
            await self._request_async(
                "get",
                "/v2/billing/pricing_plan_subscriptions/{id}".format(
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
        params: Optional["PricingPlanSubscriptionUpdateParams"] = None,
        options: Optional[RequestOptions] = None,
    ) -> PricingPlanSubscription:
        """
        Update a Pricing Plan Subscription object.
        """
        return cast(
            PricingPlanSubscription,
            self._request(
                "post",
                "/v2/billing/pricing_plan_subscriptions/{id}".format(
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
        params: Optional["PricingPlanSubscriptionUpdateParams"] = None,
        options: Optional[RequestOptions] = None,
    ) -> PricingPlanSubscription:
        """
        Update a Pricing Plan Subscription object.
        """
        return cast(
            PricingPlanSubscription,
            await self._request_async(
                "post",
                "/v2/billing/pricing_plan_subscriptions/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
