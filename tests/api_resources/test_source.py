from __future__ import absolute_import, division, print_function

import warnings

import stripe
from tests.helper import StripeTestCase


TEST_RESOURCE_ID = 'src_123'


class SourceTest(StripeTestCase):

    def test_is_retrievable(self):
        resource = stripe.Source.retrieve(TEST_RESOURCE_ID)
        self.assert_requested(
            'get',
            '/v1/sources/%s' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.Source)

    def test_is_creatable(self):
        resource = stripe.Source.create(
            type='card',
            token='tok_123'
        )
        self.assert_requested(
            'post',
            '/v1/sources'
        )
        self.assertIsInstance(resource, stripe.Source)

    def test_is_saveable(self):
        resource = stripe.Source.retrieve(TEST_RESOURCE_ID)
        resource.metadata['key'] = 'value'
        resource.save()
        self.assert_requested(
            'post',
            '/v1/sources/%s' % resource.id
        )

    def test_is_modifiable(self):
        resource = stripe.Source.modify(
            TEST_RESOURCE_ID,
            metadata={'key': 'value'}
        )
        self.assert_requested(
            'post',
            '/v1/sources/%s' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.Source)

    def test_is_detachable_when_attached(self):
        resource = stripe.Source.construct_from({
            'id': TEST_RESOURCE_ID,
            'object': 'source',
            'customer': 'cus_123'
        }, stripe.api_key)
        source = resource.detach()
        self.assertTrue(source is resource)
        self.assert_requested(
            'delete',
            '/v1/customers/cus_123/sources/%s' % TEST_RESOURCE_ID
        )

    def test_is_not_detachable_when_unattached(self):
        resource = stripe.Source.retrieve(TEST_RESOURCE_ID)
        self.assertRaises(NotImplementedError, resource.detach)

    def test_raises_a_warning_when_calling_delete(self):
        with warnings.catch_warnings(record=True) as w:
            warnings.simplefilter('always')

            resource = stripe.Source.construct_from({
                'id': TEST_RESOURCE_ID,
                'object': 'source',
                'customer': 'cus_123'
            }, stripe.api_key)
            resource.delete()

            self.assertEqual(1, len(w))
            self.assertEqual(w[0].category, DeprecationWarning)

    def test_is_verifiable(self):
        resource = stripe.Source.retrieve(TEST_RESOURCE_ID)
        source = resource.verify(values=[1, 2])
        self.assertTrue(source is resource)
        self.assert_requested(
            'post',
            '/v1/sources/%s/verify' % TEST_RESOURCE_ID,
            {'values': [1, 2]}
        )
