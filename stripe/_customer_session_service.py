# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._customer_session import CustomerSession
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from typing import List, cast
from typing_extensions import NotRequired, TypedDict


class CustomerSessionService(StripeService):
    class CreateParams(TypedDict):
        components: "CustomerSessionService.CreateParamsComponents"
        """
        Configuration for each component. Exactly 1 component must be enabled.
        """
        customer: str
        """
        The ID of an existing customer for which to create the customer session.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    class CreateParamsComponents(TypedDict):
        buy_button: NotRequired[
            "CustomerSessionService.CreateParamsComponentsBuyButton"
        ]
        """
        Configuration for buy button.
        """
        pricing_table: NotRequired[
            "CustomerSessionService.CreateParamsComponentsPricingTable"
        ]
        """
        Configuration for the pricing table.
        """

    class CreateParamsComponentsBuyButton(TypedDict):
        enabled: bool
        """
        Whether the buy button is enabled.
        """

    class CreateParamsComponentsPricingTable(TypedDict):
        enabled: bool
        """
        Whether the pricing table is enabled.
        """

    def create(
        self,
        params: "CustomerSessionService.CreateParams",
        options: RequestOptions = {},
    ) -> CustomerSession:
        """
        Creates a customer session object that includes a single-use client secret that you can use on your front-end to grant client-side API access for certain customer resources.
        """
        return cast(
            CustomerSession,
            self._request(
                "post",
                "/v1/customer_sessions",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "CustomerSessionService.CreateParams",
        options: RequestOptions = {},
    ) -> CustomerSession:
        """
        Creates a customer session object that includes a single-use client secret that you can use on your front-end to grant client-side API access for certain customer resources.
        """
        return cast(
            CustomerSession,
            await self._request_async(
                "post",
                "/v1/customer_sessions",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )
