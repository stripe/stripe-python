# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from typing import Optional, cast
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.money_management._test_helper_earned_credits_params import (
        TestHelperEarnedCreditsParams,
    )
    from stripe.v2.money_management._earned_credit_simulation import (
        EarnedCreditSimulation,
    )
    from stripe.v2.money_management.test_helpers._financial_address_service import (
        FinancialAddressService,
    )

_subservices = {
    "financial_addresses": [
        "stripe.v2.money_management.test_helpers._financial_address_service",
        "FinancialAddressService",
    ],
}


class TestHelperService(StripeService):
    financial_addresses: "FinancialAddressService"

    def __init__(self, requestor):
        super().__init__(requestor)

    def __getattr__(self, name):
        try:
            import_from, service = _subservices[name]
            service_class = getattr(
                import_module(import_from),
                service,
            )
            setattr(
                self,
                name,
                service_class(self._requestor),
            )
            return getattr(self, name)
        except KeyError:
            raise AttributeError()

    def earned_credits(
        self,
        params: "TestHelperEarnedCreditsParams",
        options: Optional["RequestOptions"] = None,
    ) -> "EarnedCreditSimulation":
        """
        Creates an EarnedCredit in a Sandbox environment for testing purposes.
        """
        return cast(
            "EarnedCreditSimulation",
            self._request(
                "post",
                "/v2/money_management/test_helpers/earned_credits",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def earned_credits_async(
        self,
        params: "TestHelperEarnedCreditsParams",
        options: Optional["RequestOptions"] = None,
    ) -> "EarnedCreditSimulation":
        """
        Creates an EarnedCredit in a Sandbox environment for testing purposes.
        """
        return cast(
            "EarnedCreditSimulation",
            await self._request_async(
                "post",
                "/v2/money_management/test_helpers/earned_credits",
                base_address="api",
                params=params,
                options=options,
            ),
        )
