from __future__ import absolute_import, division, print_function

import stripe
from tests.helper import StripeTestCase


class MyListable(stripe.api_resources.abstract.ListableAPIResource):
    pass


class ListableAPIResourceTests(StripeTestCase):

    def test_all(self):
        self.stub_request(
            'get',
            '/v1/mylistables',
            {
                'object': 'list',
                'data': [
                    {
                        'object': 'charge',
                        'name': 'jose',
                    },
                    {
                        'object': 'charge',
                        'name': 'curly',
                    }
                ],
                'url': '/v1/charges',
                'has_more': False,
            },
            rheaders={'request-id': 'req_id'}
        )

        res = MyListable.list()
        self.assert_requested(
            'get',
            '/v1/mylistables',
            {}
        )
        self.assertEqual(2, len(res.data))
        self.assertTrue(all(isinstance(obj, stripe.Charge)
                            for obj in res.data))
        self.assertEqual('jose', res.data[0].name)
        self.assertEqual('curly', res.data[1].name)

        self.assertTrue(res.last_response is not None)
        self.assertEqual('req_id', res.last_response.request_id)
