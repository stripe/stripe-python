from __future__ import absolute_import, division, print_function

import stripe


TEST_RESOURCE_ID = "tr_123"
TEST_REVERSAL_ID = "trr_123"


class TestTransfer(object):
    def test_is_listable(self, request_mock):
        resources = stripe.Transfer.list()
        request_mock.assert_requested("get", "/v1/transfers")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Transfer)

    def test_is_retrievable(self, request_mock):
        resource = stripe.Transfer.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/transfers/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Transfer)

    def test_is_creatable(self, request_mock):
        resource = stripe.Transfer.create(
            amount=100, currency="usd", destination="acct_123"
        )
        request_mock.assert_requested("post", "/v1/transfers")
        assert isinstance(resource, stripe.Transfer)

    def test_is_saveable(self, request_mock):
        resource = stripe.Transfer.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        request_mock.assert_requested(
            "post", "/v1/transfers/%s" % TEST_RESOURCE_ID
        )

    def test_is_modifiable(self, request_mock):
        resource = stripe.Transfer.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        request_mock.assert_requested(
            "post", "/v1/transfers/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Transfer)


class TestTransferReversals:
    def test_is_listable(self, request_mock):
        resources = stripe.Transfer.list_reversals(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            "get", "/v1/transfers/%s/reversals" % TEST_RESOURCE_ID
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Reversal)

    def test_is_retrievable(self, request_mock):
        resource = stripe.Transfer.retrieve_reversal(
            TEST_RESOURCE_ID, TEST_REVERSAL_ID
        )
        request_mock.assert_requested(
            "get",
            "/v1/transfers/%s/reversals/%s"
            % (TEST_RESOURCE_ID, TEST_REVERSAL_ID),
        )
        assert isinstance(resource, stripe.Reversal)

    def test_is_creatable(self, request_mock):
        resource = stripe.Transfer.create_reversal(
            TEST_RESOURCE_ID, amount=100
        )
        request_mock.assert_requested(
            "post", "/v1/transfers/%s/reversals" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Reversal)

    def test_is_modifiable(self, request_mock):
        resource = stripe.Transfer.modify_reversal(
            TEST_RESOURCE_ID, TEST_REVERSAL_ID, metadata={"foo": "bar"}
        )
        request_mock.assert_requested(
            "post",
            "/v1/transfers/%s/reversals/%s"
            % (TEST_RESOURCE_ID, TEST_REVERSAL_ID),
        )
        assert isinstance(resource, stripe.Reversal)
