# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe.tax._association import Association
from typing import List, cast
from typing_extensions import NotRequired, TypedDict


class AssociationService(StripeService):
    class FindParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        payment_intent: str
        """
        Valid [PaymentIntent](https://stripe.com/docs/api/payment_intents/object) id
        """

    def find(
        self,
        params: "AssociationService.FindParams",
        options: RequestOptions = {},
    ) -> Association:
        """
        Finds a tax association object by PaymentIntent id.
        """
        return cast(
            Association,
            self._request(
                "get",
                "/v1/tax/associations/find",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def find_async(
        self,
        params: "AssociationService.FindParams",
        options: RequestOptions = {},
    ) -> Association:
        """
        Finds a tax association object by PaymentIntent id.
        """
        return cast(
            Association,
            await self._request_async(
                "get",
                "/v1/tax/associations/find",
                base_address="api",
                params=params,
                options=options,
            ),
        )
