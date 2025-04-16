# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._fx_quote import FxQuote
from stripe._list_object import ListObject
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import List, cast
from typing_extensions import Literal, NotRequired, TypedDict


class FxQuoteService(StripeService):
    class CreateParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        from_currencies: List[str]
        """
        A list of three letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be [supported currencies](https://stripe.com/docs/currencies).
        """
        lock_duration: Literal["day", "five_minutes", "hour", "none"]
        """
        The duration that you wish the quote to be locked for. The quote will be usable for the duration specified. The default is `none`. The maximum is 1 day.
        """
        to_currency: str
        """
        Three-letter [ISO currency code](https://www.iso.org/iso-4217-currency-codes.html), in lowercase. Must be a [supported currency](https://stripe.com/docs/currencies).
        """
        usage: NotRequired["FxQuoteService.CreateParamsUsage"]
        """
        The usage specific information for the quote.
        """

    class CreateParamsUsage(TypedDict):
        payment: NotRequired["FxQuoteService.CreateParamsUsagePayment"]
        """
        The payment transaction details that are intended for the FX Quote.
        """
        transfer: NotRequired["FxQuoteService.CreateParamsUsageTransfer"]
        """
        The transfer transaction details that are intended for the FX Quote.
        """
        type: Literal["payment", "transfer"]
        """
        Which transaction the FX Quote will be used for

        Can be “payment” | “transfer”
        """

    class CreateParamsUsagePayment(TypedDict):
        destination: NotRequired[str]
        """
        The Stripe account ID that the funds will be transferred to.

        This field should match the account ID that would be used in the PaymentIntent's transfer_data[destination] field.
        """
        on_behalf_of: NotRequired[str]
        """
        The Stripe account ID that these funds are intended for.

        This field should match the account ID that would be used in the PaymentIntent's on_behalf_of field.
        """

    class CreateParamsUsageTransfer(TypedDict):
        destination: str
        """
        The Stripe account ID that the funds will be transferred to.

        This field should match the account ID that would be used in the Transfer's destination field.
        """

    class ListParams(TypedDict):
        ending_before: NotRequired[str]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        limit: NotRequired[int]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        starting_after: NotRequired[str]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """

    class RetrieveParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    def list(
        self,
        params: "FxQuoteService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[FxQuote]:
        """
        Returns a list of FX quotes that have been issued. The FX quotes are returned in sorted order, with the most recent FX quotes appearing first.
        """
        return cast(
            ListObject[FxQuote],
            self._request(
                "get",
                "/v1/fx_quotes",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "FxQuoteService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[FxQuote]:
        """
        Returns a list of FX quotes that have been issued. The FX quotes are returned in sorted order, with the most recent FX quotes appearing first.
        """
        return cast(
            ListObject[FxQuote],
            await self._request_async(
                "get",
                "/v1/fx_quotes",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "FxQuoteService.CreateParams",
        options: RequestOptions = {},
    ) -> FxQuote:
        """
        Creates an FX Quote object
        """
        return cast(
            FxQuote,
            self._request(
                "post",
                "/v1/fx_quotes",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "FxQuoteService.CreateParams",
        options: RequestOptions = {},
    ) -> FxQuote:
        """
        Creates an FX Quote object
        """
        return cast(
            FxQuote,
            await self._request_async(
                "post",
                "/v1/fx_quotes",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: "FxQuoteService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> FxQuote:
        """
        Retrieve an FX Quote object
        """
        return cast(
            FxQuote,
            self._request(
                "get",
                "/v1/fx_quotes/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: "FxQuoteService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> FxQuote:
        """
        Retrieve an FX Quote object
        """
        return cast(
            FxQuote,
            await self._request_async(
                "get",
                "/v1/fx_quotes/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
