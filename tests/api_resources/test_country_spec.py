from __future__ import absolute_import, division, print_function

import stripe


TEST_RESOURCE_ID = 'US'


class TestCountrySpec(object):
    def test_is_listable(self, request_mock):
        resources = stripe.CountrySpec.list()
        request_mock.assert_requested(
            'get',
            '/v1/country_specs'
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.CountrySpec)

    def test_is_retrievable(self, request_mock):
        resource = stripe.CountrySpec.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            'get',
            '/v1/country_specs/%s' % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.CountrySpec)
