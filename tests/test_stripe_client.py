from __future__ import absolute_import, division, print_function
import stripe


class TestGeneratedExamples(object):
    def test_customer_retrieve(self, request_mock):
        client = stripe.StripeClient()
        customer = client.v1_customers_retrieve("cus_xxxxxxxxxxxxx")
        request_mock.assert_requested("get", "/v1/customers/cus_xxxxxxxxxxxxx")
        assert customer.id is not None

    def test_llamas_create(self, mocker):
        client = stripe.StripeClient()
        mocker.patch("stripe.default_http_client.request_with_retries", return_value=("{}", 200, {}))
        llama = client.v1_llama_create({"name": "My llama"})
        stripe.default_http_client.request_with_retries.assert_called_once()
        method, abs_url, headers, post_data = stripe.default_http_client.request_with_retries.call_args[0]
        assert method == 'post'
        assert abs_url.endswith("/v1/llamas")
        assert headers["Content-Type"] == "application/json"
        assert post_data == "{\"name\": \"My llama\"}"

