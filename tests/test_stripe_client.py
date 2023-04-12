from __future__ import absolute_import, division, print_function
import stripe


class TestGeneratedExamples(object):
    def test_customer_retrieve(self, request_mock):
        client = stripe.StripeClient()
        customer = client.v1_customers_retrieve("cus_xxxxxxxxxxxxx")
        request_mock.assert_requested("get", "/v1/customers/cus_xxxxxxxxxxxxx")
        assert customer.id is not None
