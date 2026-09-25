# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._request_options import RequestOptions
from typing import List
from typing_extensions import Literal, NotRequired


class InstallCreateParams(RequestOptions):
    app: str
    """
    The ID of the app to install.
    """
    channel: NotRequired[
        "Literal['private_live', 'private_test', 'public', 'testing']|str"
    ]
    """
    The distribution channel to install from. Defaults to `public`. A private app must be installed on `private_test` or `private_live`, matching the mode of the API key.
    """
    code_challenge: NotRequired[str]
    """
    For OAuth apps, the PKCE code challenge used to issue the `auth_code` returned on the install. Must be 43 to 128 characters and contain only letters, numbers, `-`, `.`, `_`, and `~`. Only applies to installs made by the app developer or an embedding platform; ignored when an account installs its own private app.
    """
    code_challenge_method: NotRequired[str]
    """
    The method used to derive `code_challenge`. Required when `code_challenge` is provided, and must be `S256`.
    """
    expand: NotRequired[List[str]]
    """
    Specifies which fields in the response should be expanded.
    """
