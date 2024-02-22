import stripe


TEST_RESOURCE_ID = "txi_123"


class TestTaxId(object):
    def construct_resource(self):
        tax_id_dict = {
            "id": TEST_RESOURCE_ID,
            "object": "tax_id",
            "customer": "cus_123",
        }
        return stripe.TaxId.construct_from(tax_id_dict, stripe.api_key)

    def test_has_instance_url(self):
        resource = self.construct_resource()
        assert resource.instance_url() == "/v1/tax_ids/%s" % TEST_RESOURCE_ID

    def test_is_creatable(self, http_client_mock):
        stripe.TaxId.create(
            type="eu_vat",
            value="DE123456789",
        )
        http_client_mock.assert_requested("post", path="/v1/tax_ids")

    def test_is_retrievable(self, http_client_mock):
        stripe.TaxId.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/tax_ids/%s" % TEST_RESOURCE_ID
        )

    def test_is_deletable(self, http_client_mock):
        resource = stripe.TaxId.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        http_client_mock.assert_requested(
            "delete", path="/v1/tax_ids/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    def test_can_delete(self, http_client_mock):
        resource = stripe.TaxId.delete(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "delete", path="/v1/tax_ids/%s" % TEST_RESOURCE_ID
        )
        assert resource.deleted is True

    def test_is_listable(self, http_client_mock):
        resources = stripe.TaxId.list()
        http_client_mock.assert_requested("get", path="/v1/tax_ids")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.TaxId)
