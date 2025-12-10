# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import Literal, NotRequired, TypedDict


class ApiKeyCreateParams(TypedDict):
    name: NotRequired[str]
    """
    Name for the API key.
    """
    note: NotRequired[str]
    """
    Note or description for the API key.
    """
    public_key: NotRequired["ApiKeyCreateParamsPublicKey"]
    """
    Public key for encrypting the API key secret.
    This must a PEM-formatted RSA key suitable for encryption, >= 2048 bits.
    A public key is required when creating secret keys.
    Publishable keys are not encrypted and a public key should not be included.
    """
    type: Literal["publishable_key", "secret_key"]
    """
    Type of the API key to create (secret or publishable).
    """


class ApiKeyCreateParamsPublicKey(TypedDict):
    id: NotRequired[str]
    """
    Caller's identifier of the public key. This is used for tracking purposes only, and will be echoed in the response if provided.
    """
    pem_key: NotRequired["ApiKeyCreateParamsPublicKeyPemKey"]
    """
    PEM-formatted public key.
    """


class ApiKeyCreateParamsPublicKeyPemKey(TypedDict):
    algorithm: str
    """
    The encryption algorithm used with this key (e.g., RSA).
    """
    data: str
    """
    The PEM-encoded public key data. Newlines are required between header/footer and body, and optional within the body.
    """
