from __future__ import absolute_import, division, print_function

import stripe
from tests.helper import StripeTestCase


TEST_RESOURCE_ID = 'prod_123'


class ProductTest(StripeTestCase):
    def test_is_listable(self):
        resources = stripe.Product.list()
        self.assert_requested(
            'get',
            '/v1/products'
        )
        self.assertIsInstance(resources.data, list)
        self.assertIsInstance(resources.data[0], stripe.Product)

    def test_is_retrievable(self):
        resource = stripe.Product.retrieve(TEST_RESOURCE_ID)
        self.assert_requested(
            'get',
            '/v1/products/%s' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.Product)

    def test_is_creatable(self):
        resource = stripe.Product.create(
            name='NAME',
            type='good'
        )
        self.assert_requested(
            'post',
            '/v1/products'
        )
        self.assertIsInstance(resource, stripe.Product)

    def test_is_saveable(self):
        resource = stripe.Product.retrieve(TEST_RESOURCE_ID)
        resource.metadata['key'] = 'value'
        resource.save()
        self.assert_requested(
            'post',
            '/v1/products/%s' % resource.id
        )

    def test_is_modifiable(self):
        resource = stripe.Product.modify(
            TEST_RESOURCE_ID,
            metadata={'key': 'value'}
        )
        self.assert_requested(
            'post',
            '/v1/products/%s' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.Product)

    def test_is_deletable(self):
        resource = stripe.Product.retrieve(TEST_RESOURCE_ID)
        # Unfortunately stripe-mock will return a resource with a different
        # ID, so we need to store the original ID for the request assertion
        resource_id = resource.id
        resource.delete()
        self.assert_requested(
            'delete',
            '/v1/products/%s' % resource_id
        )
        self.assertTrue(resource.deleted)
