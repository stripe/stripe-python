from __future__ import absolute_import, division, print_function

import stripe
from tests.helper import StripeTestCase


TEST_RESOURCE_ID = 'fee_123'
TEST_FEEREFUND_ID = 'fr_123'


class ApplicationFeeTest(StripeTestCase):
    def test_is_listable(self):
        resources = stripe.ApplicationFee.list()
        self.assert_requested(
            'get',
            '/v1/application_fees'
        )
        self.assertIsInstance(resources.data, list)
        self.assertIsInstance(resources.data[0], stripe.ApplicationFee)


class ApplicationFeeRefundsTests(StripeTestCase):
    def test_can_call_refund(self):
        appfee = stripe.ApplicationFee.retrieve(TEST_RESOURCE_ID)
        resource = appfee.refund()
        self.assert_requested(
            'post',
            '/v1/application_fees/%s/refund' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.ApplicationFee)
        self.assertTrue(resource is appfee)

    def test_is_listable(self):
        resources = stripe.ApplicationFee.list_refunds(TEST_RESOURCE_ID)
        self.assert_requested(
            'get',
            '/v1/application_fees/%s/refunds' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resources.data, list)
        self.assertIsInstance(resources.data[0], stripe.ApplicationFeeRefund)

    def test_is_retrievable(self):
        resource = stripe.ApplicationFee.retrieve_refund(
            TEST_RESOURCE_ID,
            TEST_FEEREFUND_ID
        )
        self.assert_requested(
            'get',
            '/v1/application_fees/%s/refunds/%s' % (TEST_RESOURCE_ID,
                                                    TEST_FEEREFUND_ID)
        )
        self.assertIsInstance(resource, stripe.ApplicationFeeRefund)

    def test_is_creatable(self):
        resource = stripe.ApplicationFee.create_refund(
            TEST_RESOURCE_ID,
            amount=100
        )
        self.assert_requested(
            'post',
            '/v1/application_fees/%s/refunds' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.ApplicationFeeRefund)

    def test_is_modifiable(self):
        resource = stripe.ApplicationFee.modify_refund(
            TEST_RESOURCE_ID,
            TEST_FEEREFUND_ID,
            metadata={'foo': 'bar'}
        )
        self.assert_requested(
            'post',
            '/v1/application_fees/%s/refunds/%s' % (TEST_RESOURCE_ID,
                                                    TEST_FEEREFUND_ID)
        )
        self.assertIsInstance(resource, stripe.ApplicationFeeRefund)
