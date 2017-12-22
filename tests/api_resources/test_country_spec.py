from __future__ import absolute_import, division, print_function

import stripe
from tests.helper import StripeTestCase


TEST_RESOURCE_ID = 'US'


class CountrySpecTest(StripeTestCase):
    def test_is_listable(self):
        resources = stripe.CountrySpec.list()
        self.assert_requested(
            'get',
            '/v1/country_specs'
        )
        self.assertIsInstance(resources.data, list)
        self.assertIsInstance(resources.data[0], stripe.CountrySpec)

    def test_is_retrievable(self):
        resource = stripe.CountrySpec.retrieve(TEST_RESOURCE_ID)
        self.assert_requested(
            'get',
            '/v1/country_specs/%s' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.CountrySpec)
