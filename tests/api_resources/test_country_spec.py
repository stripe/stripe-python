import stripe


TEST_RESOURCE_ID = "US"


class TestCountrySpec(object):
    def test_is_listable(self, http_client_mock):
        resources = stripe.CountrySpec.list()
        http_client_mock.assert_requested("get", path="/v1/country_specs")
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.CountrySpec)

    def test_is_retrievable(self, http_client_mock):
        resource = stripe.CountrySpec.retrieve(TEST_RESOURCE_ID)
        http_client_mock.assert_requested(
            "get", path="/v1/country_specs/%s" % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.CountrySpec)
