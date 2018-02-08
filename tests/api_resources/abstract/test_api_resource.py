from __future__ import absolute_import, division, print_function

import stripe
from tests.helper import StripeTestCase


class MyResource(stripe.api_resources.abstract.APIResource):
    pass


class APIResourceTests(StripeTestCase):

    def test_retrieve_and_refresh(self):
        url = '/v1/myresources/foo%2A'
        self.stub_request(
            'get',
            url,
            {
                'id': 'foo2',
                'bobble': 'scrobble',
            },
            rheaders={'request-id': 'req_id'}
        )

        res = MyResource.retrieve('foo*', myparam=5)

        self.assert_requested(
            'get',
            url,
            {
                'myparam': 5,
            },
            None
        )
        self.assertEqual('scrobble', res.bobble)
        self.assertEqual('foo2', res.id)
        self.assertEqual('sk_test_123', res.api_key)

        self.assertTrue(res.last_response is not None)
        self.assertEqual('req_id', res.last_response.request_id)

        url = '/v1/myresources/foo2'
        self.stub_request(
            'get',
            url,
            {
                'frobble': 5,
            }
        )

        res = res.refresh()

        self.assert_requested(
            'get',
            url,
            {
                'myparam': 5,
            },
            None
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

        converted = stripe.util.convert_to_stripe_object(
            sample, 'akey', None, None)

        # Types
        self.assertTrue(isinstance(converted,
                                   stripe.stripe_object.StripeObject))
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

    def test_convert_array_to_dict(self):
        out = stripe.util.convert_array_to_dict([{"foo": "bar"}])
        self.assertEqual({"0": {"foo": "bar"}}, out)
        self.assertEqual({"f": "b"},
                         stripe.util.convert_array_to_dict({"f": "b"}))

    def test_raise_on_incorrect_id_type(self):
        for obj in [None, 1, 3.14, dict(), list(), set(), tuple(), object()]:
            self.assertRaises(stripe.error.InvalidRequestError,
                              MyResource.retrieve, obj)
