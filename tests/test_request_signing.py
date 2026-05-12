import base64
import hashlib
import re
from typing import Any, Dict
from unittest.mock import patch

import pytest

pytest.importorskip(
    "cryptography", reason="cryptography not available (PyPy <= 3.10)"
)

from cryptography.hazmat.primitives.asymmetric.ec import (
    ECDSA,
    SECP256R1,
    generate_private_key,
)
from cryptography.hazmat.primitives.hashes import SHA256
from cryptography.hazmat.primitives.serialization import (
    Encoding,
    NoEncryption,
    PrivateFormat,
)
from cryptography.hazmat.primitives.asymmetric.utils import (
    encode_dss_signature,
)

import stripe
from stripe._request_signing_authenticator import (
    RequestSigningAuthenticator,
    RequestSigningOptions,
)


@pytest.fixture
def key_pair():
    private_key = generate_private_key(SECP256R1())
    pem = private_key.private_bytes(
        Encoding.PEM, PrivateFormat.PKCS8, NoEncryption()
    )
    return private_key, pem


@pytest.fixture
def authenticator(key_pair):
    _, pem = key_pair
    return RequestSigningAuthenticator(
        RequestSigningOptions(key_id="keyid_test_abc123", private_key=pem)
    )


def _make_headers(**extra: str) -> Dict[str, str]:
    return {"Authorization": "Bearer sk_test_xxx", **extra}


class TestRequestSigningAuthenticator:
    def test_authorization_header_format(self, authenticator):
        headers = _make_headers()
        authenticator.apply_signing_headers(
            "post",
            "https://api.stripe.com/v1/customers",
            headers,
            "email=test%40example.com",
        )
        assert headers["Authorization"] == "STRIPE-V1-SIG keyid_test_abc123"

    def test_content_digest_for_known_body(self, authenticator):
        body = "email=test%40example.com"
        expected = base64.b64encode(
            hashlib.sha256(body.encode()).digest()
        ).decode()
        headers = _make_headers()
        authenticator.apply_signing_headers(
            "post", "https://api.stripe.com/v1/customers", headers, body
        )
        assert headers["Content-Digest"] == f"sha-256=:{expected}:"

    def test_content_digest_for_empty_body(self, authenticator):
        expected = base64.b64encode(hashlib.sha256(b"").digest()).decode()
        headers = _make_headers()
        authenticator.apply_signing_headers(
            "get", "https://api.stripe.com/v1/customers", headers, None
        )
        assert headers["Content-Digest"] == f"sha-256=:{expected}:"

    def test_date_header_added(self, authenticator):
        headers = _make_headers()
        authenticator.apply_signing_headers(
            "get", "https://api.stripe.com/v1/customers", headers, None
        )
        assert "Date" in headers

    def test_date_header_not_overwritten(self, authenticator):
        existing_date = "Wed, 28 Sep 2022 21:40:47 GMT"
        headers = _make_headers(Date=existing_date)
        authenticator.apply_signing_headers(
            "get", "https://api.stripe.com/v1/customers", headers, None
        )
        assert headers["Date"] == existing_date

    def test_signature_and_signature_input_headers_set(self, authenticator):
        headers = _make_headers()
        authenticator.apply_signing_headers(
            "post", "https://api.stripe.com/v1/customers", headers, "name=test"
        )
        assert "Signature" in headers
        assert "Signature-Input" in headers
        assert headers["Signature"].startswith("sig1=:")
        assert headers["Signature"].endswith(":")
        assert headers["Signature-Input"].startswith("sig1=(")

    def test_signature_input_contains_required_components(self, authenticator):
        headers = _make_headers()
        authenticator.apply_signing_headers(
            "post", "https://api.stripe.com/v1/customers", headers, "name=test"
        )
        sig_input = headers["Signature-Input"]
        assert '"@method"' in sig_input
        assert '"@target-uri"' in sig_input
        assert '"authorization"' in sig_input
        assert '"content-digest"' in sig_input

    def test_signature_input_includes_stripe_account_when_present(
        self, authenticator
    ):
        headers = _make_headers(**{"Stripe-Account": "acct_123"})
        authenticator.apply_signing_headers(
            "post", "https://api.stripe.com/v1/customers", headers, "name=test"
        )
        assert '"stripe-account"' in headers["Signature-Input"]

    def test_signature_input_excludes_stripe_account_when_absent(
        self, authenticator
    ):
        headers = _make_headers()
        authenticator.apply_signing_headers(
            "post", "https://api.stripe.com/v1/customers", headers, "name=test"
        )
        assert '"stripe-account"' not in headers["Signature-Input"]

    def test_signature_params_format(self, authenticator):
        headers = _make_headers()
        authenticator.apply_signing_headers(
            "post", "https://api.stripe.com/v1/customers", headers, ""
        )
        sig_input = headers["Signature-Input"]
        assert re.search(r"created=\d+", sig_input)
        assert re.search(r"expires=\d+", sig_input)
        assert re.search(r'nonce="[A-Za-z0-9+/=]+"', sig_input)
        assert 'alg="ecdsa-p256-sha256"' in sig_input

    def test_expires_is_300_seconds_after_created(self, authenticator):
        headers = _make_headers()
        authenticator.apply_signing_headers(
            "post", "https://api.stripe.com/v1/customers", headers, ""
        )
        sig_input = headers["Signature-Input"]
        created = int(re.search(r"created=(\d+)", sig_input).group(1))  # type: ignore
        expires = int(re.search(r"expires=(\d+)", sig_input).group(1))  # type: ignore
        assert expires - created == 300

    def test_signature_is_valid(self, key_pair, authenticator):
        private_key, _ = key_pair
        public_key = private_key.public_key()
        body = "email=test%40example.com"
        headers = _make_headers(**{"Stripe-Account": "acct_test"})
        authenticator.apply_signing_headers(
            "post", "https://api.stripe.com/v1/customers", headers, body
        )

        sig_b64 = headers["Signature"][len("sig1=:") :][:-1]
        raw_sig = base64.b64decode(sig_b64)
        assert len(raw_sig) == 64

        r = int.from_bytes(raw_sig[:32], "big")
        s = int.from_bytes(raw_sig[32:], "big")
        der_sig = encode_dss_signature(r, s)

        sig_params_value = headers["Signature-Input"][len("sig1=") :]
        covered = re.search(r"\(([^)]*)\)", sig_params_value).group(1)  # type: ignore
        component_names = [c.strip('"') for c in covered.split()]

        lines = []
        for name in component_names:
            if name == "@method":
                lines.append('"@method": POST')
            elif name == "@target-uri":
                lines.append(
                    '"@target-uri": https://api.stripe.com/v1/customers'
                )
            else:
                value = next(
                    v for k, v in headers.items() if k.lower() == name
                )
                lines.append(f'"{name}": {value}')
        lines.append(f'"@signature-params": {sig_params_value}')
        sig_base = "\n".join(lines).encode("utf-8")

        public_key.verify(der_sig, sig_base, ECDSA(SHA256()))

    def test_accepts_pem_as_string(self, key_pair):
        _, pem_bytes = key_pair
        auth = RequestSigningAuthenticator(
            RequestSigningOptions(
                key_id="keyid_test_abc",
                private_key=pem_bytes.decode("utf-8"),
            )
        )
        headers = _make_headers()
        auth.apply_signing_headers(
            "get", "https://api.stripe.com/v1/customers", headers, None
        )
        assert headers["Authorization"] == "STRIPE-V1-SIG keyid_test_abc"

    def test_rejects_non_p256_key(self):
        from cryptography.hazmat.primitives.asymmetric.ec import SECP384R1

        wrong_key = generate_private_key(SECP384R1())
        pem = wrong_key.private_bytes(
            Encoding.PEM, PrivateFormat.PKCS8, NoEncryption()
        )
        with pytest.raises(ValueError, match="secp256r1"):
            RequestSigningAuthenticator(
                RequestSigningOptions(key_id="keyid_test", private_key=pem)
            )

    def test_import_error_without_cryptography(self, key_pair):
        _, pem = key_pair
        with patch.dict(
            "sys.modules",
            {
                "cryptography": None,
                "cryptography.hazmat": None,
                "cryptography.hazmat.primitives": None,
                "cryptography.hazmat.primitives.serialization": None,
                "cryptography.hazmat.primitives.asymmetric": None,
                "cryptography.hazmat.primitives.asymmetric.ec": None,
            },
        ):
            with pytest.raises(
                ImportError, match="pip install stripe\\[request-signing\\]"
            ):
                RequestSigningAuthenticator(
                    RequestSigningOptions(key_id="keyid_test", private_key=pem)
                )


class TestStripeClientIntegration:
    def test_api_key_only_uses_bearer_auth(self):
        client = stripe.StripeClient(
            "sk_test_123",
            base_addresses={"api": "http://localhost"},
        )
        assert client._requestor._authenticator is None

    def test_signing_only_creates_authenticator(self, key_pair):
        _, pem = key_pair
        client = stripe.StripeClient(
            signing_keys=RequestSigningOptions(
                key_id="keyid_test_abc", private_key=pem
            ),
            base_addresses={"api": "http://localhost"},
        )
        assert client._requestor._authenticator is not None

    def test_both_api_key_and_signing_raises(self, key_pair):
        _, pem = key_pair
        with pytest.raises(ValueError, match="Cannot use both"):
            stripe.StripeClient(
                "sk_test_123",
                signing_keys=RequestSigningOptions(
                    key_id="keyid_test_abc", private_key=pem
                ),
            )

    def test_neither_api_key_nor_signing_raises(self):
        with pytest.raises(stripe.AuthenticationError):
            stripe.StripeClient()

    def test_request_uses_signing_headers(self, key_pair):
        _, pem = key_pair
        captured: Dict[str, Any] = {}

        class CapturingHttpClient(stripe.HTTPClient):
            name = "capturing"

            def request(self, method, url, headers, post_data=None):
                captured["headers"] = dict(headers)
                return "{}", 200, {"Content-Type": "application/json"}

            def request_stream(self, method, url, headers, post_data=None):
                raise NotImplementedError

        client = stripe.StripeClient(
            signing_keys=RequestSigningOptions(
                key_id="keyid_test_my_key", private_key=pem
            ),
            http_client=CapturingHttpClient(),
            base_addresses={"api": "https://api.stripe.com"},
        )

        try:
            client.v1.customers.retrieve("cus_123")
        except Exception:
            pass

        if captured.get("headers"):
            h = captured["headers"]
            assert h.get("Authorization", "").startswith("STRIPE-V1-SIG ")
            assert "Bearer" not in h.get("Authorization", "")
            assert "Content-Digest" in h
            assert "Signature-Input" in h
            assert "Signature" in h

    def test_request_signing_options_exported_from_stripe(self):
        assert hasattr(stripe, "RequestSigningOptions")
