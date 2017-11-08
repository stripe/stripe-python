from __future__ import absolute_import, division, print_function

import stripe
from tests.helper import StripeResourceTest


class OrderTest(StripeResourceTest):

    def test_list_orders(self):
        stripe.Order.list()
        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/orders',
            {}
        )

    def test_pay_order(self):
        self.mock_response({
            'id': 'or_pay',
            'status': 'paid',
        })

        order = stripe.Order(id="or_pay")

        self.assertTrue(order is order.pay())
        self.assertEquals('paid', order.status)
        self.assertEquals('or_pay', order.id)

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/orders/or_pay/pay',
            {},
            None
        )

    def test_pay_order_with_params(self):
        self.mock_response({
            'id': 'or_pay',
            'status': 'paid',
        })

        order = stripe.Order(id="or_pay")

        self.assertTrue(order is order.pay(source="src_foo"))
        self.assertEquals('paid', order.status)
        self.assertEquals('or_pay', order.id)

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/orders/or_pay/pay',
            {
                'source': 'src_foo',
            },
            None
        )

    def test_return_order(self):
        order = stripe.Order(id="or_return")
        order.return_order()

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/orders/or_return/returns',
            {},
            None
        )
