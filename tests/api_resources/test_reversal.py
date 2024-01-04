import pytest

import stripe


TEST_RESOURCE_ID = "trr_123"


class TestReversal(object):
    def construct_resource(self):
        reversal_dict = {
            "id": TEST_RESOURCE_ID,
            "object": "reversal",
            "metadata": {},
            "transfer": "tr_123",
        }
        return stripe.Reversal.construct_from(reversal_dict, stripe.api_key)

    def test_has_instance_url(self):
        resource = self.construct_resource()
        assert (
            resource.instance_url()
            == "/v1/transfers/tr_123/reversals/%s" % TEST_RESOURCE_ID
        )

    def test_is_not_modifiable(self):
        with pytest.raises(NotImplementedError):
            stripe.Reversal.modify(TEST_RESOURCE_ID, metadata={"key": "value"})

    def test_is_not_retrievable(self):
        with pytest.raises(NotImplementedError):
            stripe.Reversal.retrieve(TEST_RESOURCE_ID)

    def test_is_saveable(self, http_client_mock):
        resource = self.construct_resource()
        resource.metadata["key"] = "value"
        resource.save()
        http_client_mock.assert_requested(
            "post",
            path="/v1/transfers/tr_123/reversals/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )
