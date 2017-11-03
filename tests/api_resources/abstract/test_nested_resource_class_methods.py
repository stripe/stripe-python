from __future__ import absolute_import, division, print_function

import stripe
from tests.helper import StripeTestCase


class NestedResourceClassMethodsTests(StripeTestCase):
    @stripe.api_resources.abstract.nested_resource_class_methods(
        'nested',
        operations=['create', 'retrieve', 'update', 'delete', 'list']
    )
    class MainResource(stripe.api_resources.abstract.APIResource):
        pass

    def test_create_nested(self):
        self.stub_request(
            'post',
            '/v1/mainresources/id/nesteds',
            {
                'id': 'nested_id',
                'object': 'nested',
                'foo': 'bar',
            }
        )
        nested_resource = self.MainResource.create_nested('id', foo='bar')
        self.assert_requested(
            'post',
            '/v1/mainresources/id/nesteds',
            {
                'foo': 'bar'
            },
            None
        )
        self.assertEqual('bar', nested_resource.foo)

    def test_retrieve_nested(self):
        self.stub_request(
            'get',
            '/v1/mainresources/id/nesteds/nested_id',
            {
                'id': 'nested_id',
                'object': 'nested',
                'foo': 'bar',
            }
        )
        nested_resource = self.MainResource.retrieve_nested('id', 'nested_id')
        self.assert_requested(
            'get',
            '/v1/mainresources/id/nesteds/nested_id',
            {},
            None
        )
        self.assertEqual('bar', nested_resource.foo)

    def test_modify_nested(self):
        self.stub_request(
            'post',
            '/v1/mainresources/id/nesteds/nested_id',
            {
                'id': 'nested_id',
                'object': 'nested',
                'foo': 'baz',
            }
        )
        nested_resource = self.MainResource.modify_nested('id', 'nested_id',
                                                          foo='baz')
        self.assert_requested(
            'post',
            '/v1/mainresources/id/nesteds/nested_id',
            {
                'foo': 'baz'
            },
            None
        )
        self.assertEqual('baz', nested_resource.foo)

    def test_delete_nested(self):
        self.stub_request(
            'delete',
            '/v1/mainresources/id/nesteds/nested_id',
            {
                'id': 'nested_id',
                'object': 'nested',
                'deleted': True,
            }
        )
        nested_resource = self.MainResource.delete_nested('id', 'nested_id')
        self.assert_requested(
            'delete',
            '/v1/mainresources/id/nesteds/nested_id',
            {},
            None
        )
        self.assertEqual(True, nested_resource.deleted)

    def test_list_nesteds(self):
        self.stub_request(
            'get',
            '/v1/mainresources/id/nesteds',
            {
                'object': 'list',
                'data': [],
            }
        )
        nested_resource = self.MainResource.list_nesteds('id')
        self.assert_requested(
            'get',
            '/v1/mainresources/id/nesteds',
            {},
            None
        )
        self.assertTrue(isinstance(nested_resource.data, list))
