import stripe


TEST_INVOICE_ID = "in_123"
TEST_LINE_ITEM_ID = "il_123"


class TestInvoiceLineItem(object):
    def test_deserialize(self):
        invoice = stripe.Invoice.retrieve(TEST_INVOICE_ID)
        assert isinstance(invoice.lines.data, list)
        assert isinstance(invoice.lines.data[0], stripe.InvoiceLineItem)

    def test_is_modifiable(self, http_client_mock):
        resource = stripe.InvoiceLineItem.modify(
            TEST_INVOICE_ID, TEST_LINE_ITEM_ID, metadata={"key": "value"}
        )

        http_client_mock.assert_requested(
            "post",
            path="/v1/invoices/%s/lines/%s"
            % (TEST_INVOICE_ID, TEST_LINE_ITEM_ID),
            post_data="metadata[key]=value",
        )
        assert isinstance(resource, stripe.InvoiceLineItem)
