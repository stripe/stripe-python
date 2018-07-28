from __future__ import absolute_import, division, print_function

import stripe


TEST_RESOURCE_ID = 'acct_123'
TEST_EXTERNALACCOUNT_ID = 'ba_123'


class TestAccount(object):
    def test_is_listable(self, request_mock):
        resources = stripe.Account.list()
        request_mock.assert_requested(
            'get',
            '/v1/accounts'
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Account)

    def test_is_retrievable(self, request_mock):
        resource = stripe.Account.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            'get',
            '/v1/accounts/%s' % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Account)

    def test_is_creatable(self, request_mock):
        resource = stripe.Account.create(
            country='US',
            type='custom'
        )
        request_mock.assert_requested(
            'post',
            '/v1/accounts'
        )
        assert isinstance(resource, stripe.Account)

    def test_is_saveable(self, request_mock):
        account = stripe.Account.retrieve(TEST_RESOURCE_ID)
        account.metadata['key'] = 'value'
        resource = account.save()
        request_mock.assert_requested(
            'post',
            '/v1/accounts/%s' % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Account)
        assert resource is account

    def test_is_saveable_with_additional_owners(self, request_mock):
        # stripe-mock does not return additional owners so we construct
        account = stripe.Account.construct_from({
            'id': '%s' % TEST_RESOURCE_ID,
            'legal_entity': {
                'additional_owners': [{
                    'first_name': 'name',
                    'verification': {},
                }],
            }
        }, stripe.api_key)
        owner = account.legal_entity.additional_owners[0]
        owner.verification.document = 'file_foo'
        resource = account.save()
        request_mock.assert_requested(
            'post',
            '/v1/accounts/%s' % TEST_RESOURCE_ID,
            {
                'legal_entity': {
                    'additional_owners': {
                        '0': {
                            'verification': {
                                'document': 'file_foo',
                            },
                        },
                    },
                },
            }
        )
        assert isinstance(resource, stripe.Account)
        assert resource is account

    def test_is_modifiable(self, request_mock):
        resource = stripe.Account.modify(
            TEST_RESOURCE_ID,
            metadata={'key': 'value'}
        )
        request_mock.assert_requested(
            'post',
            '/v1/accounts/%s' % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Account)

    def test_is_deletable(self, request_mock):
        resource = stripe.Account.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested(
            'delete',
            '/v1/accounts/%s' % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    def test_can_retrieve_no_id(self, request_mock):
        resource = stripe.Account.retrieve()
        request_mock.assert_requested(
            'get',
            '/v1/account'
        )
        assert isinstance(resource, stripe.Account)

    def test_can_reject(self, request_mock):
        account = stripe.Account.retrieve(TEST_RESOURCE_ID)
        resource = account.reject(reason='fraud')
        request_mock.assert_requested(
            'post',
            '/v1/accounts/%s/reject' % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Account)
        assert resource is account

    def test_is_deauthorizable(self, request_mock):
        account = stripe.Account.retrieve(TEST_RESOURCE_ID)
        request_mock.stub_request(
            'post',
            '/oauth/deauthorize',
            {
                'stripe_user_id': account.id,
            }
        )
        account.deauthorize()
        request_mock.assert_requested(
           'post',
           '/oauth/deauthorize',
           {
               'client_id': stripe.client_id,
               'stripe_user_id': account.id,
           }
        )


class TestAccountExternalAccounts(object):
    def test_is_listable(self, request_mock):
        resources = stripe.Account.list_external_accounts(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            'get',
            '/v1/accounts/%s/external_accounts' % TEST_RESOURCE_ID
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Card)

    def test_is_retrievable(self, request_mock):
        resource = stripe.Account.retrieve_external_account(
            TEST_RESOURCE_ID,
            TEST_EXTERNALACCOUNT_ID
        )
        request_mock.assert_requested(
            'get',
            '/v1/accounts/%s/external_accounts/%s' % (TEST_RESOURCE_ID,
                                                      TEST_EXTERNALACCOUNT_ID)
        )
        assert isinstance(resource, stripe.BankAccount)

    def test_is_creatable(self, request_mock):
        resource = stripe.Account.create_external_account(
            TEST_RESOURCE_ID,
            external_account='btok_123'
        )
        request_mock.assert_requested(
            'post',
            '/v1/accounts/%s/external_accounts' % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.BankAccount)

    def test_is_modifiable(self, request_mock):
        resource = stripe.Account.modify_external_account(
            TEST_RESOURCE_ID,
            TEST_EXTERNALACCOUNT_ID,
            metadata={'foo': 'bar'}
        )
        request_mock.assert_requested(
            'post',
            '/v1/accounts/%s/external_accounts/%s' % (TEST_RESOURCE_ID,
                                                      TEST_EXTERNALACCOUNT_ID)
        )
        assert isinstance(resource, stripe.BankAccount)

    def test_is_deletable(self, request_mock):
        resource = stripe.Account.delete_external_account(
            TEST_RESOURCE_ID,
            TEST_EXTERNALACCOUNT_ID
        )
        request_mock.assert_requested(
            'delete',
            '/v1/accounts/%s/external_accounts/%s' % (TEST_RESOURCE_ID,
                                                      TEST_EXTERNALACCOUNT_ID)
        )
        assert resource.deleted is True


class TestAccountLoginLinks(object):
    def test_is_creatable(self, request_mock):
        resource = stripe.Account.create_login_link(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            'post',
            '/v1/accounts/%s/login_links' % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.LoginLink)
