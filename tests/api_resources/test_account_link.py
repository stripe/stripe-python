from __future__ import absolute_import, division, print_function

import stripe


class TestAccountLink(object):
    def test_is_creatable(self, request_mock):
        resource = stripe.AccountLink.create(
            account="acct_123",
            failure_url="https://stripe.com/failure",
            success_url="https://stripe.com/success",
            type="custom_account_verification",
        )
        request_mock.assert_requested("post", "/v1/account_links")
        assert isinstance(resource, stripe.AccountLink)
