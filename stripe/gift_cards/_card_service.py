# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._list_object import ListObject
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.gift_cards._card import Card
from typing import Dict, List, cast
from typing_extensions import Literal, NotRequired, TypedDict


class CardService(StripeService):
    class CreateParams(TypedDict):
        active: NotRequired["bool"]
        """
        The active state for the new gift card, defaults to false. The active state can be updated after creation.
        """
        created_by: NotRequired["CardService.CreateParamsCreatedBy"]
        """
        Related objects which created this gift card.
        """
        currency: str
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        initial_amount: NotRequired["int"]
        """
        The initial amount to load onto the new gift card, defaults to 0.
        """
        metadata: NotRequired["Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """

    class CreateParamsCreatedBy(TypedDict):
        payment: "CardService.CreateParamsCreatedByPayment"
        """
        The details for the payment that created this object.
        """
        type: Literal["payment"]
        """
        The type of event that created this object.
        """

    class CreateParamsCreatedByPayment(TypedDict):
        payment_intent: str
        """
        The PaymentIntent used to collect payment for this object.
        """

    class ListParams(TypedDict):
        ending_before: NotRequired["str"]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        limit: NotRequired["int"]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        starting_after: NotRequired["str"]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """

    class RetrieveParams(TypedDict):
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """

    class UpdateParams(TypedDict):
        active: NotRequired["bool"]
        """
        The new active state for the gift card.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        metadata: NotRequired["Literal['']|Dict[str, str]"]
        """
        Set of [key-value pairs](https://stripe.com/docs/api/metadata) that you can attach to an object. This can be useful for storing additional information about the object in a structured format. Individual keys can be unset by posting an empty value to them. All keys can be unset by posting an empty value to `metadata`.
        """

    class ValidateParams(TypedDict):
        code: str
        """
        The gift card code to be validated.
        """
        expand: NotRequired["List[str]"]
        """
        Specifies which fields in the response should be expanded.
        """
        giftcard_pin: NotRequired["str"]
        """
        The pin associated with the gift card. Not all gift cards have pins.
        """

    def list(
        self,
        params: "CardService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[Card]:
        """
        List gift cards for an account
        """
        return cast(
            ListObject[Card],
            self._request(
                "get",
                "/v1/gift_cards/cards",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "CardService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[Card]:
        """
        List gift cards for an account
        """
        return cast(
            ListObject[Card],
            await self._request_async(
                "get",
                "/v1/gift_cards/cards",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self, params: "CardService.CreateParams", options: RequestOptions = {}
    ) -> Card:
        """
        Creates a new gift card object.
        """
        return cast(
            Card,
            self._request(
                "post",
                "/v1/gift_cards/cards",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self, params: "CardService.CreateParams", options: RequestOptions = {}
    ) -> Card:
        """
        Creates a new gift card object.
        """
        return cast(
            Card,
            await self._request_async(
                "post",
                "/v1/gift_cards/cards",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: "CardService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> Card:
        """
        Retrieve a gift card by id
        """
        return cast(
            Card,
            self._request(
                "get",
                "/v1/gift_cards/cards/{id}".format(id=sanitize_id(id)),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: "CardService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> Card:
        """
        Retrieve a gift card by id
        """
        return cast(
            Card,
            await self._request_async(
                "get",
                "/v1/gift_cards/cards/{id}".format(id=sanitize_id(id)),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        id: str,
        params: "CardService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> Card:
        """
        Update a gift card
        """
        return cast(
            Card,
            self._request(
                "post",
                "/v1/gift_cards/cards/{id}".format(id=sanitize_id(id)),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        id: str,
        params: "CardService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> Card:
        """
        Update a gift card
        """
        return cast(
            Card,
            await self._request_async(
                "post",
                "/v1/gift_cards/cards/{id}".format(id=sanitize_id(id)),
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def validate(
        self,
        params: "CardService.ValidateParams",
        options: RequestOptions = {},
    ) -> Card:
        """
        Validates a gift card code, returning the matching gift card object if it exists.
        """
        return cast(
            Card,
            self._request(
                "post",
                "/v1/gift_cards/cards/validate",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def validate_async(
        self,
        params: "CardService.ValidateParams",
        options: RequestOptions = {},
    ) -> Card:
        """
        Validates a gift card code, returning the matching gift card object if it exists.
        """
        return cast(
            Card,
            await self._request_async(
                "post",
                "/v1/gift_cards/cards/validate",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )
