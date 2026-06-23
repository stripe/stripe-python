# Stub for DeletedObject (normally generated from our OpenAPI spec).
# Kept in the SDK base because it's needed by delete service methods.
from stripe._stripe_object import StripeObject
from typing import Optional


class DeletedObject(StripeObject):
    id: str
    object: Optional[str]
