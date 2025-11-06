# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Dict, Optional
from typing_extensions import Literal, TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Any


class ReportRun(StripeObject):
    """
    The `ReportRun` object represents an instance of a `Report` generated with specific
    run parameters. Once the object is created, Stripe begins processing the report. When
    the report has finished running, it will give you a reference to the results.
    """

    OBJECT_NAME: ClassVar[Literal["v2.reporting.report_run"]] = (
        "v2.reporting.report_run"
    )

    class Result(StripeObject):
        class File(StripeObject):
            class DownloadUrl(StripeObject):
                expires_at: Optional[str]
                """
                The time that the URL expires.
                """
                url: str
                """
                The URL that can be used for accessing the file.
                """

            content_type: Literal["csv", "zip"]
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

        file: File
        """
        Contains metadata about the file produced by the `ReportRun`, including
        its content type, size, and a URL to download its contents.
        """
        type: Literal["file"]
        """
        The type of the `ReportRun` result.
        """
        _inner_class_types = {"file": File}

    class ResultOptions(StripeObject):
        compress_file: Optional[bool]
        """
        If set, the generated report file will be compressed into a ZIP folder.
        This is useful for reducing file size and download time for large reports.
        """

    class StatusDetails(StripeObject):
        error_code: Optional[
            Literal["file_size_above_limit", "internal_error"]
        ]
        """
        Error code categorizing the reason the `ReportRun` failed.
        """
        error_message: Optional[str]
        """
        Error message with additional details about the failure.
        """

    created: str
    """
    Time at which the object was created.
    """
    id: str
    """
    The unique identifier of the `ReportRun` object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.reporting.report_run"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    report: str
    """
    The unique identifier of the `Report` object which was run.
    """
    report_name: str
    """
    The human-readable name of the `Report` which was run.
    """
    report_parameters: Dict[str, "Any"]
    """
    The parameters used to customize the generation of the report.
    """
    result: Optional[Result]
    """
    Details how to retrieve the results of a successfully completed `ReportRun`.
    """
    result_options: Optional[ResultOptions]
    """
    The options specified for customizing the output file of the `ReportRun`.
    """
    status: Literal["failed", "running", "succeeded"]
    """
    The current status of the `ReportRun`.
    """
    status_details: Dict[str, StatusDetails]
    """
    Additional details about the current state of the `ReportRun`. The field is currently only populated when a `ReportRun`
    is in the `failed` state, providing more information about why the report failed to generate successfully.
    """
    _inner_class_types = {
        "result": Result,
        "result_options": ResultOptions,
        "status_details": StatusDetails,
    }
