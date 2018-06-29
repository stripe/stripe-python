from __future__ import absolute_import, division, print_function

import stripe
from tests.helper import StripeTestCase


TEST_RESOURCE_ID = 'pi_123'


class PaymentIntentTest(StripeTestCase):
    FIXTURE = {
        'id': TEST_RESOURCE_ID,
        'object': 'payment_intent',
        'metadata': {},
    }

    def test_is_listable(self):
        self.stub_request(
            'get',
            '/v1/payment_intents',
            {
                'object': 'list',
                'data': [self.FIXTURE],
            }
        )

        resources = stripe.PaymentIntent.list()
        self.assert_requested(
            'get',
            '/v1/payment_intents'
        )
        self.assertIsInstance(resources.data, list)
        self.assertIsInstance(resources.data[0], stripe.PaymentIntent)

    def test_is_retrievable(self):
        self.stub_request(
            'get',
            '/v1/payment_intents/%s' % TEST_RESOURCE_ID,
            self.FIXTURE
        )

        resource = stripe.PaymentIntent.retrieve(TEST_RESOURCE_ID)
        self.assert_requested(
            'get',
            '/v1/payment_intents/%s' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.PaymentIntent)

    def test_is_creatable(self):
        self.stub_request(
            'post',
            '/v1/payment_intents',
            self.FIXTURE
        )

        resource = stripe.PaymentIntent.create(
            allowed_source_types=['card'],
            amount='1234',
            currency='amount'
        )
        self.assert_requested(
            'post',
            '/v1/payment_intents',
        )
        self.assertIsInstance(resource, stripe.PaymentIntent)

    def test_is_modifiable(self):
        self.stub_request(
            'post',
            '/v1/payment_intents/%s' % TEST_RESOURCE_ID,
            self.FIXTURE
        )

        resource = stripe.PaymentIntent.modify(
            TEST_RESOURCE_ID,
            metadata={'key': 'value'}
        )
        self.assert_requested(
            'post',
            '/v1/payment_intents/%s' % TEST_RESOURCE_ID,
            {'metadata': {'key': 'value'}}
        )
        self.assertIsInstance(resource, stripe.PaymentIntent)

    def test_is_saveable(self):
        resource = stripe.PaymentIntent.construct_from(self.FIXTURE,
                                                       stripe.api_key)

        self.stub_request(
            'post',
            '/v1/payment_intents/%s' % TEST_RESOURCE_ID,
            self.FIXTURE
        )

        resource.metadata['key'] = 'value'
        resource.save()
        self.assert_requested(
            'post',
            '/v1/payment_intents/%s' % resource.id,
            {'metadata': {'key': 'value'}}
        )
        self.assertIsInstance(resource, stripe.PaymentIntent)

    def test_can_cancel(self):
        resource = stripe.PaymentIntent.construct_from(self.FIXTURE,
                                                       stripe.api_key)

        self.stub_request(
            'post',
            '/v1/payment_intents/%s/cancel' % TEST_RESOURCE_ID,
            self.FIXTURE
        )

        resource.cancel()
        self.assert_requested(
            'post',
            '/v1/payment_intents/%s/cancel' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.PaymentIntent)

    def test_can_capture(self):
        resource = stripe.PaymentIntent.construct_from(self.FIXTURE,
                                                       stripe.api_key)

        self.stub_request(
            'post',
            '/v1/payment_intents/%s/capture' % TEST_RESOURCE_ID,
            self.FIXTURE
        )

        resource.capture()
        self.assert_requested(
            'post',
            '/v1/payment_intents/%s/capture' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.PaymentIntent)

    def test_can_confirm(self):
        resource = stripe.PaymentIntent.construct_from(self.FIXTURE,
                                                       stripe.api_key)

        self.stub_request(
            'post',
            '/v1/payment_intents/%s/confirm' % TEST_RESOURCE_ID,
            self.FIXTURE
        )

        resource.confirm()
        self.assert_requested(
            'post',
            '/v1/payment_intents/%s/confirm' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.PaymentIntent)
