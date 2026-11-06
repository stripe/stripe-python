# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar
from typing_extensions import Literal


class ObjectDefinition(StripeObject):
    """
    Represents a user-defined object definition that models a custom object.
    Object definitions enable the object records API to create and manage records of that object.
    """

    OBJECT_NAME: ClassVar[Literal["v2.extend.object_definition"]] = (
        "v2.extend.object_definition"
    )
    api_name_plural: str
    """
    The plural API name used in this definition's object record API paths. Immutable across versions.
    """
    api_name_singular: str
    """
    The singular API name used in the object tag of this definition's records. Immutable across versions.
    """
    created: str
    """
    Time at which the object definition was created.
    """
    id: str
    """
    Unique identifier for the object definition.
    """
    latest_version: str
    """
    The ID of the latest object definition version.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.extend.object_definition"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
