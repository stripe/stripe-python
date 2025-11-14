# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.params.privacy._redaction_job_cancel_params import (
        RedactionJobCancelParams as RedactionJobCancelParams,
    )
    from stripe.params.privacy._redaction_job_create_params import (
        RedactionJobCreateParams as RedactionJobCreateParams,
        RedactionJobCreateParamsObjects as RedactionJobCreateParamsObjects,
    )
    from stripe.params.privacy._redaction_job_list_params import (
        RedactionJobListParams as RedactionJobListParams,
    )
    from stripe.params.privacy._redaction_job_list_validation_errors_params import (
        RedactionJobListValidationErrorsParams as RedactionJobListValidationErrorsParams,
    )
    from stripe.params.privacy._redaction_job_modify_params import (
        RedactionJobModifyParams as RedactionJobModifyParams,
    )
    from stripe.params.privacy._redaction_job_retrieve_params import (
        RedactionJobRetrieveParams as RedactionJobRetrieveParams,
    )
    from stripe.params.privacy._redaction_job_run_params import (
        RedactionJobRunParams as RedactionJobRunParams,
    )
    from stripe.params.privacy._redaction_job_update_params import (
        RedactionJobUpdateParams as RedactionJobUpdateParams,
    )
    from stripe.params.privacy._redaction_job_validate_params import (
        RedactionJobValidateParams as RedactionJobValidateParams,
    )
    from stripe.params.privacy._redaction_job_validation_error_list_params import (
        RedactionJobValidationErrorListParams as RedactionJobValidationErrorListParams,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "RedactionJobCancelParams": (
        "stripe.params.privacy._redaction_job_cancel_params",
        False,
    ),
    "RedactionJobCreateParams": (
        "stripe.params.privacy._redaction_job_create_params",
        False,
    ),
    "RedactionJobCreateParamsObjects": (
        "stripe.params.privacy._redaction_job_create_params",
        False,
    ),
    "RedactionJobListParams": (
        "stripe.params.privacy._redaction_job_list_params",
        False,
    ),
    "RedactionJobListValidationErrorsParams": (
        "stripe.params.privacy._redaction_job_list_validation_errors_params",
        False,
    ),
    "RedactionJobModifyParams": (
        "stripe.params.privacy._redaction_job_modify_params",
        False,
    ),
    "RedactionJobRetrieveParams": (
        "stripe.params.privacy._redaction_job_retrieve_params",
        False,
    ),
    "RedactionJobRunParams": (
        "stripe.params.privacy._redaction_job_run_params",
        False,
    ),
    "RedactionJobUpdateParams": (
        "stripe.params.privacy._redaction_job_update_params",
        False,
    ),
    "RedactionJobValidateParams": (
        "stripe.params.privacy._redaction_job_validate_params",
        False,
    ),
    "RedactionJobValidationErrorListParams": (
        "stripe.params.privacy._redaction_job_validation_error_list_params",
        False,
    ),
}
if not TYPE_CHECKING:

    def __getattr__(name):
        try:
            target, is_submodule = _import_map[name]
            module = import_module(target)
            if is_submodule:
                return module

            return getattr(
                module,
                name,
            )
        except KeyError:
            raise AttributeError()
