from __future__ import absolute_import, division, print_function

from six.moves.urllib.parse import parse_qs, urlparse

import stripe
from tests.helper import StripeTestCase


class OAuthTests(StripeTestCase):
    def test_authorize_url(self):
        url = stripe.OAuth.authorize_url(
            scope='read_write',
            state='csrf_token',
            stripe_user={
                'email': 'test@example.com',
                'url': 'https://example.com/profile/test',
                'country': 'US',
            })

        o = urlparse(url)
        params = parse_qs(o.query)

        self.assertEqual('https', o.scheme)
        self.assertEqual('connect.stripe.com', o.netloc)
        self.assertEqual('/oauth/authorize', o.path)

        self.assertEqual(['ca_123'], params['client_id'])
        self.assertEqual(['read_write'], params['scope'])
        self.assertEqual(['test@example.com'], params['stripe_user[email]'])
        self.assertEqual(
            ['https://example.com/profile/test'],
            params['stripe_user[url]']
        )
        self.assertEqual(['US'], params['stripe_user[country]'])

    def test_token(self):
        self.stub_request(
            'post',
            '/oauth/token',
            {
                'access_token': 'sk_access_token',
                'scope': 'read_only',
                'livemode': 'false',
                'token_type': 'bearer',
                'refresh_token': 'sk_refresh_token',
                'stripe_user_id': 'acct_test',
                'stripe_publishable_key': 'pk_test',
            }
        )

        resp = stripe.OAuth.token(
            grant_type='authorization_code',
            code='this_is_an_authorization_code',
        )
        self.assert_requested(
            'post',
            '/oauth/token',
            {
                'grant_type': 'authorization_code',
                'code': 'this_is_an_authorization_code',
            }
        )
        self.assertEqual('sk_access_token', resp['access_token'])

    def test_deauthorize(self):
        self.stub_request(
            'post',
            '/oauth/deauthorize',
            {
                'stripe_user_id': 'acct_test_deauth',
            }
        )

        resp = stripe.OAuth.deauthorize(stripe_user_id='acct_test_deauth')
        self.assert_requested(
            'post',
            '/oauth/deauthorize',
            {
                'client_id': 'ca_123',
                'stripe_user_id': 'acct_test_deauth',
            }
        )
        self.assertEqual('acct_test_deauth', resp['stripe_user_id'])
