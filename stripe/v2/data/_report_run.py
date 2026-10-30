# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject, UntypedStripeObject
from typing import Any, ClassVar, List, Optional, Union
from typing_extensions import Literal


class ReportRun(StripeObject):
    """
    The `ReportRun` resource represents an instance of a `Report` generated with specific
    parameter values. Once the object is created, Stripe begins processing the report. When
    the report has finished running, it provides a reference to the results. A `ReportRun` and
    its results are retained for 90 days after the run completes. After that, Stripe deletes
    them and retrieving the `ReportRun` returns a `404` error.
    """

    OBJECT_NAME: ClassVar[Literal["v2.data.report_run"]] = "v2.data.report_run"

    class Result(StripeObject):
        class File(StripeObject):
            class Column(StripeObject):
                name: str
                """
                The name of the column.
                """
                type: Union[
                    Literal[
                        "bigint",
                        "boolean",
                        "date",
                        "datetime",
                        "decimal",
                        "double",
                        "integer",
                        "timestamp",
                        "varchar",
                    ],
                    str,
                ]
                """
                The data type of the column.
                """

            class DownloadUrl(StripeObject):
                expires_at: Optional[str]
                """
                The time that the URL expires.
                """
                url: str
                """
                The URL that can be used for accessing the file.
                """

            columns: List[Column]
            """
            The schema of the result data.
            """
            content_type: Union[Literal["csv"], str]
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
            _inner_class_types = {
                "columns": Column,
                "download_url": DownloadUrl,
            }
            _field_encodings = {"size": "int64_string"}

        class Inline(StripeObject):
            class Column(StripeObject):
                name: str
                """
                The name of the column.
                """
                type: Union[
                    Literal[
                        "bigint",
                        "boolean",
                        "date",
                        "datetime",
                        "decimal",
                        "double",
                        "integer",
                        "timestamp",
                        "varchar",
                    ],
                    str,
                ]
                """
                The data type of the column.
                """

            class Row(StripeObject):
                data: UntypedStripeObject[Any]
                """
                The column data in this row, keyed by column name.
                """

            columns: List[Column]
            """
            The schema of the result data.
            """
            next_page_url: Optional[str]
            """
            Token for the next page of rows.
            """
            previous_page_url: Optional[str]
            """
            Token for the previous page of rows.
            """
            rows: List[Row]
            """
            The result rows, each represented as a map of column name to value.
            """
            _inner_class_types = {"columns": Column, "rows": Row}

        col_count: Optional[int]
        """
        The total number of columns in the result.
        """
        file: Optional[File]
        """
        File result with a download URL. This is the default result type.
        """
        inline: Optional[Inline]
        """
        Inline result with data returned directly. Only present when requested via
        `include[0]=result.inline`.
        """
        row_count: Optional[int]
        """
        The total number of data rows in the result, excluding any header row.
        """
        _inner_class_types = {"file": File, "inline": Inline}
        _field_encodings = {
            "col_count": "int64_string",
            "row_count": "int64_string",
        }

    class ResultOptions(StripeObject):
        compression: Optional[Union[Literal["none", "zip"], str]]
        """
        The compression applied to the generated result file. Defaults to `none`. This applies
        only to downloadable file results.
        """

    class StatusDetails(StripeObject):
        class QueryError(StripeObject):
            message: str
            """
            A human-readable description of the error.
            """
            type: str
            """
            A short identifier categorizing the type of error.
            """

        canceled_at: Optional[str]
        """
        Time at which the run was canceled. Populated when the run is in the `canceled` state.
        """
        code: Optional[
            Union[
                Literal[
                    "execution_failed",
                    "file_size_above_limit",
                    "internal_error",
                    "query_run_invalid_sql",
                    "resource_limit_exceeded",
                ],
                str,
            ]
        ]
        """
        Error code categorizing the reason the run failed.
        """
        message: Optional[str]
        """
        Error message with additional details about the failure.
        """
        query_errors: List[QueryError]
        """
        Errors found in the submitted SQL. Populated when the failure was caused by invalid SQL.
        """
        _inner_class_types = {"query_errors": QueryError}

    created: str
    """
    Time at which the `ReportRun` was created.
    """
    format: Union[Literal["csv"], str]
    """
    The file format of the result.
    """
    id: str
    """
    The unique identifier of the `ReportRun`.
    """
    livemode: bool
    """
    Whether the `ReportRun` was executed in live mode.
    """
    name: str
    """
    The human-readable name of the `Report` which was run.
    """
    object: Literal["v2.data.report_run"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    parameters: UntypedStripeObject[Any]
    """
    The parameters used to customize the generation of the report.
    """
    refreshed_at: Optional[str]
    """
    Time at which the data used by this report was last refreshed.
    """
    report: str
    """
    The unique identifier of the `Report` which was run.
    """
    result: Optional[Result]
    """
    The result of the `ReportRun`, populated when it has completed.
    """
    result_options: Optional[ResultOptions]
    """
    Settings applied to the generated result file.
    """
    sql: Optional[str]
    """
    The fully-resolved SQL that was executed, or an explanatory message when the SQL cannot be
    exposed. Only present when requested via `include[0]=sql`.
    """
    status: Union[Literal["canceled", "failed", "running", "succeeded"], str]
    """
    The current status of the `ReportRun`.
    """
    status_details: Optional[StatusDetails]
    """
    Additional details about the current state of the `ReportRun`.
    """
    _inner_class_types = {
        "result": Result,
        "result_options": ResultOptions,
        "status_details": StatusDetails,
    }
