# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from typing import Optional, cast
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._request_options import RequestOptions
    from stripe.params.v2.provisioning._payment_profile_retrieve_params import (
        PaymentProfileRetrieveParams,
    )
    from stripe.v2.provisioning._payment_profile import PaymentProfile
    from stripe.v2.provisioning.payment_profile._update_limit_service import (
        UpdateLimitService,
    )

_subservices = {
    "update_limit": [
        "stripe.v2.provisioning.payment_profile._update_limit_service",
        "UpdateLimitService",
    ],
}


class PaymentProfileService(StripeService):
    update_limit: "UpdateLimitService"

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
