# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Dict, Optional
from typing_extensions import Literal


class BatchJob(StripeObject):
    """
    BatchJob resource.
    """

    OBJECT_NAME: ClassVar[Literal["v2.core.batch_job"]] = "v2.core.batch_job"

    class StatusDetails(StripeObject):
        class BatchFailed(StripeObject):
            error: str
            """
            Details about the `BatchJob` failure.
            """

        class Canceled(StripeObject):
            class OutputFile(StripeObject):
                class DownloadUrl(StripeObject):
                    expires_at: Optional[str]
                    """
                    The time that the URL expires.
                    """
                    url: str
                    """
                    The URL that can be used for accessing the file.
                    """

                content_type: str
                """
                The content type of the file.
                """
                download_url: DownloadUrl
                """
                A pre-signed URL that allows secure, time-limited access to download the file.
                """
                size: int
                """
                The total size of the file in bytes.
                """
                _inner_class_types = {"download_url": DownloadUrl}

            failure_count: int
            """
            The total number of records that failed processing.
            """
            output_file: OutputFile
            """
            The output file details. If BatchJob is cancelled it's provided only if there is already output at this point.
            """
            success_count: int
            """
            The total number of records that were successfully processed.
            """
            _inner_class_types = {"output_file": OutputFile}

        class Complete(StripeObject):
            class OutputFile(StripeObject):
                class DownloadUrl(StripeObject):
                    expires_at: Optional[str]
                    """
                    The time that the URL expires.
                    """
                    url: str
                    """
                    The URL that can be used for accessing the file.
                    """

                content_type: str
                """
                The content type of the file.
                """
                download_url: DownloadUrl
                """
                A pre-signed URL that allows secure, time-limited access to download the file.
                """
                size: int
                """
                The total size of the file in bytes.
                """
                _inner_class_types = {"download_url": DownloadUrl}

            failure_count: int
            """
            The total number of records that failed processing.
            """
            output_file: OutputFile
            """
            The output file details. If BatchJob is cancelled it's provided only if there is already output at this point.
            """
            success_count: int
            """
            The total number of records that were successfully processed.
            """
            _inner_class_types = {"output_file": OutputFile}

        class InProgress(StripeObject):
            failure_count: int
            """
            The number of records that failed processing so far.
            """
            success_count: int
            """
            The number of records that were successfully processed so far.
            """

        class ReadyForUpload(StripeObject):
            class UploadUrl(StripeObject):
                expires_at: Optional[str]
                """
                The time that the URL expires.
                """
                url: str
                """
                The URL that can be used for accessing the file.
                """

            upload_url: UploadUrl
            """
            The upload file details.
            """
            _inner_class_types = {"upload_url": UploadUrl}

        class Timeout(StripeObject):
            class OutputFile(StripeObject):
                class DownloadUrl(StripeObject):
                    expires_at: Optional[str]
                    """
                    The time that the URL expires.
                    """
                    url: str
                    """
                    The URL that can be used for accessing the file.
                    """

                content_type: str
                """
                The content type of the file.
                """
                download_url: DownloadUrl
                """
                A pre-signed URL that allows secure, time-limited access to download the file.
                """
                size: int
                """
                The total size of the file in bytes.
                """
                _inner_class_types = {"download_url": DownloadUrl}

            failure_count: int
            """
            The total number of records that failed processing.
            """
            output_file: OutputFile
            """
            The output file details. If BatchJob is cancelled it's provided only if there is already output at this point.
            """
            success_count: int
            """
            The total number of records that were successfully processed.
            """
            _inner_class_types = {"output_file": OutputFile}

        class Validating(StripeObject):
            validated_count: int
            """
            The number of records that were validated. Note that there is no failure counter here;
            once we have any validation failures we give up.
            """

        class ValidationFailed(StripeObject):
            class OutputFile(StripeObject):
                class DownloadUrl(StripeObject):
                    expires_at: Optional[str]
                    """
                    The time that the URL expires.
                    """
                    url: str
                    """
                    The URL that can be used for accessing the file.
                    """

                content_type: str
                """
                The content type of the file.
                """
                download_url: DownloadUrl
                """
                A pre-signed URL that allows secure, time-limited access to download the file.
                """
                size: int
                """
                The total size of the file in bytes.
                """
                _inner_class_types = {"download_url": DownloadUrl}

            failure_count: int
            """
            The total number of records that failed processing.
            """
            output_file: OutputFile
            """
            The output file details. If BatchJob is cancelled it's provided only if there is already output at this point.
            """
            success_count: int
            """
            The total number of records that were successfully processed.
            """
            _inner_class_types = {"output_file": OutputFile}

        batch_failed: Optional[BatchFailed]
        """
        Additional details for the `BATCH_FAILED` status of the `BatchJob`.
        """
        canceled: Optional[Canceled]
        """
        Additional details for the `CANCELED` status of the `BatchJob`.
        """
        complete: Optional[Complete]
        """
        Additional details for the `COMPLETE` status of the `BatchJob`.
        """
        in_progress: Optional[InProgress]
        """
        Additional details for the `IN_PROGRESS` status of the `BatchJob`.
        """
        ready_for_upload: Optional[ReadyForUpload]
        """
        Additional details for the `READY_FOR_UPLOAD` status of the `BatchJob`.
        """
        timeout: Optional[Timeout]
        """
        Additional details for the `TIMEOUT` status of the `BatchJob`.
        """
        validating: Optional[Validating]
        """
        Additional details for the `VALIDATING` status of the `BatchJob`.
        """
        validation_failed: Optional[ValidationFailed]
        """
        Additional details for the `VALIDATION_FAILED` status of the `BatchJob`.
        """
        _inner_class_types = {
            "batch_failed": BatchFailed,
            "canceled": Canceled,
            "complete": Complete,
            "in_progress": InProgress,
            "ready_for_upload": ReadyForUpload,
            "timeout": Timeout,
            "validating": Validating,
            "validation_failed": ValidationFailed,
        }

    created: str
    """
    Timestamp at which BatchJob was created.
    """
    id: str
    """
    Unique identifier for the BatchJob.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    maximum_rps: int
    """
    The maximum rps defined for the `BatchJob`.
    """
    metadata: Dict[str, str]
    """
    The metadata of the `BatchJob` object.
    """
    object: Literal["v2.core.batch_job"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    skip_validation: bool
    """
    If the validation will be run previous to the execution of the `BatchJob`.
    """
    status: Literal[
        "batch_failed",
        "canceled",
        "cancelling",
        "complete",
        "in_progress",
        "ready_for_upload",
        "timeout",
        "upload_timeout",
        "validating",
        "validation_failed",
    ]
    """
    The current status of the `BatchJob`.
    """
    status_details: Optional[StatusDetails]
    """
    Additional details about the current state of the `BatchJob`.
    """
    _inner_class_types = {"status_details": StatusDetails}
