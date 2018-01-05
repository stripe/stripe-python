from __future__ import absolute_import, division, print_function

import warnings

import stripe
from tests.helper import (StripeTestCase)


TEST_RESOURCE_ID = 'cus_123'
TEST_SUB_ID = 'sub_123'
TEST_SOURCE_ID = 'ba_123'


class CustomerTest(StripeTestCase):
    def test_is_listable(self):
        resources = stripe.Customer.list()
        self.assert_requested(
            'get',
            '/v1/customers'
        )
        self.assertIsInstance(resources.data, list)
        self.assertIsInstance(resources.data[0], stripe.Customer)

    def test_is_retrievable(self):
        resource = stripe.Customer.retrieve(TEST_RESOURCE_ID)
        self.assert_requested(
            'get',
            '/v1/customers/%s' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.Customer)

    def test_is_creatable(self):
        resource = stripe.Customer.create()
        self.assert_requested(
            'post',
            '/v1/customers'
        )
        self.assertIsInstance(resource, stripe.Customer)

    def test_is_saveable(self):
        resource = stripe.Customer.retrieve(TEST_RESOURCE_ID)
        resource.metadata['key'] = 'value'
        resource.save()
        self.assert_requested(
            'post',
            '/v1/customers/%s' % resource.id
        )

    def test_is_modifiable(self):
        resource = stripe.Customer.modify(
            TEST_RESOURCE_ID,
            metadata={'key': 'value'}
        )
        self.assert_requested(
            'post',
            '/v1/customers/%s' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.Customer)

    def test_is_deletable(self):
        resource = stripe.Customer.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        self.assert_requested(
            'delete',
            '/v1/customers/%s' % resource.id
        )
        self.assertIsInstance(resource, stripe.Customer)


class CustomerSourcesTests(StripeTestCase):
    def test_is_creatable(self):
        stripe.Customer.create_source(
            TEST_RESOURCE_ID,
            source='btok_123'
        )
        self.assert_requested(
            'post',
            '/v1/customers/%s/sources' % TEST_RESOURCE_ID
        )

    def test_is_retrievable(self):
        stripe.Customer.retrieve_source(
            TEST_RESOURCE_ID,
            TEST_SOURCE_ID
        )
        self.assert_requested(
            'get',
            '/v1/customers/%s/sources/%s' % (TEST_RESOURCE_ID,
                                             TEST_SOURCE_ID)
        )

    def test_is_modifiable(self):
        stripe.Customer.modify_source(
            TEST_RESOURCE_ID,
            TEST_SOURCE_ID,
            metadata={'foo': 'bar'}
        )
        self.assert_requested(
            'post',
            '/v1/customers/%s/sources/%s' % (TEST_RESOURCE_ID,
                                             TEST_SOURCE_ID)
        )

    def test_is_deletable(self):
        stripe.Customer.delete_source(
            TEST_RESOURCE_ID,
            TEST_SOURCE_ID
        )
        self.assert_requested(
            'delete',
            '/v1/customers/%s/sources/%s' % (TEST_RESOURCE_ID,
                                             TEST_SOURCE_ID)
        )

    def test_is_listable(self):
        resources = stripe.Customer.list_sources(TEST_RESOURCE_ID)
        self.assert_requested(
            'get',
            '/v1/customers/%s/sources' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resources.data, list)
