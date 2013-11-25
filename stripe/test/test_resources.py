from stripe import StripeObject, StripeObjectEncoder

from stripe.test import StripeUnitTestCase, StripeApiTestCase
from stripe.test.helper import (MySingleton, MyListable, MyCreatable,
                                MyUpdateable, MyDeletable, MyComposite,
                                MyResource, SAMPLE_INVOICE)

from stripe import importer
json = importer.import_json()

class StripeObjectEncoderTests(StripeUnitTestCase):
    def test_encoder_returns_dict(self):
        obj = StripeObject.construct_from(SAMPLE_INVOICE, 'key')
        encoded_stripe_object = StripeObjectEncoder().default(obj)
        self.assertTrue(isinstance(encoded_stripe_object, dict),
                        "StripeObject encoded to %s" % (type(encoded_stripe_object),))


class StripeObjectTests(StripeUnitTestCase):
    def test_initializes_with_parameters(self):
        obj = StripeObject('foo', 'bar', myparam=5, yourparam='boo')

        self.assertEqual('foo', obj.id)
        self.assertEqual('bar', obj.api_key)

    def test_access(self):
        obj = StripeObject('myid', 'mykey', myparam=5)

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
        self.assertRaises(TypeError, obj.__delitem__, 'myattr')

    def test_refresh_from(self):
        obj = StripeObject.construct_from({
            'foo': 'bar',
            'trans': 'me',
        }, 'mykey')

        self.assertEqual('mykey', obj.api_key)
        self.assertEqual('bar', obj.foo)
        self.assertEqual('me', obj['trans'])

        obj.refresh_from({
            'foo': 'baz',
            'johnny': 5,
        }, 'key2')

        self.assertEqual(5, obj.johnny)
        self.assertEqual('baz', obj.foo)
        self.assertRaises(AttributeError, getattr, obj, 'trans')
        self.assertEqual('key2', obj.api_key)

        obj.refresh_from({
            'trans': 4,
            'metadata': { 'amount': 42 }
        }, 'key2', True)

        self.assertEqual('baz', obj.foo)
        self.assertEqual(4, obj.trans)
        self.assertEqual({ 'amount': 42 }, obj.previous_metadata)

    def test_refresh_from_nested_object(self):
        obj = StripeObject.construct_from(SAMPLE_INVOICE, 'key')

        self.assertEqual(1, len(obj.lines.subscriptions))
        self.assertTrue(isinstance(obj.lines.subscriptions[0], StripeObject))
        self.assertEqual('month', obj.lines.subscriptions[0].plan.interval)

    def test_to_dict(self):
        obj = StripeObject.construct_from(SAMPLE_INVOICE, 'key')

        res = obj.to_dict()

        self.check_nested_objects(res)
        self.check_invoice_data(res)

    def test_to_json(self):
        obj = StripeObject.construct_from(SAMPLE_INVOICE, 'key')

        self.check_invoice_data(json.loads(str(obj)))

    # Ensure no nested StripeObjects are returned
    def check_nested_objects(self, obj):
        if isinstance(obj, dict):
            for k, v in obj.iteritems():
                self.check_nested_objects(k)
                self.check_nested_objects(v)
        elif isinstance(obj, list):
            for v in obj:
                self.check_nested_objects(v)
        else:
            self.assertFalse(isinstance(obj, StripeObject),
                             "StripeObject %s still in to_dict result" % (repr(obj),))

    def check_invoice_data(self, data):
        # Check rough structure
        self.assertEqual(20, len(data.keys()))
        self.assertEqual(3, len(data['lines'].keys()))
        self.assertEqual(0, len(data['lines']['invoiceitems']))
        self.assertEqual(1, len(data['lines']['subscriptions']))

        # Check various data types
        self.assertEqual(1338238728, data['date'])
        self.assertEqual(None, data['next_payment_attempt'])
        self.assertEqual(False, data['livemode'])
        self.assertEqual('month',
                         data['lines']['subscriptions'][0]['plan']['interval'])



class APIResourceTests(StripeApiTestCase):
    def test_refreshes(self):
        pass

    def test_retrieves(self):
        pass

class SingletonAPIResourceTests(StripeApiTestCase):
    pass

class ListableAPIResourceTests(StripeApiTestCase):
    pass

class CreateableAPIResourceTests(StripeApiTestCase):
    pass

class UpdateableAPIResourceTests(StripeApiTestCase):
    pass

class DeletableAPIResourceTests(StripeApiTestCase):
    pass
