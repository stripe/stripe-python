import stripe
from stripe.test.helper import StripeResourceTest


class CountrySpecTest(StripeResourceTest):

    def test_country_spec_list(self):
        stripe.CountrySpec.list()
        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/country_specs',
            {}
        )

    def test_country_spec_retrieve(self):
        stripe.CountrySpec.retrieve('US')

        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/country_specs/US',
            {},
            None
        )
