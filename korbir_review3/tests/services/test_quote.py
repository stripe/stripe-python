from __future__ import absolute_import, division, print_function

import stripe


TEST_RESOURCE_ID = "qt_123"


class TestQuote(object):
    def test_is_listable(self, http_client_mock, stripe_mock_stripe_client):
        resources = stripe_mock_stripe_client.quotes.list()
        http_client_mock.assert_requested("get", path="/v1/quotes")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Quote)

    def test_is_retrievable(self, http_client_mock, stripe_mock_stripe_client):
        resource = stripe_mock_stripe_client.quotes.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/quotes/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Quote)

    def test_is_creatable(self, http_client_mock, stripe_mock_stripe_client):
        resource = stripe_mock_stripe_client.quotes.create(
            params={"customer": "cus_123"}
        )
        http_client_mock.assert_requested(
            "post", path="/v1/quotes", post_data="customer=cus_123"
        )
        assert isinstance(resource, stripe.Quote)

    def test_is_updateable(self, http_client_mock, stripe_mock_stripe_client):
        resource = stripe_mock_stripe_client.quotes.update(
            TEST_RESOURCE_ID, params={"metadata": {"key": "value"}}
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/quotes/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )
        assert isinstance(resource, stripe.Quote)

    def test_can_finalize_quote(
        self, http_client_mock, stripe_mock_stripe_client
    ):
        resource = stripe_mock_stripe_client.quotes.retrieve(TEST_RESOURCE_ID)
        resource = resource.finalize_quote()
        http_client_mock.assert_requested(
            "post", path="/v1/quotes/%s/finalize" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Quote)

    def test_can_finalize_quote_classmethod(
        self, http_client_mock, stripe_mock_stripe_client
    ):
        resource = stripe_mock_stripe_client.quotes.finalize_quote(
            TEST_RESOURCE_ID
        )
        http_client_mock.assert_requested(
            "post", path="/v1/quotes/%s/finalize" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Quote)

    def test_can_cancel(self, http_client_mock, stripe_mock_stripe_client):
        resource = stripe_mock_stripe_client.quotes.cancel(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "post", path="/v1/quotes/%s/cancel" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Quote)

    def test_can_accept(self, http_client_mock, stripe_mock_stripe_client):
        resource = stripe_mock_stripe_client.quotes.accept(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "post", path="/v1/quotes/%s/accept" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Quote)

    def test_can_list_line_items(
        self, http_client_mock, stripe_mock_stripe_client
    ):
        resources = stripe_mock_stripe_client.quotes.line_items.list(
            TEST_RESOURCE_ID
        )
        http_client_mock.assert_requested(
            "get", path="/v1/quotes/%s/line_items" % TEST_RESOURCE_ID
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.LineItem)

    def test_can_list_computed_upfront_line_items(
        self, http_client_mock, stripe_mock_stripe_client
    ):
        resources = (
            stripe_mock_stripe_client.quotes.computed_upfront_line_items.list(
                TEST_RESOURCE_ID
            )
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/quotes/%s/computed_upfront_line_items"
            % TEST_RESOURCE_ID,
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.LineItem)

    def test_can_pdf(
        self,
        file_stripe_mock_stripe_client,
        http_client_mock,
    ):
        stream = file_stripe_mock_stripe_client.quotes.pdf(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get",
            api_base=stripe.upload_api_base,
            path="/v1/quotes/%s/pdf" % TEST_RESOURCE_ID,
        )
        content = stream.io.read()
        assert content == b"Stripe binary response"
