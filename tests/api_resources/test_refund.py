from __future__ import absolute_import, division, print_function

import stripe
from tests.helper import StripeTestCase


TEST_RESOURCE_ID = 're_123'


class RefundTest(StripeTestCase):
    def test_is_listable(self):
        resources = stripe.Refund.list()
        self.assert_requested(
            'get',
            '/v1/refunds'
        )
        self.assertIsInstance(resources.data, list)
        self.assertIsInstance(resources.data[0], stripe.Refund)

    def test_is_retrievable(self):
        resource = stripe.Refund.retrieve(TEST_RESOURCE_ID)
        self.assert_requested(
            'get',
            '/v1/refunds/%s' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.Refund)

    def test_is_creatable(self):
        resource = stripe.Refund.create(
            charge='ch_123'
        )
        self.assert_requested(
            'post',
            '/v1/refunds'
        )
        self.assertIsInstance(resource, stripe.Refund)

    def test_is_saveable(self):
        resource = stripe.Refund.retrieve(TEST_RESOURCE_ID)
        resource.metadata['key'] = 'value'
        resource.save()
        self.assert_requested(
            'post',
            '/v1/refunds/%s' % resource.id
        )

    def test_is_modifiable(self):
        resource = stripe.Refund.modify(
            TEST_RESOURCE_ID,
            metadata={'key': 'value'}
        )
        self.assert_requested(
            'post',
            '/v1/refunds/%s' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.Refund)
