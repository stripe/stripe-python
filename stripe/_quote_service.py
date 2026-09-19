# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._invoice_line_item import InvoiceLineItem
    from stripe._list_object import ListObject
    from stripe._quote import Quote
    from stripe._quote_computed_upfront_line_items_service import (
        QuoteComputedUpfrontLineItemsService,
    )
    from stripe._quote_line_item_service import QuoteLineItemService
    from stripe._quote_line_service import QuoteLineService
    from stripe._quote_preview_invoice_service import (
        QuotePreviewInvoiceService,
    )
    from stripe._quote_preview_subscription_schedule_service import (
        QuotePreviewSubscriptionScheduleService,
    )
    from stripe._request_options import RequestOptions
    from stripe.params._quote_accept_params import QuoteAcceptParams
    from stripe.params._quote_cancel_params import QuoteCancelParams
    from stripe.params._quote_create_params import QuoteCreateParams
    from stripe.params._quote_finalize_quote_params import (
        QuoteFinalizeQuoteParams,
    )
    from stripe.params._quote_list_params import QuoteListParams
    from stripe.params._quote_list_preview_invoice_lines_params import (
        QuoteListPreviewInvoiceLinesParams,
    )
    from stripe.params._quote_mark_draft_params import QuoteMarkDraftParams
    from stripe.params._quote_mark_stale_params import QuoteMarkStaleParams
    from stripe.params._quote_pdf_params import QuotePdfParams
    from stripe.params._quote_reestimate_params import QuoteReestimateParams
    from stripe.params._quote_retrieve_params import QuoteRetrieveParams
    from stripe.params._quote_update_params import QuoteUpdateParams
    from typing import Any

_subservices = {
    "computed_upfront_line_items": [
        "stripe._quote_computed_upfront_line_items_service",
        "QuoteComputedUpfrontLineItemsService",
    ],
    "lines": ["stripe._quote_line_service", "QuoteLineService"],
    "line_items": ["stripe._quote_line_item_service", "QuoteLineItemService"],
    "preview_invoices": [
        "stripe._quote_preview_invoice_service",
        "QuotePreviewInvoiceService",
    ],
    "preview_subscription_schedules": [
        "stripe._quote_preview_subscription_schedule_service",
        "QuotePreviewSubscriptionScheduleService",
    ],
}


class QuoteService(StripeService):
    computed_upfront_line_items: "QuoteComputedUpfrontLineItemsService"
    lines: "QuoteLineService"
    line_items: "QuoteLineItemService"
    preview_invoices: "QuotePreviewInvoiceService"
    preview_subscription_schedules: "QuotePreviewSubscriptionScheduleService"

    def __init__(self, requestor):
        super().__init__(requestor)

    def __getattr__(self, name):
        try:
            import_from, service = _subservices[name]
            service_class = getattr(
                import_module(import_from),
                service,
            )
            setattr(
                self,
                name,
                service_class(self._requestor),
            )
            return getattr(self, name)
        except KeyError:
            raise AttributeError()

    def list(
        self,
        params: Optional["QuoteListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Quote]":
        """
        Returns a list of your quotes.
        """
        return cast(
            "ListObject[Quote]",
            self._request(
                "get",
                "/v1/quotes",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["QuoteListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Quote]":
        """
        Returns a list of your quotes.
        """
        return cast(
            "ListObject[Quote]",
            await self._request_async(
                "get",
                "/v1/quotes",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: Optional["QuoteCreateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Quote":
        """
        A quote models prices and services for a customer. Default options for header, description, footer, and expires_at can be set in the dashboard via the [quote template](https://dashboard.stripe.com/settings/billing/quote).
        """
        return cast(
            "Quote",
            self._request(
                "post",
                "/v1/quotes",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: Optional["QuoteCreateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Quote":
        """
        A quote models prices and services for a customer. Default options for header, description, footer, and expires_at can be set in the dashboard via the [quote template](https://dashboard.stripe.com/settings/billing/quote).
        """
        return cast(
            "Quote",
            await self._request_async(
                "post",
                "/v1/quotes",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        /,
        params: Optional["QuoteRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Quote":
        """
        Retrieves the quote with the given ID.
        """
        return cast(
            "Quote",
            self._request(
                "get",
                "/v1/quotes/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        /,
        params: Optional["QuoteRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Quote":
        """
        Retrieves the quote with the given ID.
        """
        return cast(
            "Quote",
            await self._request_async(
                "get",
                "/v1/quotes/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        id: str,
        /,
        params: Optional["QuoteUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Quote":
        """
        A quote models prices and services for a customer.
        """
        return cast(
            "Quote",
            self._request(
                "post",
                "/v1/quotes/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        id: str,
        /,
        params: Optional["QuoteUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Quote":
        """
        A quote models prices and services for a customer.
        """
        return cast(
            "Quote",
            await self._request_async(
                "post",
                "/v1/quotes/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def accept(
        self,
        id: str,
        /,
        params: Optional["QuoteAcceptParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Quote":
        """
        Accepts the specified quote.
        """
        return cast(
            "Quote",
            self._request(
                "post",
                "/v1/quotes/{id}/accept".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def accept_async(
        self,
        id: str,
        /,
        params: Optional["QuoteAcceptParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Quote":
        """
        Accepts the specified quote.
        """
        return cast(
            "Quote",
            await self._request_async(
                "post",
                "/v1/quotes/{id}/accept".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def cancel(
        self,
        id: str,
        /,
        params: Optional["QuoteCancelParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Quote":
        """
        Cancels the quote.
        """
        return cast(
            "Quote",
            self._request(
                "post",
                "/v1/quotes/{id}/cancel".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def cancel_async(
        self,
        id: str,
        /,
        params: Optional["QuoteCancelParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Quote":
        """
        Cancels the quote.
        """
        return cast(
            "Quote",
            await self._request_async(
                "post",
                "/v1/quotes/{id}/cancel".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def finalize_quote(
        self,
        id: str,
        /,
        params: Optional["QuoteFinalizeQuoteParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Quote":
        """
        Finalizes the quote.
        """
        return cast(
            "Quote",
            self._request(
                "post",
                "/v1/quotes/{id}/finalize".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def finalize_quote_async(
        self,
        id: str,
        /,
        params: Optional["QuoteFinalizeQuoteParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Quote":
        """
        Finalizes the quote.
        """
        return cast(
            "Quote",
            await self._request_async(
                "post",
                "/v1/quotes/{id}/finalize".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def mark_draft(
        self,
        id: str,
        /,
        params: Optional["QuoteMarkDraftParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Quote":
        """
        Converts a stale quote to draft.
        """
        return cast(
            "Quote",
            self._request(
                "post",
                "/v1/quotes/{id}/mark_draft".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def mark_draft_async(
        self,
        id: str,
        /,
        params: Optional["QuoteMarkDraftParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Quote":
        """
        Converts a stale quote to draft.
        """
        return cast(
            "Quote",
            await self._request_async(
                "post",
                "/v1/quotes/{id}/mark_draft".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def mark_stale(
        self,
        id: str,
        /,
        params: Optional["QuoteMarkStaleParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Quote":
        """
        Converts a draft or open quote to stale.
        """
        return cast(
            "Quote",
            self._request(
                "post",
                "/v1/quotes/{id}/mark_stale".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def mark_stale_async(
        self,
        id: str,
        /,
        params: Optional["QuoteMarkStaleParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Quote":
        """
        Converts a draft or open quote to stale.
        """
        return cast(
            "Quote",
            await self._request_async(
                "post",
                "/v1/quotes/{id}/mark_stale".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def reestimate(
        self,
        id: str,
        /,
        params: Optional["QuoteReestimateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Quote":
        """
        Recompute the upcoming invoice estimate for the quote.
        """
        return cast(
            "Quote",
            self._request(
                "post",
                "/v1/quotes/{id}/reestimate".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def reestimate_async(
        self,
        id: str,
        /,
        params: Optional["QuoteReestimateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Quote":
        """
        Recompute the upcoming invoice estimate for the quote.
        """
        return cast(
            "Quote",
            await self._request_async(
                "post",
                "/v1/quotes/{id}/reestimate".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def pdf(
        self,
        id: str,
        /,
        params: Optional["QuotePdfParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Any":
        """
        Download the PDF for a finalized quote. Explanation for special handling can be found [here](https://docs.stripe.com/quotes/overview#quote_pdf)
        """
        return cast(
            "Any",
            self._request_stream(
                "get",
                "/v1/quotes/{id}/pdf".format(id=sanitize_id(id)),
                base_address="files",
                params=params,
                options=options,
            ),
        )

    async def pdf_async(
        self,
        id: str,
        /,
        params: Optional["QuotePdfParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Any":
        """
        Download the PDF for a finalized quote. Explanation for special handling can be found [here](https://docs.stripe.com/quotes/overview#quote_pdf)
        """
        return cast(
            "Any",
            await self._request_stream_async(
                "get",
                "/v1/quotes/{id}/pdf".format(id=sanitize_id(id)),
                base_address="files",
                params=params,
                options=options,
            ),
        )

    def list_preview_invoice_lines(
        self,
        quote_id: str,
        id: str,
        /,
        params: Optional["QuoteListPreviewInvoiceLinesParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[InvoiceLineItem]":
        """
        Preview the invoice line items that would be generated by accepting the quote.
        """
        return cast(
            "ListObject[InvoiceLineItem]",
            self._request(
                "get",
                "/v1/quotes/{quote_id}/preview_invoices/{id}/lines".format(
                    quote_id=sanitize_id(quote_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_preview_invoice_lines_async(
        self,
        quote_id: str,
        id: str,
        /,
        params: Optional["QuoteListPreviewInvoiceLinesParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[InvoiceLineItem]":
        """
        Preview the invoice line items that would be generated by accepting the quote.
        """
        return cast(
            "ListObject[InvoiceLineItem]",
            await self._request_async(
                "get",
                "/v1/quotes/{quote_id}/preview_invoices/{id}/lines".format(
                    quote_id=sanitize_id(quote_id),
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
