# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._list_object import ListObject
    from stripe._request_options import RequestOptions
    from stripe.params.tax._form_list_params import FormListParams
    from stripe.params.tax._form_pdf_params import FormPdfParams
    from stripe.params.tax._form_retrieve_params import FormRetrieveParams
    from stripe.tax._form import Form
    from typing import Any


class FormService(StripeService):
    def list(
        self,
        params: "FormListParams",
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Form]":
        """
        Returns a list of tax forms which were previously created. The tax forms are returned in sorted order, with the oldest tax forms appearing first.
        """
        return cast(
            "ListObject[Form]",
            self._request(
                "get",
                "/v1/tax/forms",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: "FormListParams",
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Form]":
        """
        Returns a list of tax forms which were previously created. The tax forms are returned in sorted order, with the oldest tax forms appearing first.
        """
        return cast(
            "ListObject[Form]",
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
        params: Optional["FormRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Form":
        """
        Retrieves the details of a tax form that has previously been created. Supply the unique tax form ID that was returned from your previous request, and Stripe will return the corresponding tax form information.
        """
        return cast(
            "Form",
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
        params: Optional["FormRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Form":
        """
        Retrieves the details of a tax form that has previously been created. Supply the unique tax form ID that was returned from your previous request, and Stripe will return the corresponding tax form information.
        """
        return cast(
            "Form",
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
        params: Optional["FormPdfParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Any":
        """
        Download the PDF for a tax form.
        """
        return cast(
            "Any",
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
        params: Optional["FormPdfParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Any":
        """
        Download the PDF for a tax form.
        """
        return cast(
            "Any",
            await self._request_stream_async(
                "get",
                "/v1/tax/forms/{id}/pdf".format(id=sanitize_id(id)),
                base_address="files",
                params=params,
                options=options,
            ),
        )
