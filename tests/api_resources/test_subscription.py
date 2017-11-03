from __future__ import absolute_import, division, print_function

import stripe
from tests.helper import StripeTestCase


TEST_RESOURCE_ID = 'sub_123'


class SubscriptionTest(StripeTestCase):
    def test_is_listable(self):
        resources = stripe.Subscription.list()
        self.assert_requested(
            'get',
            '/v1/subscriptions'
        )
        self.assertIsInstance(resources.data, list)
        self.assertIsInstance(resources.data[0], stripe.Subscription)

    def test_is_retrievable(self):
        resource = stripe.Subscription.retrieve(TEST_RESOURCE_ID)
        self.assert_requested(
            'get',
            '/v1/subscriptions/%s' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.Subscription)

    def test_is_creatable(self):
        resource = stripe.Subscription.create(
            customer='cus_123',
            plan='plan'
        )
        self.assert_requested(
            'post',
            '/v1/subscriptions'
        )
        self.assertIsInstance(resource, stripe.Subscription)

    def test_is_saveable(self):
        resource = stripe.Subscription.retrieve(TEST_RESOURCE_ID)
        resource.metadata['key'] = 'value'
        resource.save()
        self.assert_requested(
            'post',
            '/v1/subscriptions/%s' % resource.id
        )

    def test_is_modifiable(self):
        resource = stripe.Subscription.modify(
            TEST_RESOURCE_ID,
            metadata={'key': 'value'}
        )
        self.assert_requested(
            'post',
            '/v1/subscriptions/%s' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.Subscription)

    def test_is_deletable(self):
        resource = stripe.Subscription.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        self.assert_requested(
            'delete',
            '/v1/subscriptions/%s' % resource.id
        )
        self.assertIsInstance(resource, stripe.Subscription)

    def test_can_delete_discount(self):
        sub = stripe.Subscription.retrieve(TEST_RESOURCE_ID)
        sub.delete_discount()
        self.assert_requested(
            'delete',
            '/v1/subscriptions/%s/discount' % sub.id
        )

    # Test create/modify methods with subscription items

    def test_is_creatable_with_items(self):
        resource = stripe.Subscription.create(
            customer='cus_123',
            items=[{"plan": "foo", "quantity": 3}]
        )
        self.assert_requested(
            'post',
            '/v1/subscriptions',
            {
                'customer': 'cus_123',
                'items': {
                    "0": {
                        "plan": "foo",
                        "quantity": 3
                    },
                },
            },
        )
        self.assertIsInstance(resource, stripe.Subscription)

    def test_is_modifiable_with_items(self):
        resource = stripe.Subscription.modify(
            TEST_RESOURCE_ID,
            items=[{"id": "si", "plan": "foo"}]
        )
        self.assert_requested(
            'post',
            '/v1/subscriptions/%s' % TEST_RESOURCE_ID,
            {
                'items': {
                    "0": {
                        "plan": "foo",
                        "id": "si"
                    },
                },
            },
        )
        self.assertIsInstance(resource, stripe.Subscription)

    # TODO: Fix this test
    # def test_is_saveable_with_items(self):
    #    resource = stripe.Subscription.retrieve(TEST_RESOURCE_ID)
    #    resource.items = [{"id": "si", "plan": "foo"}]
    #    resource.save()
    #    self.assert_requested(
    #        'post',
    #        '/v1/subscriptions/%s' % TEST_RESOURCE_ID,
    #        {
    #            'items': {
    #                "0": {
    #                    "plan": "foo",
    #                    "id": "si"
    #                },
    #            },
    #        },
    #    )
    #    self.assertIsInstance(resource, stripe.Subscription)

    # TODO: Test serialize
