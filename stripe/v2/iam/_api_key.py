# -*- coding: utf-8 -*-
# File generated from our OpenAPI spec
from stripe._stripe_object import StripeObject
from typing import ClassVar, List, Optional
from typing_extensions import Literal


class ApiKey(StripeObject):
    """
    An API key.
    """

    OBJECT_NAME: ClassVar[Literal["v2.iam.api_key"]] = "v2.iam.api_key"

    class ManagedBy(StripeObject):
        class Application(StripeObject):
            id: str
            """
            Identifier of the application.
            """

        application: Optional[Application]
        """
        An application.
        """
        type: Literal["application"]
        """
        The type of entity.
        """
        _inner_class_types = {"application": Application}

    class PublishableKey(StripeObject):
        token: str
        """
        The plaintext token for the API key.
        """

    class SecretKey(StripeObject):
        class EncryptedSecret(StripeObject):
            ciphertext: str
            """
            The encrypted secret data in base64 format.
            """
            format: str
            """
            The format of the encrypted secret (e.g., jwe_compact).
            """
            recipient_key_id: Optional[str]
            """
            The caller's identifier of the public key provided.
            """

        encrypted_secret: Optional[EncryptedSecret]
        """
        The encrypted secret for the API key. Only included when a key is first created.
        """
        secret_token_redacted: Optional[str]
        """
        Redacted version of the secret token for display purposes.
        """
        token: Optional[str]
        """
        The plaintext token for the API key. Only included for testmode keys.
        """
        _inner_class_types = {"encrypted_secret": EncryptedSecret}

    created: str
    """
    Timestamp when the API key was created.
    """
    expires_at: Optional[str]
    """
    Timestamp when the API key expires.
    """
    id: str
    """
    Unique identifier of the API key.
    """
    ip_allowlist: List[str]
    """
    List of IP addresses allowed to use this API key. Addresses use IPv4 protocol, and may be a CIDR range (e.g., [100.10.38.255, 100.10.38.0/24]).
    """
    last_used: Optional[str]
    """
    Timestamp when the API key was last used.
    """
    livemode: bool
    """
    Has the value `true` if the object exists in live mode or the value `false` if the object exists in test mode.
    """
    managed_by: Optional[ManagedBy]
    """
    Account that manages this API key (for keys managed by platforms).
    """
    name: Optional[str]
    """
    Name of the API key.
    """
    note: Optional[str]
    """
    Note or description for the API key.
    """
    object: Literal["v2.iam.api_key"]
    """
    String representing the object's type. Objects of the same type share the same value of the object field.
    """
    publishable_key: Optional[PublishableKey]
    """
    Token set for a publishable key.
    """
    secret_key: Optional[SecretKey]
    """
    Token set for a secret key.
    """
    status: Literal["active", "expired"]
    """
    Current status of the API key (e.g., active, expired).
    """
    type: Literal["publishable_key", "secret_key"]
    """
    Type of the API key.
    """
    _inner_class_types = {
        "managed_by": ManagedBy,
        "publishable_key": PublishableKey,
        "secret_key": SecretKey,
    }
