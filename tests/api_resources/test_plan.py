from __future__ import absolute_import, division, print_function

import stripe
from tests.helper import StripeTestCase


TEST_RESOURCE_ID = '250FF'


class PlanTest(StripeTestCase):
    def test_is_listable(self):
        resources = stripe.Plan.list()
        self.assert_requested(
            'get',
            '/v1/plans'
        )
        self.assertIsInstance(resources.data, list)
        self.assertIsInstance(resources.data[0], stripe.Plan)

    def test_is_retrievable(self):
        resource = stripe.Plan.retrieve(TEST_RESOURCE_ID)
        self.assert_requested(
            'get',
            '/v1/plans/%s' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.Plan)

    def test_is_creatable(self):
        resource = stripe.Plan.create(
            amount=100,
            currency='usd',
            id='plan_id',
            interval='month',
            name='plan_name',
        )
        self.assert_requested(
            'post',
            '/v1/plans'
        )
        self.assertIsInstance(resource, stripe.Plan)

    def test_is_creatable_metered(self):
        resource = stripe.Plan.create(
            amount=100,
            currency='usd',
            id='plan_id',
            interval='month',
            name='plan_name',
            usage_type='metered',
        )
        self.assert_requested(
            'post',
            '/v1/plans'
        )
        self.assertIsInstance(resource, stripe.Plan)

    def test_is_creatable_tiered(self):
        resource = stripe.Plan.create(
            currency='usd',
            id='plan_id',
            interval='month',
            name='plan_name',
            billing_scheme='tiered',
            tiers=[
                {"up_to": 123, "amount": 123}, {"up_to": 'inf', "amount": 312}
            ],
            tiers_mode='volume',
        )
        self.assert_requested(
            'post',
            '/v1/plans'
        )
        self.assertIsInstance(resource, stripe.Plan)

    def test_is_creatable_transform_usage(self):
        resource = stripe.Plan.create(
            amount=100,
            currency='usd',
            id='plan_id',
            interval='month',
            name='plan_name',
            transform_usage={"divide_by": 100, "round": 'up'},
        )
        self.assert_requested(
            'post',
            '/v1/plans'
        )
        self.assertIsInstance(resource, stripe.Plan)

    def test_is_saveable(self):
        resource = stripe.Plan.retrieve(TEST_RESOURCE_ID)
        resource.metadata['key'] = 'value'
        resource.save()
        self.assert_requested(
            'post',
            '/v1/plans/%s' % resource.id
        )

    def test_is_modifiable(self):
        resource = stripe.Plan.modify(
            TEST_RESOURCE_ID,
            metadata={'key': 'value'}
        )
        self.assert_requested(
            'post',
            '/v1/plans/%s' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.Plan)

    def test_is_deletable(self):
        resource = stripe.Plan.retrieve(TEST_RESOURCE_ID)
        # Unfortunately stripe-mock will return a resource with a different
        # ID, so we need to store the original ID for the request assertion
        resource_id = resource.id
        resource.delete()
        self.assert_requested(
            'delete',
            '/v1/plans/%s' % resource_id
        )
        self.assertTrue(resource.deleted)
