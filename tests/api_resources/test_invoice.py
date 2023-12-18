import stripe


TEST_RESOURCE_ID = "in_123"


class TestInvoice(object):
    def test_is_listable(self, http_client_mock):
        resources = stripe.Invoice.list()
        http_client_mock.assert_requested("get", path="/v1/invoices")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Invoice)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.Invoice.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/invoices/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Invoice)

    def test_is_creatable(self, http_client_mock):
        resource = stripe.Invoice.create(customer="cus_123")
        http_client_mock.assert_requested("post", path="/v1/invoices")
        assert isinstance(resource, stripe.Invoice)

    def test_is_saveable(self, http_client_mock):
        resource = stripe.Invoice.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        http_client_mock.assert_requested(
            "post", path="/v1/invoices/%s" % TEST_RESOURCE_ID
        )

    def test_is_modifiable(self, http_client_mock):
        resource = stripe.Invoice.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        http_client_mock.assert_requested(
            "post", path="/v1/invoices/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Invoice)

    def test_is_deletable(self, http_client_mock):
        resource = stripe.Invoice.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        http_client_mock.assert_requested(
            "delete", path="/v1/invoices/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    def test_can_delete(self, http_client_mock):
        resource = stripe.Invoice.delete(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "delete", path="/v1/invoices/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    def test_can_finalize_invoice(self, http_client_mock):
        resource = stripe.Invoice.retrieve(TEST_RESOURCE_ID)
        resource = resource.finalize_invoice()
        http_client_mock.assert_requested(
            "post", path="/v1/invoices/%s/finalize" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Invoice)

    def test_can_finalize_invoice_classmethod(self, http_client_mock):
        resource = stripe.Invoice.finalize_invoice(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "post", path="/v1/invoices/%s/finalize" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Invoice)

    def test_can_mark_uncollectible(self, http_client_mock):
        resource = stripe.Invoice.retrieve(TEST_RESOURCE_ID)
        resource = resource.mark_uncollectible()
        http_client_mock.assert_requested(
            "post",
            path="/v1/invoices/%s/mark_uncollectible" % TEST_RESOURCE_ID,
        )
        assert isinstance(resource, stripe.Invoice)

    def test_can_mark_uncollectible_classmethod(self, http_client_mock):
        resource = stripe.Invoice.mark_uncollectible(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "post",
            path="/v1/invoices/%s/mark_uncollectible" % TEST_RESOURCE_ID,
        )
        assert isinstance(resource, stripe.Invoice)

    def test_can_pay(self, http_client_mock):
        resource = stripe.Invoice.retrieve(TEST_RESOURCE_ID)
        resource = resource.pay()
        http_client_mock.assert_requested(
            "post", path="/v1/invoices/%s/pay" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Invoice)

    def test_can_pay_classmethod(self, http_client_mock):
        resource = stripe.Invoice.pay(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "post", path="/v1/invoices/%s/pay" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Invoice)

    def test_can_send_invoice(self, http_client_mock):
        resource = stripe.Invoice.retrieve(TEST_RESOURCE_ID)
        resource = resource.send_invoice()
        http_client_mock.assert_requested(
            "post", path="/v1/invoices/%s/send" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Invoice)

    def test_can_send_invoice_classmethod(self, http_client_mock):
        resource = stripe.Invoice.send_invoice(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "post", path="/v1/invoices/%s/send" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Invoice)

    def test_can_upcoming(self, http_client_mock):
        resource = stripe.Invoice.upcoming(customer="cus_123")
        http_client_mock.assert_requested("get", path="/v1/invoices/upcoming")
        assert isinstance(resource, stripe.Invoice)

    def test_can_void_invoice(self, http_client_mock):
        resource = stripe.Invoice.retrieve(TEST_RESOURCE_ID)
        resource = resource.void_invoice()
        http_client_mock.assert_requested(
            "post", path="/v1/invoices/%s/void" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Invoice)

    def test_can_void_invoice_classmethod(self, http_client_mock):
        resource = stripe.Invoice.void_invoice(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "post", path="/v1/invoices/%s/void" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Invoice)

    def test_can_iterate_lines(self):
        resource = stripe.Invoice.retrieve(TEST_RESOURCE_ID)
        assert isinstance(resource.lines.data, list)
        assert isinstance(resource.lines.data[0], stripe.InvoiceLineItem)
        seen = [item["id"] for item in resource.lines.auto_paging_iter()]

        assert seen.__len__() > 0
