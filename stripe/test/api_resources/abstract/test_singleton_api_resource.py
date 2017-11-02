from __future__ import absolute_import, division, print_function

import stripe
from stripe.test.helper import StripeApiTestCase


class MySingleton(stripe.api_resources.abstract.SingletonAPIResource):
    pass


class SingletonAPIResourceTests(StripeApiTestCase):

    def test_retrieve(self):
        self.mock_response({
            'single': 'ton'
        })
        res = MySingleton.retrieve()

        self.requestor_mock.request.assert_called_with(
            'get', '/v1/mysingleton', {}, None)

        self.assertEqual('ton', res.single)
