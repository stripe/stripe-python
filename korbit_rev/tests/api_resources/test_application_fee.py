import stripe


TEST_RESOURCE_ID = "fee_123"
TEST_FEEREFUND_ID = "fr_123"


class TestApplicationFee(object):
    def test_is_listable(self, http_client_mock):
        resources = stripe.ApplicationFee.list()
        http_client_mock.assert_requested("get", path="/v1/application_fees")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.ApplicationFee)


class TestApplicationFeeRefunds(object):
    def test_is_listable(self, http_client_mock):
        resources = stripe.ApplicationFee.list_refunds(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/application_fees/%s/refunds" % TEST_RESOURCE_ID
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.ApplicationFeeRefund)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.ApplicationFee.retrieve_refund(
            TEST_RESOURCE_ID, TEST_FEEREFUND_ID
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/application_fees/%s/refunds/%s"
            % (TEST_RESOURCE_ID, TEST_FEEREFUND_ID),
        )
        assert isinstance(resource, stripe.ApplicationFeeRefund)

    def test_is_creatable(self, http_client_mock):
        resource = stripe.ApplicationFee.create_refund(
            TEST_RESOURCE_ID, amount=100
        )
        http_client_mock.assert_requested(
            "post", path="/v1/application_fees/%s/refunds" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.ApplicationFeeRefund)

    def test_is_modifiable(self, http_client_mock):
        resource = stripe.ApplicationFee.modify_refund(
            TEST_RESOURCE_ID, TEST_FEEREFUND_ID, metadata={"foo": "bar"}
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/application_fees/%s/refunds/%s"
            % (TEST_RESOURCE_ID, TEST_FEEREFUND_ID),
        )
        assert isinstance(resource, stripe.ApplicationFeeRefund)
