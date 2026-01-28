# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.reserve._hold_service import HoldService
    from stripe.reserve._plan_service import PlanService
    from stripe.reserve._release_service import ReleaseService

_subservices = {
    "holds": ["stripe.reserve._hold_service", "HoldService"],
    "plans": ["stripe.reserve._plan_service", "PlanService"],
    "releases": ["stripe.reserve._release_service", "ReleaseService"],
}


class ReserveService(StripeService):
    holds: "HoldService"
    plans: "PlanService"
    releases: "ReleaseService"

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
