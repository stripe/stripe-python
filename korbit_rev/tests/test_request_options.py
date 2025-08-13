from stripe._request_options import (
    RequestOptions,
    merge_options,
    extract_options_from_dict,
)
from stripe._requestor_options import RequestorOptions


class TestRequestOptions(object):
    def test_merge(self):
        options = RequestorOptions(
            api_key="sk_test_123",
            stripe_account="acct_123",
            base_addresses={"api": "https://api.stripe.com"},
        )
        other: RequestOptions = {
            "api_key": "sk_test_456",
            "stripe_version": "2020-01-01",
            "headers": {"foo": "bar"},
        }
        merged = merge_options(options, other)
        assert merged.get("api_key") == "sk_test_456"
        assert merged.get("stripe_version") == "2020-01-01"
        assert merged.get("stripe_account") == "acct_123"
        assert merged.get("headers") == {"foo": "bar"}

    def test_merge_none(self):
        options = RequestorOptions(
            api_key="sk_test_123",
            stripe_account="acct_123",
            base_addresses={"api": "https://api.stripe.com"},
        )
        merged = merge_options(options, None)
        assert merged.get("api_key") == "sk_test_123"
        assert merged.get("stripe_version") is None
        assert merged.get("stripe_account") == "acct_123"
        assert merged.get("headers") is None

    def test_extract_from_dict(self):
        options, remaining = extract_options_from_dict(
            {
                "api_key": "sk_test_123",
                "stripe_version": "2020-01-01",
                "stripe_account": "acct_123",
                "stripe_context": "wksp_123",
                "idempotency_key": "idemp_123",
                "headers": {
                    "X-Stripe-Header": "Some-Value",
                },
                "foo": "bar",
            }
        )
        assert options.get("api_key") == "sk_test_123"
        assert options.get("stripe_version") == "2020-01-01"
        assert options.get("stripe_account") == "acct_123"
        assert options.get("stripe_context") == "wksp_123"
        assert options.get("idempotency_key") == "idemp_123"
        assert options.get("headers") == {"X-Stripe-Header": "Some-Value"}
        assert remaining == {"foo": "bar"}
