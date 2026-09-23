# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import Literal, NotRequired, TypedDict


class ProviderListParams(TypedDict):
    catalog: NotRequired[Literal["dev", "prod", "testing"]]
    """
    Catalog partition to list providers from.
    """
    development: NotRequired[bool]
    """
    When `true`, list development-only providers. When unset or `false`, development providers are
    excluded.
    """
    limit: NotRequired[int]
    """
    Maximum number of providers to return.
    """
