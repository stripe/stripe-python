from __future__ import absolute_import, division, print_function

import stripe
from tests.helper import (StripeTestCase)


TEST_RESOURCE_ID = 'ba_123'


class BankAccountTest(StripeTestCase):
    def construct_resource(self, **params):
        bank_dict = {
            'id': TEST_RESOURCE_ID,
            'object': 'bank_account',
            'metadata': {},
        }
        bank_dict.update(params)
        return stripe.BankAccount.construct_from(bank_dict, stripe.api_key)

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

    # The previous tests already ensure that the request will be routed to the
    # correct URL, so we only test the API operations once.

    def test_is_not_retrievable(self):
        with self.assertRaises(NotImplementedError):
            stripe.BankAccount.retrieve(TEST_RESOURCE_ID)

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
            stripe.BankAccount.modify(
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
        # stripe-mock does not yet correctly handle deleting customer sources
        # self.assertTrue(resource.deleted)

    def test_is_verifiable(self):
        resource = self.construct_resource(customer='cus_123')
        resource.verify()
        self.assert_requested(
            'post',
            '/v1/customers/cus_123/sources/%s/verify' % TEST_RESOURCE_ID
        )
