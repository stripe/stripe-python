# -*- coding: utf-8 -*-
import os
import sys
import unittest
import datetime
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import stripe

class FunctionalTests(unittest.TestCase):
    def test_dns_failure(self):
        api_base = stripe.api_base
        try:
            stripe.api_base = 'https://my-invalid-domain.ireallywontresolve/v1'
            self.assertRaises(stripe.APIConnectionError, stripe.Customer.create)
        finally:
            stripe.api_base = api_base

    def test_run(self):
        c = stripe.Charge.create(amount=100, currency='usd', card={ 'number' : '4242424242424242', 'exp_month' : 03, 'exp_year' : 2015 })
        self.assertFalse(c.refunded)
        c.refund()
        self.assertTrue(c.refunded)

    def test_refresh(self):
        c = stripe.Charge.create(amount=100, currency='usd', card={ 'number' : '4242424242424242', 'exp_month' : 03, 'exp_year' : 2015 })
        d = stripe.Charge.retrieve(c.id)
        self.assertEqual(d.created, c.created)

        d.junk = 'junk'
        d.refresh()
        self.assertRaises(AttributeError, lambda: d.junk)

    def test_list_accessors(self):
        c = stripe.Customer.create(plan='gold', card={ 'number' : '4242424242424242', 'exp_month' : 03, 'exp_year' : 2015 })
        self.assertEqual(c['created'], c.created)
        c['foo'] = 'bar'
        self.assertEqual(c.foo, 'bar')

    def test_raise(self):
        self.assertRaises(stripe.CardError, stripe.Charge.create, amount=100, currency='usd', card={ 'number' : '4242424242424241', 'exp_month' : 03, 'exp_year' : 2015 })

    def test_unicode(self):
        # Make sure unicode requests can be sent
        self.assertRaises(stripe.InvalidRequestError, stripe.Charge.retrieve, id=u'☃')

    def test_none_values(self):
        c = stripe.Customer.create(plan=None)
        self.assertTrue(c.id)

    def test_missing_id(self):
        customer = stripe.Customer()
        self.assertRaises(stripe.InvalidRequestError, customer.refresh)

class ChargeTest(unittest.TestCase):
    def test_create_uncaptured_charge(self):
        c = stripe.Charge.create(amount=100, currency='usd', card={ 'number' : '4242424242424242', 'exp_month' : 03, 'exp_year' : 2015 }, uncaptured=True)
        self.assertTrue(c.paid)
        self.assertFalse(c.refunded)
        self.assertTrue(c.uncaptured)

    def test_create_uncaptured_charge(self):
        c = stripe.Charge.create(amount=100, currency='usd', card={ 'number' : '4242424242424242', 'exp_month' : 03, 'exp_year' : 2015 }, uncaptured=True)
        c.capture()
        self.assertTrue(c.paid)
        self.assertFalse(c.refunded)
        self.assertEqual(c.get('uncaptured'), None)

class CustomerTest(unittest.TestCase):
    def test_create_customer(self):
        self.assertRaises(stripe.InvalidRequestError, stripe.Customer.create, plan='gold')
        c = stripe.Customer.create(plan='gold', card={ 'number' : '4242424242424242', 'exp_month' : 03, 'exp_year' : 2015 })
        self.assertTrue(hasattr(c, 'subscription'))
        self.assertFalse(hasattr(c, 'plan'))
        c.delete()
        self.assertFalse(hasattr(c, 'subscription'))
        self.assertFalse(hasattr(c, 'plan'))
        self.assertTrue(c.deleted)

    def test_list_customers(self):
        cs = stripe.Customer.all()
        self.assertTrue(isinstance(cs, list))

    def test_cancel_subscription(self):
        c = stripe.Customer.create(plan='gold', card={ 'number' : '4242424242424242', 'exp_month' : 03, 'exp_year' : 2015 })
        c.cancel_subscription(at_period_end=True)
        self.assertEqual(c.subscription.status, 'active')
        self.assertTrue(c.subscription.cancel_at_period_end)
        c.cancel_subscription()
        self.assertEqual(c.subscription.status, 'canceled')

    def test_datetime_trial_end(self):
        c = stripe.Customer.create(plan='gold', card={ 'number' : '4242424242424242', 'exp_month' : 03, 'exp_year' : 2015 }, trial_end=datetime.datetime.now()+datetime.timedelta(days=15))
        self.assertTrue(c.id)

    def test_integer_trial_end(self):
        trial_end_dttm = datetime.datetime.now() + datetime.timedelta(days=15)
        trial_end_int = int(time.mktime(trial_end_dttm.timetuple()))
        c = stripe.Customer.create(plan='gold', card={ 'number' : '4242424242424242', 'exp_month' : 03, 'exp_year' : 2015 }, trial_end=trial_end_int)
        self.assertTrue(c.id)

if __name__ == '__main__':
    api_base = os.environ.get('STRIPE_API_BASE')
    if api_base:
        stripe.api_base = api_base
    api_key = os.environ['STRIPE_API_KEY']
    if api_key:
        stripe.api_key = api_key
    unittest.main()
