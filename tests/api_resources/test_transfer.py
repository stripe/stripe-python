from __future__ import absolute_import, division, print_function

import stripe
from tests.helper import StripeTestCase


TEST_RESOURCE_ID = 'tr_123'
TEST_REVERSAL_ID = 'trr_123'


class TransferTest(StripeTestCase):
    def test_is_listable(self):
        resources = stripe.Transfer.list()
        self.assert_requested(
            'get',
            '/v1/transfers'
        )
        self.assertIsInstance(resources.data, list)
        self.assertIsInstance(resources.data[0], stripe.Transfer)

    def test_is_retrievable(self):
        resource = stripe.Transfer.retrieve(TEST_RESOURCE_ID)
        self.assert_requested(
            'get',
            '/v1/transfers/%s' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.Transfer)

    def test_is_creatable(self):
        resource = stripe.Transfer.create(
            amount=100,
            currency='usd',
            destination='acct_123'
        )
        self.assert_requested(
            'post',
            '/v1/transfers'
        )
        self.assertIsInstance(resource, stripe.Transfer)

    def test_is_saveable(self):
        resource = stripe.Transfer.retrieve(TEST_RESOURCE_ID)
        resource.metadata['key'] = 'value'
        resource.save()
        self.assert_requested(
            'post',
            '/v1/transfers/%s' % resource.id
        )

    def test_is_modifiable(self):
        resource = stripe.Transfer.modify(
            TEST_RESOURCE_ID,
            metadata={'key': 'value'}
        )
        self.assert_requested(
            'post',
            '/v1/transfers/%s' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.Transfer)

    def test_is_cancelable(self):
        # stripe-mock does not handle this anymore as it was on an old
        # API version so we stub instead.
        self.stub_request(
            'post',
            '/v1/transfers/%s/cancel' % TEST_RESOURCE_ID,
            {
                'id': '%s' % TEST_RESOURCE_ID,
                'object': 'transfer',
                'status': 'canceled'
            }
        )
        transfer = stripe.Transfer.construct_from({
            'id': '%s' % TEST_RESOURCE_ID,
            'object': 'transfer'
        }, stripe.api_key)
        transfer_canceled = transfer.cancel()
        self.assert_requested(
            'post',
            '/v1/transfers/%s/cancel' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(transfer_canceled, stripe.Transfer)


class TransferReversalTest(StripeTestCase):
    def test_is_listable(self):
        resources = stripe.Transfer.list_reversals(TEST_RESOURCE_ID)
        self.assert_requested(
            'get',
            '/v1/transfers/%s/reversals' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resources.data, list)
        self.assertIsInstance(resources.data[0], stripe.Reversal)

    def test_is_retrievable(self):
        resource = stripe.Transfer.retrieve_reversal(
            TEST_RESOURCE_ID,
            TEST_REVERSAL_ID
        )
        self.assert_requested(
            'get',
            '/v1/transfers/%s/reversals/%s' % (TEST_RESOURCE_ID,
                                               TEST_REVERSAL_ID)
        )
        self.assertIsInstance(resource, stripe.Reversal)

    def test_is_creatable(self):
        resource = stripe.Transfer.create_reversal(
            TEST_RESOURCE_ID,
            amount=100
        )
        self.assert_requested(
            'post',
            '/v1/transfers/%s/reversals' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.Reversal)

    def test_is_modifiable(self):
        resource = stripe.Transfer.modify_reversal(
            TEST_RESOURCE_ID,
            TEST_REVERSAL_ID,
            metadata={'foo': 'bar'}
        )
        self.assert_requested(
            'post',
            '/v1/transfers/%s/reversals/%s' % (TEST_RESOURCE_ID,
                                               TEST_REVERSAL_ID)
        )
        self.assertIsInstance(resource, stripe.Reversal)
