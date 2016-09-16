import stripe
from stripe.test.helper import (
    StripeResourceTest, DUMMY_PLAN
)


class SubscriptionItemTest(StripeResourceTest):

    def test_list_subscriptions(self):
        stripe.SubscriptionItem.all(subscription='test_sub', limit=3)
        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/subscription_items',
            {
                'subscription': 'test_sub',
                'limit': 3,
            },
        )

    def test_retrieve_subscription(self):
        stripe.SubscriptionItem.retrieve('test_sub_item')

        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/subscription_items/test_sub_item',
            {},
            None
        )

    def test_create_subscription(self):
        stripe.SubscriptionItem.create(subscription='test_sub',
                                       plan=DUMMY_PLAN['id'])

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/subscription_items',
            {
                'subscription': 'test_sub',
                'plan': DUMMY_PLAN['id']
            },
            None
        )

    def test_update_subscription(self):
        item = stripe.SubscriptionItem.construct_from({
            'id': 'test_sub_item',
            'plan': 'test_plan',
        }, 'api_key')

        item.plan = DUMMY_PLAN['id']
        item.save()

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/subscription_items/test_sub_item',
            {
                'plan': DUMMY_PLAN['id'],
            },
            None
        )

    def test_modify_subscription(self):
        stripe.SubscriptionItem.modify('test_sub_item',
                                       plan=DUMMY_PLAN['id'])

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/subscription_items/test_sub_item',
            {
                'plan': DUMMY_PLAN['id'],
            },
            None
        )

    def test_delete_subscription(self):
        item = stripe.SubscriptionItem.construct_from({
            'id': 'test_sub_item',
            'plan': 'test_plan',
        }, 'api_key')

        item.delete()

        self.requestor_mock.request.assert_called_with(
            'delete',
            '/v1/subscription_items/test_sub_item',
            {},
            None
        )
