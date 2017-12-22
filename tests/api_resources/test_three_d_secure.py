from __future__ import absolute_import, division, print_function

import stripe
from tests.helper import StripeTestCase


TEST_RESOURCE_ID = 'tdsrc_123'


class ThreeDSecureTest(StripeTestCase):
    def test_is_retrievable(self):
        resource = stripe.ThreeDSecure.retrieve(TEST_RESOURCE_ID)
        self.assert_requested(
            'get',
            '/v1/3d_secure/%s' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.ThreeDSecure)

    def test_is_creatable(self):
        resource = stripe.ThreeDSecure.create(
            card="tok_123",
            amount=100,
            currency="usd",
            return_url="url"
        )
        self.assert_requested(
            'post',
            '/v1/3d_secure'
        )
        self.assertIsInstance(resource, stripe.ThreeDSecure)
