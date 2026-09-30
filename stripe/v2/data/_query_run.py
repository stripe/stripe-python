# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject, UntypedStripeObject
from typing import Any, ClassVar, List, Optional, Union
from typing_extensions import Literal


class QueryRun(StripeObject):
    """
    The `QueryRun` resource represents an execution of ad-hoc SQL against a dataset. Once
    created, Stripe processes the query. When the query has finished running, the object
    provides a reference to the results.
    """

    OBJECT_NAME: ClassVar[Literal["v2.data.query_run"]] = "v2.data.query_run"

    class Query(StripeObject):
        sql: Optional[str]
        """
        Ad-hoc SQL to execute.
        """

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
        compress_file: Optional[bool]
        """
        If set, the generated result file is compressed into a ZIP archive before
        it is stored. This applies only to downloadable file results.
        """

    class StatusDetails(StripeObject):
        canceled_at: Optional[str]
        """
        Time at which the run was canceled. Populated when the run is in the `canceled` state.
        """
        code: Optional[
            Union[
                Literal[
                    "file_size_above_limit",
                    "internal_error",
                    "query_run_invalid_sql",
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

    created: str
    """
    Time at which the `QueryRun` was created.
    """
    dataset: Union[Literal["analytical"], str]
    """
    The dataset that was queried.
    """
    format: Union[Literal["csv"], str]
    """
    The file format of the result. Only applicable when the result is a file.
    """
    id: str
    """
    The unique identifier of the `QueryRun`.
    """
    livemode: bool
    """
    Whether the `QueryRun` was executed in live mode.
    """
    object: Literal["v2.data.query_run"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    query: Query
    """
    The query that was submitted for execution.
    """
    refreshed_at: Optional[str]
    """
    Time at which the data used by this query was last refreshed.
    """
    result: Optional[Result]
    """
    The result of the `QueryRun`, populated when it has completed.
    """
    result_options: Optional[ResultOptions]
    """
    Settings applied to the generated result file.
    """
    status: Union[Literal["canceled", "failed", "running", "succeeded"], str]
    """
    The current status of the `QueryRun`.
    """
    status_details: Optional[StatusDetails]
    """
    Additional details about the current state of the `QueryRun`.
    """
    _inner_class_types = {
        "query": Query,
        "result": Result,
        "result_options": ResultOptions,
        "status_details": StatusDetails,
    }
