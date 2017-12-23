from __future__ import absolute_import, division, print_function

import stripe


TEST_RESOURCE_ID = 'apwc_123'


class TestApplePayDomain(object):
    def test_is_listable(self, request_mock):
        resources = stripe.ApplePayDomain.list()
        request_mock.assert_requested(
            'get',
            '/v1/apple_pay/domains'
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.ApplePayDomain)

    def test_is_retrievable(self, request_mock):
        resource = stripe.ApplePayDomain.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            'get',
            '/v1/apple_pay/domains/%s' % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.ApplePayDomain)

    def test_is_creatable(self, request_mock):
        resource = stripe.ApplePayDomain.create(
            domain_name='test.com',
        )
        request_mock.assert_requested(
            'post',
            '/v1/apple_pay/domains'
        )
        assert isinstance(resource, stripe.ApplePayDomain)

    def test_is_deletable(self, request_mock):
        resource = stripe.ApplePayDomain.retrieve(TEST_RESOURCE_ID)
        # Unfortunately stripe-mock will return a resource with a different
        # ID, so we need to store the original ID for the request assertion
        resource_id = resource.id
        resource.delete()
        request_mock.assert_requested(
            'delete',
            '/v1/apple_pay/domains/%s' % resource_id
        )
        assert resource.deleted is True
