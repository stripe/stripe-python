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


class OrderReturnTest(StripeResourceTest):

    def test_list_order_returns(self):
        stripe.OrderReturn.list()
        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/order_returns',
            {}
        )
