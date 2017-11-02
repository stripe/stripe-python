from __future__ import absolute_import, division, print_function

import stripe
from stripe.test.helper import StripeResourceTest


class SKUTest(StripeResourceTest):

    def test_list_skus(self):
        stripe.SKU.list()
        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/skus',
            {}
        )

    def test_delete_skus(self):
        sku = stripe.SKU(id='sku_delete')
        sku.delete()

        self.requestor_mock.request.assert_called_with(
            'delete',
            '/v1/skus/sku_delete',
            {},
            None
        )
