# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, List
from typing_extensions import Literal


class Eligibility(StripeObject):
    """
    Whether a project is eligible to provision resources with a provider, and any
    outstanding KYC requirements that must be satisfied first.
    """

    OBJECT_NAME: ClassVar[Literal["v2.provisioning.eligibility"]] = (
        "v2.provisioning.eligibility"
    )
    is_eligible: bool
    """
    Whether the project is eligible to provision resources with the provider.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    object: Literal["v2.provisioning.eligibility"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    requirements: List[str]
    """
    Outstanding requirements that must be satisfied before the project is eligible, if any.
    """
