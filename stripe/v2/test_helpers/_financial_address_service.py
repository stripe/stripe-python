# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.test_helpers._financial_address_credit_params import (
        FinancialAddressCreditParams,
    )
    from stripe.params.v2.test_helpers._financial_address_generate_microdeposits_params import (
        FinancialAddressGenerateMicrodepositsParams,
    )
    from stripe.v2._financial_address_credit_simulation import (
        FinancialAddressCreditSimulation,
    )
    from stripe.v2._financial_address_generated_microdeposits import (
        FinancialAddressGeneratedMicrodeposits,
    )


class FinancialAddressService(StripeService):
    def credit(
        self,
        id: str,
        params: "FinancialAddressCreditParams",
        options: Optional["RequestOptions"] = None,
    ) -> "FinancialAddressCreditSimulation":
        """
        Simulate crediting a FinancialAddress in a Sandbox environment. This can be used to add virtual funds and increase your balance for testing.
        """
        return cast(
            "FinancialAddressCreditSimulation",
            self._request(
                "post",
                "/v2/test_helpers/financial_addresses/{id}/credit".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def credit_async(
        self,
        id: str,
        params: "FinancialAddressCreditParams",
        options: Optional["RequestOptions"] = None,
    ) -> "FinancialAddressCreditSimulation":
        """
        Simulate crediting a FinancialAddress in a Sandbox environment. This can be used to add virtual funds and increase your balance for testing.
        """
        return cast(
            "FinancialAddressCreditSimulation",
            await self._request_async(
                "post",
                "/v2/test_helpers/financial_addresses/{id}/credit".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def generate_microdeposits(
        self,
        id: str,
        params: Optional["FinancialAddressGenerateMicrodepositsParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "FinancialAddressGeneratedMicrodeposits":
        """
        Generates microdeposits for a FinancialAddress in a Sandbox environment.
        """
        return cast(
            "FinancialAddressGeneratedMicrodeposits",
            self._request(
                "post",
                "/v2/test_helpers/financial_addresses/{id}/generate_microdeposits".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def generate_microdeposits_async(
        self,
        id: str,
        params: Optional["FinancialAddressGenerateMicrodepositsParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "FinancialAddressGeneratedMicrodeposits":
        """
        Generates microdeposits for a FinancialAddress in a Sandbox environment.
        """
        return cast(
            "FinancialAddressGeneratedMicrodeposits",
            await self._request_async(
                "post",
                "/v2/test_helpers/financial_addresses/{id}/generate_microdeposits".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
