# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.money_management.test_helpers._financial_address_debit_params import (
        FinancialAddressDebitParams,
    )
    from stripe.v2.money_management._financial_address_debit_simulation import (
        FinancialAddressDebitSimulation,
    )


class FinancialAddressService(StripeService):
    def debit(
        self,
        id: str,
        params: "FinancialAddressDebitParams",
        options: Optional["RequestOptions"] = None,
    ) -> "FinancialAddressDebitSimulation":
        """
        Simulate debiting a FinancialAddress in a Sandbox environment. This can be used to remove virtual funds and decrease your balance for testing.
        """
        return cast(
            "FinancialAddressDebitSimulation",
            self._request(
                "post",
                "/v2/money_management/test_helpers/financial_addresses/{id}/debit".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def debit_async(
        self,
        id: str,
        params: "FinancialAddressDebitParams",
        options: Optional["RequestOptions"] = None,
    ) -> "FinancialAddressDebitSimulation":
        """
        Simulate debiting a FinancialAddress in a Sandbox environment. This can be used to remove virtual funds and decrease your balance for testing.
        """
        return cast(
            "FinancialAddressDebitSimulation",
            await self._request_async(
                "post",
                "/v2/money_management/test_helpers/financial_addresses/{id}/debit".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
