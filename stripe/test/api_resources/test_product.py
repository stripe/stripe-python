from __future__ import absolute_import, division, print_function

import stripe
from stripe.test.helper import StripeResourceTest


class ProductTest(StripeResourceTest):

    def test_list_products(self):
        stripe.Product.list()
        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/products',
            {}
        )

    def test_delete_products(self):
        p = stripe.Product(id='product_to_delete')
        p.delete()

        self.requestor_mock.request.assert_called_with(
            'delete',
            '/v1/products/product_to_delete',
            {},
            None
        )
