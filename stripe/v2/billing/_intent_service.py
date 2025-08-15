# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2._list_object import ListObject
from stripe.v2.billing._intent import Intent
from typing import Dict, List, cast
from typing_extensions import Literal, NotRequired, TypedDict


class IntentService(StripeService):
    class CancelParams(TypedDict):
        pass

    class CommitParams(TypedDict):
        payment_intent: NotRequired[str]
        """
        ID of the PaymentIntent associated with this commit.
        """

    class CreateParams(TypedDict):
        actions: List["IntentService.CreateParamsAction"]
        """
        Actions to be performed by this BillingIntent.
        """
        currency: str
        """
        Three-letter ISO currency code, in lowercase.
        """
        effective_at: Literal[
            "current_billing_period_start", "on_commit", "on_reserve"
        ]
        """
        When the BillingIntent will take effect.
        """
        cadence: NotRequired[str]
        """
        ID of an existing Cadence to use.
        """

    class CreateParamsAction(TypedDict):
        type: Literal["apply", "deactivate", "modify", "remove", "subscribe"]
        """
        Type of the BillingIntentAction.
        """
        apply: NotRequired["IntentService.CreateParamsActionApply"]
        """
        Details for an apply action.
        """
        deactivate: NotRequired["IntentService.CreateParamsActionDeactivate"]
        """
        Details for a deactivate action.
        """
        modify: NotRequired["IntentService.CreateParamsActionModify"]
        """
        Details for a modify action.
        """
        remove: NotRequired["IntentService.CreateParamsActionRemove"]
        """
        Details for a remove action.
        """
        subscribe: NotRequired["IntentService.CreateParamsActionSubscribe"]
        """
        Details for a subscribe action.
        """

    class CreateParamsActionApply(TypedDict):
        type: Literal["invoice_discount_rule"]
        """
        Type of the apply action details.
        """
        invoice_discount_rule: NotRequired[
            "IntentService.CreateParamsActionApplyInvoiceDiscountRule"
        ]
        """
        Details for applying a discount rule to future invoices.
        """

    class CreateParamsActionApplyInvoiceDiscountRule(TypedDict):
        applies_to: Literal["cadence"]
        """
        The entity that the discount rule applies to, for example, the cadence.
        """
        type: Literal["percent_off"]
        """
        Type of the discount rule.
        """
        percent_off: NotRequired[
            "IntentService.CreateParamsActionApplyInvoiceDiscountRulePercentOff"
        ]
        """
        Configuration for percentage off discount.
        """

    class CreateParamsActionApplyInvoiceDiscountRulePercentOff(TypedDict):
        maximum_applications: "IntentService.CreateParamsActionApplyInvoiceDiscountRulePercentOffMaximumApplications"
        """
        The maximum number of times this discount can be applied for this cadence.
        """
        percent_off: str
        """
        Percent that will be taken off of the amount. For example, percent_off of 50.0 will make $100 amount $50 instead.
        """

    class CreateParamsActionApplyInvoiceDiscountRulePercentOffMaximumApplications(
        TypedDict,
    ):
        type: Literal["indefinite"]
        """
        The type of maximum applications configuration.
        """

    class CreateParamsActionDeactivate(TypedDict):
        pricing_plan_subscription_details: "IntentService.CreateParamsActionDeactivatePricingPlanSubscriptionDetails"
        """
        Details for deactivating a pricing plan subscription.
        """
        proration_behavior: Literal["always_invoice", "none"]
        """
        Behavior for handling prorations.
        """
        type: Literal["pricing_plan_subscription_details"]
        """
        Type of the action details.
        """

    class CreateParamsActionDeactivatePricingPlanSubscriptionDetails(
        TypedDict
    ):
        pricing_plan_subscription: str
        """
        ID of the pricing plan subscription to deactivate.
        """

    class CreateParamsActionModify(TypedDict):
        pricing_plan_subscription_details: "IntentService.CreateParamsActionModifyPricingPlanSubscriptionDetails"
        """
        Details for modifying a pricing plan subscription.
        """
        proration_behavior: Literal["always_invoice", "none"]
        """
        Behavior for handling prorations.
        """
        type: Literal["pricing_plan_subscription_details"]
        """
        Type of the action details.
        """

    class CreateParamsActionModifyPricingPlanSubscriptionDetails(TypedDict):
        component_configurations: NotRequired[
            List[
                "IntentService.CreateParamsActionModifyPricingPlanSubscriptionDetailsComponentConfiguration"
            ]
        ]
        """
        New configurations for the components of the pricing plan.
        """
        new_pricing_plan: NotRequired[str]
        """
        ID of the new pricing plan, if changing plans.
        """
        new_pricing_plan_version: NotRequired[str]
        """
        Version of the pricing plan to use.
        """
        pricing_plan_subscription: str
        """
        ID of the pricing plan subscription to modify.
        """

    class CreateParamsActionModifyPricingPlanSubscriptionDetailsComponentConfiguration(
        TypedDict,
    ):
        quantity: NotRequired[int]
        """
        Quantity of the component to be used.
        """
        lookup_key: NotRequired[str]
        """
        Lookup key for the pricing plan component.
        """
        pricing_plan_component: NotRequired[str]
        """
        ID of the pricing plan component.
        """

    class CreateParamsActionRemove(TypedDict):
        type: Literal["invoice_discount_rule"]
        """
        Type of the remove action.
        """
        invoice_discount_rule: NotRequired[str]
        """
        The ID of the discount rule to remove for future invoices.
        """

    class CreateParamsActionSubscribe(TypedDict):
        proration_behavior: Literal["always_invoice", "none"]
        """
        Behavior for handling prorations.
        """
        type: Literal["pricing_plan_subscription_details"]
        """
        Type of the action details.
        """
        pricing_plan_subscription_details: NotRequired[
            "IntentService.CreateParamsActionSubscribePricingPlanSubscriptionDetails"
        ]
        """
        Details for subscribing to a pricing plan.
        """

    class CreateParamsActionSubscribePricingPlanSubscriptionDetails(TypedDict):
        component_configurations: NotRequired[
            List[
                "IntentService.CreateParamsActionSubscribePricingPlanSubscriptionDetailsComponentConfiguration"
            ]
        ]
        """
        Configurations for the components of the pricing plan.
        """
        metadata: NotRequired[Dict[str, str]]
        """
        Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
        """
        pricing_plan: str
        """
        ID of the pricing plan to subscribe to.
        """
        pricing_plan_version: str
        """
        Version of the pricing plan to use.
        """

    class CreateParamsActionSubscribePricingPlanSubscriptionDetailsComponentConfiguration(
        TypedDict,
    ):
        quantity: NotRequired[int]
        """
        Quantity of the component to be used.
        """
        lookup_key: NotRequired[str]
        """
        Lookup key for the pricing plan component.
        """
        pricing_plan_component: NotRequired[str]
        """
        ID of the pricing plan component.
        """

    class ListParams(TypedDict):
        limit: NotRequired[int]
        """
        Optionally set the maximum number of results per page. Defaults to 10.
        """

    class ReleaseReservationParams(TypedDict):
        pass

    class ReserveParams(TypedDict):
        pass

    class RetrieveParams(TypedDict):
        pass

    def list(
        self,
        params: "IntentService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[Intent]:
        """
        List BillingIntents.
        """
        return cast(
            ListObject[Intent],
            self._request(
                "get",
                "/v2/billing/intents",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "IntentService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[Intent]:
        """
        List BillingIntents.
        """
        return cast(
            ListObject[Intent],
            await self._request_async(
                "get",
                "/v2/billing/intents",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "IntentService.CreateParams",
        options: RequestOptions = {},
    ) -> Intent:
        """
        Create a BillingIntent.
        """
        return cast(
            Intent,
            self._request(
                "post",
                "/v2/billing/intents",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "IntentService.CreateParams",
        options: RequestOptions = {},
    ) -> Intent:
        """
        Create a BillingIntent.
        """
        return cast(
            Intent,
            await self._request_async(
                "post",
                "/v2/billing/intents",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: "IntentService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> Intent:
        """
        Retrieve a BillingIntent.
        """
        return cast(
            Intent,
            self._request(
                "get",
                "/v2/billing/intents/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: "IntentService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> Intent:
        """
        Retrieve a BillingIntent.
        """
        return cast(
            Intent,
            await self._request_async(
                "get",
                "/v2/billing/intents/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def cancel(
        self,
        id: str,
        params: "IntentService.CancelParams" = {},
        options: RequestOptions = {},
    ) -> Intent:
        """
        Cancel a BillingIntent.
        """
        return cast(
            Intent,
            self._request(
                "post",
                "/v2/billing/intents/{id}/cancel".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def cancel_async(
        self,
        id: str,
        params: "IntentService.CancelParams" = {},
        options: RequestOptions = {},
    ) -> Intent:
        """
        Cancel a BillingIntent.
        """
        return cast(
            Intent,
            await self._request_async(
                "post",
                "/v2/billing/intents/{id}/cancel".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def commit(
        self,
        id: str,
        params: "IntentService.CommitParams" = {},
        options: RequestOptions = {},
    ) -> Intent:
        """
        Commit a BillingIntent.
        """
        return cast(
            Intent,
            self._request(
                "post",
                "/v2/billing/intents/{id}/commit".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def commit_async(
        self,
        id: str,
        params: "IntentService.CommitParams" = {},
        options: RequestOptions = {},
    ) -> Intent:
        """
        Commit a BillingIntent.
        """
        return cast(
            Intent,
            await self._request_async(
                "post",
                "/v2/billing/intents/{id}/commit".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def release_reservation(
        self,
        id: str,
        params: "IntentService.ReleaseReservationParams" = {},
        options: RequestOptions = {},
    ) -> Intent:
        """
        Release a BillingIntent.
        """
        return cast(
            Intent,
            self._request(
                "post",
                "/v2/billing/intents/{id}/release_reservation".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def release_reservation_async(
        self,
        id: str,
        params: "IntentService.ReleaseReservationParams" = {},
        options: RequestOptions = {},
    ) -> Intent:
        """
        Release a BillingIntent.
        """
        return cast(
            Intent,
            await self._request_async(
                "post",
                "/v2/billing/intents/{id}/release_reservation".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def reserve(
        self,
        id: str,
        params: "IntentService.ReserveParams" = {},
        options: RequestOptions = {},
    ) -> Intent:
        """
        Reserve a BillingIntent.
        """
        return cast(
            Intent,
            self._request(
                "post",
                "/v2/billing/intents/{id}/reserve".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def reserve_async(
        self,
        id: str,
        params: "IntentService.ReserveParams" = {},
        options: RequestOptions = {},
    ) -> Intent:
        """
        Reserve a BillingIntent.
        """
        return cast(
            Intent,
            await self._request_async(
                "post",
                "/v2/billing/intents/{id}/reserve".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
