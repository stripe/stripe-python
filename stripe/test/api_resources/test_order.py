from __future__ import absolute_import, division, print_function

import stripe
from stripe.test.helper import StripeResourceTest


class OrderTest(StripeResourceTest):

    def test_list_orders(self):
        stripe.Order.list()
        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/orders',
            {}
        )

    def test_pay_order(self):
        order = stripe.Order(id="or_pay")
        order.pay()

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/orders/or_pay/pay',
            {},
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
