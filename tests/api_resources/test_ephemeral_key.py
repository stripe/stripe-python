from __future__ import absolute_import, division, print_function

import warnings

import stripe
from tests.helper import StripeTestCase


class EphemeralKeyTest(StripeTestCase):

    def test_is_creatable(self):
        resource = stripe.EphemeralKey.create(
            customer='cus_123',
            stripe_version='2017-05-25'
        )
        self.request_mock.assert_api_version('2017-05-25')
        self.assert_requested(
            'post',
            '/v1/ephemeral_keys',
            {'customer': 'cus_123'}
        )
        self.assertIsInstance(resource, stripe.EphemeralKey)

    def test_raises_a_warning_when_using_api_version_arg(self):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')

            resource = stripe.EphemeralKey.create(
                customer='cus_123',
                api_version='2017-05-25'
            )
            self.request_mock.assert_api_version('2017-05-25')
            self.assert_requested(
                'post',
                '/v1/ephemeral_keys',
                {'customer': 'cus_123'}
            )
            self.assertIsInstance(resource, stripe.EphemeralKey)

            self.assertEqual(1, len(w))
            self.assertEqual(w[0].category, DeprecationWarning)

    def test_is_not_creatable_without_an_explicit_api_version(self):
        with self.assertRaisesRegex(ValueError,
                                    'stripe_version must be specified'):
            stripe.EphemeralKey.create(customer='cus_123')

    def test_is_deletable(self):
        resource = stripe.EphemeralKey.create(
            customer='cus_123',
            stripe_version='2017-05-25'
        )
        resource.delete()
        self.assert_requested(
            'delete',
            '/v1/ephemeral_keys/%s' % resource.id
        )
