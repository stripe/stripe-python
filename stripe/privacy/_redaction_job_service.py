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
        The objects at the root level that are subject to redaction.
        """
        validation_behavior: NotRequired[Literal["error", "fix"]]
        """
        Default is "error". If "error", we will make sure all objects in the graph are
        redactable in the 1st traversal, otherwise error. If "fix", where possible, we will
        auto-fix any validation errors (e.g. by auto-transitioning objects to a terminal
        state, etc.) in the 2nd traversal before redacting
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
        List redaction jobs method...
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
        List redaction jobs method...
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
        Create redaction job method
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
        Create redaction job method
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
        Retrieve redaction job method
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
        Retrieve redaction job method
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
        Update redaction job method
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
        Update redaction job method
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
        Cancel redaction job method
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
        Cancel redaction job method
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
        Run redaction job method
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
        Run redaction job method
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
        Validate redaction job method
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
        Validate redaction job method
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
