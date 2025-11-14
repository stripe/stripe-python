# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.billing._cadence_cancel_params import (
        CadenceCancelParams,
    )
    from stripe.params.v2.billing._cadence_create_params import (
        CadenceCreateParams,
    )
    from stripe.params.v2.billing._cadence_list_params import CadenceListParams
    from stripe.params.v2.billing._cadence_retrieve_params import (
        CadenceRetrieveParams,
    )
    from stripe.params.v2.billing._cadence_update_params import (
        CadenceUpdateParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.billing._cadence import Cadence


class CadenceService(StripeService):
    def list(
        self,
        params: Optional["CadenceListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Cadence]":
        """
        List Billing Cadences.
        """
        return cast(
            "ListObject[Cadence]",
            self._request(
                "get",
                "/v2/billing/cadences",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["CadenceListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Cadence]":
        """
        List Billing Cadences.
        """
        return cast(
            "ListObject[Cadence]",
            await self._request_async(
                "get",
                "/v2/billing/cadences",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "CadenceCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Cadence":
        """
        Create a Billing Cadence object.
        """
        return cast(
            "Cadence",
            self._request(
                "post",
                "/v2/billing/cadences",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "CadenceCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Cadence":
        """
        Create a Billing Cadence object.
        """
        return cast(
            "Cadence",
            await self._request_async(
                "post",
                "/v2/billing/cadences",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["CadenceRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Cadence":
        """
        Retrieve a Billing Cadence object.
        """
        return cast(
            "Cadence",
            self._request(
                "get",
                "/v2/billing/cadences/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: Optional["CadenceRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Cadence":
        """
        Retrieve a Billing Cadence object.
        """
        return cast(
            "Cadence",
            await self._request_async(
                "get",
                "/v2/billing/cadences/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        id: str,
        params: Optional["CadenceUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Cadence":
        """
        Update a Billing Cadence object.
        """
        return cast(
            "Cadence",
            self._request(
                "post",
                "/v2/billing/cadences/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        id: str,
        params: Optional["CadenceUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Cadence":
        """
        Update a Billing Cadence object.
        """
        return cast(
            "Cadence",
            await self._request_async(
                "post",
                "/v2/billing/cadences/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def cancel(
        self,
        id: str,
        params: Optional["CadenceCancelParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Cadence":
        """
        Cancel the Billing Cadence.
        """
        return cast(
            "Cadence",
            self._request(
                "post",
                "/v2/billing/cadences/{id}/cancel".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def cancel_async(
        self,
        id: str,
        params: Optional["CadenceCancelParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Cadence":
        """
        Cancel the Billing Cadence.
        """
        return cast(
            "Cadence",
            await self._request_async(
                "post",
                "/v2/billing/cadences/{id}/cancel".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )
