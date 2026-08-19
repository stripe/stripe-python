# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._list_object import ListObject
    from stripe._payment_plan import PaymentPlan
    from stripe._request_options import RequestOptions
    from stripe.params._payment_plan_create_params import (
        PaymentPlanCreateParams,
    )
    from stripe.params._payment_plan_list_params import PaymentPlanListParams
    from stripe.params._payment_plan_retrieve_params import (
        PaymentPlanRetrieveParams,
    )
    from stripe.params._payment_plan_update_params import (
        PaymentPlanUpdateParams,
    )


class PaymentPlanService(StripeService):
    def list(
        self,
        params: Optional["PaymentPlanListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[PaymentPlan]":
        """
        Returns a list of payment plans.
        """
        return cast(
            "ListObject[PaymentPlan]",
            self._request(
                "get",
                "/v1/payment_plans",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["PaymentPlanListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[PaymentPlan]":
        """
        Returns a list of payment plans.
        """
        return cast(
            "ListObject[PaymentPlan]",
            await self._request_async(
                "get",
                "/v1/payment_plans",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "PaymentPlanCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentPlan":
        """
        Creates a payment plan that splits a single invoice obligation into installments with their own due dates and amounts.
        """
        return cast(
            "PaymentPlan",
            self._request(
                "post",
                "/v1/payment_plans",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "PaymentPlanCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentPlan":
        """
        Creates a payment plan that splits a single invoice obligation into installments with their own due dates and amounts.
        """
        return cast(
            "PaymentPlan",
            await self._request_async(
                "post",
                "/v1/payment_plans",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["PaymentPlanRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentPlan":
        """
        Retrieves the payment plan with the given ID.
        """
        return cast(
            "PaymentPlan",
            self._request(
                "get",
                "/v1/payment_plans/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: Optional["PaymentPlanRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentPlan":
        """
        Retrieves the payment plan with the given ID.
        """
        return cast(
            "PaymentPlan",
            await self._request_async(
                "get",
                "/v1/payment_plans/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        id: str,
        params: Optional["PaymentPlanUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentPlan":
        """
        Updates the schedule or metadata of an existing payment plan. Only unpaid installments can be updated.
        """
        return cast(
            "PaymentPlan",
            self._request(
                "post",
                "/v1/payment_plans/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        id: str,
        params: Optional["PaymentPlanUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentPlan":
        """
        Updates the schedule or metadata of an existing payment plan. Only unpaid installments can be updated.
        """
        return cast(
            "PaymentPlan",
            await self._request_async(
                "post",
                "/v1/payment_plans/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
