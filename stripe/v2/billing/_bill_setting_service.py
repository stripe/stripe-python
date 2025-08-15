# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2._list_object import ListObject
from stripe.v2.billing._bill_setting import BillSetting
from stripe.v2.billing.bill_settings._version_service import VersionService
from typing import List, cast
from typing_extensions import Literal, NotRequired, TypedDict


class BillSettingService(StripeService):
    def __init__(self, requestor):
        super().__init__(requestor)
        self.versions = VersionService(self._requestor)

    class CreateParams(TypedDict):
        calculation: NotRequired["BillSettingService.CreateParamsCalculation"]
        """
        Settings related to calculating a bill.
        """
        display_name: NotRequired[str]
        """
        An optional customer-facing display name for the CollectionSetting object.
        Maximum length of 250 characters.
        """
        invoice: NotRequired["BillSettingService.CreateParamsInvoice"]
        """
        Settings related to invoice behavior.
        """
        invoice_rendering_template: NotRequired[str]
        """
        The ID of the invoice rendering template to be used when generating invoices.
        """
        lookup_key: NotRequired[str]
        """
        A lookup key used to retrieve settings dynamically from a static string.
        This may be up to 200 characters.
        """

    class CreateParamsCalculation(TypedDict):
        tax: NotRequired["BillSettingService.CreateParamsCalculationTax"]
        """
        Settings for calculating tax.
        """

    class CreateParamsCalculationTax(TypedDict):
        type: Literal["automatic", "manual"]
        """
        Determines if tax will be calculated automatically based on a PTC or manually based on rules defined by the merchant. Defaults to "manual".
        """

    class CreateParamsInvoice(TypedDict):
        time_until_due: NotRequired[
            "BillSettingService.CreateParamsInvoiceTimeUntilDue"
        ]
        """
        The amount of time until the invoice will be overdue for payment.
        """

    class CreateParamsInvoiceTimeUntilDue(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        """
        The interval unit for the time until due.
        """
        interval_count: int
        """
        The number of interval units. For example, if interval=day and interval_count=30,
        the invoice will be due in 30 days.
        """

    class ListParams(TypedDict):
        limit: NotRequired[int]
        """
        Optionally set the maximum number of results per page. Defaults to 20.
        """
        lookup_keys: NotRequired[List[str]]
        """
        Only return the settings with these lookup_keys, if any exist.
        You can specify up to 10 lookup_keys.
        """

    class RetrieveParams(TypedDict):
        pass

    class UpdateParams(TypedDict):
        calculation: NotRequired["BillSettingService.UpdateParamsCalculation"]
        """
        Settings related to calculating a bill.
        """
        display_name: NotRequired[str]
        """
        An optional customer-facing display name for the BillSetting object.
        To remove the display name, set it to an empty string in the request.
        Maximum length of 250 characters.
        """
        invoice: NotRequired["BillSettingService.UpdateParamsInvoice"]
        """
        Settings related to invoice behavior.
        """
        invoice_rendering_template: NotRequired[str]
        """
        The ID of the invoice rendering template to be used when generating invoices.
        """
        live_version: NotRequired[str]
        """
        Optionally change the live version of the BillSetting. Providing `live_version = "latest"` will set the
        BillSetting' `live_version` to its latest version.
        """
        lookup_key: NotRequired[str]
        """
        A lookup key used to retrieve settings dynamically from a static string.
        This may be up to 200 characters.
        """

    class UpdateParamsCalculation(TypedDict):
        tax: NotRequired["BillSettingService.UpdateParamsCalculationTax"]
        """
        Settings for calculating tax.
        """

    class UpdateParamsCalculationTax(TypedDict):
        type: Literal["automatic", "manual"]
        """
        Determines if tax will be calculated automatically based on a PTC or manually based on rules defined by the merchant. Defaults to "manual".
        """

    class UpdateParamsInvoice(TypedDict):
        time_until_due: NotRequired[
            "BillSettingService.UpdateParamsInvoiceTimeUntilDue"
        ]
        """
        The amount of time until the invoice will be overdue for payment.
        """

    class UpdateParamsInvoiceTimeUntilDue(TypedDict):
        interval: Literal["day", "month", "week", "year"]
        """
        The interval unit for the time until due.
        """
        interval_count: int
        """
        The number of interval units. For example, if interval=day and interval_count=30,
        the invoice will be due in 30 days.
        """

    def list(
        self,
        params: "BillSettingService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[BillSetting]:
        """
        List all BillSetting objects.
        """
        return cast(
            ListObject[BillSetting],
            self._request(
                "get",
                "/v2/billing/bill_settings",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "BillSettingService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[BillSetting]:
        """
        List all BillSetting objects.
        """
        return cast(
            ListObject[BillSetting],
            await self._request_async(
                "get",
                "/v2/billing/bill_settings",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "BillSettingService.CreateParams" = {},
        options: RequestOptions = {},
    ) -> BillSetting:
        """
        Create a BillSetting object.
        """
        return cast(
            BillSetting,
            self._request(
                "post",
                "/v2/billing/bill_settings",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "BillSettingService.CreateParams" = {},
        options: RequestOptions = {},
    ) -> BillSetting:
        """
        Create a BillSetting object.
        """
        return cast(
            BillSetting,
            await self._request_async(
                "post",
                "/v2/billing/bill_settings",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: "BillSettingService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> BillSetting:
        """
        Retrieve a BillSetting object by ID.
        """
        return cast(
            BillSetting,
            self._request(
                "get",
                "/v2/billing/bill_settings/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: "BillSettingService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> BillSetting:
        """
        Retrieve a BillSetting object by ID.
        """
        return cast(
            BillSetting,
            await self._request_async(
                "get",
                "/v2/billing/bill_settings/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        id: str,
        params: "BillSettingService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> BillSetting:
        """
        Update fields on an existing BillSetting object.
        """
        return cast(
            BillSetting,
            self._request(
                "post",
                "/v2/billing/bill_settings/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        id: str,
        params: "BillSettingService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> BillSetting:
        """
        Update fields on an existing BillSetting object.
        """
        return cast(
            BillSetting,
            await self._request_async(
                "post",
                "/v2/billing/bill_settings/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
