from __future__ import absolute_import, division, print_function

import stripe
from tests.helper import (StripeTestCase)


TEST_RESOURCE_ID = 'aliacc_123'


class AlipayAccountTest(StripeTestCase):
    def construct_resource(self):
        alipay_dict = {
            'id': TEST_RESOURCE_ID,
            'object': 'alipay_account',
            'metadata': {},
            'customer': 'cus_123'
        }
        return stripe.AlipayAccount.construct_from(alipay_dict, stripe.api_key)

    def test_has_instance_url(self):
        resource = self.construct_resource()
        self.assertEqual(
            '/v1/customers/cus_123/sources/%s' % TEST_RESOURCE_ID,
            resource.instance_url()
        )

    def test_is_modifiable(self):
        stripe.AlipayAccount.modify(
            'cus_123',
            TEST_RESOURCE_ID,
            metadata={'key': 'value'}
        )
        self.assert_requested(
            'post',
            '/v1/customers/cus_123/sources/%s' % TEST_RESOURCE_ID
        )

    def test_is_not_retrievable(self):
        with self.assertRaises(NotImplementedError):
            stripe.AlipayAccount.retrieve(TEST_RESOURCE_ID)

    # Below, we don't use stripe-mock as it always returns a Bank Account
    # object when you hit /v1/customers/%s/sources/%s

    def test_is_saveable(self):
        resource = self.construct_resource()
        resource.metadata['key'] = 'value'
        resource.save()
        self.assert_requested(
            'post',
            '/v1/customers/cus_123/sources/%s' % TEST_RESOURCE_ID
        )

    def test_is_deletable(self):
        resource = self.construct_resource()
        resource.delete()
        self.assert_requested(
            'delete',
            '/v1/customers/cus_123/sources/%s' % TEST_RESOURCE_ID
        )
