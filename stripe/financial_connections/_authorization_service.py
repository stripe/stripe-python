# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.financial_connections._authorization import Authorization
    from stripe.params.financial_connections._authorization_retrieve_params import (
        AuthorizationRetrieveParams,
    )


class AuthorizationService(StripeService):
    def retrieve(
        self,
        authorization: str,
        params: Optional["AuthorizationRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Authorization":
        """
        Retrieves the details of an Financial Connections Authorization.
        """
        return cast(
            "Authorization",
            self._request(
                "get",
                "/v1/financial_connections/authorizations/{authorization}".format(
                    authorization=sanitize_id(authorization),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        authorization: str,
        params: Optional["AuthorizationRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Authorization":
        """
        Retrieves the details of an Financial Connections Authorization.
        """
        return cast(
            "Authorization",
            await self._request_async(
                "get",
                "/v1/financial_connections/authorizations/{authorization}".format(
                    authorization=sanitize_id(authorization),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
