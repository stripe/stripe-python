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
            }
        )

        res = MyCreatable.create()

        self.assert_requested(
            'post',
            '/v1/mycreatables',
            {}
        )
        self.assertTrue(isinstance(res, stripe.Charge))
        self.assertEqual('bar', res.foo)

    def test_idempotent_create(self):
        self.stub_request(
            'post',
            '/v1/mycreatables',
            {
                'object': 'charge',
                'foo': 'bar',
            }
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
