from __future__ import absolute_import, division, print_function

import stripe
from tests.helper import StripeTestCase


TEST_RESOURCE_ID = '250FF'


class CouponTest(StripeTestCase):
    def test_is_listable(self):
        resources = stripe.Coupon.list()
        self.assert_requested(
            'get',
            '/v1/coupons'
        )
        self.assertIsInstance(resources.data, list)
        self.assertIsInstance(resources.data[0], stripe.Coupon)

    def test_is_retrievable(self):
        resource = stripe.Coupon.retrieve(TEST_RESOURCE_ID)
        self.assert_requested(
            'get',
            '/v1/coupons/%s' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.Coupon)

    def test_is_creatable(self):
        resource = stripe.Coupon.create(
            percent_off=25,
            duration='repeating',
            duration_in_months=3,
            id='250FF'
        )
        self.assert_requested(
            'post',
            '/v1/coupons'
        )
        self.assertIsInstance(resource, stripe.Coupon)

    def test_is_saveable(self):
        resource = stripe.Coupon.retrieve(TEST_RESOURCE_ID)
        resource.metadata['key'] = 'value'
        resource.save()
        self.assert_requested(
            'post',
            '/v1/coupons/%s' % resource.id
        )

    def test_is_modifiable(self):
        resource = stripe.Coupon.modify(
            TEST_RESOURCE_ID,
            metadata={'key': 'value'}
        )
        self.assert_requested(
            'post',
            '/v1/coupons/%s' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.Coupon)

    def test_is_deletable(self):
        resource = stripe.Coupon.retrieve(TEST_RESOURCE_ID)
        # Unfortunately stripe-mock will return a resource with a different
        # ID, so we need to store the original ID for the request assertion
        resource_id = resource.id
        resource.delete()
        self.assert_requested(
            'delete',
            '/v1/coupons/%s' % resource_id
        )
        self.assertTrue(resource.deleted)
