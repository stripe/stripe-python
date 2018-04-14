from __future__ import absolute_import, division, print_function

import stripe
from tests.helper import StripeTestCase


TEST_RESOURCE_ID = 'fr_123'
TEST_APPFEE_ID = 'fee_123'


class ApplicationFeeRefundTest(StripeTestCase):
    def test_is_saveable(self):
        appfee = stripe.ApplicationFee.retrieve(TEST_APPFEE_ID)
        resource = appfee.refunds.retrieve(TEST_RESOURCE_ID)
        resource.metadata['key'] = 'value'
        resource.save()
        self.assert_requested(
            'post',
            '/v1/application_fees/%s/refunds/%s' % (resource.fee,
                                                    resource.id)
        )

    def test_is_modifiable(self):
        resource = stripe.ApplicationFeeRefund.modify(
            TEST_APPFEE_ID,
            TEST_RESOURCE_ID,
            metadata={'key': 'value'}
        )
        self.assert_requested(
            'post',
            '/v1/application_fees/%s/refunds/%s' % (TEST_APPFEE_ID,
                                                    TEST_RESOURCE_ID)
        )
        self.assertIsInstance(resource, stripe.ApplicationFeeRefund)

    def test_is_not_retrievable(self):
        with self.assertRaises(NotImplementedError):
            stripe.ApplicationFeeRefund.retrieve(TEST_RESOURCE_ID)
