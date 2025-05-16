# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, Optional
from typing_extensions import Literal


class DeletedObject(StripeObject):
    OBJECT_NAME: ClassVar[Literal["v2.deleted_object"]] = "v2.deleted_object"
    object: Optional[Literal["v2.deleted_object"]]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    id: str
    """
    The ID of the object that's being deleted.
    """
