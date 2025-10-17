# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._fx_quote import FxQuote
    from stripe._list_object import ListObject
    from stripe._request_options import RequestOptions
    from stripe.params._fx_quote_create_params import FxQuoteCreateParams
    from stripe.params._fx_quote_list_params import FxQuoteListParams
    from stripe.params._fx_quote_retrieve_params import FxQuoteRetrieveParams


class FxQuoteService(StripeService):
    def list(
        self,
        params: Optional["FxQuoteListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[FxQuote]":
        """
        Returns a list of FX quotes that have been issued. The FX quotes are returned in sorted order, with the most recent FX quotes appearing first.
        """
        return cast(
            "ListObject[FxQuote]",
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
        params: Optional["FxQuoteListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[FxQuote]":
        """
        Returns a list of FX quotes that have been issued. The FX quotes are returned in sorted order, with the most recent FX quotes appearing first.
        """
        return cast(
            "ListObject[FxQuote]",
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
        params: "FxQuoteCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "FxQuote":
        """
        Creates an FX Quote object
        """
        return cast(
            "FxQuote",
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
        params: "FxQuoteCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "FxQuote":
        """
        Creates an FX Quote object
        """
        return cast(
            "FxQuote",
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
        params: Optional["FxQuoteRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "FxQuote":
        """
        Retrieve an FX Quote object
        """
        return cast(
            "FxQuote",
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
        params: Optional["FxQuoteRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "FxQuote":
        """
        Retrieve an FX Quote object
        """
        return cast(
            "FxQuote",
            await self._request_async(
                "get",
                "/v1/fx_quotes/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
