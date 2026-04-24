# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.orchestrated_commerce._agreement_confirm_params import (
        AgreementConfirmParams,
    )
    from stripe.params.v2.orchestrated_commerce._agreement_create_params import (
        AgreementCreateParams,
    )
    from stripe.params.v2.orchestrated_commerce._agreement_list_params import (
        AgreementListParams,
    )
    from stripe.params.v2.orchestrated_commerce._agreement_retrieve_params import (
        AgreementRetrieveParams,
    )
    from stripe.params.v2.orchestrated_commerce._agreement_terminate_params import (
        AgreementTerminateParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.orchestrated_commerce._agreement import Agreement


class AgreementService(StripeService):
    def list(
        self,
        params: Optional["AgreementListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Agreement]":
        """
        List Agreements for the profile associated with the authenticated merchant.
        """
        return cast(
            "ListObject[Agreement]",
            self._request(
                "get",
                "/v2/orchestrated_commerce/agreements",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["AgreementListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Agreement]":
        """
        List Agreements for the profile associated with the authenticated merchant.
        """
        return cast(
            "ListObject[Agreement]",
            await self._request_async(
                "get",
                "/v2/orchestrated_commerce/agreements",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "AgreementCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Agreement":
        """
        Create a new Agreement.
        """
        return cast(
            "Agreement",
            self._request(
                "post",
                "/v2/orchestrated_commerce/agreements",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "AgreementCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Agreement":
        """
        Create a new Agreement.
        """
        return cast(
            "Agreement",
            await self._request_async(
                "post",
                "/v2/orchestrated_commerce/agreements",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["AgreementRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Agreement":
        """
        Retrieve an Agreement by ID.
        """
        return cast(
            "Agreement",
            self._request(
                "get",
                "/v2/orchestrated_commerce/agreements/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: Optional["AgreementRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Agreement":
        """
        Retrieve an Agreement by ID.
        """
        return cast(
            "Agreement",
            await self._request_async(
                "get",
                "/v2/orchestrated_commerce/agreements/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def confirm(
        self,
        id: str,
        params: Optional["AgreementConfirmParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Agreement":
        """
        Confirm an Agreement.
        """
        return cast(
            "Agreement",
            self._request(
                "post",
                "/v2/orchestrated_commerce/agreements/{id}/confirm".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def confirm_async(
        self,
        id: str,
        params: Optional["AgreementConfirmParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Agreement":
        """
        Confirm an Agreement.
        """
        return cast(
            "Agreement",
            await self._request_async(
                "post",
                "/v2/orchestrated_commerce/agreements/{id}/confirm".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def terminate(
        self,
        id: str,
        params: Optional["AgreementTerminateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Agreement":
        """
        Terminate an Agreement.
        """
        return cast(
            "Agreement",
            self._request(
                "post",
                "/v2/orchestrated_commerce/agreements/{id}/terminate".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def terminate_async(
        self,
        id: str,
        params: Optional["AgreementTerminateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Agreement":
        """
        Terminate an Agreement.
        """
        return cast(
            "Agreement",
            await self._request_async(
                "post",
                "/v2/orchestrated_commerce/agreements/{id}/terminate".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
