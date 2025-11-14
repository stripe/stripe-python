# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._list_object import ListObject
    from stripe._request_options import RequestOptions
    from stripe.financial_connections._institution import Institution
    from stripe.params.financial_connections._institution_list_params import (
        InstitutionListParams,
    )
    from stripe.params.financial_connections._institution_retrieve_params import (
        InstitutionRetrieveParams,
    )


class InstitutionService(StripeService):
    def list(
        self,
        params: Optional["InstitutionListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Institution]":
        """
        Returns a list of Financial Connections Institution objects.
        """
        return cast(
            "ListObject[Institution]",
            self._request(
                "get",
                "/v1/financial_connections/institutions",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["InstitutionListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Institution]":
        """
        Returns a list of Financial Connections Institution objects.
        """
        return cast(
            "ListObject[Institution]",
            await self._request_async(
                "get",
                "/v1/financial_connections/institutions",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        institution: str,
        params: Optional["InstitutionRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Institution":
        """
        Retrieves the details of a Financial Connections Institution.
        """
        return cast(
            "Institution",
            self._request(
                "get",
                "/v1/financial_connections/institutions/{institution}".format(
                    institution=sanitize_id(institution),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        institution: str,
        params: Optional["InstitutionRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Institution":
        """
        Retrieves the details of a Financial Connections Institution.
        """
        return cast(
            "Institution",
            await self._request_async(
                "get",
                "/v1/financial_connections/institutions/{institution}".format(
                    institution=sanitize_id(institution),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
