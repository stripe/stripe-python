import pickle
import sys

import stripe

from stripe.test.helper import (
    StripeUnitTestCase, StripeApiTestCase,
    MySingleton, MyListable, MyCreatable, MyUpdateable, MyDeletable,
    MyResource, SAMPLE_INVOICE)

from stripe import util


class StripeObjectTests(StripeUnitTestCase):

    def test_initializes_with_parameters(self):
        obj = stripe.resource.StripeObject(
            'foo', 'bar', myparam=5, yourparam='boo')

        self.assertEqual('foo', obj.id)
        self.assertEqual('bar', obj.api_key)

    def test_access(self):
        obj = stripe.resource.StripeObject('myid', 'mykey', myparam=5)

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
        obj = stripe.resource.StripeObject.construct_from({
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
            'metadata': {'amount': 42}
        }, 'key2', True)

        self.assertEqual('baz', obj.foo)
        self.assertEqual(4, obj.trans)
        self.assertEqual({'amount': 42}, obj._previous_metadata)

    def test_refresh_from_nested_object(self):
        obj = stripe.resource.StripeObject.construct_from(
            SAMPLE_INVOICE, 'key')

        self.assertEqual(1, len(obj.lines.subscriptions))
        self.assertTrue(
            isinstance(obj.lines.subscriptions[0],
                       stripe.resource.StripeObject))
        self.assertEqual('month', obj.lines.subscriptions[0].plan.interval)

    def test_to_json(self):
        obj = stripe.resource.StripeObject.construct_from(
            SAMPLE_INVOICE, 'key')

        self.check_invoice_data(util.json.loads(str(obj)))

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

    def test_repr(self):
        obj = stripe.resource.StripeObject(
            'foo', 'bar', myparam=5)

        obj['object'] = u'\u4e00boo\u1f00'

        res = repr(obj)

        if sys.version_info[0] < 3:
            res = unicode(repr(obj), 'utf-8')

        self.assertTrue(u'<StripeObject \u4e00boo\u1f00' in res)
        self.assertTrue(u'id=foo' in res)

    def test_pickling(self):
        obj = stripe.resource.StripeObject(
            'foo', 'bar', myparam=5)

        obj['object'] = 'boo'
        obj.refresh_from({'fala': 'lalala'}, api_key='bar', partial=True)

        self.assertEqual('lalala', obj.fala)

        pickled = pickle.dumps(obj)
        newobj = pickle.loads(pickled)

        self.assertEqual('foo', newobj.id)
        self.assertEqual('bar', newobj.api_key)
        self.assertEqual('boo', newobj['object'])
        self.assertEqual('lalala', newobj.fala)


class ListObjectTests(StripeApiTestCase):

    def setUp(self):
        super(ListObjectTests, self).setUp()

        self.lo = stripe.resource.ListObject.construct_from({
            'id': 'me',
            'url': '/my/path',
        }, 'mykey')

        self.mock_response([{
            'object': 'charge',
            'foo': 'bar',
        }])

    def assertResponse(self, res):
        self.assertTrue(isinstance(res[0], stripe.Charge))
        self.assertEqual('bar', res[0].foo)

    def test_all(self):
        res = self.lo.all(myparam='you')

        self.requestor_mock.request.assert_called_with(
            'get', '/my/path', {'myparam': 'you'})

        self.assertResponse(res)

    def test_create(self):
        res = self.lo.create(myparam='eter')

        self.requestor_mock.request.assert_called_with(
            'post', '/my/path', {'myparam': 'eter'})

        self.assertResponse(res)

    def test_retrieve(self):
        res = self.lo.retrieve('myid', myparam='cow')

        self.requestor_mock.request.assert_called_with(
            'get', '/my/path/myid', {'myparam': 'cow'})

        self.assertResponse(res)


class APIResourceTests(StripeApiTestCase):

    def test_retrieve_and_refresh(self):
        self.mock_response({
            'id': 'foo2',
            'bobble': 'scrobble',
        })

        res = MyResource.retrieve('foo*', myparam=5)

        url = '/v1/myresources/foo%2A'
        self.requestor_mock.request.assert_called_with(
            'get', url, {'myparam': 5}
        )

        self.assertEqual('scrobble', res.bobble)
        self.assertEqual('foo2', res.id)
        self.assertEqual('reskey', res.api_key)

        self.mock_response({
            'frobble': 5,
        })

        res = res.refresh()

        url = '/v1/myresources/foo2'
        self.requestor_mock.request.assert_called_with(
            'get', url, {'myparam': 5}
        )

        self.assertEqual(5, res.frobble)
        self.assertRaises(KeyError, res.__getitem__, 'bobble')

    def test_convert_to_stripe_object(self):
        sample = {
            'foo': 'bar',
            'adict': {
                'object': 'charge',
                'id': 42,
                'amount': 7,
            },
            'alist': [
                {
                    'object': 'customer',
                    'name': 'chilango'
                }
            ]
        }

        converted = stripe.resource.convert_to_stripe_object(sample, 'akey')

        # Types
        self.assertTrue(isinstance(converted, stripe.resource.StripeObject))
        self.assertTrue(isinstance(converted.adict, stripe.Charge))
        self.assertEqual(1, len(converted.alist))
        self.assertTrue(isinstance(converted.alist[0], stripe.Customer))

        # Values
        self.assertEqual('bar', converted.foo)
        self.assertEqual(42, converted.adict.id)
        self.assertEqual('chilango', converted.alist[0].name)

        # Stripping
        # TODO: We should probably be stripping out this property
        # self.assertRaises(AttributeError, getattr, converted.adict, 'object')


class SingletonAPIResourceTests(StripeApiTestCase):

    def test_retrieve(self):
        self.mock_response({
            'single': 'ton'
        })
        res = MySingleton.retrieve()

        self.requestor_mock.request.assert_called_with(
            'get', '/v1/mysingleton', {})

        self.assertEqual('ton', res.single)


class ListableAPIResourceTests(StripeApiTestCase):

    def test_all(self):
        self.mock_response([
            {
                'object': 'charge',
                'name': 'jose',
            },
            {
                'object': 'charge',
                'name': 'curly',
            }
        ])

        res = MyListable.all()

        self.requestor_mock.request.assert_called_with(
            'get', '/v1/mylistables', {})

        self.assertEqual(2, len(res))
        self.assertTrue(all(isinstance(obj, stripe.Charge) for obj in res))
        self.assertEqual('jose', res[0].name)
        self.assertEqual('curly', res[1].name)


class CreateableAPIResourceTests(StripeApiTestCase):

    def test_create(self):
        self.mock_response({
            'object': 'charge',
            'foo': 'bar',
        })

        res = MyCreatable.create()

        self.requestor_mock.request.assert_called_with(
            'post', '/v1/mycreatables', {})

        self.assertTrue(isinstance(res, stripe.Charge))
        self.assertEqual('bar', res.foo)


class UpdateableAPIResourceTests(StripeApiTestCase):

    def setUp(self):
        super(UpdateableAPIResourceTests, self).setUp()

        self.mock_response({
            'thats': 'it'
        })

        self.obj = MyUpdateable.construct_from({
            'id': 'myid',
            'foo': 'bar',
            'baz': 'boz',
            'metadata': {
                'size': 'l',
                'score': 4,
                'height': 10
            }
        }, 'mykey')

    def checkSave(self):
        self.assertTrue(self.obj is self.obj.save())

        self.assertEqual('it', self.obj.thats)
        # TODO: Should we force id to be retained?
        # self.assertEqual('myid', obj.id)
        self.assertRaises(AttributeError, getattr, self.obj, 'baz')

    def test_save(self):
        self.obj.baz = 'updated'
        self.obj.other = 'newval'
        self.obj.metadata.size = 'm'
        self.obj.metadata.info = 'a2'
        self.obj.metadata.height = None

        self.checkSave()

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/myupdateables/myid',
            {
                'baz': 'updated',
                'other': 'newval',
                'metadata': {
                    'size': 'm',
                    'info': 'a2',
                    'height': '',
                }
            }
        )

    def test_save_replace_metadata(self):
        self.obj.baz = 'updated'
        self.obj.other = 'newval'
        self.obj.metadata = {
            'size': 'm',
            'info': 'a2',
            'score': 4,
        }

        self.checkSave()

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/myupdateables/myid',
            {
                'baz': 'updated',
                'other': 'newval',
                'metadata': {
                    'size': 'm',
                    'info': 'a2',
                    'height': '',
                    'score': 4,
                }
            }
        )


class DeletableAPIResourceTests(StripeApiTestCase):

    def test_delete(self):
        self.mock_response({
            'id': 'mid',
            'deleted': True,
        })

        obj = MyDeletable.construct_from({
            'id': 'mid'
        }, 'mykey')

        self.assertTrue(obj is obj.delete())

        self.assertEqual(True, obj.deleted)
        self.assertEqual('mid', obj.id)
