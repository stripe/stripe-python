from __future__ import absolute_import, division, print_function

import pytest

import stripe


TEST_RESOURCE_ID = "aliacc_123"


class TestAlipayAccount(object):
    def construct_resource(self):
        alipay_dict = {
            "id": TEST_RESOURCE_ID,
            "object": "alipay_account",
            "metadata": {},
            "customer": "cus_123",
        }
        return stripe.AlipayAccount.construct_from(alipay_dict, stripe.api_key)

    def test_has_instance_url(self, request_mock):
        resource = self.construct_resource()
        assert (
            resource.instance_url()
            == "/v1/customers/cus_123/sources/%s" % TEST_RESOURCE_ID
        )

    def test_is_modifiable(self, request_mock):
        stripe.AlipayAccount.modify(
            "cus_123", TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/v1/customers/cus_123/sources/%s" % TEST_RESOURCE_ID
        )

    def test_is_not_retrievable(self, request_mock):
        with pytest.raises(NotImplementedError):
            stripe.AlipayAccount.retrieve(TEST_RESOURCE_ID)

    # Below, we don't use stripe-mock as it always returns a Bank Account
    # object when you hit /v1/customers/%s/sources/%s

    def test_is_saveable(self, request_mock):
        resource = self.construct_resource()
        resource.metadata["key"] = "value"
        resource.save()
        request_mock.assert_requested(
            "post", "/v1/customers/cus_123/sources/%s" % TEST_RESOURCE_ID
        )

    def test_is_deletable(self, request_mock):
        resource = self.construct_resource()
        resource.delete()
        request_mock.assert_requested(
            "delete", "/v1/customers/cus_123/sources/%s" % TEST_RESOURCE_ID
        )
