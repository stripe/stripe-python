# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.commerce.product_catalog._import_create_params import (
        ImportCreateParams,
    )
    from stripe.params.v2.commerce.product_catalog._import_list_params import (
        ImportListParams,
    )
    from stripe.params.v2.commerce.product_catalog._import_retrieve_params import (
        ImportRetrieveParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.commerce._product_catalog_import import ProductCatalogImport


class ImportService(StripeService):
    def list(
        self,
        params: Optional["ImportListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[ProductCatalogImport]":
        """
        Returns a list of ProductCatalogImport objects.
        """
        return cast(
            "ListObject[ProductCatalogImport]",
            self._request(
                "get",
                "/v2/commerce/product_catalog/imports",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["ImportListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[ProductCatalogImport]":
        """
        Returns a list of ProductCatalogImport objects.
        """
        return cast(
            "ListObject[ProductCatalogImport]",
            await self._request_async(
                "get",
                "/v2/commerce/product_catalog/imports",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "ImportCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "ProductCatalogImport":
        """
        Creates a ProductCatalogImport.
        """
        return cast(
            "ProductCatalogImport",
            self._request(
                "post",
                "/v2/commerce/product_catalog/imports",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "ImportCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "ProductCatalogImport":
        """
        Creates a ProductCatalogImport.
        """
        return cast(
            "ProductCatalogImport",
            await self._request_async(
                "post",
                "/v2/commerce/product_catalog/imports",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        id: str,
        params: Optional["ImportRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ProductCatalogImport":
        """
        Retrieves a ProductCatalogImport by ID.
        """
        return cast(
            "ProductCatalogImport",
            self._request(
                "get",
                "/v2/commerce/product_catalog/imports/{id}".format(
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
        params: Optional["ImportRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ProductCatalogImport":
        """
        Retrieves a ProductCatalogImport by ID.
        """
        return cast(
            "ProductCatalogImport",
            await self._request_async(
                "get",
                "/v2/commerce/product_catalog/imports/{id}".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
