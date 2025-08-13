import pytest

import stripe


class TestEphemeralKey(object):
    def test_is_creatable(self, http_client_mock):
        resource = stripe.EphemeralKey.create(
            customer="cus_123", stripe_version="2017-05-25"
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/ephemeral_keys",
            stripe_version="2017-05-25",
            post_data="customer=cus_123",
        )
        assert isinstance(resource, stripe.EphemeralKey)

    def test_is_not_creatable_without_an_explicit_api_version(self):
        with pytest.raises(
            ValueError, match="stripe_version must be specified"
        ):
            stripe.EphemeralKey.create(customer="cus_123")

    def test_is_deletable(self, http_client_mock):
        resource = stripe.EphemeralKey.create(
            customer="cus_123", stripe_version="2017-05-25"
        )
        resource.delete()
        http_client_mock.assert_requested(
            "delete", path="/v1/ephemeral_keys/%s" % resource.id
        )
        assert isinstance(resource, stripe.EphemeralKey)

    def test_can_delete(self, http_client_mock):
        resource = stripe.EphemeralKey.delete("ephkey_123")
        http_client_mock.assert_requested(
            "delete", path="/v1/ephemeral_keys/ephkey_123"
        )
        assert isinstance(resource, stripe.EphemeralKey)
