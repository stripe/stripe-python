# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.risk._form_retrieve_params import FormRetrieveParams
    from stripe.params.risk._form_update_params import FormUpdateParams
    from stripe.risk._form import Form


class FormService(StripeService):
    def retrieve(
        self,
        id: str,
        /,
        params: Optional["FormRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Form":
        """
        Retrieves a risk Form by ID.

        Error Codes

        | Code | HTTP status | Description |
        | — | — | — |
        | form_not_found | 400 | No Form matches the supplied ID. |
        """
        return cast(
            "Form",
            self._request(
                "get",
                "/v1/risk/forms/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        /,
        params: Optional["FormRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Form":
        """
        Retrieves a risk Form by ID.

        Error Codes

        | Code | HTTP status | Description |
        | — | — | — |
        | form_not_found | 400 | No Form matches the supplied ID. |
        """
        return cast(
            "Form",
            await self._request_async(
                "get",
                "/v1/risk/forms/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        id: str,
        /,
        params: Optional["FormUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Form":
        """
        Updates a risk Form with the connected account's response.

        Error Codes

        | Code | HTTP status | Description |
        | — | — | — |
        | form_not_found | 400 | No Form matches the supplied ID. |
        | form_closed | 400 | The Form is closed and cannot accept updates. |
        | invalid_field_for_form_type | 400 | A submitted field is not supported by this Form type. |
        | form_field_already_submitted | 400 | A submitted field has already been submitted. |
        | form_insufficient_fields | 400 | Required fields are missing for this Form type. |
        | resource_missing | 404 | A submitted file does not exist or is not accessible to the requesting account. |
        """
        return cast(
            "Form",
            self._request(
                "post",
                "/v1/risk/forms/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        id: str,
        /,
        params: Optional["FormUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Form":
        """
        Updates a risk Form with the connected account's response.

        Error Codes

        | Code | HTTP status | Description |
        | — | — | — |
        | form_not_found | 400 | No Form matches the supplied ID. |
        | form_closed | 400 | The Form is closed and cannot accept updates. |
        | invalid_field_for_form_type | 400 | A submitted field is not supported by this Form type. |
        | form_field_already_submitted | 400 | A submitted field has already been submitted. |
        | form_insufficient_fields | 400 | Required fields are missing for this Form type. |
        | resource_missing | 404 | A submitted file does not exist or is not accessible to the requesting account. |
        """
        return cast(
            "Form",
            await self._request_async(
                "post",
                "/v1/risk/forms/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
