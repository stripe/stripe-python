from __future__ import absolute_import, division, print_function

import stripe
from tests.helper import StripeTestCase


TEST_RESOURCE_ID = 'acct_123'
TEST_EXTERNALACCOUNT_ID = 'ba_123'


class AccountTest(StripeTestCase):
    def test_is_listable(self):
        resources = stripe.Account.list()
        self.assert_requested(
            'get',
            '/v1/accounts'
        )
        self.assertIsInstance(resources.data, list)
        self.assertIsInstance(resources.data[0], stripe.Account)

    def test_is_retrievable(self):
        resource = stripe.Account.retrieve(TEST_RESOURCE_ID)
        self.assert_requested(
            'get',
            '/v1/accounts/%s' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.Account)

    def test_is_creatable(self):
        resource = stripe.Account.create(
            country='US',
            type='custom'
        )
        self.assert_requested(
            'post',
            '/v1/accounts'
        )
        self.assertIsInstance(resource, stripe.Account)

    def test_is_saveable(self):
        account = stripe.Account.retrieve(TEST_RESOURCE_ID)
        account.metadata['key'] = 'value'
        resource = account.save()
        self.assert_requested(
            'post',
            '/v1/accounts/%s' % resource.id
        )
        self.assertIsInstance(resource, stripe.Account)
        self.assertTrue(resource is account)

    def test_is_saveable_with_additional_owners(self):
        # stripe-mock does not return additional owners so we construct
        account = stripe.Account.construct_from({
            'id': '%s' % TEST_RESOURCE_ID,
            'additional_owners': [{
                'first_name': 'name',
                'verification': {},
            }]
        }, stripe.api_key)
        owner = account.additional_owners[0]
        owner.verification.document = 'file_foo'
        resource = account.save()
        self.assert_requested(
            'post',
            '/v1/accounts/%s' % TEST_RESOURCE_ID,
            {
                'additional_owners': {
                    '0': {
                        'verification': {
                            'document': 'file_foo',
                        },
                    },
                },
            }
        )
        self.assertIsInstance(resource, stripe.Account)
        self.assertTrue(resource is account)

    def test_is_modifiable(self):
        resource = stripe.Account.modify(
            TEST_RESOURCE_ID,
            metadata={'key': 'value'}
        )
        self.assert_requested(
            'post',
            '/v1/accounts/%s' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.Account)

    def test_is_deletable(self):
        resource = stripe.Account.retrieve(TEST_RESOURCE_ID)
        # Unfortunately stripe-mock will return a resource with a different
        # ID, so we need to store the original ID for the request assertion
        resource_id = resource.id
        resource.delete()
        self.assert_requested(
            'delete',
            '/v1/accounts/%s' % resource_id
        )
        self.assertTrue(resource.deleted)

    def test_can_retrieve_no_id(self):
        resource = stripe.Account.retrieve()
        self.assert_requested(
            'get',
            '/v1/account'
        )
        self.assertIsInstance(resource, stripe.Account)

    def test_can_reject(self):
        account = stripe.Account.retrieve(TEST_RESOURCE_ID)
        resource = account.reject(reason='fraud')
        self.assert_requested(
            'post',
            '/v1/accounts/%s/reject' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.Account)
        self.assertTrue(resource is account)

    def test_is_deauthorizable(self):
        account = stripe.Account.retrieve(TEST_RESOURCE_ID)
        self.stub_request(
            'post',
            '/oauth/deauthorize',
            {
                'stripe_user_id': account.id,
            }
        )
        account.deauthorize()
        self.assert_requested(
           'post',
           '/oauth/deauthorize',
           {
               'client_id': stripe.client_id,
               'stripe_user_id': account.id,
           }
        )


class AccountExternalAccountsTests(StripeTestCase):
    def test_is_listable(self):
        resources = stripe.Account.list_external_accounts(TEST_RESOURCE_ID)
        self.assert_requested(
            'get',
            '/v1/accounts/%s/external_accounts' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resources.data, list)
        self.assertIsInstance(resources.data[0], stripe.Card)

    def test_is_retrievable(self):
        resource = stripe.Account.retrieve_external_account(
            TEST_RESOURCE_ID,
            TEST_EXTERNALACCOUNT_ID
        )
        self.assert_requested(
            'get',
            '/v1/accounts/%s/external_accounts/%s' % (TEST_RESOURCE_ID,
                                                      TEST_EXTERNALACCOUNT_ID)
        )
        self.assertIsInstance(resource, stripe.BankAccount)

    def test_is_creatable(self):
        resource = stripe.Account.create_external_account(
            TEST_RESOURCE_ID,
            external_account='btok_123'
        )
        self.assert_requested(
            'post',
            '/v1/accounts/%s/external_accounts' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.BankAccount)

    def test_is_modifiable(self):
        resource = stripe.Account.modify_external_account(
            TEST_RESOURCE_ID,
            TEST_EXTERNALACCOUNT_ID,
            metadata={'foo': 'bar'}
        )
        self.assert_requested(
            'post',
            '/v1/accounts/%s/external_accounts/%s' % (TEST_RESOURCE_ID,
                                                      TEST_EXTERNALACCOUNT_ID)
        )
        self.assertIsInstance(resource, stripe.BankAccount)

    def test_is_deletable(self):
        resource = stripe.Account.delete_external_account(
            TEST_RESOURCE_ID,
            TEST_EXTERNALACCOUNT_ID
        )
        self.assert_requested(
            'delete',
            '/v1/accounts/%s/external_accounts/%s' % (TEST_RESOURCE_ID,
                                                      TEST_EXTERNALACCOUNT_ID)
        )
        self.assertTrue(resource.deleted)


class AccountLoginLinksTests(StripeTestCase):
    def test_is_creatable(self):
        resource = stripe.Account.create_login_link(TEST_RESOURCE_ID)
        self.assert_requested(
            'post',
            '/v1/accounts/%s/login_links' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.LoginLink)
