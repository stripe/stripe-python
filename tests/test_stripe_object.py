from __future__ import absolute_import, division, print_function

import datetime
import pickle
from copy import copy, deepcopy
from mock import Mock

import stripe
from stripe import util, six
from tests.helper import StripeTestCase


SAMPLE_INVOICE = stripe.util.json.loads("""
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


class StripeObjectTests(StripeTestCase):

    def test_initializes_with_parameters(self):
        obj = stripe.stripe_object.StripeObject(
            'foo', 'bar', myparam=5, yourparam='boo')

        self.assertEqual('foo', obj.id)
        self.assertEqual('bar', obj.api_key)

    def test_access(self):
        obj = stripe.stripe_object.StripeObject('myid', 'mykey', myparam=5)

        # Empty
        self.assertRaises(AttributeError, getattr, obj, 'myattr')
        self.assertRaises(KeyError, obj.__getitem__, 'myattr')
        self.assertEqual('def', obj.get('myattr', 'def'))
        self.assertEqual(None, obj.get('myattr'))

        # Setters
        obj.myattr = 'myval'
        obj['myitem'] = 'itval'
        self.assertEqual('sdef', obj.setdefault('mydef', 'sdef'))

        # Getters
        self.assertEqual('myval', obj.setdefault('myattr', 'sdef'))
        self.assertEqual('myval', obj.myattr)
        self.assertEqual('myval', obj['myattr'])
        self.assertEqual('myval', obj.get('myattr'))

        self.assertEqual(['id', 'myattr', 'mydef', 'myitem'],
                         sorted(obj.keys()))
        self.assertEqual(['itval', 'myid', 'myval', 'sdef'],
                         sorted(obj.values()))

        # Illegal operations
        self.assertRaises(ValueError, setattr, obj, 'foo', '')

    def test_refresh_from(self):
        obj = stripe.stripe_object.StripeObject.construct_from({
            'foo': 'bar',
            'trans': 'me',
        }, 'mykey')

        self.assertEqual('mykey', obj.api_key)
        self.assertEqual('bar', obj.foo)
        self.assertEqual('me', obj['trans'])
        self.assertEqual(None, obj.stripe_version)
        self.assertEqual(None, obj.stripe_account)
        self.assertEqual(None, obj.last_response)

        last_response = Mock()
        obj.refresh_from(
            {
                'foo': 'baz',
                'johnny': 5,
            }, 'key2',
            stripe_version='2017-08-15',
            stripe_account='acct_foo',
            last_response=last_response
        )

        self.assertEqual(5, obj.johnny)
        self.assertEqual('baz', obj.foo)
        self.assertRaises(AttributeError, getattr, obj, 'trans')
        self.assertEqual('key2', obj.api_key)
        self.assertEqual('2017-08-15', obj.stripe_version)
        self.assertEqual('acct_foo', obj.stripe_account)
        self.assertEqual(last_response, obj.last_response)

        obj.refresh_from({
            'trans': 4,
            'metadata': {'amount': 42}
        }, 'key2', True)

        self.assertEqual('baz', obj.foo)
        self.assertEqual(4, obj.trans)

    def test_passing_nested_refresh(self):
        obj = stripe.stripe_object.StripeObject.construct_from({
            'foos': {
                'type': 'list',
                'data': [
                    {'id': 'nested'}
                ],
            }
        }, 'key', stripe_account='acct_foo')

        nested = obj.foos.data[0]

        self.assertEqual('key', obj.api_key)
        self.assertEqual('nested', nested.id)
        self.assertEqual('key', nested.api_key)
        self.assertEqual('acct_foo', nested.stripe_account)

    def test_refresh_from_nested_object(self):
        obj = stripe.stripe_object.StripeObject.construct_from(
            SAMPLE_INVOICE, 'key')

        self.assertEqual(1, len(obj.lines.subscriptions))
        self.assertTrue(
            isinstance(obj.lines.subscriptions[0],
                       stripe.stripe_object.StripeObject))
        self.assertEqual('month', obj.lines.subscriptions[0].plan.interval)

    def test_to_json(self):
        obj = stripe.stripe_object.StripeObject.construct_from(
            SAMPLE_INVOICE, 'key')

        self.check_invoice_data(util.json.loads(str(obj)))

    def check_invoice_data(self, data):
        # Check rough structure
        self.assertEqual(20, len(list(data.keys())))
        self.assertEqual(3, len(list(data['lines'].keys())))
        self.assertEqual(0, len(data['lines']['invoiceitems']))
        self.assertEqual(1, len(data['lines']['subscriptions']))

        # Check various data types
        self.assertEqual(1338238728, data['date'])
        self.assertEqual(None, data['next_payment_attempt'])
        self.assertEqual(False, data['livemode'])
        self.assertEqual('month',
                         data['lines']['subscriptions'][0]['plan']['interval'])

    def test_repr(self):
        obj = stripe.stripe_object.StripeObject(
            'foo', 'bar', myparam=5)

        obj['object'] = u'\u4e00boo\u1f00'
        obj.date = datetime.datetime.fromtimestamp(1511136000)

        res = repr(obj)

        if six.PY2:
            res = six.text_type(repr(obj), 'utf-8')

        self.assertTrue(u'<StripeObject \u4e00boo\u1f00' in res)
        self.assertTrue(u'id=foo' in res)
        self.assertTrue(u'"date": 1511136000' in res)

    def test_pickling(self):
        obj = stripe.stripe_object.StripeObject(
            'foo', 'bar', myparam=5)

        obj['object'] = 'boo'
        obj.refresh_from(
            {
                'fala': 'lalala',
                # ensures that empty strings are correctly unpickled in Py3
                'emptystring': '',
            },
            api_key='bar', partial=True
        )

        self.assertEqual('lalala', obj.fala)

        pickled = pickle.dumps(obj)
        newobj = pickle.loads(pickled)

        self.assertEqual('foo', newobj.id)
        self.assertEqual('bar', newobj.api_key)
        self.assertEqual('boo', newobj['object'])
        self.assertEqual('lalala', newobj.fala)
        self.assertEqual('', newobj.emptystring)

    def test_deletion(self):
        obj = stripe.stripe_object.StripeObject('id', 'key')

        obj.coupon = "foo"
        self.assertEqual('foo', obj.coupon)

        del obj.coupon
        self.assertRaises(AttributeError, getattr, obj, 'coupon')

        obj.refresh_from({'coupon': 'foo'}, api_key='bar', partial=True)
        self.assertEqual('foo', obj.coupon)

    def test_copy(self):
        nested = stripe.stripe_object.StripeObject.construct_from({
            'value': 'bar',
        }, 'mykey')
        obj = stripe.stripe_object.StripeObject.construct_from({
            'empty': '',
            'value': 'foo',
            'nested': nested,
        }, 'mykey', stripe_account='myaccount')

        copied = copy(obj)

        self.assertEqual('', copied.empty)
        self.assertEqual('foo', copied.value)
        self.assertEqual('bar', copied.nested.value)

        self.assertEqual('mykey', copied.api_key)
        self.assertEqual('myaccount', copied.stripe_account)

        # Verify that we're not deep copying nested values.
        self.assertEqual(id(nested), id(copied.nested))

    def test_deepcopy(self):
        nested = stripe.stripe_object.StripeObject.construct_from({
            'value': 'bar',
        }, 'mykey')
        obj = stripe.stripe_object.StripeObject.construct_from({
            'empty': '',
            'value': 'foo',
            'nested': nested,
        }, 'mykey', stripe_account='myaccount')

        copied = deepcopy(obj)

        self.assertEqual('', copied.empty)
        self.assertEqual('foo', copied.value)
        self.assertEqual('bar', copied.nested.value)

        self.assertEqual('mykey', copied.api_key)
        self.assertEqual('myaccount', copied.stripe_account)

        # Verify that we're actually deep copying nested values.
        self.assertNotEqual(id(nested), id(copied.nested))

    def test_serialize_empty_string_unsets(self):
        class SerializeToEmptyString(stripe.stripe_object.StripeObject):
            def serialize(self, previous):
                return ''

        nested = SerializeToEmptyString.construct_from({
            'value': 'bar',
        }, 'mykey')
        obj = stripe.stripe_object.StripeObject.construct_from({
            'nested': nested,
        }, 'mykey')

        self.assertEqual(obj.serialize(None), {'nested': ''})
