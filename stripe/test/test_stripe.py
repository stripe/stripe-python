# -*- coding: utf-8 -*-
import datetime
import os
import string
import sys
import time
import random
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))
import stripe
from stripe import importer
json = importer.import_json()

# dummy information used in the tests below
NOW = datetime.datetime.now()

DUMMY_CARD = {
    'number': '4242424242424242',
    'exp_month': NOW.month,
    'exp_year': NOW.year + 4
}
DUMMY_CHARGE = {
    'amount': 100,
    'currency': 'usd',
    'card': DUMMY_CARD
}

DUMMY_PLAN = {
    'amount': 2000,
    'interval': 'month',
    'name': 'Amazing Gold Plan',
    'currency': 'usd',
    'id': 'stripe-test-gold-' + ''.join(random.choice(string.ascii_lowercase) for x in range(10))
}

DUMMY_COUPON = {
    'percent_off': 25,
    'duration': 'repeating',
    'duration_in_months': 5
}

DUMMY_RECIPIENT = {
    'name': 'John Doe',
    'type': 'individual'
}

DUMMY_TRANSFER = {
    'amount': 400,
    'currency': 'usd',
    'recipient': 'self'
}

SAMPLE_INVOICE = json.loads("""
{
  "amount_due": 1305,
  "attempt_count": 0,
  "attempted": true,
  "charge": "ch_wajkQ5aDTzFs5v",
  "closed": true,
  "customer": "cus_osllUe2f1BzrRT",
  "date": 1338238728,
  "discount": null,
  "ending_balance": 0,
  "id": "in_t9mHb2hpK7mml1",
  "livemode": false,
  "next_payment_attempt": null,
  "object": "invoice",
  "paid": true,
  "period_end": 1338238728,
  "period_start": 1338238716,
  "starting_balance": -8695,
  "subtotal": 10000,
  "total": 10000,
  "lines": {
    "invoiceitems": [],
    "prorations": [],
    "subscriptions": [
      {
        "plan": {
          "interval": "month",
          "object": "plan",
          "identifier": "expensive",
          "currency": "usd",
          "livemode": false,
          "amount": 10000,
          "name": "Expensive Plan",
          "trial_period_days": null,
          "id": "expensive"
        },
        "period": {
          "end": 1340917128,
          "start": 1338238728
        },
        "amount": 10000
      }
    ]
  }
}
""")

class StripeTestCase(unittest.TestCase):
    def setUp(self):
        super(StripeTestCase, self).setUp()

        api_base = os.environ.get('STRIPE_API_BASE')
        if api_base:
            stripe.api_base = api_base
        stripe.api_key = os.environ.get('STRIPE_API_KEY', 'tGN0bIwXnHdwOa85VABjPdSn8nWY7G7I')

class StripeObjectTests(StripeTestCase):
    def test_to_dict_doesnt_return_objects(self):
        invoice = stripe.Invoice.construct_from(SAMPLE_INVOICE, stripe.api_key)

        def check_object(obj):
            if isinstance(obj, dict):
                for k, v in obj.iteritems():
                    check_object(k)
                    check_object(v)
            elif isinstance(obj, list):
                for v in obj:
                    check_object(v)
            else:
                self.assertFalse(isinstance(obj, stripe.StripeObject),
                                 "StripeObject %s still in to_dict result" % (repr(obj),))
        check_object(invoice.to_dict())

class StripeObjectEncoderTests(StripeTestCase):
    def test_encoder_returns_dict(self):
        invoice = stripe.Invoice.construct_from(SAMPLE_INVOICE, stripe.api_key)
        encoded_stripe_object = stripe.StripeObjectEncoder().default(invoice)
        self.assertTrue(isinstance(encoded_stripe_object, dict),
                        "StripeObject encoded to %s" % (type(encoded_stripe_object),))

class FunctionalTests(StripeTestCase):
    def test_dns_failure(self):
        api_base = stripe.api_base
        try:
            stripe.api_base = 'https://my-invalid-domain.ireallywontresolve/v1'
            self.assertRaises(stripe.APIConnectionError, stripe.Customer.create)
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
        self.assertRaises(stripe.CardError, stripe.Charge.create, amount=100,
                          currency='usd', card=EXPIRED_CARD)

    def test_unicode(self):
        # Make sure unicode requests can be sent
        self.assertRaises(stripe.InvalidRequestError, stripe.Charge.retrieve,
                          id=u'☃')

    def test_none_values(self):
        customer = stripe.Customer.create(plan=None)
        self.assertTrue(customer.id)

    def test_missing_id(self):
        customer = stripe.Customer()
        self.assertRaises(stripe.InvalidRequestError, customer.refresh)

class AuthenticationErrorTest(StripeTestCase):
    def test_invalid_credentials(self):
        key = stripe.api_key
        try:
            stripe.api_key = 'invalid'
            stripe.Customer.create()
        except stripe.AuthenticationError, e:
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
        except stripe.CardError, e:
            self.assertEqual(402, e.http_status)
            self.assertTrue(isinstance(e.http_body, basestring))
            self.assertTrue(isinstance(e.json_body, dict))

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

class CustomerTest(StripeTestCase):
    def test_list_customers(self):
        customers = stripe.Customer.all()
        self.assertTrue(isinstance(customers.data, list))

    def test_unset_description(self):
        customer = stripe.Customer.create(description="foo bar")

        customer.description = None
        customer.save()

        self.assertEqual(None, customer.retrieve(customer.id).description)

    def test_cannot_set_empty_string(self):
        customer = stripe.Customer()
        self.assertRaises(ValueError, setattr, customer, "description", "")

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

class CustomerPlanTest(StripeTestCase):
    def setUp(self):
        super(CustomerPlanTest, self).setUp()
        try:
            self.plan_obj = stripe.Plan.create(**DUMMY_PLAN)
        except stripe.InvalidRequestError:
            self.plan_obj = None

    def tearDown(self):
        if self.plan_obj:
            try:
                self.plan_obj.delete()
            except stripe.InvalidRequestError:
                pass
        super(CustomerPlanTest, self).tearDown()

    def test_create_customer(self):
        self.assertRaises(stripe.InvalidRequestError, stripe.Customer.create,
                          plan=DUMMY_PLAN['id'])
        customer = stripe.Customer.create(plan=DUMMY_PLAN['id'], card=DUMMY_CARD)
        self.assertTrue(hasattr(customer, 'subscription'))
        self.assertFalse(hasattr(customer, 'plan'))
        customer.delete()
        self.assertFalse(hasattr(customer, 'subscription'))
        self.assertFalse(hasattr(customer, 'plan'))
        self.assertTrue(customer.deleted)

    def test_cancel_subscription(self):
        customer = stripe.Customer.create(plan=DUMMY_PLAN['id'],
                                          card=DUMMY_CARD)
        customer.cancel_subscription(at_period_end=True)
        self.assertEqual(customer.subscription.status, 'active')
        self.assertTrue(customer.subscription.cancel_at_period_end)
        customer.cancel_subscription()
        self.assertEqual(customer.subscription.status, 'canceled')

    def test_datetime_trial_end(self):
        customer = stripe.Customer.create(plan=DUMMY_PLAN['id'], card=DUMMY_CARD,
            trial_end=datetime.datetime.now()+datetime.timedelta(days=15))
        self.assertTrue(customer.id)

    def test_integer_trial_end(self):
        trial_end_dttm = datetime.datetime.now() + datetime.timedelta(days=15)
        trial_end_int = int(time.mktime(trial_end_dttm.timetuple()))
        customer = stripe.Customer.create(plan=DUMMY_PLAN['id'],
                                          card=DUMMY_CARD,
                                          trial_end=trial_end_int)
        self.assertTrue(customer.id)

class CouponTest(StripeTestCase):
    def test_create_coupon(self):
        self.assertRaises(stripe.InvalidRequestError, stripe.Coupon.create, percent_off=25)
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

        customer.delete()

class InvalidRequestErrorTest(StripeTestCase):
    def test_nonexistent_object(self):
        try:
            stripe.Charge.retrieve('invalid')
        except stripe.InvalidRequestError, e:
            self.assertEqual(404, e.http_status)
            self.assertTrue(isinstance(e.http_body, basestring))
            self.assertTrue(isinstance(e.json_body, dict))

    def test_invalid_data(self):
        try:
            stripe.Charge.create()
        except stripe.InvalidRequestError, e:
            self.assertEqual(400, e.http_status)
            self.assertTrue(isinstance(e.http_body, basestring))
            self.assertTrue(isinstance(e.json_body, dict))

class PlanTest(StripeTestCase):
    def setUp(self):
        super(PlanTest, self).setUp()
        try:
            stripe.Plan(DUMMY_PLAN['id']).delete()
        except stripe.InvalidRequestError:
            pass

    def test_create_plan(self):
        self.assertRaises(stripe.InvalidRequestError, stripe.Plan.create, amount=2500)
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

        self.assertEqual(sorted(['id', 'name']), sorted(plan.keys())) # should only have name and id
        plan.save()

        self.assertEqual(name, plan.name)
        self.assertEqual(p.amount, plan.amount) # should load all the properties
        p.delete()

class MetadataTest(StripeTestCase):
    def setUp(self):
        super(MetadataTest, self).setUp()
        self.initial_metadata = {
            'address': '77 Massachusetts Ave, Cambridge',
            'uuid': 'id'
        }

        charge = stripe.Charge.create(metadata=self.initial_metadata, **DUMMY_CHARGE)
        customer = stripe.Customer.create(metadata=self.initial_metadata, card=DUMMY_CARD)
        recipient = stripe.Recipient.create(metadata=self.initial_metadata, **DUMMY_RECIPIENT)
        transfer = stripe.Transfer.create(metadata=self.initial_metadata, **DUMMY_TRANSFER)

        self.support_metadata = [charge, customer, recipient, transfer]

    def test_noop_metadata(self):
        for obj in self.support_metadata:
            obj.description = 'test'
            obj.save()
            metadata = obj.retrieve(obj.id).metadata
            self.assertEqual(self.initial_metadata, metadata.to_dict())

    def test_unset_metadata(self):
        for obj in self.support_metadata:
            obj.metadata = None
            expected_metadata = {}
            obj.save()
            metadata = obj.retrieve(obj.id).metadata
            self.assertEqual(expected_metadata, metadata.to_dict())

    def test_whole_update(self):
        for obj in self.support_metadata:
            expected_metadata = {'txn_id': '3287423s34'}
            obj.metadata = expected_metadata.copy()
            obj.save()
            metadata = obj.retrieve(obj.id).metadata
            self.assertEqual(expected_metadata, metadata.to_dict())

    def test_individual_delete(self):
        for obj in self.support_metadata:
            obj.metadata['uuid'] = None
            expected_metadata = {'address': self.initial_metadata['address']}
            obj.save()
            metadata = obj.retrieve(obj.id).metadata
            self.assertEqual(expected_metadata, metadata.to_dict())

    def test_individual_update(self):
        for obj in self.support_metadata:
            obj.metadata['txn_id'] = 'abc'
            expected_metadata = {'txn_id': 'abc'}
            expected_metadata.update(self.initial_metadata)
            obj.save()
            metadata = obj.retrieve(obj.id).metadata
            self.assertEqual(expected_metadata, metadata.to_dict())

    def test_combo_update(self):
        for obj in self.support_metadata:
            obj.metadata['txn_id'] = 'bar'
            obj.metadata = {'uid': '6735'}
            obj.save()
            metadata = obj.retrieve(obj.id).metadata
            self.assertEqual({'uid': '6735'}, metadata.to_dict())

        for obj in self.support_metadata:
            obj.metadata = {'uid': '6735'}
            obj.metadata['foo'] = 'bar'
            obj.save()
            metadata = obj.retrieve(obj.id).metadata
            self.assertEqual({'uid': '6735', 'foo': 'bar'}, metadata.to_dict())


if __name__ == '__main__':
    unittest.main()
