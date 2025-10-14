# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe.identity._verification_report_service import (
    VerificationReportService,
)
from stripe.identity._verification_session_service import (
    VerificationSessionService,
)
from importlib import import_module

_subservices = {
    "verification_reports": ["stripe._account_service", "AccountService"],
    "verification_sessions": ["stripe._account_service", "AccountService"],
}


class IdentityService(StripeService):
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
