# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.tax._operation_resolve_address_params import (
        OperationResolveAddressParams,
    )
    from stripe.v2.tax._operations_resolve_address_result import (
        OperationsResolveAddressResult,
    )


class OperationService(StripeService):
    def resolve_address(
        self,
        params: "OperationResolveAddressParams",
        options: Optional["RequestOptions"] = None,
    ) -> "OperationsResolveAddressResult":
        """
        Resolves an address to its tax precision level.
        """
        return cast(
            "OperationsResolveAddressResult",
            self._request(
                "post",
                "/v2/tax/operations/resolve_address",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def resolve_address_async(
        self,
        params: "OperationResolveAddressParams",
        options: Optional["RequestOptions"] = None,
    ) -> "OperationsResolveAddressResult":
        """
        Resolves an address to its tax precision level.
        """
        return cast(
            "OperationsResolveAddressResult",
            await self._request_async(
                "post",
                "/v2/tax/operations/resolve_address",
                base_address="api",
                params=params,
                options=options,
            ),
        )
