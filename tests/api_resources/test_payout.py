from __future__ import absolute_import, division, print_function

import stripe
from tests.helper import StripeTestCase


TEST_RESOURCE_ID = 'po_123'


class PayoutTest(StripeTestCase):
    def test_is_listable(self):
        resources = stripe.Payout.list()
        self.assert_requested(
            'get',
            '/v1/payouts'
        )
        self.assertIsInstance(resources.data, list)
        self.assertIsInstance(resources.data[0], stripe.Payout)

    def test_is_retrievable(self):
        resource = stripe.Payout.retrieve(TEST_RESOURCE_ID)
        self.assert_requested(
            'get',
            '/v1/payouts/%s' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.Payout)

    def test_is_creatable(self):
        resource = stripe.Payout.create(
            amount=100,
            currency='usd'
        )
        self.assert_requested(
            'post',
            '/v1/payouts'
        )
        self.assertIsInstance(resource, stripe.Payout)

    def test_is_saveable(self):
        resource = stripe.Payout.retrieve(TEST_RESOURCE_ID)
        resource.metadata['key'] = 'value'
        resource.save()
        self.assert_requested(
            'post',
            '/v1/payouts/%s' % resource.id
        )

    def test_is_modifiable(self):
        resource = stripe.Payout.modify(
            TEST_RESOURCE_ID,
            metadata={'key': 'value'}
        )
        self.assert_requested(
            'post',
            '/v1/payouts/%s' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.Payout)

    def test_can_cancel(self):
        payout = stripe.Payout.retrieve(TEST_RESOURCE_ID)
        resource = payout.cancel()
        self.assert_requested(
            'post',
            '/v1/payouts/%s/cancel' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.Payout)
