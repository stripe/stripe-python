import pytest
from stripe._api_requestor import _APIRequestor
from stripe._stripe_context import StripeContext
from stripe.v2._event import ThinEvent


class TestStripeContext:
    def test_init_empty(self):
        context = StripeContext()
        assert str(context) == ""

    def test_init_with_segments(self):
        context = StripeContext(["a", "b", "c"])
        assert str(context) == "a/b/c"

    def test_parse_empty_string(self):
        context = StripeContext.parse("")
        assert str(context) == ""

    def test_parse_single_segment(self):
        context = StripeContext.parse("a")
        assert str(context) == "a"

    def test_parse_multiple_segments(self):
        context = StripeContext.parse("a/b/c")
        assert str(context) == "a/b/c"

    def test_child_returns_new_instance(self):
        context = StripeContext.parse("a/b")
        child_context = context.child("c")

        assert str(context) == "a/b"  # Original unchanged
        assert str(child_context) == "a/b/c"  # New instance with added segment

    def test_parent_returns_new_instance(self):
        context = StripeContext.parse("a/b/c")
        parent_context = context.parent()

        assert str(context) == "a/b/c"  # Original unchanged
        assert (
            str(parent_context) == "a/b"
        )  # New instance with removed segment

    def test_parent_of_empty_context_raises_error(self):
        context = StripeContext()
        with pytest.raises(
            ValueError, match="Cannot get parent of empty context"
        ):
            context.parent()

    def test_parent_of_single_segment_context(self):
        context = StripeContext.parse("a")
        parent_context = context.parent()
        assert str(parent_context) == ""

    def test_repr(self):
        context = StripeContext(["a", "b"])
        assert repr(context) == "StripeContext(['a', 'b'])"

    def test_chaining_operations(self):
        context = StripeContext.parse("a")
        result = context.child("b").child("c").parent()
        assert str(result) == "a/b"


class TestStripeContextThinEvent:
    def test_thin_event_with_no_context(self):
        payload = '{"id": "evt_123", "type": "payment.created", "created": "2023-01-01", "livemode": false}'
        event = ThinEvent(payload)

        assert event.context is None

    def test_thin_event_with_context_string(self):
        payload = '{"id": "evt_123", "type": "payment.created", "created": "2023-01-01", "livemode": false, "context": "a/b/c"}'
        event = ThinEvent(payload)

        assert isinstance(event.context, StripeContext)
        assert str(event.context) == "a/b/c"

    def test_thin_event_with_empty_context_string(self):
        payload = '{"id": "evt_123", "type": "payment.created", "created": "2023-01-01", "livemode": false, "context": ""}'
        event = ThinEvent(payload)

        assert isinstance(event.context, StripeContext)
        assert str(event.context) == ""


class TestHeaderConversion:
    def test_strings_get_sent(self):
        r = _APIRequestor()
        result = r.request_headers(
            "get", "V1", {"stripe_context": "ctx_123/acct_1234"}
        )
        assert result["Stripe-Context"] == "ctx_123/acct_1234"

    def test_objects_are_converted(self):
        r = _APIRequestor()
        result = r.request_headers(
            "get",
            "V1",
            {"stripe_context": StripeContext(["ctx_123", "acct_1234"])},
        )
        assert result["Stripe-Context"] == "ctx_123/acct_1234"

    def test_empty_values_arent_sent(self):
        r = _APIRequestor()
        result = r.request_headers(
            "get",
            "V1",
            {"stripe_context": StripeContext()},
        )
        assert "Stripe-Context" not in result
