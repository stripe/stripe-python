from __future__ import absolute_import, division, print_function

import stripe


TEST_RESOURCE_ID = 'prod_123'


class TestProduct(object):
    def test_is_listable(self, request_mock):
        resources = stripe.Product.list()
        request_mock.assert_requested(
            'get',
            '/v1/products'
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Product)

    def test_is_retrievable(self, request_mock):
        resource = stripe.Product.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            'get',
            '/v1/products/%s' % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Product)

    def test_is_creatable(self, request_mock):
        resource = stripe.Product.create(
            name='NAME',
            type='good'
        )
        request_mock.assert_requested(
            'post',
            '/v1/products'
        )
        assert isinstance(resource, stripe.Product)

    def test_is_saveable(self, request_mock):
        resource = stripe.Product.retrieve(TEST_RESOURCE_ID)
        resource.metadata['key'] = 'value'
        resource.save()
        request_mock.assert_requested(
            'post',
            '/v1/products/%s' % TEST_RESOURCE_ID
        )

    def test_is_modifiable(self, request_mock):
        resource = stripe.Product.modify(
            TEST_RESOURCE_ID,
            metadata={'key': 'value'}
        )
        request_mock.assert_requested(
            'post',
            '/v1/products/%s' % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Product)

    def test_is_deletable(self, request_mock):
        resource = stripe.Product.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested(
            'delete',
            '/v1/products/%s' % TEST_RESOURCE_ID
        )
        assert resource.deleted is True
