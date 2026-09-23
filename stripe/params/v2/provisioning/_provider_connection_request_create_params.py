# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import UntypedStripeObject
from typing import Any, Dict
from typing_extensions import NotRequired, TypedDict


class ProviderConnectionRequestCreateParams(TypedDict):
    code_challenge: NotRequired[str]
    """
    PKCE code challenge: BASE64URL(SHA256(code_verifier)). Optional; when present the OAuth
    callback must supply the matching code_verifier. Not a secret (it is a hash of the verifier).
    """
    code_challenge_method: NotRequired[str]
    """
    PKCE code challenge method. Only "S256" is supported.
    """
    configuration: "Dict[str, Any]|UntypedStripeObject[Any]"
    """
    Provider-specific configuration payload for the connection.
    """
    project: NotRequired[str]
    """
    Project this provider connection is created for. Used to infer the catalog partition for provider
    calls. Optional; when absent the provider connection defaults to the prod catalog.
    """
    provider: NotRequired[str]
    """
    Identifier of the provider to connect to.
    """
    provider_name: NotRequired[str]
    """
    Deprecated identifier of the provider to connect to; use `provider` instead.
    """
