import stripe


TEST_RESOURCE_ID = "rdr_123"


class TestConnectionToken(object):
    def test_is_creatable(self, http_client_mock):
        resource = stripe.terminal.ConnectionToken.create()
        http_client_mock.assert_requested(
            "post", path="/v1/terminal/connection_tokens", post_data=""
        )
        assert isinstance(resource, stripe.terminal.ConnectionToken)
