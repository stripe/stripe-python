# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe.privacy._redaction_job import RedactionJob as RedactionJob
    from stripe.privacy._redaction_job_service import (
        RedactionJobService as RedactionJobService,
    )
    from stripe.privacy._redaction_job_validation_error import (
        RedactionJobValidationError as RedactionJobValidationError,
    )
    from stripe.privacy._redaction_job_validation_error_service import (
        RedactionJobValidationErrorService as RedactionJobValidationErrorService,
    )

# name -> (import_target, is_submodule)
_import_map = {
    "RedactionJob": ("stripe.privacy._redaction_job", False),
    "RedactionJobService": ("stripe.privacy._redaction_job_service", False),
    "RedactionJobValidationError": (
        "stripe.privacy._redaction_job_validation_error",
        False,
    ),
    "RedactionJobValidationErrorService": (
        "stripe.privacy._redaction_job_validation_error_service",
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
