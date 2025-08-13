import pytest

import stripe


TEST_RESOURCE_ID = "src_123"


class TestSource(object):
    def test_is_retrievable(self, http_client_mock):
        resource = stripe.Source.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/sources/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Source)

    def test_is_creatable(self, http_client_mock):
        resource = stripe.Source.create(type="card", token="tok_123")
        http_client_mock.assert_requested(
            "post", path="/v1/sources", post_data="type=card&token=tok_123"
        )
        assert isinstance(resource, stripe.Source)

    def test_is_saveable(self, http_client_mock):
        resource = stripe.Source.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        http_client_mock.assert_requested(
            "post",
            path="/v1/sources/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )

    def test_is_modifiable(self, http_client_mock):
        resource = stripe.Source.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/sources/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )
        assert isinstance(resource, stripe.Source)

    def test_is_detachable_when_attached(self, http_client_mock):
        resource = stripe.Source.construct_from(
            {
                "id": TEST_RESOURCE_ID,
                "object": "source",
                "customer": "cus_123",
            },
            stripe.api_key,
        )
        source = resource.detach()
        assert source is resource
        http_client_mock.assert_requested(
            "delete",
            path="/v1/customers/cus_123/sources/%s" % TEST_RESOURCE_ID,
        )

    def test_is_not_detachable_when_unattached(self, http_client_mock):
        resource = stripe.Source.retrieve(TEST_RESOURCE_ID)
        with pytest.raises(stripe.error.InvalidRequestError):
            resource.detach()

    def test_is_verifiable(self, http_client_mock):
        resource = stripe.Source.retrieve(TEST_RESOURCE_ID)
        source = resource.verify(values=[1, 2])
        assert source is resource
        http_client_mock.assert_requested(
            "post",
            path="/v1/sources/%s/verify" % TEST_RESOURCE_ID,
            post_data="values[0]=1&values[1]=2",
        )


class TestSourceTransactions(object):
    def test_is_listable(self, http_client_mock):
        resource = stripe.Source.list_source_transactions(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/sources/%s/source_transactions" % TEST_RESOURCE_ID
        )
        assert isinstance(resource.data, list)
        assert isinstance(resource.data[0], stripe.SourceTransaction)
