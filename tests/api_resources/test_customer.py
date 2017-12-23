from __future__ import absolute_import, division, print_function

import warnings

import stripe


TEST_RESOURCE_ID = 'cus_123'
TEST_SUB_ID = 'sub_123'
TEST_SOURCE_ID = 'ba_123'


class TestCustomer(object):
    def test_is_listable(self, request_mock):
        resources = stripe.Customer.list()
        request_mock.assert_requested(
            'get',
            '/v1/customers'
        )
        assert isinstance(resources.data, list)
        assert isinstance(resources.data[0], stripe.Customer)

    def test_is_retrievable(self, request_mock):
        resource = stripe.Customer.retrieve(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            'get',
            '/v1/customers/%s' % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Customer)

    def test_is_creatable(self, request_mock):
        resource = stripe.Customer.create()
        request_mock.assert_requested(
            'post',
            '/v1/customers'
        )
        assert isinstance(resource, stripe.Customer)

    def test_is_saveable(self, request_mock):
        resource = stripe.Customer.retrieve(TEST_RESOURCE_ID)
        resource.metadata['key'] = 'value'
        resource.save()
        request_mock.assert_requested(
            'post',
            '/v1/customers/%s' % resource.id
        )

    def test_is_modifiable(self, request_mock):
        resource = stripe.Customer.modify(
            TEST_RESOURCE_ID,
            metadata={'key': 'value'}
        )
        request_mock.assert_requested(
            'post',
            '/v1/customers/%s' % TEST_RESOURCE_ID
        )
        assert isinstance(resource, stripe.Customer)

    def test_is_deletable(self, request_mock):
        resource = stripe.Customer.retrieve(TEST_RESOURCE_ID)
        resource.delete()
        request_mock.assert_requested(
            'delete',
            '/v1/customers/%s' % resource.id
        )
        assert isinstance(resource, stripe.Customer)

    def test_can_add_invoice_item(self, request_mock):
        resource = stripe.Customer.retrieve(TEST_RESOURCE_ID)
        resource.add_invoice_item(
            amount=100,
            currency='usd'
        )
        request_mock.assert_requested(
            'post',
            '/v1/invoiceitems',
            {
                'amount': 100,
                'currency': 'usd',
                'customer': '%s' % resource.id
            }
        )

    def test_can_invoices(self, request_mock):
        resource = stripe.Customer.retrieve(TEST_RESOURCE_ID)
        resource.invoices()
        request_mock.assert_requested(
            'get',
            '/v1/invoices',
            {
                'customer': '%s' % resource.id
            }
        )

    def test_can_invoice_items(self, request_mock):
        resource = stripe.Customer.retrieve(TEST_RESOURCE_ID)
        resource.invoice_items()
        request_mock.assert_requested(
            'get',
            '/v1/invoiceitems',
            {
                'customer': '%s' % resource.id
            }
        )

    def test_can_list_charges(self, request_mock):
        resource = stripe.Customer.retrieve(TEST_RESOURCE_ID)
        resource.charges()
        request_mock.assert_requested(
            'get',
            '/v1/charges',
            {
                'customer': '%s' % resource.id
            }
        )

    def test_can_delete_discount(self, request_mock):
        resource = stripe.Customer.retrieve(TEST_RESOURCE_ID)
        resource.delete_discount()
        request_mock.assert_requested(
            'delete',
            '/v1/customers/%s/discount' % resource.id
        )


# stripe-mock does not handle the legacy subscription endpoint so we stub
class TestCustomerLegacySubscription(object):
    def construct_resource(self):
        res_dict = {
            'id': TEST_RESOURCE_ID,
            'object': 'customer',
            'metadata': {},
        }
        return stripe.Customer.construct_from(res_dict, stripe.api_key)

    def test_can_update_legacy_subscription(self, request_mock):
        request_mock.stub_request(
            'post',
            '/v1/customers/%s/subscription' % TEST_RESOURCE_ID,
        )
        resource = self.construct_resource()
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            resource.update_subscription(plan='plan')
        request_mock.assert_requested(
            'post',
            '/v1/customers/%s/subscription' % TEST_RESOURCE_ID
        )

    def test_can_delete_legacy_subscription(self, request_mock):
        request_mock.stub_request(
            'delete',
            '/v1/customers/%s/subscription' % TEST_RESOURCE_ID
        )
        resource = self.construct_resource()
        with warnings.catch_warnings():
            warnings.simplefilter('ignore')
            resource.cancel_subscription()
        request_mock.assert_requested(
            'delete',
            '/v1/customers/%s/subscription' % TEST_RESOURCE_ID
        )


class TestCustomerSources(object):
    def test_is_creatable(self, request_mock):
        stripe.Customer.create_source(
            TEST_RESOURCE_ID,
            source='btok_123'
        )
        request_mock.assert_requested(
            'post',
            '/v1/customers/%s/sources' % TEST_RESOURCE_ID
        )

    def test_is_retrievable(self, request_mock):
        stripe.Customer.retrieve_source(
            TEST_RESOURCE_ID,
            TEST_SOURCE_ID
        )
        request_mock.assert_requested(
            'get',
            '/v1/customers/%s/sources/%s' % (TEST_RESOURCE_ID,
                                             TEST_SOURCE_ID)
        )

    def test_is_modifiable(self, request_mock):
        stripe.Customer.modify_source(
            TEST_RESOURCE_ID,
            TEST_SOURCE_ID,
            metadata={'foo': 'bar'}
        )
        request_mock.assert_requested(
            'post',
            '/v1/customers/%s/sources/%s' % (TEST_RESOURCE_ID,
                                             TEST_SOURCE_ID)
        )

    def test_is_deletable(self, request_mock):
        stripe.Customer.delete_source(
            TEST_RESOURCE_ID,
            TEST_SOURCE_ID
        )
        request_mock.assert_requested(
            'delete',
            '/v1/customers/%s/sources/%s' % (TEST_RESOURCE_ID,
                                             TEST_SOURCE_ID)
        )

    def test_is_listable(self, request_mock):
        resources = stripe.Customer.list_sources(TEST_RESOURCE_ID)
        request_mock.assert_requested(
            'get',
            '/v1/customers/%s/sources' % TEST_RESOURCE_ID
        )
        assert isinstance(resources.data, list)
