import stripe


class TestSetupAttempt(object):
    def test_is_listable(self, http_client_mock):
        resources = stripe.SetupAttempt.list(setup_intent="seti_123")
        http_client_mock.assert_requested(
            "get",
            path="/v1/setup_attempts",
            query_string="setup_intent=seti_123",
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.SetupAttempt)
