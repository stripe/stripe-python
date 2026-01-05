import warnings

from stripe._stripe_object import StripeObject
from stripe._encode import _api_encode


class TestApiEncode:
    def test_encode_stripe_object_without_id_no_deprecation_warning(self):
        """
        Test that encoding a StripeObject without an id (like metadata)
        does not trigger a deprecation warning.
        Regression test for issue #1651.
        """
        metadata = StripeObject()
        metadata["key1"] = "value1"
        metadata["key2"] = "value2"

        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            result = list(_api_encode({"metadata": metadata}))

            # Check no deprecation warnings were raised
            deprecation_warnings = [
                warning
                for warning in w
                if issubclass(warning.category, DeprecationWarning)
            ]
            assert len(deprecation_warnings) == 0, (
                f"Expected no deprecation warnings, but got {len(deprecation_warnings)}"
            )

        # Verify the metadata was encoded correctly as nested dict
        assert result == [
            ("metadata[key1]", "value1"),
            ("metadata[key2]", "value2"),
        ]

    def test_encode_stripe_object_with_id_extracts_id(self):
        """
        Test that encoding a StripeObject with an id (like a customer reference)
        correctly extracts just the id value.
        """
        customer = StripeObject()
        customer["id"] = "cus_123"
        customer["name"] = "Test Customer"

        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter("always")
            result = list(_api_encode({"customer": customer}))

            # Check no deprecation warnings were raised
            deprecation_warnings = [
                warning
                for warning in w
                if issubclass(warning.category, DeprecationWarning)
            ]
            assert len(deprecation_warnings) == 0, (
                f"Expected no deprecation warnings, but got {len(deprecation_warnings)}"
            )

        # Should encode to just the ID
        assert result == [("customer", "cus_123")]

    def test_encode_regular_dict(self):
        """Test that regular dicts are encoded as nested dicts."""
        regular_dict = {"key1": "value1", "key2": "value2"}
        result = list(_api_encode({"data": regular_dict}))

        assert result == [
            ("data[key1]", "value1"),
            ("data[key2]", "value2"),
        ]

    def test_encode_none_value_skipped(self):
        """Test that None values are skipped during encoding."""
        result = list(_api_encode({"field": None}))
        assert result == []

    def test_encode_string_value(self):
        """Test that string values are encoded directly."""
        result = list(_api_encode({"name": "John Doe"}))
        assert result == [("name", "John Doe")]

    def test_encode_boolean_value(self):
        """Test that boolean values are encoded as lowercase strings."""
        result = list(_api_encode({"active": True, "deleted": False}))
        assert result == [("active", "true"), ("deleted", "false")]

    def test_encode_list_value(self):
        """Test that list values are encoded with indexed keys."""
        result = list(_api_encode({"items": ["item1", "item2", "item3"]}))
        assert result == [
            ("items[0]", "item1"),
            ("items[1]", "item2"),
            ("items[2]", "item3"),
        ]
