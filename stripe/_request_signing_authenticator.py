import base64
import hashlib
import os
import time
from email.utils import formatdate
from typing import Dict, List, Optional, Union
from typing_extensions import TypedDict


class RequestSigningOptions(TypedDict):
    """Options for ECDSA P-256 request signing. Requires `pip install stripe[request-signing]`."""

    key_id: str
    """The signing key ID from the Stripe dashboard (starts with `keyid_`)."""

    private_key: Union[str, bytes]
    """PEM-encoded ECDSA P-256 (secp256r1) private key."""


class RequestSigningAuthenticator:
    """
    Authenticates requests using ECDSA P-256 request signing (RFC 9421 patterns).
    Used as an alternative to Bearer token auth.

    Requires the `cryptography` package: `pip install stripe[request-signing]`
    """

    _SIGNATURE_VALIDITY_SECONDS = 300
    _ALGORITHM = "ecdsa-p256-sha256"

    def __init__(self, options: RequestSigningOptions):
        try:
            from cryptography.hazmat.primitives.serialization import (
                load_pem_private_key,
            )
            from cryptography.hazmat.primitives.asymmetric.ec import (
                EllipticCurvePrivateKey,
                SECP256R1,
            )
        except ImportError:
            raise ImportError(
                "The `cryptography` package is required for request signing. "
                "Install it with: `pip install stripe[request-signing]`"
            )

        pem = options["private_key"]
        if isinstance(pem, str):
            pem = pem.encode("utf-8")

        private_key = load_pem_private_key(pem, password=None)

        if not isinstance(
            private_key, EllipticCurvePrivateKey
        ) or not isinstance(private_key.curve, SECP256R1):
            raise ValueError(
                "private_key must be an ECDSA P-256 (secp256r1) private key"
            )

        self._signing_key = options["key_id"]
        self._private_key = private_key

    def apply_signing_headers(
        self,
        method: str,
        abs_url: str,
        headers: Dict[str, str],
        body: Optional[Union[str, bytes]],
    ) -> Dict[str, str]:
        """
        Adds request signing headers to an outgoing request, replacing the
        Authorization header with STRIPE-V1-SIG scheme.
        """
        headers["Authorization"] = f"STRIPE-V1-SIG {self._signing_key}"

        if isinstance(body, str):
            body_bytes = body.encode("utf-8")
        elif body is not None:
            body_bytes = bytes(body)
        else:
            body_bytes = b""
        digest = base64.b64encode(hashlib.sha256(body_bytes).digest()).decode(
            "ascii"
        )
        headers["Content-Digest"] = f"sha-256=:{digest}:"

        if "Date" not in headers:
            headers["Date"] = formatdate(
                timeval=None, localtime=False, usegmt=True
            )

        now = int(time.time())
        nonce = base64.b64encode(os.urandom(16)).decode("ascii")
        covered = self._covered_components(headers)
        sig_params = self._signature_params(covered, now, nonce)
        sig_base = self._signature_base(
            method, abs_url, headers, covered, sig_params
        )

        raw_sig = self._sign(sig_base.encode("utf-8"))
        encoded_sig = base64.b64encode(raw_sig).decode("ascii")
        headers["Signature-Input"] = f"sig1={sig_params}"
        headers["Signature"] = f"sig1=:{encoded_sig}:"

        return headers

    def _covered_components(self, headers: Dict[str, str]) -> List[str]:
        components = [
            '"@method"',
            '"@target-uri"',
            '"authorization"',
            '"content-digest"',
        ]
        if "Stripe-Account" in headers:
            components.append('"stripe-account"')
        if "Stripe-Context" in headers:
            components.append('"stripe-context"')
        if "Date" in headers:
            components.append('"date"')
        return components

    def _signature_params(
        self, covered: List[str], created: int, nonce: str
    ) -> str:
        expires = created + self._SIGNATURE_VALIDITY_SECONDS
        return (
            f"({' '.join(covered)});created={created};expires={expires};"
            f'nonce="{nonce}";alg="{self._ALGORITHM}"'
        )

    def _signature_base(
        self,
        method: str,
        abs_url: str,
        headers: Dict[str, str],
        covered: List[str],
        sig_params: str,
    ) -> str:
        lines: List[str] = []
        for component in covered:
            name = component.strip('"')
            if name == "@method":
                lines.append(f'"@method": {method.upper()}')
            elif name == "@target-uri":
                lines.append(f'"@target-uri": {abs_url}')
            else:
                value = self._header_value(headers, name)
                lines.append(f'"{name}": {value}')
        lines.append(f'"@signature-params": {sig_params}')
        return "\n".join(lines)

    def _header_value(self, headers: Dict[str, str], name: str) -> str:
        name_lower = name.lower()
        for key, value in headers.items():
            if key.lower() == name_lower:
                return value
        return ""

    def _sign(self, data: bytes) -> bytes:
        from cryptography.hazmat.primitives.asymmetric.ec import ECDSA
        from cryptography.hazmat.primitives.hashes import SHA256
        from cryptography.hazmat.primitives.asymmetric.utils import (
            decode_dss_signature,
        )

        der_sig = self._private_key.sign(data, ECDSA(SHA256()))
        r, s = decode_dss_signature(der_sig)
        # Convert to fixed 64-byte raw (r||s) format
        return r.to_bytes(32, "big") + s.to_bytes(32, "big")
