# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe.v2._amount import AmountParam
from typing_extensions import NotRequired, TypedDict


class SpendingMandateUpdateParams(TypedDict):
    bank_transfer: NotRequired["SpendingMandateUpdateParamsBankTransfer"]
    """
    Bank transfer fields to update. Omitted fields remain unchanged.
    """


class SpendingMandateUpdateParamsBankTransfer(TypedDict):
    account_holder_name: NotRequired[str]
    """
    Display name for the authorized originator, up to 50 characters long.
    """
    ach: NotRequired["SpendingMandateUpdateParamsBankTransferAch"]
    """
    ACH authorization fields to update.
    """


class SpendingMandateUpdateParamsBankTransferAch(TypedDict):
    originator_company_id: NotRequired[str]
    """
    ACH Company ID identifying the authorized originator. Must contain exactly 10 alphanumeric characters.
    """
    transaction_limit: NotRequired[AmountParam]
    """
    Per-debit limit for originator.
    """
