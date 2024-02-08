# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._list_object import ListObject
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
        quote: str
        """
        The ID of the quote whose phases will be retrieved.
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

    def list(
        self,
        params: "QuotePhaseService.ListParams",
        options: RequestOptions = {},
    ) -> ListObject[QuotePhase]:
        """
        Returns a list of quote phases.
        """
        return cast(
            ListObject[QuotePhase],
            self._request(
                "get",
                "/v1/quote_phases",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "QuotePhaseService.ListParams",
        options: RequestOptions = {},
    ) -> ListObject[QuotePhase]:
        """
        Returns a list of quote phases.
        """
        return cast(
            ListObject[QuotePhase],
            await self._request_async(
                "get",
                "/v1/quote_phases",
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )

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
                api_mode="V1",
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
                api_mode="V1",
                base_address="api",
                params=params,
                options=options,
            ),
        )
