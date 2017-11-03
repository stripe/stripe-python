from __future__ import absolute_import, division, print_function

import stripe
from tests.helper import StripeTestCase


TEST_RESOURCE_ID = 'or_123'


class OrderTest(StripeTestCase):
    def test_is_listable(self):
        resources = stripe.Order.list()
        self.assert_requested(
            'get',
            '/v1/orders'
        )
        self.assertIsInstance(resources.data, list)
        self.assertIsInstance(resources.data[0], stripe.Order)

    def test_is_retrievable(self):
        resource = stripe.Order.retrieve(TEST_RESOURCE_ID)
        self.assert_requested(
            'get',
            '/v1/orders/%s' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.Order)

    def test_is_creatable(self):
        resource = stripe.Order.create(
            currency='usd'
        )
        self.assert_requested(
            'post',
            '/v1/orders'
        )
        self.assertIsInstance(resource, stripe.Order)

    def test_is_saveable(self):
        resource = stripe.Order.retrieve(TEST_RESOURCE_ID)
        resource.metadata['key'] = 'value'
        resource.save()
        self.assert_requested(
            'post',
            '/v1/orders/%s' % resource.id
        )

    def test_is_modifiable(self):
        resource = stripe.Order.modify(
            TEST_RESOURCE_ID,
            metadata={'key': 'value'}
        )
        self.assert_requested(
            'post',
            '/v1/orders/%s' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.Order)

    def test_is_payable(self):
        order = stripe.Order.retrieve(TEST_RESOURCE_ID)
        resource = order.pay(source='src_123')
        self.assert_requested(
            'post',
            '/v1/orders/%s/pay' % order.id,
            {
                'source': 'src_123'
            }
        )
        self.assertTrue(resource, stripe.Order)
        self.assertTrue(resource is order)

    def test_is_returnable(self):
        order = stripe.Order.retrieve(TEST_RESOURCE_ID)
        resource = order.return_order()
        self.assert_requested(
            'post',
            '/v1/orders/%s/returns' % order.id
        )
        self.assertIsInstance(resource, stripe.OrderReturn)
