# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.provisioning.catalog._service_list_params import (
        ServiceListParams,
    )
    from stripe.v2._list_object import ListObject
    from stripe.v2.provisioning._provider_service_detail import (
        ProviderServiceDetail,
    )


class ServiceService(StripeService):
    def list(
        self,
        params: Optional["ServiceListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[ProviderServiceDetail]":
        """
        Lists services available in the catalog.
        """
        return cast(
            "ListObject[ProviderServiceDetail]",
            self._request(
                "get",
                "/v2/provisioning/catalog/services",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["ServiceListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[ProviderServiceDetail]":
        """
        Lists services available in the catalog.
        """
        return cast(
            "ListObject[ProviderServiceDetail]",
            await self._request_async(
                "get",
                "/v2/provisioning/catalog/services",
                base_address="api",
                params=params,
                options=options,
            ),
        )
