import stripe
from stripe import StripeContext
from stripe import _api_requestor
from stripe._request_options import RequestOptions, merge_options
from stripe._requestor_options import RequestorOptions
from stripe.v2.core._event import EventNotification
from unittest.mock import Mock
import pytest


class TestStripeContext:
    def test_init_empty(self):
        context = StripeContext()
        assert context._segments == []

    def test_init_with_segments(self):
        context = StripeContext(["a", "b", "c"])
        assert context._segments == ["a", "b", "c"]

    def test_push(self):
        context = StripeContext(["a", "b"])
        new_context = context.push("c")

        # Original context unchanged
        assert context._segments == ["a", "b"]
        # New context has added segment
        assert new_context._segments == ["a", "b", "c"]
        # Different objects
        assert context is not new_context

    def test_pop_with_segments(self):
        context = StripeContext(["a", "b", "c"])
        new_context = context.pop()

        # Original context unchanged
        assert context._segments == ["a", "b", "c"]
        # New context has removed last segment
        assert new_context._segments == ["a", "b"]
        # Different objects
        assert context is not new_context

    def test_pop_empty(self):
        with pytest.raises(ValueError):
            StripeContext([]).pop()

    def test_str_empty(self):
        context = StripeContext([])
        assert str(context) == ""

    def test_str_single_segment(self):
        context = StripeContext(["a"])
        assert str(context) == "a"

    def test_str_multiple_segments(self):
        context = StripeContext(["a", "b", "c"])
        assert str(context) == "a/b/c"

    def test_parse_empty_string(self):
        context = StripeContext.parse("")
        assert context._segments == []

    def test_parse_single_segment(self):
        context = StripeContext.parse("a")
        assert context._segments == ["a"]

    def test_parse_multiple_segments(self):
        context = StripeContext.parse("a/b/c")
        assert context._segments == ["a", "b", "c"]


class TestStripeContextIntegration:
    def test_request_options_string_context(self):
        requestor = RequestorOptions(api_key="sk_test_123")
        request: RequestOptions = {"stripe_context": "a/b/c"}

        merged = merge_options(requestor, request)
        assert merged.get("stripe_context") == "a/b/c"

    def test_request_options_context_object(self):
        requestor = RequestorOptions(api_key="sk_test_123")
        context = StripeContext(["a", "b", "c"])
        request: RequestOptions = {"stripe_context": context}

        merged = merge_options(requestor, request)
        assert merged.get("stripe_context") == context

    def test_precedence_no_context(self):
        requestor = RequestorOptions(api_key="sk_test_123")
        merged = merge_options(requestor, None)

        assert merged.get("stripe_context") is None

    def test_precedence_client_context_only(self):
        context = StripeContext(["client"])
        requestor = RequestorOptions(
            api_key="sk_test_123", stripe_context=context
        )
        merged = merge_options(requestor, None)

        assert merged.get("stripe_context") == context

    def test_precedence_request_context_only(self):
        requestor = RequestorOptions(api_key="sk_test_123")
        context = StripeContext(["request"])
        request: RequestOptions = {"stripe_context": context}

        merged = merge_options(requestor, request)
        assert merged.get("stripe_context") == context

    def test_precedence_request_overrides_client(self):
        client_context = StripeContext(["client"])
        request_context = StripeContext(["request"])
        requestor = RequestorOptions(
            api_key="sk_test_123", stripe_context=client_context
        )
        request: RequestOptions = {"stripe_context": request_context}

        merged = merge_options(requestor, request)
        assert merged.get("stripe_context") == request_context

    def test_precedence_string_overrides_client_context(self):
        client_context = StripeContext(["client"])
        requestor = RequestorOptions(
            api_key="sk_test_123", stripe_context=client_context
        )
        request: RequestOptions = {"stripe_context": "request/string"}

        merged = merge_options(requestor, request)
        assert merged.get("stripe_context") == "request/string"

    def test_request_can_clear_client_context(self):
        client_context = StripeContext(["client"])
        requestor = RequestorOptions(
            api_key="sk_test_123", stripe_context=client_context
        )
        ctx = StripeContext()
        request: RequestOptions = {"stripe_context": ctx}

        merged = merge_options(requestor, request)
        assert merged.get("stripe_context") is ctx

    def test_stripe_client_accepts_string(self):
        client = stripe.StripeClient(
            api_key="sk_test_123", stripe_context="a/b/c"
        )
        assert client._requestor._options.stripe_context == "a/b/c"

    def test_stripe_client_accepts_context_object(self):
        context = StripeContext(["a", "b", "c"])
        client = stripe.StripeClient(
            api_key="sk_test_123", stripe_context=context
        )
        assert client._requestor._options.stripe_context == context

    def test_event_notification_parsing(self):
        mock_client = Mock()
        parsed_body = {
            "id": "evt_123",
            "type": "test.event",
            "created": "2023-01-01T00:00:00Z",
            "livemode": False,
            "context": "a/b/c",
        }

        notification = EventNotification(parsed_body, mock_client)

        assert isinstance(notification.context, StripeContext)
        assert notification.context._segments == ["a", "b", "c"]

    def test_event_notification_no_context(self):
        mock_client = Mock()
        parsed_body = {
            "id": "evt_123",
            "type": "test.event",
            "created": "2023-01-01T00:00:00Z",
            "livemode": False,
        }

        notification = EventNotification(parsed_body, mock_client)

        assert notification.context is None

    def test_event_notification_empty_context(self):
        mock_client = Mock()
        parsed_body = {
            "id": "evt_123",
            "type": "test.event",
            "created": "2023-01-01T00:00:00Z",
            "livemode": False,
            "context": "",
        }

        notification = EventNotification(parsed_body, mock_client)

        assert notification.context is None

    @pytest.mark.parametrize(
        ["options", "expected"],
        [
            ({}, None),
            ({"stripe_context": StripeContext()}, None),
            (
                {"stripe_context": "workspace_123/account_456"},
                "workspace_123/account_456",
            ),
            (
                {
                    "stripe_context": StripeContext.parse(
                        "workspace_123/account_456/customer_789"
                    )
                },
                "workspace_123/account_456/customer_789",
            ),
        ],
    )
    def test_request_headers(self, options, expected):
        requestor = _api_requestor._APIRequestor()
        headers = requestor.request_headers("get", "V1", options)

        assert headers.get("Stripe-Context") == expected


class TestStripeContextUsagePatterns:
    def test_context_manipulation_pattern(self):
        # Common usage: start with base context, add child contexts
        base = StripeContext.parse("workspace_123")
        child = base.push("account_456")
        grandchild = child.push("customer_789")

        assert str(base) == "workspace_123"
        assert str(child) == "workspace_123/account_456"
        assert str(grandchild) == "workspace_123/account_456/customer_789"

        # Go back up the hierarchy
        back_to_child = grandchild.pop()
        back_to_base = back_to_child.pop()

        assert str(back_to_child) == "workspace_123/account_456"
        assert str(back_to_base) == "workspace_123"

    def test_context_immutability(self):
        original = StripeContext(["a", "b"])

        # Multiple operations on the same context
        pushed = original.push("c")
        popped = original.pop()

        # Original remains unchanged
        assert original._segments == ["a", "b"]
        assert pushed._segments == ["a", "b", "c"]
        assert popped._segments == ["a"]

        # All are different objects
        assert original is not pushed
        assert original is not popped
        assert pushed is not popped
