import stripe


class TestBalance(object):
    def test_is_retrievable(self, http_client_mock):
        resource = stripe.Balance.retrieve()
        http_client_mock.assert_requested("get", path="/v1/balance")
        assert isinstance(resource, stripe.Balance)
