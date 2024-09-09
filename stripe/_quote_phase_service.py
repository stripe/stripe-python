# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._quote_phase import QuotePhase
from stripe._quote_phase_line_item_service import QuotePhaseLineItemService
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import List, cast
from typing_extensions import NotRequired, TypedDict


class QuotePhaseService(StripeService):
    def __init__(self, requestor):
        super().__init__(requestor)
        self.line_items = QuotePhaseLineItemService(self._requestor)

    class RetrieveParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    def retrieve(
        self,
        quote_phase: str,
        params: "QuotePhaseService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> QuotePhase:
        """
        Retrieves the quote phase with the given ID.
        """
        return cast(
            QuotePhase,
            self._request(
                "get",
                "/v1/quote_phases/{quote_phase}".format(
                    quote_phase=sanitize_id(quote_phase),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        quote_phase: str,
        params: "QuotePhaseService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> QuotePhase:
        """
        Retrieves the quote phase with the given ID.
        """
        return cast(
            QuotePhase,
            await self._request_async(
                "get",
                "/v1/quote_phases/{quote_phase}".format(
                    quote_phase=sanitize_id(quote_phase),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
