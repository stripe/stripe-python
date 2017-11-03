from __future__ import absolute_import, division, print_function

import stripe
from tests.helper import StripeTestCase


TEST_RESOURCE_ID = 'apwc_123'


class ApplePayDomainTest(StripeTestCase):
    def test_is_listable(self):
        resources = stripe.ApplePayDomain.list()
        self.assert_requested(
            'get',
            '/v1/apple_pay/domains'
        )
        self.assertIsInstance(resources.data, list)
        self.assertIsInstance(resources.data[0], stripe.ApplePayDomain)

    def test_is_retrievable(self):
        resource = stripe.ApplePayDomain.retrieve(TEST_RESOURCE_ID)
        self.assert_requested(
            'get',
            '/v1/apple_pay/domains/%s' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.ApplePayDomain)

    def test_is_creatable(self):
        resource = stripe.ApplePayDomain.create(
            domain_name='test.com',
        )
        self.assert_requested(
            'post',
            '/v1/apple_pay/domains'
        )
        self.assertIsInstance(resource, stripe.ApplePayDomain)

    def test_is_deletable(self):
        resource = stripe.ApplePayDomain.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        self.assert_requested(
            'delete',
            '/v1/apple_pay/domains/%s' % resource.id
        )
        self.assertIsInstance(resource, stripe.ApplePayDomain)
