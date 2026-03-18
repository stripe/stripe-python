"""
Tests for V2 int64_string field encoding and decoding.

V2 API int64 fields are encoded as strings on the wire but exposed as
native Python ints. These tests verify both directions:
- Request serialization: int → JSON string
- Response hydration: JSON string → int
"""

from unittest.mock import MagicMock

from stripe._encode import _coerce_int64_string, _coerce_v2_params
from stripe._stripe_object import StripeObject
from stripe._stripe_service import StripeService


class TestCoerceInt64String:
    """Tests for the shared bidirectional coercion helper."""

    def test_encode_int_to_str(self):
        assert _coerce_int64_string(42, encode=True) == "42"

    def test_decode_str_to_int(self):
        assert _coerce_int64_string("42", encode=False) == 42

    def test_encode_list(self):
        assert _coerce_int64_string([1, 2, 3], encode=True) == ["1", "2", "3"]

    def test_decode_list(self):
        assert _coerce_int64_string(["1", "2", "3"], encode=False) == [1, 2, 3]

    def test_none_passthrough(self):
        assert _coerce_int64_string(None, encode=True) is None
        assert _coerce_int64_string(None, encode=False) is None

    def test_wrong_type_passthrough(self):
        assert _coerce_int64_string("already_str", encode=True) == "already_str"
        assert _coerce_int64_string(42, encode=False) == 42


class TestCoerceV2Params:
    """Tests for outbound request coercion (int → str)."""

    def test_top_level_int64_string(self):
        params = {"amount": 12345}
        schema = {"amount": "int64_string"}
        result = _coerce_v2_params(params, schema)
        assert result == {"amount": "12345"}

    def test_nested_int64_string(self):
        params = {"nested": {"count": 42}}
        schema = {"nested": {"count": "int64_string"}}
        result = _coerce_v2_params(params, schema)
        assert result == {"nested": {"count": "42"}}

    def test_array_of_int64_string(self):
        params = {"amounts": [100, 200, 300]}
        schema = {"amounts": "int64_string"}
        result = _coerce_v2_params(params, schema)
        assert result == {"amounts": ["100", "200", "300"]}

    def test_array_of_objects_with_int64_string(self):
        params = {"items": [{"amount": 100}, {"amount": 200}]}
        schema = {"items": {"amount": "int64_string"}}
        result = _coerce_v2_params(params, schema)
        assert result == {"items": [{"amount": "100"}, {"amount": "200"}]}

    def test_unrelated_fields_unchanged(self):
        params = {"name": "test", "count": 42, "amount": 100}
        schema = {"amount": "int64_string"}
        result = _coerce_v2_params(params, schema)
        assert result == {"name": "test", "count": 42, "amount": "100"}

    def test_none_params_returns_none(self):
        schema = {"amount": "int64_string"}
        result = _coerce_v2_params(None, schema)
        assert result is None

    def test_none_value_preserved(self):
        params = {"amount": None}
        schema = {"amount": "int64_string"}
        result = _coerce_v2_params(params, schema)
        assert result == {"amount": None}

    def test_deeply_nested_int64_string(self):
        params = {"level1": {"level2": {"value": 999}}}
        schema = {"level1": {"level2": {"value": "int64_string"}}}
        result = _coerce_v2_params(params, schema)
        assert result == {"level1": {"level2": {"value": "999"}}}

    def test_mixed_fields_only_int64_coerced(self):
        params = {
            "name": "test",
            "amount": 100,
            "metadata": {"key": "val"},
            "count": 5,
        }
        schema = {"amount": "int64_string", "count": "int64_string"}
        result = _coerce_v2_params(params, schema)
        assert result == {
            "name": "test",
            "amount": "100",
            "metadata": {"key": "val"},
            "count": "5",
        }

    def test_empty_schema_no_coercion(self):
        params = {"amount": 100}
        schema = {}
        result = _coerce_v2_params(params, schema)
        assert result == {"amount": 100}

    def test_large_int64_value(self):
        params = {"amount": 9223372036854775807}  # max int64
        schema = {"amount": "int64_string"}
        result = _coerce_v2_params(params, schema)
        assert result == {"amount": "9223372036854775807"}

    def test_zero_value(self):
        params = {"amount": 0}
        schema = {"amount": "int64_string"}
        result = _coerce_v2_params(params, schema)
        assert result == {"amount": "0"}

    def test_negative_value(self):
        params = {"amount": -100}
        schema = {"amount": "int64_string"}
        result = _coerce_v2_params(params, schema)
        assert result == {"amount": "-100"}


class TestResponseFieldCoercion:
    """Tests for inbound response coercion (str → int) via _field_encodings."""

    def _make_v2_class(self, field_encodings):
        """Create a StripeObject subclass with given field encodings."""

        class V2Resource(StripeObject):
            _field_encodings = field_encodings

        return V2Resource

    def test_top_level_int64_string_response(self):
        cls = self._make_v2_class({"amount": "int64_string"})
        obj = cls.construct_from(
            {"id": "test", "amount": "12345"},
            key="sk_test",
            api_mode="V2",
        )
        assert obj["amount"] == 12345
        assert isinstance(obj["amount"], int)

    def test_nested_class_int64_string_response(self):
        """Nested StripeObject classes coerce their own fields."""

        class InnerObj(StripeObject):
            _field_encodings = {"count": "int64_string"}

        class OuterObj(StripeObject):
            _inner_class_types = {"inner": InnerObj}

        obj = OuterObj.construct_from(
            {"id": "test", "inner": {"count": "42"}},
            key="sk_test",
            api_mode="V2",
        )
        assert obj["inner"]["count"] == 42
        assert isinstance(obj["inner"]["count"], int)

    def test_array_of_int64_string_response(self):
        cls = self._make_v2_class({"amounts": "int64_string"})
        obj = cls.construct_from(
            {"id": "test", "amounts": ["100", "200", "300"]},
            key="sk_test",
            api_mode="V2",
        )
        assert obj["amounts"] == [100, 200, 300]
        assert all(isinstance(v, int) for v in obj["amounts"])

    def test_unrelated_fields_unchanged_response(self):
        cls = self._make_v2_class({"amount": "int64_string"})
        obj = cls.construct_from(
            {"id": "test", "name": "hello", "amount": "100"},
            key="sk_test",
            api_mode="V2",
        )
        assert obj["name"] == "hello"
        assert isinstance(obj["name"], str)
        assert obj["amount"] == 100

    def test_none_value_preserved_response(self):
        cls = self._make_v2_class({"amount": "int64_string"})
        obj = cls.construct_from(
            {"id": "test", "amount": None},
            key="sk_test",
            api_mode="V2",
        )
        assert obj["amount"] is None

    def test_no_field_encodings_unchanged(self):
        """StripeObject without _field_encodings leaves strings as strings."""
        obj = StripeObject.construct_from(
            {"id": "test", "amount": "12345"},
            key="sk_test",
            api_mode="V2",
        )
        assert obj["amount"] == "12345"
        assert isinstance(obj["amount"], str)

    def test_large_int64_response(self):
        cls = self._make_v2_class({"amount": "int64_string"})
        obj = cls.construct_from(
            {"id": "test", "amount": "9223372036854775807"},
            key="sk_test",
            api_mode="V2",
        )
        assert obj["amount"] == 9223372036854775807

    def test_zero_response(self):
        cls = self._make_v2_class({"amount": "int64_string"})
        obj = cls.construct_from(
            {"id": "test", "amount": "0"},
            key="sk_test",
            api_mode="V2",
        )
        assert obj["amount"] == 0

    def test_negative_response(self):
        cls = self._make_v2_class({"amount": "int64_string"})
        obj = cls.construct_from(
            {"id": "test", "amount": "-100"},
            key="sk_test",
            api_mode="V2",
        )
        assert obj["amount"] == -100


class TestServiceParamEncodings:
    """Tests that StripeService._request wires up _coerce_v2_params."""

    def test_request_coerces_params_with_encodings(self):
        mock_requestor = MagicMock()
        mock_requestor.request.return_value = StripeObject()
        service = StripeService(mock_requestor)

        service._request(
            "post",
            "/v2/test",
            params={"amount": 100, "name": "test"},
            base_address="api",
            _param_encodings={"amount": "int64_string"},
        )

        call_args = mock_requestor.request.call_args
        coerced_params = call_args[0][2]
        assert coerced_params == {"amount": "100", "name": "test"}

    def test_request_skips_coercion_without_encodings(self):
        mock_requestor = MagicMock()
        mock_requestor.request.return_value = StripeObject()
        service = StripeService(mock_requestor)

        original_params = {"amount": 100, "name": "test"}
        service._request(
            "post",
            "/v2/test",
            params=original_params,
            base_address="api",
        )

        call_args = mock_requestor.request.call_args
        passed_params = call_args[0][2]
        assert passed_params is original_params


class TestV1Unchanged:
    """Regression tests: V1 behavior should not be affected."""

    def test_v1_integer_fields_stay_integers(self):
        """V1 objects don't have _field_encodings, so ints stay ints."""
        obj = StripeObject.construct_from(
            {"id": "test", "amount": 100},
            key="sk_test",
            api_mode="V1",
        )
        assert obj["amount"] == 100
        assert isinstance(obj["amount"], int)

    def test_v1_string_fields_stay_strings(self):
        obj = StripeObject.construct_from(
            {"id": "test", "name": "hello"},
            key="sk_test",
            api_mode="V1",
        )
        assert obj["name"] == "hello"
        assert isinstance(obj["name"], str)

    def test_object_without_field_encodings_unchanged(self):
        """Objects without _field_encodings are unaffected."""
        obj = StripeObject.construct_from(
            {"id": "test", "amount": "12345", "count": 42},
            key="sk_test",
        )
        assert obj["amount"] == "12345"
        assert obj["count"] == 42
