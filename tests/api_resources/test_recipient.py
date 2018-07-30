from __future__ import absolute_import, division, print_function

import stripe


TEST_RESOURCE_ID = 'rp_123'


class TestRecipient(object):
    def test_is_listable(self, request_mock):
        resources = stripe.Recipient.list()
        request_mock.assert_requested(
            'get',
            '/v1/recipients'
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Recipient)

    def test_is_retrievable(self, request_mock):
        resource = stripe.Recipient.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            'get',
            '/v1/recipients/%s' % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Recipient)

    def test_is_creatable(self, request_mock):
        resource = stripe.Recipient.create(
            type='individual',
            name='NAME'
        )
        request_mock.assert_requested(
            'post',
            '/v1/recipients'
        )
        assert isinstance(resource, stripe.Recipient)

    def test_is_saveable(self, request_mock):
        resource = stripe.Recipient.retrieve(TEST_RESOURCE_ID)
        resource.metadata['key'] = 'value'
        resource.save()
        request_mock.assert_requested(
            'post',
            '/v1/recipients/%s' % TEST_RESOURCE_ID
        )

    def test_is_modifiable(self, request_mock):
        resource = stripe.Recipient.modify(
            TEST_RESOURCE_ID,
            metadata={'key': 'value'}
        )
        request_mock.assert_requested(
            'post',
            '/v1/recipients/%s' % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Recipient)

    def test_is_deletable(self, request_mock):
        resource = stripe.Recipient.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested(
            'delete',
            '/v1/recipients/%s' % TEST_RESOURCE_ID
        )
        assert resource.deleted is True
