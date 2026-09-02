# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.tax._integration_configuration_retrieve_params import (
        IntegrationConfigurationRetrieveParams,
    )
    from stripe.params.v2.tax._integration_configuration_update_params import (
        IntegrationConfigurationUpdateParams,
    )
    from stripe.v2.tax._integration_configuration import (
        IntegrationConfiguration,
    )


class IntegrationConfigurationService(StripeService):
    def retrieve(
        self,
        params: Optional["IntegrationConfigurationRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "IntegrationConfiguration":
        """
        Retrieve the tax integration configuration for this account.
        """
        return cast(
            "IntegrationConfiguration",
            self._request(
                "get",
                "/v2/tax/integration_configurations",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        params: Optional["IntegrationConfigurationRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "IntegrationConfiguration":
        """
        Retrieve the tax integration configuration for this account.
        """
        return cast(
            "IntegrationConfiguration",
            await self._request_async(
                "get",
                "/v2/tax/integration_configurations",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        params: Optional["IntegrationConfigurationUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "IntegrationConfiguration":
        """
        Update the tax integration configuration for this account.
        """
        return cast(
            "IntegrationConfiguration",
            self._request(
                "post",
                "/v2/tax/integration_configurations",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        params: Optional["IntegrationConfigurationUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "IntegrationConfiguration":
        """
        Update the tax integration configuration for this account.
        """
        return cast(
            "IntegrationConfiguration",
            await self._request_async(
                "post",
                "/v2/tax/integration_configurations",
                base_address="api",
                params=params,
                options=options,
            ),
        )
