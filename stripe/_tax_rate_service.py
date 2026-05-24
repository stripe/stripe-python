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
    from stripe._tax_rate import TaxRate
    from stripe.params._tax_rate_create_params import TaxRateCreateParams
    from stripe.params._tax_rate_list_params import TaxRateListParams
    from stripe.params._tax_rate_retrieve_params import TaxRateRetrieveParams
    from stripe.params._tax_rate_update_params import TaxRateUpdateParams


class TaxRateService(StripeService):
    def list(
        self,
        params: Optional["TaxRateListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[TaxRate]":
        """
        Returns a list of your tax rates. Tax rates are returned sorted by creation date, with the most recently created tax rates appearing first.
        """
        return cast(
            "ListObject[TaxRate]",
            self._request(
                "get",
                "/v1/tax_rates",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["TaxRateListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[TaxRate]":
        """
        Returns a list of your tax rates. Tax rates are returned sorted by creation date, with the most recently created tax rates appearing first.
        """
        return cast(
            "ListObject[TaxRate]",
            await self._request_async(
                "get",
                "/v1/tax_rates",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "TaxRateCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "TaxRate":
        """
        Creates a new tax rate.
        """
        return cast(
            "TaxRate",
            self._request(
                "post",
                "/v1/tax_rates",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "TaxRateCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "TaxRate":
        """
        Creates a new tax rate.
        """
        return cast(
            "TaxRate",
            await self._request_async(
                "post",
                "/v1/tax_rates",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        tax_rate: str,
        params: Optional["TaxRateRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "TaxRate":
        """
        Retrieves a tax rate with the given ID
        """
        return cast(
            "TaxRate",
            self._request(
                "get",
                "/v1/tax_rates/{tax_rate}".format(
                    tax_rate=sanitize_id(tax_rate),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        tax_rate: str,
        params: Optional["TaxRateRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "TaxRate":
        """
        Retrieves a tax rate with the given ID
        """
        return cast(
            "TaxRate",
            await self._request_async(
                "get",
                "/v1/tax_rates/{tax_rate}".format(
                    tax_rate=sanitize_id(tax_rate),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        tax_rate: str,
        params: Optional["TaxRateUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "TaxRate":
        """
        Updates an existing tax rate.
        """
        return cast(
            "TaxRate",
            self._request(
                "post",
                "/v1/tax_rates/{tax_rate}".format(
                    tax_rate=sanitize_id(tax_rate),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        tax_rate: str,
        params: Optional["TaxRateUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "TaxRate":
        """
        Updates an existing tax rate.
        """
        return cast(
            "TaxRate",
            await self._request_async(
                "post",
                "/v1/tax_rates/{tax_rate}".format(
                    tax_rate=sanitize_id(tax_rate),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def serialize_batch_create(
        self,
        params: Optional["TaxRateCreateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> str:
        """
        Serializes a TaxRate create request into a batch job JSONL line.
        """
        item_id = str(uuid4())
        stripe_version = (
            options.get("stripe_version") if options else None
        ) or _ApiVersion.CURRENT
        context = options.get("stripe_context") if options else None
        item = {
            "id": item_id,
            "params": params,
            "stripe_version": stripe_version,
        }
        if context is not None:
            item["context"] = context
        return json.dumps(item)

    def serialize_batch_update(
        self,
        tax_rate: str,
        params: Optional["TaxRateUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> str:
        """
        Serializes a TaxRate update request into a batch job JSONL line.
        """
        item_id = str(uuid4())
        stripe_version = (
            options.get("stripe_version") if options else None
        ) or _ApiVersion.CURRENT
        context = options.get("stripe_context") if options else None
        item = {
            "id": item_id,
            "path_params": {"tax_rate": tax_rate},
            "params": params,
            "stripe_version": stripe_version,
        }
        if context is not None:
            item["context"] = context
        return json.dumps(item)
