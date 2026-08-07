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

from typing import Union

from typing_extensions import Literal, NotRequired, TypedDict

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
# Inline discriminated union — discriminator at parent level
# ---------------------------------------------------------------------------


class CircleShapeParams(TypedDict):
    type: Literal["circle"]
    radius: float
    label: NotRequired[str]


class RectangleShapeParams(TypedDict):
    type: Literal["rectangle"]
    width: float
    height: float
    label: NotRequired[str]


ShapeParams = Union[CircleShapeParams, RectangleShapeParams]


# ---------------------------------------------------------------------------
# Request-side: standalone discriminated union
# ---------------------------------------------------------------------------


class TestStandaloneUnionRequestSide:
    """TypedDict params with a dedicated discriminator field."""

    def test_rgb_variant_required_fields(self):
        params: RgbColorParams = {"model": "rgb", "r": 255}
        assert params["model"] == "rgb"
        assert params["r"] == 255

    def test_rgb_variant_all_fields(self):
        params: RgbColorParams = {"model": "rgb", "r": 255, "g": 128, "b": 0}
        assert params["model"] == "rgb"
        assert params["r"] == 255
        assert params["g"] == 128
        assert params["b"] == 0

    def test_hsv_variant_required_fields(self):
        params: HsvColorParams = {"model": "hsv", "h": 180}
        assert params["model"] == "hsv"
        assert params["h"] == 180

    def test_hsv_variant_all_fields(self):
        params: HsvColorParams = {
            "model": "hsv",
            "h": 180,
            "s": 100,
            "v": 50,
        }
        assert params["model"] == "hsv"
        assert params["h"] == 180
        assert params["s"] == 100
        assert params["v"] == 50

    def test_union_type_rgb_is_dict(self):
        params: ColorParams = {"model": "rgb", "r": 255, "g": 0, "b": 0}
        assert isinstance(params, dict)

    def test_union_type_hsv_is_dict(self):
        params: ColorParams = {"model": "hsv", "h": 0, "s": 100, "v": 100}
        assert isinstance(params, dict)

    def test_discriminator_is_serialized(self):
        """The discriminator field must appear in the dict sent to the API."""
        params: RgbColorParams = {"model": "rgb", "r": 128}
        assert "model" in params
        assert params["model"] == "rgb"

    def test_optional_fields_absent_by_default(self):
        """When optional fields are omitted they are not present in the dict."""
        params: RgbColorParams = {"model": "rgb", "r": 64}
        assert "g" not in params
        assert "b" not in params

    def test_optional_fields_present_when_set(self):
        params: HsvColorParams = {"model": "hsv", "h": 90, "s": 50}
        assert "s" in params
        assert "v" not in params


# ---------------------------------------------------------------------------
# Request-side: inline discriminated union (discriminator at parent level)
# ---------------------------------------------------------------------------


class TestInlineUnionRequestSide:
    """Discriminator lives directly on the parent object."""

    def test_circle_variant(self):
        params: CircleShapeParams = {"type": "circle", "radius": 5.0}
        assert params["type"] == "circle"
        assert params["radius"] == 5.0

    def test_rectangle_variant(self):
        params: RectangleShapeParams = {
            "type": "rectangle",
            "width": 10.0,
            "height": 20.0,
        }
        assert params["type"] == "rectangle"
        assert params["width"] == 10.0
        assert params["height"] == 20.0

    def test_circle_discriminator_is_serialized(self):
        params: CircleShapeParams = {"type": "circle", "radius": 3.0}
        assert "type" in params
        assert params["type"] == "circle"

    def test_rectangle_discriminator_is_serialized(self):
        params: RectangleShapeParams = {
            "type": "rectangle",
            "width": 4.0,
            "height": 8.0,
        }
        assert "type" in params
        assert params["type"] == "rectangle"

    def test_circle_optional_label_absent(self):
        params: CircleShapeParams = {"type": "circle", "radius": 1.0}
        assert "label" not in params

    def test_circle_optional_label_present(self):
        params: CircleShapeParams = {
            "type": "circle",
            "radius": 1.0,
            "label": "small",
        }
        assert params["label"] == "small"

    def test_union_assignment_circle(self):
        params: ShapeParams = {"type": "circle", "radius": 7.5}
        assert params["type"] == "circle"

    def test_union_assignment_rectangle(self):
        params: ShapeParams = {
            "type": "rectangle",
            "width": 2.0,
            "height": 4.0,
        }
        assert params["type"] == "rectangle"


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
    """JSON with the discriminator at the parent level deserializes correctly."""

    def test_circle_discriminator_accessible(self):
        json_data = {"type": "circle", "radius": 5.0}
        obj = StripeObject.construct_from(json_data, key="sk_test_xxx")
        assert obj.type == "circle"

    def test_circle_payload_fields_accessible(self):
        json_data = {"type": "circle", "radius": 5.0}
        obj = StripeObject.construct_from(json_data, key="sk_test_xxx")
        assert obj.radius == 5.0

    def test_rectangle_discriminator_accessible(self):
        json_data = {"type": "rectangle", "width": 10.0, "height": 20.0}
        obj = StripeObject.construct_from(json_data, key="sk_test_xxx")
        assert obj.type == "rectangle"

    def test_rectangle_payload_fields_accessible(self):
        json_data = {"type": "rectangle", "width": 10.0, "height": 20.0}
        obj = StripeObject.construct_from(json_data, key="sk_test_xxx")
        assert obj.width == 10.0
        assert obj.height == 20.0

    def test_inline_discriminator_in_dict_output(self):
        json_data = {"type": "circle", "radius": 3.0}
        obj = StripeObject.construct_from(json_data, key="sk_test_xxx")
        d = obj.to_dict()
        assert d["type"] == "circle"
        assert d["radius"] == 3.0

    def test_optional_label_present_in_response(self):
        json_data = {"type": "circle", "radius": 1.0, "label": "tiny"}
        obj = StripeObject.construct_from(json_data, key="sk_test_xxx")
        assert obj.label == "tiny"


# ---------------------------------------------------------------------------
# Serialization round-trip
# ---------------------------------------------------------------------------


class TestDiscriminatedUnionSerializationRoundTrip:
    """Dict construction (params → dict) includes the discriminator on output."""

    def test_rgb_params_round_trip_via_dict(self):
        params: RgbColorParams = {"model": "rgb", "r": 200, "g": 100, "b": 50}
        # TypedDicts are plain dicts at runtime; verify the discriminator and
        # variant fields survive a shallow copy (the minimum for serialization).
        serialized = dict(params)
        assert serialized["model"] == "rgb"
        assert serialized["r"] == 200
        assert serialized["g"] == 100
        assert serialized["b"] == 50

    def test_hsv_params_round_trip_via_dict(self):
        params: HsvColorParams = {"model": "hsv", "h": 60, "s": 80, "v": 70}
        serialized = dict(params)
        assert serialized["model"] == "hsv"
        assert serialized["h"] == 60

    def test_circle_params_round_trip_via_dict(self):
        params: CircleShapeParams = {"type": "circle", "radius": 2.5}
        serialized = dict(params)
        assert serialized["type"] == "circle"
        assert serialized["radius"] == 2.5

    def test_rectangle_params_round_trip_via_dict(self):
        params: RectangleShapeParams = {
            "type": "rectangle",
            "width": 4.0,
            "height": 8.0,
        }
        serialized = dict(params)
        assert serialized["type"] == "rectangle"
        assert serialized["width"] == 4.0
        assert serialized["height"] == 8.0

    def test_response_to_dict_preserves_discriminator(self):
        """
        Round-trip: deserialize JSON into StripeObject, convert back to dict.
        The discriminator must survive both directions.
        """
        original = {"model": "rgb", "r": 255, "g": 0, "b": 0}
        obj = StripeObject.construct_from(original, key="sk_test_xxx")
        result = obj.to_dict()
        assert result["model"] == "rgb"
        assert result == original

    def test_inline_response_to_dict_preserves_discriminator(self):
        original = {"type": "rectangle", "width": 3.0, "height": 6.0}
        obj = StripeObject.construct_from(original, key="sk_test_xxx")
        result = obj.to_dict()
        assert result["type"] == "rectangle"
        assert result == original
