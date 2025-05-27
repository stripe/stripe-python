# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._createable_api_resource import CreateableAPIResource
from stripe._list_object import ListObject
from stripe._listable_api_resource import ListableAPIResource
from stripe._nested_resource_class_methods import nested_resource_class_methods
from stripe._request_options import RequestOptions
from stripe._stripe_object import StripeObject
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
    The Redaction Job object redacts Stripe objects. You can use it
    to coordinate the removal of personal information from selected
    objects, making them permanently inaccessible in the Stripe Dashboard
    and API.
    """

    OBJECT_NAME: ClassVar[Literal["privacy.redaction_job"]] = (
        "privacy.redaction_job"
    )

    class Objects(StripeObject):
        charges: Optional[List[str]]
        """
        Charge object identifiers usually starting with `ch_`
        """
        checkout_sessions: Optional[List[str]]
        """
        CheckoutSession object identifiers starting with `cs_`
        """
        customers: Optional[List[str]]
        """
        Customer object identifiers starting with `cus_`
        """
        identity_verification_sessions: Optional[List[str]]
        """
        Identity VerificationSessions object identifiers starting with `vs_`
        """
        invoices: Optional[List[str]]
        """
        Invoice object identifiers starting with `in_`
        """
        issuing_cardholders: Optional[List[str]]
        """
        Issuing Cardholder object identifiers starting with `ich_`
        """
        payment_intents: Optional[List[str]]
        """
        PaymentIntent object identifiers starting with `pi_`
        """
        radar_value_list_items: Optional[List[str]]
        """
        Fraud ValueListItem object identifiers starting with `rsli_`
        """
        setup_intents: Optional[List[str]]
        """
        SetupIntent object identifiers starting with `seti_`
        """

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
        """
        Determines the validation behavior of the job. Default is `error`.
        """

    class RetrieveParams(RequestOptions):
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
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["privacy.redaction_job"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    objects: Optional[Objects]
    """
    The objects to redact in this job.
    """
    status: Literal[
        "canceled",
        "canceling",
        "created",
        "failed",
        "ready",
        "redacting",
        "succeeded",
        "validating",
    ]
    """
    The status of the job.
    """
    validation_behavior: Optional[Literal["error", "fix"]]
    """
    Validation behavior determines how a job validates objects for redaction eligibility. Default is `error`.
    """

    @classmethod
    def _cls_cancel(
        cls, job: str, **params: Unpack["RedactionJob.CancelParams"]
    ) -> "RedactionJob":
        """
        You can cancel a redaction job when it's in one of these statuses: ready, failed.

        Canceling the redaction job will abandon its attempt to redact the configured objects. A canceled job cannot be used again.
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
        You can cancel a redaction job when it's in one of these statuses: ready, failed.

        Canceling the redaction job will abandon its attempt to redact the configured objects. A canceled job cannot be used again.
        """
        ...

    @overload
    def cancel(
        self, **params: Unpack["RedactionJob.CancelParams"]
    ) -> "RedactionJob":
        """
        You can cancel a redaction job when it's in one of these statuses: ready, failed.

        Canceling the redaction job will abandon its attempt to redact the configured objects. A canceled job cannot be used again.
        """
        ...

    @class_method_variant("_cls_cancel")
    def cancel(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["RedactionJob.CancelParams"]
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
        You can cancel a redaction job when it's in one of these statuses: ready, failed.

        Canceling the redaction job will abandon its attempt to redact the configured objects. A canceled job cannot be used again.
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
        You can cancel a redaction job when it's in one of these statuses: ready, failed.

        Canceling the redaction job will abandon its attempt to redact the configured objects. A canceled job cannot be used again.
        """
        ...

    @overload
    async def cancel_async(
        self, **params: Unpack["RedactionJob.CancelParams"]
    ) -> "RedactionJob":
        """
        You can cancel a redaction job when it's in one of these statuses: ready, failed.

        Canceling the redaction job will abandon its attempt to redact the configured objects. A canceled job cannot be used again.
        """
        ...

    @class_method_variant("_cls_cancel_async")
    async def cancel_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["RedactionJob.CancelParams"]
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
        Creates a redaction job. When a job is created, it will start to validate.
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
        Creates a redaction job. When a job is created, it will start to validate.
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
        Returns a list of redaction jobs.
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
        Returns a list of redaction jobs.
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
        Updates the properties of a redaction job without running or canceling the job.

        If the job to update is in a failed status, it will not automatically start to validate. Once you applied all of the changes, use the validate API to start validation again.
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
        Updates the properties of a redaction job without running or canceling the job.

        If the job to update is in a failed status, it will not automatically start to validate. Once you applied all of the changes, use the validate API to start validation again.
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
        Retrieves the details of a previously created redaction job.
        """
        instance = cls(id, **params)
        instance.refresh()
        return instance

    @classmethod
    async def retrieve_async(
        cls, id: str, **params: Unpack["RedactionJob.RetrieveParams"]
    ) -> "RedactionJob":
        """
        Retrieves the details of a previously created redaction job.
        """
        instance = cls(id, **params)
        await instance.refresh_async()
        return instance

    @classmethod
    def _cls_run(
        cls, job: str, **params: Unpack["RedactionJob.RunParams"]
    ) -> "RedactionJob":
        """
        Run a redaction job in a ready status.

        When you run a job, the configured objects will be redacted asynchronously. This action is irreversible and cannot be canceled once started.

        The status of the job will move to redacting. Once all of the objects are redacted, the status will become succeeded. If the job's validation_behavior is set to fix, the automatic fixes will be applied to objects at this step.
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
        Run a redaction job in a ready status.

        When you run a job, the configured objects will be redacted asynchronously. This action is irreversible and cannot be canceled once started.

        The status of the job will move to redacting. Once all of the objects are redacted, the status will become succeeded. If the job's validation_behavior is set to fix, the automatic fixes will be applied to objects at this step.
        """
        ...

    @overload
    def run(
        self, **params: Unpack["RedactionJob.RunParams"]
    ) -> "RedactionJob":
        """
        Run a redaction job in a ready status.

        When you run a job, the configured objects will be redacted asynchronously. This action is irreversible and cannot be canceled once started.

        The status of the job will move to redacting. Once all of the objects are redacted, the status will become succeeded. If the job's validation_behavior is set to fix, the automatic fixes will be applied to objects at this step.
        """
        ...

    @class_method_variant("_cls_run")
    def run(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["RedactionJob.RunParams"]
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
        Run a redaction job in a ready status.

        When you run a job, the configured objects will be redacted asynchronously. This action is irreversible and cannot be canceled once started.

        The status of the job will move to redacting. Once all of the objects are redacted, the status will become succeeded. If the job's validation_behavior is set to fix, the automatic fixes will be applied to objects at this step.
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
        Run a redaction job in a ready status.

        When you run a job, the configured objects will be redacted asynchronously. This action is irreversible and cannot be canceled once started.

        The status of the job will move to redacting. Once all of the objects are redacted, the status will become succeeded. If the job's validation_behavior is set to fix, the automatic fixes will be applied to objects at this step.
        """
        ...

    @overload
    async def run_async(
        self, **params: Unpack["RedactionJob.RunParams"]
    ) -> "RedactionJob":
        """
        Run a redaction job in a ready status.

        When you run a job, the configured objects will be redacted asynchronously. This action is irreversible and cannot be canceled once started.

        The status of the job will move to redacting. Once all of the objects are redacted, the status will become succeeded. If the job's validation_behavior is set to fix, the automatic fixes will be applied to objects at this step.
        """
        ...

    @class_method_variant("_cls_run_async")
    async def run_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["RedactionJob.RunParams"]
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
        Validate a redaction job when it is in a failed status.

        When a job is created, it automatically begins to validate on the configured objects' eligibility for redaction. Use this to validate the job again after its validation errors are resolved or the job's validation_behavior is changed.

        The status of the job will move to validating. Once all of the objects are validated, the status of the job will become ready. If there are any validation errors preventing the job from running, the status will become failed.
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
        Validate a redaction job when it is in a failed status.

        When a job is created, it automatically begins to validate on the configured objects' eligibility for redaction. Use this to validate the job again after its validation errors are resolved or the job's validation_behavior is changed.

        The status of the job will move to validating. Once all of the objects are validated, the status of the job will become ready. If there are any validation errors preventing the job from running, the status will become failed.
        """
        ...

    @overload
    def validate(
        self, **params: Unpack["RedactionJob.ValidateParams"]
    ) -> "RedactionJob":
        """
        Validate a redaction job when it is in a failed status.

        When a job is created, it automatically begins to validate on the configured objects' eligibility for redaction. Use this to validate the job again after its validation errors are resolved or the job's validation_behavior is changed.

        The status of the job will move to validating. Once all of the objects are validated, the status of the job will become ready. If there are any validation errors preventing the job from running, the status will become failed.
        """
        ...

    @class_method_variant("_cls_validate")
    def validate(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["RedactionJob.ValidateParams"]
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
        Validate a redaction job when it is in a failed status.

        When a job is created, it automatically begins to validate on the configured objects' eligibility for redaction. Use this to validate the job again after its validation errors are resolved or the job's validation_behavior is changed.

        The status of the job will move to validating. Once all of the objects are validated, the status of the job will become ready. If there are any validation errors preventing the job from running, the status will become failed.
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
        Validate a redaction job when it is in a failed status.

        When a job is created, it automatically begins to validate on the configured objects' eligibility for redaction. Use this to validate the job again after its validation errors are resolved or the job's validation_behavior is changed.

        The status of the job will move to validating. Once all of the objects are validated, the status of the job will become ready. If there are any validation errors preventing the job from running, the status will become failed.
        """
        ...

    @overload
    async def validate_async(
        self, **params: Unpack["RedactionJob.ValidateParams"]
    ) -> "RedactionJob":
        """
        Validate a redaction job when it is in a failed status.

        When a job is created, it automatically begins to validate on the configured objects' eligibility for redaction. Use this to validate the job again after its validation errors are resolved or the job's validation_behavior is changed.

        The status of the job will move to validating. Once all of the objects are validated, the status of the job will become ready. If there are any validation errors preventing the job from running, the status will become failed.
        """
        ...

    @class_method_variant("_cls_validate_async")
    async def validate_async(  # pyright: ignore[reportGeneralTypeIssues]
        self, **params: Unpack["RedactionJob.ValidateParams"]
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
        Returns a list of validation errors for the specified redaction job.
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
        Returns a list of validation errors for the specified redaction job.
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

    _inner_class_types = {"objects": Objects}
