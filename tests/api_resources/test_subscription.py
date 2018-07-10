from __future__ import absolute_import, division, print_function

import stripe


TEST_RESOURCE_ID = 'sub_123'


class TestSubscription(object):
    def test_is_listable(self, request_mock):
        resources = stripe.Subscription.list()
        request_mock.assert_requested(
            'get',
            '/v1/subscriptions'
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Subscription)

    def test_is_retrievable(self, request_mock):
        resource = stripe.Subscription.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            'get',
            '/v1/subscriptions/%s' % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Subscription)

    def test_is_creatable(self, request_mock):
        resource = stripe.Subscription.create(
            customer='cus_123',
        )
        request_mock.assert_requested(
            'post',
            '/v1/subscriptions'
        )
        assert isinstance(resource, stripe.Subscription)

    def test_is_saveable(self, request_mock):
        resource = stripe.Subscription.retrieve(TEST_RESOURCE_ID)
        resource.metadata['key'] = 'value'
        resource.save()
        request_mock.assert_requested(
            'post',
            '/v1/subscriptions/%s' % resource.id
        )

    def test_is_modifiable(self, request_mock):
        resource = stripe.Subscription.modify(
            TEST_RESOURCE_ID,
            metadata={'key': 'value'}
        )
        request_mock.assert_requested(
            'post',
            '/v1/subscriptions/%s' % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Subscription)

    def test_is_deletable(self, request_mock):
        resource = stripe.Subscription.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested(
            'delete',
            '/v1/subscriptions/%s' % resource.id
        )
        assert isinstance(resource, stripe.Subscription)

    def test_can_delete_discount(self, request_mock):
        sub = stripe.Subscription.retrieve(TEST_RESOURCE_ID)
        sub.delete_discount()
        request_mock.assert_requested(
            'delete',
            '/v1/subscriptions/%s/discount' % sub.id
        )

    # Test create/modify methods with subscription items

    def test_is_creatable_with_items(self, request_mock):
        resource = stripe.Subscription.create(
            customer='cus_123',
            items=[{"plan": "foo", "quantity": 3}]
        )
        request_mock.assert_requested(
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
        assert isinstance(resource, stripe.Subscription)

    def test_is_modifiable_with_items(self, request_mock):
        resource = stripe.Subscription.modify(
            TEST_RESOURCE_ID,
            items=[{"id": "si", "plan": "foo"}]
        )
        request_mock.assert_requested(
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
        assert isinstance(resource, stripe.Subscription)

    # TODO: Fix this test
    # def test_is_saveable_with_items(self):
    #    resource = stripe.Subscription.retrieve(TEST_RESOURCE_ID)
    #    resource.items = [{"id": "si", "plan": "foo"}]
    #    resource.save()
    #    request_mock.assert_requested(
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
    #    assert isinstance(resource, stripe.Subscription)

    # TODO: Test serialize
