# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2._list_object import ListObject
from stripe.v2.billing._license_fee import LicenseFee
from stripe.v2.billing.license_fees._version_service import VersionService
from typing import Dict, List, Optional, cast
from typing_extensions import Literal, NotRequired, TypedDict


class LicenseFeeService(StripeService):
    def __init__(self, requestor):
        super().__init__(requestor)
        self.versions = VersionService(self._requestor)

    class CreateParams(TypedDict):
        currency: str
        """
        Three-letter ISO currency code, in lowercase. Must be a supported currency.
        """
        display_name: str
        """
        A customer-facing name for the License Fee.
        This name is used in Stripe-hosted products like the Customer Portal and Checkout. It does not show up on Invoices.
        Maximum length of 250 characters.
        """
        licensed_item: str
        """
        The Licensed Item that this License Fee binds to.
        """
        lookup_key: NotRequired[str]
        """
        An internal key you can use to search for a particular license fee. Maximum length of 200 characters.
        """
        metadata: NotRequired[Dict[str, str]]
        """
        Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
        """
        service_interval: Literal["day", "month", "week", "year"]
        """
        The interval for assessing service. For example, a monthly license fee with a rate of $1 for the first 10 "workloads"
        and $2 thereafter means "$1 per workload up to 10 workloads during a month of service." This is similar to but
        distinct from billing interval; the service interval deals with the rate at which the customer accumulates fees,
        while the billing interval in Cadence deals with the rate the customer is billed.
        """
        service_interval_count: int
        """
        The length of the interval for assessing service. For example, set this to 3 and `service_interval` to `"month"` in
        order to specify quarterly service.
        """
        tax_behavior: Literal["exclusive", "inclusive"]
        """
        The Stripe Tax tax behavior - whether the license fee is inclusive or exclusive of tax.
        """
        tiering_mode: NotRequired[Literal["graduated", "volume"]]
        """
        Defines whether the tiered price should be graduated or volume-based. In volume-based tiering, the maximum
        quantity within a period determines the per-unit price. In graduated tiering, the pricing changes as the quantity
        grows into new tiers. Can only be set if `tiers` is set.
        """
        tiers: NotRequired[List["LicenseFeeService.CreateParamsTier"]]
        """
        Each element represents a pricing tier. Cannot be set if `unit_amount` is provided.
        """
        transform_quantity: NotRequired[
            "LicenseFeeService.CreateParamsTransformQuantity"
        ]
        """
        Apply a transformation to the reported usage or set quantity before computing the amount billed.
        """
        unit_amount: NotRequired[str]
        """
        The per-unit amount to be charged, represented as a decimal string in minor currency units with at most 12 decimal
        places. Cannot be set if `tiers` is provided.
        """

    class CreateParamsTier(TypedDict):
        flat_amount: NotRequired[str]
        """
        Price for the entire tier, represented as a decimal string in minor currency units with at most 12 decimal places.
        """
        unit_amount: NotRequired[str]
        """
        Per-unit price for units included in this tier, represented as a decimal string in minor currency units with at
        most 12 decimal places.
        """
        up_to_decimal: NotRequired[str]
        """
        Up to and including this quantity will be contained in the tier. Only one of `up_to_decimal` and `up_to_inf` may
        be set.
        """
        up_to_inf: NotRequired[Literal["inf"]]
        """
        No upper bound to this tier. Only one of `up_to_decimal` and `up_to_inf` may be set.
        """

    class CreateParamsTransformQuantity(TypedDict):
        divide_by: int
        """
        Divide usage by this number.
        """
        round: Literal["down", "up"]
        """
        After division, round the result up or down.
        """

    class ListParams(TypedDict):
        licensed_item: NotRequired[str]
        """
        Filter by licensed item.
        """
        limit: NotRequired[int]
        """
        Optionally set the maximum number of results per page. Defaults to 20.
        """
        lookup_keys: List[str]
        """
        Filter by lookup keys.
        You can specify up to 10 lookup keys.
        """

    class RetrieveParams(TypedDict):
        pass

    class UpdateParams(TypedDict):
        display_name: str
        """
        A customer-facing name for the License Fee.
        This name is used in Stripe-hosted products like the Customer Portal and Checkout. It does not show up on Invoices.
        Maximum length of 250 characters.
        """
        live_version: NotRequired[str]
        """
        Changes the version that new license fee will use. Providing `live_version = "latest"` will set the
        license fee's `live_version` to its latest version.
        """
        lookup_key: NotRequired[str]
        """
        An internal key you can use to search for a particular license fee. Maximum length of 200 characters.
        """
        metadata: NotRequired[Dict[str, Optional[str]]]
        """
        Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
        """
        tiering_mode: NotRequired[Literal["graduated", "volume"]]
        """
        Defines whether the tiered price should be graduated or volume-based. In volume-based tiering, the maximum
        quantity within a period determines the per-unit price. In graduated tiering, the pricing changes as the quantity
        grows into new tiers. Can only be set if `tiers` is set.
        """
        tiers: NotRequired[List["LicenseFeeService.UpdateParamsTier"]]
        """
        Each element represents a pricing tier. Cannot be set if `unit_amount` is provided.
        """
        transform_quantity: NotRequired[
            "LicenseFeeService.UpdateParamsTransformQuantity"
        ]
        """
        Apply a transformation to the reported usage or set quantity before computing the amount billed.
        """
        unit_amount: NotRequired[str]
        """
        The per-unit amount to be charged, represented as a decimal string in minor currency units with at most 12 decimal
        places. Cannot be set if `tiers` is provided.
        """

    class UpdateParamsTier(TypedDict):
        flat_amount: NotRequired[str]
        """
        Price for the entire tier, represented as a decimal string in minor currency units with at most 12 decimal places.
        """
        unit_amount: NotRequired[str]
        """
        Per-unit price for units included in this tier, represented as a decimal string in minor currency units with at
        most 12 decimal places.
        """
        up_to_decimal: NotRequired[str]
        """
        Up to and including this quantity will be contained in the tier. Only one of `up_to_decimal` and `up_to_inf` may
        be set.
        """
        up_to_inf: NotRequired[Literal["inf"]]
        """
        No upper bound to this tier. Only one of `up_to_decimal` and `up_to_inf` may be set.
        """

    class UpdateParamsTransformQuantity(TypedDict):
        divide_by: int
        """
        Divide usage by this number.
        """
        round: Literal["down", "up"]
        """
        After division, round the result up or down.
        """

    def list(
        self,
        params: "LicenseFeeService.ListParams",
        options: RequestOptions = {},
    ) -> ListObject[LicenseFee]:
        """
        List all License Fee objects.
        """
        return cast(
            ListObject[LicenseFee],
            self._request(
                "get",
                "/v2/billing/license_fees",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "LicenseFeeService.ListParams",
        options: RequestOptions = {},
    ) -> ListObject[LicenseFee]:
        """
        List all License Fee objects.
        """
        return cast(
            ListObject[LicenseFee],
            await self._request_async(
                "get",
                "/v2/billing/license_fees",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "LicenseFeeService.CreateParams",
        options: RequestOptions = {},
    ) -> LicenseFee:
        """
        Create a License Fee object.
        """
        return cast(
            LicenseFee,
            self._request(
                "post",
                "/v2/billing/license_fees",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "LicenseFeeService.CreateParams",
        options: RequestOptions = {},
    ) -> LicenseFee:
        """
        Create a License Fee object.
        """
        return cast(
            LicenseFee,
            await self._request_async(
                "post",
                "/v2/billing/license_fees",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: "LicenseFeeService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> LicenseFee:
        """
        Retrieve a License Fee object.
        """
        return cast(
            LicenseFee,
            self._request(
                "get",
                "/v2/billing/license_fees/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: "LicenseFeeService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> LicenseFee:
        """
        Retrieve a License Fee object.
        """
        return cast(
            LicenseFee,
            await self._request_async(
                "get",
                "/v2/billing/license_fees/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        id: str,
        params: "LicenseFeeService.UpdateParams",
        options: RequestOptions = {},
    ) -> LicenseFee:
        """
        Update a License Fee object.
        """
        return cast(
            LicenseFee,
            self._request(
                "post",
                "/v2/billing/license_fees/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        id: str,
        params: "LicenseFeeService.UpdateParams",
        options: RequestOptions = {},
    ) -> LicenseFee:
        """
        Update a License Fee object.
        """
        return cast(
            LicenseFee,
            await self._request_async(
                "post",
                "/v2/billing/license_fees/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
