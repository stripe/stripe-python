import stripe
from tests.helper import StripeTestCase


TEST_RESOURCE_ID = 'tu_123'


class TopupTest(StripeTestCase):
    def test_is_listable(self):
        resources = stripe.Topup.list()
        self.assert_requested(
            'get',
            '/v1/topups'
        )
        self.assertIsInstance(resources.data, list)
        self.assertIsInstance(resources.data[0], stripe.Topup)

    def test_is_retrievable(self):
        resource = stripe.Topup.retrieve(TEST_RESOURCE_ID)
        self.assert_requested(
            'get',
            '/v1/topups/%s' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.Topup)

    def test_is_creatable(self):
        resource = stripe.Topup.create(
            amount=100,
            currency='usd',
            source='src_123',
            description='description',
            statement_descriptor='statement descriptor'
        )
        self.assert_requested(
            'post',
            '/v1/topups'
        )
        self.assertIsInstance(resource, stripe.Topup)

    def test_is_saveable(self):
        resource = stripe.Topup.retrieve(TEST_RESOURCE_ID)
        resource.metadata['key'] = 'value'
        resource.save()
        self.assert_requested(
            'post',
            '/v1/topups/%s' % resource.id
        )

    def test_is_modifiable(self):
        resource = stripe.Topup.modify(
            TEST_RESOURCE_ID,
            metadata={'key': 'value'}
        )
        self.assert_requested(
            'post',
            '/v1/topups/%s' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.Topup)
