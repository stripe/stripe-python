# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject, UntypedStripeObject
from typing import Any, ClassVar, List, Optional
from typing_extensions import Literal


class ObjectDefinitionVersion(StripeObject):
    """
    Represents an immutable version of an object definition.
    It defines the fields of the object records created from it.
    """

    OBJECT_NAME: ClassVar[Literal["v2.extend.object_definition_version"]] = (
        "v2.extend.object_definition_version"
    )

    class ParentDetails(StripeObject):
        api_name_plural: str
        """
        The plural API name used in this definition's object record API paths.
        """
        api_name_singular: str
        """
        The singular API name used in this definition's object record tags.
        """
        id: str
        """
        The ID of the parent object definition.
        """

    class Properties(StripeObject):
        class Items(StripeObject):
            class Items(StripeObject):
                pass

            allowed_values: Optional[List[str]]
            """
            A required list of values for enum types.
            """
            default_value: Optional[Any]
            """
            An optional default value for the field.
            """
            description: Optional[str]
            """
            An optional human-readable description of the field.
            """
            exclusive_maximum: Optional[Any]
            """
            An optional exclusive maximum value for integer or decimal types.
            """
            exclusive_minimum: Optional[Any]
            """
            An optional exclusive minimum value for integer or decimal types.
            """
            is_deprecated: Optional[bool]
            """
            Whether or not the field is deprecated (default false).
            """
            items: Optional[Items]
            """
            The required scalar schema for each array item. Array values retain their supplied order, and
            order is significant. Values are never sorted. Empty arrays are valid unless min_items is positive.
            """
            max_items: Optional[int]
            """
            An optional maximum number of array items. It defaults to and cannot exceed 100.
            """
            max_length: Optional[int]
            """
            An optional maximum length validation for string fields.
            """
            maximum: Optional[Any]
            """
            An optional maximum value for integer or decimal types.
            """
            min_items: Optional[int]
            """
            An optional minimum number of array items. Empty arrays are valid when this is absent or zero.
            """
            min_length: Optional[int]
            """
            An optional minimum length validation for string fields.
            """
            minimum: Optional[Any]
            """
            An optional minimum value for integer or decimal types.
            """
            referenced_type: Optional[str]
            """
            The type referenced by object reference fields.
            """
            required: Optional[bool]
            """
            Whether or not the field is required (default false).
            """
            title: Optional[str]
            """
            An optional human-readable name for the field.
            """
            type: Literal[
                "array",
                "boolean",
                "currency",
                "datetime",
                "decimal",
                "enum",
                "integer",
                "monetary_amount",
                "object_reference",
                "string",
            ]
            """
            The data type of the field.
            """
            unique_items: Optional[bool]
            """
            Whether array item values must be unique (default false). Duplicate values are allowed by default.
            """
            _inner_class_types = {"items": Items}

        allowed_values: Optional[List[str]]
        """
        A required list of values for enum types.
        """
        default_value: Optional[Any]
        """
        An optional default value for the field.
        """
        description: Optional[str]
        """
        An optional human-readable description of the field.
        """
        exclusive_maximum: Optional[Any]
        """
        An optional exclusive maximum value for integer or decimal types.
        """
        exclusive_minimum: Optional[Any]
        """
        An optional exclusive minimum value for integer or decimal types.
        """
        is_deprecated: Optional[bool]
        """
        Whether or not the field is deprecated (default false).
        """
        items: Optional[Items]
        """
        The required scalar schema for each array item. Array values retain their supplied order, and
        order is significant. Values are never sorted. Empty arrays are valid unless min_items is positive.
        """
        max_items: Optional[int]
        """
        An optional maximum number of array items. It defaults to and cannot exceed 100.
        """
        max_length: Optional[int]
        """
        An optional maximum length validation for string fields.
        """
        maximum: Optional[Any]
        """
        An optional maximum value for integer or decimal types.
        """
        min_items: Optional[int]
        """
        An optional minimum number of array items. Empty arrays are valid when this is absent or zero.
        """
        min_length: Optional[int]
        """
        An optional minimum length validation for string fields.
        """
        minimum: Optional[Any]
        """
        An optional minimum value for integer or decimal types.
        """
        referenced_type: Optional[str]
        """
        The type referenced by object reference fields.
        """
        required: Optional[bool]
        """
        Whether or not the field is required (default false).
        """
        title: Optional[str]
        """
        An optional human-readable name for the field.
        """
        type: Literal[
            "array",
            "boolean",
            "currency",
            "datetime",
            "decimal",
            "enum",
            "integer",
            "monetary_amount",
            "object_reference",
            "string",
        ]
        """
        The data type of the field.
        """
        unique_items: Optional[bool]
        """
        Whether array item values must be unique (default false). Duplicate values are allowed by default.
        """
        _inner_class_types = {"items": Items}

    created: str
    """
    Time at which the object definition version was created.
    """
    description: Optional[str]
    """
    A description of what this version of the object definition represents.
    """
    display_name_plural: str
    """
    The human-readable plural name of this version.
    """
    display_name_singular: str
    """
    The human-readable singular name of this version.
    """
    id: str
    """
    The complete version ID, consisting of the object definition ID, `@`, and a semantic version.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.extend.object_definition_version"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    object_definition: str
    """
    The ID of the parent object definition.
    """
    parent_details: ParentDetails
    """
    The stable identity and API names of the parent object definition.
    """
    properties: UntypedStripeObject[Properties]
    """
    The schema of the object record fields defined by this object definition.
    """
    version: str
    """
    The semantic version of this object definition version, in `major.minor.patch` format.
    """
    _inner_class_types = {
        "parent_details": ParentDetails,
        "properties": Properties,
    }
