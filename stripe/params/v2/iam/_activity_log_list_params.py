# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class ActivityLogListParams(TypedDict):
    action_groups: NotRequired[
        List[Literal["api_key", "user_invite", "user_roles"]]
    ]
    """
    Filter results to only include activity logs for the specified action group types.
    """
    actions: NotRequired[
        List[
            Literal[
                "api_key_created",
                "api_key_deleted",
                "api_key_updated",
                "api_key_viewed",
                "user_invite_accepted",
                "user_invite_created",
                "user_invite_deleted",
                "user_roles_deleted",
                "user_roles_updated",
            ]
        ]
    ]
    """
    Filter results to only include activity logs for the specified action types.
    """
    limit: NotRequired[int]
    """
    Maximum number of results to return per page.
    """
