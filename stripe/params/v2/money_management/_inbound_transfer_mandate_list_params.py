# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import Literal, NotRequired, TypedDict


class InboundTransferMandateListParams(TypedDict):
    credential: NotRequired[str]
    """
    Filter by v2 credential.
    """
    limit: NotRequired[int]
    """
    Maximum number of results to return on a single page.
    """
    status: NotRequired[Literal["active", "canceled", "expired", "pending"]]
    """
    Filter by mandate status.
    """
    type: NotRequired["Literal['au_becs', 'bacs', 'nz_becs', 'sepa']|str"]
    """
    Filter by mandate scheme type.
    """
