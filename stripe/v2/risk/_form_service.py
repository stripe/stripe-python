# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.risk._form_retrieve_params import FormRetrieveParams
    from stripe.params.v2.risk._form_update_params import FormUpdateParams
    from stripe.v2.risk._form import Form


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
        """
        return cast(
            "Form",
            self._request(
                "get",
                "/v2/risk/forms/{id}".format(id=sanitize_id(id)),
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
        """
        return cast(
            "Form",
            await self._request_async(
                "get",
                "/v2/risk/forms/{id}".format(id=sanitize_id(id)),
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
        Submits a response to a risk Form.
        """
        return cast(
            "Form",
            self._request(
                "post",
                "/v2/risk/forms/{id}".format(id=sanitize_id(id)),
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
        Submits a response to a risk Form.
        """
        return cast(
            "Form",
            await self._request_async(
                "post",
                "/v2/risk/forms/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
