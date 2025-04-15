# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._invoice_payment import InvoicePayment
from stripe._list_object import ListObject
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import List, cast
from typing_extensions import Literal, NotRequired, TypedDict


class InvoicePaymentService(StripeService):
    class ListParams(TypedDict):
        ending_before: NotRequired[str]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        invoice: NotRequired[str]
        """
        The identifier of the invoice whose payments to return.
        """
        limit: NotRequired[int]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        payment: NotRequired["InvoicePaymentService.ListParamsPayment"]
        """
        The payment details of the invoice payments to return.
        """
        starting_after: NotRequired[str]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """
        status: NotRequired[Literal["canceled", "open", "paid"]]
        """
        The status of the invoice payments to return.
        """

    class ListParamsPayment(TypedDict):
        payment_intent: NotRequired[str]
        """
        Only return invoice payments associated by this payment intent ID.
        """
        type: Literal["payment_intent"]
        """
        Only return invoice payments associated by this payment type.
        """

    class RetrieveParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    def list(
        self,
        params: "InvoicePaymentService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[InvoicePayment]:
        """
        When retrieving an invoice, there is an includable payments property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of payments.
        """
        return cast(
            ListObject[InvoicePayment],
            self._request(
                "get",
                "/v1/invoice_payments",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "InvoicePaymentService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[InvoicePayment]:
        """
        When retrieving an invoice, there is an includable payments property containing the first handful of those items. There is also a URL where you can retrieve the full (paginated) list of payments.
        """
        return cast(
            ListObject[InvoicePayment],
            await self._request_async(
                "get",
                "/v1/invoice_payments",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        invoice_payment: str,
        params: "InvoicePaymentService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> InvoicePayment:
        """
        Retrieves the invoice payment with the given ID.
        """
        return cast(
            InvoicePayment,
            self._request(
                "get",
                "/v1/invoice_payments/{invoice_payment}".format(
                    invoice_payment=sanitize_id(invoice_payment),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        invoice_payment: str,
        params: "InvoicePaymentService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> InvoicePayment:
        """
        Retrieves the invoice payment with the given ID.
        """
        return cast(
            InvoicePayment,
            await self._request_async(
                "get",
                "/v1/invoice_payments/{invoice_payment}".format(
                    invoice_payment=sanitize_id(invoice_payment),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
