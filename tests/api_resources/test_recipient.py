from __future__ import absolute_import, division, print_function

import stripe
from tests.helper import (StripeTestCase)


TEST_RESOURCE_ID = 'rp_123'


class RecipientTest(StripeTestCase):
    def test_is_listable(self):
        resources = stripe.Recipient.list()
        self.assert_requested(
            'get',
            '/v1/recipients'
        )
        self.assertIsInstance(resources.data, list)
        self.assertIsInstance(resources.data[0], stripe.Recipient)

    def test_is_retrievable(self):
        resource = stripe.Recipient.retrieve(TEST_RESOURCE_ID)
        self.assert_requested(
            'get',
            '/v1/recipients/%s' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.Recipient)

    def test_is_creatable(self):
        resource = stripe.Recipient.create(
            type='individual',
            name='NAME'
        )
        self.assert_requested(
            'post',
            '/v1/recipients'
        )
        self.assertIsInstance(resource, stripe.Recipient)

    def test_is_saveable(self):
        resource = stripe.Recipient.retrieve(TEST_RESOURCE_ID)
        resource.metadata['key'] = 'value'
        resource.save()
        self.assert_requested(
            'post',
            '/v1/recipients/%s' % resource.id
        )

    def test_is_modifiable(self):
        resource = stripe.Recipient.modify(
            TEST_RESOURCE_ID,
            metadata={'key': 'value'}
        )
        self.assert_requested(
            'post',
            '/v1/recipients/%s' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.Recipient)

    def test_is_deletable(self):
        resource = stripe.Recipient.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        self.assert_requested(
            'delete',
            '/v1/recipients/%s' % resource.id
        )
        self.assertIsInstance(resource, stripe.Recipient)
