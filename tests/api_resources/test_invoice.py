from __future__ import absolute_import, division, print_function

import stripe


TEST_RESOURCE_ID = 'in_123'


class TestInvoice(object):
    def test_is_listable(self, request_mock):
        resources = stripe.Invoice.list()
        request_mock.assert_requested(
            'get',
            '/v1/invoices'
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Invoice)

    def test_is_retrievable(self, request_mock):
        resource = stripe.Invoice.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            'get',
            '/v1/invoices/%s' % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Invoice)

    def test_is_creatable(self, request_mock):
        resource = stripe.Invoice.create(
            customer='cus_123'
        )
        request_mock.assert_requested(
            'post',
            '/v1/invoices'
        )
        assert isinstance(resource, stripe.Invoice)

    def test_is_saveable(self, request_mock):
        resource = stripe.Invoice.retrieve(TEST_RESOURCE_ID)
        resource.metadata['key'] = 'value'
        resource.save()
        request_mock.assert_requested(
            'post',
            '/v1/invoices/%s' % resource.id
        )

    def test_is_modifiable(self, request_mock):
        resource = stripe.Invoice.modify(
            TEST_RESOURCE_ID,
            metadata={'key': 'value'}
        )
        request_mock.assert_requested(
            'post',
            '/v1/invoices/%s' % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Invoice)

    def test_can_pay(self, request_mock):
        resource = stripe.Invoice.retrieve(TEST_RESOURCE_ID)
        resource = resource.pay()
        request_mock.assert_requested(
            'post',
            '/v1/invoices/%s/pay' % resource.id
        )
        assert isinstance(resource, stripe.Invoice)

    def test_can_upcoming(self, request_mock):
        resource = stripe.Invoice.upcoming()
        request_mock.assert_requested(
            'get',
            '/v1/invoices/upcoming'
        )
        assert isinstance(resource, stripe.Invoice)

    def test_can_upcoming_and_subscription_items(self, request_mock):
        resource = stripe.Invoice.upcoming(
            subscription_items=[
                {"plan": "foo", "quantity": 3}
            ]
        )
        request_mock.assert_requested(
            'get',
            '/v1/invoices/upcoming',
            {
                'subscription_items': {
                    "0": {
                        "plan": "foo",
                        "quantity": 3,
                    },
                },
            },
        )
        assert isinstance(resource, stripe.Invoice)
