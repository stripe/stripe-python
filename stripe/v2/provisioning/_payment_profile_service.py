# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._encode import _coerce_v2_params
from stripe._stripe_service import StripeService
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.provisioning._payment_profile_retrieve_params import (
        PaymentProfileRetrieveParams,
    )
    from stripe.params.v2.provisioning._payment_profile_update_limit_params import (
        PaymentProfileUpdateLimitParams,
    )
    from stripe.v2.provisioning._payment_profile import PaymentProfile


class PaymentProfileService(StripeService):
    def retrieve(
        self,
        params: Optional["PaymentProfileRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentProfile":
        """
        Retrieves the payment profile for the current project.
        """
        return cast(
            "PaymentProfile",
            self._request(
                "get",
                "/v2/provisioning/payment_profile",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        params: Optional["PaymentProfileRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentProfile":
        """
        Retrieves the payment profile for the current project.
        """
        return cast(
            "PaymentProfile",
            await self._request_async(
                "get",
                "/v2/provisioning/payment_profile",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update_limit(
        self,
        params: "PaymentProfileUpdateLimitParams",
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentProfile":
        """
        Updates the usage limit on the payment profile for a provider.
        """
        return cast(
            "PaymentProfile",
            self._request(
                "post",
                "/v2/provisioning/payment_profile/update_limit",
                base_address="api",
                params=_coerce_v2_params(
                    params,
                    {"usage_limits": {"max_amount": "int64_string"}},
                ),
                options=options,
            ),
        )

    async def update_limit_async(
        self,
        params: "PaymentProfileUpdateLimitParams",
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentProfile":
        """
        Updates the usage limit on the payment profile for a provider.
        """
        return cast(
            "PaymentProfile",
            await self._request_async(
                "post",
                "/v2/provisioning/payment_profile/update_limit",
                base_address="api",
                params=_coerce_v2_params(
                    params,
                    {"usage_limits": {"max_amount": "int64_string"}},
                ),
                options=options,
            ),
        )
