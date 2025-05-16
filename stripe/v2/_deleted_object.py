# -*- coding: utf-8 -*-
from stripe._stripe_object import StripeObject


class DeletedObject(StripeObject):
    object: str
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    id: str
    """
    The ID of the object that's being deleted.
    """
