from __future__ import absolute_import, division, print_function

import stripe
from tests.helper import StripeTestCase


TEST_RESOURCE_ID = 'in_123'


class InvoiceTest(StripeTestCase):
    def test_is_listable(self):
        resources = stripe.Invoice.list()
        self.assert_requested(
            'get',
            '/v1/invoices'
        )
        self.assertIsInstance(resources.data, list)
        self.assertIsInstance(resources.data[0], stripe.Invoice)

    def test_is_retrievable(self):
        resource = stripe.Invoice.retrieve(TEST_RESOURCE_ID)
        self.assert_requested(
            'get',
            '/v1/invoices/%s' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.Invoice)

    def test_is_creatable(self):
        resource = stripe.Invoice.create(
            customer='cus_123'
        )
        self.assert_requested(
            'post',
            '/v1/invoices'
        )
        self.assertIsInstance(resource, stripe.Invoice)

    def test_is_saveable(self):
        resource = stripe.Invoice.retrieve(TEST_RESOURCE_ID)
        resource.metadata['key'] = 'value'
        resource.save()
        self.assert_requested(
            'post',
            '/v1/invoices/%s' % resource.id
        )

    def test_is_modifiable(self):
        resource = stripe.Invoice.modify(
            TEST_RESOURCE_ID,
            metadata={'key': 'value'}
        )
        self.assert_requested(
            'post',
            '/v1/invoices/%s' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.Invoice)

    def test_can_pay(self):
        resource = stripe.Invoice.retrieve(TEST_RESOURCE_ID)
        resource = resource.pay()
        self.assert_requested(
            'post',
            '/v1/invoices/%s/pay' % resource.id
        )
        self.assertIsInstance(resource, stripe.Invoice)

    def test_can_upcoming(self):
        resource = stripe.Invoice.upcoming()
        self.assert_requested(
            'get',
            '/v1/invoices/upcoming'
        )
        self.assertIsInstance(resource, stripe.Invoice)

    def test_can_upcoming_and_subscription_items(self):
        resource = stripe.Invoice.upcoming(
            subscription_items=[
                {"plan": "foo", "quantity": 3}
            ]
        )
        self.assert_requested(
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
        self.assertIsInstance(resource, stripe.Invoice)
