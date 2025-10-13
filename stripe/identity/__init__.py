# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.identity._verification_report import (
        VerificationReport as VerificationReport,
    )
    from stripe.identity._verification_report_service import (
        VerificationReportService as VerificationReportService,
    )
    from stripe.identity._verification_session import (
        VerificationSession as VerificationSession,
    )
    from stripe.identity._verification_session_service import (
        VerificationSessionService as VerificationSessionService,
    )

_submodules = {
    "VerificationReport": "stripe.identity._verification_report",
    "VerificationReportService": "stripe.identity._verification_report_service",
    "VerificationSession": "stripe.identity._verification_session",
    "VerificationSessionService": "stripe.identity._verification_session_service",
}
if not TYPE_CHECKING:

    def __getattr__(name):
        try:
            return getattr(
                import_module(_submodules[name]),
                name,
            )
        except KeyError:
            raise AttributeError(f"cannot import '{name}' from '{__name__}'")
