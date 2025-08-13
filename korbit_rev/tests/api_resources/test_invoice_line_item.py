import stripe


TEST_INVOICE_ID = "in_123"


class TestInvoiceLineItem(object):
    def test_deserialize(self):
        invoice = stripe.Invoice.retrieve(TEST_INVOICE_ID)
        assert isinstance(invoice.lines.data, list)
        assert isinstance(invoice.lines.data[0], stripe.InvoiceLineItem)
