# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._list_object import ListObject
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.privacy._redaction_job import RedactionJob
from stripe.privacy._redaction_job_validation_error_service import (
    RedactionJobValidationErrorService,
)
from typing import List, cast
from typing_extensions import Literal, NotRequired, TypedDict


class RedactionJobService(StripeService):
    def __init__(self, requestor):
        super().__init__(requestor)
        self.validation_errors = RedactionJobValidationErrorService(
            self._requestor,
        )

    class CancelParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    class CreateParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        objects: "RedactionJobService.CreateParamsObjects"
        """
        The objects to redact. These root objects and their related ones will be validated for redaction.
        """
        validation_behavior: NotRequired[Literal["error", "fix"]]
        """
        Determines the validation behavior of the job. Default is `error`.
        """

    class CreateParamsObjects(TypedDict):
        charges: NotRequired[List[str]]
        checkout_sessions: NotRequired[List[str]]
        customers: NotRequired[List[str]]
        identity_verification_sessions: NotRequired[List[str]]
        invoices: NotRequired[List[str]]
        issuing_cardholders: NotRequired[List[str]]
        issuing_cards: NotRequired[List[str]]
        payment_intents: NotRequired[List[str]]
        radar_value_list_items: NotRequired[List[str]]
        setup_intents: NotRequired[List[str]]

    class ListParams(TypedDict):
        ending_before: NotRequired[str]
        """
        A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
        """
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        limit: NotRequired[int]
        """
        A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
        """
        starting_after: NotRequired[str]
        """
        A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
        """
        status: NotRequired[
            Literal[
                "canceled",
                "canceling",
                "created",
                "failed",
                "ready",
                "redacting",
                "succeeded",
                "validating",
            ]
        ]

    class RetrieveParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    class RunParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    class UpdateParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        validation_behavior: NotRequired[Literal["error", "fix"]]
        """
        Determines the validation behavior of the job. Default is `error`.
        """

    class ValidateParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    def list(
        self,
        params: "RedactionJobService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[RedactionJob]:
        """
        Returns a list of redaction jobs.
        """
        return cast(
            ListObject[RedactionJob],
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
        params: "RedactionJobService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[RedactionJob]:
        """
        Returns a list of redaction jobs.
        """
        return cast(
            ListObject[RedactionJob],
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
        params: "RedactionJobService.CreateParams",
        options: RequestOptions = {},
    ) -> RedactionJob:
        """
        Creates a redaction job. When a job is created, it will start to validate.
        """
        return cast(
            RedactionJob,
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
        params: "RedactionJobService.CreateParams",
        options: RequestOptions = {},
    ) -> RedactionJob:
        """
        Creates a redaction job. When a job is created, it will start to validate.
        """
        return cast(
            RedactionJob,
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
        params: "RedactionJobService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> RedactionJob:
        """
        Retrieves the details of a previously created redaction job.
        """
        return cast(
            RedactionJob,
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
        params: "RedactionJobService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> RedactionJob:
        """
        Retrieves the details of a previously created redaction job.
        """
        return cast(
            RedactionJob,
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
        params: "RedactionJobService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> RedactionJob:
        """
        Updates the properties of a redaction job without running or canceling the job.

        If the job to update is in a failed status, it will not automatically start to validate. Once you applied all of the changes, use the validate API to start validation again.
        """
        return cast(
            RedactionJob,
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
        params: "RedactionJobService.UpdateParams" = {},
        options: RequestOptions = {},
    ) -> RedactionJob:
        """
        Updates the properties of a redaction job without running or canceling the job.

        If the job to update is in a failed status, it will not automatically start to validate. Once you applied all of the changes, use the validate API to start validation again.
        """
        return cast(
            RedactionJob,
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
        params: "RedactionJobService.CancelParams" = {},
        options: RequestOptions = {},
    ) -> RedactionJob:
        """
        You can cancel a redaction job when it's in one of these statuses: ready, failed.

        Canceling the redaction job will abandon its attempt to redact the configured objects. A canceled job cannot be used again.
        """
        return cast(
            RedactionJob,
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
        params: "RedactionJobService.CancelParams" = {},
        options: RequestOptions = {},
    ) -> RedactionJob:
        """
        You can cancel a redaction job when it's in one of these statuses: ready, failed.

        Canceling the redaction job will abandon its attempt to redact the configured objects. A canceled job cannot be used again.
        """
        return cast(
            RedactionJob,
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
        params: "RedactionJobService.RunParams" = {},
        options: RequestOptions = {},
    ) -> RedactionJob:
        """
        Run a redaction job in a ready status.

        When you run a job, the configured objects will be redacted asynchronously. This action is irreversible and cannot be canceled once started.

        The status of the job will move to redacting. Once all of the objects are redacted, the status will become succeeded. If the job's validation_behavior is set to fix, the automatic fixes will be applied to objects at this step.
        """
        return cast(
            RedactionJob,
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
        params: "RedactionJobService.RunParams" = {},
        options: RequestOptions = {},
    ) -> RedactionJob:
        """
        Run a redaction job in a ready status.

        When you run a job, the configured objects will be redacted asynchronously. This action is irreversible and cannot be canceled once started.

        The status of the job will move to redacting. Once all of the objects are redacted, the status will become succeeded. If the job's validation_behavior is set to fix, the automatic fixes will be applied to objects at this step.
        """
        return cast(
            RedactionJob,
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
        params: "RedactionJobService.ValidateParams" = {},
        options: RequestOptions = {},
    ) -> RedactionJob:
        """
        Validate a redaction job when it is in a failed status.

        When a job is created, it automatically begins to validate on the configured objects' eligibility for redaction. Use this to validate the job again after its validation errors are resolved or the job's validation_behavior is changed.

        The status of the job will move to validating. Once all of the objects are validated, the status of the job will become ready. If there are any validation errors preventing the job from running, the status will become failed.
        """
        return cast(
            RedactionJob,
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
        params: "RedactionJobService.ValidateParams" = {},
        options: RequestOptions = {},
    ) -> RedactionJob:
        """
        Validate a redaction job when it is in a failed status.

        When a job is created, it automatically begins to validate on the configured objects' eligibility for redaction. Use this to validate the job again after its validation errors are resolved or the job's validation_behavior is changed.

        The status of the job will move to validating. Once all of the objects are validated, the status of the job will become ready. If there are any validation errors preventing the job from running, the status will become failed.
        """
        return cast(
            RedactionJob,
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
