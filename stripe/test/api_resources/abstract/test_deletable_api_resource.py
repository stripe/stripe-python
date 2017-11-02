from __future__ import absolute_import, division, print_function

import stripe
from stripe.test.helper import StripeApiTestCase


class MyDeletable(stripe.api_resources.abstract.DeletableAPIResource):
    pass


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
