# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._encode import _coerce_v2_params
from stripe._stripe_service import StripeService
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.provisioning._payment_method_request_create_params import (
        PaymentMethodRequestCreateParams,
    )
    from stripe.v2.provisioning._payment_method_request import (
        PaymentMethodRequest,
    )


class PaymentMethodRequestService(StripeService):
    def create(
        self,
        params: Optional["PaymentMethodRequestCreateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentMethodRequest":
        """
        Creates a request for a customer to authorize a new payment method.
        """
        return cast(
            "PaymentMethodRequest",
            self._request(
                "post",
                "/v2/provisioning/payment_method_requests",
                base_address="api",
                params=_coerce_v2_params(
                    params,
                    {"usage_limits": {"max_amount": "int64_string"}},
                ),
                options=options,
            ),
        )

    async def create_async(
        self,
        params: Optional["PaymentMethodRequestCreateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "PaymentMethodRequest":
        """
        Creates a request for a customer to authorize a new payment method.
        """
        return cast(
            "PaymentMethodRequest",
            await self._request_async(
                "post",
                "/v2/provisioning/payment_method_requests",
                base_address="api",
                params=_coerce_v2_params(
                    params,
                    {"usage_limits": {"max_amount": "int64_string"}},
                ),
                options=options,
            ),
        )
