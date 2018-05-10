import stripe
from tests.helper import StripeTestCase


TEST_RESOURCE_ID = 'issfr_123'


class IssuerFraudRecordTest(StripeTestCase):
    def test_is_listable(self):
        resources = stripe.IssuerFraudRecord.list()
        self.assert_requested(
            'get',
            '/v1/issuer_fraud_records'
        )
        self.assertIsInstance(resources.data, list)
        self.assertIsInstance(resources.data[0], stripe.IssuerFraudRecord)

    def test_is_retrievable(self):
        resource = stripe.IssuerFraudRecord.retrieve(TEST_RESOURCE_ID)
        self.assert_requested(
            'get',
            '/v1/issuer_fraud_records/%s' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.IssuerFraudRecord)
