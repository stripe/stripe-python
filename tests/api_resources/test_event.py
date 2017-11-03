from __future__ import absolute_import, division, print_function

import stripe
from tests.helper import StripeTestCase


TEST_RESOURCE_ID = 'evt_123'


class EventTest(StripeTestCase):
    def test_is_listable(self):
        resources = stripe.Event.list()
        self.assert_requested(
            'get',
            '/v1/events'
        )
        self.assertIsInstance(resources.data, list)
        self.assertIsInstance(resources.data[0], stripe.Event)

    def test_is_retrievable(self):
        resource = stripe.Event.retrieve(TEST_RESOURCE_ID)
        self.assert_requested(
            'get',
            '/v1/events/%s' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.Event)
