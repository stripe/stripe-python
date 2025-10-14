# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe.reporting._report_run_service import ReportRunService
from stripe.reporting._report_type_service import ReportTypeService
from importlib import import_module

_subservices = {
    "report_runs": ["stripe._account_service", "AccountService"],
    "report_types": ["stripe._account_service", "AccountService"],
}


class ReportingService(StripeService):
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
