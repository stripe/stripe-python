# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.billing.pricing_plan_subscriptions._component_retrieve_params import (
        ComponentRetrieveParams,
    )
    from stripe.v2.billing._pricing_plan_subscription_components import (
        PricingPlanSubscriptionComponents,
    )


class ComponentService(StripeService):
    def retrieve(
        self,
        id: str,
        params: Optional["ComponentRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PricingPlanSubscriptionComponents":
        """
        Retrieve a Pricing Plan Subscription's components.
        """
        return cast(
            "PricingPlanSubscriptionComponents",
            self._request(
                "get",
                "/v2/billing/pricing_plan_subscriptions/{id}/components".format(
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
        params: Optional["ComponentRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PricingPlanSubscriptionComponents":
        """
        Retrieve a Pricing Plan Subscription's components.
        """
        return cast(
            "PricingPlanSubscriptionComponents",
            await self._request_async(
                "get",
                "/v2/billing/pricing_plan_subscriptions/{id}/components".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
