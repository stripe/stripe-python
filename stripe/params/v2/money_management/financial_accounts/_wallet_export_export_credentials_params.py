# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from typing import Union
from typing_extensions import Literal, TypedDict


class WalletExportExportCredentialsParams(TypedDict):
    encryption: "WalletExportExportCredentialsParamsEncryption"
    """
    Encryption parameters for the exported credentials.
    """


class WalletExportExportCredentialsParamsEncryption(TypedDict):
    recipient_public_key: str
    """
    Base64url-encoded raw P-256 recipient public key. Stripe does not persist this key material.
    """
    type: Union[Literal["hpke"], str]
    """
    Encryption scheme for the response. HPKE uses BASE mode, DHKEM_P256_HKDF_SHA256, HKDF_SHA256, and CHACHA20_POLY1305.
    """
