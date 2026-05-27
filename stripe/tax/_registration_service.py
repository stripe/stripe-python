# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
import json
from stripe._api_version import _ApiVersion
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from uuid import uuid4
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._list_object import ListObject
    from stripe._request_options import RequestOptions
    from stripe.params.tax._registration_create_params import (
        RegistrationCreateParams,
    )
    from stripe.params.tax._registration_list_params import (
        RegistrationListParams,
    )
    from stripe.params.tax._registration_retrieve_params import (
        RegistrationRetrieveParams,
    )
    from stripe.params.tax._registration_update_params import (
        RegistrationUpdateParams,
    )
    from stripe.tax._registration import Registration


class RegistrationService(StripeService):
    def list(
        self,
        params: Optional["RegistrationListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Registration]":
        """
        Returns a list of Tax Registration objects.
        """
        return cast(
            "ListObject[Registration]",
            self._request(
                "get",
                "/v1/tax/registrations",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["RegistrationListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[Registration]":
        """
        Returns a list of Tax Registration objects.
        """
        return cast(
            "ListObject[Registration]",
            await self._request_async(
                "get",
                "/v1/tax/registrations",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "RegistrationCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Registration":
        """
        Creates a new Tax Registration object.
        """
        return cast(
            "Registration",
            self._request(
                "post",
                "/v1/tax/registrations",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "RegistrationCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "Registration":
        """
        Creates a new Tax Registration object.
        """
        return cast(
            "Registration",
            await self._request_async(
                "post",
                "/v1/tax/registrations",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["RegistrationRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Registration":
        """
        Returns a Tax Registration object.
        """
        return cast(
            "Registration",
            self._request(
                "get",
                "/v1/tax/registrations/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        id: str,
        params: Optional["RegistrationRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Registration":
        """
        Returns a Tax Registration object.
        """
        return cast(
            "Registration",
            await self._request_async(
                "get",
                "/v1/tax/registrations/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        id: str,
        params: Optional["RegistrationUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Registration":
        """
        Updates an existing Tax Registration object.

        A registration cannot be deleted after it has been created. If you wish to end a registration you may do so by setting expires_at.
        """
        return cast(
            "Registration",
            self._request(
                "post",
                "/v1/tax/registrations/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        id: str,
        params: Optional["RegistrationUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Registration":
        """
        Updates an existing Tax Registration object.

        A registration cannot be deleted after it has been created. If you wish to end a registration you may do so by setting expires_at.
        """
        return cast(
            "Registration",
            await self._request_async(
                "post",
                "/v1/tax/registrations/{id}".format(id=sanitize_id(id)),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def serialize_batch_create(
        self,
        params: Optional["RegistrationCreateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> str:
        """
        Serializes a Registration create request into a batch job JSONL line.
        """
        item_id = str(uuid4())
        stripe_version = (
            options.get("stripe_version") if options else None
        ) or _ApiVersion.CURRENT
        context = options.get("stripe_context") if options else None
        batch_request = {
            "id": item_id,
            "params": params,
            "stripe_version": stripe_version,
        }
        if context is not None:
            batch_request["context"] = context
        return json.dumps(batch_request)

    def serialize_batch_update(
        self,
        id: str,
        params: Optional["RegistrationUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> str:
        """
        Serializes a Registration update request into a batch job JSONL line.
        """
        item_id = str(uuid4())
        stripe_version = (
            options.get("stripe_version") if options else None
        ) or _ApiVersion.CURRENT
        context = options.get("stripe_context") if options else None
        batch_request = {
            "id": item_id,
            "path_params": {"id": id},
            "params": params,
            "stripe_version": stripe_version,
        }
        if context is not None:
            batch_request["context"] = context
        return json.dumps(batch_request)
