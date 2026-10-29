# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import Literal, NotRequired, TypedDict


class MoneyManagementRecipientVerificationsParams(TypedDict):
    match_result: Literal["close_match", "match", "no_match", "unavailable"]
    """
    Expected match level of the RecipientVerification to be created: `match`, `close_match`, `no_match`, `unavailable`.
    For `close_match`, the simulated response appends "close_match" to the provided name in match_result_details.matched_name.
    """
    payout_method: str
    """
    ID of the payout method.
    """
    recipient: NotRequired[str]
    """
    ID of the recipient account. Required if the recipient is different from the sender. Omit for payouts to your own account.
    """
