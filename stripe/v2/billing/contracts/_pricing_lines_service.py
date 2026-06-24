# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.v2.billing.contracts.pricing_lines._quantity_change_service import (
        QuantityChangeService,
    )

_subservices = {
    "quantity_changes": [
        "stripe.v2.billing.contracts.pricing_lines._quantity_change_service",
        "QuantityChangeService",
    ],
}


class PricingLinesService(StripeService):
    quantity_changes: "QuantityChangeService"

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
