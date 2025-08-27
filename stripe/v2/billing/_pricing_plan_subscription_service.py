# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2._list_object import ListObject
from stripe.v2.billing._pricing_plan_subscription import (
    PricingPlanSubscription,
)
from typing import cast
from typing_extensions import Literal, NotRequired, TypedDict


class PricingPlanSubscriptionService(StripeService):
    class ListParams(TypedDict):
        billing_cadence: NotRequired[str]
        """
        Filter by Billing Cadence ID. Mutually exclusive with `payer`, `pricing_plan`, and `pricing_plan_version`.
        """
        limit: NotRequired[int]
        """
        Optionally set the maximum number of results per page. Defaults to 20.
        """
        payer: NotRequired["PricingPlanSubscriptionService.ListParamsPayer"]
        """
        Filter by payer. Mutually exclusive with `billing_cadence`, `pricing_plan`, and `pricing_plan_version`.
        """
        pricing_plan: NotRequired[str]
        """
        Filter by PricingPlan ID. Mutually exlcusive with `billing_cadence`, `payer`, and `pricing_plan_version`.
        """
        pricing_plan_version: NotRequired[str]
        """
        Filter by Pricing Plan Version ID. Mutually exlcusive with `billing_cadence`, `payer`, and `pricing_plan`.
        """
        servicing_status: NotRequired[
            Literal["active", "canceled", "paused", "pending"]
        ]
        """
        Filter by servicing status.
        """

    class ListParamsPayer(TypedDict):
        customer: NotRequired[str]
        """
        The ID of the Customer object. If provided, only Pricing Plan Subscriptions that are subscribed on the cadences with the specified payer will be returned.
        """
        type: Literal["customer"]
        """
        A string identifying the type of the payer. Currently the only supported value is `customer`.
        """

    class RetrieveParams(TypedDict):
        pass

    def list(
        self,
        params: "PricingPlanSubscriptionService.ListParams" = {},
        options: RequestOptions = {},
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
        params: "PricingPlanSubscriptionService.ListParams" = {},
        options: RequestOptions = {},
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
        params: "PricingPlanSubscriptionService.RetrieveParams" = {},
        options: RequestOptions = {},
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
        params: "PricingPlanSubscriptionService.RetrieveParams" = {},
        options: RequestOptions = {},
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
