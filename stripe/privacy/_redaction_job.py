# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._createable_api_resource import CreateableAPIResource
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._nested_resource_class_methods import nested_resource_class_methods
from stripe._request_options import RequestOptions
from stripe._updateable_api_resource import UpdateableAPIResource
from stripe._util import class_method_variant, sanitize_id
from typing import ClassVar, List, Optional, cast, overload
from typing_extensions import (
    Literal,
    NotRequired,
    TypedDict,
    Unpack,
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from stripe.privacy._redaction_job_root_objects import (
        RedactionJobRootObjects,
    )
    from stripe.privacy._redaction_job_validation_error import (
        RedactionJobValidationError,
    )


@nested_resource_class_methods("validation_error")
class RedactionJob(
    CreateableAPIResource["RedactionJob"],
    ListableAPIResource["RedactionJob"],
    UpdateableAPIResource["RedactionJob"],
):
    """
    Redaction Jobs store the status of a redaction request. They are created
    when a redaction request is made and track the redaction validation and execution.
    """

    OBJECT_NAME: ClassVar[Literal["privacy.redaction_job"]] = (
        "privacy.redaction_job"
    )

    class CancelParams(RequestOptions):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    class CreateParams(RequestOptions):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        objects: "RedactionJob.CreateParamsObjects"
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

    class ListParams(RequestOptions):
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

    class ListValidationErrorsParams(RequestOptions):
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

    class ModifyParams(RequestOptions):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """
        validation_behavior: NotRequired[Literal["error", "fix"]]

    class RetrieveParams(RequestOptions):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    class RetrieveValidationErrorParams(RequestOptions):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    class RunParams(RequestOptions):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    class ValidateParams(RequestOptions):
        expand: NotRequired[List[str]]
        """
        Specifies which fields in the response should be expanded.
        """

    created: int
    """
    Time at which the object was created. Measured in seconds since the Unix epoch.
    """
    id: str
    """
    Unique identifier for the object.
    """
    object: Literal["privacy.redaction_job"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    objects: Optional["RedactionJobRootObjects"]
    """
    The objects at the root level that are subject to redaction.
    """
    status: str
    """
    The status field represents the current state of the redaction job. It can take on any of the following values: VALIDATING, READY, REDACTING, SUCCEEDED, CANCELED, FAILED.
    """
    validation_behavior: Optional[str]
    """
    Default is "error". If "error", we will make sure all objects in the graph are redactable in the 1st traversal, otherwise error. If "fix", where possible, we will auto-fix any validation errors (e.g. by auto-transitioning objects to a terminal state, etc.) in the 2nd traversal before redacting
    """

    @classmethod
    def _cls_cancel(
        cls, job: str, **params: Unpack["RedactionJob.CancelParams"]
    ) -> "RedactionJob":
        """
        Cancel redaction job method
        """
        return cast(
            "RedactionJob",
            cls._static_request(
                "post",
                "/v1/privacy/redaction_jobs/{job}/cancel".format(
                    job=sanitize_id(job)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def cancel(
        job: str, **params: Unpack["RedactionJob.CancelParams"]
    ) -> "RedactionJob":
        """
        Cancel redaction job method
        """
        ...

    @overload
    def cancel(
        self, **params: Unpack["RedactionJob.CancelParams"]
    ) -> "RedactionJob":
        """
        Cancel redaction job method
        """
        ...

    @class_method_variant("_cls_cancel")
    def cancel(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["RedactionJob.CancelParams"]
    ) -> "RedactionJob":
        """
        Cancel redaction job method
        """
        return cast(
            "RedactionJob",
            self._request(
                "post",
                "/v1/privacy/redaction_jobs/{job}/cancel".format(
                    job=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_cancel_async(
        cls, job: str, **params: Unpack["RedactionJob.CancelParams"]
    ) -> "RedactionJob":
        """
        Cancel redaction job method
        """
        return cast(
            "RedactionJob",
            await cls._static_request_async(
                "post",
                "/v1/privacy/redaction_jobs/{job}/cancel".format(
                    job=sanitize_id(job)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def cancel_async(
        job: str, **params: Unpack["RedactionJob.CancelParams"]
    ) -> "RedactionJob":
        """
        Cancel redaction job method
        """
        ...

    @overload
    async def cancel_async(
        self, **params: Unpack["RedactionJob.CancelParams"]
    ) -> "RedactionJob":
        """
        Cancel redaction job method
        """
        ...

    @class_method_variant("_cls_cancel_async")
    async def cancel_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["RedactionJob.CancelParams"]
    ) -> "RedactionJob":
        """
        Cancel redaction job method
        """
        return cast(
            "RedactionJob",
            await self._request_async(
                "post",
                "/v1/privacy/redaction_jobs/{job}/cancel".format(
                    job=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def create(
        cls, **params: Unpack["RedactionJob.CreateParams"]
    ) -> "RedactionJob":
        """
        Create redaction job method
        """
        return cast(
            "RedactionJob",
            cls._static_request(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    async def create_async(
        cls, **params: Unpack["RedactionJob.CreateParams"]
    ) -> "RedactionJob":
        """
        Create redaction job method
        """
        return cast(
            "RedactionJob",
            await cls._static_request_async(
                "post",
                cls.class_url(),
                params=params,
            ),
        )

    @classmethod
    def list(
        cls, **params: Unpack["RedactionJob.ListParams"]
    ) -> ListObject["RedactionJob"]:
        """
        List redaction jobs method...
        """
        result = cls._static_request(
            "get",
            cls.class_url(),
            params=params,
        )
        if not isinstance(result, ListObject):
            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    async def list_async(
        cls, **params: Unpack["RedactionJob.ListParams"]
    ) -> ListObject["RedactionJob"]:
        """
        List redaction jobs method...
        """
        result = await cls._static_request_async(
            "get",
            cls.class_url(),
            params=params,
        )
        if not isinstance(result, ListObject):
            raise TypeError(
                "Expected list object from API, got %s"
                % (type(result).__name__)
            )

        return result

    @classmethod
    def modify(
        cls, id: str, **params: Unpack["RedactionJob.ModifyParams"]
    ) -> "RedactionJob":
        """
        Update redaction job method
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(id))
        return cast(
            "RedactionJob",
            cls._static_request(
                "post",
                url,
                params=params,
            ),
        )

    @classmethod
    async def modify_async(
        cls, id: str, **params: Unpack["RedactionJob.ModifyParams"]
    ) -> "RedactionJob":
        """
        Update redaction job method
        """
        url = "%s/%s" % (cls.class_url(), sanitize_id(id))
        return cast(
            "RedactionJob",
            await cls._static_request_async(
                "post",
                url,
                params=params,
            ),
        )

    @classmethod
    def retrieve(
        cls, id: str, **params: Unpack["RedactionJob.RetrieveParams"]
    ) -> "RedactionJob":
        """
        Retrieve redaction job method
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["RedactionJob.RetrieveParams"]
    ) -> "RedactionJob":
        """
        Retrieve redaction job method
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    @classmethod
    def _cls_run(
        cls, job: str, **params: Unpack["RedactionJob.RunParams"]
    ) -> "RedactionJob":
        """
        Run redaction job method
        """
        return cast(
            "RedactionJob",
            cls._static_request(
                "post",
                "/v1/privacy/redaction_jobs/{job}/run".format(
                    job=sanitize_id(job)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def run(
        job: str, **params: Unpack["RedactionJob.RunParams"]
    ) -> "RedactionJob":
        """
        Run redaction job method
        """
        ...

    @overload
    def run(
        self, **params: Unpack["RedactionJob.RunParams"]
    ) -> "RedactionJob":
        """
        Run redaction job method
        """
        ...

    @class_method_variant("_cls_run")
    def run(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["RedactionJob.RunParams"]
    ) -> "RedactionJob":
        """
        Run redaction job method
        """
        return cast(
            "RedactionJob",
            self._request(
                "post",
                "/v1/privacy/redaction_jobs/{job}/run".format(
                    job=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_run_async(
        cls, job: str, **params: Unpack["RedactionJob.RunParams"]
    ) -> "RedactionJob":
        """
        Run redaction job method
        """
        return cast(
            "RedactionJob",
            await cls._static_request_async(
                "post",
                "/v1/privacy/redaction_jobs/{job}/run".format(
                    job=sanitize_id(job)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def run_async(
        job: str, **params: Unpack["RedactionJob.RunParams"]
    ) -> "RedactionJob":
        """
        Run redaction job method
        """
        ...

    @overload
    async def run_async(
        self, **params: Unpack["RedactionJob.RunParams"]
    ) -> "RedactionJob":
        """
        Run redaction job method
        """
        ...

    @class_method_variant("_cls_run_async")
    async def run_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["RedactionJob.RunParams"]
    ) -> "RedactionJob":
        """
        Run redaction job method
        """
        return cast(
            "RedactionJob",
            await self._request_async(
                "post",
                "/v1/privacy/redaction_jobs/{job}/run".format(
                    job=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def _cls_validate(
        cls, job: str, **params: Unpack["RedactionJob.ValidateParams"]
    ) -> "RedactionJob":
        """
        Validate redaction job method
        """
        return cast(
            "RedactionJob",
            cls._static_request(
                "post",
                "/v1/privacy/redaction_jobs/{job}/validate".format(
                    job=sanitize_id(job)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    def validate(
        job: str, **params: Unpack["RedactionJob.ValidateParams"]
    ) -> "RedactionJob":
        """
        Validate redaction job method
        """
        ...

    @overload
    def validate(
        self, **params: Unpack["RedactionJob.ValidateParams"]
    ) -> "RedactionJob":
        """
        Validate redaction job method
        """
        ...

    @class_method_variant("_cls_validate")
    def validate(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["RedactionJob.ValidateParams"]
    ) -> "RedactionJob":
        """
        Validate redaction job method
        """
        return cast(
            "RedactionJob",
            self._request(
                "post",
                "/v1/privacy/redaction_jobs/{job}/validate".format(
                    job=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    async def _cls_validate_async(
        cls, job: str, **params: Unpack["RedactionJob.ValidateParams"]
    ) -> "RedactionJob":
        """
        Validate redaction job method
        """
        return cast(
            "RedactionJob",
            await cls._static_request_async(
                "post",
                "/v1/privacy/redaction_jobs/{job}/validate".format(
                    job=sanitize_id(job)
                ),
                params=params,
            ),
        )

    @overload
    @staticmethod
    async def validate_async(
        job: str, **params: Unpack["RedactionJob.ValidateParams"]
    ) -> "RedactionJob":
        """
        Validate redaction job method
        """
        ...

    @overload
    async def validate_async(
        self, **params: Unpack["RedactionJob.ValidateParams"]
    ) -> "RedactionJob":
        """
        Validate redaction job method
        """
        ...

    @class_method_variant("_cls_validate_async")
    async def validate_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["RedactionJob.ValidateParams"]
    ) -> "RedactionJob":
        """
        Validate redaction job method
        """
        return cast(
            "RedactionJob",
            await self._request_async(
                "post",
                "/v1/privacy/redaction_jobs/{job}/validate".format(
                    job=sanitize_id(self.get("id"))
                ),
                params=params,
            ),
        )

    @classmethod
    def list_validation_errors(
        cls,
        job: str,
        **params: Unpack["RedactionJob.ListValidationErrorsParams"],
    ) -> ListObject["RedactionJobValidationError"]:
        """
        List validation errors method
        """
        return cast(
            ListObject["RedactionJobValidationError"],
            cls._static_request(
                "get",
                "/v1/privacy/redaction_jobs/{job}/validation_errors".format(
                    job=sanitize_id(job)
                ),
                params=params,
            ),
        )

    @classmethod
    async def list_validation_errors_async(
        cls,
        job: str,
        **params: Unpack["RedactionJob.ListValidationErrorsParams"],
    ) -> ListObject["RedactionJobValidationError"]:
        """
        List validation errors method
        """
        return cast(
            ListObject["RedactionJobValidationError"],
            await cls._static_request_async(
                "get",
                "/v1/privacy/redaction_jobs/{job}/validation_errors".format(
                    job=sanitize_id(job)
                ),
                params=params,
            ),
        )

    @classmethod
    def retrieve_validation_error(
        cls,
        job: str,
        error: str,
        **params: Unpack["RedactionJob.RetrieveValidationErrorParams"],
    ) -> "RedactionJobValidationError":
        """
        Retrieve validation error method
        """
        return cast(
            "RedactionJobValidationError",
            cls._static_request(
                "get",
                "/v1/privacy/redaction_jobs/{job}/validation_errors/{error}".format(
                    job=sanitize_id(job), error=sanitize_id(error)
                ),
                params=params,
            ),
        )

    @classmethod
    async def retrieve_validation_error_async(
        cls,
        job: str,
        error: str,
        **params: Unpack["RedactionJob.RetrieveValidationErrorParams"],
    ) -> "RedactionJobValidationError":
        """
        Retrieve validation error method
        """
        return cast(
            "RedactionJobValidationError",
            await cls._static_request_async(
                "get",
                "/v1/privacy/redaction_jobs/{job}/validation_errors/{error}".format(
                    job=sanitize_id(job), error=sanitize_id(error)
                ),
                params=params,
            ),
        )
