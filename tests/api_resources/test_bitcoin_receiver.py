from __future__ import absolute_import, division, print_function

import stripe
from tests.helper import StripeTestCase


TEST_RESOURCE_ID = 'btcrcv_123'


class BitcoinReceiverTest(StripeTestCase):
    def construct_resource(self, **params):
        res_dict = {
            'id': TEST_RESOURCE_ID,
            'object': 'bitcoin_receiver',
            'metadata': {},
        }
        res_dict.update(params)
        return stripe.BitcoinReceiver.construct_from(res_dict, stripe.api_key)

    def test_has_customer_instance_url(self):
        resource = self.construct_resource(customer='cus_123')
        self.assertEqual(
            '/v1/customers/cus_123/sources/%s' % TEST_RESOURCE_ID,
            resource.instance_url()
        )

    def test_has_receiver_instance_url(self):
        resource = self.construct_resource()
        self.assertEqual(
            '/v1/bitcoin/receivers/%s' % TEST_RESOURCE_ID,
            resource.instance_url()
        )

    def test_is_listable(self):
        resources = stripe.BitcoinReceiver.list()
        self.assert_requested(
            'get',
            '/v1/bitcoin/receivers'
        )
        self.assertIsInstance(resources.data, list)
        self.assertIsInstance(resources.data[0], stripe.BitcoinReceiver)

    def test_is_retrievable(self):
        resource = stripe.BitcoinReceiver.retrieve(TEST_RESOURCE_ID)
        self.assert_requested(
            'get',
            '/v1/bitcoin/receivers/%s' % TEST_RESOURCE_ID
        )
        self.assertIsInstance(resource, stripe.BitcoinReceiver)

    # stripe-mock does not handle most write operations anymore so we stub
    # each one instead. This endpoint/resource is mostly deprecated today.
    # The previous tests already ensure that the request will be routed to the
    # correct URL, so we also only test the API operations once.

    def test_is_creatable(self):
        self.stub_request(
            'post',
            '/v1/bitcoin/receivers',
            {
                'id': '%s' % TEST_RESOURCE_ID,
                'object': 'bitcoin_receiver'
            }
        )
        resource = stripe.BitcoinReceiver.create()
        self.assert_requested(
            'post',
            '/v1/bitcoin/receivers'
        )
        self.assertIsInstance(resource, stripe.BitcoinReceiver)

    def test_is_saveable(self):
        self.stub_request(
            'post',
            '/v1/bitcoin/receivers/%s' % TEST_RESOURCE_ID
        )
        resource = self.construct_resource()
        resource.metadata['key'] = 'value'
        resource.save()
        self.assert_requested(
            'post',
            '/v1/bitcoin/receivers/%s' % TEST_RESOURCE_ID
        )

    def test_is_modifiable(self):
        self.stub_request(
            'post',
            '/v1/bitcoin/receivers/%s' % TEST_RESOURCE_ID
        )
        stripe.BitcoinReceiver.modify(
            TEST_RESOURCE_ID,
            metadata={'key': 'value'}
        )
        self.assert_requested(
            'post',
            '/v1/bitcoin/receivers/%s' % TEST_RESOURCE_ID
        )

    def test_is_deletable(self):
        self.stub_request(
            'delete',
            '/v1/bitcoin/receivers/%s' % TEST_RESOURCE_ID
        )
        resource = self.construct_resource()
        resource.delete()
        self.assert_requested(
            'delete',
            '/v1/bitcoin/receivers/%s' % TEST_RESOURCE_ID
        )
