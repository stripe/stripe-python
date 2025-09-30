# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import NotRequired, TypedDict


class RecipientVerificationCreateParams(TypedDict):
    payout_method: str
    """
    ID of the payout method.
    """
    recipient: NotRequired[str]
    """
    ID of the recipient account. Required if the recipient distinct from the sender. Leave empty if the recipient and sender are the same entity (i.e. for me-to-me payouts).
    """
