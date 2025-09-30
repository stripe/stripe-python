# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import NotRequired, TypedDict


class ServiceActionUpdateParams(TypedDict):
    lookup_key: NotRequired[str]
    """
    An internal key you can use to search for this service action. Maximum length of 200 characters.
    """
    credit_grant: NotRequired["ServiceActionUpdateParamsCreditGrant"]
    """
    Details for the credit grant. Can only be set if the service action's `type` is `credit_grant`.
    """
    credit_grant_per_tenant: NotRequired[
        "ServiceActionUpdateParamsCreditGrantPerTenant"
    ]
    """
    Details for the credit grant per tenant. Can only be set if the service action's `type` is `credit_grant_per_tenant`.
    """


class ServiceActionUpdateParamsCreditGrant(TypedDict):
    name: NotRequired[str]
    """
    A descriptive name shown in dashboard.
    """


class ServiceActionUpdateParamsCreditGrantPerTenant(TypedDict):
    name: NotRequired[str]
    """
    A descriptive name shown in dashboard.
    """
