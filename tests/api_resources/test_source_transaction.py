import stripe


class TestSourceTransaction(object):
    def test_is_listable(self, http_client_mock):
        source = stripe.Source.construct_from(
            {"id": "src_123", "object": "source"}, stripe.api_key
        )
        source_transactions = source.list_source_transactions()
        http_client_mock.assert_requested(
            "get", path="/v1/sources/src_123/source_transactions"
        )
        assert isinstance(source_transactions.data, list)
        assert isinstance(
            source_transactions.data[0], stripe.SourceTransaction
        )
