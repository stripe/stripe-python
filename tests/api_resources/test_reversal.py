from __future__ import absolute_import, division, print_function

import stripe
from tests.helper import StripeTestCase


TEST_RESOURCE_ID = 'trr_123'


class ReversalTest(StripeTestCase):
    def construct_resource(self):
        reversal_dict = {
            'id': TEST_RESOURCE_ID,
            'object': 'reversal',
            'metadata': {},
            'transfer': 'tr_123'
        }
        return stripe.Reversal.construct_from(reversal_dict, stripe.api_key)

    def test_has_instance_url(self):
        resource = self.construct_resource()
        self.assertEqual(
            '/v1/transfers/tr_123/reversals/%s' % TEST_RESOURCE_ID,
            resource.instance_url()
        )

    def test_is_not_modifiable(self):
        with self.assertRaises(NotImplementedError):
            stripe.Reversal.modify(
                TEST_RESOURCE_ID,
                metadata={'key': 'value'}
            )

    def test_is_not_retrievable(self):
        with self.assertRaises(NotImplementedError):
            stripe.Reversal.retrieve(TEST_RESOURCE_ID)

    # We don't use stripe-mock as the reversal returned has a transfer id that
    # is different from the transfer used to access the reversal
    def test_is_saveable(self):
        resource = self.construct_resource()
        resource.metadata['key'] = 'value'
        resource.save()
        self.assert_requested(
            'post',
            '/v1/transfers/tr_123/reversals/%s' % TEST_RESOURCE_ID
        )
