# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.issuing._card import Card
from typing import List, Optional, cast
from typing_extensions import NotRequired, TypedDict


class CardService(StripeService):
    class DeliverCardParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    class FailCardParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    class ReturnCardParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    class ShipCardParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    class SubmitCardParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    def deliver_card(
        self,
        card: str,
        params: "CardService.DeliverCardParams" = None,
        options: Optional[RequestOptions] = None,
    ) -> Card:
        """
        Updates the shipping status of the specified Issuing Card object to delivered.
        """
        if params is None:
            params = {}
        if options is None:
            options = {}
        return cast(
            Card,
            self._request(
                "post",
                "/v1/test_helpers/issuing/cards/{card}/shipping/deliver".format(
                    card=sanitize_id(card),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def deliver_card_async(
        self,
        card: str,
        params: "CardService.DeliverCardParams" = None,
        options: Optional[RequestOptions] = None,
    ) -> Card:
        """
        Updates the shipping status of the specified Issuing Card object to delivered.
        """
        if params is None:
            params = {}
        if options is None:
            options = {}
        return cast(
            Card,
            await self._request_async(
                "post",
                "/v1/test_helpers/issuing/cards/{card}/shipping/deliver".format(
                    card=sanitize_id(card),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def fail_card(
        self,
        card: str,
        params: "CardService.FailCardParams" = None,
        options: Optional[RequestOptions] = None,
    ) -> Card:
        """
        Updates the shipping status of the specified Issuing Card object to failure.
        """
        if params is None:
            params = {}
        if options is None:
            options = {}
        return cast(
            Card,
            self._request(
                "post",
                "/v1/test_helpers/issuing/cards/{card}/shipping/fail".format(
                    card=sanitize_id(card),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def fail_card_async(
        self,
        card: str,
        params: "CardService.FailCardParams" = None,
        options: Optional[RequestOptions] = None,
    ) -> Card:
        """
        Updates the shipping status of the specified Issuing Card object to failure.
        """
        if params is None:
            params = {}
        if options is None:
            options = {}
        return cast(
            Card,
            await self._request_async(
                "post",
                "/v1/test_helpers/issuing/cards/{card}/shipping/fail".format(
                    card=sanitize_id(card),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def return_card(
        self,
        card: str,
        params: "CardService.ReturnCardParams" = None,
        options: Optional[RequestOptions] = None,
    ) -> Card:
        """
        Updates the shipping status of the specified Issuing Card object to returned.
        """
        if params is None:
            params = {}
        if options is None:
            options = {}
        return cast(
            Card,
            self._request(
                "post",
                "/v1/test_helpers/issuing/cards/{card}/shipping/return".format(
                    card=sanitize_id(card),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def return_card_async(
        self,
        card: str,
        params: "CardService.ReturnCardParams" = None,
        options: Optional[RequestOptions] = None,
    ) -> Card:
        """
        Updates the shipping status of the specified Issuing Card object to returned.
        """
        if params is None:
            params = {}
        if options is None:
            options = {}
        return cast(
            Card,
            await self._request_async(
                "post",
                "/v1/test_helpers/issuing/cards/{card}/shipping/return".format(
                    card=sanitize_id(card),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def ship_card(
        self,
        card: str,
        params: "CardService.ShipCardParams" = None,
        options: Optional[RequestOptions] = None,
    ) -> Card:
        """
        Updates the shipping status of the specified Issuing Card object to shipped.
        """
        if params is None:
            params = {}
        if options is None:
            options = {}
        return cast(
            Card,
            self._request(
                "post",
                "/v1/test_helpers/issuing/cards/{card}/shipping/ship".format(
                    card=sanitize_id(card),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def ship_card_async(
        self,
        card: str,
        params: "CardService.ShipCardParams" = None,
        options: Optional[RequestOptions] = None,
    ) -> Card:
        """
        Updates the shipping status of the specified Issuing Card object to shipped.
        """
        if params is None:
            params = {}
        if options is None:
            options = {}
        return cast(
            Card,
            await self._request_async(
                "post",
                "/v1/test_helpers/issuing/cards/{card}/shipping/ship".format(
                    card=sanitize_id(card),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def submit_card(
        self,
        card: str,
        params: "CardService.SubmitCardParams" = None,
        options: Optional[RequestOptions] = None,
    ) -> Card:
        """
        Updates the shipping status of the specified Issuing Card object to submitted. This method requires Stripe Version ‘2024-09-30.acacia' or later.
        """
        if params is None:
            params = {}
        if options is None:
            options = {}
        return cast(
            Card,
            self._request(
                "post",
                "/v1/test_helpers/issuing/cards/{card}/shipping/submit".format(
                    card=sanitize_id(card),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def submit_card_async(
        self,
        card: str,
        params: "CardService.SubmitCardParams" = None,
        options: Optional[RequestOptions] = None,
    ) -> Card:
        """
        Updates the shipping status of the specified Issuing Card object to submitted. This method requires Stripe Version ‘2024-09-30.acacia' or later.
        """
        if params is None:
            params = {}
        if options is None:
            options = {}
        return cast(
            Card,
            await self._request_async(
                "post",
                "/v1/test_helpers/issuing/cards/{card}/shipping/submit".format(
                    card=sanitize_id(card),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
