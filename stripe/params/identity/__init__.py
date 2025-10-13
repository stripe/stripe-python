# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.identity._verification_report_list_params import (
        VerificationReportListParams as VerificationReportListParams,
        VerificationReportListParamsCreated as VerificationReportListParamsCreated,
    )
    from stripe.params.identity._verification_report_retrieve_params import (
        VerificationReportRetrieveParams as VerificationReportRetrieveParams,
    )
    from stripe.params.identity._verification_session_cancel_params import (
        VerificationSessionCancelParams as VerificationSessionCancelParams,
    )
    from stripe.params.identity._verification_session_create_params import (
        VerificationSessionCreateParams as VerificationSessionCreateParams,
        VerificationSessionCreateParamsOptions as VerificationSessionCreateParamsOptions,
        VerificationSessionCreateParamsOptionsDocument as VerificationSessionCreateParamsOptionsDocument,
        VerificationSessionCreateParamsProvidedDetails as VerificationSessionCreateParamsProvidedDetails,
        VerificationSessionCreateParamsRelatedPerson as VerificationSessionCreateParamsRelatedPerson,
    )
    from stripe.params.identity._verification_session_list_params import (
        VerificationSessionListParams as VerificationSessionListParams,
        VerificationSessionListParamsCreated as VerificationSessionListParamsCreated,
    )
    from stripe.params.identity._verification_session_modify_params import (
        VerificationSessionModifyParams as VerificationSessionModifyParams,
        VerificationSessionModifyParamsOptions as VerificationSessionModifyParamsOptions,
        VerificationSessionModifyParamsOptionsDocument as VerificationSessionModifyParamsOptionsDocument,
        VerificationSessionModifyParamsProvidedDetails as VerificationSessionModifyParamsProvidedDetails,
    )
    from stripe.params.identity._verification_session_redact_params import (
        VerificationSessionRedactParams as VerificationSessionRedactParams,
    )
    from stripe.params.identity._verification_session_retrieve_params import (
        VerificationSessionRetrieveParams as VerificationSessionRetrieveParams,
    )
    from stripe.params.identity._verification_session_update_params import (
        VerificationSessionUpdateParams as VerificationSessionUpdateParams,
        VerificationSessionUpdateParamsOptions as VerificationSessionUpdateParamsOptions,
        VerificationSessionUpdateParamsOptionsDocument as VerificationSessionUpdateParamsOptionsDocument,
        VerificationSessionUpdateParamsProvidedDetails as VerificationSessionUpdateParamsProvidedDetails,
    )

_submodules = {
    "VerificationReportListParams": "stripe.params.identity._verification_report_list_params",
    "VerificationReportListParamsCreated": "stripe.params.identity._verification_report_list_params",
    "VerificationReportRetrieveParams": "stripe.params.identity._verification_report_retrieve_params",
    "VerificationSessionCancelParams": "stripe.params.identity._verification_session_cancel_params",
    "VerificationSessionCreateParams": "stripe.params.identity._verification_session_create_params",
    "VerificationSessionCreateParamsOptions": "stripe.params.identity._verification_session_create_params",
    "VerificationSessionCreateParamsOptionsDocument": "stripe.params.identity._verification_session_create_params",
    "VerificationSessionCreateParamsProvidedDetails": "stripe.params.identity._verification_session_create_params",
    "VerificationSessionCreateParamsRelatedPerson": "stripe.params.identity._verification_session_create_params",
    "VerificationSessionListParams": "stripe.params.identity._verification_session_list_params",
    "VerificationSessionListParamsCreated": "stripe.params.identity._verification_session_list_params",
    "VerificationSessionModifyParams": "stripe.params.identity._verification_session_modify_params",
    "VerificationSessionModifyParamsOptions": "stripe.params.identity._verification_session_modify_params",
    "VerificationSessionModifyParamsOptionsDocument": "stripe.params.identity._verification_session_modify_params",
    "VerificationSessionModifyParamsProvidedDetails": "stripe.params.identity._verification_session_modify_params",
    "VerificationSessionRedactParams": "stripe.params.identity._verification_session_redact_params",
    "VerificationSessionRetrieveParams": "stripe.params.identity._verification_session_retrieve_params",
    "VerificationSessionUpdateParams": "stripe.params.identity._verification_session_update_params",
    "VerificationSessionUpdateParamsOptions": "stripe.params.identity._verification_session_update_params",
    "VerificationSessionUpdateParamsOptionsDocument": "stripe.params.identity._verification_session_update_params",
    "VerificationSessionUpdateParamsProvidedDetails": "stripe.params.identity._verification_session_update_params",
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
