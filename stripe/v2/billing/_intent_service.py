# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2._list_object import ListObject
from stripe.v2.billing._intent import Intent
from stripe.v2.billing.intents._action_service import ActionService
from typing import Dict, List, cast
from typing_extensions import Literal, NotRequired, TypedDict


class IntentService(StripeService):
    def __init__(self, requestor):
        super().__init__(requestor)
        self.actions = ActionService(self._requestor)

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
        Actions to be performed by this Billing Intent.
        """
        currency: str
        """
        Three-letter ISO currency code, in lowercase. Must be a supported currency.
        """
        cadence: NotRequired[str]
        """
        ID of an existing Cadence to use.
        """

    class CreateParamsAction(TypedDict):
        type: Literal["apply", "deactivate", "modify", "remove", "subscribe"]
        """
        Type of the Billing Intent action.
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
        billing_details: NotRequired[
            "IntentService.CreateParamsActionDeactivateBillingDetails"
        ]
        """
        Configuration for the billing details.
        """
        effective_at: NotRequired[
            "IntentService.CreateParamsActionDeactivateEffectiveAt"
        ]
        """
        When the deactivate action will take effect. If not specified, the default behavior is on_reserve.
        """
        pricing_plan_subscription_details: "IntentService.CreateParamsActionDeactivatePricingPlanSubscriptionDetails"
        """
        Details for deactivating a pricing plan subscription.
        """
        type: Literal[
            "pricing_plan_subscription_details", "v1_subscription_details"
        ]
        """
        Type of the action details.
        """

    class CreateParamsActionDeactivateBillingDetails(TypedDict):
        proration_behavior: NotRequired[
            Literal["no_adjustment", "prorated_adjustment"]
        ]
        """
        This controls the proration adjustment for the partial servicing period.
        """

    class CreateParamsActionDeactivateEffectiveAt(TypedDict):
        timestamp: NotRequired[str]
        """
        The timestamp at which the deactivate action will take effect. Only present if type is timestamp.
        """
        type: Literal[
            "current_billing_period_start", "on_reserve", "timestamp"
        ]
        """
        When the deactivate action will take effect.
        """

    class CreateParamsActionDeactivatePricingPlanSubscriptionDetails(
        TypedDict
    ):
        pricing_plan_subscription: str
        """
        ID of the pricing plan subscription to deactivate.
        """

    class CreateParamsActionModify(TypedDict):
        billing_details: NotRequired[
            "IntentService.CreateParamsActionModifyBillingDetails"
        ]
        """
        Configuration for the billing details.
        """
        effective_at: NotRequired[
            "IntentService.CreateParamsActionModifyEffectiveAt"
        ]
        """
        When the modify action will take effect. If not specified, the default behavior is on_reserve.
        """
        pricing_plan_subscription_details: "IntentService.CreateParamsActionModifyPricingPlanSubscriptionDetails"
        """
        Details for modifying a pricing plan subscription.
        """
        type: Literal[
            "pricing_plan_subscription_details", "v1_subscription_details"
        ]
        """
        Type of the action details.
        """

    class CreateParamsActionModifyBillingDetails(TypedDict):
        proration_behavior: NotRequired[
            Literal["no_adjustment", "prorated_adjustment"]
        ]
        """
        This controls the proration adjustment for the partial servicing period.
        """

    class CreateParamsActionModifyEffectiveAt(TypedDict):
        timestamp: NotRequired[str]
        """
        The timestamp at which the modify action will take effect. Only present if type is timestamp.
        """
        type: Literal[
            "current_billing_period_start", "on_reserve", "timestamp"
        ]
        """
        When the modify action will take effect.
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
        The ID of the new Pricing Plan, if changing plans.
        """
        new_pricing_plan_version: NotRequired[str]
        """
        The ID of the new Pricing Plan Version to use.
        """
        pricing_plan_subscription: str
        """
        The ID of the Pricing Plan Subscription to modify.
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
        billing_details: NotRequired[
            "IntentService.CreateParamsActionSubscribeBillingDetails"
        ]
        """
        Configuration for the billing details. If not specified, see the default behavior for individual attributes.
        """
        effective_at: NotRequired[
            "IntentService.CreateParamsActionSubscribeEffectiveAt"
        ]
        """
        When the subscribe action will take effect. If not specified, the default behavior is on_reserve.
        """
        type: Literal[
            "pricing_plan_subscription_details", "v1_subscription_details"
        ]
        """
        Type of the action details.
        """
        pricing_plan_subscription_details: NotRequired[
            "IntentService.CreateParamsActionSubscribePricingPlanSubscriptionDetails"
        ]
        """
        Details for subscribing to a pricing plan.
        """
        v1_subscription_details: NotRequired[
            "IntentService.CreateParamsActionSubscribeV1SubscriptionDetails"
        ]
        """
        Details for subscribing to a v1 subscription.
        """

    class CreateParamsActionSubscribeBillingDetails(TypedDict):
        proration_behavior: NotRequired[
            Literal["no_adjustment", "prorated_adjustment"]
        ]
        """
        This controls the proration adjustment for the partial servicing period.
        """

    class CreateParamsActionSubscribeEffectiveAt(TypedDict):
        timestamp: NotRequired[str]
        """
        The timestamp at which the subscribe action will take effect. Only present if type is timestamp.
        """
        type: Literal[
            "current_billing_period_start", "on_reserve", "timestamp"
        ]
        """
        When the subscribe action will take effect.
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
        Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
        """
        pricing_plan: str
        """
        ID of the Pricing Plan to subscribe to.
        """
        pricing_plan_version: str
        """
        Version of the Pricing Plan to use.
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

    class CreateParamsActionSubscribeV1SubscriptionDetails(TypedDict):
        description: NotRequired[str]
        """
        The subscription's description, meant to be displayable to the customer.
        Use this field to optionally store an explanation of the subscription for rendering in Stripe surfaces and certain local payment methods UIs.
        """
        items: List[
            "IntentService.CreateParamsActionSubscribeV1SubscriptionDetailsItem"
        ]
        """
        A list of up to 20 subscription items, each with an attached price.
        """
        metadata: NotRequired[Dict[str, str]]
        """
        Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
        """

    class CreateParamsActionSubscribeV1SubscriptionDetailsItem(TypedDict):
        metadata: NotRequired[Dict[str, str]]
        """
        Set of key-value pairs that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
        """
        price: str
        """
        The ID of the price object.
        """
        quantity: NotRequired[int]
        """
        Quantity for this item. If not provided, will default to 1.
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
        List Billing Intents.
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
        List Billing Intents.
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
        Create a Billing Intent.
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
        Create a Billing Intent.
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
        Retrieve a Billing Intent.
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
        Retrieve a Billing Intent.
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
        Cancel a Billing Intent.
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
        Cancel a Billing Intent.
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
        Commit a Billing Intent.
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
        Commit a Billing Intent.
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
        Release a Billing Intent.
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
        Release a Billing Intent.
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
        Reserve a Billing Intent.
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
        Reserve a Billing Intent.
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
