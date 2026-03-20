"""
Tests for V2 decimal_string field encoding and decoding.

V2 API decimal fields are encoded as strings on the wire but exposed as
native Python Decimal values. These tests verify both directions:
- Request serialization: Decimal/int/float → JSON string
- Response hydration: JSON string → Decimal
"""

from decimal import Decimal

from stripe._encode import _coerce_decimal_string, _coerce_v2_params
from stripe._stripe_object import StripeObject


class TestCoerceDecimalString:
    """Tests for the shared bidirectional coercion helper."""

    def test_encode_decimal_to_str(self):
        assert _coerce_decimal_string(Decimal("1.5"), encode=True) == "1.5"

    def test_encode_int_to_str(self):
        assert _coerce_decimal_string(100, encode=True) == "100"

    def test_encode_float_to_str(self):
        assert _coerce_decimal_string(1.5, encode=True) == "1.5"

    def test_decode_str_to_decimal(self):
        result = _coerce_decimal_string("1.5", encode=False)
        assert result == Decimal("1.5")
        assert isinstance(result, Decimal)

    def test_encode_list(self):
        result = _coerce_decimal_string(
            [Decimal("1.1"), Decimal("2.2"), Decimal("3.3")], encode=True
        )
        assert result == ["1.1", "2.2", "3.3"]

    def test_decode_list(self):
        result = _coerce_decimal_string(["1.1", "2.2", "3.3"], encode=False)
        assert result == [Decimal("1.1"), Decimal("2.2"), Decimal("3.3")]
        assert all(isinstance(v, Decimal) for v in result)

    def test_none_passthrough(self):
        assert _coerce_decimal_string(None, encode=True) is None
        assert _coerce_decimal_string(None, encode=False) is None

    def test_bool_not_coerced_encode(self):
        """Booleans must not be coerced (bool is subclass of int)."""
        assert _coerce_decimal_string(True, encode=True) is True
        assert _coerce_decimal_string(False, encode=True) is False

    def test_already_str_passthrough_encode(self):
        """A string value passes through on encode (already serialized)."""
        assert _coerce_decimal_string("1.5", encode=True) == "1.5"

    def test_non_str_passthrough_decode(self):
        """Non-string values pass through on decode."""
        assert _coerce_decimal_string(42, encode=False) == 42


class TestDecimalStringPrecision:
    """Precision is preserved through the encode/decode round-trip."""

    def test_high_precision_encode(self):
        value = Decimal("1.23456789012345678901234567890")
        result = _coerce_decimal_string(value, encode=True)
        assert result == "1.23456789012345678901234567890"

    def test_high_precision_decode(self):
        result = _coerce_decimal_string(
            "1.23456789012345678901234567890", encode=False
        )
        assert result == Decimal("1.23456789012345678901234567890")

    def test_round_trip_preserves_precision(self):
        original = Decimal("9999999999999999.9999999999999999")
        encoded = _coerce_decimal_string(original, encode=True)
        decoded = _coerce_decimal_string(encoded, encode=False)
        assert decoded == original

    def test_zero(self):
        assert _coerce_decimal_string(Decimal("0"), encode=True) == "0"
        assert _coerce_decimal_string("0", encode=False) == Decimal("0")

    def test_negative(self):
        assert _coerce_decimal_string(Decimal("-1.5"), encode=True) == "-1.5"
        assert _coerce_decimal_string("-1.5", encode=False) == Decimal("-1.5")


class TestCoerceV2ParamsDecimalString:
    """Tests for outbound request coercion (Decimal → str)."""

    def test_top_level_decimal_string(self):
        params = {"price": Decimal("9.99")}
        schema = {"price": "decimal_string"}
        result = _coerce_v2_params(params, schema)
        assert result == {"price": "9.99"}

    def test_nested_decimal_string(self):
        params = {"item": {"price": Decimal("1.50")}}
        schema = {"item": {"price": "decimal_string"}}
        result = _coerce_v2_params(params, schema)
        assert result == {"item": {"price": "1.50"}}

    def test_array_of_decimal_string(self):
        params = {"prices": [Decimal("1.0"), Decimal("2.0"), Decimal("3.0")]}
        schema = {"prices": "decimal_string"}
        result = _coerce_v2_params(params, schema)
        assert result == {"prices": ["1.0", "2.0", "3.0"]}

    def test_array_of_objects_with_decimal_string(self):
        params = {"items": [{"price": Decimal("1.00")}, {"price": Decimal("2.00")}]}
        schema = {"items": {"price": "decimal_string"}}
        result = _coerce_v2_params(params, schema)
        assert result == {"items": [{"price": "1.00"}, {"price": "2.00"}]}

    def test_unrelated_fields_unchanged(self):
        params = {"name": "test", "count": 42, "price": Decimal("9.99")}
        schema = {"price": "decimal_string"}
        result = _coerce_v2_params(params, schema)
        assert result == {"name": "test", "count": 42, "price": "9.99"}

    def test_none_params_returns_none(self):
        schema = {"price": "decimal_string"}
        result = _coerce_v2_params(None, schema)
        assert result is None

    def test_none_value_preserved(self):
        params = {"price": None}
        schema = {"price": "decimal_string"}
        result = _coerce_v2_params(params, schema)
        assert result == {"price": None}

    def test_int_value_coerced(self):
        """int values are also accepted as decimal_string inputs."""
        params = {"price": 10}
        schema = {"price": "decimal_string"}
        result = _coerce_v2_params(params, schema)
        assert result == {"price": "10"}

    def test_mixed_decimal_and_int64(self):
        params = {"price": Decimal("9.99"), "quantity": 5}
        schema = {"price": "decimal_string", "quantity": "int64_string"}
        result = _coerce_v2_params(params, schema)
        assert result == {"price": "9.99", "quantity": "5"}


class TestResponseFieldCoercion:
    """Tests for inbound response coercion (str → Decimal) via _field_encodings."""

    def _make_v2_class(self, field_encodings):
        """Create a StripeObject subclass with given field encodings."""

        class V2Resource(StripeObject):
            _field_encodings = field_encodings

        return V2Resource

    def test_top_level_decimal_string_response(self):
        cls = self._make_v2_class({"price": "decimal_string"})
        obj = cls.construct_from(
            {"id": "test", "price": "9.99"},
            key="sk_test",
            api_mode="V2",
        )
        assert obj["price"] == Decimal("9.99")
        assert isinstance(obj["price"], Decimal)

    def test_array_of_decimal_string_response(self):
        cls = self._make_v2_class({"prices": "decimal_string"})
        obj = cls.construct_from(
            {"id": "test", "prices": ["1.0", "2.0", "3.0"]},
            key="sk_test",
            api_mode="V2",
        )
        assert obj["prices"] == [Decimal("1.0"), Decimal("2.0"), Decimal("3.0")]
        assert all(isinstance(v, Decimal) for v in obj["prices"])

    def test_unrelated_fields_unchanged_response(self):
        cls = self._make_v2_class({"price": "decimal_string"})
        obj = cls.construct_from(
            {"id": "test", "name": "hello", "price": "9.99"},
            key="sk_test",
            api_mode="V2",
        )
        assert obj["name"] == "hello"
        assert isinstance(obj["name"], str)
        assert obj["price"] == Decimal("9.99")

    def test_none_value_preserved_response(self):
        cls = self._make_v2_class({"price": "decimal_string"})
        obj = cls.construct_from(
            {"id": "test", "price": None},
            key="sk_test",
            api_mode="V2",
        )
        assert obj["price"] is None

    def test_no_field_encodings_unchanged(self):
        """StripeObject without _field_encodings leaves strings as strings."""
        obj = StripeObject.construct_from(
            {"id": "test", "price": "9.99"},
            key="sk_test",
            api_mode="V2",
        )
        assert obj["price"] == "9.99"
        assert isinstance(obj["price"], str)

    def test_high_precision_response(self):
        cls = self._make_v2_class({"rate": "decimal_string"})
        obj = cls.construct_from(
            {"id": "test", "rate": "0.00123456789012345678"},
            key="sk_test",
            api_mode="V2",
        )
        assert obj["rate"] == Decimal("0.00123456789012345678")

    def test_negative_response(self):
        cls = self._make_v2_class({"balance": "decimal_string"})
        obj = cls.construct_from(
            {"id": "test", "balance": "-100.50"},
            key="sk_test",
            api_mode="V2",
        )
        assert obj["balance"] == Decimal("-100.50")


class TestV1Unchanged:
    """Regression tests: V1 behavior should not be affected."""

    def test_v1_integer_fields_stay_integers(self):
        """V1 objects don't have decimal _field_encodings, so ints stay ints."""
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
        """Objects without decimal _field_encodings are unaffected."""
        obj = StripeObject.construct_from(
            {"id": "test", "price": "9.99", "count": 42},
            key="sk_test",
        )
        assert obj["price"] == "9.99"
        assert obj["count"] == 42
