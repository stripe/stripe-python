# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2._list_object import ListObject
from stripe.v2.billing._cadence import Cadence
from typing import Dict, List, Optional, cast
from typing_extensions import Literal, NotRequired, TypedDict


class CadenceService(StripeService):
    class CancelParams(TypedDict):
        include: NotRequired[List[Literal["invoice_discount_rules"]]]
        """
        Additional resource to include in the response.
        """

    class CreateParams(TypedDict):
        billing_cycle: "CadenceService.CreateParamsBillingCycle"
        """
        The billing cycle is the object that defines future billing cycle dates.
        """
        include: NotRequired[List[Literal["invoice_discount_rules"]]]
        """
        Additional resource to include in the response.
        """
        metadata: NotRequired[Dict[str, str]]
        """
        Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
        """
        payer: "CadenceService.CreateParamsPayer"
        """
        The payer determines the entity financially responsible for the bill.
        """
        settings: NotRequired["CadenceService.CreateParamsSettings"]
        """
        The settings associated with the cadence.
        """

    class CreateParamsBillingCycle(TypedDict):
        interval_count: NotRequired[int]
        """
        The number of intervals (specified in the interval attribute) between
        cadence billings. For example, type=month and interval_count=3 bills every
        3 months. If this is not provided, it will default to 1.
        """
        type: Literal["day", "month", "week", "year"]
        """
        The frequency at which a cadence bills.
        """
        day: NotRequired["CadenceService.CreateParamsBillingCycleDay"]
        """
        Specific configuration for determining billing dates when type=day.
        """
        month: NotRequired["CadenceService.CreateParamsBillingCycleMonth"]
        """
        Specific configuration for determining billing dates when type=month.
        """
        week: NotRequired["CadenceService.CreateParamsBillingCycleWeek"]
        """
        Specific configuration for determining billing dates when type=week.
        """
        year: NotRequired["CadenceService.CreateParamsBillingCycleYear"]
        """
        Specific configuration for determining billing dates when type=year.
        """

    class CreateParamsBillingCycleDay(TypedDict):
        time: NotRequired["CadenceService.CreateParamsBillingCycleDayTime"]
        """
        The time at which the billing cycle ends.
        This field is optional, and if not provided, it will default to
        the time at which the cadence was created in UTC timezone.
        """

    class CreateParamsBillingCycleDayTime(TypedDict):
        hour: int
        """
        The hour at which the billing cycle ends.
        This must be an integer between 0 and 23, inclusive.
        0 represents midnight, and 23 represents 11 PM.
        """
        minute: int
        """
        The minute at which the billing cycle ends.
        Must be an integer between 0 and 59, inclusive.
        """
        second: int
        """
        The second at which the billing cycle ends.
        Must be an integer between 0 and 59, inclusive.
        """

    class CreateParamsBillingCycleMonth(TypedDict):
        day_of_month: int
        """
        The day to anchor the billing on for a type="month" billing cycle from
        1-31. If this number is greater than the number of days in the month being
        billed, this will anchor to the last day of the month. If not provided,
        this will default to the day the cadence was created.
        """
        time: NotRequired["CadenceService.CreateParamsBillingCycleMonthTime"]
        """
        The time at which the billing cycle ends.
        This field is optional, and if not provided, it will default to
        the time at which the cadence was created in UTC timezone.
        """

    class CreateParamsBillingCycleMonthTime(TypedDict):
        hour: int
        """
        The hour at which the billing cycle ends.
        This must be an integer between 0 and 23, inclusive.
        0 represents midnight, and 23 represents 11 PM.
        """
        minute: int
        """
        The minute at which the billing cycle ends.
        Must be an integer between 0 and 59, inclusive.
        """
        second: int
        """
        The second at which the billing cycle ends.
        Must be an integer between 0 and 59, inclusive.
        """

    class CreateParamsBillingCycleWeek(TypedDict):
        day_of_week: int
        """
        The day of the week to bill the type=week billing cycle on.
        Numbered from 1-7 for Monday to Sunday respectively, based on the ISO-8601
        week day numbering. If not provided, this will default to the day the
        cadence was created.
        """
        time: NotRequired["CadenceService.CreateParamsBillingCycleWeekTime"]
        """
        The time at which the billing cycle ends.
        This field is optional, and if not provided, it will default to
        the time at which the cadence was created in UTC timezone.
        """

    class CreateParamsBillingCycleWeekTime(TypedDict):
        hour: int
        """
        The hour at which the billing cycle ends.
        This must be an integer between 0 and 23, inclusive.
        0 represents midnight, and 23 represents 11 PM.
        """
        minute: int
        """
        The minute at which the billing cycle ends.
        Must be an integer between 0 and 59, inclusive.
        """
        second: int
        """
        The second at which the billing cycle ends.
        Must be an integer between 0 and 59, inclusive.
        """

    class CreateParamsBillingCycleYear(TypedDict):
        day_of_month: NotRequired[int]
        """
        The day to anchor the billing on for a type="month" billing cycle from
        1-31. If this number is greater than the number of days in the month being
        billed, this will anchor to the last day of the month. If not provided,
        this will default to the day the cadence was created.
        """
        month_of_year: NotRequired[int]
        """
        The month to bill on from 1-12. If not provided, this will default to the
        month the cadence was created.
        """
        time: NotRequired["CadenceService.CreateParamsBillingCycleYearTime"]
        """
        The time at which the billing cycle ends.
        This field is optional, and if not provided, it will default to
        the time at which the cadence was created in UTC timezone.
        """

    class CreateParamsBillingCycleYearTime(TypedDict):
        hour: int
        """
        The hour at which the billing cycle ends.
        This must be an integer between 0 and 23, inclusive.
        0 represents midnight, and 23 represents 11 PM.
        """
        minute: int
        """
        The minute at which the billing cycle ends.
        Must be an integer between 0 and 59, inclusive.
        """
        second: int
        """
        The second at which the billing cycle ends.
        Must be an integer between 0 and 59, inclusive.
        """

    class CreateParamsPayer(TypedDict):
        billing_profile: NotRequired[str]
        """
        The ID of the Billing Profile object which determines how a bill will be paid. If provided, the created cadence will be
        associated with the provided Billing Profile. If not provided, a new Billing Profile will be created and associated with the cadence.
        """
        customer: NotRequired[str]
        """
        The ID of the Customer object.
        """
        type: NotRequired[Literal["customer"]]
        """
        A string identifying the type of the payer. Currently the only supported value is `customer`.
        """

    class CreateParamsSettings(TypedDict):
        bill: NotRequired["CadenceService.CreateParamsSettingsBill"]
        """
        Settings that configure bill generation, which includes calculating totals, tax, and presenting invoices.
        If no setting is provided here, the settings from the customer referenced on the payer will be used.
        If no customer settings are present, the merchant default settings will be used.
        """
        collection: NotRequired[
            "CadenceService.CreateParamsSettingsCollection"
        ]
        """
        Settings that configure and manage the behavior of collecting payments.
        If no setting is provided here, the settings from the customer referenced from the payer will be used if they exist.
        If no customer settings are present, the merchant default settings will be used.
        """

    class CreateParamsSettingsBill(TypedDict):
        id: str
        """
        The ID of the referenced settings object.
        """
        version: NotRequired[str]
        """
        An optional field to specify the version of the Settings to use.
        If not provided, this will always default to the live version any time the settings are used.
        """

    class CreateParamsSettingsCollection(TypedDict):
        id: str
        """
        The ID of the referenced settings object.
        """
        version: NotRequired[str]
        """
        An optional field to specify the version of the Settings to use.
        If not provided, this will always default to the live version any time the settings are used.
        """

    class ListParams(TypedDict):
        include: NotRequired[List[Literal["invoice_discount_rules"]]]
        """
        Additional resource to include in the response.
        """
        limit: NotRequired[int]
        """
        Optionally set the maximum number of results per page. Defaults to 20.
        """
        payer: NotRequired["CadenceService.ListParamsPayer"]
        """
        If provided, only cadences that specifically reference the payer will be returned. Mutually exclusive with `test_clock`.
        """
        test_clock: NotRequired[str]
        """
        If provided, only cadences that specifically reference the provided test clock ID (via the
        customer's test clock) will be returned.
        Mutually exclusive with `payer`.
        """

    class ListParamsPayer(TypedDict):
        customer: NotRequired[str]
        """
        The ID of the Customer object. If provided, only cadences that specifically reference the provided customer ID will be returned.
        """
        type: Literal["customer"]
        """
        A string identifying the type of the payer. Currently the only supported value is `customer`.
        """

    class RetrieveParams(TypedDict):
        include: NotRequired[List[Literal["invoice_discount_rules"]]]
        """
        Additional resource to include in the response.
        """

    class UpdateParams(TypedDict):
        include: NotRequired[List[Literal["invoice_discount_rules"]]]
        """
        Additional resource to include in the response.
        """
        metadata: NotRequired[Dict[str, Optional[str]]]
        """
        Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
        """
        payer: NotRequired["CadenceService.UpdateParamsPayer"]
        """
        The payer determines the entity financially responsible for the bill.
        """
        settings: NotRequired["CadenceService.UpdateParamsSettings"]
        """
        The settings associated with the cadence.
        """

    class UpdateParamsPayer(TypedDict):
        billing_profile: NotRequired[str]
        """
        The ID of the Billing Profile object which determines how a bill will be paid.
        """

    class UpdateParamsSettings(TypedDict):
        bill: NotRequired[Optional["CadenceService.UpdateParamsSettingsBill"]]
        """
        Settings that configure bills generation, which includes calculating totals, tax, and presenting invoices. If null is provided, the current bill settings will be removed from the billing cadence.
        """
        collection: NotRequired[
            Optional["CadenceService.UpdateParamsSettingsCollection"]
        ]
        """
        Settings that configure and manage the behavior of collecting payments. If null is provided, the current collection settings will be removed from the billing cadence.
        """

    class UpdateParamsSettingsBill(TypedDict):
        id: str
        """
        The ID of the referenced settings object.
        """
        version: NotRequired[Optional[str]]
        """
        An optional field to specify the version of Settings to use.
        If not provided, this will always default to the `live_version` specified on the setting, any time the settings are used.
        Using a specific version here will prevent the settings from updating, and is discouraged for cadences.
        To clear a pinned version, set the version to null.
        """

    class UpdateParamsSettingsCollection(TypedDict):
        id: str
        """
        The ID of the referenced settings object.
        """
        version: NotRequired[Optional[str]]
        """
        An optional field to specify the version of Settings to use.
        If not provided, this will always default to the `live_version` specified on the setting, any time the settings are used.
        Using a specific version here will prevent the settings from updating, and is discouraged for cadences.
        To clear a pinned version, set the version to null.
        """

    def list(
        self,
        params: "CadenceService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[Cadence]:
        """
        List Billing Cadences.
        """
        return cast(
            ListObject[Cadence],
            self._request(
                "get",
                "/v2/billing/cadences",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "CadenceService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[Cadence]:
        """
        List Billing Cadences.
        """
        return cast(
            ListObject[Cadence],
            await self._request_async(
                "get",
                "/v2/billing/cadences",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "CadenceService.CreateParams",
        options: RequestOptions = {},
    ) -> Cadence:
        """
        Create a Billing Cadence object.
        """
        return cast(
            Cadence,
            self._request(
                "post",
                "/v2/billing/cadences",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "CadenceService.CreateParams",
        options: RequestOptions = {},
    ) -> Cadence:
        """
        Create a Billing Cadence object.
        """
        return cast(
            Cadence,
            await self._request_async(
                "post",
                "/v2/billing/cadences",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: "CadenceService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> Cadence:
        """
        Retrieve a Billing Cadence object.
        """
        return cast(
            Cadence,
            self._request(
                "get",
                "/v2/billing/cadences/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: "CadenceService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> Cadence:
        """
        Retrieve a Billing Cadence object.
        """
        return cast(
            Cadence,
            await self._request_async(
                "get",
                "/v2/billing/cadences/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        id: str,
        params: "CadenceService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> Cadence:
        """
        Update a Billing Cadence object.
        """
        return cast(
            Cadence,
            self._request(
                "post",
                "/v2/billing/cadences/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        id: str,
        params: "CadenceService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> Cadence:
        """
        Update a Billing Cadence object.
        """
        return cast(
            Cadence,
            await self._request_async(
                "post",
                "/v2/billing/cadences/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def cancel(
        self,
        id: str,
        params: "CadenceService.CancelParams" = {},
        options: RequestOptions = {},
    ) -> Cadence:
        """
        Cancel the Billing Cadence.
        """
        return cast(
            Cadence,
            self._request(
                "post",
                "/v2/billing/cadences/{id}/cancel".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def cancel_async(
        self,
        id: str,
        params: "CadenceService.CancelParams" = {},
        options: RequestOptions = {},
    ) -> Cadence:
        """
        Cancel the Billing Cadence.
        """
        return cast(
            Cadence,
            await self._request_async(
                "post",
                "/v2/billing/cadences/{id}/cancel".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
