"""
Tests for discriminated union runtime behavior.

Validates that the generated TypedDict param shapes and StripeObject responses
work correctly at runtime (dict construction, field access, round-trip).
Static type narrowing (Literal discriminators, Union resolution) is verified
separately by pyright/mypy — this file exercises runtime semantics only.

Covers both sides of the API boundary:
- Request side: TypedDict params with Literal discriminator fields
- Response side: StripeObject deserialization from JSON with a discriminator

Two structural patterns are tested:
- Standalone union: the discriminated union is its own type (e.g. ColorParams)
- Inline union: the discriminator lives at the parent object level (e.g. shape.type)
"""

from typing import Optional, Union

from typing_extensions import Literal, NotRequired, TypedDict

from stripe._encode import _api_encode
from stripe._stripe_object import StripeObject


# ---------------------------------------------------------------------------
# Standalone discriminated union — TypedDict variants
# ---------------------------------------------------------------------------


class RgbColorParams(TypedDict):
    model: Literal["rgb"]
    r: int
    g: NotRequired[int]
    b: NotRequired[int]


class HsvColorParams(TypedDict):
    model: Literal["hsv"]
    h: int
    s: NotRequired[int]
    v: NotRequired[int]


ColorParams = Union[RgbColorParams, HsvColorParams]


# ---------------------------------------------------------------------------
# Inline discriminated union — flattened onto parent TypedDict
# ---------------------------------------------------------------------------


class CardData(TypedDict):
    number: str
    exp_month: NotRequired[int]


class BankData(TypedDict):
    routing_number: str
    account_number: NotRequired[str]


# Inline union: discriminator + per-variant nullable payload fields on one parent TypedDict
class PaymentParams(TypedDict):
    amount: int
    type: NotRequired[str]
    card: NotRequired[CardData]
    bank: NotRequired[BankData]


# ---------------------------------------------------------------------------
# Request-side: standalone discriminated union
# ---------------------------------------------------------------------------


class TestStandaloneUnionRequestSide:
    """Standalone DU params encode through _api_encode with bracket notation."""

    def test_rgb_variant_encodes_discriminator(self):
        params: RgbColorParams = {"model": "rgb", "r": 255, "g": 128, "b": 0}
        encoded = dict(_api_encode({"color": params}))
        assert encoded["color[model]"] == "rgb"

    def test_rgb_variant_encodes_payload_fields(self):
        params: RgbColorParams = {"model": "rgb", "r": 255, "g": 128, "b": 0}
        encoded = dict(_api_encode({"color": params}))
        assert encoded["color[r]"] == 255
        assert encoded["color[g]"] == 128
        assert encoded["color[b]"] == 0

    def test_hsv_variant_encodes_discriminator(self):
        params: HsvColorParams = {"model": "hsv", "h": 180, "s": 100, "v": 50}
        encoded = dict(_api_encode({"color": params}))
        assert encoded["color[model]"] == "hsv"

    def test_hsv_variant_encodes_payload_fields(self):
        params: HsvColorParams = {"model": "hsv", "h": 180, "s": 100, "v": 50}
        encoded = dict(_api_encode({"color": params}))
        assert encoded["color[h]"] == 180
        assert encoded["color[s]"] == 100
        assert encoded["color[v]"] == 50

    def test_optional_fields_omitted_when_absent(self):
        """None values are skipped by _api_encode."""
        params: RgbColorParams = {"model": "rgb", "r": 255}
        encoded = dict(_api_encode({"color": params}))
        assert encoded["color[model]"] == "rgb"
        assert encoded["color[r]"] == 255
        assert "color[g]" not in encoded
        assert "color[b]" not in encoded

    def test_union_type_rgb_encodes_correctly(self):
        params: ColorParams = {"model": "rgb", "r": 255, "g": 0, "b": 0}
        encoded = dict(_api_encode({"color": params}))
        assert encoded["color[model]"] == "rgb"
        assert encoded["color[r]"] == 255


# ---------------------------------------------------------------------------
# Request-side: inline discriminated union (discriminator at parent level)
# ---------------------------------------------------------------------------


class TestInlineUnionRequestSide:
    """Inline DU params encode with discriminator at top level and nested variant payloads."""

    def test_card_variant_encodes_discriminator_at_top_level(self):
        params: PaymentParams = {"amount": 1000, "type": "card", "card": {"number": "4242424242424242"}}
        encoded = dict(_api_encode(params))
        assert encoded["type"] == "card"

    def test_card_variant_encodes_nested_payload(self):
        params: PaymentParams = {"amount": 1000, "type": "card", "card": {"number": "4242424242424242", "exp_month": 12}}
        encoded = dict(_api_encode(params))
        assert encoded["card[number]"] == "4242424242424242"
        assert encoded["card[exp_month]"] == 12

    def test_card_variant_encodes_base_fields(self):
        params: PaymentParams = {"amount": 1000, "type": "card", "card": {"number": "4242"}}
        encoded = dict(_api_encode(params))
        assert encoded["amount"] == 1000

    def test_bank_variant_encodes_correctly(self):
        params: PaymentParams = {"amount": 500, "type": "bank", "bank": {"routing_number": "110000000", "account_number": "000123456789"}}
        encoded = dict(_api_encode(params))
        assert encoded["type"] == "bank"
        assert encoded["bank[routing_number]"] == "110000000"
        assert encoded["bank[account_number]"] == "000123456789"

    def test_non_selected_variant_not_encoded(self):
        """When card is selected, bank keys do not appear in encoded output."""
        params: PaymentParams = {"amount": 1000, "type": "card", "card": {"number": "4242"}}
        encoded = dict(_api_encode(params))
        assert "bank[routing_number]" not in encoded
        assert "bank[account_number]" not in encoded

    def test_optional_nested_fields_omitted(self):
        params: PaymentParams = {"amount": 100, "type": "card", "card": {"number": "4242"}}
        encoded = dict(_api_encode(params))
        assert "card[exp_month]" not in encoded


# ---------------------------------------------------------------------------
# Response-side: StripeObject deserialization
# ---------------------------------------------------------------------------


class TestStandaloneUnionResponseDeserialization:
    """JSON payloads with a discriminator field deserialize via StripeObject."""

    def test_rgb_response_discriminator_accessible(self):
        json_data = {"model": "rgb", "r": 255, "g": 128, "b": 0}
        obj = StripeObject.construct_from(json_data, key="sk_test_xxx")
        assert obj.model == "rgb"

    def test_rgb_response_payload_fields_accessible(self):
        json_data = {"model": "rgb", "r": 255, "g": 128, "b": 0}
        obj = StripeObject.construct_from(json_data, key="sk_test_xxx")
        assert obj.r == 255
        assert obj.g == 128
        assert obj.b == 0

    def test_hsv_response_discriminator_accessible(self):
        json_data = {"model": "hsv", "h": 180, "s": 75, "v": 90}
        obj = StripeObject.construct_from(json_data, key="sk_test_xxx")
        assert obj.model == "hsv"

    def test_hsv_response_payload_fields_accessible(self):
        json_data = {"model": "hsv", "h": 180, "s": 75, "v": 90}
        obj = StripeObject.construct_from(json_data, key="sk_test_xxx")
        assert obj.h == 180
        assert obj.s == 75
        assert obj.v == 90

    def test_response_discriminator_in_dict_output(self):
        """to_dict() must include the discriminator field."""
        json_data = {"model": "rgb", "r": 64, "g": 64, "b": 64}
        obj = StripeObject.construct_from(json_data, key="sk_test_xxx")
        d = obj.to_dict()
        assert "model" in d
        assert d["model"] == "rgb"

    def test_response_bracket_access(self):
        """Discriminator and payload fields are accessible via bracket notation."""
        json_data = {"model": "rgb", "r": 10}
        obj = StripeObject.construct_from(json_data, key="sk_test_xxx")
        assert obj["model"] == "rgb"
        assert obj["r"] == 10

    def test_rgb_minimal_response(self):
        """Only the discriminator and one required field is sufficient."""
        json_data = {"model": "rgb", "r": 255}
        obj = StripeObject.construct_from(json_data, key="sk_test_xxx")
        assert obj.model == "rgb"
        assert obj.r == 255


class TestInlineUnionResponseDeserialization:
    """JSON with the discriminator at the parent level and variant data nested."""

    def test_card_discriminator_accessible(self):
        json_data = {"type": "card", "card": {"number": "4242424242424242", "exp_month": 12}, "amount": 1000}
        obj = StripeObject.construct_from(json_data, key="sk_test_xxx")
        assert obj.type == "card"

    def test_card_payload_is_stripe_object(self):
        json_data = {"type": "card", "card": {"number": "4242424242424242", "exp_month": 12}, "amount": 1000}
        obj = StripeObject.construct_from(json_data, key="sk_test_xxx")
        assert obj.card.number == "4242424242424242"
        assert obj.card.exp_month == 12

    def test_bank_discriminator_accessible(self):
        json_data = {"type": "bank", "bank": {"routing_number": "110000000", "account_number": "000123456789"}, "amount": 500}
        obj = StripeObject.construct_from(json_data, key="sk_test_xxx")
        assert obj.type == "bank"

    def test_bank_payload_is_stripe_object(self):
        json_data = {"type": "bank", "bank": {"routing_number": "110000000", "account_number": "000123456789"}, "amount": 500}
        obj = StripeObject.construct_from(json_data, key="sk_test_xxx")
        assert obj.bank.routing_number == "110000000"
        assert obj.bank.account_number == "000123456789"

    def test_non_selected_variant_absent(self):
        json_data = {"type": "card", "card": {"number": "4242"}, "amount": 100}
        obj = StripeObject.construct_from(json_data, key="sk_test_xxx")
        assert obj.type == "card"
        assert not hasattr(obj, "bank") or obj.get("bank") is None

    def test_inline_discriminator_in_dict_output(self):
        json_data = {"type": "card", "card": {"number": "4242"}, "amount": 100}
        obj = StripeObject.construct_from(json_data, key="sk_test_xxx")
        d = obj.to_dict()
        assert d["type"] == "card"
        assert d["card"]["number"] == "4242"


# ---------------------------------------------------------------------------
# Serialization round-trip
# ---------------------------------------------------------------------------


class TestDiscriminatedUnionSerializationRoundTrip:
    """Full pipeline: params encode via _api_encode, responses deserialize via construct_from."""

    def test_standalone_params_encode_round_trip(self):
        params: RgbColorParams = {"model": "rgb", "r": 200, "g": 100, "b": 50}
        encoded = dict(_api_encode({"color": params}))
        assert encoded["color[model]"] == "rgb"
        assert encoded["color[r]"] == 200
        assert encoded["color[g]"] == 100
        assert encoded["color[b]"] == 50

    def test_inline_params_encode_round_trip(self):
        params: PaymentParams = {"amount": 100, "type": "card", "card": {"number": "4242"}}
        encoded = dict(_api_encode(params))
        assert encoded["type"] == "card"
        assert encoded["card[number]"] == "4242"
        assert encoded["amount"] == 100

    def test_standalone_response_round_trip(self):
        """Deserialize and re-serialize preserves discriminator."""
        original = {"model": "rgb", "r": 255, "g": 0, "b": 0}
        obj = StripeObject.construct_from(original, key="sk_test_xxx")
        result = obj.to_dict()
        assert result["model"] == "rgb"
        assert result == original

    def test_inline_response_round_trip(self):
        """Deserialize inline DU response and re-serialize preserves structure."""
        original = {"type": "card", "card": {"number": "4242"}, "amount": 100}
        obj = StripeObject.construct_from(original, key="sk_test_xxx")
        result = obj.to_dict()
        assert result["type"] == "card"
        assert result["card"] == {"number": "4242"}
        assert result["amount"] == 100
