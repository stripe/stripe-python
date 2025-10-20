# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.money_management._payout_methods_bank_account_spec_retrieve_params import (
        PayoutMethodsBankAccountSpecRetrieveParams,
    )
    from stripe.v2.money_management._payout_methods_bank_account_spec import (
        PayoutMethodsBankAccountSpec,
    )


class PayoutMethodsBankAccountSpecService(StripeService):
    def retrieve(
        self,
        params: Optional["PayoutMethodsBankAccountSpecRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PayoutMethodsBankAccountSpec":
        """
        Fetch the specifications for a set of countries to know which
        credential fields are required, the validations for each fields, and how to translate these
        country-specific fields to the generic fields in the PayoutMethodBankAccount type.
        """
        return cast(
            "PayoutMethodsBankAccountSpec",
            self._request(
                "get",
                "/v2/money_management/payout_methods_bank_account_spec",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        params: Optional["PayoutMethodsBankAccountSpecRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PayoutMethodsBankAccountSpec":
        """
        Fetch the specifications for a set of countries to know which
        credential fields are required, the validations for each fields, and how to translate these
        country-specific fields to the generic fields in the PayoutMethodBankAccount type.
        """
        return cast(
            "PayoutMethodsBankAccountSpec",
            await self._request_async(
                "get",
                "/v2/money_management/payout_methods_bank_account_spec",
                base_address="api",
                params=params,
                options=options,
            ),
        )
