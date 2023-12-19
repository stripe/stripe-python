import pytest

import stripe


TEST_RESOURCE_ID = "acap_123"


class TestCapability(object):
    def construct_resource(self):
        capability_dict = {
            "id": TEST_RESOURCE_ID,
            "object": "capability",
            "account": "acct_123",
        }
        return stripe.Capability.construct_from(
            capability_dict, stripe.api_key
        )

    def test_has_instance_url(self):
        resource = self.construct_resource()
        assert (
            resource.instance_url()
            == "/v1/accounts/acct_123/capabilities/%s" % TEST_RESOURCE_ID
        )

    def test_is_not_modifiable(self):
        with pytest.raises(NotImplementedError):
            stripe.Capability.modify(TEST_RESOURCE_ID, requested=True)

    def test_is_not_retrievable(self):
        with pytest.raises(NotImplementedError):
            stripe.Capability.retrieve(TEST_RESOURCE_ID)

    def test_is_saveable(self, http_client_mock):
        resource = self.construct_resource()
        resource.requested = True
        resource.save()
        http_client_mock.assert_requested(
            "post",
            path="/v1/accounts/acct_123/capabilities/%s" % TEST_RESOURCE_ID,
            post_data="requested=True",
        )
