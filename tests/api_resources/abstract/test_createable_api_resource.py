from __future__ import absolute_import, division, print_function

import stripe
from tests.helper import StripeTestCase


class MyCreatable(stripe.api_resources.abstract.CreateableAPIResource):
    pass


class CreateableAPIResourceTests(StripeTestCase):

    def test_create(self):
        self.stub_request(
            'post',
            '/v1/mycreatables',
            {
                'object': 'charge',
                'foo': 'bar',
            },
            rheaders={'request-id': 'req_id'}
        )

        res = MyCreatable.create()

        self.assert_requested(
            'post',
            '/v1/mycreatables',
            {}
        )
        self.assertTrue(isinstance(res, stripe.Charge))
        self.assertEqual('bar', res.foo)

        self.assertTrue(res.last_response is not None)
        self.assertEqual('req_id', res.last_response.request_id)

    def test_idempotent_create(self):
        self.stub_request(
            'post',
            '/v1/mycreatables',
            {
                'object': 'charge',
                'foo': 'bar',
            },
            rheaders={'idempotency-key': 'foo'}
        )

        res = MyCreatable.create(idempotency_key='foo')

        self.assert_requested(
            'post',
            '/v1/mycreatables',
            {},
            {'Idempotency-Key': 'foo'}
        )
        self.assertTrue(isinstance(res, stripe.Charge))
        self.assertEqual('bar', res.foo)

        self.assertTrue(res.last_response is not None)
        self.assertEqual('foo', res.last_response.idempotency_key)
