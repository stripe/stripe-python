# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing_extensions import NotRequired, TypedDict


class ApiKeyRotateParams(TypedDict):
    expire_current_key_in_minutes: NotRequired[int]
    """
    Duration in minutes before the current key expires, with a maximum of 7 days (10080 minutes).
    If not provided, the current key expires immediately.
    """
    public_key: NotRequired["ApiKeyRotateParamsPublicKey"]
    """
    Public key for encrypting the new API key secret.
    This must a PEM-formatted RSA key suitable for encryption, >= 2048 bits.
    A public key is required when rotating secret keys.
    Publishable keys are not encrypted and a public key should not be included.
    """


class ApiKeyRotateParamsPublicKey(TypedDict):
    id: NotRequired[str]
    """
    Caller's identifier of the public key. This is used for tracking purposes only, and will be echoed in the response if provided.
    """
    pem_key: NotRequired["ApiKeyRotateParamsPublicKeyPemKey"]
    """
    PEM-formatted public key.
    """


class ApiKeyRotateParamsPublicKeyPemKey(TypedDict):
    algorithm: str
    """
    The encryption algorithm used with this key (e.g., RSA).
    """
    data: str
    """
    The PEM-encoded public key data. Newlines are required between header/footer and body, and optional within the body.
    """
