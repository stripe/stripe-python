from __future__ import absolute_import, division, print_function

import stripe
from tests.helper import (StripeTestCase)


TEST_RESOURCE_ID = 'card_123'


class CardTest(StripeTestCase):
    def construct_resource(self, **params):
        card_dict = {
            'id': TEST_RESOURCE_ID,
            'object': 'card',
            'metadata': {},
        }
        card_dict.update(params)
        return stripe.Card.construct_from(card_dict, stripe.api_key)

    def test_has_account_instance_url(self):
        resource = self.construct_resource(account='acct_123')
        self.assertEqual(
            '/v1/accounts/acct_123/external_accounts/%s' % TEST_RESOURCE_ID,
            resource.instance_url()
        )

    def test_has_customer_instance_url(self):
        resource = self.construct_resource(customer='cus_123')
        self.assertEqual(
            '/v1/customers/cus_123/sources/%s' % TEST_RESOURCE_ID,
            resource.instance_url()
        )

    def test_has_recipient_instance_url(self):
        resource = self.construct_resource(recipient='rp_123')
        self.assertEqual(
            '/v1/recipients/rp_123/cards/%s' % TEST_RESOURCE_ID,
            resource.instance_url()
        )

    # The previous tests already ensure that the request will be routed to the
    # correct URL, so we only test the API operations once.

    def test_is_not_retrievable(self):
        with self.assertRaises(NotImplementedError):
            stripe.Card.retrieve(TEST_RESOURCE_ID)

    def test_is_saveable(self):
        resource = self.construct_resource(customer='cus_123')
        resource.metadata['key'] = 'value'
        resource.save()
        self.assert_requested(
            'post',
            '/v1/customers/cus_123/sources/%s' % TEST_RESOURCE_ID
        )

    def test_is_not_modifiable(self):
        with self.assertRaises(NotImplementedError):
            stripe.Card.modify(
                TEST_RESOURCE_ID,
                metadata={'key': 'value'}
            )

    def test_is_deletable(self):
        resource = self.construct_resource(customer='cus_123')
        resource.delete()
        self.assert_requested(
            'delete',
            '/v1/customers/cus_123/sources/%s' % TEST_RESOURCE_ID
        )
