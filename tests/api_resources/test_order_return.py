from __future__ import absolute_import, division, print_function

import stripe
from tests.helper import StripeTestCase


TEST_RESOURCE_ID = 'orret_123'


class OrderReturnTest(StripeTestCase):
    def test_is_listable(self):
        resources = stripe.OrderReturn.list()
        self.assert_requested(
            'get',
            '/v1/order_returns'
        )
        self.assertIsInstance(resources.data, list)
        self.assertIsInstance(resources.data[0], stripe.OrderReturn)

    def test_is_retrievable(self):
        resource = stripe.OrderReturn.retrieve(TEST_RESOURCE_ID)
        self.assert_requested(
            'get',
            '/v1/order_returns/%s' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.OrderReturn)
