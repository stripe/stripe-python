import stripe
from stripe.test.helper import StripeResourceTest


class ApplicationFeeTest(StripeResourceTest):

    def test_list_application_fees(self):
        stripe.ApplicationFee.all()
        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/application_fees',
            {}
        )


class ApplicationFeeRefundTest(StripeResourceTest):

    def test_fetch_refund(self):
        fee = stripe.ApplicationFee.construct_from({
            'id': 'fee_get_refund',
            'refunds': {
                'object': 'list',
                'url': '/v1/application_fees/fee_get_refund/refunds',
            }
        }, 'api_key')

        fee.refunds.retrieve("ref_get")

        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/application_fees/fee_get_refund/refunds/ref_get',
            {},
            None
        )

    def test_list_refunds(self):
        fee = stripe.ApplicationFee.construct_from({
            'id': 'fee_get_refund',
            'refunds': {
                'object': 'list',
                'url': '/v1/application_fees/fee_get_refund/refunds',
            }
        }, 'api_key')

        fee.refunds.all()

        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/application_fees/fee_get_refund/refunds',
            {},
            None
        )

    def test_update_refund(self):
        refund = stripe.resource.ApplicationFeeRefund.construct_from({
            'id': "ref_update",
            'fee': "fee_update",
            'metadata': {},
        }, 'api_key')
        refund.metadata["key"] = "value"
        refund.save()

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/application_fees/fee_update/refunds/ref_update',
            {
                'metadata': {
                    'key': 'value',
                }
            },
            None
        )
