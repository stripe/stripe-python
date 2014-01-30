# -*- coding: utf-8 -*-
import datetime
import os
import sys
import time
import unittest

from mock import patch

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
import stripe

from stripe.test.helper import (
    StripeTestCase,
    NOW, DUMMY_CARD, DUMMY_CHARGE, DUMMY_PLAN, DUMMY_COUPON,
    DUMMY_RECIPIENT, DUMMY_TRANSFER, DUMMY_INVOICE_ITEM)


class FunctionalTests(StripeTestCase):
    request_client = stripe.http_client.Urllib2Client

    def setUp(self):
        super(FunctionalTests, self).setUp()

        def get_http_client(*args, **kwargs):
            return self.request_client(*args, **kwargs)

        self.client_patcher = patch(
            'stripe.http_client.new_default_http_client')

        client_mock = self.client_patcher.start()
        client_mock.side_effect = get_http_client

    def tearDown(self):
        super(FunctionalTests, self).tearDown()

        self.client_patcher.stop()

    def test_dns_failure(self):
        api_base = stripe.api_base
        try:
            stripe.api_base = 'https://my-invalid-domain.ireallywontresolve/v1'
            self.assertRaises(stripe.error.APIConnectionError,
                              stripe.Customer.create)
        finally:
            stripe.api_base = api_base

    def test_run(self):
        charge = stripe.Charge.create(**DUMMY_CHARGE)
        self.assertFalse(charge.refunded)
        charge.refund()
        self.assertTrue(charge.refunded)

    def test_refresh(self):
        charge = stripe.Charge.create(**DUMMY_CHARGE)
        charge2 = stripe.Charge.retrieve(charge.id)
        self.assertEqual(charge2.created, charge.created)

        charge2.junk = 'junk'
        charge2.refresh()
        self.assertRaises(AttributeError, lambda: charge2.junk)

    def test_list_accessors(self):
        customer = stripe.Customer.create(card=DUMMY_CARD)
        self.assertEqual(customer['created'], customer.created)
        customer['foo'] = 'bar'
        self.assertEqual(customer.foo, 'bar')

    def test_raise(self):
        EXPIRED_CARD = DUMMY_CARD.copy()
        EXPIRED_CARD['exp_month'] = NOW.month - 2
        EXPIRED_CARD['exp_year'] = NOW.year - 2
        self.assertRaises(stripe.error.CardError, stripe.Charge.create,
                          amount=100, currency='usd', card=EXPIRED_CARD)

    def test_unicode(self):
        # Make sure unicode requests can be sent
        self.assertRaises(stripe.error.InvalidRequestError,
                          stripe.Charge.retrieve,
                          id=u'☃')

    def test_none_values(self):
        customer = stripe.Customer.create(plan=None)
        self.assertTrue(customer.id)

    def test_missing_id(self):
        customer = stripe.Customer()
        self.assertRaises(stripe.error.InvalidRequestError, customer.refresh)


class RequestsFunctionalTests(FunctionalTests):
    request_client = stripe.http_client.RequestsClient

# Avoid skipTest errors in < 2.7
if sys.version_info >= (2, 7):
    class UrlfetchFunctionalTests(FunctionalTests):
        request_client = 'urlfetch'

        def setUp(self):
            if stripe.http_client.urlfetch is None:
                self.skipTest(
                    '`urlfetch` from Google App Engine is unavailable.')
            else:
                super(UrlfetchFunctionalTests, self).setUp()


class PycurlFunctionalTests(FunctionalTests):
    def setUp(self):
        if sys.version_info >= (3, 0):
            self.skipTest('Pycurl is not supported in Python 3')
        else:
            super(PycurlFunctionalTests, self).setUp()

    request_client = stripe.http_client.PycurlClient


class AuthenticationErrorTest(StripeTestCase):

    def test_invalid_credentials(self):
        key = stripe.api_key
        try:
            stripe.api_key = 'invalid'
            stripe.Customer.create()
        except stripe.error.AuthenticationError, e:
            self.assertEqual(401, e.http_status)
            self.assertTrue(isinstance(e.http_body, basestring))
            self.assertTrue(isinstance(e.json_body, dict))
        finally:
            stripe.api_key = key


class CardErrorTest(StripeTestCase):

    def test_declined_card_props(self):
        EXPIRED_CARD = DUMMY_CARD.copy()
        EXPIRED_CARD['exp_month'] = NOW.month - 2
        EXPIRED_CARD['exp_year'] = NOW.year - 2
        try:
            stripe.Charge.create(amount=100, currency='usd', card=EXPIRED_CARD)
        except stripe.error.CardError, e:
            self.assertEqual(402, e.http_status)
            self.assertTrue(isinstance(e.http_body, basestring))
            self.assertTrue(isinstance(e.json_body, dict))

# Note that these are in addition to the core functional charge tests


class ChargeTest(StripeTestCase):

    def setUp(self):
        super(ChargeTest, self).setUp()

    def test_charge_list_all(self):
        charge_list = stripe.Charge.all(created={'lt': NOW})
        list_result = charge_list.all(created={'lt': NOW})

        self.assertEqual(len(charge_list.data),
                         len(list_result.data))

        for expected, actual in zip(charge_list.data,
                                    list_result.data):
            self.assertEqual(expected.id, actual.id)

    def test_charge_list_create(self):
        charge_list = stripe.Charge.all()

        charge = charge_list.create(**DUMMY_CHARGE)

        self.assertTrue(isinstance(charge, stripe.Charge))
        self.assertEqual(DUMMY_CHARGE['amount'], charge.amount)

    def test_charge_list_retrieve(self):
        charge_list = stripe.Charge.all()

        charge = charge_list.retrieve(charge_list.data[0].id)

        self.assertTrue(isinstance(charge, stripe.Charge))

    def test_charge_capture(self):
        params = DUMMY_CHARGE.copy()
        params['capture'] = False

        charge = stripe.Charge.create(**params)

        self.assertFalse(charge.captured)

        self.assertTrue(charge is charge.capture())
        self.assertTrue(stripe.Charge.retrieve(charge.id).captured)

    def test_charge_dispute(self):
        # We don't have a good way of simulating disputes
        # This is a pretty lame test but it at least checks that the
        # dispute code fails in the way we predict, not from e.g.
        # a syntax error

        charge = stripe.Charge.create(**DUMMY_CHARGE)

        self.assertRaisesRegexp(stripe.error.InvalidRequestError,
                                'No dispute for charge',
                                charge.update_dispute)

        self.assertRaisesRegexp(stripe.error.InvalidRequestError,
                                'No dispute for charge',
                                charge.close_dispute)


class AccountTest(StripeTestCase):

    def test_retrieve_account(self):
        account = stripe.Account.retrieve()
        self.assertEqual('test+bindings@stripe.com', account.email)
        self.assertFalse(account.charge_enabled)
        self.assertFalse(account.details_submitted)


class BalanceTest(StripeTestCase):

    def test_retrieve_balance(self):
        balance = stripe.Balance.retrieve()
        self.assertTrue(hasattr(balance, 'available'))
        self.assertTrue(isinstance(balance['available'], list))
        if len(balance['available']):
            self.assertTrue(hasattr(balance['available'][0], 'amount'))
            self.assertTrue(hasattr(balance['available'][0], 'currency'))

        self.assertTrue(hasattr(balance, 'pending'))
        self.assertTrue(isinstance(balance['pending'], list))
        if len(balance['pending']):
            self.assertTrue(hasattr(balance['pending'][0], 'amount'))
            self.assertTrue(hasattr(balance['pending'][0], 'currency'))

        self.assertEqual(False, balance['livemode'])
        self.assertEqual('balance', balance['object'])


class BalanceTransactionTest(StripeTestCase):

    def test_list_balance_transactions(self):
        balance_transactions = stripe.BalanceTransaction.all()
        self.assertTrue(hasattr(balance_transactions, 'count'))
        self.assertTrue(isinstance(balance_transactions.data, list))


class ApplicationFeeTest(StripeTestCase):
    def test_list_application_fees(self):
        application_fees = stripe.ApplicationFee.all()
        self.assertTrue(hasattr(application_fees, 'count'))
        self.assertTrue(isinstance(application_fees.data, list))


class CustomerTest(StripeTestCase):

    def test_list_customers(self):
        customers = stripe.Customer.all()
        self.assertTrue(isinstance(customers.data, list))

    def test_list_charges(self):
        customer = stripe.Customer.create(description="foo bar",
                                          card=DUMMY_CARD)

        stripe.Charge.create(customer=customer.id, amount=100, currency='usd')

        self.assertEqual(1,
                         len(customer.charges().data))

    def test_unset_description(self):
        customer = stripe.Customer.create(description="foo bar")

        customer.description = None
        customer.save()

        self.assertEqual(None, customer.retrieve(customer.id).description)

    def test_cannot_set_empty_string(self):
        customer = stripe.Customer()
        self.assertRaises(ValueError, setattr, customer, "description", "")

    def test_update_customer_card(self):
        customer = stripe.Customer.create(description="update_customer_card")
        card = customer.cards.create(card=DUMMY_CARD)

        card.name = 'Python bindings test'
        card.save()

        self.assertEqual('Python bindings test',
                         customer.cards.retrieve(card.id).name)


class TransferTest(StripeTestCase):

    def test_list_transfers(self):
        transfers = stripe.Transfer.all()
        self.assertTrue(isinstance(transfers.data, list))
        self.assertTrue(isinstance(transfers.data[0], stripe.Transfer))


class RecipientTest(StripeTestCase):

    def test_list_recipients(self):
        recipients = stripe.Recipient.all()
        self.assertTrue(isinstance(recipients.data, list))
        self.assertTrue(isinstance(recipients.data[0], stripe.Recipient))

    def test_recipient_transfers(self):
        recipient = stripe.Recipient.all(count=1).data[0]

        # Weak assertion since the list could be empty
        for transfer in recipient.transfers().data:
            self.assertTrue(isinstance(transfer, stripe.Transfer))


class CustomerPlanTest(StripeTestCase):

    def setUp(self):
        super(CustomerPlanTest, self).setUp()
        try:
            self.plan_obj = stripe.Plan.create(**DUMMY_PLAN)
        except stripe.error.InvalidRequestError:
            self.plan_obj = None

    def tearDown(self):
        if self.plan_obj:
            try:
                self.plan_obj.delete()
            except stripe.error.InvalidRequestError:
                pass
        super(CustomerPlanTest, self).tearDown()

    def test_create_customer(self):
        self.assertRaises(stripe.error.InvalidRequestError,
                          stripe.Customer.create,
                          plan=DUMMY_PLAN['id'])
        customer = stripe.Customer.create(
            plan=DUMMY_PLAN['id'], card=DUMMY_CARD)
        self.assertTrue(hasattr(customer, 'subscriptions'))
        self.assertFalse(hasattr(customer, 'plan'))
        customer.delete()
        self.assertFalse(hasattr(customer, 'plan'))
        self.assertTrue(customer.deleted)

    def test_legacy_update_and_cancel_subscription(self):
        customer = stripe.Customer.create(card=DUMMY_CARD)

        sub = customer.update_subscription(plan=DUMMY_PLAN['id'])
        self.assertEqual(customer.subscription.id, sub.id)
        self.assertEqual(DUMMY_PLAN['id'], sub.plan.id)

        customer.cancel_subscription(at_period_end=True)
        self.assertEqual(customer.subscription.status, 'active')
        self.assertTrue(customer.subscription.cancel_at_period_end)
        customer.cancel_subscription()
        self.assertEqual(customer.subscription.status, 'canceled')

    def test_create_and_cancel_customer_subscription(self):
        customer = stripe.Customer.create(card=DUMMY_CARD)

        subscription = customer.subscriptions.create(plan=DUMMY_PLAN['id'])
        self.assertEqual(DUMMY_PLAN['id'], subscription.plan.id)

        subscription = customer.subscriptions.retrieve(subscription.id)
        subscription.delete(at_period_end=True)
        subscription = customer.subscriptions.retrieve(subscription.id)
        self.assertEqual(subscription.status, 'active')
        self.assertTrue(subscription.cancel_at_period_end)

        subscription = customer.subscriptions.retrieve(subscription.id)
        subscription = subscription.delete()
        self.assertEqual(subscription.status, 'canceled')

    def test_create_and_update_customer_subscription(self):
        customer = stripe.Customer.create(card=DUMMY_CARD)
        subscription = customer.subscriptions.create(plan=DUMMY_PLAN['id'])
        self.assertEqual(DUMMY_PLAN['id'], subscription.plan.id)

        subscription = customer.subscriptions.retrieve(subscription.id)
        trial_end_dttm = datetime.datetime.now() + datetime.timedelta(days=15)
        trial_end_int = int(time.mktime(trial_end_dttm.timetuple()))
        subscription.trial_end = trial_end_int
        subscription.plan = subscription.plan.id
        subscription.save()

        self.assertEqual(
            trial_end_int,
            customer.subscriptions.retrieve(subscription.id).trial_end)

    def test_datetime_trial_end(self):
        customer = stripe.Customer.create(
            plan=DUMMY_PLAN['id'], card=DUMMY_CARD,
            trial_end=datetime.datetime.now() + datetime.timedelta(days=15))
        self.assertTrue(customer.id)

    def test_integer_trial_end(self):
        trial_end_dttm = datetime.datetime.now() + datetime.timedelta(days=15)
        trial_end_int = int(time.mktime(trial_end_dttm.timetuple()))
        customer = stripe.Customer.create(plan=DUMMY_PLAN['id'],
                                          card=DUMMY_CARD,
                                          trial_end=trial_end_int)
        self.assertTrue(customer.id)


class InvoiceTest(StripeTestCase):

    def test_invoice(self):
        customer = stripe.Customer.create(card=DUMMY_CARD)

        customer.add_invoice_item(**DUMMY_INVOICE_ITEM)

        items = customer.invoice_items()
        self.assertEqual(1, len(items.data))

        invoice = stripe.Invoice.create(customer=customer)

        invoices = customer.invoices()
        self.assertEqual(1, len(invoices.data))
        self.assertEqual(1, len(invoices.data[0].lines.data))
        self.assertEqual(invoice.id, invoices.data[0].id)

        self.assertTrue(invoice.pay().paid)

        # It would be better to test for an actually existing
        # upcoming invoice but that isn't working so we'll just
        # check that the appropriate error comes back for now
        self.assertRaisesRegexp(
            stripe.error.InvalidRequestError,
            'No upcoming invoices',
            stripe.Invoice.upcoming,
            customer=customer)


class CouponTest(StripeTestCase):

    def test_create_coupon(self):
        self.assertRaises(stripe.error.InvalidRequestError,
                          stripe.Coupon.create, percent_off=25)
        c = stripe.Coupon.create(**DUMMY_COUPON)
        self.assertTrue(isinstance(c, stripe.Coupon))
        self.assertTrue(hasattr(c, 'percent_off'))
        self.assertTrue(hasattr(c, 'id'))

    def test_delete_coupon(self):
        c = stripe.Coupon.create(**DUMMY_COUPON)
        self.assertFalse(hasattr(c, 'deleted'))
        c.delete()
        self.assertFalse(hasattr(c, 'percent_off'))
        self.assertTrue(hasattr(c, 'id'))
        self.assertTrue(c.deleted)


class CustomerCouponTest(StripeTestCase):

    def setUp(self):
        super(CustomerCouponTest, self).setUp()
        self.coupon_obj = stripe.Coupon.create(**DUMMY_COUPON)

    def tearDown(self):
        self.coupon_obj.delete()

    def test_attach_coupon(self):
        customer = stripe.Customer.create(coupon=self.coupon_obj.id)
        self.assertTrue(hasattr(customer, 'discount'))
        self.assertNotEqual(None, customer.discount)

        customer.delete_discount()
        self.assertEqual(None, customer.discount)


class SubscriptionCouponTest(StripeTestCase):

    def setUp(self):
        super(SubscriptionCouponTest, self).setUp()
        self.plan_obj = stripe.Plan.create(**DUMMY_PLAN)
        self.coupon_obj = stripe.Coupon.create(**DUMMY_COUPON)

    def tearDown(self):
        self.coupon_obj.delete()

    def test_attach_coupon_to_subscription(self):
        customer = stripe.Customer.create(card=DUMMY_CARD)

        subscription = customer.subscriptions.create(
            plan=DUMMY_PLAN['id'], coupon=self.coupon_obj.id)

        self.assertTrue(hasattr(subscription, 'discount'))
        self.assertNotEqual(None, subscription.discount)

        subscription.delete_discount()
        self.assertEqual(None, subscription.discount)


class InvalidRequestErrorTest(StripeTestCase):

    def test_nonexistent_object(self):
        try:
            stripe.Charge.retrieve('invalid')
        except stripe.error.InvalidRequestError, e:
            self.assertEqual(404, e.http_status)
            self.assertTrue(isinstance(e.http_body, basestring))
            self.assertTrue(isinstance(e.json_body, dict))

    def test_invalid_data(self):
        try:
            stripe.Charge.create()
        except stripe.error.InvalidRequestError, e:
            self.assertEqual(400, e.http_status)
            self.assertTrue(isinstance(e.http_body, basestring))
            self.assertTrue(isinstance(e.json_body, dict))


class PlanTest(StripeTestCase):

    def setUp(self):
        super(PlanTest, self).setUp()
        try:
            stripe.Plan(DUMMY_PLAN['id']).delete()
        except stripe.error.InvalidRequestError:
            pass

    def test_create_plan(self):
        self.assertRaises(stripe.error.InvalidRequestError,
                          stripe.Plan.create, amount=2500)
        p = stripe.Plan.create(**DUMMY_PLAN)
        self.assertTrue(hasattr(p, 'amount'))
        self.assertTrue(hasattr(p, 'id'))
        self.assertEqual(DUMMY_PLAN['amount'], p.amount)
        p.delete()
        self.assertTrue(hasattr(p, 'deleted'))
        self.assertTrue(p.deleted)

    def test_update_plan(self):
        p = stripe.Plan.create(**DUMMY_PLAN)
        name = "New plan name"
        p.name = name
        p.save()
        self.assertEqual(name, p.name)
        p.delete()

    def test_update_plan_without_retrieving(self):
        p = stripe.Plan.create(**DUMMY_PLAN)

        name = 'updated plan name!'
        plan = stripe.Plan(p.id)
        plan.name = name

        # should only have name and id
        self.assertEqual(sorted(['id', 'name']), sorted(plan.keys()))
        plan.save()

        self.assertEqual(name, plan.name)
        # should load all the properties
        self.assertEqual(p.amount, plan.amount)
        p.delete()


class MetadataTest(StripeTestCase):

    def setUp(self):
        super(MetadataTest, self).setUp()
        self.initial_metadata = {
            'address': '77 Massachusetts Ave, Cambridge',
            'uuid': 'id'
        }

        charge = stripe.Charge.create(
            metadata=self.initial_metadata, **DUMMY_CHARGE)
        customer = stripe.Customer.create(
            metadata=self.initial_metadata, card=DUMMY_CARD)
        recipient = stripe.Recipient.create(
            metadata=self.initial_metadata, **DUMMY_RECIPIENT)
        transfer = stripe.Transfer.create(
            metadata=self.initial_metadata, **DUMMY_TRANSFER)

        self.support_metadata = [charge, customer, recipient, transfer]

    def test_noop_metadata(self):
        for obj in self.support_metadata:
            obj.description = 'test'
            obj.save()
            metadata = obj.retrieve(obj.id).metadata
            self.assertEqual(self.initial_metadata, metadata)

    def test_unset_metadata(self):
        for obj in self.support_metadata:
            obj.metadata = None
            expected_metadata = {}
            obj.save()
            metadata = obj.retrieve(obj.id).metadata
            self.assertEqual(expected_metadata, metadata)

    def test_whole_update(self):
        for obj in self.support_metadata:
            expected_metadata = {'txn_id': '3287423s34'}
            obj.metadata = expected_metadata.copy()
            obj.save()
            metadata = obj.retrieve(obj.id).metadata
            self.assertEqual(expected_metadata, metadata)

    def test_individual_delete(self):
        for obj in self.support_metadata:
            obj.metadata['uuid'] = None
            expected_metadata = {'address': self.initial_metadata['address']}
            obj.save()
            metadata = obj.retrieve(obj.id).metadata
            self.assertEqual(expected_metadata, metadata)

    def test_individual_update(self):
        for obj in self.support_metadata:
            obj.metadata['txn_id'] = 'abc'
            expected_metadata = {'txn_id': 'abc'}
            expected_metadata.update(self.initial_metadata)
            obj.save()
            metadata = obj.retrieve(obj.id).metadata
            self.assertEqual(expected_metadata, metadata)

    def test_combo_update(self):
        for obj in self.support_metadata:
            obj.metadata['txn_id'] = 'bar'
            obj.metadata = {'uid': '6735'}
            obj.save()
            metadata = obj.retrieve(obj.id).metadata
            self.assertEqual({'uid': '6735'}, metadata)

        for obj in self.support_metadata:
            obj.metadata = {'uid': '6735'}
            obj.metadata['foo'] = 'bar'
            obj.save()
            metadata = obj.retrieve(obj.id).metadata
            self.assertEqual({'uid': '6735', 'foo': 'bar'}, metadata)


if __name__ == '__main__':
    unittest.main()
