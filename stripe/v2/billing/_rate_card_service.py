# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2._list_object import ListObject
from stripe.v2.billing._rate_card import RateCard
from stripe.v2.billing.rate_cards._rate_service import RateService
from stripe.v2.billing.rate_cards._version_service import VersionService
from typing import Dict, List, Optional, cast
from typing_extensions import Literal, NotRequired, TypedDict


class RateCardService(StripeService):
    def __init__(self, requestor):
        super().__init__(requestor)
        self.rates = RateService(self._requestor)
        self.versions = VersionService(self._requestor)

    class CreateParams(TypedDict):
        currency: str
        """
        The currency of this RateCard.
        """
        display_name: str
        """
        A customer-facing name for the RateCard.
        This name is used in Stripe-hosted products like the Customer Portal and Checkout. It does not show up on Invoices.
        Maximum length of 250 characters.
        """
        lookup_key: NotRequired[str]
        """
        An internal key you can use to search for a particular RateCard. Maximum length of 200 characters.
        """
        metadata: NotRequired[Dict[str, str]]
        """
        Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
        """
        service_interval: Literal["day", "month", "week", "year"]
        """
        The interval for assessing service. For example, a monthly RateCard with a rate of $1 for the first 10 "workloads"
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
        The Stripe Tax tax behavior - whether the rates are inclusive or exclusive of tax.
        """

    class ListParams(TypedDict):
        active: NotRequired[bool]
        """
        Optionally filter to active/inactive RateCards.
        """
        limit: NotRequired[int]
        """
        Optionally set the maximum number of results per page. Defaults to 20.
        """
        lookup_keys: NotRequired[List[str]]
        """
        Filter by lookup keys.
        You can specify up to 10 lookup keys.
        """

    class RetrieveParams(TypedDict):
        pass

    class UpdateParams(TypedDict):
        active: NotRequired[bool]
        """
        Sets whether the RateCard is active. Inactive RateCards cannot be used in new activations or have new rates added.
        """
        display_name: NotRequired[str]
        """
        A customer-facing name for the RateCard.
        This name is used in Stripe-hosted products like the Customer Portal and Checkout. It does not show up on Invoices.
        Maximum length of 250 characters.
        """
        live_version: NotRequired[str]
        """
        Changes the version that new RateCard activations will use. Providing `live_version = "latest"` will set the
        RateCard's `live_version` to its latest version.
        """
        lookup_key: NotRequired[str]
        """
        An internal key you can use to search for a particular RateCard. Maximum length of 200 characters.
        """
        metadata: NotRequired[Dict[str, Optional[str]]]
        """
        Set of [key-value pairs](https://docs.stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format.
        """

    def list(
        self,
        params: "RateCardService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[RateCard]:
        """
        List all Rate Card objects.
        """
        return cast(
            ListObject[RateCard],
            self._request(
                "get",
                "/v2/billing/rate_cards",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "RateCardService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[RateCard]:
        """
        List all Rate Card objects.
        """
        return cast(
            ListObject[RateCard],
            await self._request_async(
                "get",
                "/v2/billing/rate_cards",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "RateCardService.CreateParams",
        options: RequestOptions = {},
    ) -> RateCard:
        """
        Create a Rate Card object.
        """
        return cast(
            RateCard,
            self._request(
                "post",
                "/v2/billing/rate_cards",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "RateCardService.CreateParams",
        options: RequestOptions = {},
    ) -> RateCard:
        """
        Create a Rate Card object.
        """
        return cast(
            RateCard,
            await self._request_async(
                "post",
                "/v2/billing/rate_cards",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: "RateCardService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> RateCard:
        """
        Retrieve the latest version of a Rate Card object.
        """
        return cast(
            RateCard,
            self._request(
                "get",
                "/v2/billing/rate_cards/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: "RateCardService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> RateCard:
        """
        Retrieve the latest version of a Rate Card object.
        """
        return cast(
            RateCard,
            await self._request_async(
                "get",
                "/v2/billing/rate_cards/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        id: str,
        params: "RateCardService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> RateCard:
        """
        Update a Rate Card object.
        """
        return cast(
            RateCard,
            self._request(
                "post",
                "/v2/billing/rate_cards/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        id: str,
        params: "RateCardService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> RateCard:
        """
        Update a Rate Card object.
        """
        return cast(
            RateCard,
            await self._request_async(
                "post",
                "/v2/billing/rate_cards/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
