# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, Optional
from typing_extensions import Literal


class RedactionJobRootObjects(StripeObject):
    """
    The objects to redact, grouped by type. All redactable objects associated with these objects will be redacted as well.
    """

    OBJECT_NAME: ClassVar[Literal["privacy.redaction_job_root_objects"]] = (
        "privacy.redaction_job_root_objects"
    )
    charges: Optional[List[str]]
    checkout_sessions: Optional[List[str]]
    customers: Optional[List[str]]
    identity_verification_sessions: Optional[List[str]]
    invoices: Optional[List[str]]
    issuing_cardholders: Optional[List[str]]
    object: Literal["privacy.redaction_job_root_objects"]
    """
    String representing the object's type. Objects of the same type share the same value.
    """
    payment_intents: Optional[List[str]]
    radar_value_list_items: Optional[List[str]]
    setup_intents: Optional[List[str]]
