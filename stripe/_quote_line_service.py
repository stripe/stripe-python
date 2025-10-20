# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._list_object import ListObject
    from stripe._quote_line import QuoteLine
    from stripe._request_options import RequestOptions
    from stripe.params._quote_line_list_params import QuoteLineListParams


class QuoteLineService(StripeService):
    def list(
        self,
        quote: str,
        params: Optional["QuoteLineListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[QuoteLine]":
        """
        Retrieves a paginated list of lines for a quote. These lines describe changes that will be used to create new subscription schedules or update existing subscription schedules when the quote is accepted.
        """
        return cast(
            "ListObject[QuoteLine]",
            self._request(
                "get",
                "/v1/quotes/{quote}/lines".format(quote=sanitize_id(quote)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        quote: str,
        params: Optional["QuoteLineListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[QuoteLine]":
        """
        Retrieves a paginated list of lines for a quote. These lines describe changes that will be used to create new subscription schedules or update existing subscription schedules when the quote is accepted.
        """
        return cast(
            "ListObject[QuoteLine]",
            await self._request_async(
                "get",
                "/v1/quotes/{quote}/lines".format(quote=sanitize_id(quote)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
