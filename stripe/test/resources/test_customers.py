import datetime
import time
import warnings

import stripe
from stripe.test.helper import (
    StripeResourceTest, DUMMY_CARD, DUMMY_PLAN
)


class CustomerTest(StripeResourceTest):

    def test_list_customers(self):
        stripe.Customer.list()
        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/customers',
            {},
        )

    def test_create_customer(self):
        stripe.Customer.create(description="foo bar", card=DUMMY_CARD,
                               coupon='cu_discount', idempotency_key='foo')
        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/customers',
            {
                'coupon': 'cu_discount',
                'description': 'foo bar',
                'card': DUMMY_CARD
            },
            {'Idempotency-Key': 'foo'}
        )

    def test_unset_description(self):
        customer = stripe.Customer(id="cus_unset_desc")
        customer.description = "Hey"
        customer.save(idempotency_key='foo')

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/customers/cus_unset_desc',
            {
                'description': 'Hey',
            },
            {'Idempotency-Key': 'foo'}
        )

    def test_del_coupon(self):
        customer = stripe.Customer(id="cus_unset_desc")
        customer.description = "bar"
        customer.coupon = "foo"
        del customer.coupon
        customer.save()

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/customers/cus_unset_desc',
            {
                'description': 'bar'
            },
            None
        )

    def test_cannot_set_empty_string(self):
        customer = stripe.Customer()
        self.assertRaises(ValueError, setattr, customer, "description", "")

    def test_customer_add_card(self):
        customer = stripe.Customer.construct_from({
            'id': 'cus_add_card',
            'sources': {
                'object': 'list',
                'url': '/v1/customers/cus_add_card/sources',
            },
        }, 'api_key')
        customer.sources.create(card=DUMMY_CARD, idempotency_key='foo')

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/customers/cus_add_card/sources',
            {
                'card': DUMMY_CARD,
            },
            {'Idempotency-Key': 'foo'}
        )

    def test_customer_add_source(self):
        customer = stripe.Customer.construct_from({
            'id': 'cus_add_source',
            'sources': {
                'object': 'list',
                'url': '/v1/customers/cus_add_source/sources',
            },
        }, 'api_key')
        customer.sources.create(source=DUMMY_CARD, idempotency_key='foo')

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/customers/cus_add_source/sources',
            {
                'source': DUMMY_CARD,
            },
            {'Idempotency-Key': 'foo'}
        )

    def test_customer_update_card(self):
        card = stripe.Card.construct_from({
            'customer': 'cus_update_card',
            'id': 'ca_update_card',
        }, 'api_key')
        card.name = 'The Best'
        card.save(idempotency_key='foo')

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/customers/cus_update_card/sources/ca_update_card',
            {
                'name': 'The Best',
            },
            {'Idempotency-Key': 'foo'}
        )

    def test_customer_update_source(self):
        source = stripe.BitcoinReceiver.construct_from({
            'customer': 'cus_update_source',
            'id': 'btcrcv_update_source',
        }, 'api_key')
        source.name = 'The Best'
        source.save(idempotency_key='foo')

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/customers/cus_update_source/sources/btcrcv_update_source',
            {
                'name': 'The Best',
            },
            {'Idempotency-Key': 'foo'}
        )

    def test_customer_update_alipay_account(self):
        aa = stripe.AlipayAccount.construct_from({
            'customer': 'cus_update_alipay',
            'id': 'ali_update',
        }, 'api_key')
        aa.metadata = {'name': 'The Best'}
        aa.save(idempotency_key='foo')

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/customers/cus_update_alipay/sources/ali_update',
            {
                'metadata': {'name': 'The Best'},
            },
            {'Idempotency-Key': 'foo'}
        )

    def test_customer_delete_card(self):
        card = stripe.Card.construct_from({
            'customer': 'cus_delete_card',
            'id': 'ca_delete_card',
        }, 'api_key')
        card.delete()

        self.requestor_mock.request.assert_called_with(
            'delete',
            '/v1/customers/cus_delete_card/sources/ca_delete_card',
            {},
            None
        )

    def test_customer_delete_source(self):
        source = stripe.BitcoinReceiver.construct_from({
            'customer': 'cus_delete_source',
            'id': 'btcrcv_delete_source',
        }, 'api_key')
        source.delete()

        self.requestor_mock.request.assert_called_with(
            'delete',
            '/v1/customers/cus_delete_source/sources/btcrcv_delete_source',
            {},
            None
        )

    def test_customer_delete_alipay_account(self):
        aa = stripe.AlipayAccount.construct_from({
            'customer': 'cus_delete_alipay',
            'id': 'ali_delete',
        }, 'api_key')
        aa.delete()

        self.requestor_mock.request.assert_called_with(
            'delete',
            '/v1/customers/cus_delete_alipay/sources/ali_delete',
            {},
            None
        )

    def test_customer_delete_bank_account(self):
        source = stripe.BankAccount.construct_from({
            'customer': 'cus_delete_source',
            'id': 'ba_delete_source',
        }, 'api_key')
        source.delete()

        self.requestor_mock.request.assert_called_with(
            'delete',
            '/v1/customers/cus_delete_source/sources/ba_delete_source',
            {},
            None
        )

    def test_customer_verify_bank_account(self):
        source = stripe.BankAccount.construct_from({
            'customer': 'cus_verify_source',
            'id': 'ba_verify_source',
        }, 'api_key')
        source.verify()

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/customers/cus_verify_source/sources/ba_verify_source/verify',
            {},
            None
        )


class CustomerPlanTest(StripeResourceTest):

    def test_create_customer(self):
        stripe.Customer.create(plan=DUMMY_PLAN['id'], card=DUMMY_CARD)

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/customers',
            {
                'card': DUMMY_CARD,
                'plan': DUMMY_PLAN['id'],
            },
            None
        )

    def test_legacy_update_subscription(self):
        with warnings.catch_warnings(record=True) as w:
            customer = stripe.Customer(id="cus_legacy_sub_update")
            customer.update_subscription(idempotency_key='foo',
                                         plan=DUMMY_PLAN['id'])

            self.requestor_mock.request.assert_called_with(
                'post',
                '/v1/customers/cus_legacy_sub_update/subscription',
                {
                    'plan': DUMMY_PLAN['id'],
                },
                {'Idempotency-Key': 'foo'}
            )

            self.assertEqual(len(w), 1)
            self.assertTrue(issubclass(w[-1].category, DeprecationWarning))

    def test_legacy_delete_subscription(self):
        with warnings.catch_warnings(record=True) as w:
            customer = stripe.Customer(id="cus_legacy_sub_delete")
            customer.cancel_subscription()

            self.requestor_mock.request.assert_called_with(
                'delete',
                '/v1/customers/cus_legacy_sub_delete/subscription',
                {},
                None
            )

            self.assertEqual(len(w), 1)
            self.assertTrue(issubclass(w[-1].category, DeprecationWarning))

    def test_list_customer_subscriptions(self):
        customer = stripe.Customer.construct_from({
            'id': 'cus_foo',
            'subscriptions': {
                'object': 'list',
                'url': 'v1/customers/cus_foo/subscriptions',
            }
        }, 'api_key')

        customer.subscriptions.all()

        self.requestor_mock.request.assert_called_with(
            'get',
            'v1/customers/cus_foo/subscriptions',
            {},
            None
        )

    def test_create_customer_subscription(self):
        customer = stripe.Customer.construct_from({
            'id': 'cus_sub_create',
            'subscriptions': {
                'object': 'list',
                'url': '/v1/customers/cus_sub_create/subscriptions',
            }
        }, 'api_key')

        customer.subscriptions.create(plan=DUMMY_PLAN['id'], coupon='foo')

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/customers/cus_sub_create/subscriptions',
            {
                'plan': DUMMY_PLAN['id'],
                'coupon': 'foo',
            },
            None
        )

    def test_retrieve_customer_subscription(self):
        customer = stripe.Customer.construct_from({
            'id': 'cus_foo',
            'subscriptions': {
                'object': 'list',
                'url': '/v1/customers/cus_foo/subscriptions',
            }
        }, 'api_key')

        customer.subscriptions.retrieve('sub_cus')

        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/customers/cus_foo/subscriptions/sub_cus',
            {},
            None
        )

    def test_update_customer_subscription(self):
        subscription = stripe.Subscription.construct_from({
            'id': "sub_update",
            'customer': "cus_foo",
        }, 'api_key')

        trial_end_dttm = datetime.datetime.now() + datetime.timedelta(days=15)
        trial_end_int = int(time.mktime(trial_end_dttm.timetuple()))

        subscription.trial_end = trial_end_int
        subscription.plan = DUMMY_PLAN['id']
        subscription.save()

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/subscriptions/sub_update',
            {
                'plan': DUMMY_PLAN['id'],
                'trial_end': trial_end_int,
            },
            None
        )

    def test_delete_customer_subscription(self):
        subscription = stripe.Subscription.construct_from({
            'id': "sub_delete",
            'customer': "cus_foo",
        }, 'api_key')

        subscription.delete()

        self.requestor_mock.request.assert_called_with(
            'delete',
            '/v1/subscriptions/sub_delete',
            {},
            None
        )
