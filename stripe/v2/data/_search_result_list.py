# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from decimal import Decimal
from stripe._stripe_object import StripeObject, UntypedStripeObject
from typing import ClassVar, List, Optional, Union
from typing_extensions import Literal


class SearchResultList(StripeObject):
    """
    A ranked set of public analytical resources matching a natural-language query.
    """

    OBJECT_NAME: ClassVar[Literal["v2.data.search_result_list"]] = (
        "v2.data.search_result_list"
    )

    class Context(StripeObject):
        class BusinessConcept(StripeObject):
            definition: str
            """
            What the term means in the context of this domain.
            """
            term: str
            """
            The name of the concept, for example "decline reason".
            """

        business_concepts: List[BusinessConcept]
        """
        Domain vocabulary relevant to the request, so that callers interpret the
        returned resources consistently with how Stripe defines these terms.
        """
        domain: str
        """
        The business domain the request was matched to, for example "payments".
        """
        guidance: str
        """
        High-level routing guidance for the agent. When `data` is empty, may
        advise how to refine the request or browse canonical resources.
        """
        _inner_class_types = {"business_concepts": BusinessConcept}

    class Data(StripeObject):
        class ExecutionSpec(StripeObject):
            execution_url: str
            """
            The canonical run endpoint, e.g. "/v2/data/report_runs" or "/v2/data/query_runs".
            """
            http_method: Union[Literal["GET", "POST"], str]
            """
            The HTTP method for `execution_url`.
            """
            id: str
            """
            The identifier to submit to `execution_url`, e.g. "report_123" or "table_123".
            """

        class Metrics(StripeObject):
            class Dimension(StripeObject):
                description: str
                """
                A description of what the dimension represents.
                """
                name: str
                """
                The public dimension name accepted by the metric query endpoint.
                """

            accepts_currency: bool
            """
            Whether the metric query endpoint accepts a `currency` parameter for this
            metric. False for pure ratios and growth rates.
            """
            dimensions: List[Dimension]
            """
            Dimensions the metric can be filtered and grouped by.
            """
            measure_format: Union[
                Literal["currency", "number", "percent"], str
            ]
            """
            How the metric's value is formatted.
            """
            metric_namespace: str
            """
            The metric namespace. Metrics queried together in one metric query request
            must share a namespace.
            """
            _inner_class_types = {"dimensions": Dimension}

        class Reports(StripeObject):
            class OutputColumn(StripeObject):
                description: str
                """
                What the column represents.
                """
                name: str
                """
                The name of the column in the report output.
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

            class Parameters(StripeObject):
                class ArrayDetails(StripeObject):
                    class EnumDetails(StripeObject):
                        allowed_values: List[str]
                        """
                        Allowed values of the enum.
                        """

                    element_type: Union[
                        Literal["array", "enum", "string", "timestamp"], str
                    ]
                    """
                    The data type of the elements in the array.
                    """
                    enum_details: Optional[EnumDetails]
                    """
                    Details about enum elements in the array.
                    """
                    _inner_class_types = {"enum_details": EnumDetails}

                class EnumDetails(StripeObject):
                    allowed_values: List[str]
                    """
                    Allowed values of the enum.
                    """

                array_details: Optional[ArrayDetails]
                """
                For array parameters, details about the array elements.
                """
                description: str
                """
                Explains the purpose and usage of the parameter.
                """
                enum_details: Optional[EnumDetails]
                """
                For enum parameters, the list of allowed values.
                """
                required: bool
                """
                Indicates whether the parameter must be provided.
                """
                type: Union[
                    Literal["array", "enum", "string", "timestamp"], str
                ]
                """
                The data type of the parameter.
                """
                _inner_class_types = {
                    "array_details": ArrayDetails,
                    "enum_details": EnumDetails,
                }

            output_columns: List[OutputColumn]
            """
            Shape of the report output when known.
            """
            parameters: UntypedStripeObject[Parameters]
            """
            Parameter schema, keyed by parameter name, matching the `/v2/data/reports`
            resource.
            """
            _inner_class_types = {
                "output_columns": OutputColumn,
                "parameters": Parameters,
            }
            _inner_class_dicts = ["parameters"]

        class Schemas(StripeObject):
            class Column(StripeObject):
                class ForeignKeysFrom(StripeObject):
                    column: str
                    """
                    The name of the referenced column.
                    """
                    schema: str
                    """
                    The identifier of the referenced schema.
                    """
                    schema_name: str
                    """
                    The name of the referenced schema.
                    """

                class ForeignKeysTo(StripeObject):
                    column: str
                    """
                    The name of the referenced column.
                    """
                    schema: str
                    """
                    The identifier of the referenced schema.
                    """
                    schema_name: str
                    """
                    The name of the referenced schema.
                    """

                description: str
                """
                A description of what the column represents.
                """
                foreign_keys_from: List[ForeignKeysFrom]
                """
                Columns in other schemas that reference this column as a foreign key.
                """
                foreign_keys_to: List[ForeignKeysTo]
                """
                Columns in other schemas that this column references as a foreign key.
                """
                is_primary_key: bool
                """
                Whether the column forms part of the table's primary key.
                """
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
                _inner_class_types = {
                    "foreign_keys_from": ForeignKeysFrom,
                    "foreign_keys_to": ForeignKeysTo,
                }

            class RelevantReport(StripeObject):
                description: str
                """
                A description of the `Report`.
                """
                id: str
                """
                The unique identifier of the `Report`.
                """
                name: str
                """
                The human-readable name of the `Report`.
                """
                reference_url: str
                """
                Canonical API path for the `Report`, e.g. "/v2/data/reports/report_123".
                """

            columns: List[Column]
            """
            Compact schema projection.
            """
            dataset: Union[Literal["analytical"], str]
            """
            The dataset used when submitting an ad-hoc query run.
            """
            relevant_reports: List[RelevantReport]
            """
            Stripe-defined reports that are relevant to this schema.
            """
            _inner_class_types = {
                "columns": Column,
                "relevant_reports": RelevantReport,
            }

        catalog: Optional[Union[Literal["metrics", "reports", "schemas"], str]]
        description: str
        """
        What the canonical resource contains.
        """
        execution_spec: ExecutionSpec
        """
        How to execute this result.
        """
        extended_description: Optional[str]
        """
        Per-result additional context: constraints, interpretation rules, and gotchas.
        """
        id: str
        """
        Canonical resource identity.
        """
        metrics: Optional[Metrics]
        """
        A pre-defined measure queryable through the metric query endpoint.
        """
        name: str
        """
        Human-readable name of the canonical resource.
        """
        object_type: str
        """
        The canonical resource type this result points at, e.g. "v2.data.schema"
        or "v2.data.report". May name a resource that is not yet publicly
        retrievable, in which case `reference_url` is omitted. Distinct from
        `object`, which identifies this result itself.
        """
        reference_url: str
        """
        Canonical API path for retrieving the complete resource, e.g.
        "/v2/data/reports/report_123".
        """
        refreshed_at: str
        """
        Present for schemas when known; omitted for resource types without data
        freshness.
        """
        relevance_score: Decimal
        """
        Relative ordering signal from the search service (0-1). Not a
        calibrated guarantee; callers must not use it as a configurable cutoff.
        """
        reports: Optional[Reports]
        """
        A Stripe-defined report exposed by `/v2/data/reports`.
        """
        schemas: Optional[Schemas]
        """
        A queryable table exposed by `/v2/data/schemas`.
        """
        _inner_class_types = {
            "execution_spec": ExecutionSpec,
            "metrics": Metrics,
            "reports": Reports,
            "schemas": Schemas,
        }
        _field_encodings = {"relevance_score": "decimal_string"}

    context: Optional[Context]
    """
    Domain-level intelligence. Present when a known domain matches; omitted
    when the system falls back to direct semantic search.
    """
    data: List[Data]
    """
    Ranked public resources. Always present, including when empty.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    next_page_url: Optional[str]
    """
    Token for the next page.
    """
    object: Literal["v2.data.search_result_list"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    previous_page_url: Optional[str]
    """
    Token for the previous page.
    """
    _inner_class_types = {"context": Context, "data": Data}
