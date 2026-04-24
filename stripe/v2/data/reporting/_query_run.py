# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject, UntypedStripeObject
from typing import ClassVar, Optional
from typing_extensions import Literal


class QueryRun(StripeObject):
    """
    The `QueryRun` object represents an ad-hoc SQL execution. Once created, Stripe processes the query. When
    the query has finished running, the object provides a reference to the results.
    """

    OBJECT_NAME: ClassVar[Literal["v2.data.reporting.query_run"]] = (
        "v2.data.reporting.query_run"
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
            _field_encodings = {"size": "int64_string"}

        file: Optional[File]
        """
        Contains metadata about the file produced by the `ReportRun` or `QueryRun`, including
        its content type, size, and a URL to download its contents.
        """
        type: Literal["file"]
        """
        The type of the `ReportRun` or `QueryRun` result.
        """
        _inner_class_types = {"file": File}

    class ResultOptions(StripeObject):
        compress_file: Optional[bool]
        """
        If set, the generated results file will be compressed into a ZIP folder.
        This is useful for reducing file size and download time for large results.
        """

    class StatusDetails(StripeObject):
        error_code: Optional[
            Literal["file_size_above_limit", "internal_error"]
        ]
        """
        Error code categorizing the reason the `QueryRun` failed.
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
    The unique identifier of the `QueryRun` object.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.data.reporting.query_run"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    result: Optional[Result]
    """
    Details how to retrieve the results of a successfully completed `QueryRun`.
    """
    result_options: Optional[ResultOptions]
    """
    The options specified for customizing the output of the `QueryRun`.
    """
    sql: str
    """
    The SQL that was executed.
    """
    status: Literal["failed", "running", "succeeded"]
    """
    The current status of the `QueryRun`.
    """
    status_details: UntypedStripeObject[StatusDetails]
    """
    Additional details about the current state of the `QueryRun`. Populated when the `QueryRun`
    is in the `failed` state, providing more information about why the query failed.
    """
    _inner_class_types = {
        "result": Result,
        "result_options": ResultOptions,
        "status_details": StatusDetails,
    }
