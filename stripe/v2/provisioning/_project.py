# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, Optional
from typing_extensions import Literal


class Project(StripeObject):
    """
    The `Project` resource represents a container for provisioned resources and their
    associated configuration.
    """

    OBJECT_NAME: ClassVar[Literal["v2.provisioning.project"]] = (
        "v2.provisioning.project"
    )

    class Profile(StripeObject):
        email: Optional[str]
        """
        Email address associated with the developer profile.
        """
        verified_fields: List[Literal["country", "email", "name", "phone"]]
        """
        Fields of the developer profile that have been verified.
        """

    catalog: Literal["dev", "prod", "testing"]
    """
    Catalog partition the project belongs to.
    """
    created: str
    """
    Time at which the project was created.
    """
    id: str
    """
    Unique identifier for the project.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    name: str
    """
    Human-readable name of the project.
    """
    object: Literal["v2.provisioning.project"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    profile: Optional[Profile]
    """
    Use the /v2/provisioning/identity endpoint instead for IAM information.
    """
    project_profile: Optional[str]
    """
    Identifier of the developer profile associated with the project.
    """
    _inner_class_types = {"profile": Profile}
