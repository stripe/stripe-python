# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import Literal, NotRequired, TypedDict


class ProjectCreateParams(TypedDict):
    catalog: NotRequired[Literal["dev", "prod", "testing"]]
    """
    Catalog partition to create the project in.
    """
    name: str
    """
    Human-readable name for the new project.
    """
    project_profile: NotRequired[str]
    """
    Identifier of the developer profile to associate with the new project.
    """
