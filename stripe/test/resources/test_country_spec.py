import stripe
from stripe.test.helper import (
    StripeResourceTest
)


class CountrySpecTest(StripeResourceTest):

    def test_country_spec_list_all(self):
        stripe.CountrySpec.all()

        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/country_specs',
            {}
        )

    def test_country_spec_list_retrieve(self):
        stripe.CountrySpec.retrieve('US')

        self.requestor_mock.request.assert_called_with(
            'get',
            '/v1/country_specs/US',
            {},
            None
        )
