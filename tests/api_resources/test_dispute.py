from __future__ import absolute_import, division, print_function

import stripe


TEST_RESOURCE_ID = 'dp_123'


class TestDispute(object):
    def test_is_listable(self, request_mock):
        resources = stripe.Dispute.list()
        request_mock.assert_requested(
            'get',
            '/v1/disputes'
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Dispute)

    def test_is_retrievable(self, request_mock):
        resource = stripe.Dispute.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            'get',
            '/v1/disputes/%s' % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Dispute)

    def test_is_saveable(self, request_mock):
        resource = stripe.Dispute.retrieve(TEST_RESOURCE_ID)
        resource.metadata['key'] = 'value'
        resource.save()
        request_mock.assert_requested(
            'post',
            '/v1/disputes/%s' % resource.id
        )

    def test_is_modifiable(self, request_mock):
        resource = stripe.Dispute.modify(
            TEST_RESOURCE_ID,
            metadata={'key': 'value'}
        )
        request_mock.assert_requested(
            'post',
            '/v1/disputes/%s' % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Dispute)

    def test_is_closeable(self, request_mock):
        resource = stripe.Dispute.retrieve(TEST_RESOURCE_ID)
        resource.close()
        request_mock.assert_requested(
            'post',
            '/v1/disputes/%s/close' % resource.id
        )
