from __future__ import absolute_import, division, print_function

import stripe


TEST_RESOURCE_ID = 'si_123'


class TestSubscriptionItem(object):
    def test_is_listable(self, request_mock):
        resources = stripe.SubscriptionItem.list(
            subscription="sub_123"
        )
        request_mock.assert_requested(
            'get',
            '/v1/subscription_items',
            {
                'subscription': 'sub_123',
            }
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.SubscriptionItem)

    def test_is_retrievable(self, request_mock):
        resource = stripe.SubscriptionItem.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            'get',
            '/v1/subscription_items/%s' % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.SubscriptionItem)

    def test_is_creatable(self, request_mock):
        resource = stripe.SubscriptionItem.create(
            plan='plan',
            subscription='sub_123'
        )
        request_mock.assert_requested(
            'post',
            '/v1/subscription_items'
        )
        assert isinstance(resource, stripe.SubscriptionItem)

    def test_is_saveable(self, request_mock):
        resource = stripe.SubscriptionItem.retrieve(TEST_RESOURCE_ID)
        resource.plan = 'plan'
        resource.save()
        request_mock.assert_requested(
            'post',
            '/v1/subscription_items/%s' % TEST_RESOURCE_ID,
            {
                'plan': 'plan',
            },
        )

    def test_is_modifiable(self, request_mock):
        resource = stripe.SubscriptionItem.modify(
            TEST_RESOURCE_ID,
            plan='plan'
        )
        request_mock.assert_requested(
            'post',
            '/v1/subscription_items/%s' % TEST_RESOURCE_ID,
            {
                'plan': 'plan',
            },
        )
        assert isinstance(resource, stripe.SubscriptionItem)

    def test_is_deletable(self, request_mock):
        resource = stripe.SubscriptionItem.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested(
            'delete',
            '/v1/subscription_items/%s' % TEST_RESOURCE_ID
        )
        assert resource.deleted is True
