from __future__ import absolute_import, division, print_function

import stripe
from tests.helper import StripeTestCase


class MyDeletable(stripe.api_resources.abstract.DeletableAPIResource):
    pass


class DeletableAPIResourceTests(StripeTestCase):
    def test_delete(self):
        self.stub_request(
            'delete',
            '/v1/mydeletables/mid',
            {
                'id': 'mid',
                'deleted': True,
            }
        )

        obj = MyDeletable.construct_from({
            'id': 'mid'
        }, 'mykey')

        self.assertTrue(obj is obj.delete())
        self.assert_requested(
            'delete',
            '/v1/mydeletables/mid',
            {}
        )
        self.assertEqual(True, obj.deleted)
        self.assertEqual('mid', obj.id)
