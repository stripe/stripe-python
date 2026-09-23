# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.financial_connections._consent import Consent
    from stripe.params.financial_connections._consent_create_params import (
        ConsentCreateParams,
    )
    from stripe.params.financial_connections._consent_retrieve_params import (
        ConsentRetrieveParams,
    )


class ConsentService(StripeService):
    def retrieve(
        self,
        consent: str,
        /,
        params: Optional["ConsentRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Consent":
        """
        Retrieves the details of a Financial Connections Consent.
        """
        return cast(
            "Consent",
            self._request(
                "get",
                "/v1/financial_connections/consents/{consent}".format(
                    consent=sanitize_id(consent),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        consent: str,
        /,
        params: Optional["ConsentRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Consent":
        """
        Retrieves the details of a Financial Connections Consent.
        """
        return cast(
            "Consent",
            await self._request_async(
                "get",
                "/v1/financial_connections/consents/{consent}".format(
                    consent=sanitize_id(consent),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "ConsentCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Consent":
        """
        Creates a Financial Connections Consent object for an account holder.
        """
        return cast(
            "Consent",
            self._request(
                "post",
                "/v1/financial_connections/consents",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "ConsentCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Consent":
        """
        Creates a Financial Connections Consent object for an account holder.
        """
        return cast(
            "Consent",
            await self._request_async(
                "post",
                "/v1/financial_connections/consents",
                base_address="api",
                params=params,
                options=options,
            ),
        )
