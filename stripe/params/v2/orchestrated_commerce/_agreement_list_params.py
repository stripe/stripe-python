# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import NotRequired, TypedDict


class AgreementListParams(TypedDict):
    limit: NotRequired[int]
    """
    The limit for the number of results per page.
    """
    network_business_profile: NotRequired[str]
    """
    Filter list to Orchestrated Commerce Agreements with a specific counterparty.
    """
