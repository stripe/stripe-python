# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._list_object import ListObject
from stripe._request_options import RequestOptions
from stripe._stripe_service import StripeService
from stripe._util import sanitize_id
from stripe.privacy._redaction_job_validation_error import (
    RedactionJobValidationError,
)
from typing import List, cast
from typing_extensions import NotRequired, TypedDict


class RedactionJobValidationErrorService(StripeService):
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

    class RetrieveParams(TypedDict):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    def list(
        self,
        job: str,
        params: "RedactionJobValidationErrorService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[RedactionJobValidationError]:
        """
        List validation errors method
        """
        return cast(
            ListObject[RedactionJobValidationError],
            self._request(
                "get",
                "/v1/privacy/redaction_jobs/{job}/validation_errors".format(
                    job=sanitize_id(job),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def list_async(
        self,
        job: str,
        params: "RedactionJobValidationErrorService.ListParams" = {},
        options: RequestOptions = {},
    ) -> ListObject[RedactionJobValidationError]:
        """
        List validation errors method
        """
        return cast(
            ListObject[RedactionJobValidationError],
            await self._request_async(
                "get",
                "/v1/privacy/redaction_jobs/{job}/validation_errors".format(
                    job=sanitize_id(job),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    def retrieve(
        self,
        job: str,
        error: str,
        params: "RedactionJobValidationErrorService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> RedactionJobValidationError:
        """
        Retrieve validation error method
        """
        return cast(
            RedactionJobValidationError,
            self._request(
                "get",
                "/v1/privacy/redaction_jobs/{job}/validation_errors/{error}".format(
                    job=sanitize_id(job),
                    error=sanitize_id(error),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )

    async def retrieve_async(
        self,
        job: str,
        error: str,
        params: "RedactionJobValidationErrorService.RetrieveParams" = {},
        options: RequestOptions = {},
    ) -> RedactionJobValidationError:
        """
        Retrieve validation error method
        """
        return cast(
            RedactionJobValidationError,
            await self._request_async(
                "get",
                "/v1/privacy/redaction_jobs/{job}/validation_errors/{error}".format(
                    job=sanitize_id(job),
                    error=sanitize_id(error),
                ),
                base_address="api",
                params=params,
                options=options,
            ),
        )
