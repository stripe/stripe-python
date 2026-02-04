# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class ConnectionSessionCreateParams(TypedDict):
    account: str
    """
    The Account the ConnectionSession will create a connection for.
    """
    allowed_connection_types: NotRequired[List[Literal["link"]]]
    """
    The Connection types that the ConnectionSession is allowed to establish.
    """
    requested_access: NotRequired[List[Literal["payout_methods"]]]
    """
    The access that should be collected with the ConnectionSession.
    """
