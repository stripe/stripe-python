from __future__ import absolute_import, division, print_function

import stripe
from tests.helper import StripeTestCase


TEST_RESOURCE_ID = 'dp_123'


class DisputeTest(StripeTestCase):
    def test_is_listable(self):
        resources = stripe.Dispute.list()
        self.assert_requested(
            'get',
            '/v1/disputes'
        )
        self.assertIsInstance(resources.data, list)
        self.assertIsInstance(resources.data[0], stripe.Dispute)

    def test_is_retrievable(self):
        resource = stripe.Dispute.retrieve(TEST_RESOURCE_ID)
        self.assert_requested(
            'get',
            '/v1/disputes/%s' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.Dispute)

    def test_is_saveable(self):
        resource = stripe.Dispute.retrieve(TEST_RESOURCE_ID)
        resource.metadata['key'] = 'value'
        resource.save()
        self.assert_requested(
            'post',
            '/v1/disputes/%s' % resource.id
        )

    def test_is_modifiable(self):
        resource = stripe.Dispute.modify(
            TEST_RESOURCE_ID,
            metadata={'key': 'value'}
        )
        self.assert_requested(
            'post',
            '/v1/disputes/%s' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.Dispute)

    def test_is_closeable(self):
        resource = stripe.Dispute.retrieve(TEST_RESOURCE_ID)
        resource.close()
        self.assert_requested(
            'post',
            '/v1/disputes/%s/close' % resource.id
        )
