import pytest

import stripe


TEST_RESOURCE_ID = "fr_123"
TEST_APPFEE_ID = "fee_123"


class TestApplicationFeeRefund(object):
    def test_is_saveable(self, http_client_mock):
        appfee = stripe.ApplicationFee.retrieve(TEST_APPFEE_ID)
        resource = appfee.refunds.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        http_client_mock.assert_requested(
            "post",
            path="/v1/application_fees/%s/refunds/%s"
            % (TEST_APPFEE_ID, TEST_RESOURCE_ID),
        )

    def test_is_modifiable(self, http_client_mock):
        resource = stripe.ApplicationFeeRefund.modify(
            TEST_APPFEE_ID, TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/application_fees/%s/refunds/%s"
            % (TEST_APPFEE_ID, TEST_RESOURCE_ID),
        )
        assert isinstance(resource, stripe.ApplicationFeeRefund)

    def test_is_not_retrievable(self):
        with pytest.raises(NotImplementedError):
            stripe.ApplicationFeeRefund.retrieve(TEST_RESOURCE_ID)
