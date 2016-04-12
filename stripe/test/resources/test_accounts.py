import stripe
from stripe.test.helper import StripeResourceTest


class AccountTest(StripeResourceTest):

    def test_retrieve_account_deprecated(self):
        stripe.Account.retrieve()

        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/account',
            {},
            None
        )

    def test_retrieve_account(self):
        stripe.Account.retrieve('acct_foo')
        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/accounts/acct_foo',
            {},
            None
        )

    def test_list_accounts(self):
        stripe.Account.list()
        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/accounts',
            {}
        )

    def test_create_account(self):
        pii = {
            'type': 'individual',
            'first_name': 'Joe',
            'last_name': 'Smith',
        }
        stripe.Account.create(legal_entity=pii)
        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/accounts',
            {
                'legal_entity': pii,
            },
            None,
        )

    def test_update_account(self):
        acct = stripe.Account.construct_from({
            'id': 'acct_update',
            'legal_entity': {'first_name': 'Joe'},
        }, 'api_key')
        acct.legal_entity['first_name'] = 'Bob'
        acct.save()

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/accounts/acct_update',
            {
                'legal_entity': {
                    'first_name': 'Bob',
                },
            },
            None,
        )

    def test_account_delete_bank_account(self):
        source = stripe.BankAccount.construct_from({
            'account': 'acc_delete_ba',
            'id': 'ba_delete_ba',
        }, 'api_key')
        source.delete()

        self.requestor_mock.request.assert_called_with(
            'delete',
            '/v1/accounts/acc_delete_ba/external_accounts/ba_delete_ba',
            {},
            None
        )

    def test_reject_account(self):
        self.mock_response({
            'id': 'acct_reject',
            'verification': {
                'disabled_reason': 'rejected.fraud'
            },
        })

        obj = stripe.Account.construct_from({
            'id': 'acct_reject'
        }, 'mykey')

        self.assertTrue(obj is obj.reject(reason='fraud'))
        self.assertEqual('rejected.fraud', obj.verification['disabled_reason'])
        self.assertEqual('acct_reject', obj.id)

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/accounts/acct_reject/reject',
            {'reason': 'fraud'},
            None
        )

    def test_reject_account_without_reason(self):
        self.mock_response({
            'id': 'acct_reject',
            'verification': {
                'disabled_reason': 'rejected.fraud'
            },
        })

        obj = stripe.Account.construct_from({
            'id': 'acct_reject'
        }, 'mykey')

        self.assertTrue(obj is obj.reject())
        self.assertEqual('rejected.fraud', obj.verification['disabled_reason'])
        self.assertEqual('acct_reject', obj.id)

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/accounts/acct_reject/reject',
            {},
            None
        )

    def test_verify_additional_owner(self):
        acct = stripe.Account.construct_from({
            'id': 'acct_update',
            'additional_owners': [{
                'first_name': 'Alice',
                'verification': {},
            }]
        }, 'api_key')
        owner = acct.additional_owners[0]
        owner.verification.document = 'file_foo'
        acct.save()

        self.requestor_mock.request.assert_called_with(
            'post',
            '/v1/accounts/acct_update',
            {
                'additional_owners': {
                    '0': {
                        'verification': {
                            'document': 'file_foo',
                        },
                    },
                },
            },
            None,
        )
