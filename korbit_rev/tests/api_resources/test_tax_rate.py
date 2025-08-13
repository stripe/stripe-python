import stripe


TEST_RESOURCE_ID = "txr_123"


class TestTaxRate(object):
    def test_is_listable(self, http_client_mock):
        resources = stripe.TaxRate.list()
        http_client_mock.assert_requested("get", path="/v1/tax_rates")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.TaxRate)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.TaxRate.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/tax_rates/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.TaxRate)

    def test_is_creatable(self, http_client_mock):
        resource = stripe.TaxRate.create(
            display_name="name", inclusive=False, percentage=10.15
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/tax_rates",
            post_data="display_name=name&inclusive=false&percentage=10.15",
        )
        assert isinstance(resource, stripe.TaxRate)

    def test_is_saveable(self, http_client_mock):
        resource = stripe.TaxRate.retrieve(TEST_RESOURCE_ID)
        resource.metadata["key"] = "value"
        resource.save()
        http_client_mock.assert_requested(
            "post",
            path="/v1/tax_rates/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )

    def test_is_modifiable(self, http_client_mock):
        resource = stripe.TaxRate.modify(
            TEST_RESOURCE_ID, metadata={"key": "value"}
        )
        http_client_mock.assert_requested(
            "post",
            path="/v1/tax_rates/%s" % TEST_RESOURCE_ID,
            post_data="metadata[key]=value",
        )
        assert isinstance(resource, stripe.TaxRate)
