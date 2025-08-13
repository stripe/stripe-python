import stripe


TEST_RESOURCE_ID = "txcd_123"


class TestTaxCode(object):
    def test_is_listable(self, http_client_mock):
        resources = stripe.TaxCode.list()
        http_client_mock.assert_requested("get", path="/v1/tax_codes")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.TaxCode)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.TaxCode.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/tax_codes/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.TaxCode)
