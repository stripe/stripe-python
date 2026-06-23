# Minimal stub for the Event class (V1).
# The full _event.py is generated from the OpenAPI spec for V1 resources.
# This stub exists so _webhook.py can import Event without error in
# custom-object SDKs that don't include V1 resources.
from stripe._stripe_object import StripeObject


class Event(StripeObject):
    """Stub for V1 Event resource."""

    OBJECT_NAME = "event"
