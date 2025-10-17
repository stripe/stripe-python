# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from typing import Optional, cast
from importlib import import_module
from typing_extensions import TYPE_CHECKING

if TYPE_CHECKING:
    from stripe._list_object import ListObject
    from stripe._request_options import RequestOptions
    from stripe.params.privacy._redaction_job_cancel_params import (
        RedactionJobCancelParams,
    )
    from stripe.params.privacy._redaction_job_create_params import (
        RedactionJobCreateParams,
    )
    from stripe.params.privacy._redaction_job_list_params import (
        RedactionJobListParams,
    )
    from stripe.params.privacy._redaction_job_retrieve_params import (
        RedactionJobRetrieveParams,
    )
    from stripe.params.privacy._redaction_job_run_params import (
        RedactionJobRunParams,
    )
    from stripe.params.privacy._redaction_job_update_params import (
        RedactionJobUpdateParams,
    )
    from stripe.params.privacy._redaction_job_validate_params import (
        RedactionJobValidateParams,
    )
    from stripe.privacy._redaction_job import RedactionJob
    from stripe.privacy._redaction_job_validation_error_service import (
        RedactionJobValidationErrorService,
    )

_subservices = {
    "validation_errors": [
        "stripe.privacy._redaction_job_validation_error_service",
        "RedactionJobValidationErrorService",
    ],
}


class RedactionJobService(StripeService):
    validation_errors: "RedactionJobValidationErrorService"

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

    def list(
        self,
        params: Optional["RedactionJobListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[RedactionJob]":
        """
        Returns a list of redaction jobs.
        """
        return cast(
            "ListObject[RedactionJob]",
            self._request(
                "get",
                "/v1/privacy/redaction_jobs",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        params: Optional["RedactionJobListParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "ListObject[RedactionJob]":
        """
        Returns a list of redaction jobs.
        """
        return cast(
            "ListObject[RedactionJob]",
            await self._request_async(
                "get",
                "/v1/privacy/redaction_jobs",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def create(
        self,
        params: "RedactionJobCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "RedactionJob":
        """
        Creates a redaction job. When a job is created, it will start to validate.
        """
        return cast(
            "RedactionJob",
            self._request(
                "post",
                "/v1/privacy/redaction_jobs",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def create_async(
        self,
        params: "RedactionJobCreateParams",
        options: Optional["RequestOptions"] = None,
    ) -> "RedactionJob":
        """
        Creates a redaction job. When a job is created, it will start to validate.
        """
        return cast(
            "RedactionJob",
            await self._request_async(
                "post",
                "/v1/privacy/redaction_jobs",
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        job: str,
        params: Optional["RedactionJobRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RedactionJob":
        """
        Retrieves the details of a previously created redaction job.
        """
        return cast(
            "RedactionJob",
            self._request(
                "get",
                "/v1/privacy/redaction_jobs/{job}".format(
                    job=sanitize_id(job)
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        job: str,
        params: Optional["RedactionJobRetrieveParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RedactionJob":
        """
        Retrieves the details of a previously created redaction job.
        """
        return cast(
            "RedactionJob",
            await self._request_async(
                "get",
                "/v1/privacy/redaction_jobs/{job}".format(
                    job=sanitize_id(job)
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def update(
        self,
        job: str,
        params: Optional["RedactionJobUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RedactionJob":
        """
        Updates the properties of a redaction job without running or canceling the job.

        If the job to update is in a failed status, it will not automatically start to validate. Once you applied all of the changes, use the validate API to start validation again.
        """
        return cast(
            "RedactionJob",
            self._request(
                "post",
                "/v1/privacy/redaction_jobs/{job}".format(
                    job=sanitize_id(job)
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def update_async(
        self,
        job: str,
        params: Optional["RedactionJobUpdateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RedactionJob":
        """
        Updates the properties of a redaction job without running or canceling the job.

        If the job to update is in a failed status, it will not automatically start to validate. Once you applied all of the changes, use the validate API to start validation again.
        """
        return cast(
            "RedactionJob",
            await self._request_async(
                "post",
                "/v1/privacy/redaction_jobs/{job}".format(
                    job=sanitize_id(job)
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def cancel(
        self,
        job: str,
        params: Optional["RedactionJobCancelParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RedactionJob":
        """
        You can cancel a redaction job when it's in one of these statuses: ready, failed.

        Canceling the redaction job will abandon its attempt to redact the configured objects. A canceled job cannot be used again.
        """
        return cast(
            "RedactionJob",
            self._request(
                "post",
                "/v1/privacy/redaction_jobs/{job}/cancel".format(
                    job=sanitize_id(job),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def cancel_async(
        self,
        job: str,
        params: Optional["RedactionJobCancelParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RedactionJob":
        """
        You can cancel a redaction job when it's in one of these statuses: ready, failed.

        Canceling the redaction job will abandon its attempt to redact the configured objects. A canceled job cannot be used again.
        """
        return cast(
            "RedactionJob",
            await self._request_async(
                "post",
                "/v1/privacy/redaction_jobs/{job}/cancel".format(
                    job=sanitize_id(job),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def run(
        self,
        job: str,
        params: Optional["RedactionJobRunParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RedactionJob":
        """
        Run a redaction job in a ready status.

        When you run a job, the configured objects will be redacted asynchronously. This action is irreversible and cannot be canceled once started.

        The status of the job will move to redacting. Once all of the objects are redacted, the status will become succeeded. If the job's validation_behavior is set to fix, the automatic fixes will be applied to objects at this step.
        """
        return cast(
            "RedactionJob",
            self._request(
                "post",
                "/v1/privacy/redaction_jobs/{job}/run".format(
                    job=sanitize_id(job),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def run_async(
        self,
        job: str,
        params: Optional["RedactionJobRunParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RedactionJob":
        """
        Run a redaction job in a ready status.

        When you run a job, the configured objects will be redacted asynchronously. This action is irreversible and cannot be canceled once started.

        The status of the job will move to redacting. Once all of the objects are redacted, the status will become succeeded. If the job's validation_behavior is set to fix, the automatic fixes will be applied to objects at this step.
        """
        return cast(
            "RedactionJob",
            await self._request_async(
                "post",
                "/v1/privacy/redaction_jobs/{job}/run".format(
                    job=sanitize_id(job),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def validate(
        self,
        job: str,
        params: Optional["RedactionJobValidateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RedactionJob":
        """
        Validate a redaction job when it is in a failed status.

        When a job is created, it automatically begins to validate on the configured objects' eligibility for redaction. Use this to validate the job again after its validation errors are resolved or the job's validation_behavior is changed.

        The status of the job will move to validating. Once all of the objects are validated, the status of the job will become ready. If there are any validation errors preventing the job from running, the status will become failed.
        """
        return cast(
            "RedactionJob",
            self._request(
                "post",
                "/v1/privacy/redaction_jobs/{job}/validate".format(
                    job=sanitize_id(job),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def validate_async(
        self,
        job: str,
        params: Optional["RedactionJobValidateParams"] = None,
        options: Optional["RequestOptions"] = None,
    ) -> "RedactionJob":
        """
        Validate a redaction job when it is in a failed status.

        When a job is created, it automatically begins to validate on the configured objects' eligibility for redaction. Use this to validate the job again after its validation errors are resolved or the job's validation_behavior is changed.

        The status of the job will move to validating. Once all of the objects are validated, the status of the job will become ready. If there are any validation errors preventing the job from running, the status will become failed.
        """
        return cast(
            "RedactionJob",
            await self._request_async(
                "post",
                "/v1/privacy/redaction_jobs/{job}/validate".format(
                    job=sanitize_id(job),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
