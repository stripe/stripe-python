from __future__ import absolute_import, division, print_function

import stripe
from tests.helper import StripeTestCase


TEST_RESOURCE_ID = 'ch_123'


class ChargeTest(StripeTestCase):
    def test_is_listable(self):
        resources = stripe.Charge.list()
        self.assert_requested(
            'get',
            '/v1/charges'
        )
        self.assertIsInstance(resources.data, list)
        self.assertIsInstance(resources.data[0], stripe.Charge)

    def test_is_retrievable(self):
        resource = stripe.Charge.retrieve(TEST_RESOURCE_ID)
        self.assert_requested(
            'get',
            '/v1/charges/%s' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.Charge)

    def test_is_creatable(self):
        resource = stripe.Charge.create(
            amount=100,
            currency='usd',
            source='tok_123'
        )
        self.assert_requested(
            'post',
            '/v1/charges'
        )
        self.assertIsInstance(resource, stripe.Charge)

    def test_is_saveable(self):
        resource = stripe.Charge.retrieve(TEST_RESOURCE_ID)
        resource.metadata['key'] = 'value'
        resource.save()
        self.assert_requested(
            'post',
            '/v1/charges/%s' % resource.id
        )

    def test_is_modifiable(self):
        resource = stripe.Charge.modify(
            TEST_RESOURCE_ID,
            metadata={'key': 'value'}
        )
        self.assert_requested(
            'post',
            '/v1/charges/%s' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.Charge)


class ChargeMethodsTest(StripeTestCase):
    def test_can_refund(self):
        charge = stripe.Charge.retrieve(TEST_RESOURCE_ID)
        resource = charge.refund()
        self.assert_requested(
            'post',
            '/v1/charges/%s/refund' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.Charge)

    def test_can_capture(self):
        charge = stripe.Charge.retrieve(TEST_RESOURCE_ID)
        resource = charge.capture()
        self.assert_requested(
            'post',
            '/v1/charges/%s/capture' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.Charge)

    def test_can_update_dispute(self):
        charge = stripe.Charge.retrieve(TEST_RESOURCE_ID)
        resource = charge.update_dispute()
        self.assert_requested(
            'post',
            '/v1/charges/%s/dispute' % charge.id
        )
        self.assertIsInstance(resource, stripe.Dispute)

    def test_can_close_dispute(self):
        charge = stripe.Charge.retrieve(TEST_RESOURCE_ID)
        resource = charge.close_dispute()
        self.assert_requested(
            'post',
            '/v1/charges/%s/dispute/close' % charge.id
        )
        self.assertIsInstance(resource, stripe.Dispute)

    def test_can_mark_as_fraudulent(self):
        charge = stripe.Charge.retrieve(TEST_RESOURCE_ID)
        resource = charge.mark_as_fraudulent()
        self.assert_requested(
            'post',
            '/v1/charges/%s' % charge.id,
            {
                'fraud_details': {'user_report': 'fraudulent'}
            }
        )
        self.assertIsInstance(resource, stripe.Charge)

    def test_can_mark_as_safe(self):
        charge = stripe.Charge.retrieve(TEST_RESOURCE_ID)
        resource = charge.mark_as_safe()
        self.assert_requested(
            'post',
            '/v1/charges/%s' % charge.id,
            {
                'fraud_details': {'user_report': 'safe'}
            }
        )
        self.assertIsInstance(resource, stripe.Charge)
