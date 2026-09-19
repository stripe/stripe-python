# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._list_object import ListObject
    from stripe._request_options import RequestOptions
    from stripe.params.privacy._redaction_job_validation_error_list_params import (
        RedactionJobValidationErrorListParams,
    )
    from stripe.privacy._redaction_job_validation_error import (
        RedactionJobValidationError,
    )


class RedactionJobValidationErrorService(StripeService):
    def list(
        self,
        id: str,
        /,
        params: Optional["RedactionJobValidationErrorListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[RedactionJobValidationError]":
        """
        Returns a list of validation errors for the specified redaction job.
        """
        return cast(
            "ListObject[RedactionJobValidationError]",
            self._request(
                "get",
                "/v1/privacy/redaction_jobs/{id}/validation_errors".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        id: str,
        /,
        params: Optional["RedactionJobValidationErrorListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[RedactionJobValidationError]":
        """
        Returns a list of validation errors for the specified redaction job.
        """
        return cast(
            "ListObject[RedactionJobValidationError]",
            await self._request_async(
                "get",
                "/v1/privacy/redaction_jobs/{id}/validation_errors".format(
                    id=sanitize_id(id),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
