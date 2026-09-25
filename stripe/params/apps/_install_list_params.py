# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List
from typing_extensions import Literal, NotRequired, TypedDict


class InstallListParams(RequestOptions):
    account: NotRequired[str]
    """
    Only return installs made by this account. Only useful to app developers and embedding platforms, whose lists span the accounts that installed their app.
    """
    app: NotRequired[str]
    """
    Only return installs for the app specified by this app ID.
    """
    approval_required: NotRequired[bool]
    """
    Only return installs whose installer must authorize pending permissions, content security policy entries, or endpoints.
    """
    channel: NotRequired[
        "Literal['private_live', 'private_test', 'public', 'testing']|str"
    ]
    """
    Only return installs in the distribution channel specified by this channel name.
    """
    created: NotRequired["InstallListParamsCreated|int"]
    """
    Only return app installs that were created during the given date interval.
    """
    created_by: NotRequired[str]
    """
    Only return installs created by the embedding platform specified by this account ID.
    """
    ending_before: NotRequired[str]
    """
    A cursor for use in pagination. `ending_before` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, starting with `obj_bar`, your subsequent call can include `ending_before=obj_bar` in order to fetch the previous page of the list.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
    limit: NotRequired[int]
    """
    A limit on the number of objects to be returned. Limit can range between 1 and 100, and the default is 10.
    """
    starting_after: NotRequired[str]
    """
    A cursor for use in pagination. `starting_after` is an object ID that defines your place in the list. For instance, if you make a list request and receive 100 objects, ending with `obj_foo`, your subsequent call can include `starting_after=obj_foo` in order to fetch the next page of the list.
    """
    status: NotRequired[
        "Literal['install_failed', 'installed', 'installing', 'uninstall_failed', 'uninstalling']|str"
    ]
    """
    Only return installs with the given status.
    """


class InstallListParamsCreated(TypedDict):
    gt: NotRequired[int]
    """
    Minimum value to filter by (exclusive)
    """
    gte: NotRequired[int]
    """
    Minimum value to filter by (inclusive)
    """
    lt: NotRequired[int]
    """
    Maximum value to filter by (exclusive)
    """
    lte: NotRequired[int]
    """
    Maximum value to filter by (inclusive)
    """
