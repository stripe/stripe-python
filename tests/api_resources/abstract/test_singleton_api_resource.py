from __future__ import absolute_import, division, print_function

import stripe
from tests.helper import StripeTestCase


class MySingleton(stripe.api_resources.abstract.SingletonAPIResource):
    pass


class SingletonAPIResourceTests(StripeTestCase):

    def test_retrieve(self):
        self.stub_request(
            'get',
            '/v1/mysingleton',
            {
                'single': 'ton'
            },
            rheaders={'request-id': 'req_id'}
        )

        res = MySingleton.retrieve()

        self.assert_requested(
            'get',
            '/v1/mysingleton',
            {}
        )
        self.assertEqual('ton', res.single)
        self.assertTrue(res.last_response is not None)
        self.assertEqual('req_id', res.last_response.request_id)
