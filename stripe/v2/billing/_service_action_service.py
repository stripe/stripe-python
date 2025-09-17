# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2._amount import AmountParam
from stripe.v2.billing._service_action import ServiceAction
from typing import List, cast
from typing_extensions import Literal, NotRequired, TypedDict


class ServiceActionService(StripeService):
    class CreateParams(TypedDict):
        lookup_key: NotRequired[str]
        """
        An internal key you can use to search for this service action. Maximum length of 200 characters.
        """
        service_interval: Literal["day", "month", "week", "year"]
        """
        The interval for assessing service.
        """
        service_interval_count: int
        """
        The length of the interval for assessing service.
        """
        type: Literal["credit_grant", "credit_grant_per_tenant"]
        """
        The type of the service action.
        """
        credit_grant: NotRequired[
            "ServiceActionService.CreateParamsCreditGrant"
        ]
        """
        Details for the credit grant. Required if `type` is `credit_grant`.
        """
        credit_grant_per_tenant: NotRequired[
            "ServiceActionService.CreateParamsCreditGrantPerTenant"
        ]
        """
        Details for the credit grant per tenant. Required if `type` is `credit_grant_per_tenant`.
        """

    class CreateParamsCreditGrant(TypedDict):
        amount: "ServiceActionService.CreateParamsCreditGrantAmount"
        """
        The amount of the credit grant.
        """
        applicability_config: (
            "ServiceActionService.CreateParamsCreditGrantApplicabilityConfig"
        )
        """
        Defines the scope where the credit grant is applicable.
        """
        expiry_config: (
            "ServiceActionService.CreateParamsCreditGrantExpiryConfig"
        )
        """
        The expiry configuration for the credit grant.
        """
        name: str
        """
        A descriptive name shown in dashboard.
        """

    class CreateParamsCreditGrantAmount(TypedDict):
        type: Literal["custom_pricing_unit", "monetary"]
        """
        The type of the credit grant amount. We currently support `monetary` and `custom_pricing_unit` billing credits.
        """
        custom_pricing_unit: NotRequired[
            "ServiceActionService.CreateParamsCreditGrantAmountCustomPricingUnit"
        ]
        """
        The custom pricing unit amount of the credit grant. Required if `type` is `custom_pricing_unit`.
        """
        monetary: NotRequired[AmountParam]
        """
        The monetary amount of the credit grant. Required if `type` is `monetary`.
        """

    class CreateParamsCreditGrantAmountCustomPricingUnit(TypedDict):
        id: str
        """
        The id of the custom pricing unit.
        """
        value: str
        """
        The value of the credit grant, decimal value represented as a string.
        """

    class CreateParamsCreditGrantApplicabilityConfig(TypedDict):
        scope: "ServiceActionService.CreateParamsCreditGrantApplicabilityConfigScope"
        """
        The applicability scope of the credit grant.
        """

    class CreateParamsCreditGrantApplicabilityConfigScope(TypedDict):
        billable_items: NotRequired[List[str]]
        """
        The billable items to apply the credit grant to.
        """
        price_type: NotRequired[Literal["metered"]]
        """
        The price type that credit grants can apply to. We currently only support the `metered` price type. This will apply to metered prices and rate cards. Cannot be used in combination with `billable_items`.
        """

    class CreateParamsCreditGrantExpiryConfig(TypedDict):
        type: Literal["end_of_service_period"]
        """
        The type of the expiry configuration. We currently support `end_of_service_period`.
        """

    class CreateParamsCreditGrantPerTenant(TypedDict):
        amount: "ServiceActionService.CreateParamsCreditGrantPerTenantAmount"
        """
        The amount of the credit grant.
        """
        applicability_config: "ServiceActionService.CreateParamsCreditGrantPerTenantApplicabilityConfig"
        """
        Defines the scope where the credit grant is applicable.
        """
        expiry_config: (
            "ServiceActionService.CreateParamsCreditGrantPerTenantExpiryConfig"
        )
        """
        The expiry configuration for the credit grant.
        """
        grant_condition: "ServiceActionService.CreateParamsCreditGrantPerTenantGrantCondition"
        """
        The grant condition for the credit grant.
        """
        name: str
        """
        Customer-facing name for the credit grant.
        """

    class CreateParamsCreditGrantPerTenantAmount(TypedDict):
        type: Literal["custom_pricing_unit", "monetary"]
        """
        The type of the credit grant amount. We currently support `monetary` and `custom_pricing_unit` billing credits.
        """
        custom_pricing_unit: NotRequired[
            "ServiceActionService.CreateParamsCreditGrantPerTenantAmountCustomPricingUnit"
        ]
        """
        The custom pricing unit amount of the credit grant. Required if `type` is `custom_pricing_unit`.
        """
        monetary: NotRequired[AmountParam]
        """
        The monetary amount of the credit grant. Required if `type` is `monetary`.
        """

    class CreateParamsCreditGrantPerTenantAmountCustomPricingUnit(TypedDict):
        id: str
        """
        The id of the custom pricing unit.
        """
        value: str
        """
        The value of the credit grant, decimal value represented as a string.
        """

    class CreateParamsCreditGrantPerTenantApplicabilityConfig(TypedDict):
        scope: "ServiceActionService.CreateParamsCreditGrantPerTenantApplicabilityConfigScope"
        """
        The applicability scope of the credit grant.
        """

    class CreateParamsCreditGrantPerTenantApplicabilityConfigScope(TypedDict):
        billable_items: NotRequired[List[str]]
        """
        The billable items to apply the credit grant to.
        """
        price_type: NotRequired[Literal["metered"]]
        """
        The price type that credit grants can apply to. We currently only support the `metered` price type. This will apply to metered prices and rate cards. Cannot be used in combination with `billable_items`.
        """

    class CreateParamsCreditGrantPerTenantExpiryConfig(TypedDict):
        type: Literal["end_of_service_period"]
        """
        The type of the expiry configuration. We currently support `end_of_service_period`.
        """

    class CreateParamsCreditGrantPerTenantGrantCondition(TypedDict):
        type: Literal["meter_event_first_per_period"]
        """
        The type of the grant condition. We currently support `meter_event_first_per_period`.
        """
        meter_event_first_per_period: NotRequired[
            "ServiceActionService.CreateParamsCreditGrantPerTenantGrantConditionMeterEventFirstPerPeriod"
        ]
        """
        The grant condition for the meter event first per period.
        """

    class CreateParamsCreditGrantPerTenantGrantConditionMeterEventFirstPerPeriod(
        TypedDict,
    ):
        meter_segment_conditions: List[
            "ServiceActionService.CreateParamsCreditGrantPerTenantGrantConditionMeterEventFirstPerPeriodMeterSegmentCondition"
        ]
        """
        The meter segment conditions for the grant condition.
        """

    class CreateParamsCreditGrantPerTenantGrantConditionMeterEventFirstPerPeriodMeterSegmentCondition(
        TypedDict,
    ):
        type: Literal["dimension"]
        """
        The type of the meter segment condition. We currently support `dimension`.
        """
        dimension: NotRequired[
            "ServiceActionService.CreateParamsCreditGrantPerTenantGrantConditionMeterEventFirstPerPeriodMeterSegmentConditionDimension"
        ]
        """
        Dimension-based meter segment condition.
        """

    class CreateParamsCreditGrantPerTenantGrantConditionMeterEventFirstPerPeriodMeterSegmentConditionDimension(
        TypedDict,
    ):
        payload_key: str
        """
        The payload key for the dimension.
        """
        value: str
        """
        The value for the dimension.
        """

    class RetrieveParams(TypedDict):
        pass

    def create(
        self,
        params: "ServiceActionService.CreateParams",
        options: RequestOptions = {},
    ) -> ServiceAction:
        """
        Create a Service Action object.
        """
        return cast(
            ServiceAction,
            self._request(
                "post",
                "/v2/billing/service_actions",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "ServiceActionService.CreateParams",
        options: RequestOptions = {},
    ) -> ServiceAction:
        """
        Create a Service Action object.
        """
        return cast(
            ServiceAction,
            await self._request_async(
                "post",
                "/v2/billing/service_actions",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: "ServiceActionService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> ServiceAction:
        """
        Retrieve a Service Action object.
        """
        return cast(
            ServiceAction,
            self._request(
                "get",
                "/v2/billing/service_actions/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: "ServiceActionService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> ServiceAction:
        """
        Retrieve a Service Action object.
        """
        return cast(
            ServiceAction,
            await self._request_async(
                "get",
                "/v2/billing/service_actions/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
