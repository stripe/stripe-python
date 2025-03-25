# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.v2._amount import AmountParam
from stripe.v2._financial_address_credit_simulation import (
    FinancialAddressCreditSimulation,
)
from stripe.v2._financial_address_generated_microdeposits import (
    FinancialAddressGeneratedMicrodeposits,
)
from typing import cast
from typing_extensions import Literal, NotRequired, TypedDict


class FinancialAddressService(StripeService):
    class CreditParams(TypedDict):
        amount: AmountParam
        """
        Object containing the amount value and currency to credit.
        """
        network: Literal["ach", "fps", "rtp", "wire"]
        """
        Open Enum. The network to use in simulating the funds flow. This will be the reflected in the resulting ReceivedCredit.
        """
        statement_descriptor: NotRequired[str]
        """
        String explaining funds flow. Use this field to populate the statement descriptor of the ReceivedCredit created as an eventual result of this simulation.
        """

    class GenerateMicrodepositsParams(TypedDict):
        pass

    def credit(
        self,
        id: str,
        params: "FinancialAddressService.CreditParams",
        options: RequestOptions = {},
    ) -> FinancialAddressCreditSimulation:
        """
        Simulate crediting a FinancialAddress in a Sandbox environment. This can be used to add virtual funds and increase your balance for testing.
        """
        return cast(
            FinancialAddressCreditSimulation,
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
        params: "FinancialAddressService.CreditParams",
        options: RequestOptions = {},
    ) -> FinancialAddressCreditSimulation:
        """
        Simulate crediting a FinancialAddress in a Sandbox environment. This can be used to add virtual funds and increase your balance for testing.
        """
        return cast(
            FinancialAddressCreditSimulation,
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
        params: "FinancialAddressService.GenerateMicrodepositsParams" = {},
        options: RequestOptions = {},
    ) -> FinancialAddressGeneratedMicrodeposits:
        """
        Generates microdeposits for a FinancialAddress in a Sandbox environment.
        """
        return cast(
            FinancialAddressGeneratedMicrodeposits,
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
        params: "FinancialAddressService.GenerateMicrodepositsParams" = {},
        options: RequestOptions = {},
    ) -> FinancialAddressGeneratedMicrodeposits:
        """
        Generates microdeposits for a FinancialAddress in a Sandbox environment.
        """
        return cast(
            FinancialAddressGeneratedMicrodeposits,
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
