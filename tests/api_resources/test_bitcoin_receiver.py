from __future__ import absolute_import, division, print_function

import stripe


TEST_RESOURCE_ID = 'btcrcv_123'


class TestBitcoinReceiver(object):
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
        assert resource.instance_url() == \
            '/v1/customers/cus_123/sources/%s' % TEST_RESOURCE_ID

    def test_has_receiver_instance_url(self):
        resource = self.construct_resource()
        assert resource.instance_url() == \
            '/v1/bitcoin/receivers/%s' % TEST_RESOURCE_ID

    def test_is_listable(self, request_mock):
        resources = stripe.BitcoinReceiver.list()
        request_mock.assert_requested(
            'get',
            '/v1/bitcoin/receivers'
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.BitcoinReceiver)

    def test_is_retrievable(self, request_mock):
        resource = stripe.BitcoinReceiver.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            'get',
            '/v1/bitcoin/receivers/%s' % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.BitcoinReceiver)

    # stripe-mock does not handle most write operations anymore so we stub
    # each one instead. This endpoint/resource is mostly deprecated today.
    # The previous tests already ensure that the request will be routed to the
    # correct URL, so we also only test the API operations once.

    def test_is_creatable(self, request_mock):
        request_mock.stub_request(
            'post',
            '/v1/bitcoin/receivers',
            {
                'id': '%s' % TEST_RESOURCE_ID,
                'object': 'bitcoin_receiver'
            }
        )
        resource = stripe.BitcoinReceiver.create()
        request_mock.assert_requested(
            'post',
            '/v1/bitcoin/receivers'
        )
        assert isinstance(resource, stripe.BitcoinReceiver)

    def test_is_saveable(self, request_mock):
        request_mock.stub_request(
            'post',
            '/v1/bitcoin/receivers/%s' % TEST_RESOURCE_ID
        )
        resource = self.construct_resource()
        resource.metadata['key'] = 'value'
        resource.save()
        request_mock.assert_requested(
            'post',
            '/v1/bitcoin/receivers/%s' % TEST_RESOURCE_ID
        )

    def test_is_modifiable(self, request_mock):
        request_mock.stub_request(
            'post',
            '/v1/bitcoin/receivers/%s' % TEST_RESOURCE_ID
        )
        stripe.BitcoinReceiver.modify(
            TEST_RESOURCE_ID,
            metadata={'key': 'value'}
        )
        request_mock.assert_requested(
            'post',
            '/v1/bitcoin/receivers/%s' % TEST_RESOURCE_ID
        )

    def test_is_deletable(self, request_mock):
        request_mock.stub_request(
            'delete',
            '/v1/bitcoin/receivers/%s' % TEST_RESOURCE_ID
        )
        resource = self.construct_resource()
        resource.delete()
        request_mock.assert_requested(
            'delete',
            '/v1/bitcoin/receivers/%s' % TEST_RESOURCE_ID
        )
