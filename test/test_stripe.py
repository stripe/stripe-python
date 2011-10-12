# -*- coding: utf-8 -*-
import datetime
import os
import sys
import time
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import stripe

# dummy information used in the tests below
NOW = datetime.datetime.now()
DUMMY_CARD = {
    'number': '4242424242424242',
    'exp_month': NOW.month + 1,
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
    'id': 'gold'
}

class FunctionalTests(unittest.TestCase):
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
        plan_obj = stripe.Plan.create(**DUMMY_PLAN)
        customer = stripe.Customer.create(plan=DUMMY_PLAN['id'], card=DUMMY_CARD)
        self.assertEqual(customer['created'], customer.created)
        customer['foo'] = 'bar'
        self.assertEqual(customer.foo, 'bar')
        plan = stripe.Plan.retrieve(plan_obj.id)
        plan.delete()

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

class ChargeTest(unittest.TestCase):
    def test_create_uncaptured_charge(self):
        charge = stripe.Charge.create(uncaptured=True, **DUMMY_CHARGE)
        self.assertTrue(charge.paid)
        self.assertFalse(charge.refunded)
        self.assertTrue(charge.uncaptured)

    def test_create_uncaptured_charge_and_capture(self):
        charge = stripe.Charge.create(uncaptured=True, **DUMMY_CHARGE)
        charge.capture()
        self.assertTrue(charge.paid)
        self.assertFalse(charge.refunded)
        self.assertEqual(charge.get('uncaptured'), None)

class CustomerTest(unittest.TestCase):
    def test_create_plan(self):
        plan_obj = stripe.Plan.create(**DUMMY_PLAN)
        self.assertTrue(hasattr(plan_obj, 'amount'))
        self.assertEquals(DUMMY_PLAN['amount'], plan_obj.amount)
        plan = stripe.Plan.retrieve(plan_obj.id)
        self.assertFalse(hasattr(plan, 'deleted'))
        plan.delete()
        self.assertTrue(hasattr(plan, 'deleted'))
        self.assertTrue(plan.deleted)
    
    def test_create_customer(self):
        plan_obj = stripe.Plan.create(**DUMMY_PLAN)
        self.assertRaises(stripe.InvalidRequestError, stripe.Customer.create,
                          plan=DUMMY_PLAN['id'])
        customer = stripe.Customer.create(plan=DUMMY_PLAN['id'], card=DUMMY_CARD)
        self.assertTrue(hasattr(customer, 'subscription'))
        self.assertFalse(hasattr(customer, 'plan'))
        customer.delete()
        self.assertFalse(hasattr(customer, 'subscription'))
        self.assertFalse(hasattr(customer, 'plan'))
        self.assertTrue(customer.deleted)
        stripe.Plan.retrieve(plan_obj.id).delete()

    def test_list_customers(self):
        customers = stripe.Customer.all()
        self.assertTrue(isinstance(customers.data, list))

    def test_cancel_subscription(self):
        plan_obj = stripe.Plan.create(**DUMMY_PLAN)
        customer = stripe.Customer.create(plan=DUMMY_PLAN['id'],
                                          card=DUMMY_CARD)
        customer.cancel_subscription(at_period_end=True)
        self.assertEqual(customer.subscription.status, 'active')
        self.assertTrue(customer.subscription.cancel_at_period_end)
        customer.cancel_subscription()
        self.assertEqual(customer.subscription.status, 'canceled')
        plan = stripe.Plan.retrieve(plan_obj.id)
        plan.delete()

    def test_datetime_trial_end(self):
        plan_obj = stripe.Plan.create(**DUMMY_PLAN)
        customer = stripe.Customer.create(plan=DUMMY_PLAN['id'], card=DUMMY_CARD,
            trial_end=datetime.datetime.now()+datetime.timedelta(days=15))
        self.assertTrue(customer.id)
        plan = stripe.Plan.retrieve(plan_obj.id)
        plan.delete()

    def test_integer_trial_end(self):
        plan_obj = stripe.Plan.create(**DUMMY_PLAN)
        trial_end_dttm = datetime.datetime.now() + datetime.timedelta(days=15)
        trial_end_int = int(time.mktime(trial_end_dttm.timetuple()))
        customer = stripe.Customer.create(plan=DUMMY_PLAN['id'],
                                          card=DUMMY_CARD,
                                          trial_end=trial_end_int)
        self.assertTrue(customer.id)
        plan = stripe.Plan.retrieve(plan_obj.id)
        plan.delete()

class CouponTest(unittest.TestCase):
    def test_create_coupon(self):
        self.assertRaises(stripe.InvalidRequestError, stripe.Coupon.create, percent_off=25)
        c = stripe.Coupon.create(percent_off=25, duration='repeating', duration_in_months=5)
        self.assertTrue(hasattr(c, 'percent_off')) 
        self.assertTrue(hasattr(c, 'id')) 
        c.delete()
        self.assertFalse(hasattr(c, 'percent_off'))
        self.assertFalse(hasattr(c, 'id'))
        self.assertTrue(c.deleted)

if __name__ == '__main__':
    api_base = os.environ.get('STRIPE_API_BASE')
    if api_base:
        stripe.api_base = api_base
    api_key = os.environ['STRIPE_API_KEY']
    if api_key:
        stripe.api_key = api_key
    unittest.main()
