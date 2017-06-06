import urlparse

import stripe
from stripe.test.helper import StripeApiTestCase


class OAuthTests(StripeApiTestCase):
    def setUp(self):
        super(OAuthTests, self).setUp()
        self.mock_response({})

        stripe.client_id = 'ca_test'

    def tearDown(self):
        super(OAuthTests, self).tearDown()

        stripe.client_id = None

    def test_authorize_url(self):
        url = stripe.OAuth.authorize_url(
            scope='read_write',
            state='csrf_token',
            stripe_user={
                'email': 'test@example.com',
                'url': 'https://example.com/profile/test',
                'country': 'US',
            })

        o = urlparse.urlparse(url)
        params = urlparse.parse_qs(o.query)

        self.assertEqual('https', o.scheme)
        self.assertEqual('connect.stripe.com', o.netloc)
        self.assertEqual('/oauth/authorize', o.path)

        self.assertEqual(['ca_test'], params['client_id'])
        self.assertEqual(['read_write'], params['scope'])
        self.assertEqual(['test@example.com'], params['stripe_user[email]'])
        self.assertEqual(
            ['https://example.com/profile/test'],
            params['stripe_user[url]']
        )
        self.assertEqual(['US'], params['stripe_user[country]'])

    def test_token(self):
        stripe.OAuth.token(
            grant_type='authorization_code',
            code='this_is_an_authorization_code',
        )

        self.requestor_mock.request.assert_called_with(
            'post',
            '/oauth/token',
            {
                'grant_type': 'authorization_code',
                'code': 'this_is_an_authorization_code',
            },
            None
        )

    def test_deauthorize(self):
        stripe.OAuth.deauthorize(stripe_user_id='acct_deauth')

        self.requestor_mock.request.assert_called_with(
            'post',
            '/oauth/deauthorize',
            {
                'client_id': 'ca_test',
                'stripe_user_id': 'acct_deauth',
            },
            None
        )

    def test_deauthorize_account_instance(self):
        acct = stripe.Account.construct_from({
            'id': 'acct_deauth',
        }, 'api_key')
        acct.deauthorize()

        self.requestor_mock.request.assert_called_with(
            'post',
            '/oauth/deauthorize',
            {
                'client_id': 'ca_test',
                'stripe_user_id': 'acct_deauth',
            },
            None
        )
