# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.provisioning._eligibility_retrieve_params import (
        EligibilityRetrieveParams,
    )
    from stripe.v2.provisioning._eligibility import Eligibility


class EligibilityService(StripeService):
    def retrieve(
        self,
        params: Optional["EligibilityRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Eligibility":
        """
        Checks whether a project is eligible to provision resources with a provider, including
        any outstanding KYC requirements that must be satisfied first.
        """
        return cast(
            "Eligibility",
            self._request(
                "get",
                "/v2/provisioning/eligibility",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        params: Optional["EligibilityRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "Eligibility":
        """
        Checks whether a project is eligible to provision resources with a provider, including
        any outstanding KYC requirements that must be satisfied first.
        """
        return cast(
            "Eligibility",
            await self._request_async(
                "get",
                "/v2/provisioning/eligibility",
                base_address="api",
                params=params,
                options=options,
            ),
        )
