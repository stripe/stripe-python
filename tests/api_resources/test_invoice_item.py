import stripe


TEST_RESOURCE_ID = "ii_123"


class TestInvoiceItem(object):
    def test_is_listable(self, http_client_mock):
        resources = stripe.InvoiceItem.list()
        http_client_mock.assert_requested("get", path="/v1/invoiceitems")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.InvoiceItem)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.InvoiceItem.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/invoiceitems/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.InvoiceItem)

    def test_is_creatable(self, http_client_mock):
        resource = stripe.InvoiceItem.create(
            customer="cus_123", amount=123, currency="usd"
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/invoiceitems",
            post_data="customer=cus_123&amount=123&currency=usd",
        )
        assert isinstance(resource, stripe.InvoiceItem)

    def test_is_saveable(self, http_client_mock):
        resource = stripe.InvoiceItem.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        http_client_mock.assert_requested(
            "post",
            path="/v1/invoiceitems/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )

    def test_can_delete(self, http_client_mock):
        resource = stripe.InvoiceItem.delete(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "delete", path="/v1/invoiceitems/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    def test_is_modifiable(self, http_client_mock):
        resource = stripe.InvoiceItem.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/invoiceitems/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )
        assert isinstance(resource, stripe.InvoiceItem)

    def test_is_deletable(self, http_client_mock):
        resource = stripe.InvoiceItem.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        http_client_mock.assert_requested(
            "delete", path="/v1/invoiceitems/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True
