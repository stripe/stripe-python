# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import Literal, NotRequired, TypedDict


class OutboundSetupIntentFromFinancialConnectionsParams(TypedDict):
    financial_connections_account: NotRequired[str]
    """
    Used to create a US Bank Account directly from a Financial Connections Account.
    """
    financial_connections_session: NotRequired[str]
    """
    Used to create a US Bank Account from the internal-only "payment account" associated with a Financial Connections
    Session. Only useful when the Session completed with manual entry (i.e. there is no Financial Connections Account).
    """
    usage_intent: NotRequired[Literal["payment", "transfer"]]
    """
    Specify which type of outbound money movement this credential should be set up for (payment | transfer).
    If not provided, defaults to payment.
    """
