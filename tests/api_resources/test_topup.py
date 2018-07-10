from __future__ import absolute_import, division, print_function

import stripe


TEST_RESOURCE_ID = 'tu_123'


class TestTopup(object):
    def test_is_listable(self, request_mock):
        resources = stripe.Topup.list()
        request_mock.assert_requested(
            'get',
            '/v1/topups'
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Topup)

    def test_is_retrievable(self, request_mock):
        resource = stripe.Topup.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            'get',
            '/v1/topups/%s' % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Topup)

    def test_is_creatable(self, request_mock):
        resource = stripe.Topup.create(
            amount=100,
            currency='usd',
            source='src_123',
            description='description',
            statement_descriptor='statement descriptor'
        )
        request_mock.assert_requested(
            'post',
            '/v1/topups'
        )
        assert isinstance(resource, stripe.Topup)

    def test_is_saveable(self, request_mock):
        resource = stripe.Topup.retrieve(TEST_RESOURCE_ID)
        resource.metadata['key'] = 'value'
        resource.save()
        request_mock.assert_requested(
            'post',
            '/v1/topups/%s' % resource.id
        )

    def test_is_modifiable(self, request_mock):
        resource = stripe.Topup.modify(
            TEST_RESOURCE_ID,
            metadata={'key': 'value'}
        )
        request_mock.assert_requested(
            'post',
            '/v1/topups/%s' % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Topup)
