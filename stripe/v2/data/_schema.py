# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, Optional, Union
from typing_extensions import Literal


class Schema(StripeObject):
    """
    The `Schema` resource describes the columns, types, and relationships of a table that
    can be queried.
    """

    OBJECT_NAME: ClassVar[Literal["v2.data.schema"]] = "v2.data.schema"

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

        class ForeignKeysTo(StripeObject):
            column: str
            """
            The name of the referenced column.
            """
            schema: str
            """
            The identifier of the referenced schema.
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

    columns: List[Column]
    """
    The columns of the table.
    """
    dataset: Union[Literal["analytical"], str]
    """
    The dataset the table belongs to.
    """
    description: str
    """
    A description of the table.
    """
    extended_description: Optional[str]
    """
    An extended, LLM-friendly description of the table, useful for query generation.
    """
    id: str
    """
    The unique identifier of the `Schema`.
    """
    livemode: bool
    """
    Whether this `Schema` describes live mode data.
    """
    name: str
    """
    The human-readable name of the table.
    """
    object: Literal["v2.data.schema"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    refreshed_at: str
    """
    Time at which the table's schema was last refreshed.
    """
    relevant_reports: List[RelevantReport]
    """
    Reports relevant to this table.
    """
    _inner_class_types = {
        "columns": Column,
        "relevant_reports": RelevantReport,
    }
