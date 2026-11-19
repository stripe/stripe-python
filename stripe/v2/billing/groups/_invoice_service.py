# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.billing.groups._invoice_create_params import (
        InvoiceCreateParams,
    )
    from stripe.v2.billing._group_invoice import GroupInvoice


class InvoiceService(StripeService):
    def create(
        self,
        id: str,
        /,
        params: Optional["InvoiceCreateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "GroupInvoice":
        """
        Create an empty invoice using the billing group's settings.
        """
        return cast(
            "GroupInvoice",
            self._request(
                "post",
                "/v2/billing/groups/{id}/invoices".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        id: str,
        /,
        params: Optional["InvoiceCreateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "GroupInvoice":
        """
        Create an empty invoice using the billing group's settings.
        """
        return cast(
            "GroupInvoice",
            await self._request_async(
                "post",
                "/v2/billing/groups/{id}/invoices".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
