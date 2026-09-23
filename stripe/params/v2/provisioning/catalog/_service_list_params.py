# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import Literal, NotRequired, TypedDict


class ServiceListParams(TypedDict):
    catalog: NotRequired[Literal["dev", "prod", "testing"]]
    """
    Catalog partition to list services from.
    """
    development: NotRequired[bool]
    """
    When `true`, list development-only services. When unset or `false`, development services are
    excluded.
    """
    limit: NotRequired[int]
    """
    Maximum number of services to return.
    """
    provider_name: NotRequired[str]
    """
    Filters services to those offered by the provider with this name.
    """
