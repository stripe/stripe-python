# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._encode import _coerce_v2_params
from stripe._stripe_service import StripeService
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.provisioning.payment_profile._update_limit_update_params import (
        UpdateLimitUpdateParams,
    )
    from stripe.v2.provisioning._payment_profile import PaymentProfile


class UpdateLimitService(StripeService):
    def update(
        self,
        params: "UpdateLimitUpdateParams",
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

    async def update_async(
        self,
        params: "UpdateLimitUpdateParams",
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
