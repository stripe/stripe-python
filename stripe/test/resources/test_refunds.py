import stripe
from stripe.test.helper import StripeResourceTest


class RefundTest(StripeResourceTest):

    def test_create_refund(self):
        stripe.Refund.create(charge='ch_foo')

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/refunds',
            {'charge': 'ch_foo'},
            None
        )

    def test_fetch_refund(self):
        stripe.Refund.retrieve('re_foo')

        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/refunds/re_foo',
            {},
            None
        )

    def test_list_refunds(self):
        stripe.Refund.list(limit=3, charge='ch_foo')

        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/refunds',
            {'limit': 3, 'charge': 'ch_foo'}
        )

    def test_update_refund(self):
        refund = stripe.resource.Refund.construct_from({
            'id': "ref_update",
            'charge': "ch_update",
            'metadata': {},
        }, 'api_key')
        refund.metadata["key"] = "value"
        refund.save()

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/refunds/ref_update',
            {
                'metadata': {
                    'key': 'value',
                }
            },
            None
        )


class ChargeRefundTest(StripeResourceTest):

    def test_create_refund(self):
        charge = stripe.Charge.construct_from({
            'id': 'ch_foo',
            'refunds': {
                'object': 'list',
                'url': '/v1/charges/ch_foo/refunds',
            }
        }, 'api_key')

        charge.refunds.create()

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/charges/ch_foo/refunds',
            {},
            None
        )

    def test_non_recursive_save(self):
        charge = stripe.Charge.construct_from({
            'id': 'ch_nested_update',
            'customer': {
                'object': 'customer',
                'description': 'foo',
            },
            'refunds': {
                'object': 'list',
                'url': '/v1/charges/ch_foo/refunds',
                'data': [{
                    'id': 'ref_123',
                }],
            },
        }, 'api_key')

        charge.customer.description = 'bar'
        charge.refunds.has_more = True
        charge.refunds.data[0].description = 'bar'
        charge.save()

        # Note: ideally, we'd want the library to NOT issue requests in this
        # case (i.e. the assert should actually be `assert_not_called()`).
        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/charges/ch_nested_update',
            {'refunds': {'has_more': True}},
            None
        )

    def test_fetch_refund(self):
        charge = stripe.Charge.construct_from({
            'id': 'ch_get_refund',
            'refunds': {
                'object': 'list',
                'url': '/v1/charges/ch_get_refund/refunds',
            }
        }, 'api_key')

        charge.refunds.retrieve("ref_get")

        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/charges/ch_get_refund/refunds/ref_get',
            {},
            None
        )

    def test_list_refunds(self):
        charge = stripe.Charge.construct_from({
            'id': 'ch_get_refund',
            'refunds': {
                'object': 'list',
                'url': '/v1/charges/ch_get_refund/refunds',
            }
        }, 'api_key')

        charge.refunds.list()

        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/charges/ch_get_refund/refunds',
            {},
            None
        )

    def test_update_refund(self):
        refund = stripe.resource.Refund.construct_from({
            'id': "ref_update",
            'charge': "ch_update",
            'metadata': {},
        }, 'api_key')
        refund.metadata["key"] = "value"
        refund.save()

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/refunds/ref_update',
            {
                'metadata': {
                    'key': 'value',
                }
            },
            None
        )
