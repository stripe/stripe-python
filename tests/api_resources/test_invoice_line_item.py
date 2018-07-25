from __future__ import absolute_import, division, print_function

import stripe


TEST_INVOICE_ID = 'in_123'


class TestInvoiceLineItem(object):
    def test_deserialize(self, request_mock):
        invoice = stripe.Invoice.retrieve(TEST_INVOICE_ID)
        assert isinstance(invoice.lines.data, list)
        assert isinstance(invoice.lines.data[0], stripe.InvoiceLineItem)
