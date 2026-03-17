from __future__ import absolute_import, division, print_function

import json
import uuid

from stripe import StripeClient
from stripe._api_version import _ApiVersion


class TestCustomerServiceSerializeBatch(object):
    def setup_method(self):
        self.client = StripeClient("sk_test_123")

    def test_serialize_batch_update_basic_structure(self):
        params = {"description": "test customer"}
        result = json.loads(
            self.client.customers.serialize_batch_update(
                "cus_123", params=params
            )
        )

        # id is a valid UUID
        uuid.UUID(result["id"])

        assert result["path_params"] == {"customer": "cus_123"}
        assert result["params"] == {"description": "test customer"}
        assert result["stripe_version"] == _ApiVersion.CURRENT
        assert "context" not in result

    def test_serialize_batch_update_unique_ids(self):
        params = {"description": "test"}
        r1 = json.loads(
            self.client.customers.serialize_batch_update(
                "cus_123", params=params
            )
        )
        r2 = json.loads(
            self.client.customers.serialize_batch_update(
                "cus_123", params=params
            )
        )
        assert r1["id"] != r2["id"]

    def test_serialize_batch_update_with_stripe_context(self):
        params = {"description": "test"}
        options = {"stripe_context": "acct_123"}
        result = json.loads(
            self.client.customers.serialize_batch_update(
                "cus_123", params=params, options=options
            )
        )
        assert result["context"] == "acct_123"

    def test_serialize_batch_update_null_params(self):
        result = json.loads(
            self.client.customers.serialize_batch_update(
                "cus_123", params=None
            )
        )
        assert result["params"] is None
        uuid.UUID(result["id"])
        assert result["path_params"] == {"customer": "cus_123"}
        assert result["stripe_version"] == _ApiVersion.CURRENT

    def test_serialize_batch_update_with_metadata(self):
        params = {"metadata": {"key1": "value1", "key2": "value2"}}
        result = json.loads(
            self.client.customers.serialize_batch_update(
                "cus_123", params=params
            )
        )
        assert result["params"] == {
            "metadata": {"key1": "value1", "key2": "value2"}
        }

    def test_serialize_batch_update_only_set_keys_serialized(self):
        params = {"description": "test"}
        result = json.loads(
            self.client.customers.serialize_batch_update(
                "cus_123", params=params
            )
        )
        assert list(result["params"].keys()) == ["description"]

    def test_serialize_batch_update_custom_stripe_version(self):
        params = {"description": "test"}
        options = {"stripe_version": "2025-01-01"}
        result = json.loads(
            self.client.customers.serialize_batch_update(
                "cus_123", params=params, options=options
            )
        )
        assert result["stripe_version"] == "2025-01-01"

    def test_serialize_batch_update_null_options(self):
        params = {"description": "test"}
        result = json.loads(
            self.client.customers.serialize_batch_update(
                "cus_123", params=params
            )
        )
        assert result["stripe_version"] == _ApiVersion.CURRENT
        assert "context" not in result
