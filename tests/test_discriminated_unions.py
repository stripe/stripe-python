"""
Tests for discriminated union runtime behavior.

A discriminated union field arrives as a plain JSON object, and the SDK has to
pick the variant class out of the discriminator carried inside that object. The
fixtures below mirror what codegen emits for the fake spec's `test.llama`
resource, including the part that makes dispatch *observable*: the two color
variants declare different `_field_encodings`, so identical wire bytes hydrate
differently based only on the discriminator. Without dispatch the value becomes
a bare StripeObject carrying no encodings, and every coercion assertion here
fails.

Static type narrowing (Literal discriminators, Union resolution) is checked by
pyright, not here.
"""

from decimal import Decimal
from typing import Any, Dict, Optional, Union

from typing_extensions import Literal

from stripe._encode import _coerce_v2_params
from stripe._stripe_object import StripeObject


# ---------------------------------------------------------------------------
# Fixtures — shaped the way codegen emits them
# ---------------------------------------------------------------------------


class RgbColor(StripeObject):
    luminance: Optional[int]
    model: Literal["rgb"]
    _field_encodings = {"luminance": "int64_string"}


class HsvColor(StripeObject):
    model: Literal["hsv"]
    saturation_precision: Optional[Decimal]
    _field_encodings = {"saturation_precision": "decimal_string"}


class HslColor(StripeObject):
    model: Literal["hsl"]


class MagicLlama(StripeObject):
    mana_cost: Optional[int]
    _field_encodings = {"mana_cost": "int64_string"}


class Llama(StripeObject):
    """
    Carries both union shapes the generator produces: a standalone `color`
    union whose variants are separate classes, and an inline `magic_llama`
    union whose discriminator lives on the parent and whose payload is a
    plain inner class.
    """

    color: Union[RgbColor, HsvColor, HslColor]
    magic_llama: Optional[MagicLlama]
    name: str
    type: Literal["earth_llama", "magic_llama"]
    _inner_class_types = {"magic_llama": MagicLlama}
    _inner_class_union_variant_types = {
        "color": (
            "model",
            {"rgb": RgbColor, "hsv": HsvColor, "hsl": HslColor},
        ),
    }


def _llama(**values: Any) -> Llama:
    return Llama.construct_from(
        {"name": "kuzco", **values}, key="sk_test", api_mode="V2"
    )


# Copied from the generated `LlamaService.create` call site. The generator
# flattens every variant's fields into one map keyed by field name, so this
# single schema covers both `luminance` (rgb) and `saturation_precision` (hsv).
_COLOR_REQUEST_SCHEMA: Dict[str, Any] = {
    "color": {
        "luminance": "int64_string",
        "saturation_precision": "decimal_string",
    },
}


# ---------------------------------------------------------------------------
# Response side — variant dispatch
# ---------------------------------------------------------------------------


class TestVariantDispatch:
    """The discriminator selects the variant class, not the base."""

    def test_dispatches_to_the_rgb_variant(self):
        llama = _llama(color={"model": "rgb", "luminance": "1500"})
        assert isinstance(llama.color, RgbColor)

    def test_dispatches_to_the_hsv_variant(self):
        llama = _llama(color={"model": "hsv", "saturation_precision": "0.125"})
        assert isinstance(llama.color, HsvColor)

    def test_dispatches_to_a_variant_with_no_payload_fields(self):
        llama = _llama(color={"model": "hsl"})
        assert isinstance(llama.color, HslColor)
        assert llama.color.model == "hsl"

    def test_the_variants_int64_encoding_applies(self):
        llama = _llama(color={"model": "rgb", "luminance": "1500"})
        assert llama.color.luminance == 1500
        assert isinstance(llama.color.luminance, int)

    def test_the_variants_decimal_encoding_applies(self):
        llama = _llama(color={"model": "hsv", "saturation_precision": "0.125"})
        assert llama.color.saturation_precision == Decimal("0.125")
        assert isinstance(llama.color.saturation_precision, Decimal)

    def test_only_the_discriminator_decides_which_field_coerces(self):
        """
        The sharpest statement of what dispatch buys: two payloads differing
        in nothing but the discriminator coerce different fields, because each
        variant class knows only its own encodings.
        """
        payload = {"luminance": "1500", "saturation_precision": "0.125"}

        as_rgb = _llama(color={"model": "rgb", **payload}).color
        assert as_rgb.luminance == 1500
        assert as_rgb.saturation_precision == "0.125"

        as_hsv = _llama(color={"model": "hsv", **payload}).color
        assert as_hsv.luminance == "1500"
        assert as_hsv.saturation_precision == Decimal("0.125")

    def test_the_discriminator_itself_is_readable_on_the_variant(self):
        llama = _llama(color={"model": "rgb", "luminance": "1"})
        assert llama.color.model == "rgb"
        assert llama.color["model"] == "rgb"


# ---------------------------------------------------------------------------
# Response side — fallback
# ---------------------------------------------------------------------------


class TestUnknownVariantFallback:
    """
    A variant the API adds after this release must still deserialize. The
    fallback is a plain StripeObject: readable, but with no encodings, since
    the SDK has no idea what the new variant's fields mean.
    """

    def test_an_unknown_discriminator_falls_back(self):
        llama = _llama(color={"model": "cmyk", "cyan": "1"})
        assert type(llama.color) is StripeObject
        assert llama.color.model == "cmyk"
        assert llama.color.cyan == "1"

    def test_an_absent_discriminator_falls_back(self):
        llama = _llama(color={"luminance": "1500"})
        assert type(llama.color) is StripeObject
        assert llama.color.luminance == "1500"

    def test_a_non_string_discriminator_falls_back(self):
        llama = _llama(color={"model": 7})
        assert type(llama.color) is StripeObject

    def test_a_null_union_value_stays_none(self):
        assert _llama(color=None).color is None

    def test_a_non_object_union_value_passes_through(self):
        """
        Not a shape the API produces, but the lookup must not raise on it —
        the union field is read before anything has validated its type.
        """
        assert _llama(color="rgb").color == "rgb"


# ---------------------------------------------------------------------------
# Response side — inline unions are unaffected
# ---------------------------------------------------------------------------


class TestInlineUnionsUseInnerClassTypes:
    """
    Inline union variants are namespaced by field name, so they need no
    discriminator lookup and keep going through `_inner_class_types`. These
    pin that the union lookup did not displace it.
    """

    def test_the_inline_variant_gets_its_inner_class(self):
        llama = _llama(type="magic_llama", magic_llama={"mana_cost": "42"})
        assert isinstance(llama.magic_llama, MagicLlama)

    def test_the_inline_variants_encoding_applies(self):
        llama = _llama(type="magic_llama", magic_llama={"mana_cost": "42"})
        assert llama.magic_llama.mana_cost == 42
        assert isinstance(llama.magic_llama.mana_cost, int)

    def test_the_non_selected_variant_is_not_fabricated(self):
        llama = _llama(type="earth_llama")
        assert llama.type == "earth_llama"
        # `__getattr__` raises for a key absent from `_data`, so this is a
        # real statement that nothing was materialized for the other variant.
        assert not hasattr(llama, "magic_llama")


# ---------------------------------------------------------------------------
# Response side — serialization back out
# ---------------------------------------------------------------------------


class TestUnionValueSerialization:
    def test_to_dict_recurses_into_the_variant(self):
        llama = _llama(color={"model": "rgb", "luminance": "1500"})
        assert llama.to_dict()["color"] == {
            "model": "rgb",
            "luminance": 1500,
        }

    def test_to_dict_for_json_restringifies_the_decimal(self):
        """
        The variant hydrates `saturation_precision` to a Decimal, which is not
        JSON-serializable, so `for_json` has to put the string back.
        """
        llama = _llama(color={"model": "hsv", "saturation_precision": "0.125"})

        plain = llama.to_dict()["color"]["saturation_precision"]
        assert isinstance(plain, Decimal)

        for_json = llama.to_dict(for_json=True)["color"]
        assert for_json["saturation_precision"] == "0.125"
        assert isinstance(for_json["saturation_precision"], str)

    def test_to_dict_preserves_an_unknown_variant_verbatim(self):
        llama = _llama(color={"model": "cmyk", "cyan": "1"})
        assert llama.to_dict()["color"] == {"model": "cmyk", "cyan": "1"}


# ---------------------------------------------------------------------------
# Request side
# ---------------------------------------------------------------------------


class TestUnionRequestCoercion:
    """
    Outbound coercion runs off the method-level schema, which is keyed by
    field name only — there is no discriminator in it.
    """

    def test_the_rgb_variants_int64_field_is_stringified(self):
        result = _coerce_v2_params(
            {"color": {"model": "rgb", "luminance": 1500}},
            _COLOR_REQUEST_SCHEMA,
        )
        assert result == {"color": {"model": "rgb", "luminance": "1500"}}

    def test_the_hsv_variants_decimal_field_is_stringified(self):
        result = _coerce_v2_params(
            {
                "color": {
                    "model": "hsv",
                    "saturation_precision": Decimal("0.125"),
                }
            },
            _COLOR_REQUEST_SCHEMA,
        )
        assert result == {
            "color": {"model": "hsv", "saturation_precision": "0.125"}
        }

    def test_a_payload_free_variant_passes_through_untouched(self):
        result = _coerce_v2_params(
            {"color": {"model": "hsl"}}, _COLOR_REQUEST_SCHEMA
        )
        assert result == {"color": {"model": "hsl"}}

    def test_coercion_is_by_field_name_not_by_variant(self):
        """
        Pins the generator's flattening decision: every variant's fields land
        in one map, so a field is coerced whenever it appears, whatever the
        discriminator says. Safe while variants do not share a field name with
        conflicting encodings.
        """
        result = _coerce_v2_params(
            {
                "color": {
                    "model": "rgb",
                    "saturation_precision": Decimal("0.5"),
                }
            },
            _COLOR_REQUEST_SCHEMA,
        )
        assert result == {
            "color": {"model": "rgb", "saturation_precision": "0.5"}
        }

    def test_unknown_variant_fields_pass_through(self):
        result = _coerce_v2_params(
            {"color": {"model": "cmyk", "cyan": 1}},
            _COLOR_REQUEST_SCHEMA,
        )
        assert result == {"color": {"model": "cmyk", "cyan": 1}}

    def test_a_null_union_is_not_coerced(self):
        result = _coerce_v2_params({"color": None}, _COLOR_REQUEST_SCHEMA)
        assert result == {"color": None}
