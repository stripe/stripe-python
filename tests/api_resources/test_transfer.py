import stripe


TEST_RESOURCE_ID = "tr_123"
TEST_REVERSAL_ID = "trr_123"


class TestTransfer(object):
    def test_is_listable(self, http_client_mock):
        resources = stripe.Transfer.list()
        http_client_mock.assert_requested("get", path="/v1/transfers")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Transfer)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.Transfer.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/transfers/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Transfer)

    def test_is_creatable(self, http_client_mock):
        resource = stripe.Transfer.create(
            amount=100, currency="usd", destination="acct_123"
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/transfers",
            post_data="amount=100&currency=usd&destination=acct_123",
        )
        assert isinstance(resource, stripe.Transfer)

    def test_is_saveable(self, http_client_mock):
        resource = stripe.Transfer.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        http_client_mock.assert_requested(
            "post",
            path="/v1/transfers/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )

    def test_is_modifiable(self, http_client_mock):
        resource = stripe.Transfer.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/transfers/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )
        assert isinstance(resource, stripe.Transfer)


class TestTransferReversals:
    def test_is_listable(self, http_client_mock):
        resources = stripe.Transfer.list_reversals(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/transfers/%s/reversals" % TEST_RESOURCE_ID
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Reversal)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.Transfer.retrieve_reversal(
            TEST_RESOURCE_ID, TEST_REVERSAL_ID
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/transfers/%s/reversals/%s"
            % (TEST_RESOURCE_ID, TEST_REVERSAL_ID),
        )
        assert isinstance(resource, stripe.Reversal)

    def test_is_creatable(self, http_client_mock):
        resource = stripe.Transfer.create_reversal(
            TEST_RESOURCE_ID, amount=100
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/transfers/%s/reversals" % TEST_RESOURCE_ID,
            post_data="amount=100",
        )
        assert isinstance(resource, stripe.Reversal)

    def test_is_modifiable(self, http_client_mock):
        resource = stripe.Transfer.modify_reversal(
            TEST_RESOURCE_ID, TEST_REVERSAL_ID, metadata={"foo": "bar"}
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/transfers/%s/reversals/%s"
            % (TEST_RESOURCE_ID, TEST_REVERSAL_ID),
            post_data="metadata[foo]=bar",
        )
        assert isinstance(resource, stripe.Reversal)
