# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._list_object import ListObject
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.tax._form import Form
from typing import Any, List, cast
from typing_extensions import Literal, NotRequired, TypedDict


class FormService(StripeService):
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
        payee: "FormService.ListParamsPayee"
        """
        The payee whose volume is represented on the tax form.
        """
        starting_after: NotRequired[str]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """
        type: NotRequired[
            Literal[
                "au_serr",
                "ca_mrdp",
                "eu_dac7",
                "gb_mrdp",
                "nz_mrdp",
                "us_1099_k",
                "us_1099_misc",
                "us_1099_nec",
            ]
        ]
        """
        An optional filter on the list, based on the object `type` field. Without the filter, the list includes all current and future tax form types. If your integration expects only one type of tax form in the response, make sure to provide a type value in the request.
        """

    class ListParamsPayee(TypedDict):
        account: NotRequired[str]
        """
        The ID of the Stripe account whose forms will be retrieved.
        """
        external_reference: NotRequired[str]
        """
        The external reference to the payee whose forms will be retrieved.
        """
        type: NotRequired[Literal["account", "external_reference"]]
        """
        Specifies the payee type. Either `account` or `external_reference`.
        """

    class PdfParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    class RetrieveParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    def list(
        self, params: "FormService.ListParams", options: RequestOptions = {}
    ) -> ListObject[Form]:
        """
        Returns a list of tax forms which were previously created. The tax forms are returned in sorted order, with the oldest tax forms appearing first.
        """
        return cast(
            ListObject[Form],
            self._request(
                "get",
                "/v1/tax/forms",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self, params: "FormService.ListParams", options: RequestOptions = {}
    ) -> ListObject[Form]:
        """
        Returns a list of tax forms which were previously created. The tax forms are returned in sorted order, with the oldest tax forms appearing first.
        """
        return cast(
            ListObject[Form],
            await self._request_async(
                "get",
                "/v1/tax/forms",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: "FormService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> Form:
        """
        Retrieves the details of a tax form that has previously been created. Supply the unique tax form ID that was returned from your previous request, and Stripe will return the corresponding tax form information.
        """
        return cast(
            Form,
            self._request(
                "get",
                "/v1/tax/forms/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: "FormService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> Form:
        """
        Retrieves the details of a tax form that has previously been created. Supply the unique tax form ID that was returned from your previous request, and Stripe will return the corresponding tax form information.
        """
        return cast(
            Form,
            await self._request_async(
                "get",
                "/v1/tax/forms/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def pdf(
        self,
        id: str,
        params: "FormService.PdfParams" = {},
        options: RequestOptions = {},
    ) -> Any:
        """
        Download the PDF for a tax form.
        """
        return cast(
            Any,
            self._request_stream(
                "get",
                "/v1/tax/forms/{id}/pdf".format(id=sanitize_id(id)),
                base_address="files",
                params=params,
                options=options,
            ),
        )

    async def pdf_async(
        self,
        id: str,
        params: "FormService.PdfParams" = {},
        options: RequestOptions = {},
    ) -> Any:
        """
        Download the PDF for a tax form.
        """
        return cast(
            Any,
            await self._request_stream_async(
                "get",
                "/v1/tax/forms/{id}/pdf".format(id=sanitize_id(id)),
                base_address="files",
                params=params,
                options=options,
            ),
        )
