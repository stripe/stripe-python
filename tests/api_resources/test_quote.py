import stripe
import pytest


TEST_RESOURCE_ID = "qt_123"


class TestQuote(object):
    @pytest.fixture(scope="function")
    def setup_upload_api_base(self):
        stripe.upload_api_base = stripe.api_base
        yield
        stripe.api_base = stripe.upload_api_base
        stripe.upload_api_base = "https://files.stripe.com"

    def test_is_listable(self, http_client_mock):
        resources = stripe.Quote.list()
        http_client_mock.assert_requested("get", path="/v1/quotes")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Quote)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.Quote.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/quotes/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Quote)

    def test_is_creatable(self, http_client_mock):
        resource = stripe.Quote.create(customer="cus_123")
        http_client_mock.assert_requested(
            "post", path="/v1/quotes", post_data="customer=cus_123"
        )
        assert isinstance(resource, stripe.Quote)

    def test_is_saveable(self, http_client_mock):
        resource = stripe.Quote.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        http_client_mock.assert_requested(
            "post",
            path="/v1/quotes/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )

    def test_is_modifiable(self, http_client_mock):
        resource = stripe.Quote.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/quotes/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )
        assert isinstance(resource, stripe.Quote)

    def test_can_finalize_quote(self, http_client_mock):
        resource = stripe.Quote.retrieve(TEST_RESOURCE_ID)
        resource = resource.finalize_quote()
        http_client_mock.assert_requested(
            "post", path="/v1/quotes/%s/finalize" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Quote)

    def test_can_finalize_quote_classmethod(self, http_client_mock):
        resource = stripe.Quote.finalize_quote(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "post", path="/v1/quotes/%s/finalize" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Quote)

    def test_can_cancel(self, http_client_mock):
        resource = stripe.Quote.retrieve(TEST_RESOURCE_ID)
        resource = resource.cancel()
        http_client_mock.assert_requested(
            "post", path="/v1/quotes/%s/cancel" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Quote)

    def test_can_cancel_classmethod(self, http_client_mock):
        resource = stripe.Quote.cancel(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "post", path="/v1/quotes/%s/cancel" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Quote)

    def test_can_accept(self, http_client_mock):
        resource = stripe.Quote.retrieve(TEST_RESOURCE_ID)
        resource = resource.accept()
        http_client_mock.assert_requested(
            "post", path="/v1/quotes/%s/accept" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Quote)

    def test_can_accept_classmethod(self, http_client_mock):
        resource = stripe.Quote.accept(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "post", path="/v1/quotes/%s/accept" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Quote)

    def test_can_list_line_items(self, http_client_mock):
        resources = stripe.Quote.list_line_items(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/quotes/%s/line_items" % TEST_RESOURCE_ID
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.LineItem)

    def test_can_list_line_items_classmethod(self, http_client_mock):
        resources = stripe.Quote.list_line_items(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/quotes/%s/line_items" % TEST_RESOURCE_ID
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.LineItem)

    def test_can_list_computed_upfront_line_items(self, http_client_mock):
        resources = stripe.Quote.list_computed_upfront_line_items(
            TEST_RESOURCE_ID
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/quotes/%s/computed_upfront_line_items"
            % TEST_RESOURCE_ID,
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.LineItem)

    def test_can_list_computed_upfront_line_items_classmethod(
        self, http_client_mock
    ):
        resources = stripe.Quote.list_computed_upfront_line_items(
            TEST_RESOURCE_ID
        )
        http_client_mock.assert_requested(
            "get",
            path="/v1/quotes/%s/computed_upfront_line_items"
            % TEST_RESOURCE_ID,
        )
        assert isinstance(resources.data[0], stripe.LineItem)

    def test_can_pdf(self, setup_upload_api_base, http_client_mock_streaming):
        resource = stripe.Quote.retrieve(TEST_RESOURCE_ID)
        stream = resource.pdf()
        http_client_mock_streaming.assert_requested(
            "get",
            api_base=stripe.upload_api_base,
            path="/v1/quotes/%s/pdf" % TEST_RESOURCE_ID,
        )
        content = stream.io.read()
        assert content == b"Stripe binary response"

    def test_can_pdf_classmethod(
        self, setup_upload_api_base, http_client_mock_streaming
    ):
        stream = stripe.Quote.pdf(TEST_RESOURCE_ID)
        http_client_mock_streaming.assert_requested(
            "get",
            api_base=stripe.upload_api_base,
            path="/v1/quotes/%s/pdf" % TEST_RESOURCE_ID,
        )
        content = stream.io.read()
        assert content == b"Stripe binary response"
