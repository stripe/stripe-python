from __future__ import absolute_import, division, print_function

import stripe


TEST_RESOURCE_ID = 'idp_123'


class TestDispute(object):
    def test_is_creatable(self, request_mock):
        resource = stripe.issuing.Dispute.create(
            reason='fraudulent',
            disputed_transaction='ipi_123'
        )
        request_mock.assert_requested(
            'post',
            '/v1/issuing/disputes'
        )
        assert isinstance(resource, stripe.issuing.Dispute)

    def test_is_listable(self, request_mock):
        resources = stripe.issuing.Dispute.list()
        request_mock.assert_requested(
            'get',
            '/v1/issuing/disputes'
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.issuing.Dispute)

    def test_is_modifiable(self, request_mock):
        resource = stripe.issuing.Dispute.modify(
            TEST_RESOURCE_ID,
            metadata={'key': 'value'}
        )
        request_mock.assert_requested(
            'post',
            '/v1/issuing/disputes/%s' % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.issuing.Dispute)

    def test_is_retrievable(self, request_mock):
        resource = stripe.issuing.Dispute.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            'get',
            '/v1/issuing/disputes/%s' % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.issuing.Dispute)

    def test_is_saveable(self, request_mock):
        resource = stripe.issuing.Dispute.retrieve(TEST_RESOURCE_ID)
        resource.metadata['key'] = 'value'
        dispute = resource.save()
        request_mock.assert_requested(
            'post',
            '/v1/issuing/disputes/%s' % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.issuing.Dispute)
        assert resource is dispute
