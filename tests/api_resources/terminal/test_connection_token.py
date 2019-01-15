from __future__ import absolute_import, division, print_function

import stripe


TEST_RESOURCE_ID = "rdr_123"


class TestConnectionToken(object):
    def test_is_creatable(self, request_mock):
        resource = stripe.terminal.ConnectionToken.create()
        request_mock.assert_requested("post", "/v1/terminal/connection_tokens")
        assert isinstance(resource, stripe.terminal.ConnectionToken)
