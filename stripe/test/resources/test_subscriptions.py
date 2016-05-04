import datetime
import time

import stripe
from stripe.test.helper import (
    StripeResourceTest, DUMMY_PLAN
)


class SubscriptionTest(StripeResourceTest):

    def test_list_subscriptions(self):
        stripe.Subscription.all(customer="test_cus", plan=DUMMY_PLAN['id'],
                                limit=3)
        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/subscriptions',
            {
                'customer': 'test_cus',
                'plan': DUMMY_PLAN['id'],
                'limit': 3,
            },
        )

    def test_retrieve_subscription(self):
        stripe.Subscription.retrieve('test_sub')

        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/subscriptions/test_sub',
            {},
            None
        )

    def test_create_subscription(self):
        stripe.Subscription.create(customer="test_cus", plan=DUMMY_PLAN['id'])

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/subscriptions',
            {
                'customer': 'test_cus',
                'plan': DUMMY_PLAN['id']
            },
            None
        )

    def test_update_subscription(self):
        subscription = stripe.Subscription.construct_from({
            'id': 'test_sub',
            'customer': 'test_cus',
        }, 'api_key')

        trial_end_dttm = datetime.datetime.now() + datetime.timedelta(days=15)
        trial_end_int = int(time.mktime(trial_end_dttm.timetuple()))

        subscription.plan = DUMMY_PLAN['id']
        subscription.trial_end = trial_end_int
        subscription.save()

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/subscriptions/test_sub',
            {
                'plan': DUMMY_PLAN['id'],
                'trial_end': trial_end_int
            },
            None
        )

    def test_delete_subscription(self):
        subscription = stripe.Subscription.construct_from({
            'id': 'test_sub',
            'customer': 'test_cus',
        }, 'api_key')

        subscription.delete()

        self.requestor_mock.request.assert_called_with(
            'delete',
            '/v1/subscriptions/test_sub',
            {},
            None
        )

    def test_delete_subscription_discount(self):
        subscription = stripe.Subscription.construct_from({
            'id': 'test_sub',
            'customer': 'test_cus',
            'coupon': 'test_discount'
        }, 'api_key')

        subscription.delete_discount()

        self.requestor_mock.request.assert_called_with(
            'delete',
            '/v1/subscriptions/test_sub/discount'
        )
